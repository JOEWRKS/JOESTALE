# Project roadmap — JOESTALE (작가의 어휘로 쓰는 한국어 작문 스킬)

Project scope: 한국어 입력(완성 문장·단순 아이디어·러프한 의견·"써줘" 요청)을 받아 허관 작가의 원칙(정도부사·상태형용사 축소, 사물·행동·감각으로 제시)에 따라 쓰고, 기계 검증(조사·어미·금지어·수식어 비율·대장 일치)과 독립 검수를 거친 본문·설계서·리포트를 내는 Claude Code 스킬 `joestale`.
Product authority: [기획서.md](기획서.md) 3장·3-B·3-C (2026-10-29 사용자 동의). 세부 결정은 JOEFLOW DISCOVER로 보충 예정(FREEZE 생략).
Current stage: Phase 1 complete (2026-10-30). Phase 2 on hold (우리말샘 키), Phase 3 not started (공유마당 텍스트).
Next eligible work: 사용자 작업 2건 — (1) 우리말샘 인증키 발급·약관 확인 → P2-1 실제 응답 검증, (2) 공유마당에서 김유정·이상·현진건 텍스트 확보 → P3-1. 둘 다 없으면 Phase 4 중 스킬 유/무 블라인드 비교(P4-1)는 Phase 3 없이도 예비 실행 가능(임계값 미보정 상태로 표기).
Phase 0 사용자 수락: pending (기술 검증은 complete).
Status words: not started / in progress / verification pending / on hold / complete / removed from scope.

## Stage Phase 0 — 프로토타입 — verification pending

Goal: SKILL.md + 원칙 레퍼런스 + 측정 스크립트로 허관 작가 예문 4쌍의 "전→후" 변환을 재현하고 수치로 확인한다.
Entry condition: 기획서 동의(2026-10-29). 충족.
Completion condition: P0-1~P0-4 모두 통과. 사용자 수락은 별도.

| ID | Required outcome | Status | Check / completion criterion | Evidence or gap |
| --- | --- | --- | --- | --- |
| P0-1 | `skills/joestale/SKILL.md`, `references/principles.md`, `references/scene-design.md`, `references/cliche-list.md` 존재, 5단계 절차와 R1~R6 규칙 명시 | complete | 파일 존재 + SKILL.md가 R1~R6와 0단계(소재 낚기)를 포함 | TASK T-003 |
| P0-2 | `scripts/check_text.py`가 R1(정도부사)·R2(수식어 비율, XSA 포함)·조사 오류(ㄹ받침 버그 수정)·어미 반복을 JSON으로 보고 | complete | 주입 오류 5건 중 5건 검출, 작가 "후" 예문 4개 오탐 0 | TASK T-003, examples/before-after.md |
| P0-3 | 작가 "전" 예문 4개를 스킬 절차로 다시 써서 측정 | complete | 4개 모두 수식어 비율 ≤ 0.18, 정도부사 0, 비시각 감각 ≥ 1 | 비율 0.05~0.09, examples/before-after.md |
| P0-4 | 예문 전후·측정 결과를 `examples/before-after.md`에 기록 | complete | 파일 존재, P0-3 수치 포함 | skills/joestale/examples/before-after.md |

Scope decisions: 우리말샘 API 연동·감각 어휘장·스타일 프로파일은 Phase 1~3(아래)로 분리. none removed.
User acceptance: Phase 0 결과물에 대한 사용자 확인 pending.
Optional/later: 검증 리포트 HTML 뷰(JOEDESIGN 사용). JOEFLOW DISCOVER 등록은 decisions.md로 대체(사용자 지시 2026-10-30 "회색지대 없이 채워줘"). 새 세션에서 joestale 트리거 확인.

## Stage Phase 1 — 레퍼런스 구축 — complete (2026-10-30)

Goal: 감각 어휘장(촉각·청각·후각·미각·온도·신체감각), 클리셰·번역투 목록, 장면 설계 질문지, 결정표 완성.
Entry condition: Phase 0 complete. 충족(기술 검증).
Completion condition: P1-1~P1-4.

| ID | Required outcome | Status | Check / completion criterion | Evidence or gap |
| --- | --- | --- | --- | --- |
| P1-1 | `references/lexicon.json` 감각별 30개 이상, 출처 표기 | complete | `check_text.py --lexicon-stats` senses_min ≥ 30 | 36~50개 (TASK T-004) |
| P1-2 | 정도부사·감정 직설·번역투·AI 관용구 목록을 check_text.py가 파일에서 읽어 사용 | complete | test_check_text.py T1 검출 | TASK T-004 |
| P1-3 | 결정표 `references/decisions.md` (입력 분류·기본값·임계값·실패 동작·출력 형식·파일 위치·묻는 경우) | complete | 문서 존재, SKILL.md가 참조 | TASK T-004 |
| P1-4 | B 유형 실전 예 1건이 절차대로 PASS | complete | examples/worked-B/report.json pass=true | 검수는 DEGRADED(같은 맥락) |

## Stage Phase 2 — 데이터 연결 — on hold

Goal: 우리말샘 view API의 relation_info로 유의어·상하위어 조회, 강제 결합 시드의 "관계 있음" 배제.
Entry condition: 우리말샘 인증키 발급(사용자 작업) + 약관 확인. **미충족.**
Completion condition: P2-1.

| ID | Required outcome | Status | Check / completion criterion | Evidence or gap |
| --- | --- | --- | --- | --- |
| P2-1 | `scripts/lookup_synonyms.py`가 단어 1개에 대해 비슷한말·반대말·상위어를 JSON으로 반환하고 `--related-check`로 관계 유무를 exit 코드로 알림 | verification pending | 실제 API 응답 3건 캡처 | 스크립트 작성됨, 키 없음 → exit 3 확인만 (ISSUES I-1). 응답 JSON 필드명(senseInfo/relation_info)은 문서 기준 추정 |

## Stage Phase 3 — 스타일 프로파일·임계값 보정 — not started

Goal: 저작권 만료 작가(김유정·이상·현진건) 텍스트로 R2 임계값 보정, 작가별 프로파일.
Entry condition: Phase 1 complete, 공유마당 텍스트 확보.
Completion condition: P3-1.

| ID | Required outcome | Status | Check / completion criterion | Evidence or gap |
| --- | --- | --- | --- | --- |
| P3-1 | 작가 3인 이상 수식어 비율·감각어 밀도 측정표와 보정된 임계값 | not started | 측정표 + 보정 근거 | — |

## Stage Phase 4 — 평가 — not started

Goal: 같은 장면을 스킬 유/무로 쓴 뒤 블라인드 비교, description 트리거 정확도 확인.
Entry condition: Phase 1·3 complete.
Completion condition: P4-1.

| ID | Required outcome | Status | Check / completion criterion | Evidence or gap |
| --- | --- | --- | --- | --- |
| P4-1 | 블라인드 비교 결과(사용자 + 가능하면 독자 3인) 기록 | not started | 비교표 | — |
