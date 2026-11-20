# 회귀 세트 ch15_v1 (T-078)

본문: T-track 15장 첫 판 final(2026-11-19). 사용자 판독(2026-11-20) 세 자리 — 대사의 호칭(중위님·반장님)이 누구인지 모름, 앞 장 사건 요약으로 짐작할 것이 많음, 독백 'P-16은 지금 어디서 자나'가 어거지(살았는지를 먼저 묻는 단계).
정답지: must_catch.json(검증기 2·독백 1).
기준: 셋 다 검수자가 앞 패스에서 짚었다(인물 ②·문장 C·플랫폼 P6, 전문 독백 × 두 번). 작성자가 '연재 전제'·'설계 훅'으로 기각한 것이 뿌리 → 처리 규칙(앞 장 전제 기각 상한 셋, 독백 관문)과 검증기 W31~W33. 옛 검증기 0/3(review_out_baseline/verifier_notes.md) → 새 검증기 2 notes(review_out/verifier_notes.md): W31 대사의 호칭 3개가 이 장 안에서 사람과 묶이지 않음: 중위님, 반장님, 중사님 (첫 등장 서술에 이름+직책 한 번 — | W32 앞 장 전제 6개(기준 3): 10장 퇴실 서류 앞에서 유진이 P를 물었고 / 9장 열에 들떠 들은 '네 명 올렸는데 
돌리기: check_text.py text.txt --design design.json --json → notes를 'note: ' 줄로 저장해 score_review.py must_catch.json <파일> --lens 검증기. 독백은 build_review_inputs.py --final → 전문_독백.md를 서브에이전트에 → --lens 독백.
