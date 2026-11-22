"""JOESTALE 기계 검증.

사용: PYTHONIOENCODING=utf-8 python check_text.py <본문.txt | -> [--design 설계서.json] [--json]
      python check_text.py --lexicon-stats

규칙(임계값은 references/decisions.md D3):
  R1 정도부사 0회 · R2 수식어 비율 ≤0.18(문장 ≥0.50도 위반) · R3 상태 서술 패턴 · R4 감정 직설(대화문 제외)
  R5 글 전체 비시각 감각 ≥1(문단별 부재는 W3 note) · R6 문단당 숫자·고유명사 ≥1 · R7 사고 동사 · R8 문단 첫 문장 상태 요약
  G1 조사 받침 규칙 · G2 마지막 어절 3연속 반복 · G4 한 명사 앞 수식어 2개 이상 · W4 상투 beat note · W5 서술문 5개 연속 note
  G3 설계서 대장(누락·미등록 고유명사) · T1 번역투·AI 관용구 상한 · T2 문단 첫 어절 3연속 반복 · X1 작가 예문 복제
  G5 앞 장 문장 재사용(--prev) · R9 문장 밀도(서술문 평균 내용어 ≤7.9, 절 ≤2.3, 절 3개 이상 문장 ≤35%; 1~10장 보정, T-051)
  G8 인물표 근거(characters[].evidence가 --prev 본문에 없으면 위반) · X2 금지 표현(banned_phrases) 위반 · X3 판독·검수 예시 복사(user_examples 8자 이상 겹침) note · W13 동음이의 후보 note
  W10 밀도 하한 note · W11 주어 없이 끊긴 짧은 문장 note · inference(시점 인물의 짐작)는 R3·R4·R7·R8 면제
  W14 문단 3문장·140자 초과 note · W15 대사 종결 단조(EF 비율 ≥0.9) note · W16 대사 3연속에 발화자 표지 없음 note · W17 남의 말·사건 3연속에 pov 반응 없음 note · W18 자리만 알리는 문장 note · W19 모름의 보고문 note (T-057)
  W20 서술 문단 박자(20개 이상에서 1문장 문단 < 50% 또는 3문장 이상 > 10%) note · W21 마지막 문단 2문장 이상·70자 초과 note · 박자 문단(1문장·20자 이하)은 R6 면제 (T-058)
  W22 토막 대사(완결 종결 아닌 줄 > 35% 또는 셋 연속) note · W23 생각의 명사화("~인지가/생각이 돌아왔다") note · W24 독백(정당화·-다 셋 연속) note · W25 대비 꼴 셈("A가 아니라 B였다") note · G9 premises[].shown_in 본문 부재 위반 · R4 조연 표정 어절 면제 (T-063)
  W26 되받기 쌍 둘 이상 note · W27 '그렇-' 사실 답 둘 이상 note · W28 대사 끝 연결어미 셋 이상 note · W29 대사 안 대칭("많이 주면 많이") note · W30 대사 안 인칭 지칭(성 하나·그/그녀·당신) note(패턴 94, T-075) · W31 대사의 호칭이 그 장 안에서 사람과 안 묶임 note(시점 인물을 부르는 호칭은 면제, T-080) · W32 앞 장 전제 넷 이상 note · W33 앞 일 요약문 셋 이상 note(패턴 95, T-078) · W34 서술이 시점 인물을 풀네임+계급으로 부름 note · W35 대사 안 명사+안/못 조사 떼기 note(패턴 97, T-080) · W36 사다리 물음(앞뒤가 다른 사람의 대사인 짧은 '가서요/그래서요' 꼴) note · W37 대사 풀이 어미('-는 겁니다/-는 거예요') 셋 이상 note · W38 대사 안 '명사+일' 포괄 지칭 note(패턴 97 ④·98, T-082) · G10 설계서 dialogue_plan 요지 그대로 옮김 note · W24에 "거니까" (T-064)
  L1 반영 뒤 분량(--draft: 초고 ×1.05를 넘고 밀도도 오르면 위반. 이야기가 늘어 길어진 것은 통과) · W8 내용어 13개 이상 문장 note · W9 대사 안 서술체 종결(-ㄴ다·-는다) note
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
THOUGHT = LEX.get("thought_verbs", {})
THOUGHT_NOUN = set(THOUGHT.get("noun_xsv", []))
THOUGHT_VERB = set(THOUGHT.get("verb", []))
THOUGHT_AUX = set(THOUGHT.get("aux", []))
WEAK_BEATS = [re.compile(p) for p in LEX.get("weak_beats", {}).get("patterns", [])]
G4_MM_IGNORE = set(LEX.get("g4_mm_ignore", []))
EMOTION_NOUN_HOMOGRAPHS = set(LEX.get("emotion_noun_homographs", []))  # I-24: 감정어 어간과 같은 꼴의 명사(그립=손잡이)
ADJ_TAGS = ("VA", "VA-I", "VA-R", "XSA", "XSA-I", "XSA-R")


def thought_verbs(toks):
    """R7 사고 동사(패턴 23): 생각하다·깨닫다·느끼다·싶다 같은 사고·욕망 동사가 서술문에 있으면 그 형태를 돌려준다."""
    out = []
    for i, t in enumerate(toks):
        if t.tag == "NNG" and t.form in THOUGHT_NOUN and i + 1 < len(toks) and toks[i + 1].tag.startswith("XSV"):
            out.append(t.form + "하다")
        elif t.tag.startswith("VV") and t.form in THOUGHT_VERB:
            out.append(t.form + "다")
        elif t.tag == "VX" and t.form in THOUGHT_AUX:
            out.append(t.form + "다")
    return out


def first_sentence_state(toks):
    """R8 문단 첫 문장의 상태 요약(패턴 24): 서술어가 상태 형용사(VA·XSA)로 끝나면 그 형태를 돌려준다. 있다·없다는 제외."""
    pred, prev = None, None
    for i, t in enumerate(toks):
        if t.tag.startswith(("VA", "VV", "VX", "XSA", "XSV", "VCP", "VCN")):
            pred, prev = t, (toks[i - 1] if i else None)
    if pred is not None and pred.tag.startswith(ADJ_TAGS) and pred.form not in ("있", "없"):
        return (prev.form if prev is not None and prev.tag == "XR" else "") + pred.form
    return None


def stacked_modifiers(toks):
    """G4 수식어 간격(패턴 26): 한 명사 앞에 상태 관형어(VA/XSA+ETM, '~고' 연결 포함)나 관형사가 2개 이상 쌓이면 돌려준다."""
    out = []
    for i, t in enumerate(toks):
        if t.tag not in ("NNG", "NNP"):
            continue
        j, n, forms = i - 1, 0, []
        while j >= 0:
            tg, fm = toks[j].tag, toks[j].form
            if tg in ("ETM", "EC") and (tg == "ETM" or fm == "고") and j >= 1 and toks[j - 1].tag.startswith(ADJ_TAGS) and toks[j - 1].form not in ("있", "없"):
                f = toks[j - 1].form; j -= 2
                if j >= 0 and toks[j].tag == "XR":
                    f = toks[j].form + f; j -= 1
                n += 1; forms.append(f)
            elif tg == "MM" and not NUMDET.match(fm) and fm not in G4_MM_IGNORE:
                n += 1; forms.append(fm); j -= 1
            else:
                break
        if n >= 2:
            out.append({"noun": t.form, "modifiers": forms[::-1]})
    return out
# 항목 "쓰/VA"는 형태 '쓰' + 태그가 VA로 시작할 때만(쓰다=bitter, VV 쓰다=write 구분). 태그 없는 항목은 (sense, word, None).
def _parse_sense(w):
    if "/" in w:
        f, tag = w.split("/", 1); return f, tag
    return w, None
ALL_SENSE = [(k, *_parse_sense(w)) for k, ws in SENSES.items() for w in ws]
JOSA = {"이":1,"가":0,"을":1,"를":0,"은":1,"는":0,"과":1,"와":0,"이랑":1,"랑":0,"으로":1,"로":0,"아":1,"야":0}
JOSA_PAT = re.compile(r"([가-힣]+?)(이랑|으로|이|가|을|를|은|는|과|와|랑|로|아|야)(?=[\s.,!?'\"”’]|$)")
QUOTE_PAT = re.compile(r"[\"“][^\"”]*[\"”]|'[^']*'")
R2_TEXT, R2_SENT, R2_PARA, G2_RUN, T2_RUN = 0.18, 0.50, 0.30, 3, 3   # R2_PARA = 고전 코퍼스 문단 p90 (corpus/MEASURE.md)

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
            if len(ej) == 1 and ej[0].tag.startswith("N"):   # "창가"처럼 어절 전체가 사전에 있는 한 단어
                continue
            if not any(t.start == len(stem) for t in ej):   # 어간/조사 경계에 토큰 경계가 없음: Kiwi가 다르게 끊어 읽은 한 단어("그사이" = 그+사이)
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

REUSE_TAGS = ("NNG", "VV", "VA", "XR", "MAG", "NR")
REUSE_STOP = {"하다", "되다", "있다", "없다", "말", "것", "수", "때", "그", "보다", "가다", "오다", "들다", "손", "눈", "앞", "뒤", "안", "위"}
DAY_WORDS = ("하루", "이틀", "사흘", "나흘", "닷새", "엿새", "이레", "여드레", "아흐레", "열흘", "보름")

def _lemmas(s):
    return {t.form for t in kiwi().tokenize(s) if t.tag in REUSE_TAGS and t.form not in REUSE_STOP}

def reused_sentences(sents, prev_text, min_shared=4, min_ratio=0.5, ok=()):
    """앞 장 문장의 재사용(T-050): 내용어 4개 이상이 앞 장의 한 문장과 겹치고 그것이 이 문장 내용어의 절반 이상."""
    prev = [(p, _lemmas(p)) for p in split_sents(prev_text)]
    prev = [(p, l) for p, l in prev if len(l) >= min_shared]
    out = []
    for s_ in sents:
        if any(o and o in s_ for o in ok): continue
        L = _lemmas(s_)
        if len(L) < min_shared: continue
        best, shared = None, set()
        for p, l in prev:
            sh = L & l
            if len(sh) > len(shared): best, shared = p, sh
        if len(shared) >= min_shared and len(shared) / len(L) >= min_ratio:
            out.append({"sentence": s_, "prev_sentence": best, "shared": sorted(shared)})
    return out

def repeated_numbers(sents, window=6):
    """같은 수치·날수가 가까운 문장에서 되풀이(T-050). note용."""
    where = {}
    for i, s_ in enumerate(sents):
        exprs = set(number_expressions(s_)) | {w for w in DAY_WORDS if w in s_}
        for e in exprs: where.setdefault(e, []).append(i)
    out = []
    for e, ix in where.items():
        if any(b - a <= window for a, b in zip(ix, ix[1:])):
            out.append((e, [sents[i] for i in ix]))
    return out

CONTENT_TAGS = ("NNG", "NNP", "NNB", "NP", "NR", "VV", "VA", "XR", "MAG", "MM", "SN")
DENS_CONTENT, DENS_CLAUSES, DENS_C3, DENS_LONG, DENS_MIN_N = 7.9, 2.3, 0.35, 13, 20   # T-051: 1~10장 서술문 5.8~7.8 / 1.79~2.29 / 0.18~0.34
DRAFT_RATIO = 1.05   # L1: 반영 뒤 글자 수 상한(초고 대비). T-053: 밀도가 같이 오를 때만 위반
L1_DCONTENT, L1_DCLAUSES = 0.3, 0.1   # L1: 초고보다 내용어·절 평균이 이만큼 넘게 오르면 덧붙이기로 본다
DENS_MIN_CONTENT, DENS_MIN_CLAUSES = 5.82, 1.79   # W10: 1~10장 하한. 밑돌면 잘게 끊긴 글(T-052 판독)
CHOP_MIN, INFER_MAX = 3, 4   # W11: 끊긴 쌍이 이만큼이면 note / inference 구절 상한
EXAMPLE_MIN = 8   # X3: 판독·검수 예시 문장과 이 글자 수 이상 겹치면 옮겨 적은 것
WATCH_WORDS = {   # W13 동음이의 후보(T-054 판독에서 자람): 구절 → 먼저 읽히는 뜻
    "양을 보": "짐승 양", "양을 세": "짐승 양", "불려 오": "늘려 오다", "불려 올": "늘려 오다", "불려다": "늘려다", "불려 놓": "늘려 놓다",
}
WRITTEN_EF = ("ᆫ다", "ㄴ다", "는다")   # ᆫ다(Kiwi 자모)·ㄴ다·는다
DIALOG_PAT = re.compile(r"[\"“]([^\"”]+)[\"”]")

def copied_examples(text, examples, n=EXAMPLE_MIN):
    """X3(패턴 58): 판독·검수의 예시 문장을 그대로 옮겼는지. 예시의 n글자 창이 본문에 있으면 돌려준다(공백 무시)."""
    flat = text.replace(" ", "")
    out = []
    for ex in examples:
        e = ex.replace(" ", "")
        hit = next((e[i:i + n] for i in range(0, max(1, len(e) - n + 1)) if e[i:i + n] in flat), None)
        if hit:
            out.append((ex, hit))
    return out

PARA_MAX_SENTS, PARA_MAX_CHARS = 3, 140   # W14 문단 호흡(패턴 70. T-058 카카오페이지 3작품 19화: 서술 문단 평균 45~56자, 3문장 이상 1~3%)
ONE_SENT_MIN, MULTI_MAX, RHYTHM_MIN_PARAS = 0.5, 0.10, 20   # W20 문단 박자(패턴 70·74. 표본: 1문장 서술 문단 86%, 3문장 이상 1~3%)
LAST_MAX_SENTS, LAST_MAX_CHARS = 1, 70   # W21 장의 끝(패턴 73): 마지막 문단은 한 문장
BEAT_MAX_CHARS = 20   # 박자 문단(한 낱말·한 짧은 문장, 패턴 74)은 R6 면제
DIALOG_EF_RATIO, DIALOG_MIN_N = 0.9, 10
POV_RUN = 4   # W17: 남의 말·사건이 이만큼 이어지는 동안 pov의 줄이 없으면 note(대사는 pov 것도 섞이므로 3은 과민)   # W15 대사 종결 단조(패턴 66)
STAY_PAT = re.compile(r'^[^,]{1,14}(은|는|이|가) [^,]{0,16}(에|위에|앞에|뒤에|옆에|밑에) (남았다|남아 있었다|서 있었다|있었다|앉아 있었다)[.]?$')   # W18 자리만 알리는 문장(패턴 69)
UNKNOWN_PAT = re.compile(r'(알지 못했다|알 수 없었다|몰랐다|모르고 있었다)')   # W19 모름의 보고문(패턴 69)
FRAG_MAX, FRAG_RUN = 0.35, 3   # W22 토막 대사(패턴 75): 명사·조사·부사로 끊긴 대사 줄 비율 상한, 연속 상한
FRAG_FILLERS = ('뭐', '뭘', '좀', '그냥', '아', '야', '응', '네', '예', '거', '요', '참')   # 군말·대답 한마디는 토막이 아니다
NOMINAL_PAT = re.compile(r'([가-힣]+인지가|(?:그 )?몇 [가-힣]{1,4}(?:이|가)|(?:그 )?(?:생각|물음|궁금함|궁금증|말|셈|질문)이) (?:자꾸 |다시 |또 )?(돌아왔다|떠올랐다|따라왔다|남았다|걸렸다|맴돌았다|머물렀다)')   # W23 생각의 명사화(패턴 78)
MONO_PAT = re.compile(r"'([^']{2,}?)'")   # W24 독백(패턴 79)
JUSTIFY_PAT = re.compile(r'(그래서|그러니까|때문에|셈은 맞다|맞는 셈이다|당연했다|당연하다|거니까)')   # '~라는 거니까'는 까닭 한 줄로 메운 해설(패턴 79, T-064)
ECHO_MAX, FACT_MAX, TAIL_MAX = 2, 2, 2   # T-066: 1은 "그렇대요"·"한 주 치래요" 같은 자연스러운 답까지 피하게 만들어 어색한 대사를 낳았다   # W26 되받기 쌍, W27 '그렇-' 답, W28 대사 끝 연결어미 장당 상한(패턴 86·87)
FACT_ANSWER_PAT = re.compile(r'^[…\s]*(그렇|그러|그래)')
SYMM_PAT = re.compile(r'(?<![가-힣])([가-힣]{2,}) [가-힣]+(?:면|니|고|야|서|도) \1(?![가-힣])')   # W29 대칭 수사(패턴 87)
GIST_MIN = 8   # G10 설계서 요지가 본문에 그대로 있다고 보는 최소 글자 수
CONTRAST_PAT = re.compile(r'(은|는) [^,.]{1,20}(이|가) 아니라 [^,.]{1,20}(였다|이었다)[.]?$')   # W25 대비 꼴 셈(패턴 82)
FACE_NOUNS = ('얼굴', '표정', '낯', '웃음', '눈', '입', '눈빛', '목소리')   # R4 조연 표정 어절 면제(패턴 83)

def is_quote_para(p):
    s = p.strip()
    return s[:1] in ('"', '“') and s[-1:] in ('"', '”')

def long_paras(paras, skip=()):
    """W14 문단 호흡: 대사·독백만인 문단은 빼고, 서술 문단이 3문장을 넘거나 140자를 넘으면 (번호, 문장 수, 글자 수)."""
    out = []
    for i, p in enumerate(paras, 1):
        if is_quote_para(p) or all(x in skip for x in split_sents(p)):
            continue
        n = len(split_sents(p)); c = len(p.replace(' ', ''))
        if n > PARA_MAX_SENTS or c > PARA_MAX_CHARS:
            out.append((i, n, c))
    return out

def rhythm_stats(paras, skip=()):
    """W20 문단 박자: 서술 문단(대사·독백만인 문단 제외) 가운데 1문장 문단 수와 3문장 이상 문단 수."""
    narr = [p for p in paras if not is_quote_para(p) and not all(x in skip for x in split_sents(p))]
    one = sum(1 for p in narr if len(split_sents(p)) == 1)
    multi = sum(1 for p in narr if len(split_sents(p)) >= 3)
    return {"narr": len(narr), "one": one, "multi": multi}

def dialogue_ending_stats(text):
    """W15 대사 종결: 대사 줄마다 마지막 형태소가 종결어미(EF)면 완결로 센다. (완결 수, 전체 수, 완결 아닌 줄 예)."""
    lines = re.findall(r'["“]([^"”]+)["”]', text)
    ef, other = 0, []
    for q in lines:
        body = re.sub(r'[.!?…\s]+$', '', q.strip())
        if not body:
            continue
        toks = kiwi().tokenize(body)
        if toks and toks[-1].tag == 'EF':
            ef += 1
        else:
            other.append(q.strip())
    return ef, ef + len(other), other

def unanchored_dialogue_runs(paras, names):
    """W16 발화자 표지: 대사 문단이 3개 이상 이어지는데 그 앞 서술 문단에 인물 이름이 하나도 없으면 그 묶음의 첫 대사."""
    names = list(names) + [n[-2:] for n in names if len(n) == 3]   # 서도현 → 도현
    out, run, prev_narr = [], [], ''
    for p in paras + ['']:
        if is_quote_para(p):
            run.append(p)
            continue
        if len(run) >= 3 and names and not any(n in prev_narr for n in names):
            out.append(run[0])
        run, prev_narr = [], p
    return out

def no_pov_reaction_runs(paras, pov, mono=()):
    """W17 받는 줄(패턴 68): 대사·사건 문단이 넷 이어지는 동안 pov 이름도 독백('…')도 없으면 그 묶음의 첫 문단."""
    if not pov:
        return []
    out, run = [], []
    for p in paras:
        if (not is_quote_para(p)) and (pov in p or p.strip()[:1] in ("'", '‘') or any(m in p for m in mono)):
            run = []
            continue
        run.append(p)
        if len(run) == POV_RUN:
            out.append(run[0])
    return out


def chopped_pairs(paras, skip=()):
    """W11 끊긴 문장(T-052): 같은 문단에서 앞 서술문에 이어지는 서술문이 주어 표지(이/가·은/는) 없이 한 절, 내용어 4개 이하면 앞 문장에 이을 후보다."""
    out = []
    for p in paras:
        ss = split_sents(p)
        for a, b in zip(ss, ss[1:]):
            if any('"' in x or "“" in x or x in skip for x in (a, b)):
                continue
            tb = kiwi().tokenize(b)
            c = sum(1 for t in tb if t.tag in CONTENT_TAGS)
            subj = any(t.tag in ("JKS", "JX") for t in tb) or (len(tb) > 1 and tb[0].tag == "NNP" and tb[1].tag == "XSN")   # "태석이"는 NNP+XSN
            if 2 <= c <= 4 and not subj and not any(t.tag == "EC" for t in tb):
                out.append(a[-18:] + " / " + b)
    return out

def density_stats(sents, skip=()):
    """R9 문장 밀도(패턴 51): 대사·독백을 뺀 서술문의 평균 내용어 수, 절 수(1+EC), 절 3개 이상 비율. 내용어 DENS_LONG개 이상 문장은 long."""
    rows = []
    for s in sents:
        if '"' in s or "“" in s or s in skip:
            continue
        toks = kiwi().tokenize(s)
        c = sum(1 for t in toks if t.tag in CONTENT_TAGS)
        if c < 2:
            continue
        cl = 1 + sum(1 for t in toks if t.tag == "EC")
        rows.append((c, cl, s))
    n = len(rows)
    if not n:
        return {"n": 0, "content": 0, "clauses": 0, "c3": 0, "long": []}
    return {"n": n, "content": round(sum(r[0] for r in rows) / n, 2), "clauses": round(sum(r[1] for r in rows) / n, 2),
            "c3": round(sum(1 for r in rows if r[1] >= 3) / n, 2), "long": [r[2] for r in rows if r[0] >= DENS_LONG]}

def written_endings_in_dialogue(text):
    """W9 대사 입말(패턴 43·49): 큰따옴표 안 문장이 서술체 종결(-ㄴ다·-는다)로 끝나면 돌려준다. '아니다·없다·됐다·없겠다' 같은 입말 -다는 두고 본다."""
    out = []
    for m in DIALOG_PAT.finditer(text):
        q = m.group(1)
        for s in kiwi().split_into_sents(q):
            toks = kiwi().tokenize(s.text)
            tail = [t for t in toks if t.tag not in ("SF", "SP", "SS", "SE", "SO", "SW")][-2:]
            if not tail:
                continue
            last = tail[-1]
            if last.tag == "EF" and last.form in WRITTEN_EF:
                out.append(s.text)
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
    """감각 매칭(P15-3). 3글자 이상 또는 공백 포함 표현은 부분 문자열, 1~2글자 어간은 Kiwi 토큰(용언·명사·부사)의 형태와 일치할 때만."""
    toks = [t for t in kiwi().tokenize(text) if t.tag[0] in "NVM" or t.tag.startswith("XR")]
    found = set()
    for k, w, tag in ALL_SENSE:
        if tag:
            if any(t.form == w and t.tag.startswith(tag) for t in toks): found.add(k)
        elif len(w) >= 3 or " " in w:
            if w in text: found.add(k)
        elif any(t.form == w for t in toks):
            found.add(k)
    return sorted(found)

def length_note(text, rng):
    """분량(공백 포함, 줄바꿈 제외)이 a-b 범위 밖이면 note 문자열, 아니면 None (P15-2)."""
    n = len(text.replace("\n", "").replace("\r", ""))
    a, b = rng
    if a <= n <= b: return None
    return f"분량: {n}자 (기준 {a}~{b}자. 모자라면 장면을 더하지 문장을 더하지 않는다, D2·패턴 90)"

def is_emotion_token(t):
    """R4 감정어 판정. 형용사(VA*)는 어간 접두 일치, 명사(NNG)·어근(XR)은 전체 일치만 — 수직손잡이 "그립"(NNG)이 "그립다" 어간에 걸리지 않게(I-24)."""
    if t.tag in ("VA", "VA-I", "VA-R"):
        return any(t.form.startswith(e) for e in EMOTION)
    if t.tag in ("NNG", "XR"):
        return t.form in EMOTION and t.form not in EMOTION_NOUN_HOMOGRAPHS
    return False

def face_modifier(toks, i):
    """R4 면제(패턴 83): 감정 형용사가 관형형(ETM)으로 얼굴·표정·웃음 같은 명사 앞에 오면 시점 인물이 보는 조연의 표정이다."""
    t = toks[i]
    if not t.tag.startswith("VA"):
        return False
    j = i + 1
    while j < len(toks) and toks[j].tag in ("ETM", "XSA", "EP"):
        if toks[j].tag == "ETM":
            return j + 1 < len(toks) and toks[j + 1].form in FACE_NOUNS
        j += 1
    return False

def fragment_dialogue(text):
    """W22 토막 대사(패턴 75): 큰따옴표 대사 줄마다 마지막 형태소가 명사·조사·부사면 토막(군말·EC·EF는 아님). (토막 수, 전체 수, 토막 예, 셋 연속 여부)."""
    lines = re.findall(r'["“]([^"”]+)["”]', text)
    frag, n, run, best, ex = 0, 0, 0, 0, []
    for q in lines:
        body = re.sub(r'[.!?…\s]+$', '', q.strip())
        if not body:
            continue
        n += 1
        toks = kiwi().tokenize(body)
        last = toks[-1] if toks else None
        if last is not None and (last.tag.startswith(('NN', 'NP', 'NR', 'J', 'SN', 'SL', 'XSN', 'MM', 'MAG')) and last.form not in FRAG_FILLERS):
            frag += 1; run += 1; best = max(best, run); ex.append(q.strip())
        else:
            run = 0
    return frag, n, ex, best

def _dialogue_core(q):
    return re.sub(r'[\s.!?…,]+', '', q).rstrip('요')

def echo_pairs(text):
    """W26 되받기(패턴 86): 잇단 대사 두 줄에서 뒤 줄이 앞 줄의 낱말을 되풀이해 묻거나(A → "A요?"), 되묻기를 되풀이로 받으면(A요? → A …) 쌍으로 센다."""
    lines = [q.strip() for q in re.findall(r'["“]([^"”]+)["”]', text)]
    out = []
    for a, b in zip(lines, lines[1:]):
        ca, cb = _dialogue_core(a), _dialogue_core(b)
        if not ca or not cb:
            continue
        if b.endswith('?') and len(cb) <= 4 and cb in ca:
            out.append((a, b))
        elif a.endswith('?') and len(ca) <= 4 and cb.startswith(ca):
            out.append((a, b))
    return out

def fact_answers(text):
    """W27 사실 답(패턴 86): '그렇-/그러-/그래'로 시작하는 짧은 대사 줄(12자 이하)."""
    return [q.strip() for q in re.findall(r'["“]([^"”]+)["”]', text) if FACT_ANSWER_PAT.match(q) and len(_dialogue_core(q)) <= 12]

def connective_tails(text):
    """W28 대사 끝 연결어미(패턴 87): 대사 안 문장의 마지막 형태소가 EC(-고·-서·-니까·-는데)인 줄."""
    out = []
    for m in DIALOG_PAT.finditer(text):
        for s in kiwi().split_into_sents(m.group(1)):
            body = re.sub(r'[.!?…\s]+$', '', s.text.strip())
            toks = kiwi().tokenize(body) if body else []
            if toks and toks[-1].tag == 'EC' and toks[-1].form not in ('지', '게', '어', '아', '요'):
                out.append(s.text.strip())
                break
    return out

PERSON_PRONOUN_PAT = re.compile(r"(?<![가-힣])(그녀[가-힣]{0,2}|그(?:는|가|를|의|에게|한테)|당신[가-힣]{0,2})(?![가-힣])")   # W30 대사 안 3인칭 대명사·'당신'(패턴 94)
PARTICLE_PAT = r"(?:한테서|한테는|한테도|한테|한텐|에게서|에게는|에게|께서|께|더러|보고|이랑|하고|이야|이|가|은|는|을|를|도|과|와|의|야)"

def person_calls(text, design):
    """W30 대사·독백 안 인칭 지칭(패턴 94): ① 대장 인물의 성 하나+조사("황한테") ② 3인칭 대명사(그녀·그는·그가·그를) ③ '당신'. 성+직함("황 사장")·이름·관계말은 잡지 않고, 서술은 보지 않는다. note다."""
    persons = ((design or {}).get("ledger") or {}).get("persons") or []
    surnames = set()
    for p_ in persons:
        p_ = p_.strip()
        if " " in p_ and len(p_.split()[0]) == 1 and re.fullmatch(r"[가-힣]", p_.split()[0]):
            surnames.add(p_.split()[0])
        elif len(p_) >= 3 and re.fullmatch(r"[가-힣]+", p_):
            surnames.add(p_[0])
    sur_pat = re.compile(r"(?<![가-힣])(" + "|".join(sorted(surnames)) + r")" + PARTICLE_PAT + r"(?![가-힣])") if surnames else None
    out = []
    for q in re.findall(r"[\"“'‘]([^\"”'’]+)[\"”'’]", text):
        hit = []
        if sur_pat and sur_pat.search(q):
            hit.append("성만")
        m = PERSON_PRONOUN_PAT.search(q)
        if m:
            hit.append(m.group(1))
        if hit:
            out.append((q.strip(), "·".join(hit)))
    return out

surname_calls = lambda text, design: [q for q, _ in person_calls(text, design)]   # 호환

TITLE_WORDS = "간호장교|군의관|소대장|대대장|중대장|반장|사장|선생|기사|사수|관측병|통신병|운전병|대위|중위|소위|상사|중사|하사|병장|상병|일병|이병|과장|부장|팀장|원장|교수|박사|형사|경장|순경|이사|대표|주임|실장"
TITLE_CALL_PAT = re.compile(r"(?<![가-힣])(" + TITLE_WORDS + r")님")   # W31 대사 안 '~님' 호칭(패턴 95)
RECALL_PAT = re.compile(r"((?:열흘|사흘|나흘|닷새|이틀|보름|일주일|한 달|두 달|석 달|넉 달) 전|지난달|작년|재작년|그날 밤|그때|그 밤|(?:넉 달|석 달|두 달|한 달) 동안)")   # W33 앞 일 요약문(패턴 95): 때 표지
RECALL_VERB_PAT = re.compile(r"(물었|말했|했다고|하던 말|들었|올렸|왔|갔|받았|썼|적었|잤|살았|했다)")   # + 앞 일을 보고하는 서술어
RECALL_MAX = 3
PRIOR_PREMISE_MAX = 3
NEG_DROP_PAT = re.compile(r"([가-힣]{2,}) (안|못) ([가-힣]{1,6})(?=[.!?…]|$)")   # W35 대사 안 명사+안/못(패턴 97): 조사 없이 안/못이 붙고 그 서술어로 문장이 끝나는 꼴("번호 안 건드려."). "안 건드린다고 약속하지"처럼 이어지면 아님
NEG_DROP_OK_TAIL = "은는이가을를도만에로서께야나며랑와과면까럼지"   # 앞 낱말 끝이 조사면 뗀 것이 아님
NEG_DROP_COUNTERS = ("번", "개", "명", "시", "분", "날", "달", "해", "살", "잔", "병", "줄", "장", "통", "발", "방", "채", "켤레")   # "한 번 안 해 본"처럼 수량 뒤는 부사구
NEG_DROP_MAX = 0   # 장당 상한(하나라도 있으면 note)
NEG_DROP_ADVERBS = ("아직", "이제", "아예", "절대", "다시", "별로", "아무도", "하나도", "전혀", "그거", "그걸", "그건", "이거", "이걸", "저거", "거기", "여기", "지금", "오늘", "내일", "어제", "같이", "진짜", "정말", "너무", "얼마", "거의", "통", "영", "꼭", "잘", "못", "안", "왜", "다")   # 부사·대명사 뒤의 안/못은 입말

def pov_fullname_rank(text, design):
    """W34 시점 인물 풀네임+계급 서술(패턴 97 ③): 설계서 pov(이름)에 성이 붙은 대장 인물("서도현")이 서술(대사 밖)에서 직책·계급과 붙어 나오면("서도현 중사는") 그 꼴을 돌려준다. 호칭 앵커(95 ①)는 남의 호칭에 두는 것이고 시점 인물은 연재가 부르던 대로 쓴다. note다."""
    pov = (design or {}).get("pov")
    if not isinstance(pov, str) or not pov:
        return []
    persons = ((design or {}).get("ledger") or {}).get("persons") or []
    fulls = [p for p in persons if isinstance(p, str) and p != pov and " " not in p and p.endswith(pov) and 1 <= len(p) - len(pov) <= 2]
    if not fulls:
        return []
    narr = strip_quotes(text)
    out = []
    for f in fulls:
        for m in re.finditer(re.escape(f) + r" ?(" + TITLE_WORDS + r")(?=[은는이가도의 ,.])", narr):
            out.append(m.group(0))
    return out

def neg_drops(text):
    """W35 대사 안 명사+안/못 조사 떼기(패턴 97 ②): 큰따옴표 대사 안에서 두 글자 이상 낱말 뒤에 조사 없이 안/못이 붙고 그 서술어로 문장이 끝나는 꼴("그 번호 안 건드려."). "안 건드린다고 약속하지"처럼 말이 이어지면 세지 않는다. 앞 낱말 끝이 조사·수량 단위면 세지 않는다. 꼴 목록을 돌려준다."""
    out = []
    for m_ in DIALOG_PAT.finditer(text):
        q = m_.group(1)
        for m in NEG_DROP_PAT.finditer(q):
            w = m.group(1)
            if w[-1] in NEG_DROP_OK_TAIL or w.endswith(NEG_DROP_COUNTERS) or w in NEG_DROP_ADVERBS or w.endswith(NEG_DROP_ADVERBS):
                continue
            out.append(q[max(0, m.start() - 4):m.end() + 6].strip())
    return out

LADDER_PAT = re.compile(r"^(그래서|그러고|그러면|그럼|가서|와서|누가|언제까지|언제|어디서|왜|뭘|무슨|그다음에?|다음에?|그리고|그런데)[가-힣 ]{0,8}(요|죠|데요|는데요|나요|까요|가요)[.?]?$")   # W36 사다리 물음(패턴 98): 다음 사실을 끌어내려고 둔 짧은 되물음
LADDER_MAX = 0
EXPLAIN_PAT = re.compile(r"[가-힣]는 (겁니다|거예요|거야|거요)(?=[.!…]|$)")   # W37 풀이 어미(패턴 97 ④): 제 행동을 가르치듯 푸는 평서의 '-는 겁니다'("점만 찍는 겁니다"). 물음("뭘 보시는 거예요?")과 과거 관형형("찍은 겁니다")은 세지 않는다
EXPLAIN_MAX = 1
NOUN_IL_PAT = re.compile(r"(?<![가-힣])([가-힣]{2,4}) 일(로|을|은|이|도|에|이라|이에요|입니다|이면|이니)(?=[ .!?,]|$)")   # W38 '명사+일' 포괄 지칭(패턴 97 ①): "번호 일", "유예 일"
NOUN_IL_OK = ("무슨", "어떤", "그런", "이런", "저런", "다른", "좋은", "나쁜", "급한", "바쁜", "작은", "남의", "우리", "회사", "집안", "농사", "오늘", "내일", "어제", "이번", "다음", "지난", "주말", "평일", "하는", "하실", "되는", "없는", "있는", "힘든", "쉬운", "궂은", "큰일", "잔일", "뒷일", "옛일", "별일", "헛일", "할일", "온일", "볼일", "큰", "할", "볼", "한", "온", "간", "갈", "올", "안", "못", "잘", "첫", "모든", "온갖", "같은", "여러", "그날", "그때", "이날", "온종일", "하루", "밭일", "집일", "군일", "일일", "사람", "남의", "자네", "당신", "제", "내", "네", "저희")

def ladder_questions(text):
    """W36 사다리 물음(패턴 98): 대사 세 줄이 잇따르는 자리에서 가운데 줄이 '가서요/그래서요/누가요' 꼴의 짧은 되물음이면 — 다음 사실을 끌어내려고 둔 물음일 가능성. 한 턴에 사실이 둘이라 나눌 때 상대에게 물음을 만들어 주면 생긴다. 가운데 줄들을 돌려준다. note다."""
    paras = [l.strip() for l in text.split("\n") if l.strip()]
    def dlg(x):
        return x[:1] in '"“' and x[-1:] in '"”.?!…'
    out = []
    for i in range(1, len(paras) - 1):
        a, b, c = paras[i - 1], paras[i], paras[i + 1]
        if dlg(a) and dlg(b) and dlg(c):
            core = b.strip('"“”')
            if len(core) <= 12 and LADDER_PAT.match(core):
                out.append(b)
    return out

def explain_endings(text):
    """W37 풀이 어미(패턴 97 ④): 큰따옴표 대사 안에서 '-는/-ㄴ 겁니다·거예요·거야'로 끝나는 꼴. 제 행동·사정을 상대에게 가르치듯 푸는 어미라 셋을 넘으면 note."""
    out = []
    for m_ in DIALOG_PAT.finditer(text):
        q = m_.group(1)
        for m in EXPLAIN_PAT.finditer(q):
            out.append(q[max(0, m.start() - 10):m.end()].strip())
    return out

def noun_il(text):
    """W38 '명사+일' 포괄 지칭(패턴 97 ①): 대사 안에서 "번호 일로", "유예 일을"처럼 '일'이 사건·건·부탁을 대신하는 꼴. 그 일의 낱말로 집어 말한다. note다."""
    out = []
    for m_ in DIALOG_PAT.finditer(text):
        q = m_.group(1)
        for m in NOUN_IL_PAT.finditer(q):
            w = m.group(1)
            if w in NOUN_IL_OK or w[-1] in "은는이가을를의도만에서" or w.endswith(("하는", "되는", "있는", "없는", "오는", "가는", "큰", "한", "할", "볼")):
                continue
            out.append(q[max(0, m.start() - 4):m.end() + 4].strip())
    return out


def title_anchors(text, design):
    """W31 대사의 호칭 앵커(패턴 95): 대사·독백 안에서 '~님'으로 부른 직책·계급(중위님·반장님)이 그 대사보다 앞의 서술에서 사람과 묶였나. 묶임 = 서술 문장에서 그 직책이 대장 인물의 이름(호칭 항목은 제외)과 8자 안에 함께 있거나("간호장교 한유진 중위", "격리반장 류정우 대위") 성+직책 꼴("한 중위", "류 반장")이 있음. 대사 뒤에 나오는 묶임은 늦다. 시점 인물을 부르는 호칭(설계서 characters[].speech.address에 "<pov>에게 '중사님'"으로 적힌 것)은 면제한다 — 시점 인물은 서술이 소개하지 않는다(패턴 97 ③, W34). 안 묶인 호칭을 돌려준다. note다."""
    persons = ((design or {}).get("ledger") or {}).get("persons") or []
    pov = (design or {}).get("pov")
    pov_titles = set()
    if isinstance(pov, str) and pov:
        for c in ((design or {}).get("characters") or {}).values():
            addr = ((c or {}).get("speech") or {}).get("address") if isinstance(c, dict) else None
            if isinstance(addr, str):
                for m in re.finditer(re.escape(pov) + r"에게([^.;,]*)", addr):
                    pov_titles.update(re.findall("(" + TITLE_WORDS + ")님", m.group(1)))
    title_re = re.compile("(?:" + TITLE_WORDS + ")님?$")
    names = [p for p in persons if 2 <= len(p) <= 4 and re.fullmatch(r"[가-힣]+", p) and not title_re.search(p)]
    surnames = {n[0] for n in names if len(n) >= 3}
    anchored, out = set(), []
    for s_ in re.split(r"(?<=[.!?])\s+|\n", text):
        if not s_.strip():
            continue
        is_dialogue = '"' in s_ or "“" in s_ or "'" in s_
        for m in TITLE_CALL_PAT.finditer(s_) if is_dialogue else []:
            t = m.group(1)
            if t in pov_titles:
                continue
            if t not in anchored and t + "님" not in out:
                out.append(t + "님")
        if is_dialogue:
            continue
        for t in re.findall("(?:" + TITLE_WORDS + ")", s_):
            ti = s_.find(t)
            if any(n in s_ and abs(s_.find(n) - ti) <= 8 for n in names) or any(re.search(sn + r"\s?" + t, s_) for sn in surnames):
                anchored.add(t)
    return out


def prior_premises(design):
    """W32 앞 장 전제 수(패턴 95): premises[].item에 'N장'이 든 것. 셋을 넘으면 note."""
    out = []
    for pr in (design or {}).get("premises") or []:
        it = pr.get("item") or ""
        if re.search(r"\d+장", it):
            out.append(it[:24])
    return out


def symmetric_dialogue(text):
    """W29 대칭 수사(패턴 87): 한 대사 안에서 같은 낱말이 -면/-니/-고 건너 되풀이("많이 주면 많이")."""
    return [q.strip() for q in re.findall(r'["“]([^"”]+)["”]', text) if SYMM_PAT.search(q)]

def copied_gists(text, design):
    """G10(패턴 85): 설계서 dialogue_plan[].lines[].gist가 8자 이상 본문에 그대로 있는 줄."""
    out = []
    flat = re.sub(r'\s+', '', text)
    for blk in (design or {}).get('dialogue_plan') or []:
        for ln in blk.get('lines') or []:
            g = (ln.get('gist') or '').strip()
            g = re.sub(r'^\([^)]*\)\s*', '', g)
            for piece in re.split(r'[.!?]\s*', g):
                core = re.sub(r'\s+', '', piece)
                if len(core) >= GIST_MIN and core in flat:
                    out.append(piece.strip())
                    break
    return out

def monologue_issues(text):
    """W24 독백(패턴 79): 작은따옴표 속말에 -다 종결이 셋 이상, 같은 어미가 잇따르거나(-지. -지.), 정당화 표지가 있으면 돌려준다."""
    out = []
    for m in MONO_PAT.finditer(text):
        q = m.group(1)
        if ' ' not in q and len(q) < 4:
            continue
        sents = [x for x in re.split(r'(?<=[.!?])\s*', q) if x.strip()]
        da = sum(1 for x in sents if re.search(r'다[.!?]?$', x.strip()))
        tails = [re.sub(r'[.!?…]+$', '', x.strip())[-1:] for x in sents]
        if len(sents) >= 3 and da >= 3:
            out.append(("-다 종결 %d연속" % da, q))
        elif len(sents) >= 2 and len(set(tails)) == 1 and tails[0]:
            out.append(("같은 어미 '-%s' 연속" % tails[0], q))
        elif JUSTIFY_PAT.search(q):
            out.append(("정당화 논증 '%s'" % JUSTIFY_PAT.search(q).group(1), q))
    return out

def check(text, design=None, length=None, prev=None, draft_chars=None, draft_dens=None):
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    sents = split_sents(text)
    V = []
    # 원문 유지(직관성 우선, principles 서열): 설계서 keep_original의 구절이 든 문장은 R1~R4·문장 R2에서 제외하고 kept로 보고
    keep = (design or {}).get("keep_original") or []
    kept = [s for s in sents if any(k in s for k in keep)]
    # 전제 감정(패턴 16): 설계서 premise_emotions의 구절이 든 문장은 R4만 면제(결론 감정이 아니라 독자가 짐작할 전제)
    premise = (design or {}).get("premise_emotions") or []
    premised = [s for s in sents if s not in kept and any(k in s for k in premise)]
    # 독백(패턴 18): 설계서 monologue의 구절이 든 문장은 대화문처럼 R1~R4·문장 R2에서 제외하고 보고
    mono = (design or {}).get("monologue") or []
    monologued = [s for s in sents if s not in kept and any(k in s for k in mono)]
    # 여러 문장 독백(패턴 79): 설계서 구절이 든 작은따옴표 속말의 다른 문장도 독백으로 다룬다(T-063: 둘째 문장이 서술문으로 R2에 걸림)
    for m_ in MONO_PAT.finditer(text):
        if any(k in m_.group(1) for k in mono):
            for ss in split_sents(m_.group(1)):
                ss = ss.strip()
                for s_ in sents:
                    if s_ not in monologued and s_ not in kept and s_.strip().strip("'").strip() == ss.strip("'").strip():
                        monologued.append(s_)
    # 짐작(패턴 52): 설계서 inference의 구절이 든 문장은 시점 인물이 남의 속·사정을 짐작·판단하는 서술. R3·R4·R7·R8 면제
    infer = (design or {}).get("inference") or []
    inferred = [s for s in sents if s not in kept and any(k in s for k in infer)]
    # 여러 문장 대사(패턴 75): 큰따옴표 안의 둘째 문장부터는 split_sents가 따옴표 없는 문장으로 떼어 내 서술문처럼 R1~R4를 매겼다(T-063). 대사 속 문장은 전부 대화문으로 다룬다
    dialogue_sents = set()
    for m_ in DIALOG_PAT.finditer(text):
        for ss in split_sents(m_.group(1)):
            dialogue_sents.add(ss.strip().strip('\"“”').strip())
    spoken = [s for s in sents if s.strip().strip('\"“”').strip() in dialogue_sents]
    for s in sents:
        if s in kept or s in monologued or s in spoken:
            continue
        plain = strip_quotes(s)
        toks = kiwi().tokenize(plain)
        for i, t in enumerate(toks):
            if t.tag == "MAG" and t.form in DEGREE:
                V.append({"rule": "R1", "sentence": s, "form": t.form})
            if s not in premised and s not in inferred and is_emotion_token(t) and not face_modifier(toks, i):
                V.append({"rule": "R4", "sentence": s, "form": t.form})
        if s not in inferred and any(p.search(plain) for p in STATE_PATS):
            V.append({"rule": "R3", "sentence": s})
        if s not in premised and s not in inferred:
            for f in thought_verbs(toks):
                V.append({"rule": "R7", "sentence": s, "form": f})
        for m in stacked_modifiers(toks):
            V.append({"rule": "G4", "sentence": s, **m})
        for e in josa_errors(s):
            V.append({"rule": "G1", "sentence": s, **e})
        ms = modifier_stats(plain)
        if ms["content"] >= 4 and ms["ratio"] >= R2_SENT:
            V.append({"rule": "R2", "sentence": s, "ratio": ms["ratio"], "forms": ms["forms"]})
    measured = strip_quotes(text)   # 글 전체 R2는 서술문만 잰다. 대사의 좀·뭐·많이를 세면 입말을 깎게 된다(T-063)
    for s in kept + monologued:
        measured = measured.replace(s, " ")
    ms = modifier_stats(measured)
    if ms["ratio"] > R2_TEXT:
        V.append({"rule": "R2", "scope": "text", "ratio": ms["ratio"], "forms": ms["forms"]})
    no_sense_paras = []
    for i, p in enumerate(paras, 1):
        if not strip_quotes(p).strip() or all(x in monologued for x in split_sents(p)):   # 대화문·독백만 있는 문단: 문단 규칙 R2·R5·R6 제외
            continue
        pmeas = strip_quotes(p)
        for x in kept + monologued:   # 원문 유지·독백 문장은 문단 비율에서도 제외
            pmeas = pmeas.replace(x, " ")
        pm = modifier_stats(pmeas)
        if pm["content"] >= 8 and pm["ratio"] >= R2_PARA:
            V.append({"rule": "R2", "paragraph": i, "ratio": pm["ratio"], "forms": pm["forms"]})
        if not senses_in(p):
            no_sense_paras.append(i)
        first = next((s for s in split_sents(p) if strip_quotes(s).strip()), None)
        if first and first not in kept and first not in monologued and first not in premised and first not in inferred:
            f = first_sentence_state(kiwi().tokenize(strip_quotes(first)))
            if f:
                V.append({"rule": "R8", "paragraph": i, "sentence": first, "form": f})
        toks = kiwi().tokenize(p)
        has_number = any(t.tag in ("NR", "SN", "NNP") or (t.tag == "MM" and NUMDET.match(t.form)) for t in toks)
        nng = sum(1 for t in toks if t.tag == "NNG")
        if not has_number and nng < 3 and not (len(split_sents(p)) == 1 and len(p.replace(' ', '')) <= BEAT_MAX_CHARS):   # 박자 문단은 R6 면제(패턴 74)
            V.append({"rule": "R6", "paragraph": i, "nouns": nng})
    # R5: 글 전체에 비시각 감각이 없으면 위반. 문단별 부재는 W3 note(코퍼스 기준 비시각 문단 23~27%, 압축 원칙 패턴 15와 충돌하므로 위반 아님)
    if not senses_in(text):
        V.append({"rule": "R5", "scope": "text"})
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
    if design and prev:   # G8 인물표 근거(패턴 57): characters[*].evidence의 인용이 앞 장 본문에 있어야 한다
        pflat = prev.replace(" ", "")
        for who, c in (design.get("characters") or {}).items():
            for ev in (c.get("evidence") or []):
                if ev.replace(" ", "") not in pflat:
                    V.append({"rule": "G8", "who": who, "evidence": ev})
    for ph in (design or {}).get("banned_phrases") or []:   # X2 금지 표현(패턴 59): 판독에서 지적된 표현의 재등장
        if ph.replace(" ", "") in text.replace(" ", ""):
            V.append({"rule": "X2", "phrase": ph})
    tflat = text.replace(" ", "")
    for pr in (design or {}).get("premises") or []:   # G9 전제의 자리(패턴 76): premises[].shown_in 구절이 본문에 있어야 한다
        si = (pr or {}).get("shown_in") if isinstance(pr, dict) else None
        if si and si.replace(" ", "") not in tflat:
            V.append({"rule": "G9", "shown_in": si, "item": (pr.get("item") or "")[:40]})
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
            if n < 2 or len(form) < 2 or form in ALLOW_ADV or any(form == w for _, w, _t in ALL_SENSE): continue
            V.append({"rule": "G3", "kind": "unregistered_NNP", "form": form, "count": n})
        ledger_nums = design["ledger"].get("numbers", [])
        for expr in sorted(set(number_expressions(text))):
            if not any(expr in ln or ln in expr for ln in ledger_nums):
                V.append({"rule": "G3", "kind": "number_not_in_ledger", "form": expr})
    if prev:   # G5 앞 장 문장 재사용. 일부러 되풀이하는 구절은 design["repeat_ok"]에 적는다
        for r in reused_sentences(sents, prev, ok=(design or {}).get("repeat_ok") or ()):
            V.append({"rule": "G5", **r})
    dens = density_stats(sents, skip=set(monologued))   # R9 문장 밀도
    if dens["n"] >= DENS_MIN_N and (dens["content"] > DENS_CONTENT or dens["clauses"] > DENS_CLAUSES or dens["c3"] > DENS_C3):
        V.append({"rule": "R9", "scope": "text", "content": dens["content"], "clauses": dens["clauses"], "c3": dens["c3"],
                  "limit": {"content": DENS_CONTENT, "clauses": DENS_CLAUSES, "c3": DENS_C3}})
    chars = len(text.replace("\n", "").replace("\r", ""))
    grown = bool(draft_chars) and chars > draft_chars * DRAFT_RATIO
    denser = draft_dens is None or dens["content"] > draft_dens["content"] + L1_DCONTENT or dens["clauses"] > draft_dens["clauses"] + L1_DCLAUSES
    if grown and denser:   # L1 반영 뒤 분량: 길어지고 빽빽해졌으면 덧붙이기
        V.append({"rule": "L1", "chars": chars, "draft_chars": draft_chars, "limit": int(draft_chars * DRAFT_RATIO)})
    spaced = kiwi().space(text)
    notes = []
    if grown and not denser:
        notes.append(f"L1 통과: 초고 {draft_chars}자 → {chars}자로 늘었으나 밀도는 그대로(내용어 {draft_dens['content']} → {dens['content']}). 는 것이 이야기(대사·짐작·다리)인지 확인")
    if dens["n"] >= DENS_MIN_N and (dens["content"] < DENS_MIN_CONTENT or dens["clauses"] < DENS_MIN_CLAUSES):   # W10 밀도 하한
        notes.append(f"W10 잘게 끊김: 서술문 평균 내용어 {dens['content']}·절 {dens['clauses']} (1~10장 하한 {DENS_MIN_CONTENT}·{DENS_MIN_CLAUSES}). 이어지는 행동은 한 문장으로 잇는다")
    chop = chopped_pairs(paras, skip=set(monologued))   # W11 끊긴 문장
    if len(chop) >= CHOP_MIN:
        notes.append(f"W11 주어 없이 끊긴 짧은 문장 {len(chop)}곳: " + " | ".join(chop[:8]) + " (앞 문장에 '-고·-어·-ㄴ 뒤'로 이을 후보)")
    for ex, hit in copied_examples(text, (design or {}).get("user_examples") or []):   # X3 예시 복사
        notes.append(f"X3 예시를 옮겨 적음: 「{hit}」 ← 예시 「{ex[:30]}」 (방향만 쓰고 제 문장으로)")
    for w, meaning in WATCH_WORDS.items():   # W13 동음이의 후보
        if w in text:
            notes.append(f"W13 동음이의 후보 '{w}' (먼저 읽히는 뜻: {meaning}). 다른 말로 바꾸거나 뜻이 서는 말을 곁에 둔다")
    if len(infer) > INFER_MAX:
        notes.append(f"W12 inference {len(infer)}개 (기준 {INFER_MAX}개 이하. 짐작이 많으면 서술이 해설이 된다)")
    lp = long_paras(paras, skip=set(monologued))   # W14 문단 호흡
    if lp:
        notes.append(f"W14 긴 문단 {len(lp)}개(기준 {PARA_MAX_SENTS}문장·{PARA_MAX_CHARS}자 이하): " + ', '.join(f'{i}번({n}문장·{c}자)' for i, n, c in lp[:8]) + ' (한 문단에 한 움직임, 플랫폼 호흡)')
    rs = rhythm_stats(paras, skip=set(monologued))   # W20 문단 박자(패턴 70·74)
    if rs["narr"] >= RHYTHM_MIN_PARAS and (rs["one"] < rs["narr"] * ONE_SENT_MIN or rs["multi"] > rs["narr"] * MULTI_MAX):
        notes.append(f"W20 서술 문단 {rs['narr']}개 중 1문장 문단 {rs['one']}개({rs['one'] * 100 // rs['narr']}%)·3문장 이상 {rs['multi']}개({rs['multi'] * 100 // rs['narr']}%) (기준 1문장 50% 이상·3문장 이상 10% 이하. 플랫폼 표본 86%·1~3%: 한 문단에 한 움직임, 둘째 문장은 반응이나 판단일 때만)")
    last = next((p for p in reversed(paras) if p.strip()), '')   # W21 장의 끝(패턴 73)
    if last and (len(split_sents(last)) > LAST_MAX_SENTS or len(last.replace(' ', '')) > LAST_MAX_CHARS):
        notes.append(f"W21 마지막 문단 {len(split_sents(last))}문장·{len(last.replace(' ', ''))}자 (장의 끝은 한 줄: 대사·그림·다음 목표·새 인물의 첫 마디·질문형 독백 가운데 하나)")
    ef, nq, others = dialogue_ending_stats(text)   # W15 대사 종결 단조
    if nq >= DIALOG_MIN_N and ef / nq >= DIALOG_EF_RATIO:
        notes.append(f"W15 대사 {nq}줄 중 {ef}줄이 완결 종결로 닫힘(기준 {int(DIALOG_EF_RATIO*100)}% 미만). 명사·토막·되물음으로 끝나는 줄을 섞는다")
    persons = list(((design or {}).get('ledger') or {}).get('persons') or [])
    pov = (design or {}).get('pov') or ''
    for q in unanchored_dialogue_runs(paras, persons):   # W16 발화자 표지
        notes.append(f"W16 대사 3연속인데 앞 서술에 인물 이름이 없음: 「{q[:30]}」 (셋 이상 장면이면 앞뒤 행동으로 발화자를)")
    for q in no_pov_reaction_runs(paras, pov, mono=mono):   # W17 받는 줄
        notes.append(f"W17 남의 말·사건 3연속에 {pov}의 반응 없음: 「{q[:30]}」부터 (보고다. 그 자리에서 인물이 실제로 하는 것이 바로 떠오를 때만 한 줄, 아니면 둔다 — 패턴 90)")
    for s_ in sents:
        if '"' in s_ or '“' in s_ or s_ in monologued:
            continue
        if STAY_PAT.match(s_.strip()):   # W18 자리만 알리는 문장
            notes.append(f"W18 자리만 알리는 문장: 「{s_}」 (무엇을 하는지로)")
        m_ = UNKNOWN_PAT.search(s_)
        if m_ and s_ not in inferred:   # W19 모름의 보고문
            notes.append(f"W19 모름의 보고문 '{m_.group(1)}': 「{s_[:40]}」 (질문형 독백으로)")
    if dens["long"]:
        notes.append(f"W8 내용어 {DENS_LONG}개 이상 문장 {len(dens['long'])}개: " + " / ".join(x[:40] for x in dens["long"]) + " (둘로 나누거나 덜어낼 것)")
    for q in written_endings_in_dialogue(text):   # W9 대사 안 서술체 종결
        notes.append(f"W9 대사가 서술체 종결: 「{q}」 (입말로: -ㄹ게·-지·-ㄹ 텐데·-어)")
    fr, fn, fex, frun = fragment_dialogue(text)   # W22 토막 대사(패턴 75)
    if fn >= DIALOG_MIN_N and (fr / fn > FRAG_MAX or frun >= FRAG_RUN):
        notes.append(f"W22 토막 대사 {fn}줄 중 {fr}줄({fr * 100 // fn}%, 최장 {frun}연속; 기준 {int(FRAG_MAX * 100)}% 이하·{FRAG_RUN}연속 미만): " + " / ".join(x[:24] for x in fex[:6]) + " (어미·조사를 끝까지 말한다. 토막은 양념)")
    for s_ in sents:   # W23 생각의 명사화(패턴 78)
        if '"' in s_ or '“' in s_ or s_ in monologued:
            continue
        m_ = NOMINAL_PAT.search(s_)
        if m_:
            notes.append(f"W23 생각의 명사화 '{m_.group(0)}': 「{s_[:40]}」 (행동이나 질문형 독백으로)")
        if CONTRAST_PAT.search(s_.strip()) and s_ not in inferred:   # W25 대비 꼴 셈(패턴 82)
            notes.append(f"W25 대비 꼴 셈: 「{s_[:40]}」 (뜻을 한 번에 말하는 문장으로)")
        elif CONTRAST_PAT.search(s_.strip()):
            notes.append(f"W25 대비 꼴 셈(inference): 「{s_[:40]}」 (면제는 규칙 면제이지 뜻 면제가 아니다)")
    for why, q in monologue_issues(text):   # W24 독백(패턴 79)
        notes.append(f"W24 독백 {why}: 「{q[:40]}」 (속말은 바람·투정·셈·되물음. 정당화·같은 어미 연속은 해설)")
    ec = echo_pairs(text)   # W26 되받기(패턴 86)
    if len(ec) > ECHO_MAX:
        notes.append(f"W26 되받기 쌍 {len(ec)}개(장당 {ECHO_MAX}): " + " / ".join(f"「{a[:12]}」→「{b[:12]}」" for a, b in ec[:4]) + " (묻는 말에는 태도로 답한다)")
    fa = fact_answers(text)   # W27 '그렇-' 사실 답(패턴 86)
    if len(fa) > FACT_MAX:
        notes.append(f"W27 '그렇-' 답 {len(fa)}줄(장당 {FACT_MAX}): " + " / ".join(x[:16] for x in fa[:5]) + " (사실 확인이 아니라 그 사람의 태도로)")
    ct_ = connective_tails(text)   # W28 대사 끝 연결어미(패턴 87)
    if len(ct_) > TAIL_MAX:
        notes.append(f"W28 대사 끝 연결어미 {len(ct_)}줄(장당 {TAIL_MAX}): " + " / ".join(x[:20] for x in ct_[:5]) + " (둘째 정보는 한 문장으로 잇거나 지운다)")
    sc_ = person_calls(text, design)   # W30 대사 안 인칭 지칭(패턴 94)
    if sc_:
        notes.append(f"W30 대사 안 인칭 지칭 {len(sc_)}줄: " + " / ".join(f"「{x[:18]}」({k})" for x, k in sc_[:5]) + " (성 하나·그/그녀·당신은 번역투. 그 자리의 호칭·이름·관계말로, 패턴 94)")
    ta_ = title_anchors(text, design)   # W31 대사의 호칭 앵커(패턴 95)
    if ta_:
        notes.append(f"W31 대사의 호칭 {len(ta_)}개가 이 장 안에서 사람과 묶이지 않음: " + ", ".join(ta_) + " (첫 등장 서술에 이름+직책 한 번 — 연재의 장은 따로 읽힌다, 패턴 95)")
    pf_ = pov_fullname_rank(text, design)   # W34 시점 인물 풀네임+계급(패턴 97)
    if pf_:
        notes.append(f"W34 서술이 시점 인물을 풀네임+계급으로 부름 {len(pf_)}곳: " + ", ".join(pf_[:4]) + " (호칭 앵커는 남의 호칭에. 시점 인물은 연재가 부르던 대로 — 자기소개가 된다, 패턴 97)")
    nd_ = neg_drops(text)   # W35 대사 안 명사+안/못 조사 떼기(패턴 97)
    if len(nd_) > NEG_DROP_MAX:
        notes.append(f"W35 대사 안 조사를 뗀 안/못 {len(nd_)}곳: " + " / ".join(f"「{x}」" for x in nd_[:5]) + " (약속·거절·조건은 그 일의 서술어로 — 안 건드린다고 약속하지, 패턴 97)")
    lq_ = ladder_questions(text)
    if len(lq_) > LADDER_MAX:
        notes.append(f"W36 사다리 물음 {len(lq_)}곳: " + ", ".join(lq_[:4]) + " (한 턴을 나눌 때 상대에게 다음 사실을 끌어내는 되물음을 만들어 주지 않는다 — 같은 사람이 숨을 끊고 잇거나 상대의 몸·태도 한 줄이 사이에 선다, 패턴 98)")
    ee_ = explain_endings(text)
    if len(ee_) > EXPLAIN_MAX:
        notes.append(f"W37 대사 풀이 어미(-는 겁니다/-는 거예요) {len(ee_)}곳: " + ", ".join("「" + x + "」" for x in ee_[:4]) + " (제 행동을 가르치듯 푸는 어미 — 한 행동은 그 서술어로 끝낸다: 적었습니다·안 적었습니다, 패턴 97 ④)")
    ni_ = noun_il(text)
    if ni_:
        notes.append(f"W38 대사 안 '명사+일' 포괄 지칭 {len(ni_)}곳: " + ", ".join("「" + x + "」" for x in ni_[:4]) + " ('일'이 사건·건·부탁을 대신한다 — 그 일의 낱말로: 번호를 쥔 건, 유예, 부탁, 패턴 97 ①)")
    pp_ = prior_premises(design)   # W32 앞 장 전제 수(패턴 95)
    if len(pp_) > PRIOR_PREMISE_MAX:
        notes.append(f"W32 앞 장 전제 {len(pp_)}개(기준 {PRIOR_PREMISE_MAX}): " + " / ".join(pp_[:6]) + " (넷째부터는 이 장 안에서 사람·사건을 세우거나 뺀다. '연재 전제' 기각도 셋까지, 패턴 95)")
    rc_ = [s_ for s_ in sents if s_ not in spoken and s_ not in monologued and '"' not in s_ and "“" not in s_ and RECALL_PAT.search(s_) and RECALL_VERB_PAT.search(s_)]   # W33 앞 일 요약문(패턴 95)
    if len(rc_) >= RECALL_MAX:
        notes.append(f"W33 앞 일을 요약하는 서술 {len(rc_)}문장: " + " / ".join(x[:22] for x in rc_[:5]) + " (관건 선택의 까닭을 앞 장 요약으로 대지 않는다. 이 장의 행동으로, 패턴 95)")
    for q in symmetric_dialogue(text):   # W29 대칭 수사(패턴 87)
        notes.append(f"W29 대사 안 대칭: 「{q[:30]}」 (작가의 말맛이지 그 자리 사람의 말이 아니다)")
    for g in copied_gists(text, design):   # G10 설계서 요지 옮김(패턴 85)
        notes.append(f"G10 설계서 요지를 그대로 옮긴 대사: 「{g[:30]}」 (dialogue_plan에는 move만, 문장은 본문에서)")
    for e, ss in repeated_numbers(sents):   # W7 수치 되풀이
        notes.append(f"W7 수치 되풀이 '{e}': " + " / ".join(x[:30] for x in ss) + " (한 번 준 수치를 대사·독백에서 다시 말하는지 확인)")
    if length:
        ln = length_note(text, length)
        if ln: notes.append(ln)
    objs = ((design or {}).get("materials") or {}).get("objects") or []
    if len(objs) > 3:   # W2 사물 경제 (decisions D2: 핵심 사물 2~3개)
        notes.append(f"W2 설계서 사물 {len(objs)}개 (기준 3개 이하, 같은 역할은 합칠 것): {objs}")
    if no_sense_paras:
        notes.append(f"W3 비시각 감각 없는 문단: {no_sense_paras} (글 전체 ≥1이면 통과, 문단마다 넣으려고 묘사를 늘리지 말 것)")
    weak = [s for s in sents if any(p.search(strip_quotes(s)) for p in WEAK_BEATS)]
    if weak:   # W4 상투 beat(패턴 25): 한숨·어깨 으쓱·미소 같은 누구나 하는 동작은 대사 사이 지문 자격이 없음
        notes.append("W4 상투 동작(beat): " + " / ".join(weak) + " (대사 사이 지문이면 인물만의 작은 동작으로)")
    run, best = 0, 0   # W5 묘사 연속(패턴 32): 대사·독백 없이 서술문만 5개 이상 이어지면 note
    for s_ in sents:
        if '"' in s_ or "“" in s_ or s_ in monologued:
            run = 0
        else:
            run += 1; best = max(best, run)
    if best >= 5:
        notes.append(f"W5 대사·독백 없는 서술문 {best}개 연속 (기준 4개. 보고다 — 채우려고 속말·대사를 짓지 않는다, 패턴 90)")
    for i, p in enumerate(paras, 1):   # W1 묘사 과잉 의심: 문단 5문장 이상 (decisions D2 "문단 4문장 이하")
        n = len(split_sents(p))
        if n >= 5:
            notes.append(f"W1 문단 {i}: {n}문장 (기준 4문장 이하, 같은 상태의 반복 묘사인지 확인)")
    return {
        "sentences": len(sents), "paragraphs": len(paras), "chars": chars, "density": dens, "rhythm": rs,
        "notes": notes, "kept_original": kept, "premise_emotions": premised, "monologue": monologued, "inference": inferred, "chopped": chop, "spoken": spoken,
        "modifier": ms, "senses": senses_in(text), "ending": er, "para_first": pr,
        "translationese_counts": trans,
        "spacing_differs": spaced != text,
        "violations": V, "pass": not V,
    }

def summary_line(r):
    return (f"문장 {r['sentences']} / 문단 {r['paragraphs']} / {r['chars']}자 / 수식어 비율 {r['modifier']['ratio']} {r['modifier']['forms']} "
            f"/ 명사 {r['modifier']['nouns']} 동사 {r['modifier']['verbs']} / 감각 {r['senses']} / 번역투 {r['translationese_counts']} "
            f"/ 밀도 내용어 {r['density']['content']} 절 {r['density']['clauses']} 절3+ {r['density']['c3']}")

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
    ap.add_argument("--prev", nargs="*", help="앞 장 final.txt들. 주면 G5(앞 장 문장 재사용)를 본다")
    ap.add_argument("--length", help="분량 기준 a-b (예: 400-700). 범위 밖은 위반이 아니라 notes")
    ap.add_argument("--draft", help="초고 파일. 주면 L1(반영 뒤 글자 수가 초고 ×1.05를 넘고 밀도도 오르면 위반)을 본다")
    a = ap.parse_args()
    length = tuple(int(x) for x in a.length.split("-")) if a.length else None
    if a.lexicon_stats:
        print(json.dumps(lexicon_stats(), ensure_ascii=False, indent=1)); return
    if not a.path:
        ap.error("본문 경로 또는 - 필요")
    text = sys.stdin.read() if a.path == "-" else open(a.path, encoding="utf-8").read()
    design = json.load(open(a.design, encoding="utf-8")) if a.design else None
    prev = "\n".join(open(f, encoding="utf-8").read() for f in a.prev) if a.prev else None
    dd = density_stats(split_sents(open(a.draft, encoding="utf-8").read())) if a.draft else None
    dc = len(open(a.draft, encoding="utf-8").read().replace("\n", "").replace("\r", "")) if a.draft else None
    r = check(text, design, length, prev, dc, dd)
    if a.json:
        print(json.dumps(r, ensure_ascii=False, indent=1))
    else:
        print(summary_line(r))
        for n in r["notes"]: print("  note:", n)
        for k in r["kept_original"]: print("  원문 유지(직관성):", k)
        for k in r["premise_emotions"]: print("  전제 감정(짐작 유도):", k)
        for k in r["monologue"]: print("  독백(대화문 취급):", k)
        for k in r["inference"]: print("  짐작(시점 인물):", k)
        print("PASS" if r["pass"] else "위반:")
        for v in r["violations"]:
            print(" ", json.dumps(v, ensure_ascii=False))
    sys.exit(0 if r["pass"] else 1)

if __name__ == "__main__":
    main()
