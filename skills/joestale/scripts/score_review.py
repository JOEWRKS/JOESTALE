# -*- coding: utf-8 -*-
"""검수 독자 출력(마크다운 표)을 정답지와 대조해 적중 수를 센다.

python score_review.py regression/ch11/must_catch.json reader_out.md [reader_out2.md ...] [--lens 문장|연결] [--json]
여러 출력 파일을 주면 합쳐서(합집합) 센다. 전문 검수자 표의 판정 ○ 행은 세지 않는다(T-067).
"""
import argparse, json, re, sys

def rows(path):
    out = []
    for line in open(path, encoding="utf-8").read().splitlines():
        line = line.strip()
        if line.startswith("## 장부 추가분"):
            break
        if not line.startswith("|"):
            # "- [항목] "인용" — 문제: …" 꼴(41항목 검수 출력)도 받는다
            if line.startswith("- ") and ("\"" in line or "“" in line):
                out.append((line, line))
            elif line.startswith(("{", "note:")):   # 검증기 출력(위반 JSON·note 줄)도 행으로 받는다(T-055)
                out.append((line, line))
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if not cells or not (re.fullmatch(r"\d+", cells[0]) or any(c in ("×", "△") for c in cells)):   # 번호 없는 표(인물 검수자)는 판정 ×·△ 행만 받는다(T-067)
            continue
        if any(c == "○" for c in cells):   # 전문 검수자(5-C) 표는 모든 단위에 행이 있다. 판정 ○ 행은 지적이 아니다(T-067)
            continue
        out.append((cells[1] if len(cells) > 1 else "", line))
    return out

def norm(s):
    return re.sub(r"\s+", "", s)

def score(spec, files, lens=None):
    rs = [r for f in files for r in rows(f)]
    res = []
    for it in spec["items"]:
        if lens and it["lens"] != lens:
            continue
        hit = any(norm(k) in norm(q) for k in it["keys"] for q, _ in rs) or \
              any(norm(k) in norm(full) for k in it.get("row_keys", []) for _, full in rs)
        res.append({"id": it["id"], "lens": it["lens"], "hit": hit, "why": it["why"]})
    return {"findings": len(rs), "total": len(res), "hit": sum(r["hit"] for r in res), "items": res}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("spec"); ap.add_argument("files", nargs="+")
    ap.add_argument("--lens"); ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    r = score(json.load(open(a.spec, encoding="utf-8")), a.files, a.lens)
    if a.json:
        print(json.dumps(r, ensure_ascii=False, indent=1)); return
    print(f"지적 {r['findings']}건, 정답지 적중 {r['hit']}/{r['total']}")
    for it in r["items"]:
        if not it["hit"]:
            print(f"  놓침 {it['id']} [{it['lens']}] {it['why']}")

if __name__ == "__main__":
    main()
