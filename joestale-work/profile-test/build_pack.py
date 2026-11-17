# 블라인드 평가 묶음 생성 (T-060). 실행: PYTHONIOENCODING=utf-8 python build_pack.py
# 장면 2개(S1 초소, S2 배급) × 판 3종(A 한 줄 문단형, B 문장형, C 대조군=일곱 번째 판 원문)에서 같은 장면의 쌍 3개씩 = 6쌍.
# 평가자마다 6쌍을 두 번(전반·후반 순서 뒤집음) = 12판정. 어느 쪽이 어느 판인지는 judge_N/key.json에만 적는다.
import io, json, random, os
HERE = os.path.dirname(os.path.abspath(__file__))
SCENES = {"S1": "초소 인수와 손 베임, 코펠", "S2": "배급 체육관과 계단의 사내"}
VERS = ["A", "B", "C"]
texts = {f"{s}_{v}": io.open(os.path.join(HERE, f"{s}_{v}.txt"), encoding="utf-8").read().strip() for s in SCENES for v in VERS}
pairs = [(s, a, b) for s in SCENES for a, b in [("A", "B"), ("A", "C"), ("B", "C")]]

RUBRIC = """# 블라인드 비교 평가

같은 장면을 쓴 두 글 '가'와 '나'를 읽고 아래 다섯 항목에 답한다. 어느 쪽이 누가 썼는지, 어떤 방식인지 모른다. 추측하지 말고 읽힌 대로 답한다.
글은 한국 웹소설(카카오페이지·문피아 연재) 독자가 휴대폰으로 읽는다고 가정한다. 장면은 어느 장편의 11장 일부이고, 앞 장을 못 읽은 상태다.

항목 (각각 '가' / '나' / '같음' 중 하나):
1. 읽힘: 멈추거나 되돌아가지 않고 끝까지 더 매끄럽게 읽힌 쪽
2. 당김: 다음 줄, 다음 장면이 더 궁금해진 쪽
3. 설명감: 작가가 독자에게 설명하고 있다고 느껴진 문단이 **더 적은** 쪽
4. 인물: 인물이 사람으로 보인 쪽 (속이 보이거나, 행동으로 성격이 드러남)
5. 종합: 카카오페이지에서 다음 화를 넘길 쪽 (둘 다 넘김 / 둘 다 안 넘김도 허용)

각 쌍마다 걸린 문장 하나씩(가·나 각 1문장, 그대로 인용)을 적는다. 좋아서든 걸려서든 한 문장.

결과는 지정된 파일에 아래 표 형식으로만 적는다. 12쌍 전부 채운다. 표 밖 총평은 다섯 줄 이내.

| 쌍 | 읽힘 | 당김 | 설명감 | 인물 | 종합 | 가 인용 | 나 인용 |
|---|---|---|---|---|---|---|---|
| P01 | 가 | 나 | 같음 | 가 | 가 | ... | ... |
"""

for j in (1, 2, 3):
    random.seed(20261115 + j)
    d = os.path.join(HERE, f"judge{j}"); os.makedirs(d, exist_ok=True)
    first = pairs[:]; random.shuffle(first)
    flips = [random.random() < 0.5 for _ in first]
    second = list(zip(first, [not f for f in flips])); random.shuffle(second)
    seq = list(zip(first, flips)) + second
    key, md = {}, [RUBRIC, "\n---\n"]
    for i, ((s, a, b), flip) in enumerate(seq, 1):
        pid = f"P{i:02d}"
        ga, na = (b, a) if flip else (a, b)
        key[pid] = {"scene": s, "가": ga, "나": na}
        md.append(f"\n## {pid}\n")
        for label, v in (("가", ga), ("나", na)):
            md.append(f"\n### {pid} {label}\n\n" + texts[f"{s}_{v}"] + "\n")
    io.open(os.path.join(d, "pairs.md"), "w", encoding="utf-8").write("\n".join(md))
    json.dump(key, io.open(os.path.join(d, "key.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"judge{j}: pairs.md ({sum(1 for _ in seq)}쌍), key.json")
