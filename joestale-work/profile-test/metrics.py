"""플랫폼 수치 측정 (T-059 JS met() 포팅). 사용: PYTHONIOENCODING=utf-8 python metrics.py 파일...
문단 = 빈 줄 구분. 대사 문단 = 따옴표(" ' “ ‘)로 시작. 나머지가 서술 문단.
1문장 서술 % = 문장 1개인 서술 문단 / 서술 문단. 서술 평균 = 서술 문단 글자 평균. 3문장+ = 문장 3개 이상 서술 문단 수."""
import sys, re, io, json
def met(text):
    text = text.replace("\r\n", "\n")
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    quote = [p for p in paras if p[0] in "\"'“‘「"]
    narr = [p for p in paras if p[0] not in "\"'“‘「" and not p.startswith("***")]
    def nsent(p):
        return max(1, len([s for s in re.split(r"(?<=[.!?…])\s+|(?<=[.!?…])$", p) if s.strip()]))
    counts = [nsent(p) for p in narr]
    chars = len(re.sub(r"\s", "", text))
    return {
        "chars": chars, "paras": len(paras), "quote_pct": round(100 * len(quote) / max(1, len(paras))),
        "narr_avg": round(sum(len(p) for p in narr) / max(1, len(narr))),
        "one_pct": round(100 * sum(1 for c in counts if c == 1) / max(1, len(narr))),
        "three_plus": sum(1 for c in counts if c >= 3),
        "max_sents": max(counts) if counts else 0,
        "last": paras[-1][:40] if paras else "",
    }
if __name__ == "__main__":
    for f in sys.argv[1:]:
        m = met(io.open(f, encoding="utf-8").read())
        print(f"{f}: {json.dumps(m, ensure_ascii=False)}")
