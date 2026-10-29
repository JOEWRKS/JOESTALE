"""JOESTALE 기계 검증.

사용: PYTHONIOENCODING=utf-8 python check_text.py <본문.txt | -> [--design 설계서.json] [--json]
      python check_text.py --lexicon-stats

규칙(임계값은 references/decisions.md D3):
  R1 정도부사 0회 · R2 수식어 비율 ≤0.18(문장 ≥0.50도 위반) · R3 상태 서술 패턴 · R4 감정 직설(대화문 제외)
  R5 문단당 비시각 감각 ≥1 · R6 문단당 숫자·고유명사 ≥1 · G1 조사 받침 규칙 · G2 마지막 어절 3연속 반복
  G3 설계서 대장(누락·미등록 고유명사) · T1 번역투·AI 관용구 상한 · T2 문단 첫 어절 3연속 반복 · X1 작가 예문 복제
목록은 references/lexicon.json. Kiwi 오타 교정은 쓰지 않는다. 띄어쓰기는 보고만.
"""
import sys, re, json, argparse, pathlib

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

LEX_PATH = pathlib.Path(__file__).resolve().parent.parent / "references" / "lexicon.json"
LEX = json.loads(LEX_PATH.read_text(encoding="utf-8"))
DEGREE = set(LEX["degree_adverbs"])
ALLOW_ADV = set(LEX["allowed_adverbs"])
NUMDET = re.compile(LEX["numeral_determiner_regex"])
EMOTION = LEX["emotion_stems"]
STATE_PATS = [re.compile(p) for p in LEX["state_patterns"]]
TRANS = [(re.compile(t["pattern"]), t["label"], t["max"]) for t in LEX["translationese"]]
AUTHOR_PHRASES = LEX["author_example_phrases"]
SENSES = LEX["senses"]
ALL_SENSE = [(k, w) for k, ws in SENSES.items() for w in ws]
JOSA = {"이":1,"가":0,"을":1,"를":0,"은":1,"는":0,"과":1,"와":0,"이랑":1,"랑":0,"으로":1,"로":0,"아":1,"야":0}
JOSA_PAT = re.compile(r"([가-힣]+?)(이랑|으로|이|가|을|를|은|는|과|와|랑|로|아|야)(?=[\s.,!?'\"”’]|$)")
QUOTE_PAT = re.compile(r"[\"“][^\"”]*[\"”]|'[^']*'")
R2_TEXT, R2_SENT, G2_RUN, T2_RUN = 0.18, 0.50, 3, 3

_kiwi = None
def kiwi():
    global _kiwi
    if _kiwi is None:
        from kiwipiepy import Kiwi
        _kiwi = Kiwi()
    return _kiwi

def batchim(ch):
    c = ord(ch)
    return None if not (0xAC00 <= c <= 0xD7A3) else (c - 0xAC00) % 28

def split_sents(text):
    return [s.text for s in kiwi().split_into_sents(text)]

def strip_quotes(s):
    return QUOTE_PAT.sub(" ", s)

def modifier_stats(text):
    content = mods = nouns = verbs = 0
    forms = []
    for t in kiwi().tokenize(text):
        tag = t.tag
        if tag.startswith("NN") or tag in ("NP", "NR", "SN", "NNB"):
            content += 1
            if tag.startswith("NN"): nouns += 1
        elif tag.startswith("VV"):
            content += 1; verbs += 1
        elif tag == "MAG":
            content += 1
            if t.form not in ALLOW_ADV:
                mods += 1; forms.append(t.form)
        elif tag.startswith("VA") or tag == "XSA":
            content += 1; mods += 1; forms.append(t.form)
        elif tag == "MM":
            content += 1
            if not NUMDET.match(t.form):
                mods += 1; forms.append(t.form)
    return {"content": content, "modifiers": mods, "ratio": round(mods / max(content, 1), 2), "forms": forms, "nouns": nouns, "verbs": verbs}

def josa_errors(text):
    """받침 규칙 위반 조사. 어절을 Kiwi로 분석해 어미(E*)·용언(V*)·파생접사(XS*)가 있으면 조사가 아니므로 제외(I-5)."""
    out = []
    for m in JOSA_PAT.finditer(text):
        stem, j = m.group(1), m.group(2)
        b = batchim(stem[-1])
        if b is None: continue
        has, want = (1 if b else 0), JOSA[j]
        if j in ("로", "으로") and b == 8: has = 0   # ㄹ받침: 로 정상, 으로 오류
        if want != has:
            ej = kiwi().tokenize(stem + j)
            if any(t.tag.startswith(("E", "V", "XSV", "XSA")) for t in ej):   # XSM("손톱로"의 '로')은 제외하지 않음
                continue
            toks = kiwi().tokenize(stem)
            if toks and (toks[-1].tag[0] in "NX" or toks[-1].tag in ("SL", "SN", "NP", "NNB", "NR")):
                out.append({"stem": stem, "josa": j})
    return out

def number_expressions(text):
    """본문의 수량 표현: 수사(NR)·숫자(SN)·수관형사 + 뒤따르는 단위/명사 1개 (I-6)."""
    toks = kiwi().tokenize(text)
    out = []
    ONE = {"한", "하나", "첫", "한번"}   # 수량 1은 대장 대상이 아님(한 번, 하나, 한 그릇)
    for i, t in enumerate(toks):
        is_num = t.tag in ("NR", "SN") or (t.tag == "MM" and NUMDET.match(t.form) and t.form not in ("이", "그", "저", "어느", "무슨", "맨", "온", "반", "몇"))
        if not is_num or t.form in ONE: continue
        end = t.start + t.len
        if i + 1 < len(toks) and toks[i + 1].tag in ("NNB", "NNG", "NR", "SN") and toks[i + 1].start - end <= 1:
            end = toks[i + 1].start + toks[i + 1].len
        out.append(text[t.start:end])
    return out

def run_length(items, limit):
    run, best, bf = 1, 1, ""
    for i in range(1, len(items)):
        if items[i] and items[i] == items[i - 1]:
            run += 1
            if run > best: best, bf = run, items[i]
        else:
            run = 1
    return {"max_run": best, "form": bf, "violation": best >= limit}

def ending_repeat(sents, limit=G2_RUN):
    ends = [(re.findall(r"[가-힣]+", s) or [""])[-1] for s in sents]
    return run_length(ends, limit)

def para_first_repeat(paras, limit=T2_RUN):
    firsts = [(re.findall(r"[가-힣]+", p) or [""])[0] for p in paras]
    return run_length(firsts, limit)

def senses_in(text):
    return sorted({k for k, w in ALL_SENSE if w in text})

def check(text, design=None):
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    sents = split_sents(text)
    V = []
    for s in sents:
        plain = strip_quotes(s)
        toks = kiwi().tokenize(plain)
        for t in toks:
            if t.tag == "MAG" and t.form in DEGREE:
                V.append({"rule": "R1", "sentence": s, "form": t.form})
            if t.tag in ("VA", "VA-I", "VA-R", "XR", "NNG") and any(t.form.startswith(e) for e in EMOTION):
                V.append({"rule": "R4", "sentence": s, "form": t.form})
        if any(p.search(plain) for p in STATE_PATS):
            V.append({"rule": "R3", "sentence": s})
        for e in josa_errors(s):
            V.append({"rule": "G1", "sentence": s, **e})
        ms = modifier_stats(plain)
        if ms["content"] >= 4 and ms["ratio"] >= R2_SENT:
            V.append({"rule": "R2", "sentence": s, "ratio": ms["ratio"], "forms": ms["forms"]})
    ms = modifier_stats(text)
    if ms["ratio"] > R2_TEXT:
        V.append({"rule": "R2", "scope": "text", "ratio": ms["ratio"], "forms": ms["forms"]})
    for i, p in enumerate(paras, 1):
        if not senses_in(p):
            V.append({"rule": "R5", "paragraph": i})
        toks = kiwi().tokenize(p)
        has_number = any(t.tag in ("NR", "SN", "NNP") or (t.tag == "MM" and NUMDET.match(t.form)) for t in toks)
        nng = sum(1 for t in toks if t.tag == "NNG")
        if not has_number and nng < 3:
            V.append({"rule": "R6", "paragraph": i, "nouns": nng})
    er = ending_repeat(sents)
    if er["violation"]: V.append({"rule": "G2", **er})
    pr = para_first_repeat(paras)
    if pr["violation"]: V.append({"rule": "T2", **pr})
    trans = {}
    for pat, label, mx in TRANS:
        n = len(pat.findall(text))
        if n: trans[label] = n
        if n > mx: V.append({"rule": "T1", "label": label, "count": n, "max": mx})
    for ph in AUTHOR_PHRASES:
        if ph in text: V.append({"rule": "X1", "phrase": ph})
    if design and "ledger" in design:
        for kind, items in design["ledger"].items():
            for it in items:
                if it and it not in text:
                    V.append({"rule": "G3", "kind": kind, "missing": it})
        known = set(design["ledger"].get("persons", [])) | set(design["ledger"].get("places", []))
        counts = {}
        for t in kiwi().tokenize(text):
            if t.tag == "NNP": counts[t.form] = counts.get(t.form, 0) + 1
        for form, n in counts.items():
            # 의성어·의태어 오태깅 방지(I-5): 2회 이상 나오고 2글자 이상이며 허용 부사·감각 목록에 없는 것만
            if form in known or any(form in k for k in known): continue
            if n < 2 or len(form) < 2 or form in ALLOW_ADV or any(form == w for _, w in ALL_SENSE): continue
            V.append({"rule": "G3", "kind": "unregistered_NNP", "form": form, "count": n})
        ledger_nums = design["ledger"].get("numbers", [])
        for expr in sorted(set(number_expressions(text))):
            if not any(expr in ln or ln in expr for ln in ledger_nums):
                V.append({"rule": "G3", "kind": "number_not_in_ledger", "form": expr})
    spaced = kiwi().space(text)
    return {
        "sentences": len(sents), "paragraphs": len(paras), "chars": len(text),
        "modifier": ms, "senses": senses_in(text), "ending": er, "para_first": pr,
        "translationese_counts": trans,
        "spacing_differs": spaced != text,
        "violations": V, "pass": not V,
    }

def summary_line(r):
    return (f"문장 {r['sentences']} / 문단 {r['paragraphs']} / {r['chars']}자 / 수식어 비율 {r['modifier']['ratio']} {r['modifier']['forms']} "
            f"/ 명사 {r['modifier']['nouns']} 동사 {r['modifier']['verbs']} / 감각 {r['senses']} / 번역투 {r['translationese_counts']}")

def lexicon_stats():
    return {"degree_adverbs": len(DEGREE), "allowed_adverbs": len(ALLOW_ADV), "emotion_stems": len(EMOTION),
            "state_patterns": len(STATE_PATS), "translationese": len(TRANS),
            "senses": {k: len(v) for k, v in SENSES.items()}, "senses_min": min(len(v) for v in SENSES.values())}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path", nargs="?")
    ap.add_argument("--design")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--lexicon-stats", action="store_true")
    a = ap.parse_args()
    if a.lexicon_stats:
        print(json.dumps(lexicon_stats(), ensure_ascii=False, indent=1)); return
    if not a.path:
        ap.error("본문 경로 또는 - 필요")
    text = sys.stdin.read() if a.path == "-" else open(a.path, encoding="utf-8").read()
    design = json.load(open(a.design, encoding="utf-8")) if a.design else None
    r = check(text, design)
    if a.json:
        print(json.dumps(r, ensure_ascii=False, indent=1))
    else:
        print(summary_line(r))
        print("PASS" if r["pass"] else "위반:")
        for v in r["violations"]:
            print(" ", json.dumps(v, ensure_ascii=False))
    sys.exit(0 if r["pass"] else 1)

if __name__ == "__main__":
    main()
