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

## T-027 / 2026-10-31 / round2 v3: 9차 피드백 수용(A 전환·C 상식 행동·D 양가 독백)

Roadmap item: Phase 0 user acceptance(round2).
Result: 검증기 — 문단 R2도 keep_original·monologue 문장 제외(테스트 61 OK). 사용자 지시 "원칙과 정면으로 대치하는 부분 없으면 객관적으로 수용" → 세 지적 모두 기존 원칙과 정합(28 표지 뒤 전환, 21 기대되지 않은 부정의 반례, 30 동기 독백)이라 수용. **정정(같은 날)**: D 수정의 본질은 양가 감정이 아니라 "묘사만 이어진 문단에 속마음·대사로 직관적 표현을 넣는다"는 일반 원칙 → 패턴 32 신설, 검수 32, decisions W5, 검증기 W5 note(대사·독백 없는 서술문 5개 연속) + 테스트 3(ALL OK). A v3(219자)·C v3(288자)·D v3(465자), B 확정(287자). principles 28·21·30 보강, 검수 28 보강.
Changed files: round2/A·C·D (v2 보관), README, references/principles.md·reviewer-prompt.md, scripts/check_text.py·test_check_text.py.
Check / target / result: 4편 PASS(C의 "급히 다른 불마저" 문장은 수식어 3개라 keep_original). 수락본 A~C PASS 유지.
Evidence: round2/README.md v3.
Limits: 사용자 제시 문장이라 검수 생략. A 분량 초과 note 유지. W5는 수락본 D(8개 연속)에도 떠서 위반이 아닌 note로 둠. 커밋 안 함.
Required specialist verdict: not applicable.
Completion boundaries: B 수락. A·C·D v3 판정 pending.
Related issue / knowledge: I-19, 패턴 21·28·30.
Record handoff gap: none.

## T-026 / 2026-10-31 / round2 v2: 8차 피드백 → 패턴 28~31, 네 편 재작성

Roadmap item: Phase 0 user acceptance 연장(round2).
Result: ISSUES I-19. principles 패턴 28(첫 문장 신체 표지·분위기 시간어)·29(고조는 점층·의성어·더듬는 대사·짧은 독백)·30(동기 감정은 숫자 든 독백 + 외부 호출 + 판정 독백; 패턴 18 자리 확장)·31(소개 대사·관계어, 공간 종류, 처지에 맞는 사물, 흔한 행동) + 검사법, 13 보강(상태 전환 트리거). reviewer 31항목. decisions 4줄 + D4 setting 포함. SKILL 서열 문단. 검증기: 독백만 있는 문단 R6 제외(+테스트 1, 60 OK). round2 A~D v2(사용자 제시 문장 채택) 검증 PASS, 검수 17건 → 8건 처리, D 재검수 1회.
Changed files: references/principles.md·reviewer-prompt.md·decisions.md, SKILL.md, scripts/check_text.py·test_check_text.py, ISSUES.md, joestale-work/round2/* (v1 보관).
Check / target / result: 4편 PASS. 테스트 ALL OK(60).
Evidence: round2/README.md v2 표, 각 review.md.
Limits: A는 분량 기본값(82~184) 초과 215자(사용자 제시 독백·호출 채택, note). A "망했다"·현재형 "나지 않는다"는 사용자 문장이라 검수 지적 미처리. 패턴 28~31은 검수자만 봄(기계 검사 없음). 커밋 안 함.
Required specialist verdict: not applicable.
Completion boundaries: round2 v2 사용자 판정 pending.
Related issue / knowledge: ISSUES I-19, 패턴 28~31.
Record handoff gap: none.

## T-025 / 2026-10-31 / round2: 새 소재 4편 생성(패턴 1~27 일반화 확인)

Roadmap item: Next eligible work (0). 사용자 "네가 골라서 써".
Result: `joestale-work/round2/{A,B,C,D}/` — A 면접 긴장 리라이트(144자), B 첫 월급 굴비 선물(279자), C 혼자 사는 밤(226자), D 비 오는 밤 강아지 산책(303자). 전부 설계서 → 초고 → 검증 PASS → haiku 검수(27항목) → 국소 수정 → 재검증 PASS. C는 처리 3건이라 재검수 1회(상한).
Changed files: round2/* (input·design·draft·final·report·review_input·review·README).
Check / target / result: 4편 PASS. 검수 지적 합계 17건 → 처리 12건. 새 규칙 R7·R8·G4·W4는 초고에서 0건(초고 단계에서 이미 지켜짐).
Evidence: 각 report.json, review.md, README.md 표.
Limits: 검수자 haiku. R8이 절 안의 상태 요약("문 밖은 조용했고")을 못 잡음(검수가 잡음). D 결합 시드 우산은 API 미조회(LLM 판단). 사용자 판정 pending. 커밋 안 함.
Required specialist verdict: not applicable.
Completion boundaries: 사용자 판정 → 수락이면 examples/로 승격, 아니면 피드백 → 패턴 보강.
Related issue / knowledge: 패턴 1~27, T-024.
Record handoff gap: none.

## T-024 / 2026-10-31 / 방법론 조사 추천안 반영: 패턴 23~27, 검증기 R7·R8·G4·W4·T1 확장

Roadmap item: T-023 후속. 사용자 "추천안만 반영"(A1·A3·A4·A6·A9).
Result: principles 패턴 23(사고 동사 풀기)·24(문단 첫 문장 상태 요약 금지)·25(beat는 인물만의 작은 동작)·26(수식어 간격)·27(이중 피동·"에 의해" 금지) + 검사법. reviewer 27항목. decisions D3에 R7·R8·G4·W4 행, T1 비고. SKILL 규칙 요약·서열 문단. 검증기: `thought_verbs()` R7(NNG+XSV·VV·VX 싶, 대화문·독백·원문 유지·전제 감정 제외), `first_sentence_state()` R8(문단 첫 문장 서술어 VA·XSA, 있다·없다 제외), `stacked_modifiers()` G4(한 명사 앞 상태 관형어·관형사 ≥2, 있는·없는 제외), W4 note(`weak_beats`), lexicon 이중 피동 패턴 확장(잊혀지·보여지 …, max 0). lexicon에 `thought_verbs`·`weak_beats`·`g4_mm_ignore`.
Changed files: `references/principles.md`·`reviewer-prompt.md`·`decisions.md`·`lexicon.json`, `SKILL.md`, `scripts/check_text.py`·`test_check_text.py`.
Check / target / result: test_check_text.py 59 OK(+15: R7 5, R8 3, G4 4, T1 1, W4 2). 수락본 A v5·B v5·C v5·D v4 전부 PASS 유지. 오탐 수정 2건: R7 "바라보다"(startswith → 완전 일치), G4 작가 예문 "가루 하나 없는 매끄러운 책상"(관계절 없는·있는 제외).
Evidence: 테스트 출력, 수락본 4건 PASS.
Limits: R7 목록은 보수적(알다·보다 제외). R8은 형용사 술어만 보며 "성격이었다"류는 R3이 맡음. W4는 note라 "고개를 끄덕였다"(B 수락본)는 목록 밖. A2·A5·A7·A8·A10은 미채택(사용자 결정). 커밋 안 함.
Required specialist verdict: not applicable.
Completion boundaries: 새 규칙이 새 글에서 어떻게 작동하는지는 다음 생성에서 확인.
Related issue / knowledge: T-023 보고서 A1·A3·A4·A6·A9, principles 패턴 23~27.
Record handoff gap: none.

## T-023 / 2026-10-31 / 글쓰기 방법론 조사(deep-research): 채용·보강·충돌 후보

Roadmap item: 사용자 요청 "글쓰기 방법론에 대해 면밀히 조사해서 채용할 방식과 보강할 방식이 있는지 찾기".
Result: 조사 노트 5건(국내 작가 문장론, 한국 교재·웹소설 작법, 해외 고전 문장론, 해외 현대 작법서, 실증 연구·한국어 특수성) → 보고서 `joestale-work/reports/소설 문장 기법 방법론 조사.md`. 패턴 1~22 ↔ 출처 이론 대조표(19개는 외부 이론에 뿌리, 10·11·7/16 검사법은 고유). 채용 후보 A1~A10(사고 동사 풀기, 심리적 거리 단계, 문단 첫 문장 감정 요약 금지, beat 규칙, 엇나간 응답, 수식어 간격, 서술자의 한숨 금지, 쉼표·연결어미 지표, 이중 피동·'-에 의해' 규범, 섬광·감각적 선택성). 보강 B1~B12(수식어 판정 3문, 실증 각주, Burroway significant detail, 주어 생략 실험, Maass inner mode, 부정문 조건 등). 충돌·약한 근거 C1~C12(감정 명명 전면 금지·혼자 있는 인물 금지·웹소설 깊은 3인칭은 채택 안 함; 구체어 선호 전제는 Maslej 2021이 역방향; 능동태·단문 직역 주의; 과격 격언 원문 단서; 수식어 밀도→질 저하 직접 실증 없음).
Changed files: `joestale-work/research_notes/소설 문장 기법 방법론 조사/*.md`(5), `joestale-work/reports/소설 문장 기법 방법론 조사.md`.
Check / target / result: 보고서 BLUF + 대조표 + 후보표 3개. 스킬 파일은 아직 바꾸지 않음.
Evidence: 보고서 각 행의 URL.
Limits: 인용 다수가 2차 자료(블로그·서평·AI 요약). 『문장강화』 7강·Strunk 1959판·체호프 고리키 서한·Stein liposuction 장 원문 미열람. 실증은 영어·독일어 소표본. 커밋 안 함.
Required specialist verdict: not applicable.
Completion boundaries: 사용자가 A1~A10 중 채용할 것을 고르면 T-024에서 원칙·검증기·설계서에 반영.
Related issue / knowledge: principles 패턴 1~22, negation-check.md.
Record handoff gap: none.

## T-022 / 2026-10-31 / 패턴 21 검증(코퍼스 분류 + 쌍 블라인드), 1원칙에 "묘사를 늘리지 않음" 명시

Roadmap item: Phase 4 — 규칙 검증. 사용자 요청 "문구처럼 고치면 효과가 있는지도 면밀하고 넓게 검증해".
Result: `joestale-work/blind-P4-1/negation-check.md`. (1) 고전 3편 부정문 비율 23~28%, 샘플 60문장 중 상태·습관 설명 17·반전 9·기타 30(분류자 2인 일치 71/75). (2) 긍정/부정 12쌍 판정자 3인: 상태 쌍은 구체 사물을 든 긍정형만 이김(5쌍 3:0), 사용자 제안 두 문장("같은 채널만", "콧바람이 닿지 않도록")은 0:3 패배. 반전 쌍은 "장면이 그려지는가" 기준에서 행동형 긍정이 10:2. 결론: 이기는 것은 긍정형이 아니라 구체형. 패턴 21을 "상태 설명에서는 구체성이 긍정/부정보다 먼저, 부정문 자체는 결함 아님, 구체 사물을 든 긍정형이 있을 때만 교체, 반전·무반응·불능 부정은 유지"로 확정. 검수 21·decisions·SKILL 동기화. 사용자 명시(2026-10-31) "묘사를 늘리라는 게 아니라 수식어를 감각 묘사로 대체, 더 간결해야"를 SKILL 1원칙과 principles 묘사의 양 절에 적음.
Changed files: `joestale-work/blind-P4-1/negation_extract.py`·`neg_*.json`·`neg_sample.txt`·`judge*.txt`·`judge*.key.json`·`judge*.result.txt`·`class*.txt`·`pair_tally.json`·`negation-check.md`, `references/principles.md`·`reviewer-prompt.md`·`decisions.md`, `SKILL.md`.
Check / target / result: 분류 일치 71/75. 쌍 판정 36표 집계 pair_tally.json. test_check_text.py ALL OK(검증기 미변경).
Evidence: negation-check.md 표 3개.
Limits: 판정자·분류자는 LLM(haiku 2·sonnet 1), 사람 독자 아님. 쌍 12개는 작성자가 만듦. 판정 문구("떠올렸다가 지울 것 없이")가 부정형에 불리했을 수 있음. 반전 쌍 결과는 극적 효과를 묻지 않은 것이라 패턴 18·19를 뒤집는 근거로 쓰지 않음. 커밋 안 함.
Required specialist verdict: not applicable.
Completion boundaries: 패턴 21 문구 확정. 사용자가 제안했던 두 문장의 판정 결과는 보고만 함.
Related issue / knowledge: 패턴 21, T-021.
Record handoff gap: none.

## T-021 / 2026-10-31 / P4-1 판정 기록, 기준본 결함 → 패턴 21·22

Roadmap item: Phase 4 P4-1 닫기.
Result: pairs.md "판정" 절(항목별 선택·요지·결과, 기준본 결함 → 원칙 대응표). 스킬본 선호 3/4, 동률 1/4. principles 패턴 21(상태는 긍정·목적 서술, 부정문은 세계의 무반응에만), 22(한 장면 한 자리, 장소 분산 금지, 등장 자리의 사건 논리), 13 보강(결말 행동 변화의 원인), 19 보강(난감한 사건 뒤 반응 한 문장), 검사법 21·22. reviewer 22항목(8 물리 현실성, 9 양방향 신체 표현, 11 부수 연상, 21·22 신설). decisions 2줄, SKILL 서열 문단.
Changed files: `joestale-work/blind-P4-1/pairs.md`, `references/principles.md`·`reviewer-prompt.md`·`decisions.md`, `SKILL.md`, ROADMAP.
Check / target / result: 수락된 A~D 본문은 바꾸지 않음(스킬본이 전부 선호·동률). 새 패턴은 검수자 항목이며 기계 검사 없음. test_check_text.py 변경 없음.
Evidence: pairs.md 판정 절·대응표.
Limits: 판정자 1인(사용자). A·B 스킬본에 판정자 제안 문장이 있어 완전 블라인드 아님. 기준본 1회 생성. 외부 독자 3인 미실시. 커밋 안 함.
Required specialist verdict: not applicable.
Completion boundaries: P4-1 complete(1인). 외부 독자 비교는 Optional.
Related issue / knowledge: ROADMAP P4-1, principles 패턴 21·22.
Record handoff gap: none.

## T-020 / 2026-10-30 / P4-1 블라인드 비교표 준비, D candidates[].api 기록

Roadmap item: Phase 4 P4-1, Next eligible work (3).
Result: `joestale-work/blind-P4-1/`: baseline/A~D.txt(스킬·파일·지침 없이 서브에이전트가 같은 입력·분량으로 쓴 기준본), skill/A~D.txt(수락된 A v5·B v5·C v5·D v4 복사), build_pairs.py(가/나 무작위 배치 + check_text 수치), pairs.md(판정용), key.json(정답, 판정 전 열지 않음). D design.json `seed.candidates[]`에 `api` 필드: 전기밥솥 ↔ 장례식장·수능·횡단보도 모두 exit 0(관계 없음).
Changed files: `joestale-work/blind-P4-1/*`, `joestale-work/live-test-D/design.json`, ROADMAP.
Check / target / result: pairs.md 4항목 8본문 생성. 기계 수치(설계서 없이): 수식어 비율 스킬 0.03~0.13 / 기준본 0.07~0.19, 감각 종류 스킬 2~3 / 기준본 1~5. D PASS 유지.
Evidence: pairs.md 하단 표, key.json.
Limits: 기준본도 같은 모델이 썼으므로 "스킬 없음"은 "원칙 지침 없음"이지 다른 작가가 아니다. 기준본은 1회 생성(변동 미측정). 외부 독자 3인은 없음. 작성자(이 세션)는 key를 봤으므로 블라인드는 사용자에게만 성립. 커밋 안 함.
Required specialist verdict: not applicable.
Completion boundaries: 사용자 판정 완료(2026-10-31) → pairs.md "판정" 절, P4-1 닫음(T-021).
Related issue / knowledge: ROADMAP P4-1, 기획서 165행.
Record handoff gap: none.

## T-019 / 2026-10-30 / C v5·D v4: 패턴 19(저항과 무반응)·20(결말 신체 반응)

Roadmap item: Phase 0 User acceptance — 7차 피드백(C 무기력, D 끝맺음) 반영.
Result: principles 패턴 19·20 + 검사법, decisions 2줄, scene-design `closing_body`, reviewer 19·20(20항목), SKILL 서열 문단. C v5(381자): "내릴 역은 아니었다" 뒤 저항 대사 + 무반응 대비 문장 + 뻗은 손. D v4(361자): 마지막 문장 "수연의 뺨을 타고 그제야 못다 흘린 눈물이 내렸다".
Changed files: `references/principles.md`·`decisions.md`·`reviewer-prompt.md`·`scene-design.md`, `SKILL.md`, `examples/worked-C/final.txt`·`design.json`·`report.json`·README(v4 보관), `joestale-work/live-test-D/final.txt`·`design.json`·`report.json`·README(v3 보관), `재판정-v2.md`, ISSUES I-18, ROADMAP.
Check / target / result: C·D PASS. 검수 C 10건 → 0건 처리(사용자 수락·제시 문장), D 9건 → 1건 처리(못다 흘린). 재검수 없음(각 2건 이하). test_check_text.py 변경 없음(검증기 미변경).
Evidence: 각 report.json, README v5/v4, 재판정-v2.md.
Limits: 패턴 19·20은 검수자만 본다(기계 검사 없음). "나직한 외침"과 "!"의 세기 불일치, 두 시간 부사(나서야·그제야) 겹침은 검수 지적이나 사용자 제시 구절이라 유지. 커밋 안 함.
Required specialist verdict: not applicable.
Completion boundaries: C v5·D v4 사용자 수락(2026-10-30 "둘 다 수락, 커밋"). 커밋 완료.
Related issue / knowledge: ISSUES I-18, principles 패턴 19·20.
Record handoff gap: none.

## T-018 / 2026-10-30 / C v4·D v3: 패턴 15~18 적용 재작성

Roadmap item: Phase 0 User acceptance — C·D 재제시.
Result: C v4(278자): 수족관 연상 삭제(seed.used false), 대사 1줄 + 반응 문장, 결말에 손해 사실("내릴 역은 아니었다"). D v3(332자): 조립 세부 삭제, 클라이맥스 독백 1문장, 검수로 용어 3건 수정(부의 봉투 위 종이 → 사망진단서, 잠금 손잡이 → 뚜껑 손잡이를 열림으로, 사흘/72시간 중복 → 발인을 마치고).
Changed files: `examples/worked-C/final.txt`·`design.json`·`report.json`·README(v3 보관), `joestale-work/live-test-D/final.txt`·`design.json`·`report.json`·README(v2 보관), `재판정-v2.md`.
Check / target / result: C·D PASS. 검수 C 5건 → 1건 처리, D 9건 → 3건 처리 → 재검수 1회(결과는 live-test-D/README v3).
Evidence: 각 report.json, 재판정-v2.md C·D.
Limits: D의 "솥을 엎고 수도를 틂"이 청소로 읽힐 위험은 검수자 지적, 사용자 판정 대상. D는 1인 장면이라 대사 없음.
Required specialist verdict: not applicable.
Completion boundaries: C v4·D v3 사용자 판정 pending.
Related issue / knowledge: ISSUES I-17, principles 패턴 15~18.
Record handoff gap: none.

## T-017 / 2026-10-30 / B v5: 클라이맥스 독백(패턴 18), 검증기 monologue·G1 "그사이" 오탐

Roadmap item: Phase 0 User acceptance — B 방향 수락("그래 좋다"), 문구 1건 수정("기운" → "휜").
Result: 사용자 제안(결말을 극적으로: 우산을 펴는 사이 문이 닫힘, 차마 세우지 못함, "왜 하필 지금")을 패턴 18로 규칙화: 불가역 사실 뒤에 독백 두 문장까지(질문형·불능 표현), 결론 감정은 쓰지 않고 행동으로 돌아옴. 검증기: 설계서 `monologue` 문장을 대화문처럼 처리·보고, G1 오탐("그사이")을 어간/조사 경계의 토큰 경계 유무로 제외. decisions 독백 행, 검수 18번, SKILL·scene-design 반영. B v5 329자 PASS.
Changed files: `references/principles.md`(패턴 18, 분석 사례 2 결말 행), `decisions.md`, `reviewer-prompt.md`, `scene-design.md`, `SKILL.md`, `scripts/check_text.py`·`test_check_text.py`(+4건), `examples/worked-B/*`(v4 보관), `재판정-v2.md`.
Check / target / result: test ALL OK(48건). B v5 PASS, A·C·D PASS 유지. 검수 7건 → 처리 0건(worked-B/README v5에 이유).
Evidence: worked-B/report.json, 재판정-v2.md B.
Limits: B 결말 문장 대부분이 사용자 제시문. "독백 한 자리"는 기계 검사 없음(검수 18만).
Required specialist verdict: not applicable.
Completion boundaries: B v5 사용자 수락(2026-10-30) / C·D 패턴 15~18 미적용.
Related issue / knowledge: ISSUES I-17, principles 패턴 18.
Record handoff gap: none.

## T-016 / 2026-10-30 / 5차 피드백(B v3): 패턴 15~17, 검증기 전제 감정·대화 문단·R5 완화, B v4

Roadmap item: Phase 0 User acceptance — B 재제시.
Result: 사용자 피드백(공상 과제·대화문 부재·연상 반복)을 패턴 15(행동 시간순, 한 문장 한 행동, 상태는 수식어 하나로 압축 가능), 16(대사 한 줄 + 반응 문장, 전제 감정은 쓰고 결론 감정은 독자 몫), 17(연상은 상태당 1회, 결합 시드 미사용 허용, 설명 없는 세부 숫자 금지)로 규칙화. 검증기: 설계서 `premise_emotions` 문장은 R4 면제·보고, 대화문만 있는 문단은 R2·R5·R6 제외, R5는 글 전체 기준으로 완화(문단별은 W3 note), 청각에 목소리·말소리. decisions: B·C 200~500자, 대화문 사용 조건, 묘사 순서, 결합 시드 조건. 검수 항목 15~17. B v4(248자, 대사 2줄, 치과·숫자 삭제) PASS. 검수 지적 6건 → 처리 1건(버스 등장 근거).
Changed files: `references/principles.md`(패턴 15~17, 분석 사례 2), `decisions.md`, `reviewer-prompt.md`, `scene-design.md`, `design.template.json`, `lexicon.json`, `SKILL.md`, `scripts/check_text.py`·`test_check_text.py`(+7건), `examples/worked-B/*`(v3 보관), `재판정-v2.md`.
Check / target / result: test ALL OK(44건). B v4 PASS, A·C·D 여전히 PASS(R5 완화로 위반 감소 없음, 전부 0건 유지). 검수(haiku) 결과는 worked-B/README v4.
Evidence: worked-B/report.json, 재판정-v2.md B.
Limits: B·C 하한 200자는 내가 정한 기본값(사용자 확인 필요). 대화문 삽입 여부·"공상 과제" 판정은 기계 검사 없음(검수 15·16만). B v4의 대사·반응 문장은 사용자 제시문을 거의 그대로 채택.
Required specialist verdict: not applicable.
Completion boundaries: B v4 pending / C·D는 패턴 15~17 미적용(재작성 필요 여부 사용자 판단).
Related issue / knowledge: ISSUES I-17, principles 분석 사례 2.
Record handoff gap: none.

## T-015 / 2026-10-30 / 4차 피드백: 사용자안 분석으로 패턴 10·11·13 보강, 14 추가, A v5 확정, B v3

Roadmap item: Phase 0 User acceptance — A 확정, B 재제시.
Result: 사용자 제시 문장("아깝다고 고집부리며 틀지도 않던 장판을 내가 오면 켜곤 하셨다. 나는 그제야 미지근해진 이불 밑에 발을 밀어 넣곤 했다")이 스킬 v4보다 나은 이유를 분석해 규칙화: 패턴 10(양면성 = 한 행동의 평소/예외 대비, 예외 조건이 감정), 11(장면 전체 같은 상, 존대 어미로 관계), 13(트리거는 사물의 상태 변화, 사건을 요약하는 형용사는 남김), 14(행위 주체 전환 1회, 마음은 질문 보고가 아니라 행동). A v5 = 사용자안 확정(146자 PASS, 원문 유지 1문장). B v3: 사물 3(우산살·운동화 끈·버스), 주체 전환 최소, 상태 변화 트리거(손을 떼자 → 기움), 308자 PASS.
Changed files: `references/principles.md`(패턴 10·11·13·14, 분석 사례 표), `lexicon.json`(촉각: 엄지·검지·손목·발바닥), `examples/worked-A/final.txt`·`design.json`·`report.json`·README, `worked-B/final.txt`·`design.json`·`report.json`·README, `재판정-v2.md`.
Check / target / result: test ALL OK. A·B PASS.
Evidence: principles.md 분석 사례 표, 재판정-v2.md.
Limits: A 확정 문장은 사용자안이라 스킬 자력 생성 증거가 아님. B v3·C·D는 재판정 pending. "주체 전환 횟수"는 기계 검사 없음(검수 14번 미추가 → 다음 보강).
Required specialist verdict: not applicable.
Completion boundaries: A 수락 complete / B·C·D pending.
Related issue / knowledge: ISSUES I-15·I-16, principles 분석 사례.
Record handoff gap: none.

## T-014 / 2026-10-30 / 3차 피드백 반영: 사물 경제·전환 트리거 (I-16)

Roadmap item: Phase 0 User acceptance 3차 → 원칙 보강.
Result: 패턴 12(핵심 사물 2~3개, 한 사물 다역), 13(새 사물은 앞 문장의 원인·연속으로만) 추가. 설계서 objects ≤ 3·전환마다 트리거, 검수 13번, 검증기 W2 note. 연결·습관 부사 6개 허용 목록 추가(그제야·곧잘 등은 패턴 11·13의 도구). A v4: 난로 삭제, 장판 하나가 고집(아깝다고 화냄)·외로움(춥지 않은지 물어옴)·편안함(그제야 켜진 장판에 발을 넣곤 함)을 들게 함.
Changed files: `references/principles.md`·`decisions.md`·`reviewer-prompt.md`·`scene-design.md`·`lexicon.json`, `scripts/check_text.py`(W2), `examples/worked-A/final.txt`·`design.json`·`report.json`·README, `재판정-v2.md`, ISSUES I-16.
Check / target / result: test ALL OK. A v4 155자 PASS(원문 유지 1문장, 비율 허용 부사 반영 후).
Evidence: worked-A/README v4.
Limits: 사물 수는 설계서 기준으로만 세고 본문에서 자동 추출하지 않음(검수 13번 의존). 재판정 pending.
Required specialist verdict: not applicable.
Completion boundaries: 반영 complete / 사용자 재판정 pending.
Related issue / knowledge: ISSUES I-16.
Record handoff gap: none.

## T-013 / 2026-10-30 / 2차 피드백 반영: 직관성 우선 원칙 (I-15)

Roadmap item: Phase 0 User acceptance 2차 → 원칙 보강.
Result: 원칙 서열을 "직관성 > 감정의 방향 > 수식어 제거"로 명시하고 패턴 8(인식 경로·한 단계 연상), 9(감각 전환은 실제 쓰는 연어로), 10(이중 성격은 대비문), 11(습관 "~곤 했다") 추가. 검증기에 `keep_original`(원문 유지 문장을 R1~R4에서 제외, 리포트 표시). 설계서에 인식 경로 칸, 검수 11·12번. A v3: 사용자 제시 문장 채택("머리를 숙여야만", "눅눅한 나무와 나프탈렌 냄새", "화를 내면서도 춥지는 않은지", "찬 발을 … 밀어 넣곤 했다"), "공기는 늘 축축하고 무거웠다"는 원문 유지. C "손가락이 두 개씩 밀려 내려갔다" → "손이 한 뼘씩 아래로 밀렸다". B·D는 패턴 8·9로 점검, 변경 없음.
Changed files: `references/principles.md`·`decisions.md`·`reviewer-prompt.md`·`scene-design.md`, `scripts/check_text.py`(keep_original)·`test_check_text.py`(+2, 35건), `SKILL.md`, `examples/worked-A/final.txt`·`design.json`·`report.json`·README, `worked-C/final.txt`·`design.json`·`report.json`, `examples/재판정-v2.md`, ISSUES I-15.
Check / target / result: test 35건 ALL OK. A 159자 PASS(원문 유지 1문장), C·B·D PASS.
Evidence: worked-A/README v3, 재판정-v2.md.
Limits: "실제로 쓰는 말인가"(연어)는 기계가 못 재고 검수 11번에 의존. A v3 문장 4개 중 3개는 사용자 제시안을 그대로 채택한 것이라 스킬의 자력 생성 증거는 아님. 재판정 pending.
Required specialist verdict: not applicable.
Completion boundaries: 규칙·예문 반영 complete / 사용자 재판정 pending.
Related issue / knowledge: ISSUES I-15, principles 패턴 8~11.
Record handoff gap: none.

## T-012 / 2026-10-30 / 실전 예 4건 v2 재작성 (재판정용)

Roadmap item: Phase 0 User acceptance 재판정 준비.
Result: B·C·D·A를 T-011 규칙으로 다시 씀. 분량 B 305·C 311·D 331·A 167자(전부 기준 안), 상태당 2문장, 설계서에 배경·방향·오독 위험 추가. 서브에이전트(haiku) 검수 1차 지적 4건(B 대장, C 방향·반복, A 방향) → 전부 처리, 2차 지적 1건(B 작가 구절 변형) → 처리. 4건 최종 PASS.
Changed files: 각 폴더 `final.txt`·`design.json`·`report.json`·README v2 절, 이전 판 `final.v1.txt`·`design.v1.json` 보존.
Check / target / result: check_text.py --length 4건 PASS. 검수 2회.
Evidence: 각 README v2 절, report.json.
Limits: 검증기가 문맥에 따라 "땀내"를 땀+내로 쪼개 감각을 놓침(2글자 어휘장 한계, C README). 사용자 재판정 pending.
Required specialist verdict: not applicable.
Completion boundaries: 재작성·검수 complete / 사용자 재판정 pending.
Related issue / knowledge: ISSUES I-12~I-14, principles 패턴 7.
Record handoff gap: none.

## T-011 / 2026-10-30 / 사용자 1차 수락 피드백 반영 (I-12~I-14)

Roadmap item: Phase 0 User acceptance(부분 수락) → 규칙 보강.
Result: 피드백 3건을 규칙으로 변환. (1) 길이·반복: 한 치환 목표당 문장 ≤ 2, 문단 ≤ 4문장, 분량 기본값 축소(A 0.8~1.8배, B·C 300~500, D 600~1,000), 검증기 W1 note. (2) 배경·시대 정합성: 설계서 `setting` 필수, 시대 중립 사물 목록 30개, 검수 8번. (3) 감정의 방향: principles 패턴 7, 설계서 치환 계획에 방향·문장 수·오독 가능성, 검수 9·10번. 기각된 D 예문을 방향 표지를 넣어 다시 써서 PASS(0.04, 165자).
Changed files: `references/decisions.md`·`principles.md`·`scene-design.md`·`reviewer-prompt.md`·`design.template.json`·`lexicon.json`(seed_objects_era_neutral), `scripts/check_text.py`(W1), `SKILL.md`, `examples/before-after.md`, ISSUES I-12~I-14, ROADMAP User acceptance.
Check / target / result: test_check_text.py 33건 ALL OK. 새 D 예문 PASS. 기존 실전 예 4건은 새 분량 기준에서 note(길이 초과)가 뜨지만 위반 아님.
Evidence: examples/before-after.md D 2차.
Limits: 감정의 방향·배경 정합성·묘사 과잉은 기계가 못 재고 검수자(LLM)가 맡음. 기존 실전 예(B·C·D·A)는 새 분량·반복 상한으로 다시 쓰지 않음 → 재판정 시 새로 돌릴 것. 사용자 재판정 pending.
Required specialist verdict: not applicable.
Completion boundaries: 규칙 반영 complete / 사용자 재판정 pending.
Related issue / knowledge: ISSUES I-12~I-14.
Record handoff gap: none.

## T-010 / 2026-10-30 / 코퍼스 측정과 임계값 보정 (Phase 3, P3-1)

Roadmap item: ROADMAP.md P3-1.
Result: 사용자가 넣은 공유마당 zip 3개(동백꽃·날개·운수 좋은 날)를 extracted/로 풀고 줄바꿈을 정규화해 측정. 전체 수식어 비율 0.18/0.20/0.18, 문단 p50 0.17~0.19, p90 0.27~0.30, 정도부사 4~11/1k, 감정어 2~6/1k, 비시각 감각 문단 23~27%. R2에 문단 상한 0.30(고전 p90) 추가, 글 전체 0.18 유지(고전 평균 수준, 스킬 산출물 0.02~0.09). R1·R5는 고전보다 엄격한 작가 원칙임을 결정표에 명시.
Changed files: `scripts/measure_corpus.py`(신규), `scripts/check_text.py`(문단 R2), `scripts/test_check_text.py`(+1), `references/decisions.md`, `corpus/SOURCES.md`·`MEASURE.md`·`measure.json`·`*/extracted/*.txt`, `.gitignore`(zip/pdf/hwp 제외), ROADMAP Phase 3 complete, Library/user-actions.md 2번 완료.
Check / target / result: measure_corpus.py 3편 정상, test_check_text.py 33건 ALL OK, 기존 실전 예 4건 PASS 유지(확인 결과는 아래 상세).
Evidence: corpus/MEASURE.md, corpus/measure.json.
Limits: 작가당 1편이라 작가별 프로파일은 미작성. 1930년대 표기(얼리었다, 뺏다 등)로 Kiwi 태깅 오차 → 수치는 참고치. 공유마당 출처 메모의 라이선스 표기란이 비어 있어 "만료저작물"은 사이트 분류 기준(사용자 확인).
Required specialist verdict: not applicable.
Completion boundaries: 측정·보정 complete / 사용자 수락 pending.
Related issue / knowledge: Library/research.md 코퍼스 항목.
Record handoff gap: none.

## T-009 / 2026-10-30 / 우리말샘 API 연결 검증 (Phase 2, P2-1)

Roadmap item: ROADMAP.md P2-1.
Result: 사용자가 키를 환경변수로 등록(끝 공백 1자 제거 후 재저장). 실제 응답으로 스크립트 수정: num≥10(오류 103), 응답 구조(sense[].target_code, senseInfo dict, relation_info 선택적), 동형어 번호·하이픈 제거, chunked 끊김 재시도, 역방향·공통 상위어 검사(일반 상위어 제외 목록). 4쌍 판정이 작가 규칙과 일치.
Changed files: `scripts/lookup_synonyms.py`, `references/decisions.md`(관계 배제 규칙), `Library/research.md`(API 실측), `Library/user-actions.md`(1번 완료), ROADMAP Phase 2 complete, ISSUES I-1 closed.
Check / target / result: 경첩 → 비슷한말 접철·정첩·합엽·힌지, 상위어 철물. 슬픔/기쁨 exit 2(반대말), 소금/설탕 exit 2(공통 상위어 결정체), 우산/치과·구름/중학교 exit 0.
Evidence: 채팅 실행 출력, Library/research.md.
Limits: 바다/육지는 사전에 반대말 관계가 없어 "곳" 제외 후 관계 없음으로 나옴 → LLM 판단이 보완(decisions D2). 소금처럼 동형어(악기 소금)의 관계어가 섞임 → 뜻풀이 기준 필터는 미구현. 키는 기록하지 않음.
Required specialist verdict: not applicable.
Completion boundaries: 구현·기술 검증 complete / 사용자 수락 pending.
Related issue / knowledge: ISSUES I-1 (closed).
Record handoff gap: none.

## T-008 / 2026-10-30 / 공개 저장소 생성 (우리말샘 API 신청용 URL)

Roadmap item: Phase 2 entry condition 준비(사용자 지시 2026-10-30).
Result: GitHub CLI 2.103.3 설치(winget), 사용자가 기기 인증으로 로그인, `JOEWRKS/JOESTALE` 공개 저장소 생성 후 main 푸시. URL https://github.com/JOEWRKS/JOESTALE.
Changed files: `README.md`(공개용), `Library/user-actions.md`(신청 기입값), 원격 origin 추가.
Check / target / result: `gh repo view` url·visibility PUBLIC·defaultBranch main 확인. 푸시 전 32자 키 패턴 스캔 0건.
Evidence: gh 출력(채팅).
Limits: 저장소에 허관 작가 예문 4쌍·소재 낚기 5단계가 출처 표기와 함께 인용돼 공개됨(사용자에게 알림). 저장된 자격증명 자동 사용은 분류기가 차단해 수동 로그인.
Required specialist verdict: not applicable.
Completion boundaries: 저장소 생성 complete / API 키 신청은 사용자 작업.
Related issue / knowledge: ISSUES I-1, Library/user-actions.md.
Record handoff gap: none.

## T-007 / 2026-10-30 / Phase 1.5 실전 보강 (P15-1~P15-5)

Roadmap item: ROADMAP.md Phase 1.5 P15-1 ~ P15-5.
Result: A(리라이트)·C(의견→장면) 실전 예를 T-006 규칙으로 0~5단계 수행, 서브에이전트 검수 2회(1차 지적 A 3·C 3 → 처리 3·기각 3, 2차 결과는 README 참조), 최종 PASS. 검증기 `--length` note, R5 형태소 단위 매칭(`형태/태그` 항목), G1 사전 단어 제외. SKILL.md 검수 서브에이전트 기본화·설치 절. VERSION 0.2.0, install.ps1.
Changed files: `skills/joestale/scripts/check_text.py`·`test_check_text.py`(+6건, 총 32건), `references/lexicon.json`(태그 고정 9항목)·`decisions.md`(A 분량 3.0배, 분량 보충 규칙)·`reviewer-prompt.md`(항목 7 복제 금지 명시), `SKILL.md`, `VERSION`, `scripts/install.ps1`, `examples/worked-A/*`, `examples/worked-C/*`, `Library/user-actions.md`, ROADMAP, ISSUES I-10·I-11.
Check / target / result: test_check_text.py 32건 ALL OK. worked-A 219자(1회 G1 오탐 → 수정 후 PASS), worked-C 349→436자(분량 보충 1회 → PASS). live-test-D·worked-B PASS 유지. install.ps1 임시 홈에서 ready→current→removed.
Evidence: examples/worked-A/README.md, worked-C/README.md, report.json.
Limits: 실전 예는 작성자(이 세션)가 직접 쓴 것이라 트리거 경로는 거치지 않음(트리거는 T-005에서 확인). 검수자는 haiku 모델. 개인 설치(~/.claude/skills)는 임시 홈으로만 시험.
Required specialist verdict: not applicable.
Completion boundaries: 구현·기술 검증 complete / 사용자 수락 pending (Library/user-actions.md 3번).
Related issue / knowledge: ISSUES I-10, I-11 (closed); Library/user-actions.md.
Record handoff gap: none.

## T-006 / 2026-10-30 / 실전 테스트에서 나온 오탐·결정표 공백 수정 (I-5~I-9)

Roadmap item: P0-2, P1-2, P1-3 보강 (ISSUES I-5~I-9 닫기).
Result: 검증기 G1 어절 분석 필터, G3 미등록 이름 한정·숫자 양방향 대조, 글자 수 출력. 결정표 D2(분량 우선순위·단위, 사물 시드 결정적 선택, 결합 시드 집계 기준)·D4(오탐 보고, 설계서 수정형 지적, 재검수, 검수자 설계서 범위)·D5(리포트 행 3개) 보강. seed_objects 30개.
Changed files: `scripts/check_text.py`, `scripts/test_check_text.py`(+8건), `references/decisions.md`, `references/lexicon.json`, `references/reviewer-prompt.md`, `references/scene-design.md`, `ISSUES.md`.
Check / target / result: test_check_text.py 26건 ALL OK. live-test-D `draft.v0.txt`(원래 오탐 3건이 난 판) 재검사 → G1·NNP 오탐 0. `final.txt`·worked-B `final.txt` PASS.
Evidence: 이 항목의 실행 출력(채팅), test_check_text.py.
Limits: XSM 태그 오류("손톱로")는 Kiwi 쪽 문제라 필터에서 일부러 제외. 수량 1은 대장 대조에서 빼기로 한 결정이라 "한 칸" 같은 누락은 못 잡음. 새 규칙으로 다시 쓴 실전 예는 없음.
Required specialist verdict: not applicable.
Completion boundaries: 구현·기술 검증 complete / 사용자 수락 pending.
Related issue / knowledge: ISSUES I-5~I-9 (closed).
Record handoff gap: none.

## T-005 / 2026-10-30 / 새 세션 트리거 확인과 D 유형 실전 테스트

Roadmap item: Phase 0 Optional "새 세션에서 joestale 트리거 확인", P4-1 예비 근거.
Result: 새 세션 스킬 목록에 `joestale` 있음, "짧은 단편 하나 써줘"에 Skill 도구로 호출됨(트리거 성공). D 유형으로 0~5단계 전부 수행: 사물 시드 전기밥솥 + 결합 시드 장례식장, 6문단 1,229자, 검증 3회(위반 3 → 0 → 0), 서브에이전트 검수 지적 4건 → 처리 4건, 최종 PASS.
Changed files: `joestale-work/live-test-D/`(design.json, draft.v0~v2.txt, final.txt, check.round1~3.json, report.json), `ISSUES.md`(I-5~I-9), `ROADMAP.md`(Optional 항목 갱신). `skills/joestale/`은 손대지 않음.
Check / target / result: `check_text.py final.txt --design design.json` PASS, 수식어 비율 0.05, 정도부사 0, 감정 직설 0, 번역투 0, 감각 6종, 대장 일치.
Evidence: joestale-work/live-test-D/report.json.
Limits: 검증기 오탐 2종(G1 관형사형 어미, G3 의성어 NNP)·놓침 1종(본문 숫자의 대장 누락) 확인(I-5, I-6). 회색지대 8건은 report.json `grey_zones`, 결정표·절차 모호점은 I-7~I-9. 분량 1,229자는 가정(약 1,500자)에 미달. 검수 반영 후 재검수는 하지 않음. 커밋하지 않음.
Required specialist verdict: not applicable.
Completion boundaries: 트리거·절차 실행 complete / 본문 품질·회색지대 결정은 사용자 수락 pending.
Related issue / knowledge: ISSUES I-5~I-9.
Record handoff gap: none.
