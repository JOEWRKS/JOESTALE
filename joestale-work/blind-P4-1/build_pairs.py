# 블라인드 비교표 생성 (P4-1). 실행: PYTHONIOENCODING=utf-8 python build_pairs.py
# baseline/<X>.txt(스킬 없음)와 skill/<X>.txt(스킬 결과)를 가/나로 무작위 배치해 pairs.md를 만들고,
# 어느 쪽이 스킬인지는 key.json에만 적는다. 판정 전에는 key.json을 열지 않는다.
import io, json, random, subprocess, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
CHECK = os.path.join(ROOT, "skills", "joestale", "scripts", "check_text.py")
INPUTS = {
    "A": "이 문단 고쳐줘: 할머니의 방은 매우 작고 낡았다. 벽지는 누렇게 변색되어 있었고 공기는 늘 축축하고 무거웠다. 할머니는 아주 외롭고 고집스러운 성격이었다. 그래도 나는 그 방에 들어가면 정말 마음이 편해졌다.",
    "B": "비 오는 날 재회",
    "C": "요즘 지하철이 너무 답답해",
    "D": "짧은 단편 하나 써줘",
}

def metrics(path):
    out = subprocess.run([sys.executable, CHECK, path, "--json"], capture_output=True, text=True,
                         encoding="utf-8", env={**os.environ, "PYTHONIOENCODING": "utf-8"})
    try:
        d = json.loads(out.stdout)
    except Exception:
        return {"error": out.stdout[-300:] + out.stderr[-300:]}
    return {"chars": d["chars"], "ratio": d["modifier"]["ratio"], "senses": d["senses"],
            "violations": sorted({v["rule"] for v in d["violations"]}), "pass": d["pass"]}

random.seed(int(sys.argv[1]) if len(sys.argv) > 1 else 20261030)
key, md = {}, ["# 블라인드 비교 (P4-1)\n", "같은 입력을 두 방식으로 썼다. 어느 쪽이 스킬인지 모른 채 읽고, 항목마다 **가/나 중 더 '작가의 어휘'에 가까운 쪽**과 걸리는 문장 하나를 적는다. 판정 뒤 key.json을 연다.\n"]
table = ["| 항목 | 쪽 | 글자 | 수식어 비율 | 감각 | 검증 위반 |", "|---|---|---|---|---|---|"]
for k, inp in INPUTS.items():
    b = io.open(os.path.join(HERE, "baseline", k + ".txt"), encoding="utf-8").read().strip()
    s = io.open(os.path.join(HERE, "skill", k + ".txt"), encoding="utf-8").read().strip()
    order = ["baseline", "skill"]; random.shuffle(order)
    texts = {"baseline": b, "skill": s}
    key[k] = {"가": order[0], "나": order[1]}
    md.append(f"\n## {k}\n\n**입력**\n\n> {inp}\n")
    for label, src in zip(["가", "나"], order):
        md.append(f"\n**{label}**\n\n" + "\n".join(("> " + l) if l else ">" for l in texts[src].split("\n")) + "\n")
        m = metrics(os.path.join(HERE, src, k + ".txt"))
        table.append(f"| {k} | {label} | {m.get('chars')} | {m.get('ratio')} | {','.join(m.get('senses', []))} | {','.join(m.get('violations', [])) or '없음'} |")
md.append("\n## 기계 수치 (참고, 판정 뒤에 볼 것)\n\n설계서 없이 측정했으므로 원문 유지·전제 감정·독백 면제가 적용되지 않는다(스킬 쪽에도 R1·R2·R4가 뜰 수 있음).\n\n" + "\n".join(table) + "\n")
io.open(os.path.join(HERE, "pairs.md"), "w", encoding="utf-8").write("\n".join(md))
json.dump(key, io.open(os.path.join(HERE, "key.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("pairs.md, key.json written")
