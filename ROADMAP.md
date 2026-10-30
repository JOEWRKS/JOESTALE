# Project roadmap — JOESTALE (작가의 어휘로 쓰는 한국어 작문 스킬)

Project scope: 한국어 입력(완성 문장·단순 아이디어·러프한 의견·"써줘" 요청)을 받아 허관 작가의 원칙(정도부사·상태형용사 축소, 사물·행동·감각으로 제시)에 따라 쓰고, 기계 검증(조사·어미·금지어·수식어 비율·대장 일치)과 독립 검수를 거친 본문·설계서·리포트를 내는 Claude Code 스킬 `joestale`.
Product authority: [기획서.md](기획서.md) 3장·3-B·3-C (2026-10-29 사용자 동의). 세부 결정은 JOEFLOW DISCOVER로 보충 예정(FREEZE 생략).
Current stage: Phase 3 complete (2026-10-30, 작가 3인 × 1편). Phase 4 평가 진입 가능. 열린 이슈는 I-2·I-4뿐.
Next eligible work: (1) 사용자 수락 판정(Library/user-actions.md 3번) → P4-1 블라인드 비교의 기준점. (2) 작가당 편수 늘리기(동백꽃·날개·운수 좋은 날 외 각 2편) → 작가별 프로파일. (3) D 유형 실전 예를 API 관계 배제를 켜고 재실행해 `candidates[].api` 형식 확정. — (1) 우리말샘 인증키 발급·약관 확인 → P2-1 실제 응답 검증, (2) 공유마당에서 김유정·이상·현진건 텍스트 확보 → P3-1. 둘 다 없으면 Phase 4 중 스킬 유/무 블라인드 비교(P4-1)는 Phase 3 없이도 예비 실행 가능(임계값 미보정 상태로 표기).
Phase 0 사용자 수락: **부분 수락 2026-10-30** — 좋다: 정류장 장면의 공감·연상. 아니다: (1) 전체적으로 길고 묘사 과반복, (2) 배경·시대와 맞지 않는 사물 위험, (3) D 예문의 가난·위축 치환이 감정 방향을 잃음(ISSUES I-12~I-14 → T-011 반영). T-011 규칙 반영 → T-012 v2 재작성 → **2차 피드백(A, 2026-10-30)**: 좋다 1문장(온기를 기다림, 단 간결하게), 아니다 4문장(비직관적 치환·쓰지 않는 연어·한 면만 보여준 성격) → I-15, T-013에서 원칙 서열(직관성 우선)과 패턴 8~11 추가, A v3. **3차 피드백(A v3)**: 난로·장판 사물 과다, 전환 트리거 없음 → I-16, T-014 패턴 12·13, A v4. **4차(A v4)**: 사용자안 채택·분석 → 패턴 10·11·13 보강, 14 추가(T-015). **A 수락(v5 확정, 2026-10-30).** **5차(B v3)**: 공상 과제·대화문 부재·연상 반복 → I-17, T-016 패턴 15~17, 검증기 완화, B v4. **6차(B v4 수락 + 결말 제안)**: 클라이맥스 독백 → T-017 패턴 18, B v5. **B 수락(v5 확정, 2026-10-30 "좋아").** C v4·D v3(T-018) → **7차(C 무기력·D 끝맺음)**: I-18, T-019 패턴 19·20, C v5·D v4. **C 수락(v5 확정)·D 수락(v4 확정, 2026-10-30 "둘 다 수락"). A·B·C·D 네 유형 모두 사용자 수락.**
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
Optional/later: 검증 리포트 HTML 뷰(JOEDESIGN 사용). JOEFLOW DISCOVER 등록은 decisions.md로 대체(사용자 지시 2026-10-30 "회색지대 없이 채워줘"). 새 세션에서 joestale 트리거 확인: 완료(2026-10-30, TASK T-005, D 유형 실전 PASS; 회색지대 ISSUES I-5~I-9 → T-006에서 전부 닫음).

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

## Stage Phase 1.5 — 실전 보강 — complete (2026-10-30, 기술 검증; 사용자 수락 별도)

Goal: 사용자 입력 없이 가능한 보강 5건. 새 규칙으로 A·C 유형 실전 예를 돌려 회색지대를 더 찾고, 검증기·절차·설치를 다듬는다.
Entry condition: Phase 1 complete, I-5~I-9 closed. 충족.
Completion condition: P15-1~P15-5.

| ID | Required outcome | Status | Check / completion criterion | Evidence or gap |
| --- | --- | --- | --- | --- |
| P15-1 | A 유형(완성 글 리라이트)·C 유형(의견→장면) 실전 예 각 1건을 T-006 이후 규칙으로 0~5단계 수행, 서브에이전트 검수 포함 | complete | `examples/worked-A`, `examples/worked-C`의 report.json pass=true, README에 회색지대 목록 | 둘 다 PASS, 검수 2회(haiku), 회색지대 7건 → 전부 반영 (TASK T-007, ISSUES I-10·I-11) |
| P15-2 | check_text.py `--length a-b`: 글자 수(공백 포함·줄바꿈 제외)가 범위 밖이면 위반 아닌 `notes`로 보고 | complete | 회귀 테스트 2건 | test_check_text.py P15-2 2건 OK (TASK T-007) |
| P15-3 | R5 감각 매칭을 형태소 단위로: 1~2글자 어간은 Kiwi 토큰 일치, 3글자 이상·공백 포함 표현은 부분 문자열, 동형이의어는 `형태/태그`로 고정 | complete | "글을 쓰다"가 미각으로 안 잡힘, 작가 예문·실전 예 모두 여전히 PASS | test_check_text.py P15-3 3건 OK, live-test-D·worked-B PASS 유지 |
| P15-4 | SKILL.md 5단계를 "서브에이전트 기본, 불가 시 DEGRADED"로 고정, 검수자에게 주는 설계서 범위 명시 | complete | SKILL.md 본문 확인 | SKILL.md 5단계 절 |
| P15-5 | 설치 절차: `skills/joestale/VERSION`(0.2.0), `scripts/install.ps1`(Check/Apply/Remove, 버전 다르면 blocked), SKILL.md 설치 절 | complete | install.ps1 -Check 출력 JSON | 임시 홈에서 Check ready → Apply current → Check current → Remove removed 확인 (T-007) |

## Stage Phase 2 — 데이터 연결 — complete (2026-10-30)

Goal: 우리말샘 view API의 relation_info로 유의어·상하위어 조회, 강제 결합 시드의 "관계 있음" 배제.
Entry condition: 우리말샘 인증키 발급(사용자 작업) + 약관 확인. 충족(2026-10-30).
Completion condition: P2-1.

| ID | Required outcome | Status | Check / completion criterion | Evidence or gap |
| --- | --- | --- | --- | --- |
| P2-1 | `scripts/lookup_synonyms.py`가 단어 1개에 대해 비슷한말·반대말·상위어를 JSON으로 반환하고 `--related-check`로 관계 유무를 exit 코드로 알림 | complete | 실제 API 응답 3건 캡처 | 경첩·슬픔·바다 응답 확인, 관계 검사 4쌍(소금/설탕·슬픔/기쁨 관계 있음, 우산/치과·구름/중학교 없음) (TASK T-009, Library/research.md) |

## Stage Phase 3 — 스타일 프로파일·임계값 보정 — complete (2026-10-30, 1차)

Goal: 저작권 만료 작가(김유정·이상·현진건) 텍스트로 R2 임계값 보정, 작가별 프로파일.
Entry condition: Phase 1 complete, 공유마당 텍스트 확보. 충족(작가 3인 × 1편, 2026-10-30).
Completion condition: P3-1.

| ID | Required outcome | Status | Check / completion criterion | Evidence or gap |
| --- | --- | --- | --- | --- |
| P3-1 | 작가 3인 이상 수식어 비율·감각어 밀도 측정표와 보정된 임계값 | complete | 측정표 + 보정 근거 | corpus/MEASURE.md(3편), decisions D3 R2 문단 상한 0.30 추가, 고전 기준치 기록 (TASK T-010). 한계: 작가당 1편뿐 → 작가별 프로파일은 편수 늘린 뒤(Optional) |

## Stage Phase 4 — 평가 — not started

Goal: 같은 장면을 스킬 유/무로 쓴 뒤 블라인드 비교, description 트리거 정확도 확인.
Entry condition: Phase 1·3 complete.
Completion condition: P4-1.

| ID | Required outcome | Status | Check / completion criterion | Evidence or gap |
| --- | --- | --- | --- | --- |
| P4-1 | 블라인드 비교 결과(사용자 + 가능하면 독자 3인) 기록 | not started | 비교표 | — |
