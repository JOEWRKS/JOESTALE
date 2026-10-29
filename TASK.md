# Work results

## T-001 / 2026-10-29 / 기획 조사와 실측

Roadmap item: Phase 0 entry condition (기획서 동의).
Result: 허관 작가 Threads 2편 분석, AI 창작 한계·검증기 연구 조사, 한국어 데이터·도구 조사, Kiwi 실측 2건 완료. 사용자 동의.
Changed files: `기획서.md`(기획·조사 전체), `prototype/modifier_ratio.py`(수식어 비율 실측), `prototype/josa_check.py`(조사 오류 정규식 검출).
Check / target / result: 작가 예문 4쌍 수식어 비율 0.17~0.50 → 0.00~0.18; 조사 오류 주입 5건 중 4건 검출, 정상 문장 오탐 0.
Evidence: 기획서.md §1.3, §3-C 표.
Limits: 조사 검사의 ㄹ받침+으로 미검출 1건(ISSUES I-3). Kiwi typo 모드는 문학 어휘를 오타로 오인(ISSUES I-4). 우리말샘 약관 미확인(I-1).
Required specialist verdict: not applicable.
Completion boundaries: 조사·실측 완료 / 스킬 구현 미착수 / 사용자 수락: 기획 동의만.
Related issue / knowledge: ISSUES I-1~I-4, Library/research.md.
Record handoff gap: none.

## T-002 / 2026-10-29 / JOE 도구 최신본 연결과 JOENESS 설정

Roadmap item: 운영 준비(단계 외 승인 작업, 사용자 지시 2026-10-29).
Result: GitHub 최신본(JOENESS 1.1.0, JOEFLOW 1.2.0, JOEDESIGN 1.0.0)을 `D:\JOEWRKS\.local\joe-latest-20261029\`에 클론하고 `D:\JOEWRKS\.claude\skills\`의 정션 3개를 거기로 교체. 이 프로젝트를 Git 초기화하고 JOENESS 5개 문서·Library 작성, 관리 블록 적용.
Changed files: `AGENTS.md`(관리 블록), `ROADMAP.md`, `TASK.md`, `ISSUES.md`, `DESIGN.md`, `Library/research.md`, `.joeness/setup-state.json`.
Check / target / result: project-setup.ps1 -Check → ready(적용 전) / 적용 결과는 아래 상세 보고 참조.
Evidence: project-setup.ps1 JSON 출력(채팅 보고).
Limits: 개인 설치본(`~/.codex/skills`)은 갱신하지 않음(JOENESS 소유권 불일치, ISSUES I-2). 새 세션에서의 지침 전달은 미검증.
Required specialist verdict: not applicable.
Completion boundaries: 연결 적용 / 문서 적합성은 이 기록 기준 / 새 세션 전달 미검증 / 사용자 수락 별도.
Related issue / knowledge: ISSUES I-2.
Record handoff gap: none.

## T-003 / 2026-10-29 / Phase 0 프로토타입과 재현 테스트

Roadmap item: ROADMAP.md P0-1 ~ P0-4.
Result: 스킬 `skills/joestale/` 골격(SKILL.md, references 3개, check_text.py, examples) 작성. 작가 예문 4쌍 재현: "전" 4개 전부 위반, 작가 "후" 4개 오탐 0, 스킬로 다시 쓴 4개 비율 0.05~0.09 통과. 조사 오류 주입 5/5 검출(ㄹ받침 버그 수정).
Changed files: `skills/joestale/SKILL.md`(절차·규칙), `references/principles.md`(원칙·예문·패턴), `references/scene-design.md`(설계서 질문지), `references/cliche-list.md`(금지 목록·검수 체크리스트), `scripts/check_text.py`(R1~R6·G1~G3 검증), `examples/before-after.md`(재현 수치).
Check / target / result: 스크래치 테스트 `p0_test.py` 실행 결과 전부 기대값 일치; CLI 스모크 테스트 exit 1(위반 보고) 정상.
Evidence: examples/before-after.md 표.
Limits: R5 비시각 감각은 키워드 초안(Phase 1 어휘장으로 대체 필요). G3 대장 대조는 문자열 포함 검사만. 5단계 독립 검수는 미실행. 새 세션에서 스킬 트리거 미검증. 사용자 수락 pending.
Required specialist verdict: not applicable.
Completion boundaries: 구현·기술 검증 완료 / 사용자 수락 pending.
Related issue / knowledge: ISSUES I-3(닫힘), I-4.
Record handoff gap: none.

## T-004 / 2026-10-30 / Phase 1 레퍼런스·결정표·검증기 확장, Phase 2 스크립트

Roadmap item: P1-1 ~ P1-4, P2-1(부분).
Result: 결정표(decisions.md D1~D7), lexicon.json(감각 6종 36~50개, 정도부사 30, 감정어 49, 번역투 20), check_text.py를 파일 기반으로 재작성(T1·T2·X1·문장 단위 R2·대화문 R4 예외·G3 미등록 고유명사 추가), 회귀 테스트 18건 ALL OK, B 유형 실전 예 PASS, lookup_synonyms.py 작성(키 없음 → exit 3).
Changed files: `references/decisions.md`, `references/lexicon.json`, `references/reviewer-prompt.md`, `references/design.template.json`, `references/scene-design.md`(문단당 감각), `references/cliche-list.md`(해설용으로 전환), `scripts/check_text.py`, `scripts/test_check_text.py`, `scripts/lookup_synonyms.py`, `examples/worked-B/*`, `SKILL.md`, `.gitattributes`.
Check / target / result: `test_check_text.py` ALL OK; `check_text.py --lexicon-stats` senses_min 36; worked-B 검증 1회 R5 1건 → 국소 수정 → PASS.
Evidence: examples/worked-B/report.json, README.md.
Limits: R6를 "숫자 또는 명사 3개"로 완화(작가 예문 A·B가 숫자 없이 통과해야 함). 우리말샘 응답 필드명 미검증. 5단계 검수는 서브에이전트 없이 DEGRADED. 새 세션 트리거 미검증.
Required specialist verdict: not applicable.
Completion boundaries: 구현·기술 검증 complete / 사용자 수락 pending.
Related issue / knowledge: ISSUES I-1, I-4.
Record handoff gap: none.
