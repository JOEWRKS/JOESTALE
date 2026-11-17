# 분리 재검증 표본 생성. 마스터(⟦⟧ = 인물 셈 문장)에서 형태 F1(한 줄형: 서술 문장마다 문단) / F2(문장형: 마스터 문단 그대로) × 내용 K+(셈 포함) / K-(셈 삭제) = 4편/장면.
import io, re, os
HERE = os.path.dirname(os.path.abspath(__file__))
def sents(p):
    return [s for s in re.split(r"(?<=[.!?])\s+(?=[^\s])", p) if s.strip()]
for s in ("S1", "S2"):
    master = io.open(os.path.join(HERE, f"{s}_master.txt"), encoding="utf-8").read().strip()
    paras = [p.strip() for p in re.split(r"\n\s*\n", master) if p.strip()]
    for k in ("K+", "K-"):
        ps = []
        for p in paras:
            q = re.sub(r"⟦(.*?)⟧", r"\1", p) if k == "K+" else re.sub(r"\s*⟦.*?⟧", "", p)
            q = re.sub(r"\s{2,}", " ", q).strip()
            if q: ps.append(q)
        f2 = "\n\n".join(ps) + "\n"
        f1 = "\n\n".join(x for p in ps for x in ([p] if p[0] in "\"'“‘「" else sents(p))) + "\n"
        tag = "p" if k == "K+" else "m"
        io.open(os.path.join(HERE, f"{s}_F1{tag}.txt"), "w", encoding="utf-8").write(f1)
        io.open(os.path.join(HERE, f"{s}_F2{tag}.txt"), "w", encoding="utf-8").write(f2)
print("written")
