# Project roadmap — JOESTALE (작가의 어휘로 쓰는 한국어 작문 스킬)

Project scope: 한국어 입력(완성 문장·단순 아이디어·러프한 의견·"써줘" 요청)을 받아 허관 작가의 원칙(정도부사·상태형용사 축소, 사물·행동·감각으로 제시)에 따라 쓰고, 기계 검증(조사·어미·금지어·수식어 비율·대장 일치)과 독립 검수를 거친 본문·설계서·리포트를 내는 Claude Code 스킬 `joestale`.
Product authority: [기획서.md](기획서.md) 3장·3-B·3-C (2026-10-29 사용자 동의). 세부 결정은 JOEFLOW DISCOVER로 보충 예정(FREEZE 생략).
Current stage: Phase 0 — verification pending (P0-1~P0-4 기술 검증 완료, 사용자 확인 대기).
Next eligible work: Phase 0 사용자 확인 → Phase 1 P1-1 감각 어휘장 (R5 키워드 초안 대체).
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
Optional/later: 검증 리포트 HTML 뷰(JOEDESIGN 사용), JOEFLOW DISCOVER로 입력별 기본값 결정 등록.

## Stage Phase 1 — 레퍼런스 구축 — not started

Goal: 감각 어휘장(촉각·청각·후각·미각·온도·통각), 클리셰·번역투 목록, 장면 설계 질문지 완성.
Entry condition: Phase 0 complete.
Completion condition: P1-1~P1-2.

| ID | Required outcome | Status | Check / completion criterion | Evidence or gap |
| --- | --- | --- | --- | --- |
| P1-1 | `references/sensory-lexicon.md` 감각별 동사·명사 각 30개 이상, 출처 표기 | not started | 항목 수 집계 스크립트 | — |
| P1-2 | `references/cliche-list.md` 정도부사·감정 직설·번역투·AI 관용구 목록과 대체 전략 | not started | 목록 존재 + check_text.py가 읽어 사용 | — |

## Stage Phase 2 — 데이터 연결 — not started

Goal: 우리말샘 view API의 relation_info로 유의어·상하위어 조회, 강제 결합 시드의 "관계 있음" 배제.
Entry condition: 우리말샘 인증키 발급(사용자 작업) + 약관 확인.
Completion condition: P2-1.

| ID | Required outcome | Status | Check / completion criterion | Evidence or gap |
| --- | --- | --- | --- | --- |
| P2-1 | `scripts/lookup_synonyms.py`가 단어 1개에 대해 비슷한말·반대말·상위어를 JSON으로 반환 | not started | 실제 API 응답 3건 캡처 | 인증키·약관 미확인 (ISSUES I-1) |

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
