# 회귀 세트 ch14_v1 (T-075)

본문: T-track 14장 첫 판 final(2026-11-19). 사용자만 잡은 두 줄 — '손님'(1장 은어, 열세 장 쉼), '황한테'(대사에서 성 하나로 부름).
정답지: must_catch.json(문장 1·대사 1).
기준: T01은 문장 독자가 잡았으나 항목 40 예외로 기각된 것 → 예외 축소. T02는 옛 대사 문구 0/1 → check_text W30 1/1(review_out/verifier_notes.md), 보강 전문 대사 ⑧ review_out/전문_대사.md.
돌리기: build_review_inputs.py text.txt --design design.json --out review_in --final → 전문_대사.md를 서브에이전트에 → score_review.py must_catch.json <출력> --lens 대사. 검증기: check_text.py text.txt --design design.json --json → notes를 'note: ' 줄로 저장해 score.
