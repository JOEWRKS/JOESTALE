"""JOESTALE 기계 검증 (Phase 0).

사용: PYTHONIOENCODING=utf-8 python check_text.py <본문.txt | -> [--design 설계서.json] [--json]

검사: R1 정도부사, R2 수식어 비율(MAG+VA+XSA+MM, 화이트리스트 제외), R3 상태 서술 패턴,
      R4 감정 직설, R5 비시각 감각(문단당), R6 구체화(문단당), G1 조사 받침 규칙,
      G2 종결어미 연속 반복, G3 설계서 대장 대조.
Kiwi 오타 교정 모드는 쓰지 않는다. 띄어쓰기는 보고만 한다.
"""
import sys, re, json, argparse
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass
from kiwipiepy import Kiwi

DEGREE_ADV = {"매우","몹시","너무","정말","진짜","아주","굉장히","엄청","완전","늘","항상","무척","대단히","상당히","꽤","참","되게","심히","극히","한없이"}
EMOTION = {"슬프","기쁘","불안","답답","외롭","두렵","행복","화나","짜증","설레","우울","괴롭","서럽","꼼꼼","예민","착하","성실","게으르","소심","위축"}
STATE_PAT = re.compile(r"(한|던|은|는) (성격|사람|분위기|느낌)이었다|해 보였다|처럼 보였다")
ALLOW_ADV = {"꾹","나란히","비로소","천천히","가만히","살짝","문득","겨우","다시","이미","아직","막","곧","함께","따로","홀로","소리없이"}
NONVISUAL = {"소리","쇳소리","냄새","향","베","찌르","차갑","뜨겁","미지근","축축","끈적","거칠","매끄럽","딱딱","말랑","쓰","달","짜","시큼","비릿","살얼음","바람이","긁","울리","속삭","두드리","떨리","식","데","얼",
             "손끝","손톱","손바닥","쓸어","눌러","누르","만지","쥐","비비","문지르","더듬","저리","굳어","시리","따끔","간지럽","까끌","미끈","축축","눅눅","후끈","서늘","훈기","한기"}
JOSA = {"이":1,"가":0,"을":1,"를":0,"은":1,"는":0,"과":1,"와":0,"이랑":1,"랑":0,"으로":1,"로":0,"아":1,"야":0}
JOSA_PAT = re.compile(r"([가-힣]+?)(이랑|으로|이|가|을|를|은|는|과|와|랑|로|아|야)(?=[\s.,!?'\"”’]|$)")

kiwi = Kiwi()

def batchim(ch):
    c = ord(ch)
    return None if not (0xAC00 <= c <= 0xD7A3) else (c - 0xAC00) % 28

def split_sents(text):
    return [s.text for s in kiwi.split_into_sents(text)]

def modifier_stats(text):
    toks = kiwi.tokenize(text)
    content = mods = 0
    mod_forms, nouns, verbs = [], 0, 0
    for t in toks:
        tag = t.tag
        if tag.startswith("NN") or tag in ("NP","NR","SN","NNB"):
            content += 1
            if tag.startswith("NN"): nouns += 1
        elif tag.startswith("VV"):
            content += 1; verbs += 1
        elif tag == "MAG":
            content += 1
            if t.form not in ALLOW_ADV:
                mods += 1; mod_forms.append(t.form)
        elif tag.startswith("VA") or tag == "XSA":
            content += 1; mods += 1; mod_forms.append(t.form)
        elif tag == "MM":
            content += 1
            if not re.fullmatch(r"[한두세네다섯여섯일곱여덟아홉열]|몇|맨|첫|온", t.form):
                mods += 1; mod_forms.append(t.form)
    return {"content": content, "modifiers": mods, "ratio": round(mods/max(content,1),2), "forms": mod_forms, "nouns": nouns, "verbs": verbs}

def josa_errors(text):
    out = []
    for m in JOSA_PAT.finditer(text):
        stem, j = m.group(1), m.group(2)
        b = batchim(stem[-1])
        if b is None: continue
        has = 1 if b else 0
        want = JOSA[j]
        if j == "로" and b == 8: has = 0      # ㄹ받침 + 로 는 정상
        if j == "으로" and b == 8: has = 0    # ㄹ받침 + 으로 는 오류
        if want != has:
            toks = kiwi.tokenize(stem)
            if toks and (toks[-1].tag[0] in "NX" or toks[-1].tag in ("SL","SN","NP","NNB","NR")):
                out.append({"stem": stem, "josa": j})
    return out

def ending_repeat(sents, limit=3):
    """연속 문장의 마지막 어절(서술어 전체)이 같은 횟수. '~다'로 끝나는 것 자체는 한국어 서술문의 기본이라 세지 않는다."""
    ends = []
    for s in sents:
        words = re.findall(r"[가-힣]+", s)
        ends.append(words[-1] if words else "")
    run, best, bf = 1, 1, ""
    for i in range(1, len(ends)):
        if ends[i] and ends[i] == ends[i-1]:
            run += 1
            if run > best: best, bf = run, ends[i]
        else:
            run = 1
    return {"max_run": best, "form": bf, "violation": best >= limit}

def check(text, design=None):
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    sents = split_sents(text)
    report = {"sentences": len(sents), "paragraphs": len(paras), "violations": []}
    V = report["violations"]
    # R1, R3, R4, G1 per sentence
    for s in sents:
        toks = kiwi.tokenize(s)
        for t in toks:
            if t.tag == "MAG" and t.form in DEGREE_ADV:
                V.append({"rule":"R1","sentence":s,"form":t.form})
            if (t.tag.startswith("VA") or t.tag == "XR" or t.tag.startswith("NN")) and any(t.form.startswith(e) for e in EMOTION):
                V.append({"rule":"R4","sentence":s,"form":t.form})
        if STATE_PAT.search(s):
            V.append({"rule":"R3","sentence":s})
        for e in josa_errors(s):
            V.append({"rule":"G1","sentence":s, **e})
    # R2 overall + per sentence over 0.5
    ms = modifier_stats(text)
    report["modifier"] = ms
    if ms["ratio"] > 0.18:
        V.append({"rule":"R2","ratio":ms["ratio"],"forms":ms["forms"]})
    # R5, R6 per paragraph
    for i, p in enumerate(paras):
        if not any(k in p for k in NONVISUAL):
            V.append({"rule":"R5","paragraph":i+1})
        toks = kiwi.tokenize(p)
        if not any(t.tag in ("NR","SN","NNP") or re.fullmatch(r"[한두세네다섯여섯일곱여덟아홉열]", t.form) for t in toks):
            V.append({"rule":"R6","paragraph":i+1})
    # G2
    er = ending_repeat(sents)
    report["ending"] = er
    if er["violation"]:
        V.append({"rule":"G2","form":er["form"],"run":er["max_run"]})
    # G3 ledger
    if design and "ledger" in design:
        for kind, items in design["ledger"].items():
            for it in items:
                if it and it not in text:
                    V.append({"rule":"G3","kind":kind,"missing":it})
    # spacing (report only)
    spaced = kiwi.space(text)
    report["spacing_suggestion_differs"] = spaced.replace(" ","") == text.replace(" ","") and spaced != text
    report["pass"] = len(V) == 0
    return report

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--design")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    text = sys.stdin.read() if a.path == "-" else open(a.path, encoding="utf-8").read()
    design = json.load(open(a.design, encoding="utf-8")) if a.design else None
    r = check(text, design)
    if a.json:
        print(json.dumps(r, ensure_ascii=False, indent=1))
    else:
        print(f"문장 {r['sentences']} / 문단 {r['paragraphs']} / 수식어 비율 {r['modifier']['ratio']} ({r['modifier']['forms']}) / 명사 {r['modifier']['nouns']} 동사 {r['modifier']['verbs']}")
        print("PASS" if r["pass"] else "위반:")
        for v in r["violations"]:
            print(" ", json.dumps(v, ensure_ascii=False))
    sys.exit(0 if r["pass"] else 1)

if __name__ == "__main__":
    main()
