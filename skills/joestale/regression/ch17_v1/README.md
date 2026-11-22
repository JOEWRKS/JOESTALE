# ch17_v1 — 17장 「지도」 첫 판, 사용자 판독 1차 4건 (T-082)

text.txt = ch17_v2/final_v1.txt(2,583자, 2026-11-21 판독 전 판). design.json = 같은 설계서(user_examples는 collect_examples.py로 일곱 패스의 문장 독자 고친 문장에서 모은 87 토막).

채점: `python ../../scripts/check_text.py text.txt --design design.json --json`의 notes를 review_out/verifier_notes.md에 `note: ` 접두로 쓰고 `python ../../scripts/score_review.py must_catch.json review_out/verifier_notes.md --lens 검증기`.

- 새 검증기(W36 사다리 물음·W37 풀이 어미·W38 '명사+일'·X3 with 모은 토막): 4/4.
- 옛 검증기(T-081 시점): W36~W38이 없고 user_examples가 비어 있어 X3도 침묵 — 0/4(review_out_baseline/verifier_notes.md는 그 시점 check.final.json의 notes).

뿌리: 넷 다 검수자가 짚었다 — 흐름 ③ '독자 대신 묻는 질문'(1회차·마지막 패스), 전문 대사 ⑧·문장 독자 C('번호 일'), 문장 독자 A·플랫폼('점만 두는 겁니다 / 보고서 꼴'), 문장 독자 A('점을 안으로 넣었다' → 검수자 예시 '점이 안쪽으로 들어갔다'를 그대로 옮김). 작성자가 사다리를 늘려 쓰고(토막 지적만 받음), 어미를 두고 내용만 바꾸고, 검수 예시를 옮겼다.
