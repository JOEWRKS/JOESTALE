# 회귀 세트 ch13_v1 (T-073)

본문: T-track 13장 첫 판 final(2026-11-18). 사용자(군필)만 잡은 두 줄 — 총번 여덟 자리(총번은 여섯 자리), 민규에게 총을 넘겨 쥐어 보게 함(총기 피탈 방지).
정답지: must_catch.json(이치 2건).
기준: review_out_baseline/전문_이치.md(보강 전 문구) 0/2 → review_out/전문_이치_A·B.md(전문 이치 ⑨ + design domain_rules) 2/2·2/2, review_out/전문_이치_ctrl.md(design_ctrl.json, domain_rules 비움) 2/2.
돌리기: build_review_inputs.py text.txt --design design.json --out review_in --final → 전문_이치.md를 서브에이전트에 → score_review.py must_catch.json <출력>.
