"""check_text.py 회귀 테스트. 실행: PYTHONIOENCODING=utf-8 python test_check_text.py  (전부 OK면 exit 0)"""
import sys, json, pathlib, importlib.util
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass
here = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("ct", here / "check_text.py")
ct = importlib.util.module_from_spec(spec); spec.loader.exec_module(ct)

BEFORE = ["낡고 오래된 문이 시끄럽게 열렸다.", "매서운 바람이 몹시 차갑게 불었다.",
          "그는 매우 꼼꼼하고 예민한 성격이었다.", "그녀는 지독한 가난에 시달리며 늘 위축되어 있었다."]
AUTHOR = ["문손잡이를 당기자 녹슨 경첩이 쇳소리를 뱉어냈다.",
          "창틈으로 밀려든 바람이 뺨을 베고 지나갔다. 난로 곁에 둔 물그릇 표면에 살얼음이 덮였다.",
          "그는 책상 위 연필 세 자루의 끄트머리가 일직선이 되도록 나란히 맞췄다. 지우개 가루 하나 없는 매끄러운 책상 표면을 손끝으로 두 번 쓸어내린 뒤에야 비로소 의자에 등을 기댔다.",
          "마트 마감 시간이 되자 그녀는 반값 할인 스티커가 세 겹으로 덧붙여진 식빵을 집어 들었다. 딱딱해진 빵 가장자리를 손톱으로 꾹 눌러본 뒤, 타인의 시선을 피하듯 카트 맨 밑바닥으로 소리 없이 밀어 넣었다."]
MINE = ["손잡이를 돌리자 문짝이 틀에 걸려 멈췄다. 어깨로 두 번 밀고 나서야 돌쩌귀가 끼익 소리를 끌며 돌아갔고, 문틈에서 먼지 뭉치가 발등으로 떨어졌다.",
        "버스 정류장 유리벽 틈으로 바람이 들이쳤다. 귀 끝이 먼저 저리더니, 장갑 낀 손가락 세 개가 굳어 교통카드를 두 번 떨어뜨렸다.",
        "그는 회의실에 들어오면 의자를 테이블 선에 맞춰 밀어 넣고 나서야 앉았다. 옆자리 동료가 볼펜을 딸깍거리자 세 번째 소리에서 그의 손이 멈췄고, 회의록 여백에 같은 글자를 네 번 겹쳐 썼다.",
        "그녀는 전기요금 고지서를 뜯지 않고 서랍 맨 아래 칸에 넣었다. 편의점 삼각김밥 두 개를 사며 계산대에 동전을 열두 개 세어 올렸고, 뒤에 선 사람의 발소리가 가까워지자 남은 하나를 도로 선반에 올려놓았다."]
JOSA = ["경첩가 쇳소리를 뱉어냈다.", "바람를 맞으며 뺨이 베였다.", "그녀은 식빵을 집어 들었다.", "손톱로 눌렀다.", "서울으로 갔다."]
AI_TEXT = ("민재는 그녀에 대해 생각했다. 마치 시간이 멈춘 듯했다. 깊은 한숨을 쉬었다. 사랑, 우정, 그리고 희망이 떠올랐다.\n\n"
           "민재는 걸었다. 민재는 또 걸었다.\n\nx민재는 멈췄다.")
DIALOG = "\"나 너무 슬퍼.\" 수진이 말했다. 수진은 컵을 두 번 돌렸다. 컵 가장자리에 입술 자국 세 개가 남았다."
DESIGN = {"ledger": {"persons": ["수진"], "places": [], "numbers": ["두 번", "세 개"]}}
DESIGN_BAD = {"ledger": {"persons": ["민재"], "places": [], "numbers": ["두 번"]}}

fails = []
def expect(name, cond, detail=""):
    print(("OK   " if cond else "FAIL ") + name, detail)
    if not cond: fails.append(name)

for i, t in enumerate(BEFORE):
    r = ct.check(t); expect(f"before-{i} 위반", not r["pass"], sorted({v['rule'] for v in r['violations']}))
for i, t in enumerate(AUTHOR):
    r = ct.check(t); rules = {v["rule"] for v in r["violations"]}
    expect(f"author-{i} X1 외 오탐 0", rules <= {"X1"}, (r["modifier"]["ratio"], sorted(rules)))
for i, t in enumerate(MINE):
    r = ct.check(t); expect(f"mine-{i} PASS", r["pass"], (r["modifier"]["ratio"], r["senses"]))
hits = sum(bool(ct.josa_errors(t)) for t in JOSA); expect("josa 5/5", hits == 5, hits)
r = ct.check(AI_TEXT); rules = {v["rule"] for v in r["violations"]}
expect("AI 관용구 T1", "T1" in rules, r["translationese_counts"])
expect("문단 첫 어절 T2", "T2" in rules, r["para_first"])
expect("R4 대화문 예외", "R4" not in {v["rule"] for v in ct.check(DIALOG, DESIGN)["violations"]})
expect("G3 대장 일치 통과", not any(v["rule"] == "G3" for v in ct.check(DIALOG, DESIGN)["violations"]))
g3 = [v for v in ct.check(DIALOG, DESIGN_BAD)["violations"] if v["rule"] == "G3"]
expect("G3 누락·미등록 검출", any(v.get("missing") == "민재" for v in g3) and any(v.get("form") == "수진" for v in g3), g3)
st = ct.lexicon_stats(); expect("어휘장 감각별 ≥30", st["senses_min"] >= 30, st["senses"])
print("\n" + ("ALL OK" if not fails else f"FAILED: {fails}"))
sys.exit(1 if fails else 0)
