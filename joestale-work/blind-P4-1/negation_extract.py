# 패턴 21 검증용: 텍스트에서 부정 서술 문장을 뽑아 JSON으로 낸다.
# 실행: PYTHONIOENCODING=utf-8 python negation_extract.py <파일>... > negations.json
import io, re, sys, json, os
NEG = re.compile(r"(지\s*않|지\s*못|지\s*말|않았|않는|않고|못했|못하|없었|없는|없이|없다|안\s+\S|못\s+\S|아니었|아니다|아닌)")
def sents(text):
    text = re.sub(r"\s+", " ", text)
    return [s.strip() for s in re.split(r"(?<=[.!?다])\s+(?=[^\s])", text) if s.strip()]
out = []
for path in sys.argv[1:]:
    t = io.open(path, encoding="utf-8").read()
    ss = sents(t)
    n = 0
    for i, s in enumerate(ss):
        if NEG.search(s) and len(s) < 160:
            n += 1
            out.append({"src": os.path.basename(path), "idx": i, "prev": ss[i-1] if i else "", "sent": s})
    sys.stderr.write(f"{os.path.basename(path)}: 문장 {len(ss)}, 부정 {n} ({n/len(ss):.0%})\n")
json.dump(out, sys.stdout, ensure_ascii=False, indent=1)
