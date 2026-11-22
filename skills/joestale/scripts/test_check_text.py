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
# I-24 R4: 명사 "그립"(수직손잡이)은 감정어가 아님, 형용사 "그리웠다"·명사 "그리움"은 감정어
GRIP = "건우는 수직 그립을 쥐었다. 레일의 그립 자국을 떼고 왔다."
expect("I-24 그립(NNG) R4 오탐 0", not any(v["rule"] == "R4" for v in ct.check(GRIP)["violations"]), [v for v in ct.check(GRIP)["violations"] if v["rule"] == "R4"])
expect("I-24 그리웠다 R4 검출", any(v["rule"] == "R4" for v in ct.check("그는 어머니가 그리웠다.")["violations"]))
expect("I-24 그리움 R4 검출", any(v["rule"] == "R4" for v in ct.check("그리움이 밀려왔다.")["violations"]))
g3 = [v for v in ct.check(DIALOG, DESIGN_BAD)["violations"] if v["rule"] == "G3"]
expect("G3 누락·미등록 검출", any(v.get("missing") == "민재" for v in g3) and any(v.get("form") == "수진" for v in g3), g3)
st = ct.lexicon_stats(); expect("어휘장 감각별 ≥30", st["senses_min"] >= 30, st["senses"])
# I-5: 관형사형 어미 '-는/-은'을 조사로 오인하지 않음, 의성어 1회 NNP를 미등록 이름으로 보지 않음
expect("I-5 관형사형 어미 오탐 없음", not ct.josa_errors("수연은 그날부터 밥을 짓지 않고 한 칸 남은 쌀을 잡는 버릇이 생겼다."))
expect("I-5 조사 오류는 여전히 검출", bool(ct.josa_errors("경첩가 울었다.")))
expect("P15-1 사전 단어 '창가'는 조사 아님", not ct.josa_errors("벽지는 창가 쪽만 햇볕에 바랬다."))
ONO = "밥솥이 치익 소리를 냈다. 수연은 두 번 뚜껑을 눌렀다. 수연은 숨을 참았다."
g3 = [v for v in ct.check(ONO, {"ledger": {"persons": ["수연"], "places": [], "numbers": ["두 번"]}})["violations"] if v["rule"] == "G3"]
expect("I-5 의성어 1회 NNP 오탐 없음", not any(v.get("kind") == "unregistered_NNP" for v in g3), g3)
# I-6: 본문 숫자가 대장에 없으면 검출
NUM = "수연은 둘째 날 아침에 밥솥 액정의 72시간을 보았다. 쌀통에는 한 칸이 남았다."
g3 = [v for v in ct.check(NUM, {"ledger": {"persons": ["수연"], "places": [], "numbers": ["72시간"]}})["violations"] if v.get("kind") == "number_not_in_ledger"]
expect("I-6 대장 누락 숫자 검출(둘째 날), 수량 1(한 칸)은 제외", any("둘째" in v["form"] for v in g3) and not any("한 칸" in v["form"] for v in g3), g3)
g3 = [v for v in ct.check(NUM, {"ledger": {"persons": ["수연"], "places": [], "numbers": ["72시간", "한 칸", "둘째 날"]}})["violations"] if v.get("kind") == "number_not_in_ledger"]
expect("I-6 대장 완비 시 통과", not g3, g3)
expect("seed_objects 30개", len(ct.LEX.get("seed_objects", [])) == 30)
# 원문 유지(keep_original): 직관성 우선 문장은 R1·R2에서 제외
KEEP = "방 안에서는 나프탈렌 냄새가 났다. 공기는 늘 축축하고 무거웠다. 나는 찬 발을 장판에 밀어 넣곤 했다."
r0 = ct.check(KEEP); r1 = ct.check(KEEP, {"keep_original": ["축축하고 무거웠다"]})
expect("keep 없이 R1 검출", any(v["rule"] == "R1" for v in r0["violations"]))
expect("keep 지정 시 R1 제외·kept 보고", not any(v["rule"] == "R1" for v in r1["violations"]) and len(r1["kept_original"]) == 1, r1["kept_original"])
# P3 문단 R2 (고전 p90 0.30)
HEAVY = "매서운 바람이 몹시 차갑게 불었다. 낡고 오래된 문이 시끄럽게 열렸다. 어둡고 축축한 방이 넓게 펼쳐졌다.\n\n민재는 두 번 문을 두드렸다. 쇠 손잡이가 손바닥에 닿았다."
r = ct.check(HEAVY); expect("P3 문단 R2 위반(문단 1만)", [v.get("paragraph") for v in r["violations"] if v["rule"] == "R2" and "paragraph" in v] == [1], [v for v in r["violations"] if v["rule"] == "R2"])
# P15-2 분량 note
expect("P15-2 분량 범위 밖 note", ct.check("민재는 걸었다. 두 번 멈췄다.", length=(400, 700))["notes"] != [])
expect("P15-2 분량 범위 안 note 없음", not any(n.startswith("분량") for n in ct.check("민재는 걸었다. 두 번 멈췄다.", length=(1, 100))["notes"]))
# T-016 전제 감정(premise_emotions): R4만 면제
PREM = "민재는 우산을 털었다. 그토록 그리웠지만 지금은 듣고 싶지 않은 목소리였다. 버스 문이 닫혔다."
r0 = ct.check(PREM); r1 = ct.check(PREM, {"premise_emotions": ["그리웠지만"]})
expect("T-016 premise 없이 R4 검출", any(v["rule"] == "R4" for v in r0["violations"]))
expect("T-016 premise 지정 시 R4 제외·보고", not any(v["rule"] == "R4" for v in r1["violations"]) and len(r1["premise_emotions"]) == 1, r1["violations"])
# T-016 대화문만 있는 문단은 R5·R6 제외, R5는 글 전체 기준 + W3 note
DLG = "민재는 상가 입구에서 우산을 털었다.\n\n\"오랜만이네…. 잘…, 지내?\"\n\n민재는 휜 살을 엄지로 밀어 폈다."
r = ct.check(DLG)
expect("T-016 대화 문단 R6 없음", not any(v["rule"] == "R6" for v in r["violations"]), r["violations"])
expect("T-016 R5 문단별 위반 없음·W3 note", not any(v["rule"] == "R5" for v in r["violations"]) and any(n.startswith("W3") for n in r["notes"]), r["notes"])
expect("T-016 R5 글 전체 없으면 위반", any(v["rule"] == "R5" for v in ct.check("민재는 걸었다. 두 번 멈췄다.")["violations"]))
expect("T-016 목소리는 청각", "hearing" in ct.senses_in("듣고 싶지 않은 목소리였다."))
# T-017 독백(monologue): 대화문처럼 R2 문장·R4 면제, G1 "그사이" 오탐 없음
MONO = "민재는 우산을 폈다. 왜 하필 오늘, 여기서였을까. 그사이 눈앞에서 문이 닫혔다."
r0 = ct.check(MONO); r1 = ct.check(MONO, {"monologue": ["왜 하필"]})
expect("T-017 독백 지정 전 R2 문장 검출", any(v["rule"] == "R2" and "sentence" in v for v in r0["violations"]), r0["violations"])
expect("T-017 독백 지정 시 R2 제외·보고", not any(v["rule"] == "R2" for v in r1["violations"]) and len(r1["monologue"]) == 1, r1["violations"])
expect("T-017 '그사이' G1 오탐 없음", not any(v["rule"] == "G1" for v in r0["violations"]), [v for v in r0["violations"] if v["rule"] == "G1"])
expect("T-017 '손톱로' G1 여전히 검출", any(v["rule"] == "G1" for v in ct.check("손톱로 긁었다.")["violations"]))
# P15-3 감각 매칭 형태소 단위
expect("P15-3 '글을 쓰다'는 미각 아님", "taste" not in ct.senses_in("민재는 편지를 쓰다가 멈췄다."), ct.senses_in("민재는 편지를 쓰다가 멈췄다."))
expect("P15-3 '쓴맛'은 미각", "taste" in ct.senses_in("커피에서 쓴맛이 올라왔다."))
expect("P15-3 '베고'는 촉각", "touch" in ct.senses_in("바람이 뺨을 베고 지나갔다."))

# T-024 (2026-10-31): 패턴 23~27 — R7 사고 동사, R8 문단 첫 문장 상태 요약, G4 수식어 간격, T1 이중 피동, W4 상투 beat
def rules_of(t, design=None):
    return sorted({v["rule"] for v in ct.check(t, design)["violations"]})
FILL = " 컵을 두 번 돌렸다. 창문 세 개가 닫혔다."
expect("R7 생각했다", "R7" in rules_of("민재는 그녀를 생각했다." + FILL))
expect("R7 싶었다", "R7" in rules_of("민재는 집에 가고 싶었다." + FILL))
expect("R7 바라보았다 오탐 없음", "R7" not in rules_of("민재는 물을 바라보았다." + FILL))
expect("R7 대화문 안 제외", "R7" not in rules_of('"나는 네 생각했어."' + FILL))
expect("R7 전제 감정 문장 제외", "R7" not in rules_of("그토록 보고 싶었지만 지금은 아니었다." + FILL, {"premise_emotions": ["보고 싶었지만"]}))
expect("R8 문단 첫 문장 가난했다", "R8" in rules_of("그녀는 가난했다. 집세가 석 달 밀렸다. 고지서 세 통이 쌓였다."))
expect("R8 둘째 문장은 대상 아님", "R8" not in rules_of("집세가 석 달 밀렸다. 그녀는 가난했다. 고지서 세 통이 쌓였다."))
expect("R8 있었다 제외", "R8" not in rules_of("방문은 머리를 숙여야만 드나들 수 있었다. 집세가 석 달 밀렸다. 고지서 세 통이 쌓였다."))
expect("G4 길고 어둡고 축축한 복도", "G4" in rules_of("길고 어둡고 축축한 복도를 지났다." + FILL))
expect("G4 새 빨간 모자", "G4" in rules_of("민재는 새 빨간 모자를 썼다." + FILL))
expect("G4 낯익은 운동화 통과", "G4" not in rules_of("낯익은 운동화가 멈춰 섰다." + FILL))
expect("G4 '가루 하나 없는 매끄러운' 관계절 통과", "G4" not in rules_of("지우개 가루 하나 없는 매끄러운 책상을 닦았다." + FILL))
expect("T1 이중 피동 잊혀진", "T1" in rules_of("잊혀진 계절이 왔다." + FILL))
w4 = ct.check('"응."\n\n민재는 깊은 한숨을 쉬었다.' + FILL)["notes"]
expect("W4 상투 beat note", any(n.startswith("W4") for n in w4), w4)
expect("W4 없음", not any(n.startswith("W4") for n in ct.check("민재는 컵을 두 번 돌렸다. 창문 세 개가 닫혔다.")["notes"]))

# T-050 (2026-11-07): G5 앞 장 문장 재사용, W7 수치 되풀이
PREV = "태석이 쌀죽을 세 몫으로 덜었다. 알루미늄 컵 하나, 뚜껑 하나, 코펠 하나. 민규가 받은 뚜껑을 후후 불었다."
NOW = "태석이 죽을 덜었다. 알루미늄 컵 하나, 코펠 뚜껑 하나, 코펠 하나. 창문 세 개가 닫혔다."
g5 = [v for v in ct.check(NOW, None, None, PREV)["violations"] if v["rule"] == "G5"]
expect("G5 앞 장 문장 재사용", len(g5) == 1 and "알루미늄" in g5[0]["sentence"], g5)
expect("G5 prev 없으면 안 봄", "G5" not in rules_of(NOW))
expect("G5 repeat_ok 면제", not [v for v in ct.check(NOW, {"repeat_ok": ["알루미늄 컵 하나"]}, None, PREV)["violations"] if v["rule"] == "G5"])
expect("G5 다른 문장 오탐 없음", not [v for v in ct.check("민규는 군장을 끌어당겨 지퍼를 올렸다. 창문 세 개가 닫혔다.", None, None, PREV)["violations"] if v["rule"] == "G5"])
w7 = ct.check('"닷새 갈 게 사흘 간 거야."\n\n그는 손을 거두었다.\n\n닷새가 사흘이면 무엇이 달라진 것인가.')["notes"]
expect("W7 수치 되풀이 note", any(n.startswith("W7") and "닷새" in n for n in w7), w7)

# T-051 (2026-11-09): R9 문장 밀도, L1 반영 뒤 분량, W8 긴 문장, W9 대사 서술체 종결
DENSE = "도현은 격리반 침상에 앓아누운 사이 주마다 도는 근무 순번이 넘어가 그의 조가 야간에서 저녁 근무로 옮겨 와 있는 것을 인수 대장의 날짜와 사수의 서명을 번갈아 보고서야 알았다. " * 25
PLAIN = "민규가 컵을 들었다. 창문 세 개가 닫혔다. " * 15
r9 = ct.check(DENSE)
expect("R9 빽빽한 글 위반", "R9" in rules_of(DENSE), r9["density"])
expect("R9 보통 글 통과", "R9" not in rules_of(PLAIN), ct.check(PLAIN)["density"])
expect("R9 서술문 20개 미만이면 안 봄", "R9" not in rules_of(DENSE[:len(DENSE)//5]))
expect("W8 내용어 13개 이상 note", any(n.startswith("W8") for n in r9["notes"]), [n[:40] for n in r9["notes"]])
expect("L1 초고 ×1.05 초과 위반", "L1" in [v["rule"] for v in ct.check(PLAIN, None, None, None, int(len(PLAIN) * 0.8))["violations"]])
expect("L1 초고 이하 통과", "L1" not in [v["rule"] for v in ct.check(PLAIN, None, None, None, len(PLAIN))["violations"]])
w9 = ct.check(chr(10).join(['"저 판은 내가 치운다."', "", "태석이 판을 들었다.", "", '"꿰맬 건 아니다. 세 시간 됐다."']))["notes"]
expect("W9 대사 -ㄴ다 종결 note", any(n.startswith("W9") and "치운다" in n for n in w9), w9)
expect("W9 아니다·됐다는 안 잡음", not any("아니다" in n or "됐다" in n for n in w9 if n.startswith("W9")), w9)


# T-053 (2026-11-10): L1 밀도 조건, W10 하한, W11 끊긴 문장, inference 면제
_d = ct.density_stats(ct.split_sents(PLAIN))
expect("L1 길어졌어도 밀도 그대로면 통과", "L1" not in [v["rule"] for v in ct.check(PLAIN, None, None, None, int(len(PLAIN) * 0.8), _d)["violations"]])
expect("L1 길어지고 빽빽해지면 위반", "L1" in [v["rule"] for v in ct.check(DENSE, None, None, None, int(len(DENSE) * 0.8), _d)["violations"]])
expect("W10 잘게 끊긴 글 note", any(n.startswith("W10") for n in ct.check(PLAIN)["notes"]))
CHOP = "도현은 장갑을 벗어 겨드랑이에 끼웠다. 맨손으로 서명했다. 민규가 구급낭을 열었다. 붕대를 꺼냈다. 태석이 판을 들었다. 둔치로 던졌다."
_c = ct.check(CHOP)
expect("W11 끊긴 문장 3곳 note", any(n.startswith("W11") for n in _c["notes"]) and len(_c["chopped"]) == 3, _c["chopped"])
INF = "태석은 알고 있었으리라고 도현은 생각했다. 도현은 불안했다."
expect("inference 없으면 R4·R7", {"R4", "R7"} <= set(rules_of(INF)), rules_of(INF))
_i = [v["rule"] for v in ct.check(INF, {"inference": ["생각했다", "불안했다"]})["violations"]]
expect("inference 구절은 R3·R4 면제", not (set(_i) & {"R3", "R4", "R7"}), _i)
# T-055 (2026-11-10): G8 인물표 근거, X2 금지 표현, X3 예시 복사, W13 동음이의
PREV = "민규가 말했다. 집사람이랑 돌 지난 애한테 부치려고요. 태석은 묻지 않고 스위치를 내렸다."
DZ = {"characters": {"민규": {"evidence": ["집사람이랑 돌 지난 애한테"]}, "태석": {"evidence": ["묻지 않고 랜턴을 껐다"]}}, "banned_phrases": ["얼마나 더 빨라지는"], "user_examples": ["알면서 모른 척해 준 거겠지. 무른 사람이었다."]}
TX = "도현은 컵을 들었다. 그걸 맞으면 얼마나 더 빨라지는 거지. 태석은 알면서 모른 척해 준 것이다. 쌀은 내일 치로 불려 올게."
_g = ct.check(TX, DZ, None, PREV)
expect("G8 근거 없는 인물표 위반(태석만)", [v.get("who") for v in _g["violations"] if v["rule"] == "G8"] == ["태석"], _g["violations"])
expect("X2 금지 표현 위반", any(v["rule"] == "X2" for v in _g["violations"]))
expect("X3 예시 복사 note", any(n.startswith("X3") for n in _g["notes"]), [n for n in _g["notes"] if n[:2] in ("X3", "W1")])
expect("W13 동음이의 note", any(n.startswith("W13") and "불려 올" in n for n in _g["notes"]))
expect("G8은 --prev 없으면 안 봄", not any(v["rule"] == "G8" for v in ct.check(TX, DZ)["violations"]))

# T-057 (2026-11-12): W14 문단 호흡, W15 대사 종결 단조, W16 발화자 표지, W17 받는 줄, W18 자리만 알리는 문장, W19 모름의 보고문
LONGP = '도현은 컵을 들었다. 민규가 뚜껑을 들었다. 태석이 코펠을 저었다. 창문 세 개가 닫혔다. 바람이 문을 흔들었다.'
expect('W14 5문장 문단 note', any(n.startswith('W14') for n in ct.check(LONGP)['notes']))
expect('W14 3문장 문단 통과', not any(n.startswith('W14') for n in ct.check('도현은 컵을 들었다. 민규가 뚜껑을 들었다. 창문 세 개가 닫혔다.')['notes']))
EFQ = chr(10).join(['"이상 없습니다."', '', '민규가 섰다.', '', '"바람 막는다고요."', '', '태석이 왔다.', '', '"꿰맬 건 아니야."', '', '민규가 앉았다.', '', '"그건 못 들었어요."', '', '태석이 섰다.', '', '"이건 내가 치울게."', '', '민규가 갔다.', '', '"안 팝니다."', '', '태석이 앉았다.', '', '"다 먹으라고 준 겁니다."', '', '민규가 웃었다.', '', '"매주 나온대."', '', '태석이 웃었다.', '', '"세 갑 드릴게요."', '', '민규가 섰다.', '', '"다음 주에 보자."'])
expect('W15 대사 전부 완결 종결 note', any(n.startswith('W15') for n in ct.check(EFQ)['notes']), [n[:30] for n in ct.check(EFQ)['notes']])
MIXQ = EFQ.replace('"꿰맬 건 아니야."', '"꿰맬 건 아니고."').replace('"안 팝니다."', '"쌀을요?"').replace('"매주 나온대."', '"매주."')
expect('W15 섞이면 통과', not any(n.startswith('W15') for n in ct.check(MIXQ)['notes']), [n[:40] for n in ct.check(MIXQ)['notes'] if n.startswith('W15')])
RUN3 = chr(10).join(['컵이 세 개 놓였다.', '', '"이상 없습니다."', '', '"그래."', '', '"탄피는요?"', '', '"몰라."', '', '민규가 섰다.'])
DZ2 = {'ledger': {'persons': ['도현', '민규', '태석']}, 'pov': '도현'}
expect('W16 대사 3연속·이름 없음 note', any(n.startswith('W16') for n in ct.check(RUN3, DZ2)['notes']))
expect('W16 앞 서술에 이름 있으면 통과', not any(n.startswith('W16') for n in ct.check(RUN3.replace('컵이 세 개 놓였다.', '민규가 컵 세 개를 놓았다.'), DZ2)['notes']))
expect('W17 pov 반응 없음 note', any(n.startswith('W17') for n in ct.check(RUN3, DZ2)['notes']))
expect('W17 사이에 pov 줄 있으면 통과', not any(n.startswith('W17') for n in ct.check(RUN3.replace('"탄피는요?"', '도현은 컵을 돌렸다.'), DZ2)['notes']))
expect('W17 pov 없으면 안 봄', not any(n.startswith('W17') for n in ct.check(RUN3)['notes']))
STAY = '사내는 계단 위에 남았다. 창문 세 개가 닫혔다.'
expect('W18 자리만 알리는 문장 note', any(n.startswith('W18') for n in ct.check(STAY)['notes']))
expect('W18 행동 있으면 통과', not any(n.startswith('W18') for n in ct.check('사내는 계단 위에서 다음 사람을 불렀다. 창문 세 개가 닫혔다.')['notes']))
UNK = '다음에는 어디가 달라질지 그는 알지 못했다. 창문 세 개가 닫혔다.'
expect('W19 모름의 보고문 note', any(n.startswith('W19') for n in ct.check(UNK)['notes']))
expect('W19 inference 면제', not any(n.startswith('W19') for n in ct.check(UNK, {'inference': ['알지 못했다']})['notes']))

# T-058 (2026-11-15): W14 기준 3문장·140자, W20 문단 박자, W21 장의 끝, 박자 문단 R6 면제
expect('W14 4문장 문단 note', any(n.startswith('W14') for n in ct.check('도현은 컵을 들었다. 민규가 뚜껑을 들었다. 태석이 코펠을 저었다. 창문 세 개가 닫혔다.')['notes']))
TWO = (chr(10) + chr(10)).join([f'도현은 컵 {i}개를 들었다. 민규가 뚜껑 {i}개를 들었다.' for i in range(2, 24)])
expect('W20 2문장 문단뿐이면 note', any(n.startswith('W20') for n in ct.check(TWO)['notes']), [n[:40] for n in ct.check(TWO)['notes'] if n.startswith('W20')])
ONE = (chr(10) + chr(10)).join([f'도현은 컵 {i}개를 들었다.' for i in range(2, 24)])
expect('W20 1문장 문단이면 통과', not any(n.startswith('W20') for n in ct.check(ONE)['notes']))
expect('W20 서술 문단 20개 미만이면 안 봄', not any(n.startswith('W20') for n in ct.check('도현은 컵을 들었다. 민규가 뚜껑을 들었다.')['notes']))
expect('W21 마지막 문단 3문장 note', any(n.startswith('W21') for n in ct.check('민규가 섰다.' + chr(10) + chr(10) + '도현은 컵을 들었다. 민규가 뚜껑을 들었다. 태석이 코펠을 저었다.')['notes']))
expect('W21 마지막 문단 한 줄이면 통과', not any(n.startswith('W21') for n in ct.check('도현은 컵을 들었다. 민규가 뚜껑을 들었다.' + chr(10) + chr(10) + '도현은 불을 껐다.')['notes']))
expect('R6 박자 문단 면제', not any(v['rule'] == 'R6' and v.get('paragraph') == 2 for v in ct.check('도현은 컵 세 개를 들었다.' + chr(10) + chr(10) + '단련.')['violations']), [v for v in ct.check('도현은 컵 세 개를 들었다.' + chr(10) + chr(10) + '단련.')['violations'] if v['rule'] == 'R6'])
# T-063 패턴 75~83 ----------------------------------------------------------
FRAG_TEXT = "\n\n".join(['"꿰맬 건 아니고. 살갗만."', '"방아쇠 손인데."', '"킬로에 6,000. 깡통은 따로."', '"안 팝니다."', '"혼자 다 먹게?"',
                            '"먹으라고 준 겁니다."', '"담 주에도 여기."', '"얼굴은 왜."', '"손님 얼굴은 외워 두는 게 장사지."', '"두 개요?"', '"그래. 다음 주 거 나오면 또 둘."', '"매주 나온대."'])
r = ct.check(FRAG_TEXT)
expect("W22 토막 대사 note", any(n.startswith("W22") for n in r["notes"]), str([n for n in r["notes"] if n.startswith("W22")])[:120])
FULL_TEXT = "\n\n".join(['"꿰맬 정도는 아니네."', '"총 쏘기 불편해졸네요, 젠장."', '"뭣하면 왼손으로 쏴야지 뭐."', '"안 팝니다."', '"혼자 그걸 다 먹게?"',
                            '"먹으라고 준 겁니다."', '"담 주에도 여기 있을 테니까."', '"얼굴은 왜 외웁니까."', '"얼굴이나 튼 셈 치지."', '"두 개요?"', '"애한테 먹여."', '"매주 나온대."'])
r = ct.check(FULL_TEXT)
expect("W22 어미를 끝까지 말한 대사는 통과", not any(n.startswith("W22") for n in r["notes"]), str([n for n in r["notes"] if n.startswith("W22")])[:120])
r = ct.check("줄이 한 걸음 움직일 때마다 몇 킬로인지가 돌아왔다. 도현은 앞사람의 포대를 눈으로 재었다.")
expect("W23 생각의 명사화 note", any(n.startswith("W23") for n in r["notes"]))
r = ct.check("줄이 한 걸음 움직일 때마다 도현은 앞사람의 포대를 눈으로 재었다.\n\n'고작 몇백 그램 얹어 주는 건 아니겠지.'")
expect("W23 독백으로 쓴 궁금함은 통과", not any(n.startswith("W23") for n in r["notes"]))
r = ct.check("도현은 고개를 들지 않았다.\n\n'싸움 나면 먼저 나가는 몸이다. 그래서 더 받는다. 셈은 맞다.'")
expect("W24 독백 -다 셋 연속·정당화 note", any(n.startswith("W24") for n in r["notes"]), str([n for n in r["notes"] if n.startswith("W24")])[:120])
r = ct.check("도현은 고개를 들지 않았다.\n\n'이게 다 내 거라고?'")
expect("W24 되물음 독백은 통과", not any(n.startswith("W24") for n in r["notes"]))
r = ct.check("도현은 손을 오므렸다. 보이기 싫은 것은 포대가 아니라 손이었다.")
expect("W25 대비 꼴 셈 note", any(n.startswith("W25") for n in r["notes"]))
r = ct.check("민규가 멋쩍은 얼굴로 덮개 끈을 당겨 매 주었다. 민규는 슬픈 얼굴로 끈을 당겼다.")
expect("R4 조연 표정 어절 면제(슬픈 얼굴)", not any(v["rule"] == "R4" for v in r["violations"]), str([v for v in r["violations"] if v["rule"] == "R4"])[:120])
r = ct.check("민규는 슬펐다. 끈을 당겼다.")
expect("R4 시점 인물 감정 명명은 여전히 위반", any(v["rule"] == "R4" for v in r["violations"]))
r = ct.check('"그건 늘 네가 닦았고. 야, 많이 주면 많이 보태고. 식어, 먹어." 태석이 코펠을 내밀었다.')
expect("여러 문장 대사의 둘째 문장은 R1·R2 면제(T-063)", not any(v["rule"] in ("R1", "R2") for v in r["violations"]), str([v for v in r["violations"] if v["rule"] in ("R1", "R2")])[:120])
r = ct.check("도현은 줄에 섰다." + chr(10) + chr(10) + "'더 나오긴 하겠지. 몇백 그램은 아니겠지.'")
expect("W24 독백 같은 어미 연속 note", any("같은 어미" in n for n in r["notes"]))
r = ct.check("도현은 줄에 섰다." + chr(10) + chr(10) + "'더 나오긴 할 텐데. 몇백 그램은 아니겠지.'")
expect("W24 어미가 다르면 통과", not any(n.startswith("W24") for n in r["notes"]))
r = ct.check("도현은 포대를 들었다." + chr(10) + chr(10) + "'두고 가기엔 좀 그렇네. 아까 그 사람도 있고.'", design={"monologue": ["두고 가기엔"]})
expect("여러 문장 독백의 둘째 문장도 독백으로(R2 면제, T-063)", not any(v["rule"] == "R2" for v in r["violations"]), str([v for v in r["violations"] if v["rule"] == "R2"])[:100])
ECHO = '"담배는 됐어. 그냥 가져가."' + chr(10) + chr(10) + '"그냥요?"' + chr(10) + chr(10) + '"그냥. 집에 셋이라며."' + chr(10) + chr(10) + '"다음 주에 또 줄게."' + chr(10) + chr(10) + '"매주요?"' + chr(10) + chr(10) + '"매주 나온대."'
r = ct.check(ECHO)
expect("W26 되받기 쌍 둘 이상 note(T-064)", any(n.startswith("W26") for n in r["notes"]), str([n for n in r["notes"] if n.startswith("W26")])[:160])
r = ct.check('"담배는 됐어. 그냥 가져가."' + chr(10) + chr(10) + '"그냥요?"' + chr(10) + chr(10) + '"애한테나 먹여."' + chr(10) + chr(10) + '"다음 주에도요?"' + chr(10) + chr(10) + '"그건 네가 하는 거 봐서."')
expect("W26 되받기 한 쌍·태도 답은 통과", not any(n.startswith("W26") for n in r["notes"]), str([n for n in r["notes"] if n.startswith("W26")])[:160])
r = ct.check('"이게 한 주 치야?"' + chr(10) + chr(10) + '"그렇다던데요."' + chr(10) + chr(10) + '"저도 맞으면 이만큼 나오는 거죠?"' + chr(10) + chr(10) + '"그렇겠지."')
r = ct.check('"이게 한 주 치야?"' + chr(10) + chr(10) + '"그렇다던데요."' + chr(10) + chr(10) + '"나오는 거죠?"' + chr(10) + chr(10) + '"그렇겠지."' + chr(10) + chr(10) + '"아물었죠?"' + chr(10) + chr(10) + '"그러네."')
expect("W27 '그렇-' 답 셋 이상 note", any(n.startswith("W27") for n in r["notes"]))
r = ct.check('"이게 한 주 치야?"' + chr(10) + chr(10) + '"그렇다던데요."' + chr(10) + chr(10) + '"저도 맞으면 이만큼 나오는 거죠?"' + chr(10) + chr(10) + '"네 순번부터 받고 말해."')
expect("W27 하나는 통과", not any(n.startswith("W27") for n in r["notes"]))
r = ct.check('"이게 한 주 치야?"' + chr(10) + chr(10) + '"그렇대요."' + chr(10) + chr(10) + '"저도 맞으면 이만큼 나오는 거죠?"' + chr(10) + chr(10) + '"그렇겠지."')
expect("W27 둘은 통과(T-066 문턱 2)", not any(n.startswith("W27") for n in r["notes"]))
r = ct.check('"네 쌀도 좀 보태 봐. 끓이는 건 내가 하고."' + chr(10) + chr(10) + '"깡통은 따로 값 매기고."' + chr(10) + chr(10) + '"안 팔면 할 수 없고."' + chr(10) + chr(10) + '"깡통도 하나 따고요."')
expect("W28 대사 끝 연결어미 셋 이상 note", any(n.startswith("W28") for n in r["notes"]), str([n for n in r["notes"] if n.startswith("W28")])[:160])
r = ct.check('"네 쌀도 좀 보태 봐. 끓이는 건 형이 해 줄게."' + chr(10) + chr(10) + '"깡통은 따로 값 매겨 줄게."' + chr(10) + chr(10) + '"안 팔면 할 수 없지."')
expect("W28 어미를 닫으면 통과", not any(n.startswith("W28") for n in r["notes"]), str([n for n in r["notes"] if n.startswith("W28")])[:160])
r = ct.check('"많이 주면 많이 보탤게요."')
expect("W29 대사 안 대칭 note", any(n.startswith("W29") for n in r["notes"]))
DP = {"ledger": {"persons": ["도현", "황", "황 사장", "황대식", "민규"]}}
r = ct.check('"황한테 줄 돈을 황한테 빌렸어?"', design=DP)
expect("W30 대사 안 성+조사 note", any(n.startswith("W30") for n in r["notes"]), str([n for n in r["notes"] if n.startswith("W30")])[:160])
r = ct.check('"황 사장한테 줄 돈을 황 사장한테 빌렸어?"', design=DP)
expect("W30 성+직함은 통과", not any(n.startswith("W30") for n in r["notes"]))
r = ct.check('황은 장부를 덮었다.', design=DP)
expect("W30 서술의 성은 보지 않음", not any(n.startswith("W30") for n in r["notes"]))
r = ct.check('"그녀가 그걸 알고 있었어요."', design=DP)
expect("W30 대사 안 그녀 note", any("그녀" in n for n in r["notes"] if n.startswith("W30")))
r = ct.check('"당신이 뭔데 그래요."', design=DP)
expect("W30 대사 안 당신 note", any("당신" in n for n in r["notes"] if n.startswith("W30")))
r = ct.check('그녀는 차트에 적었다. 그는 총을 들었다.' + chr(10) + chr(10) + '"소대장님이 그랬잖아요. 그 사람 번호래요."', design=DP)
expect("W30 서술의 그녀·대사의 그 사람은 통과", not any(n.startswith("W30") for n in r["notes"]))
r = ct.check('"그렇게 하면 그만이지. 그게 다야."', design=DP)
expect("W30 그렇게·그게는 통과", not any(n.startswith("W30") for n in r["notes"]))
r = ct.check('"주는 거 봐서요."')
expect("W29 대칭 없으면 통과", not any(n.startswith("W29") for n in r["notes"]))
r = ct.check("'……보태라는 말이 고맙네. 이제 얻어먹는 쪽은 아니라는 거니까.'")
expect("W24 까닭 한 줄(거니까)은 정당화 note(T-064)", any(n.startswith("W24") and "거니까" in n for n in r["notes"]), str([n for n in r["notes"] if n.startswith("W24")])[:120])
D10 = {"dialogue_plan": [{"where": "코펠", "lines": [{"who": "태석", "wants": "제안", "gist": "그럼 받아 오면 네 쌀도 좀 보태 봐."}]}]}
r = ct.check('"그럼 받아 오면 네 쌀도 좀 보태 봐. 끓이는 건 형이 해 줄게."', D10)
expect("G10 설계서 요지 그대로 옮김 note", any(n.startswith("G10") for n in r["notes"]))
D10m = {"dialogue_plan": [{"where": "코펠", "lines": [{"who": "태석", "wants": "제안", "move": "농담에 섞어 떠넘기기"}]}]}
r = ct.check('"그럼 받아 오면 네 쌀도 좀 보태 봐. 끓이는 건 형이 해 줄게."', D10m)
expect("G10 move만 적은 설계서는 통과", not any(n.startswith("G10") for n in r["notes"]))
D9 = {"premises": [{"item": "태석이 제 쌀로 셋을 먹인다", "shown_in": "내 쌀 먹는 놈들이 인사가 없어"}]}
r = ct.check('"내 쌀 먹는 놈들이 인사가 없어."\n\n도현은 코펠을 받았다.', design=D9)
expect("G9 shown_in이 본문에 있으면 통과", not any(v["rule"] == "G9" for v in r["violations"]))
r = ct.check("도현은 코펠을 받았다.", design=D9)
expect("G9 shown_in이 본문에 없으면 위반", any(v["rule"] == "G9" for v in r["violations"]))

DT = {"ledger": {"persons": ["도현", "서도현", "유진", "한유진", "정우", "류정우"]}}
r = ct.check('서도현은 처치대에 앉았다. 한유진이 고개를 들었다.' + chr(10) + chr(10) + '"가세요, 중사님."' + chr(10) + chr(10) + '"네, 반장님하고 같이요."', design=DT)
expect("W31 안 묶인 호칭 note(중사님·반장님)", any(n.startswith("W31") and "중사님" in n and "반장님" in n for n in r["notes"]), str([n for n in r["notes"] if n.startswith("W31")])[:160])
r = ct.check('서도현 중사는 처치대에 앉았다. 간호장교 한유진 중위가 고개를 들었다. 복도에서 격리반장 류정우 대위가 유진을 불렀다.' + chr(10) + chr(10) + '"가세요, 중사님."' + chr(10) + chr(10) + '"네, 류 반장님하고 같이요."' + chr(10) + chr(10) + '"중위님이 지키십니까."', design=DT)
expect("W31 서술에서 묶인 호칭은 통과", not any(n.startswith("W31") for n in r["notes"]), str([n for n in r["notes"] if n.startswith("W31")])[:160])
r = ct.check('도현은 걸었다.' + chr(10) + chr(10) + '"한 중위님, 가세요."', design=DT)
expect("W31 대사 안의 성+직책만으로는 안 묶임(서술이 묶어야 함)", any(n.startswith("W31") for n in r["notes"]))
r = ct.check('"네, 반장님하고 같이요."' + chr(10) + chr(10) + '복도에서 반장 류정우가 유진을 불렀다.', design=DT)
expect("W31 대사 뒤에 묶인 것은 늦음(note)", any(n.startswith("W31") and "반장님" in n for n in r["notes"]))
DT3 = {"pov": "도현", "ledger": {"persons": ["도현", "서도현", "유진", "한유진"]}, "characters": {"유진": {"speech": {"address": "도현에게 '중사님', 정우에게 '반장님'"}}}}
r = ct.check('서도현은 처치대에 앉았다.' + chr(10) + chr(10) + '"가세요, 중사님."' + chr(10) + chr(10) + '"네, 반장님하고 같이요."', design=DT3)
expect("W31 시점 인물을 부르는 호칭은 면제(characters.speech.address), 남의 호칭은 그대로", any(n.startswith("W31") and "반장님" in n and "중사님" not in n for n in r["notes"]), str([n for n in r["notes"] if n.startswith("W31")])[:160])
expect("W31 면제 본문은 W34도 없음", not any(n.startswith("W34") for n in r["notes"]))
r = ct.check('"아닙니다. 어제 아침에 제가 창고에 갔습니다."' + chr(10) + chr(10) + '"가서 뭘 하셨는데요."' + chr(10) + chr(10) + '"그 번호, 손대지 않겟다는 약속을 받았습니다."')
expect("W36 사다리 물음 note(가서 뭘 하셨는데요)", any(n.startswith("W36") and "가서" in n for n in r["notes"]), str([n for n in r["notes"] if n.startswith("W36")])[:160])
r = ct.check('"아닙니다. 어제 아침에 제가 창고에 갔습니다."' + chr(10) + chr(10) + '가을이 손잡이를 놓았다가 다시 쥐었다.' + chr(10) + chr(10) + '"가서 뭘 하셨는데요."' + chr(10) + chr(10) + '"약속을 받았습니다."')
expect("W36 사이에 서술이 있으면 안 셈", not any(n.startswith("W36") for n in r["notes"]))
r = ct.check('"황 사장이 보냈어요?"' + chr(10) + chr(10) + '"아닙니다. 제가 가서 약속을 받았습니다."' + chr(10) + chr(10) + '"그 사람이 그냥 미뤄 줄 리는 없고요. 뭘 줬어요?"')
expect("W36 제 사정에서 나온 긴 물음은 안 셈", not any(n.startswith("W36") for n in r["notes"]))
r = ct.check('"점만 찍는 겁니다."' + chr(10) + chr(10) + '"가짜를 가려 주는 겁니다."' + chr(10) + chr(10) + '도현은 걸었다.')
expect("W37 평서 '-는 겁니다' 둘이면 note", any(n.startswith("W37") and "찍는 겁니다" in n for n in r["notes"]), str([n for n in r["notes"] if n.startswith("W37")])[:160])
r = ct.check('"점만 찍었습니다."' + chr(10) + chr(10) + '"뭘 보시는 거예요?"' + chr(10) + chr(10) + '"복사해 온 겁니다."' + chr(10) + chr(10) + '"가려 주는 겁니다."' + chr(10) + chr(10) + '도현은 걸었다.')
expect("W37 물음·과거 관형형은 안 셈(평서 하나는 통과)", not any(n.startswith("W37") for n in r["notes"]))
r = ct.check('"황 사장이 쥐고 있다는 전화번호 일로 왔습니다."' + chr(10) + chr(10) + '"그 번호 일을 어떻게 아세요."')
expect("W38 명사+일 포괄 지칭 note(번호 일)", any(n.startswith("W38") and "번호 일" in n for n in r["notes"]), str([n for n in r["notes"] if n.startswith("W38")])[:160])
r = ct.check('"무슨 일로 오셨어요."' + chr(10) + chr(10) + '"집안 일이 있어서요. 오늘 일은 끝났습니다."' + chr(10) + chr(10) + '"큰일 났네요. 남의 사람 일에 왜 나서나."')
expect("W38 무슨 일·집안 일·오늘 일·큰일은 안 셈", not any(n.startswith("W38") for n in r["notes"]), str([n for n in r["notes"] if n.startswith("W38")])[:160])
r = ct.check('번호 일로 왔다고 도현은 말하지 않았다. 그 일을 어떻게 아는지도.')
expect("W38 서술은 안 셈", not any(n.startswith("W38") for n in r["notes"]))
DT2 = {"ledger": {"persons": ["도현", "서도현", "중사님", "중위님"]}}
r = ct.check('서도현은 걸었다.' + chr(10) + chr(10) + '"가세요, 중사님."', design=DT2)
expect("W31 대장의 호칭 항목은 이름이 아님", any(n.startswith("W31") and "중사님" in n for n in r["notes"]))
r = ct.check("지난주 바늘 자리는 멍도 없이 살빛이었다. 지난번 자리보다 한 마디 위였다. 지난주 것도 있었다. 도현은 걸었다.")
expect("W33 묘사의 지난주·지난번은 안 셈", not any(n.startswith("W33") for n in r["notes"]))

D32 = {"premises": [{"item": "10장 모릅니다", "shown_in": "x"}, {"item": "9장 네 명", "shown_in": "x"}, {"item": "4장 옆 침대", "shown_in": "x"}, {"item": "8장 양식", "shown_in": "x"}]}
r = ct.check("도현은 걸었다.", design=D32)
expect("W32 앞 장 전제 넷은 note", any(n.startswith("W32") for n in r["notes"]))
D32b = {"premises": D32["premises"][:3]}
r = ct.check("도현은 걸었다.", design=D32b)
expect("W32 셋은 통과", not any(n.startswith("W32") for n in r["notes"]))
r = ct.check("열흘 전 퇴실 서류 앞에서 그는 모른다고 했다. 작년 가을에 문자가 왔다. 넉 달 동안 등 뒤에서 잤다. 도현은 걸었다.")
expect("W33 앞 일 요약문 셋은 note", any(n.startswith("W33") for n in r["notes"]))
r = ct.check("열흘 전 퇴실 서류 앞에서 그는 모른다고 했다. 도현은 걸었다.")
expect("W33 하나는 통과", not any(n.startswith("W33") for n in r["notes"]))

D34 = {"pov": "도현", "ledger": {"persons": ["도현", "서도현", "서도현 중사", "민규", "박민규"]}}
r = ct.check("서도현 중사는 총을 병기고에 넣고 나왔다. 거점 문 앞에 관측병 박민규가 서 있었다.", design=D34)
expect("W34 시점 인물 풀네임+계급 서술은 note", any(n.startswith("W34") and "서도현 중사" in n for n in r["notes"]), str([n for n in r["notes"] if n.startswith("W34")])[:120])
r = ct.check("서도현은 총을 병기고에 넣고 나왔다. 거점 문 앞에 관측병 박민규가 서 있었다.", design=D34)
expect("W34 풀네임만(계급 없음)은 통과", not any(n.startswith("W34") for n in r["notes"]))
r = ct.check("도현은 걸었다." + chr(10) + chr(10) + '"서도현 중사 맞지?"', design=D34)
expect("W34 대사 안은 안 셈", not any(n.startswith("W34") for n in r["notes"]))
r = ct.check('"그거 봐 주면 3월 9일까진 그 번호 안 건드려."' + chr(10) + chr(10) + '"검문 시간 못 드립니다."')
expect("W35 명사+안/못 조사 떼기는 note", any(n.startswith("W35") and "번호 안 건드려" in n for n in r["notes"]), str([n for n in r["notes"] if n.startswith("W35")])[:140])
r = ct.check('"그 번호는 안 건드린다고 약속하지."' + chr(10) + chr(10) + '"검문 시간은 못 드립니다."' + chr(10) + chr(10) + '"말 한 번 안 해 본 사람 일에 왜 나서나."' + chr(10) + chr(10) + '"나도 못 가렸어. 이제 안 베여. 그거 안 팔아? 주시면 안 돼요? 아직 못 드세요."')
expect("W35 조사·수량·부사·대명사·-면 뒤는 안 셈", not any(n.startswith("W35") for n in r["notes"]), str([n for n in r["notes"] if n.startswith("W35")])[:140])
r = ct.check('"그 번호 안 건드린다고 약속하지."')
expect("W35 안/못 뒤가 이어지면 안 셈", not any(n.startswith("W35") for n in r["notes"]))
r = ct.check("그 번호 안 건드린다. 검문 시간 못 준다.")
expect("W35 서술은 안 셈", not any(n.startswith("W35") for n in r["notes"]))

print("\n" + ("ALL OK" if not fails else f"FAILED: {fails}"))
sys.exit(1 if fails else 0)
