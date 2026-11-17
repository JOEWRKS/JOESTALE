# 요인별 집계. 형태 효과: F1 vs F2 (내용 고정). 내용 효과: p(셈 있음) vs m(셈 없음) (형태 고정).
import io, json, re, os, collections
HERE = os.path.dirname(os.path.abspath(__file__))
ITEMS = ["읽힘", "당김", "설명감", "인물", "종합"]
def kind(a, b):
    if a[:2] != b[:2]: return "형태"
    return "내용"
res = {k: {it: collections.Counter() for it in ITEMS} for k in ("형태", "내용")}
byjudge = {}
consist = collections.Counter()
import sys
JUDGES=[int(x) for x in sys.argv[1:]] or [1,2,3]
for j in JUDGES:
    key = json.load(io.open(os.path.join(HERE, f"judge{j}", "key.json"), encoding="utf-8"))
    md = io.open(os.path.join(HERE, f"judge{j}", "result.md"), encoding="utf-8").read()
    bj = {k: {it: collections.Counter() for it in ITEMS} for k in ("형태", "내용")}
    seen = {}
    for line in md.splitlines():
        m = re.match(r"\|\s*(P\d\d)\s*\|(.*)", line)
        if not m: continue
        pid = m.group(1); cells = [c.strip() for c in m.group(2).split("|")]
        k = key[pid]; kd = kind(k["가"], k["나"])
        for it, cell in zip(ITEMS, cells):
            if cell.startswith("가"): w = k["가"]
            elif cell.startswith("나"): w = k["나"]
            else:
                lab = "둘 다" if "둘 다" in cell and "아님" not in cell else "같음" if it != "종합" else cell
                res[kd][it][lab] += 1; bj[kd][it][lab] += 1; continue
            # 승자 특성: 형태 쌍이면 F1/F2, 내용 쌍이면 p/m
            lab = w[:2] if kd == "형태" else ("셈 있음" if w.endswith("p") else "셈 없음")
            res[kd][it][lab] += 1; bj[kd][it][lab] += 1
        pk = (k["scene"], tuple(sorted([k["가"], k["나"]])))
        v = cells[4]; vv = "both" if "둘 다" in v else k["가"] if v.startswith("가") else k["나"] if v.startswith("나") else v
        if pk in seen: consist["일치" if seen[pk] == vv else "불일치"] += 1
        else: seen[pk] = vv
    byjudge[j] = bj
for kd, labs in (("형태", ["F1", "F2"]), ("내용", ["셈 있음", "셈 없음"])):
    print(f"\n## {kd} 효과 ({len(JUDGES)*8}판정, 평가자 {JUDGES})")
    print(f"| 항목 | {labs[0]} 승 | {labs[1]} 승 | 같음/둘 다 |\n|---|---|---|---|")
    for it in ITEMS:
        c = res[kd][it]; tie = sum(v for k2, v in c.items() if k2 not in labs)
        print(f"| {it} | {c[labs[0]]} | {c[labs[1]]} | {tie} |")
    print("평가자별 종합:", {j: dict(byjudge[j][kd]["종합"]) for j in byjudge})
print(f"\n같은 쌍 두 번 판정(종합) 일치 {consist['일치']} / 불일치 {consist['불일치']}")
