# 판정 집계: judgeN/result.md 표를 key.json으로 풀어 판(A/B/C)별 승수를 센다. 실행: PYTHONIOENCODING=utf-8 python tally.py
import io, json, re, os, collections
HERE = os.path.dirname(os.path.abspath(__file__))
ITEMS = ["읽힘", "당김", "설명감", "인물", "종합"]
NAME = {"A": "한 줄형", "B": "문장형", "C": "대조군"}
wins = {it: collections.Counter() for it in ITEMS}      # 판별 승수
ties = {it: 0 for it in ITEMS}
h2h = {it: collections.Counter() for it in ITEMS}       # (승, 패) 쌍별
overall_both = 0; n = 0
consist = collections.Counter()  # 같은 쌍 두 번 판정 일치 여부 (종합)
per_judge = {}
for j in (1, 2, 3):
    key = json.load(io.open(os.path.join(HERE, f"judge{j}", "key.json"), encoding="utf-8"))
    md = io.open(os.path.join(HERE, f"judge{j}", "result.md"), encoding="utf-8").read()
    rows = {}
    for line in md.splitlines():
        m = re.match(r"\|\s*(P\d\d)\s*\|(.*)", line)
        if not m: continue
        cells = [c.strip() for c in m.group(2).split("|")]
        rows[m.group(1)] = cells
    per_judge[j] = rows
    seen = {}
    for pid, cells in rows.items():
        k = key[pid]; n += 1
        for it, cell in zip(ITEMS, cells):
            if it == "종합":
                if "둘 다 아님" in cell: continue
                if "둘 다" in cell: overall_both += 1; verdict = None
                elif cell.startswith("가"): verdict = k["가"]
                elif cell.startswith("나"): verdict = k["나"]
                else: verdict = None
            else:
                verdict = k["가"] if cell.startswith("가") else k["나"] if cell.startswith("나") else None
            if verdict is None: ties[it] += 1; continue
            loser = k["나"] if verdict == k["가"] else k["가"]
            wins[it][verdict] += 1; h2h[it][(verdict, loser)] += 1
        pairkey = (k["scene"], tuple(sorted([k["가"], k["나"]])))
        v = cells[4]
        vv = "both" if "둘 다" in v else k["가"] if v.startswith("가") else k["나"] if v.startswith("나") else "?"
        if pairkey in seen: consist["일치" if seen[pairkey] == vv else "불일치"] += 1
        else: seen[pairkey] = vv
print(f"판정 {n}건 (평가자 3 × 12쌍)\n")
print("| 항목 | 한 줄형(A) 승 | 문장형(B) 승 | 대조군(C) 승 | 같음/둘 다 |\n|---|---|---|---|---|")
for it in ITEMS:
    print(f"| {it} | {wins[it]['A']} | {wins[it]['B']} | {wins[it]['C']} | {ties[it]} |")
print("\n쌍별 (승-패, 종합 기준은 '둘 다' 제외):")
for it in ITEMS:
    print(f"- {it}: " + ", ".join(f"{NAME[a]}>{NAME[b]} {h2h[it][(a,b)]}:{h2h[it][(b,a)]}" for a, b in [("A","B"),("A","C"),("B","C")]))
print(f"\n같은 쌍 두 번 판정(종합) 일치 {consist['일치']} / 불일치 {consist['불일치']}")
