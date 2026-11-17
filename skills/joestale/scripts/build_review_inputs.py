# -*- coding: utf-8 -*-
"""5단계·5-B단계 검수자 입력 파일을 reviewer-prompt.md에서 만들어 낸다.

python build_review_inputs.py final.txt --design design.json --out review_in/ [--memory reader_memory.md] [--short]

만드는 것: 눈_가.md ~ 눈_아.md (항목 검수, 눈마다 항목과 설계서 블록만), 문장독자.md, 플랫폼독자.md, (--memory가 있으면) 연결독자.md.
--final은 마지막 패스용: 전문_대사·독백·이치·이야기·인물.md + 문장독자.md + 플랫폼독자.md (T-065).
검수자마다 파일 하나만 주면 된다. --short는 1,000자 미만 글용으로 가·다·마 세 눈만 만든다.
"""
import argparse, json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
PROMPT = HERE.parent / "references" / "reviewer-prompt.md"

LENSES = {   # reviewer-prompt.md "검수자 한 명에 한 가지 눈" 표와 같아야 한다
    "가": ([1, 2, 3, 6, 14, 15, 22, 39], []),
    "나": ([4, 8, 33, 34, 35, 36, 40, 41, 49], ["ledger", "setting", "assumptions", "continuity"]),
    "다": ([5, 9, 11, 12, 16, 17, 21, 30], ["banned_targets", "assumptions"]),
    "라": ([7, 10, 13, 25, 31], ["setting"]),
    "마": ([18, 19, 20, 28, 29, 37, 38], ["setting", "assumptions", "structure"]),
    "바": ([42, 43, 44, 45, 50], ["structure", "premises", "bridges", "exchanges", "inference", "banned_phrases"]),   # T-053: 이야기(반응·닫기·다리·주고받기·짐작)
    "사": ([46, 47, 48, 55], ["characters", "dialogue_plan", "exchanges"]),   # T-063: 55 사람의 말(전보문·토막·장면 결)   # T-055: 인물(성격·사정·아는 것과 대사, 처지 누락, 대화 사슬)
    "아": ([51, 52, 53, 54, 56, 57], ["timeline", "scenes", "plants", "hooks", "characters", "pov", "premises", "exchanges"]),   # T-063: 56 주는 쪽의 전제, 57 독백·셈의 결   # T-057: 장면·납득(심은 문장의 자리, 행동의 납득·주인공의 품, 시간표·비중, 입말·받는 줄)
}
MAX_ITEMS = 9
SPECIALISTS = {   # reviewer-prompt.md "전문 검수자" 표와 같아야 한다 (T-065)
    "대사": ["characters", "dialogue_plan", "exchanges"],
    "독백": ["pov", "monologue", "scenes"],
    "이치": ["ledger", "setting", "timeline", "assumptions", "continuity"],
    "이야기": ["scenes", "structure", "premises", "hooks", "plants"],
    "인물": ["characters", "pov", "exchanges"],
}

def fenced(text, start):
    a = text.index("```", start) + 3
    b = text.index("```", a)
    return text[a:b].strip()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("text"); ap.add_argument("--design"); ap.add_argument("--out", required=True)
    ap.add_argument("--memory"); ap.add_argument("--short", action="store_true")
    ap.add_argument("--final", action="store_true", help="마지막 패스: 전문 검수자 5 + 문장·플랫폼 독자(T-065)")
    a = ap.parse_args()
    r = PROMPT.read_text(encoding="utf-8").replace("\r\n", "\n")
    body = pathlib.Path(a.text).read_text(encoding="utf-8").strip()
    design = json.loads(pathlib.Path(a.design).read_text(encoding="utf-8")) if a.design else {}
    out = pathlib.Path(a.out); out.mkdir(parents=True, exist_ok=True)

    if a.final:
        for name, keys in SPECIALISTS.items():
            t = fenced(r, r.index(f"### 전문 검수자: {name}"))
            sub = {k: design[k] for k in keys if k in design}
            t = t.replace("{본문}", body).replace("{설계서}", json.dumps(sub, ensure_ascii=False, indent=1) if sub else "(없음)")
            (out / f"전문_{name}.md").write_text(t, encoding="utf-8", newline="\n")
        i = r.index("### 문장 독자"); pf = r.index("### 플랫폼 독자")
        (out / "문장독자.md").write_text(fenced(r, i).replace("{본문}", body), encoding="utf-8", newline="\n")
        (out / "플랫폼독자.md").write_text(fenced(r, pf).replace("{본문}", body), encoding="utf-8", newline="\n")
        print("만든 파일:", ", ".join(sorted(p.name for p in out.iterdir())))
        return

    block = fenced(r, r.index("| 가. 문장"))
    lines = block.split("\n")
    none = "(이 눈에는 주지 않는다)"
    for name, (nums, keys) in LENSES.items():
        assert len(nums) <= MAX_ITEMS, f"눈 {name}: 항목 {len(nums)}개 (상한 {MAX_ITEMS})"
        if a.short and name not in ("가", "다", "마"):
            continue
        kept = [l for l in lines if not (re.match(r"(\d+)\. ", l) and int(re.match(r"(\d+)\. ", l).group(1)) not in nums)]
        t = "\n".join(kept).replace("{이 눈의 항목 번호}", ", ".join(map(str, nums)) + "번")
        sub = {k: design[k] for k in keys if k in design and k != "continuity"}
        cont = json.dumps(design["continuity"], ensure_ascii=False, indent=1) if "continuity" in keys and design.get("continuity") else none
        t = t.replace("{본문}", body).replace("{설계서}", json.dumps(sub, ensure_ascii=False, indent=1) if sub else none)
        t = re.sub(r"\{continuity — .*?\}", lambda m: cont, t, flags=re.S)
        (out / f"눈_{name}.md").write_text(t, encoding="utf-8", newline="\n")

    i = r.index("### 문장 독자"); j = r.index("### 연결 독자"); k = r.index("### 처리 규칙 (첫 읽기)"); pf = r.index("### 플랫폼 독자")
    (out / "문장독자.md").write_text(fenced(r, i).replace("{본문}", body), encoding="utf-8", newline="\n")
    (out / "플랫폼독자.md").write_text(fenced(r, pf).replace("{본문}", body), encoding="utf-8", newline="\n")
    if a.memory:
        mem = pathlib.Path(a.memory).read_text(encoding="utf-8").strip()
        (out / "연결독자.md").write_text(fenced(r, j).replace("{reader_memory.md}", mem).replace("{본문}", body), encoding="utf-8", newline="\n")
    print("만든 파일:", ", ".join(sorted(p.name for p in out.iterdir())))

if __name__ == "__main__":
    main()
