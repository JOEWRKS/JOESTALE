# 분리 재검증 묶음 (T-061). 쌍 4종/장면: 형태 효과(F1p-F2p, F1m-F2m), 내용 효과(F2p-F2m, F1p-F1m). 2장면 = 8쌍, 순서 뒤집어 두 번 = 16판정/평가자.
import io, json, random, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
RUBRIC = re.search(r'RUBRIC = """(.*?)"""', io.open(os.path.join(HERE, "..", "build_pack.py"), encoding="utf-8").read(), re.S).group(1)
RUBRIC = RUBRIC.replace("12쌍 전부", "16쌍 전부")
VERS = ["F1p", "F1m", "F2p", "F2m"]
texts = {f"{s}_{v}": io.open(os.path.join(HERE, f"{s}_{v}.txt"), encoding="utf-8").read().strip() for s in ("S1", "S2") for v in VERS}
pairs = [(s, a, b) for s in ("S1", "S2") for a, b in [("F1p", "F2p"), ("F1m", "F2m"), ("F2p", "F2m"), ("F1p", "F1m")]]
import sys
JUDGES = [int(x) for x in sys.argv[1:]] or [1, 2, 3]
for j in JUDGES:
    random.seed(20261116 + j)
    d = os.path.join(HERE, f"judge{j}"); os.makedirs(d, exist_ok=True)
    first = pairs[:]; random.shuffle(first)
    flips = [random.random() < 0.5 for _ in first]
    second = list(zip(first, [not f for f in flips])); random.shuffle(second)
    seq = list(zip(first, flips)) + second
    key, md = {}, [RUBRIC, "\n---\n"]
    for i, ((s, a, b), flip) in enumerate(seq, 1):
        pid = f"P{i:02d}"; ga, na = (b, a) if flip else (a, b)
        key[pid] = {"scene": s, "가": ga, "나": na}
        md.append(f"\n## {pid}\n")
        for label, v in (("가", ga), ("나", na)):
            md.append(f"\n### {pid} {label}\n\n" + texts[f"{s}_{v}"] + "\n")
    io.open(os.path.join(d, "pairs.md"), "w", encoding="utf-8").write("\n".join(md))
    json.dump(key, io.open(os.path.join(d, "key.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"judge{j}: {len(seq)}쌍")
