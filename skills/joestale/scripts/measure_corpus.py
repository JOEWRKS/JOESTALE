"""코퍼스 측정 (Phase 3, P3-1). 공유마당 텍스트를 작품별로 측정해 R2 임계값 보정 근거를 만든다.

사용: PYTHONIOENCODING=utf-8 python measure_corpus.py <corpus 폴더> [--out MEASURE.md] [--json out.json]
입력: <corpus>/<작가>/extracted/*.txt 중 본문 파일(출처 메모 파일은 '출처 링크'로 시작하므로 제외).
전처리: 공유마당 txt는 행 중간에 줄바꿈이 있어(예: "때이었\n다") 문장부호로 끝나지 않는 줄은 다음 줄과 붙인다.
측정: 글자 수, 문장 수, 수식어 비율(check_text.modifier_stats), 정도부사/1000 내용어, 감정어/1000, 문단 수식어 비율 분포(p50·p90·max),
      비시각 감각 문단 비율, 번역투 건수, 마지막 어절 최대 연속. 1930년대 표기라 Kiwi 태깅 오차가 있음을 리포트에 명시.
"""
import sys, re, json, argparse, pathlib, statistics, importlib.util

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("ct", HERE / "check_text.py")
ct = importlib.util.module_from_spec(spec); spec.loader.exec_module(ct)

def normalize(raw: str) -> str:
    lines = [l.rstrip() for l in raw.replace("\r\n", "\n").split("\n")]
    out, buf = [], ""
    for l in lines:
        s = l.strip()
        if not s:
            if buf: out.append(buf); buf = ""
            continue
        if buf and not re.search(r"[.!?」』”\"']$", buf):
            buf += s if re.match(r"^[가-힣]", s) and re.search(r"[가-힣]$", buf) else " " + s
        else:
            if buf: out.append(buf)
            buf = s
    if buf: out.append(buf)
    # 첫 1~3줄 제목·작가명 제거(짧고 문장부호 없음)
    while out and len(out[0]) < 20 and not re.search(r"[.!?]", out[0]):
        out.pop(0)
    return "\n\n".join(out)

def percentile(xs, p):
    if not xs: return 0.0
    xs = sorted(xs); k = (len(xs) - 1) * p
    f, c = int(k), min(int(k) + 1, len(xs) - 1)
    return round(xs[f] + (xs[c] - xs[f]) * (k - f), 3)

def measure(text: str) -> dict:
    paras = [p for p in text.split("\n\n") if p.strip()]
    sents = ct.split_sents(text)
    ms = ct.modifier_stats(text)
    toks = ct.kiwi().tokenize(text)
    content = ms["content"] or 1
    degree = sum(1 for t in toks if t.tag == "MAG" and t.form in ct.DEGREE)
    emotion = sum(1 for t in toks if t.tag in ("VA", "VA-I", "VA-R", "XR", "NNG") and any(t.form.startswith(e) for e in ct.EMOTION))
    para_ratios = [ct.modifier_stats(p)["ratio"] for p in paras if ct.modifier_stats(p)["content"] >= 8]
    nonvisual = sum(1 for p in paras if ct.senses_in(p))
    trans = {label: len(pat.findall(text)) for pat, label, _ in ct.TRANS if pat.findall(text)}
    return {
        "chars": len(text.replace("\n", "")), "sentences": len(sents), "paragraphs": len(paras),
        "modifier_ratio": ms["ratio"], "nouns": ms["nouns"], "verbs": ms["verbs"],
        "degree_per_1000": round(degree / content * 1000, 1), "emotion_per_1000": round(emotion / content * 1000, 1),
        "para_ratio_p50": percentile(para_ratios, 0.5), "para_ratio_p90": percentile(para_ratios, 0.9),
        "para_ratio_max": max(para_ratios) if para_ratios else 0.0, "paras_measured": len(para_ratios),
        "nonvisual_para_share": round(nonvisual / max(len(paras), 1), 2),
        "senses": ct.senses_in(text), "translationese": trans, "ending_max_run": ct.ending_repeat(sents)["max_run"],
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("corpus")
    ap.add_argument("--out", default=None)
    ap.add_argument("--json", default=None)
    a = ap.parse_args()
    root = pathlib.Path(a.corpus)
    rows = []
    for t in sorted(root.glob("*/extracted/*.txt")):
        raw = t.read_text(encoding="utf-8-sig", errors="replace")
        if raw.lstrip().startswith("출처 링크") or len(raw) < 2000:
            continue
        text = normalize(raw)
        m = measure(text)
        m["author"], m["file"] = t.parent.parent.name, t.name
        rows.append(m)
        (t.parent / (t.stem + ".normalized.txt")).write_text(text, encoding="utf-8")
        print(f"{m['author']:4s} {t.name[:28]:28s} {m['chars']:>6}자 비율 {m['modifier_ratio']:.2f} p50 {m['para_ratio_p50']:.2f} p90 {m['para_ratio_p90']:.2f} 정도부사/1k {m['degree_per_1000']} 감정/1k {m['emotion_per_1000']} 비시각문단 {m['nonvisual_para_share']}")
    if not rows:
        print("본문 파일 없음"); sys.exit(1)
    allr = [r["modifier_ratio"] for r in rows]
    p90s = [r["para_ratio_p90"] for r in rows]
    summary = {"works": len(rows), "ratio_mean": round(statistics.mean(allr), 3), "ratio_max": max(allr),
               "para_p90_mean": round(statistics.mean(p90s), 3), "para_p90_max": max(p90s),
               "degree_per_1000_mean": round(statistics.mean(r["degree_per_1000"] for r in rows), 1),
               "emotion_per_1000_mean": round(statistics.mean(r["emotion_per_1000"] for r in rows), 1)}
    print("\n요약:", json.dumps(summary, ensure_ascii=False))
    if a.json:
        pathlib.Path(a.json).write_text(json.dumps({"rows": rows, "summary": summary}, ensure_ascii=False, indent=1), encoding="utf-8")
    if a.out:
        md = ["# 코퍼스 측정표 (공유마당 저작권 만료 작품)", "",
              "측정: `skills/joestale/scripts/measure_corpus.py`. 수식어 비율 = (MAG+VA+XSA+MM − 화이트리스트)/내용어. 1930년대 표기라 Kiwi 태깅 오차가 있다(참고치).", "",
              "| 작가 | 파일 | 글자 | 문장 | 수식어 비율 | 문단 p50 | 문단 p90 | 문단 max | 정도부사/1k | 감정어/1k | 비시각 감각 문단 | 어미 최대연속 |",
              "|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for r in rows:
            md.append(f"| {r['author']} | {r['file']} | {r['chars']} | {r['sentences']} | {r['modifier_ratio']:.2f} | {r['para_ratio_p50']:.2f} | {r['para_ratio_p90']:.2f} | {r['para_ratio_max']:.2f} | {r['degree_per_1000']} | {r['emotion_per_1000']} | {r['nonvisual_para_share']} | {r['ending_max_run']} |")
        md += ["", "## 요약", "", "```json", json.dumps(summary, ensure_ascii=False, indent=1), "```"]
        pathlib.Path(a.out).write_text("\n".join(md) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
