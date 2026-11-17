# Work results

닫힌 항목 T-001~T-031은 [TASK-archive.md](TASK-archive.md)로 이동(2026-11-02). 여기에는 열린 항목만 둔다.

## T-066 / 2026-11-17 / 판독 5차 7건 → 규칙을 피하려 깎은 대사: 패턴 90, W26·W27 문턱 완화, 코펠 장면 둘 재작성

Roadmap item: (0-2) 후속. 사용자 "다시 써".
Result: 일곱 줄 전부 검수·검증기 지적을 한 줄씩 피하는 말로 반영한 산물("받는 대로 다 가져올게요", "주는 대로 받아 왔어요", "맞고 나서 세어 봐", W5 피하려 넣은 "제 박자로 뛰었다"; "인사가 없어"·"한 끼는 봐줄게"는 T-063부터 있던 번역문 같은 생색). 수정: principles 90(규칙을 피하려 만든 말 금지 — 고친 줄은 소리 내어 읽고 어색하면 지적을 기각)·86 보정(짧은 사실 답 하나는 사람의 말), check_text ECHO_MAX·FACT_MAX 1→2(테스트 갱신, ALL OK), reviewer 처리 규칙 "지적을 피하는 말을 만들지 않는다", SKILL 2단계, decisions 행. 본문: 목요일 코펠·토요일 초소 대화를 사람 말로 다시 씀, 맥박 문장·'보태라니' 독백 삭제, 전제 shown_in '밥값'·'쌀만 가져와'. 확인 패스 2회(대사 검수·문장 독자) 반영/기각은 review_out7/decisions.md. 설계서 repeat_ok에 태석의 4장 소문 되풀이. 최종 2,969자·대사 48줄·PASS. 이전 본문 v9_r6.txt.
Changed files: skills/joestale/SKILL.md, references/(principles.md, reviewer-prompt.md, decisions.md), scripts/(check_text.py, test_check_text.py), joestale-work/long-run-test/T-track/ch11_v2/t063/(design.json, final.txt, v9_r6.txt, check.final.json, review_in7, review_out7(+decisions.md)), 보고서(판독 5차 절·본문), TASK.md, ROADMAP.md.
Check / target / result: test_check_text ALL OK. 검수 서브에이전트 4회(Sonnet). 분량 2,969자(하한 3,000 미달 31자, note).
미처리: 사용자 판독 전. ch11_v2/final.txt 미교체. T-048~T-066 커밋 전. VERSION 미증가.

## T-065 / 2026-11-17 / 판독 4차 → 검수 체계 분화(전문 검수자 5 + 독자 2, 기각 사유 의무), 패턴 88·89·56 보정, 11장 아홉 번째 판 최종

Roadmap item: (0-2) 후속. 사용자 "검증에서는 문제 없었냐", "검수자 별로 다양화하고 파고들 부분을 나눠서 더 깊게".
Result: 검증기 PASS는 형태만 재고 검수 30건 중 9건만 반영한 것이 "음? 하는 부분"의 원인. 반영: ① reviewer-prompt 5-C 전문 검수자 다섯(대사·독백·이치·이야기·인물; 단위마다 한 행, ○△×, 빠진 행 무효) 블록 + `build_review_inputs.py --final`; 처리 규칙 "마지막 패스는 전문 검수자", "기각 사유는 본문 안의 근거로 `review_out*/decisions.md`에", "동음이의·지시어 지적은 맥락을 보고 기각". ② principles 88(수량은 단위 명사와: 세 개), 89(값은 희소성 서열: 분유 > 통조림 > 쌀, 설계서 `setting.values`), 56 보정(앞 문장이 세운 지시 대상은 동음이의 아님); SKILL 5단계·2단계·"패턴 8~89"; scene-design `setting.values`; decisions 행. ③ 본문: 판독 3건(세 개 / 애 먹이라고 유지 / 분유 물가) + 통독 10곳 + 일곱 검수 전부 처리(반영 20·기각 15, review_out5/decisions.md). 설계서 옛 판 날짜·가정(01-21 일요일, 함석판 던짐, 쌀 봉지) 갱신. 확인 패스: 문장 독자 24건(B 1·I 0), 대사 검수 47행(× 3) → 4건 반영·3건 기각(사유 파일). 최종 2,980자·대사 47줄·PASS. 이전 본문 v9_r3·r4·r5.txt.
Changed files: skills/joestale/SKILL.md, references/(principles.md, reviewer-prompt.md, scene-design.md, decisions.md), scripts/build_review_inputs.py, joestale-work/long-run-test/T-track/ch11_v2/t063/(design.json, final.txt, v9_r4.txt, v9_r5.txt, check.final.json, review_in5·in6, review_out5(+decisions.md)·out6), joestale-work/reports/11장 아홉 번째 판 (판독 반영·스킬 수정).md(판독 4차 절·본문), TASK.md, ROADMAP.md.
Check / target / result: test_check_text ALL OK. 검수 서브에이전트 9회(Sonnet). 분량 2,980자(하한 3,000 미달 20자, note). 회귀 세트(score_review) 미실행 — 눈 가~아 문구는 안 바꿨고 전문 검수자는 새 세트가 필요.
미처리: 사용자 판독 전(수락 관문). ch11_v2/final.txt 미교체. 전문 검수자용 회귀 세트(must_catch) 없음. ch01~ch10 설계서는 옛 gist 양식. VERSION 미증가. T-048~T-065 커밋 전.

## T-064 / 2026-11-16 / 아홉 번째 판 판독 3차 6건 → 대사 어색함의 근본 원인 넷(설계서 문장 옮김·되받기·-고 꼬리·까닭 한 줄) → 패턴 85~87·79 수정, W26~W29·G10

Roadmap item: (0-2) 후속. 사용자 판독 2026-11-16 3차 "내가 지적한 부분만 고치지 말고 근본적 원인 파악".
Result: 여섯 줄의 공통 원인 넷을 검증기로 확인. ① 대사가 설계서 `dialogue_plan[].gist`에 문장으로 먼저 쓰여 본문에 그대로 옮겨짐(19줄 일치, G10) + `shown_in` 문장 강제 → 설정을 말하는 대사. ② `speech.endings`에 셋 모두 '되묻는다' + 패턴 42 좁은 해석 → 되받기 쌍 3·'그렇-' 답 4(W26·W27). ③ 패턴 62·69의 대사 번짐 → -고 꼬리 5·대칭 1(W28·W29). ④ 판독 2차의 "까닭 한 줄" 규칙(패턴 79)이 설명 독백을 낳음(W24 거니까). 수정: principles 79 수정·85(move만, 정보는 묻어 나옴)·86(묻는 말에 태도로, 되받기 장당 1)·87(-고 꼬리 장당 2, 대칭 금지)·검사법; scene-design `dialogue_plan` 양식 `{who,wants,move,info}`·`endings` 안내·`shown_in` 핵; reviewer 55 확장·57 ④ 반전·처리 규칙; SKILL 2단계·규칙 요약·"패턴 8~87"; decisions 행; check_text W26 되받기·W27 사실 답·W28 연결어미 꼬리·W29 대칭·G10 요지 옮김·JUSTIFY '거니까', 테스트 11건 ALL OK. 본문: t063 설계서를 move 양식으로, 코펠·중심 장면 대화 재작성, 최종 패스 셋(눈 사·문장 독자·플랫폼 독자) 겹친 지적 전부 반영(거즈 농담 → 죽 농담+민규 발뺌, "한 주 치" 되받기, 분유 줄 군말, 아문 손 붕대 모순, '아까 그 사람', '얻어먹는 놈 소리' → '내 쌀 먹는 놈 소리는 이번 주로 끝이네', 정당화 독백 삭제). 이전 본문은 v9_r3.txt. 최종 3,143자, 대사 53줄, PASS, 플랫폼 독자 "다음 화 연다".
Changed files: skills/joestale/SKILL.md, references/(principles.md, reviewer-prompt.md, scene-design.md, decisions.md), scripts/(check_text.py, test_check_text.py), joestale-work/long-run-test/T-track/ch11_v2/t063/(design.json, final.txt, v9_r3.txt, check.final.json, review_in4, review_out4), joestale-work/reports/11장 아홉 번째 판 (판독 반영·스킬 수정).md(판독 3차 절·본문), TASK.md, ROADMAP.md.
Check / target / result: test_check_text ALL OK. 새 규칙을 판독 전 본문에 돌리면 W26 3쌍·W27 4·W28 5·W29 1·G10 19·W24 1을 잡고, 고친 본문은 0. 검수 서브에이전트 3회(Sonnet). 회귀 세트(score_review) 미실행. ch01~ch10 설계서는 여전히 `gist` 양식(새 장부터 move).
미처리: 사용자 판독 전(수락 관문). ch11_v2/final.txt 미교체. 기각 사유 기록: "잘 먹겠습니다, 형", 태석 소문 줄, '싸움 나면' 독백, 함석판 단 길이(12장 훅과 함께), 민규 제 손 보이기. VERSION 미증가. T-048~T-064 커밋 전.

## T-063 / 2026-11-16 / 여덟 번째 판 판독 11건 → 원인 규칙 추적·스킬 수정(패턴 75~83, 검수 55~57, W22~W25·G9, 검증기 대사 버그 2), 11장 아홉 번째 판

Roadmap item: (0-2) 후속. 사용자 판독 2026-11-16 "내가 말한 부분만 다시 쓰지 말고 아예 스킬 자체를 고쳐".
Result: 판독 11건 전부 규칙이 만든 것으로 확인. (1) 전보문 대사 ← 패턴 62·66·69 + `speech.endings` 겹침 + 검증기가 여러 문장 대사의 둘째 문장을 서술문으로 계산해 R1·R2를 매김(버그) + 글 전체 R2에 대사 포함(버그). (2) 얻어먹는 주인공 ← 전제를 앞 장에 두고 이 장에 안 깜, `shown_before` 미검사. (3) 어거지 쌀 이야기 ← 뼈대 "그대로" 가정, 설계 단계 검산 없음. (4) 명사화된 생각 ← R7 회피. (5) 정당화 독백 ← 패턴 74 번짐, G2가 독백 안을 안 봄. (6)(10) 토막 ← 같은 겹침. (7) 협박조 거래 ← 장면 결 미정. (8) 세부 독백·근시안 패치. (9) 대비 꼴 셈 ← inference 면제 오용. (11) 표정 어절 ← R4·패턴 25 과적용. 스킬 수정: principles 패턴 75~83 + 검사법, 패턴 74 보정; reviewer-prompt 55(사람의 말)·56(주는 쪽의 전제)·57(독백·셈의 결), 문장 독자 B 확장·I 신설, 플랫폼 P2·P4 확장, 처리 규칙 "마지막 패스 지적은 상한 무관 반영"·"통독"; scene-design `scenes[].check`·`premises[].shown_in`·`exchanges[].tone`·`faces`; SKILL 1원칙·규칙 요약·1·2·4·5단계; decisions D3 행; check_text W22 토막 대사·W23 생각의 명사화·W24 독백·W25 대비 꼴 셈·G9·R4 표정 면제·대사 둘째 문장 R1~R4 면제·글 전체 R2 strip_quotes; test 11건 추가(ALL OK); build_review_inputs 눈 사·아 항목. 아홉 번째 판: 설계서 이야기 검산(12장면 전부 ✓), 초고 PASS → 1회차 5명 87건 → v9_r1 PASS → 2회차 4명 59건 → v9_r2 PASS → 최종 문장 독자 14·플랫폼 독자 11, B·I·P2·P4 전부 반영 → final PASS. 3,077자, 1문장 71%, 3문장+ 1, 대사 41%, 독백 10. 플랫폼 독자 셋 전부 "다음 화 연다". 사용자 판독 2차(같은 날) 5건: "그거면 됐고"(인물표 안 보고 앞 말 반응만으로 쓴 대사 — 패턴 75에 "대사마다 인물표·상황·바람 셋, 고치는 줄도" 추가), '보태란 말이 왜 고맙지'(까닭 한 줄 규칙, 패턴 79), '-지. -지.'(W24 같은 어미 연속), '먼저 나가라고'(설계서를 알아야 서는 셈 → '싸움 나면 앞에 세울 몸'), 자물쇠 → 도어락(패턴 84 현대 사물 퇴행 금지). 여러 문장 독백 둘째 문장 R2 버그도 수정. 최종 3,097자, PASS, 테스트 ALL OK. 사용자: "그 외에는 대화도 문장도 전체적으로 매끄러워졌네".
Changed files: skills/joestale/SKILL.md, references/(principles.md, reviewer-prompt.md, scene-design.md, decisions.md), scripts/(check_text.py, test_check_text.py, build_review_inputs.py), joestale-work/long-run-test/T-track/ch11_v2/t063/(design.json, draft.txt, v9_r1.txt, v9_r2.txt, final.txt, check.*.json, review_in·in2·in3, review_out·out2·out3), joestale-work/reports/11장 아홉 번째 판 (판독 반영·스킬 수정).md(신규), TASK.md, ROADMAP.md.
Check / target / result: test_check_text ALL OK. 새 검증기를 여덟 번째 판에 돌리면 W24(정당화 독백)·W25(대비 꼴 셈)·W23(명사화)을 잡음. 아홉 번째 판 검증기 PASS(설계서·앞 장 10개·--draft). 검수 서브에이전트 11회(Sonnet). 회귀 세트(score_review) 미실행.
미처리: 사용자 판독 전(수락 관문). ch11_v2/final.txt 미교체. 함석판 손질 단은 세 판 연속 플랫폼 독자가 "길다" — 12장 훅과 함께 존재 여부 재검토. 태석 계급·입장 미표시(앞 장 몫). 연결 독자 미실시. VERSION 미증가. T-048~T-063 커밋 전.

## T-062 / 2026-11-15 / 11장 여덟 번째 판 — 플랫폼 프로필(1문장 73%·대사 35%·셈 문장 3), 검수 2회 + 최종 독자

Roadmap item: (0-2) 후속. T-059~T-061의 결론을 본문에 적용. 사용자 "여덟 번째 판 쓰기".
Result: 일곱 번째 판 뼈대 그대로, 호흡만 바꿈. 설계서 `ch11_v2/t062/design.json`에 `profile`(문단 1문장 60~70%, 대사 30~40%, 셈 문장 목록·규칙, 외부 시점 첫 어절, 끝 한 줄) 추가, banned_phrases에 작가 풀이·이력 소개·독백 중복 문장 7개 추가, 3,500kcal·황대식·망우동 대장에서 내림. 초고 3,320자(1문장 70%, 3문장+ 0, 대사 33%) → 최종 3,082자(1문장 73%, 3문장+ 3, 대사 35%, 서술 평균 30자). 검증기 PASS(설계서·앞 장 10개·--draft, R9·L1 포함). 검수 1회차 8명 115건 → 단 단위 재작성(장갑 모순, 민규 시점 이탈·손바닥 선행 삭제, 노인의 말을 등 뒤에서 들린 말로, 황대식 비유 삭제, 담배 거래 '두 개만 주세요, 담배로 드릴게요', 되풀이 정보, 끝의 전망 두 문장 삭제) → 2회차 6명 48건(눈 사 1·0, 눈 아 8·7) → 반영 → 최종 문장 독자 15·플랫폼 독자 24("뒤로가기 없음, 다음 화 연다") → 낱말 치환 5곳. 보고서 `joestale-work/reports/11장 여덟 번째 판 (플랫폼 프로필).md`(수치표·검수 경과·본문).
수치 결론: 문단 형태는 플랫폼 중간 축(변경의 죄수 68%)에 들어갔고 검증기 W20 기준(1문장 50%↑·3문장+ 10%↓)도 처음 충족. 셈 문장 3개 중 "태석은 두 달 뒤를 셈하고도 웃고 있었다"는 검수자 3/5·플랫폼 독자가 해설로 짚음(T-061 설명감 비용 재현). 플랫폼 독자 셋 전부 다음 화 연다이되 "주인공 속이 안 보인다"(통조림 주는 까닭, 2.9kg 본 순간)는 일곱 번째 판과 같은 지적.
Changed files: joestale-work/long-run-test/T-track/ch11_v2/t062/(design.json, draft.txt, v8_r1.txt, v8_r2.txt, final.txt, check.*.json, review_in·in2·in3, review_out·out2·out3), joestale-work/reports/11장 여덟 번째 판 (플랫폼 프로필).md(신규), TASK.md, ROADMAP.md.
Check / target / result: 검증기 PASS. 검수 서브에이전트 16회(Sonnet). 연결 독자 미실시(장부 파일 없음). 패턴·검증기·test 미변경.
미처리: 관문(눈 사·눈 아 0건) 2회 상한으로 미달 — 남은 것: 장갑 장치(맨손으로 오르는 까닭), "앓고 난 몸이었다" 홀로 선 설명, 자물쇠 단 세 문장. 사용자 판독(수락 관문) 미실시 — 판독 뒤 ch11_v2/final.txt 교체 여부 결정. 셈 문장 규칙·문장형 프로필의 패턴/검증기 반영은 판독 뒤. T-048~T-062 커밋 전.

## T-061 / 2026-11-15 / 문체·내용 분리 재검증(형태 2 × 셈 문장 2, 표본 8편, Claude 3 + Codex Astra 3 + 웹 ChatGPT 1 = 112판정) → 형태 효과 0(전원 일치), 셈 문장 종합은 회사 간 정반대

Roadmap item: (0-2) 후속, T-060 한계("문체와 내용이 분리되지 않음") 해소. 사용자 "분리 재검증 먼저".
Result: T-060 문장형(B)에서 작가 풀이 3문장을 뺀 마스터 문장 집합 하나(⟦⟧ = 인물 셈 문장)에서 `sep/gen.py`로 기계 변환 — 형태 F1 한 줄형(1문장 100%, 서술 24~26자) / F2 문장형(1문장 37~50%, 서술 46~59자) × 내용 p 셈 있음 / m 셈 없음, 2장면 8편(997~1,114자, 전부 check_text PASS). 쌍은 장면마다 형태 효과 2쌍 + 내용 효과 2쌍 = 8쌍, 평가자 3세션(Sonnet 5.5 ×2, Opus 5.5 ×1, fresh, pairs.md만) × 16판정 = 48.
수치 결론: Claude 48판정 — 형태 효과 종합 24/24 "둘 다", 읽힘 F1 16:8; 셈 있음이 종합 15:0·인물 16:0·당김 11:0, 설명감 0:24. GPT Astra 48판정(Codex CLI 0.169, 격리 폴더) — 형태 효과 종합 20/24 "둘 다", 읽힘 F2 24:0; 셈 없음이 종합 24:0·읽힘 24:0·당김 22:0·설명감 24:0, 인물만 셈 있음 12:4. 웹 ChatGPT 16판정(사용자 실행, 모델명 미확인)은 Astra와 동일 방향(셈 없음 종합 8:0·읽힘 8:0·설명감 8:0, 문장형 읽힘 8:0, 종합 형태 쌍 8/8 둘 다). OpenAI 넷 합산: 셈 없음 종합 32:0, Claude 셋: 셈 있음 15:0. 일치하는 것: 문단 형태는 종합 무관(48 중 44 둘 다), 셈 문장은 인물↑ 설명감·읽힘↓, 좋은 셈("그 셈을 하고도 웃었다")·나쁜 셈(이력 소개·독백 중복) 인용 동일. 갈리는 것: 셈 문장이 종합·당김에 득인가(Claude 득, GPT 손). T-060 "문장형 + 셈 문장" 결론은 평가 모델 취향이 섞인 것으로 판정. 셈 문장은 다이얼(인물 ↔ 읽힘·설명감)이고 다음 화 넘김에 득이라는 증거 없음.
Changed files: joestale-work/profile-test/sep/(S1·S2_master, gen.py, 표본 8편, build_pack.py·tally.py(평가자 번호 인자), judge1~3 Claude, judge4~6 Codex Astra, judge7 웹 ChatGPT, judge8 Gemini용 미실행, web_*_pairs.md·web_prompt.txt), joestale-work/reports/문체·내용 분리 재검증 (T-061).md(신규), skills/joestale/references/platform-norms.md("JOESTALE 적용" T-060 줄을 T-060·T-061로 교정: 형태는 종합 무관, 셈 문장 규칙), TASK.md, ROADMAP.md.
Check / target / result: 검증기 PASS 8/8(설계서 없이). Claude 세션 3회 + Codex Astra 3회 실행(사용자 승인; Sol은 ChatGPT 계정 거부, 설치된 Codex 0.146은 Astra 미지원이라 최신 CLI를 scratch에 따로 설치해 사용, 개인 설치 미변경). 패턴·검증기·test 미변경.
미처리: 셈 문장의 종합 득실은 Anthropic/OpenAI 정반대라 미확정(Gemini 묶음 judge8 준비됨, 미실행; 또는 사람 독자). 11장 여덟 번째 판 미작성 — 교정 방향: 1문장 60~70%, 셈 문장 장면당 1~2개 이하를 행동 문단 끝에(지각·행동에 붙은 것만), 이력 소개·독백 중복·의도 단정 셈 금지, 작가 풀이 금지, 외부 시점 첫 어절 표지, 끝 한 줄. T-060·T-059 미처리 그대로. T-048~T-061 커밋 전.

## T-060 / 2026-11-15 / 두 축 문체 프로필을 11장 장면 둘로 직접 써서 블라인드 평가(표본 6편, Opus 3세션 36판정) → 문장형 종합 24:0

Roadmap item: (0-2) 후속, T-059의 "여덟 번째 판 뒤 결정"을 앞당기는 사전 검증. 사용자 "네가 여러 문장·문단·단편을 구사해서 먼저 검증하고 자체적으로 외부세션 평가를 돌리는 건 어떻게 생각해" → "표본 쓰기 시작".
Result: 11장 일곱 번째 판의 두 장면(S1 초소 인수·손 베임·코펠, S2 배급 체육관·계단 사내)을 A 한 줄 문단형(1문장 97%, 서술 25~26자)·B 문장형(1문장 40~41%, 서술 56~60자, 3문장+ 9~11)으로 다시 쓰고, C 대조군은 일곱 번째 판 원문(1문장 13~33%). 각 970~1,170자. A·B 넷 다 check_text PASS(첫 B는 복문으로 R9 걸려 짧은 문장·긴 문단으로 수정). 장면별 쌍 3개 × 2 = 6쌍을 평가자 3세션(Opus fresh, pairs.md만 열람, key는 별도)이 순서 뒤집어 두 번씩 = 36판정. 채점 5항목(읽힘·당김·설명감·인물·종합) + 쌍마다 인용 문장.
수치 결론: 종합 B 24 / A 2 / C 0 / 둘 다 10. 당김·인물 B 24:0 전승, 읽힘 C 18(B 2), 설명감 A 12·C 12·B 0. 같은 쌍 두 번 판정 18/18 일치. 셋이 같은 문장을 짚음 — 설명감 패인은 작가 비유 풀이("낮의 끝과 밤의 앞", "열량은 종이에 적는 단위"), 당김·인물 승인은 인물의 셈("태석은 그 셈을 하고도 웃었다", "그 계단도 매주였다"). 3인칭에서 1문장 97%는 "툭툭 끊김", 외부 시점 한 줄 전환은 누구인지 되짚게 함.
Changed files: joestale-work/profile-test/(S1·S2 ×A·B·C, metrics.py, build_pack.py, tally.py, judge1~3/pairs.md·key.json·result.md), joestale-work/reports/문체 프로필 블라인드 검증 (T-060).md(신규), skills/joestale/references/platform-norms.md("JOESTALE 적용" 절에 T-060 검증 세 줄), TASK.md, ROADMAP.md.
Check / target / result: 검증기 PASS 4/4(설계서 없이). 평가 세션 3회 실행(사용자 승인). 패턴·검증기·test 미변경.
미처리: 문체와 내용(외부 시점 문단·인물 셈 문장)이 분리되지 않아 B 승리의 몫을 가를 수 없음(재검증은 여덟 번째 판 뒤 결정). 평가자 셋이 같은 모델. 11장 여덟 번째 판 미작성(방향 확정: 문장형 1문장 40~50%·서술 55~65자 + 인물 셈 + 작가 풀이 금지 + 외부 시점 표지). T-059 미처리 그대로. T-048~T-060 커밋 전.

## T-059 / 2026-11-15 / 카카오페이지 커뮤 필력 검증작 10작품 무료분 읽기 → 2차 표본 수치(두 축), platform-norms 2차 절

Roadmap item: (0-2) 후속, T-058 연장. 사용자 "커뮤나 후기에서 필력 검증된 소설 리스트업 → 전부 읽어".
Result: 후보 10편(`joestale-work/platform-reading/candidates_2026-11-15.md`) 무료분 전부 읽음 — 크툴루 1권 25장·멸망한 세계의 사냥꾼 1권 12장·검은머리 미군 대원수 1권 24장·불꽃의 기사 1권 7장(단행본 ePub, 장별 수치), 변경의 죄수 1~25·예언의 아이 1~25·어두운 바다 1~25·괴담 1~20·데못죽 1~25(신규 대여권 25·25·25·15·20장 전량), 검을 든 꽃 1~3(무료분 한도). 화별 메모 약 110건 + 작품별 총평 10건.
수치 결론: "1문장 서술 84~96%"는 현판·1인칭 축(백덕수·글근육·명원 69~97%)이고, 정통 판타지·로판·재난물(Cadilet·은소로·연산호·도동파)은 1문장 5~50%, 서술 60~150자의 문장형 축. 두 축 공통 규범 넷: 끝 한 줄(10작품 전부), 한 줄 문단은 자리(사건·정체·감정 정점), 설명 뒤 역접 한 줄로 행동 복귀, 외부 시점 선행. 기법 12항 추가(인용 포맷 7종, 3층 아이러니, 외부 시점 세 용도, 인물 소개 3박자, 전략 엔진, 금언+풀이, 복선 세 번 뜻 바꾸기, 끝 유형 8종 추가 등).
Changed files: skills/joestale/references/platform-norms.md(2차 표본 절·표·적용·기법), joestale-work/platform-reading/kakaopage_notes.md(2차 표본 절 추가), joestale-work/reports/카카오페이지 커뮤 필력 검증작 읽기 (T-059).md(신규), TASK.md, ROADMAP.md.
Check / target / result: 수치는 뷰어 shadow DOM 본문에서 JS로 측정(검증기 미변경, test 미실행). 본문 미저장(저작권).
미처리: 패턴·검증기에는 반영하지 않음(문장형 프로필 선택 규칙, 끝 유형 추가, 인용 포맷 패턴은 여덟 번째 판을 써 보고 결정). 11장 여덟 번째 판 미작성(기준점: 변경의 죄수 1문장 68%). 검을 든 꽃 4화 이후는 12시간 기다무라 미독. T-058 미처리 그대로. T-048~T-059 커밋 전.

## T-058 / 2026-11-15 / 카카오페이지 무료분 60화 읽기(대여권 전량) → 플랫폼 표본 수치, 패턴 72~74, 검증기 W20·W21·R6 박자 면제

Roadmap item: (0-2) 후속. 사용자 "시리즈는 자체 프로그램이 있어야 하니 카카오페이지에서 읽어", "대여권 받았으니 30장 다 써서 읽어".
Result: ① 카카오페이지 검색: 알브레히트 일대기·약먹는 천재마법사·방랑기사로 살아가는 법 있음, 망나니 경비조장·여포가 효도를 잘함·프롤로그에서 30년 없음. ② 읽음: 알브레히트 1~30화(이미지, 캡처), 약먹는 천재마법사 1~25화(ePub, 본문 수치 측정), 방랑기사 1~15화(이미지). 대여권 70장 전량 소진. ③ 표본 수치(약먹는 25화): 서술 문단 평균 42~56자, 1문장 문단 84~96%, 3문장 이상 0~3%, 대사 문단 15~39%, 60화 전부 끝 한 줄. 추가 기법: 화당 시점 교차 3~5회(적·조연 시점은 평가·자만 뒤집기·답 선공개), 같은 순간 두 시점, 전투 공식(의성어→한 글자 대사→결과→까닭→적 반응), 복선 대사 한 줄 던지고 설명 없이 회수, 결심은 한 줄 문단 연속, 제도는 한 줄에 한 항목. 일곱 번째 판은 3문장 이상 31%·대사 49%·1문장 27%. ④ 스킬 반영: 패턴 72(설정은 세 입으로)·73(장의 끝은 한 줄)·74(문단은 박자, 주인공 평가는 남의 눈), 패턴 70 수치 갱신, 검증기 W14 기준 3문장·140자, W20 문단 박자, W21 장의 끝, 박자 문단(1문장·20자 이하) R6 면제, 플랫폼 독자 P5·P6 보강, `references/platform-norms.md` 신설, decisions D3·D4.
Changed files: skills/joestale/{SKILL.md, references/principles.md·reviewer-prompt.md·decisions.md·platform-norms.md(신규), scripts/check_text.py·test_check_text.py}, joestale-work/platform-reading/kakaopage_notes.md(신규), joestale-work/reports/카카오페이지 무료분 읽기 (T-058).md, TASK.md, ROADMAP.md.
Check / target / result: test_check_text.py ALL OK(T-058 8건 추가). 일곱 번째 판 final.txt에 새 검증기: W20·W21 note 발생(간격 확인).
미처리: 시리즈 전용 세 작품 미독(카카오페이지에 없음). 11장 여덟 번째 판(새 기준 적용) 미작성. 추가 기법(시점 교차·전투 공식·복선 한 줄)은 platform-norms.md에만 적었고 패턴·검증기로는 아직 안 옮김. T-057 미처리 항목 그대로.

## T-057 / 2026-11-12 / 여섯 번째 판 판독 21건 → 원인 34~45, 패턴 64~71, 눈 아·플랫폼 독자, 검증기 W14~W19, 11장 일곱 번째 판

Roadmap item: (0-2) 후속. 사용자 판독 21건 + "문장 생성 원인부터 바로잡고 스킬 자체를 전부 재검토, 검증 과정까지" + "문피아·시리즈 무료분이라도 읽어라".
Result: ① 원인 34~45(규칙 충족용 삽입, 결과에서 거꾸로 짠 행동, 시간표 미검증, 대사 꼴, 장면·요약 미구분, 받는 줄 없음, 문장 구사, 세계 디테일, 모름의 보고문, 떡밥 대장, 문단 호흡, 구성). ② 패턴 64~71(심는 문장은 행동 속에, 가장 쉬운 행동·주인공의 품, 입말의 꼴, 장면/요약/회상, 받는 줄, 문장 하나의 뜻, 플랫폼 문단, 시간표). ③ 설계서 `pov`·`timeline`·`scenes`·`plants`·`hooks`·`speech.endings`·`flaw`. ④ 검증기 W14(문단)·W15(대사 종결 단조)·W16(발화자 표지)·W17(pov 받는 줄)·W18(자리만 알리는 문장)·W19(모름의 보고문), test ALL OK. ⑤ 검수 눈 아(51~54 심은 자리·행동 납득·시간표/비중·입말/받는 줄)와 **플랫폼 독자**(P1~P6, 뒤로가기 자리). 처리 규칙: 문장 쌍 치환 금지(단 다시 쓰기), 눈 아 관문. ⑥ 문피아 무료 베스트 1화 둘 읽음(호흡 수치는 보고서). ⑦ 11장 일곱 번째 판: 뼈대 교체(당당히 꺼냄) → 검수 3회 245건 반영 → **4,037자 PASS**, 밀도 6.59/2.06/0.24, 문단 최대 4문장. ⑧ 회귀 세트 `regression/ch11_v6/`(M01~M21 중 20).
Changed files: skills/joestale/{SKILL.md, references/principles.md·reviewer-prompt.md·decisions.md·scene-design.md·design.template.json, scripts/check_text.py·test_check_text.py·build_review_inputs.py, regression/ch11_v6/*}, joestale-work/long-run-test/T-track/ch11_v2/{design.json, design.t056.json, t057/*}, 판정/T057_회귀/*, reports/11장 일곱 번째 판 (구성부터 다시).md, 판독_11-25장.md, TASK.md, ROADMAP.md.
Check / target / result: test_check_text.py ALL OK(W14~W19 12건 추가). 회귀 ch11_v6(여섯 번째 판, 판독 20건): 검증기 3/3, 눈 아 6/9, 문장 독자 1/3, 눈 나 1/1, 플랫폼 독자 4/4 → 합산 15/20(놓침: M04·M05·M12 대사 꼴·발화자, M08·M13 문장 구사). 일곱 번째 판 관문: 눈 사·눈 아 2회차 지적을 반영했으나 2회 상한으로 재검수 없음(미달 기록). 미검증: 사용자 판독, 시리즈 여섯 작품(브라우저 차단).
미처리: 플랫폼 독자 "끝이 밍밍, 주인공 속이 안 보임". 눈 나: 태석 쌀 셈(세 주먹×7일 vs 1.3kg), 2장 민규 "부치려고요"(앞 장 수정 후보 유지), 도현이 셋방에서 출퇴근하는 까닭. 연결 독자 G6 옥상 점멸(이 장에서 기각). 시리즈 작품 읽기(Chrome 사용 여부 사용자 결정).

## T-056 / 2026-11-12 / 다섯 번째 판 판독 4건 → 패턴 60~63, 검수 항목 49·50, 11장 여섯 번째 판

Roadmap item: (0-2) 후속. 사용자 판독(총평 "매끈해지고 역학관계 받아들일 만함", 4건은 "문장만 고치지 말고 문제점을 파악해 품질을 올릴 방향으로").
Result: ① 판독 4건을 버릇 넷으로 진단(원인 30~33): 변화를 통증·수치로만 씀, 지운 자리를 반대 표현으로 채움(과보정), 정보 둘을 한 대사에 묶음, 옮기는 말의 세계의 길을 안 봄. ② 패턴 60~63과 검사법. ③ 검수 항목 49(눈 나: 옮기는 말과 세계의 길), 50(눈 바: 신호 선행·금지 표현 자리의 반대 표현·한 대사 한 정보). 눈 바에 `banned_phrases` 제공. ④ 11장 설계서: `wound.signals`, 인물 사정(민규 날마다 집에서 올라옴), banned_phrases 3개 추가. ⑤ 여섯 번째 판: 신호 심기(간지러움 → 땅김 → 딱지, 멍), 정해성 반박 문장 삭제, 제대는 서술 + 태석 대사 하나, 민규 흥정 3단, "가져가게요" → 관문 1회차 57건·2회차 31건 반영 → **4,914자 PASS**. `reports/11장 여섯 번째 판 (신호·압축·세계의 길).md`. ⑥ 회귀 세트 `regression/ch11_v5/`(K01~K04).
Changed files: skills/joestale/{SKILL.md, references/principles.md·reviewer-prompt.md·decisions.md, scripts/build_review_inputs.py, regression/ch11_v5/*}, joestale-work/long-run-test/T-track/ch11_v2/{design.json, design.t055.json, t056/*}, 판정/T056_회귀/*, reports/11장 여섯 번째 판 (신호·압축·세계의 길).md, 판독_11-25장.md, TASK.md, ROADMAP.md.
Check / target / result: 회귀 ch11_v5(다섯 번째 판, 판독 4건): 눈 나(49)+눈 바(50)+문장 독자 → 3/4(K01 회복 신호만 놓침. 눈 바 50이 멍은 짚고 욱신은 안 짚음). 2장 "부치려고요"는 앞 장 수정 후보로 기록(세계의 길 없음). 미검증: 여섯 번째 판 사용자 판독, 관문 2회차 뒤 수정 2건의 재검수, test_check_text.py는 이번에 코드 변경 없음(스크립트 LENSES만).
미처리: 문장 독자 설정·구조 지적(처치자 용어, 근무표 대사, 호칭 관계, 탄피 대화). 분량 상한. 대장 수치(쌀 6,000원·3,500kcal). 2장 "부치려고요" 수정 여부.

## T-055 / 2026-11-10 / 인물표·대화 설계·인물 관문(패턴 57~59, G8·X2·X3·W13, 눈 사), 11장 다섯 번째 판

Roadmap item: (0-2) 후속. T-054 방향 여섯 가지 + "검증 과정을 늘려 확실하게 잡을 방법"에 사용자 "그렇게 해".
Result: ① 설계서 `characters`(situation·temperament·speech·toward·wants_here·knows·not_knows·evidence)·`dialogue_plan`·`user_examples`·`banned_phrases`. ② 검증기 G8(evidence가 --prev 본문에 없으면 위반), X2(금지 표현 재등장 위반), X3(판독·검수 예시와 8자 이상 겹침 note), W13(동음이의 후보 note, `WATCH_WORDS`). ③ 패턴 57~59(대사는 인물표에서, 예시는 방향이지 본문이 아니다·사용자 예시도, 지적된 표현은 설계서에서 지우고 금지 목록으로). ④ 검수 항목 46·47·48과 눈 사(인물) 신설, 연결 독자 G8, 처리 규칙(대화는 장면 단위, 사용자 예시 옮기지 않기, 설계서에서 지적 표현 지우기, 인물 관문 0건, 관문 검수 2회 합치기). ⑤ 채점기가 검증기 출력 줄도 행으로 읽음. ⑥ 독자 장부에 2·4·5·6·7장 누락 줄 보강(연결 독자 G8 오판 원인). ⑦ 11장 다섯 번째 판: 인물표·대화 설계에서 대화 장면 셋 다시 씀 → 일곱 눈·두 독자 61건 → 관문 1회차 42건 → 관문 2회차 27건 반영 → **4,881자 PASS**, 밀도 7.26/2.16/0.28. `reports/11장 다섯 번째 판 (인물표에서 다시 쓰기).md`.
Changed files: skills/joestale/{SKILL.md, references/principles.md·reviewer-prompt.md·decisions.md·scene-design.md·design.template.json, scripts/check_text.py·test_check_text.py·build_review_inputs.py·score_review.py, regression/ch11_v{2,3,4}/reader_memory.md, regression/ch11_v4/must_catch.json}, joestale-work/long-run-test/T-track/ch11_v2/{design.json, design.t053.json, t055/*}, 판정/T055_회귀/*, reports/11장 다섯 번째 판 (인물표에서 다시 쓰기).md, 판독_11-25장.md, TASK.md, ROADMAP.md.
Check / target / result: test_check_text.py → ALL OK(G8 2·X2·X3·W13 추가). 회귀 ch11_v4(네 번째 판, 판독 7건): 검증기 X2가 F04(11-09 판독 표현 재발)·X3가 F06 예시 복사, W13이 F05, 눈 사 2회 합산이 F03·F06·F07, 연결 독자 G8이 F06 → 검수자+검증기 6/7. F02(나무라는 투 대사)는 검수자 다섯 번 모두 놓침 → 항목 46에 "말의 결" 추가(재측정 전). F01·F02는 이번 판독에서 넣은 banned_phrases로는 잡히나 순환이라 세지 않음. 같은 본문에 문장 독자 7건/19건/39건 → 관문 검수 2회 합치기 규칙. 회귀 ch11_v3 12/12 유지. 미검증: 다섯 번째 판 사용자 판독, 관문 2회차 뒤 수정 4건의 재검수, 옛 회귀 세트(ch11, ch11_v2) 재채점.
미처리: 문장 독자 설정·구조 지적 7건(처치자 용어, 첫 문장 감각 시작, 붕대 푸는 까닭, 근무표 대사 등). 분량 4,881자(설계서 상한 4,500 초과). 쌀 6,000원·3,500kcal 대비(연결 독자 의심 2건, 사용자 판단 대기).

## T-054 / 2026-11-10 / 네 번째 판 사용자 판독 7건 기록·진단, 회귀 세트 ch11_v4

Roadmap item: (0-2) 후속. 사용자 판독 2차("고치라고 한 내용을 그대로 쓰기만 했다. 캐릭터성·맥락 없음").
Result: 판독 7건(F01~F07)과 원인 25~29를 `판독_11-25장.md`에 기록. 요지: ① 설계서에 인물의 사정·성격·관계·장면에서 원하는 것이 없어 대사를 인물에서 끌어내지 못함(민규 2장 "집사람이랑 돌 지난 애", 태석 4장 "나도 옆에서 얻어먹지"가 설계서에 없음) ② 사용자 예시를 앞 장 사실과 대조 없이 붙임 ③ 대화를 문장 단위로 기워 사슬이 끊김 ④ 지적된 독백이 설계서 `feeling_monologue`에 남아 재발 ⑤ 동음이의 "불려 올게". 회귀 세트 `regression/ch11_v4/` 신설. 본문·규칙은 고치지 않았다(방향 사용자 확인 대기).
Changed files: joestale-work/long-run-test/T-track/판독_11-25장.md, skills/joestale/regression/ch11_v4/*, TASK.md, ROADMAP.md.
Check / target / result: 세트 keys가 text.txt에 모두 있음을 스크립트로 확인. T-053 검수 출력과 대조 → F03·F05는 적중 0, F02 일부는 검수 반영이 만든 문장. 미검증: 새 세트 점수(인물 눈을 만든 뒤 잰다).

## T-053 / 2026-11-10 / 세 번째 판 판독 대책: 짐작·다리·주고받기(패턴 52~56), L1 밀도 조건, W10~W12, 눈 바, 11장 네 번째 판

Roadmap item: (0-2) 후속. T-052 방향 다섯 가지에 사용자 "그렇게 해".
Result: ① 검증기: L1을 "초고 ×1.05를 넘고 밀도도 오를 때(내용어 +0.3·절 +0.1 초과)만 위반"으로, W10 밀도 하한(5.82·1.79), W11 주어 없이 끊긴 짧은 문장 3곳 이상, W12 inference 5개 이상, 설계서 `inference` 구절은 R3·R4·R7·R8 면제. ② 패턴 52~56(시점 인물의 짐작, 시간 다리와 계기, 갈등 주고받기와 중심 장면, 이어지는 행동·인물 주어 닫기·검수 예시 옮기지 않기, 말은 한 번에 가리킨다). ③ 검수 항목 44·45와 눈 바(42~45) 신설(눈 마는 7개로), 문장 독자 물음 G(가리키는 것이 흐림)·H(끊김·건너뜀·싱거움). ④ 설계서 `bridges`·`exchanges`·`inference`. ⑤ 처리 규칙: 덜어내는 것은 수식어·설명뿐, 수정 예시 옮기지 않기, 마지막 반영 뒤에도 문장 독자. ⑥ 11장 네 번째 판: 초고에서 다시 씀 → 여섯 눈·두 독자 101건 반영 → 문장 독자 재검수 24건(1차 39건) 문장 단위 반영 → **4,381자 PASS**, 밀도 7.43/2.14/0.30(1~10장 범위 안). `reports/11장 네 번째 판 (이야기 되살리기).md`.
Changed files: skills/joestale/{SKILL.md, references/principles.md·reviewer-prompt.md·decisions.md·scene-design.md·design.template.json, scripts/check_text.py·test_check_text.py·build_review_inputs.py}, joestale-work/long-run-test/T-track/ch11_v2/{design.json, design.t051.json, t053/*}, 판정/T053_회귀/*, reports/11장 네 번째 판 (이야기 되살리기).md, 판독_11-25장.md, TASK.md, ROADMAP.md.
Check / target / result: test_check_text.py → ALL OK(L1 2·W10 1·W11 1·inference 2 추가). 새 판(11-07)은 여전히 R9·L1 위반, 세 번째 판은 W10. 회귀 ch11_v3: 문장 독자(G·H 추가)+눈 바 → 12/12(이전 2차 검수 0/12), 표본 7건은 뜻도 판독과 같음. 미검증: 옛 세트·v2 세트 재채점(눈 마에서 42·43이 눈 바로 옮겨 감), 네 번째 판 사용자 판독, 12~25장 적용.
미처리: 검수가 지우라 한 짐작 세 문장·"꺼림칙했다"·"염치없는 놈"은 사용자 판독 요구라 유지. 쌀 kg 6,000원, "쉰여덟 날", 사흘·닷새, 버너 10분(대장 수치, 사용자 판단 대기). 탄피 대화 유지(앞 장 이음).

## T-052 / 2026-11-10 / 세 번째 판 사용자 판독 13건 기록·진단, 회귀 세트 ch11_v3

Roadmap item: (0-2) 후속. 사용자 판독(세 번째 판: 끊김, 시간 건너뛰기, 위협·걱정·대화·짐작 부족, 낯선 말).
Result: 판독 12개 자리(T01~T12)를 `판독_11-25장.md`에 기록하고 원인 18~24를 적었다. 요지: ① L1 상한과 "넣으면 뺀다"가 이야기(주고받기·걱정·짐작)까지 덜었다 ② 시점 인물의 짐작·판단이 원칙 적용에서 빠졌다 ③ 시간 건너뛰기에 다리와 계기가 없다 ④ T03·T06은 검수 항목 42·43의 수정 예시가 본문이 된 것 ⑤ R9에 하한이 없다 ⑥ 낯선 말·지시어·동음이의를 묻는 독자 물음이 없다 ⑦ 2차 반영 뒤 본문은 검수 없이 나갔다. 회귀 세트 `regression/ch11_v3/` 신설. 본문·규칙은 고치지 않았다(방향 사용자 확인 대기).
Changed files: joestale-work/long-run-test/T-track/판독_11-25장.md, skills/joestale/regression/ch11_v3/*, TASK.md, ROADMAP.md.
Check / target / result: 세트 keys 13개가 text.txt에 모두 있음을 스크립트로 확인. 2차 검수 출력과 대조 → 같은 뜻 적중 0/12. 미검증: 새 세트로 검수자를 돌린 점수(규칙을 고친 뒤 잰다).

## T-051 / 2026-11-09 / 새 판 가독성 악화 대책: 밀도·분량 검증, 덜어내기 반영 규칙, 수락 관문, 패턴 48~51, 11장 세 번째 판

Roadmap item: (0-2) 후속. 사용자 판독(새 판 "가독성 최악" 12건) → 방향 A~E 의논 → 사용자 "그렇게 해"(밀도 잣대 1~10장).
Result: ① 검증기 R9 문장 밀도(서술문 평균 내용어 ≤7.9·절 ≤2.3·절3+ ≤35%, 1~10장 5.82~7.82/1.79~2.29/0.18~0.34로 보정), L1 반영 뒤 분량(`--draft`, 초고 ×1.05), W8 내용어 13+ 문장, W9 대사 -ㄴ다 종결. ② 반영 규칙 "넣으면 뺀다"·단 다시 쓰기(SKILL 4단계, reviewer-prompt 처리 규칙, D4). ③ 수락 관문 = 검증기 + 사용자 판독, 모델 블라인드는 모순 확인용(D4). ④ 패턴 48~51(위협 뒤 반응·사건 순간·단 주제 하나와 닫기·고치기는 바꾸기), 검수 항목 42·43 신설, 눈 가에 39 이동, 마 = 18·19·20·28·29·37·38·42·43. ⑤ 설계서 `stages[].topic`·`closing`, 최상위 `premises`. ⑥ 회귀 세트 `regression/ch11_v2/`(V01~V12). ⑦ 11장 세 번째 판: v2 초고(3,203자)에 같은 1차 지적 116건을 새 규칙으로 반영(107 처리, 전 단 다시 씀) → 3,267자 → 2차 검수 55건(50 처리) → **3,338자 PASS**, 밀도 5.8/1.74/0.13(새 판 8.3/2.36/0.39). 문장 독자 지적 48 → 17. `reports/11장 세 번째 판 (덜어내기 규칙).md`.
Changed files: skills/joestale/{SKILL.md, references/principles.md·reviewer-prompt.md·decisions.md·scene-design.md·design.template.json, scripts/check_text.py·test_check_text.py·build_review_inputs.py, regression/ch11_v2/*}, joestale-work/long-run-test/T-track/ch11_v2/{design.json, design.v2final.json, t051/*}, 판정/T051_회귀/*, reports/11장 세 번째 판 (덜어내기 규칙).md, 판독_11-25장.md, TASK.md, ROADMAP.md.
Check / target / result: test_check_text.py → ALL OK(R9 3·W8 1·L1 2·W9 2 추가). 새 판 final → R9·L1 위반, 1~10장 10장 전부 R9 통과, 옛 11장 R9 위반(절3+ 0.39). 회귀 옛 세트: 다섯 눈 15/27 유지(마 1→2), 연결 독자 새 G6 문구 9/10(C10 탄피 놓침) → 문구를 "닿는 자리를 적는다"로 되돌려 완화. 회귀 v2 세트: 독자·마 9/12 + 검증기 V01 + W9 V04 = 11/12, V06("무겁지")은 기계·독자 모두 못 잡음(사용자 판독만). 미검증: 세 번째 판이 사용자에게 읽히는가(밀도가 1~10장 하한 5.8이라 잘게 끊긴 느낌 가능), 12~25장 적용.
미처리(사용자 판단 대기): 쌀 kg 6,000원 시세, "쉰여덟 날" 표기, 패턴 42~51 확인, 2.9kg/통조림 7 산수.

## T-050 / 2026-11-07 / 검수 누락 대책 3종(정답지·기계 이관·눈 나누기)과 11장 새 판 비교

Roadmap item: (0-2) 후속. 사용자 지시("1번부터 차례로 작업해서 완료 후 글 생성 후 비교, 결과 보고").
Result: ① 검수 회귀 세트: `skills/joestale/regression/ch11/`(고정 본문·앞 장·독자 기억 장부·must_catch.json 27건 = 사용자 판독 15 + 독자 공통 2 + 연결 10)과 `scripts/score_review.py`. ② 기계 이관: check_text.py `--prev`로 G5(앞 장 문장 재사용, 내용어 4개 이상·절반 이상 겹침, `repeat_ok` 면제)와 W7(수치 되풀이 note). 옛 11장에서 G5 4건·W7 5건. ③ 눈 나누기: 41항목을 다섯 눈(가 문장 7 / 나 사실·이치 8 / 다 감정 치환 8 / 라 묘사·사물 5 / 마 구조·대사 8, 상한 9, 기계 항목 23·24·26·27·32 제외). `scripts/build_review_inputs.py`가 눈별·독자별 입력 파일을 만든다. ④ 쓰는 쪽 패턴 42~47(대사는 주고받는 말, 꼴과 하는 일, 바로 닿는 말, 전제 먼저, 도구와 결과, 하는 일 없는 문장·수치 되풀이)을 principles에 추가(사용자 판독에서 도출, 사용자 지시 범위 밖의 내 판단. 확인 pending). ⑤ 11장 새 판(T-track/ch11_v2): 옛 판·판독을 못 본 작성자가 새 절차로 집필 → 다섯 눈+두 독자 → 반영 2회.
Changed files: skills/joestale/{SKILL.md, references/reviewer-prompt.md·decisions.md·principles.md, scripts/check_text.py·test_check_text.py·score_review.py·build_review_inputs.py, regression/ch11/*}, joestale-work/long-run-test/T-track/ch11_v2/*, 판정/눈나누기/*, 판정/ch11_옛판_새판/*, TASK.md, ROADMAP.md.
Check / target / result: test_check_text.py → ALL OK(G5 4·W7 1 추가). 눈 나누기 → 한 명 41항목 17건·항목 11가지·정답지 5/27 vs 다섯 눈 40건·24가지·15/27. 첫 읽기 두 독자 → 정답지 25/27(놓침: "붕대요", 국 냄새). 11장 새 판 → 초고 3,203자(목표 3,600 미달), 최종 3,896자 PASS. 문장 독자 지적 48 → 31(1회 반영 뒤), 연결 독자 11 → 9(옛 판 17). 블라인드 견주기 2회(순서 교체): 새 판이 한 번에 읽힘 2/2·이치 2/2·종합 2/2, 옛 판이 군더더기 2/2, 대사·장면·다음 장은 1/1. 2026-11-09 사용자 판독: **새 판 가독성 최악**(단어 과다·겹문장, 무관한 삽입, 무미건조한 사건 순간, 서술체 대사, 장면 전환 생략, 주제 뒤섞임 등 12건, T-track/판독_11-25장.md). 측정: 반영 뒤 글자 +22%, 내용어/문장 6.6→7.3, 절/문장 2.12→2.28(1~10장 6.0~6.5/1.75~2.1). 모델 판정과 사용자 판정 불일치 확인. 미검증·열린 것: 2회차 41항목 재검수 생략(절차 이탈), 최종본의 문장 독자 재측정 25건(옛 판 44, 초고 48, 1회 반영 뒤 31; 이 25건은 반영하지 않음), 쌀값 6,000원·닷새→사흘·"쉰여덟 날"·가산량 셈은 사용자 판단 대기, 싼 모델로 눈을 돌려도 되는지 미측정.

## T-049 / 2026-11-07 / 첫 읽기 검수(문장 독자·연결 독자) 스킬 반영, continuity에 knows·used_scenes

Roadmap item: (0-2) 후속. 사용자 지시("둘로 나누는 것과 추적 파일에 더하는 것까지").
Result: 5-B단계 신설. 문장 독자(본문만, A~F)와 연결 독자(본문+독자 기억 장부 `reader_memory.md`, G1~G7)를 따로 띄움. 설계서는 둘 다 안 줌. 수정으로 들어온 문장도 문장 독자를 거침(3건 이상이면 1회 더, 최대 2회). 서브에이전트 불가면 미실시(같은 맥락 대체 없음). 스킬에 별도 추적 파일 규정이 없어 두 칸은 설계서 `continuity`에 넣음: `knows`(인물이 듣고 겪은 것), `used_scenes`(이미 쓴 장면·농담과 그 끝). 쓰는 규칙도 D2 앞 장 맥락에 추가.
Changed files: skills/joestale/SKILL.md, references/reviewer-prompt.md, references/decisions.md(D2 앞 장 맥락, D4 첫 읽기, D6 장부), references/scene-design.md, references/design.template.json, 판정/첫읽기_검수/(입력_문장독자.md, 입력_연결독자.md, reader_문장.md, reader_연결.md).
Check / target / result: test_check_text.py → ALL OK. 스킬 문구 그대로 11장 확인 시험 → 문장 독자 43건(사용자 15건 중 13, 놓침: "붕대요", 국 냄새), 연결 독자 17건(G5 재사용 7, G6 3, G2 2, G4 2, G1 1, G3 1, G7 1). 미검증: 지적을 반영해 고친 11장이 사용자에게 읽히는가, 12~25장, `knows`·`used_scenes`를 채우고 쓴 초고에서 G 지적이 줄어드는가. "붕대요" 같은 짧은 대사의 어감은 세 번 모두 못 잡음. 원인 확인: 대사의 하는 일과 문장 꼴만 견주게 한 독자는 "붕대요"를 첫 번째로 집음(대사 34개 중 11개 지적) → 못 보는 것이 아니라 지시가 넓어 밀린 것. 문장 독자에 '대사만 따로 한 번 더' 훑기를 추가함(합친 상태의 재현은 미검증).

## T-048 / 2026-11-06 / 사용자 판독(11장에서 중단)·첫 읽기 검수 시험

Roadmap item: (0-2) 후속.
Result: 사용자가 11장을 읽다 15건을 짚고 "더 읽을 가치가 없다"며 중단. 기존 검수(11장 지적 32건)는 15건 중 0건을 잡음. 뿌리: 첫 읽기에 뜻이 안 닿음(대사가 앞 말에 답하지 않고 정보를 전달, 함축하다 뜻을 잃음, 전제 생략, 수치 되풀이, 물리적으로 안 맞는 문장). 설계·대장 없이 본문만 읽는 '첫 읽기 검수' 프롬프트를 만들어 11장에 독자 둘로 시험: A(1~10장을 먼저 읽음) 43건, B(11장만) 45건. 사용자 15건 중 같은 문장을 짚은 것 A 14, B 13(둘 다 놓친 것은 "붕대요"). 사용자가 안 짚은 것도 다수(4장 문장·동작 재사용, 코펠과 컵 불일치, 7장 설명회와 어긋나는 대사, 쌀값 나눗셈 대사).
Changed files: joestale-work/long-run-test/T-track/판독_11-25장.md, joestale-work/long-run-test/판정/첫읽기_검수/(prompt.md, reader_A.md, reader_B.md, 입력 2), reports/1권 11~25장 본문 (T 트랙).md, TASK.md, ROADMAP.md.
2026-11-07 추가: 사용자 판정 — 과잉 지적 없음, 고친 문장 질 좋음, 다만 앞 장을 기억해 잇는 판단이 약함. 프롬프트 v2(독자 기억 장부를 먼저 쓰고 G '앞과 안 이어짐' 7갈래로 대조)로 독자 C 시험: 34건 중 G 13건. G 지적이 댄 앞 장 근거 11곳을 본문에서 확인, 전부 실재(4장 문장·동작 재사용 5곳, 7장 '조직 재생과 통각'을 잊은 대사, 8장 가산 안내를 잊은 대사, 10장 2회차 01-22를 아무도 안 꺼냄 등). 문장 단위 지적은 43→21건으로 줄어 사용자 15건 중 13건. 산출: 판정/첫읽기_검수/prompt.md(v2), prompt_v1.md, 기억_01-10.md, reader_C.md.
Check / target / result: 사용자 지적 재현 → 15건 중 13~14건(문장 기준). 정밀도(추가 지적 약 30건이 타당한가) → 사용자 판정 전. 스킬 반영·11장 수정 → 안 함, 사용자 결정 pending.

## T-047 / 2026-11-05 / (e) T 11~25장 이어 쓰기 완료·새 규정 측정

Roadmap item: (0-2) 후속 (e).
Result: T 세션(Opus)이 11~25장 15장을 새 규정(continuity·terms_introduced·추적 갱신 장마다·초고 3,600 5단 배분·검수 39~41)으로 집필. 전 장 PASS, 검수 2회. 초고 중앙값 3,163(1~10장 3,118), 3,000 미만 4/15, 3,600 도달 2/15, 보충 4, 재집필 0. 검수 지적 553(장당 37, 1~10장 22), 걸러냄 141(25.5%) — 주 사유는 앞 장에 이미 소개한 용어 재지적. 대장 밖 수치 첫 검증 196(장당 13). 절차 이탈 8건(세션 보고). 자체 결정 25건은 T-track/issues.md "자체 결정" 절, 사용자 확인 전. 보고서 절 추가. (f) 반영: reviewer 40번에 terms_introduced 수록 용어 제외·장비명 비ID 명시.
Changed files: skills/joestale/references/reviewer-prompt.md, joestale-work/long-run-test/T-track/ch11~ch25 (세션 산출), T-track/issues.md·log.md·tracking.json·세부개요_11-25장.md (세션), reports/장편 일관성 테스트 1권 1~10장.md(절 추가), TASK.md, ROADMAP.md.
Check / target / result: 분량 규칙 → 세션 작성자에게는 약함(T-046 서브에이전트 10/10 vs 세션 2/15). 걸러낸 비율 25.5% → 감당 가능하나 40번 문구 보강 필요(f). 대장 사후 추가 → 규정 미준수, 상한 후보(h).
Evidence: T-track/ch11~25/report.json(draft_chars, filtered_count, ledger_not_in_ledger_first_check), T 세션 최종 보고(2026-11-05 01:xx).
Limits: filtered는 세션 자체 판단, 독립 확인 없음. 최종 자수는 세션 표와 100~200자 차이(세션이 보충 전 값을 적은 듯). 11~25장 세부 개요는 세션이 만든 것이라 입력 동결본 밖. 블라인드 모순 판정은 아직 안 함. 커밋 안 함.
Required specialist verdict: not applicable.
Completion boundaries: 사용자 자체 결정 확인·11~25장 판독, (f)(g)(h) 결정.
Related issue / knowledge: T-045, T-046, I-26.
Record handoff gap: none.

## T-046 / 2026-11-04 / (c) 분량 규칙 검증: T 1~10장 초고 재생성 비교

Roadmap item: (0-2) 후속 (c) 증명.
Result: 같은 설계서(T-track design.json)로 초고만 새 규칙(3,600 5단 배분)으로 재생성(Opus 서브에이전트 10회, 검수·보충 없음). 글자 수 중앙값 3,118 → 3,606, 범위 2,779~3,721 → 3,214~3,619, 3,000 미만 4 → 0, 4,500 초과 0. 수식어 비율 평균 0.068 → 0.045, 문체 위반(G3 제외) 27 → 7, W1 긴 문단 63 → 13. 블라인드 채우기 판정(sonnet 2회 순서 교환): A 구 134·새 176, B 새 150·구 189 — 둘 다 뒤에 놓인 쪽이 많아 순서 편향, 합산 구 323·새 326으로 차이 없음. 부작용: 대장 밖 수치 23 → 60(걸음·발·초를 지어냄), 미등록 인명 0 → 19. 조치: D2 분량 행에 "채울 때 대장에 없는 수치를 만들지 않는다" 추가, SKILL 한 줄. 통과 판정 → (e) 진행.
Changed files: references/decisions.md, SKILL.md, joestale-work/long-run-test/판정/분량규칙_검증/ (ch01~10 draft_new·stages, measure.json, blind_A·B, 판정A·B.md, blind_key.txt), reports/장편 일관성 테스트 1권 1~10장.md(절 추가), TASK.md, ROADMAP.md.
Check / target / result: 통과 기준 3,000 미만 0·중앙값 ≥3,300·4,500 초과 0 → 충족. 수식어 차이 ≤0.01 → 오히려 감소. 채우기 블라인드 → 차이 없음.
Evidence: 판정/분량규칙_검증/measure.json, 판정A.md, 판정B.md.
Limits: 재생성은 서브에이전트(세션 기억 없음)라 인명·수치 대장 이탈 일부는 조건 차이일 수 있음. ch03은 3,214로 목표 미달(재료 소진 보고). 판정자 순서 편향이 커서 채우기 측정은 "차이 없음"까지만. 커밋 안 함.
Required specialist verdict: not applicable.
Completion boundaries: (e) 11~25장에서 초고 분포·G3 수치 재확인.
Related issue / knowledge: T-045, T-039.
Record handoff gap: none.

## T-045 / 2026-11-04 / (c) 장편 장 분량 규칙: D2 "분량 (E 본문 장)" 행, D4 보충 2회·재집필 기준

Roadmap item: (0-2) 후속 (c).
Result: decisions D2에 E 본문 장 3,000~4,500자(세부 개요 지정값 우선), 초고 목표 하한+20%(3,600자)를 5단 구성에 배분. D4 분량 note 행에 E 장은 보충 2회, 가장 짧은 단에 설계 재료로만, 초고가 하한 85% 미만이면 5단 배분을 고쳐 2단계 재집필. SKILL 5단계 한 줄. 글 생성 없음(규칙만).
Changed files: references/decisions.md, SKILL.md, TASK.md, ROADMAP.md.
Check / target / result: test_check_text.py 무관(검증기 미변경). 효과는 (e) 11~25장에서 초고 글자 수 분포로 측정.
Evidence: T-039 보고서 해석 4, N issues H, T log.md(초고 2,500~3,100).
Limits: 3,600 목표가 묘사 과잉을 부르는지 미확인. 커밋 안 함.
Required specialist verdict: not applicable.
Completion boundaries: (e)에서 측정.
Related issue / knowledge: T-039, T-044.
Record handoff gap: none.

## T-044 / 2026-11-04 / (d) 기획 입력 모순 정리: long-plan-input 동결 v2

Roadmap item: (0-2) 후속 (d).
Result: T·N 두 집필 세션의 issues.md(I1~I14, 1~10)와 15차 피드백에서 입력 모순 19건을 합쳐 16항목 24곳 수정. 원칙은 T 본문(본편)이 택한 쪽. 수정: 야간 발사 보고 시점, 태석 소개 문답(패턴 39), 탄피 회수 의무/눕혀 세기 버릇/책상 세움 양식, 1장 관건 50m·30m·발수 이유(패턴 41), 1회차 일시 공개 장, 3장 투시경 주체, 4장 별지 미룬 이유, 5장 채혈 장소·시간·사례(05 헌혈 사례 신설)·조사 오타, 6장 관측 하루 대신 맡기·합동 보급 점검, 7장 사본 수단, 8·9장 간호장교 교대 없음·12시간 안내·정우 입실, 유진 소개 자리, 10장 5단 순서, 교차_대조 #12. 원본은 `long-plan-input/원본_동결v1/`, 목록은 `long-plan-input/변경_기록.md`.
Changed files: long-plan-input/{01_세계관/01,05, 02_인물/01,02, 04_세부개요/1권_01-10장, 교차_대조}.md, 변경_기록.md(신규), 원본_동결v1/(신규), TASK.md, ROADMAP.md.
Check / target / result: 24곳 앵커 전부 1회 일치 후 치환. T 1~10장 본문과의 재대조는 안 함(T 선택에 맞췄으므로 어긋남 없어야 하나 미검증).
Evidence: 변경_기록.md 표.
Limits: 보류 3건(9장 K10 구절, N 탄피 이유, 05 혈장 채혈 주체 현실성). 2~5권 분권표·11~25장 장별표에는 손 안 댐. 커밋 안 함.
Required specialist verdict: not applicable.
Completion boundaries: (c) 장편 분량 행, (e) T 11~25장 이어 쓰기.
Related issue / knowledge: T-039, T-043, I-26.
Record handoff gap: none.

## T-043 / 2026-11-04 / 패턴 40 잔여 용어 7건 국소 수정(T 2·5·8·9장, N 1·9장) + continuity terms_introduced·검수 39/40 보강

Roadmap item: (0-2) 후속, I-27.
Result: 스킬 — continuity에 `terms_introduced`(독자에게 드러난 용어·관행 → 장·방식) 추가(decisions D2, reviewer 앞 장 맥락 절, template, scene-design), 검수 40에 설정 ID 유출·목록 밖 용어, 39에 질책·농담형 비껴감 명시. 본문 — T: 2장 TOD·가산 배급, 5장 회복자, 8장(추가) 동의서·처분 장면, 9장 처분 문장; N: 1장 TOD·탄피 제도, 9장 K5 ID 제거. 전부 PASS, 고친 문장에 39~41 지적 0. T tracking.json terms_introduced 47항목. 이전 판 final.v1.txt 보관.
Changed files: references/reviewer-prompt.md·decisions.md·design.template.json·scene-design.md, long-run-test/T-track/ch0{2,5,8,9}/*·tracking.json·report.json, N-notrack/ch0{1,9}/*·log.md, TASK.md, ROADMAP.md.
Check / target / result: 고친 곳 39~41 지적 0 → 통과. 고친 곳 밖 새 지적: T 3건(저확신), N 10건(1장 40 4·41 2·39 1, 9장 3) 미처리.
Evidence: 두 세션 보고(전/후 표), 판정/패턴39-41_검증/.
Limits: T 8장 동의서 장면(서술 2문장+대사 2줄, 수레에 양식이 있다는 설정)은 세션 선택 — 사용자 확인 전. N 9·10장 "눕혀서 세고, 세워 두면 굴러가"는 집필자가 붙인 이유가 물리적으로 거꾸로(눕힌 원통이 더 구름) — 미수정, 10장 연동 필요. 새 검수 항목이 용어 지적을 많이 냄(N 1장 4건) — 억지 비율 미측정. 커밋 안 함.
Required specialist verdict: not applicable.
Completion boundaries: 사용자 결정 2026-11-04 — T 본편, 8장 장면 수락, N 동결(탄피 이유 미수정). 닫힘.
Related issue / knowledge: I-27, T-041, T-042.
Record handoff gap: none.

## T-042 / 2026-11-04 / 1장 v2 재작성(Opus, T 세션) + 단면 수정 여부 검증(패턴 39~41 전수 스캔·연속성)

Roadmap item: (0-2) 후속, I-27.
Result: T-track/ch01 v2 3,672자 PASS(수식어 0.06, 검수 12→11·10→8), 15차 지적 5곳 전부 반영(v1은 final.v1.txt). 검증 ① 패턴 39~41 전수 스캔(sonnet): T 1장 v2 0건, T 2~10장 용어(40) 4건(TOD·가산 배급·회복자·처분/교상자), N 1~10장 3건(1장 TOD·탄피 제도 모순, 9장 지식 ID "K5" 본문 유출), 문답(39)·이유(41)는 1장 밖에서 0. ② 감도: 같은 스캔을 T 1장 v1에 돌려 사용자 지적 4건 중 3건 검출(AA 문답·총성 이유·탄피 제도) + 미지적 1건("손님" 은어), "셋 맞죠?" 비껴감은 질책으로 보고 미검출. ③ 연속성: v2가 바꾼 사실 14건 중 2~10장과 어긋남 0. 결론: 1장 국소 수정이 아니라 결함 유형이 1장(설정 노출이 가장 많은 장)에 집중돼 있었고, 나머지 장의 잔여는 용어 7건.
Changed files: long-run-test/T-track/ch01/*(v2, v1 보관, README), 판정/패턴39-41_검증/*, TASK.md, ROADMAP.md.
Check / target / result: v2 결함 0/0/0, 연속성 어긋남 0 → 통과. 스캐너 감도 3/4.
Evidence: 판정/패턴39-41_검증/scan39_T.md·scan39_N.md·scan39_T_ch01_v1.md·cont_v2.md, ch01/README.md.
Limits: 사용자 v2 판정 전. 2~10장 용어 7건 미수정. 스캐너가 질책형 비껴감을 못 잡음(검수 39 문구 보강 후보). 커밋 안 함.
Required specialist verdict: not applicable.
Completion boundaries: 사용자 v2 판정 → 용어 7건 국소 수정 여부.
Related issue / knowledge: I-27, T-041.
Record handoff gap: none.

## T-041 / 2026-11-04 / 15차 피드백 → 패턴 39~41(문답 호응·관행 첫 등장·이유 검산), 검수 39~41

Roadmap item: (0-2) 후속, Phase 0 사용자 수락.
Result: ISSUES I-27. principles 39·40·41 + 검사법(39~41). reviewer 39~41(항목 수 41). decisions D2 3행. scene-design 6-C ④에 첫 등장 관행·용어, 이유 검산 항목. SKILL 1원칙 한 문장. 판정 기록: T(추적 유) 판정승 — 문장·흐름; N은 모순 적음. 블라인드 모순 수(T 1·0 / N 2·2)와 사용자 판정이 어긋난 이유: 판정 유형에 문답 호응·용어 설명·이유 검산이 없었음.
Changed files: references/principles.md·reviewer-prompt.md·decisions.md·scene-design.md, SKILL.md, ISSUES.md, TASK.md, ROADMAP.md.
Check / target / result: test_check_text.py ALL OK(검증기 미변경). 패턴 효과는 T 1장 재작성 후 사용자 판정.
Evidence: I-27 피드백 원문.
Limits: 패턴 39~41은 검수자만 봄(기계 검사 없음). 커밋 안 함.
Required specialist verdict: not applicable.
Completion boundaries: T 1장 v2 재작성·판정 pending.
Related issue / knowledge: I-27, T-039, T-040.
Record handoff gap: none.

## T-040 / 2026-11-04 / 장편 본문 후속 (a) continuity 검수 입력, (b) 검수 34·36 강화 + 6장 재검수 검증

Roadmap item: (0-2) 후속.
Result: decisions D2 "앞 장 맥락" 행·D4 검수자 설계서 범위(+setting·continuity), reviewer 34(감각 차단 뒤 시각·경과 기간)·36(시점 인물 자신이 모르는 것의 단정·withheld_still) + "앞 장 맥락" 입력 절, design.template `continuity`, scene-design 6-C 본문 문장, SKILL 5단계. 검증: 기존 6장 재검수(sonnet) → 블라인드 모순 3건 전부 검출, 앞 장 대조 지적 23건 신규, 지적 수 장당 2~3배. 보고서 `reports/장편 일관성 테스트 1권 1~10장.md` 후속 절, 원문 `long-run-test/판정/재검수_ab/`.
Changed files: references/decisions.md·reviewer-prompt.md·design.template.json·scene-design.md, SKILL.md, long-run-test/판정/재검수_ab/*, reports/장편 일관성 테스트….md, ROADMAP.md, TASK.md.
Check / target / result: 기존 놓친 모순 3/3 검출 → 통과. test_check_text.py ALL OK(검증기 미변경). 억지 지적 비율 미측정.
Evidence: 재검수_ab/rr_*.md.
Limits: 재검수에서 continuity를 검수자가 직접 작성(규정은 작성자). T7 DEGRADED. 재생성 안 함. 커밋 안 함.
Required specialist verdict: not applicable.
Completion boundaries: (c) 장편 분량 행, (d) 입력 모순 20건, (e) 11~25장 연장은 미착수.
Related issue / knowledge: T-039, I-26.
Record handoff gap: none.

## T-039 / 2026-11-04 / (0-2) 장편 일관성 테스트 실행: 1권 1~10장, 추적 파일 유(T)/무(N), Opus 5.5

Roadmap item: (0-2).
Result: 두 세션(write-T-track·write-N-notrack)이 같은 입력으로 10장씩 집필(T 31,130자 / N 30,693자, 전 장 PASS). 블라인드 모순 수(sonnet 조건당 2회): T 1·0 / N 2·2. 유형은 시점(36) 2건·경과 기간(P1) 1건뿐, 추적 항목(위치·장비·수량·복선·지식)은 양쪽 0. 결론: 10장 범위에서 추적 파일 효과 미측정, 스킬 기본 절차로 일관성 유지됨. T는 절차 이탈(갱신 묶음, 5/10장만 파일 반영). 보고서 `reports/장편 일관성 테스트 1권 1~10장.md`.
Changed files: joestale-work/long-run-test/**(README·T-track·N-notrack·판정/), reports/장편 일관성 테스트 1권 1~10장.md, ROADMAP.md, TASK.md.
Check / target / result: 통과 기준 T ≤ N/2 → 숫자상 충족(0.5 vs 2)이나 바닥 효과. 결정 후보 (a)~(e)는 보고서.
Evidence: long-run-test/판정/*.md, T-track/log.md·tracking.json·issues.md, N-notrack/log.md·issues.md, 공유 노트 2건.
Limits: 판정자 sonnet·작성자 Opus(같은 계열). T 절차 이탈. 문장 품질 미측정(사용자 판독 전). 입력 모순 약 20건은 long-plan-input 동결본 결함으로 남음. 커밋 안 함.
Required specialist verdict: not applicable.
Completion boundaries: 사용자 결정 — 추적 파일 검수 입력 축소 도입(a), 검수 34·36 강화(b), 장편 분량 행(c), 입력 모순 처리(d), 11~25장 연장(e).
Related issue / knowledge: T-038, I-26, ROADMAP (0-2).
Record handoff gap: none.

## T-038 / 2026-11-04 / I-24 R4 "그립" 오탐 수정 + (0-2) 본문 1~10장 테스트 설계(추적 파일 유/무)

Roadmap item: P1-2 검증기, (0-2) 장편 일관성 테스트.
Result: check_text.py R4를 `is_emotion_token()`으로 분리(VA* 접두 일치 / NNG·XR 전체 일치 / lexicon `emotion_noun_homographs` 제외), lexicon 키 추가, test_check_text.py에 I-24 케이스 3건 → ALL OK. 테스트 설계 `joestale-work/long-run-test/README.md`(T 추적 유 / N 추적 무, 같은 입력·같은 모델 Opus 5.5, 장 3,000~4,500자, 측정 = sonnet 블라인드 모순 수 2회 + 검증기 + 비용, 통과 기준 T ≤ N/2) + `T-track/tracking.json` 초기값.
Changed files: scripts/check_text.py·test_check_text.py, references/lexicon.json, joestale-work/long-run-test/{README.md, T-track/tracking.json}, ISSUES.md(I-24 closed), TASK.md.
Check / target / result: 회귀 ALL OK. 집필 세션 2개는 Remote Control 환경 제한으로 시작 못 함(데스크톱 앱에서 입력 필요).
Evidence: test_check_text.py 출력, long-run-test/README.md.
Limits: 추적 파일은 테스트용 형식이고 스킬 규정 아님(결과에 따라 round5 반영). 커밋 안 함.
Required specialist verdict: not applicable.
Completion boundaries: 집필 세션 T·N 실행 → 판정 → 결과 기록이 남음.
Related issue / knowledge: I-24, I-26, T-037.
Record handoff gap: none.

## T-037 / 2026-11-03 / (0-2) 기획 입력 제작 ③·④ 검증(Opus 5.5) + 폴더명 변경

Roadmap item: (0-2) 장편 일관성 테스트의 고정 입력.
Result: A/B 세션을 목적 변경(제목 "장편 기획 입력 제작 (0-2)", 모델 Opus 5.5)해 ③ 권별 개요(5권 25장) + ④ 첫 10장을 생산. 폴더 `ab-test-world` → `long-plan-input`. 블라인드 모순 수(sonnet 2회, 순서 교환): A(live-test-long, Fable·구 스킬) 5·5 / B(long-plan-input, Opus·신 스킬) 1·0. B를 (0-2) 입력으로 채택. 보고서 `reports/장편 기획 반영 AB 테스트.md` ③④ 절, 판정 원문 `long-plan-input/판정/③④_*`.
Changed files: joestale-work/long-plan-input/**(세션 산출 + 판정/), reports/장편 기획 반영 AB 테스트.md, ISSUES.md(I-26), ROADMAP.md, TASK.md. 경로 참조 갱신(TASK·ROADMAP·보고서·공유 노트).
Check / target / result: 모순 수 B ≤ A → 충족. B 잔여 1건(2차 자격 단축 일수 45 vs 44) 미수정.
Evidence: 판정/③④_블라인드1_A먼저.md·③④_블라인드2_B먼저.md, 공유 노트 joestale-ab-b.md ③④ 절.
Limits: 모델 효과와 스킬 효과 미분리(A는 구 스킬). B 장별표 25장 vs A 45장. B 2차 수정분은 세션 내 재검수 없음(상한). B의 ① 영역별 점검표 "고친 초안" 6건은 실재하지 않는 인용(I-26). 커밋 안 함.
Required specialist verdict: not applicable.
Completion boundaries: 본문 테스트(1권 1~10장) 전 산수 1건 수정, (확인 필요) 10건 사용자 확인.
Related issue / knowledge: T-035, T-036, I-26.
Record handoff gap: none.

## T-036 / 2026-11-02 / I-25 반영: 6-C ① 뒤 검수·원본_v0 보관, 관문 고정 질문, 전제 요소 단서

Roadmap item: (0-3) 후속.
Result: scene-design 6-C 관문에 ① 고정 질문 3(허구 요소·핵심 설정의 모델 단계/연속·성장 경로)과 미응답 시 가정 표, ① 뒤 기획 문서 모드 검수 1회 + 검수 전 판 `원본_v0/` 보관, 1-B 현실 기본값에 "전제가 요구하는 요소는 제도의 변형으로 살린다" 단서. decisions D2 2행 갱신. reviewer 기획 문서 모드에 ① 전용 머리말(부재·확인 필요 값 비지적, 8·P5·P6·34 중심). SKILL 1-E 갱신. I-25 닫음.
Changed files: references/scene-design.md·decisions.md·reviewer-prompt.md, SKILL.md, ISSUES.md, ROADMAP.md.
Check / target / result: test_check_text.py ALL OK(검증기 미변경). 효과 재측정은 안 함.
Evidence: T-035 보고서 후속 후보 1~4 ↔ 위 변경.
Limits: 재발 ②(엽총)·③(편제 연도)는 규칙이 아니라 조사·지식 문제라 미대응. 커밋 안 함.
Required specialist verdict: not applicable.
Completion boundaries: (0-2)에서 재측정.
Related issue / knowledge: I-25, T-035.
Record handoff gap: none.

## T-035 / 2026-11-02 / 장편 기획 반영 A/B 테스트(1단계 세계관, 블라인드 2회 + v1 지적 재발 대조)

Roadmap item: (0-3) 후속, T-034 효과 측정.
Result: A(원본_v1, 반영 전) vs B(long-plan-input, 반영 후·자율 실행·검수 2회). 블라인드 P5+8 지적 수 A 14·17 / B 3·2(순서 교환, 출처 표기 제외 13·16 / 3·2). v1 사용자 지적 11건 유형: 재발 4(개조 고정 단계표·엽총 누락·2026 편제·부착물 경로)·해소 5·미다룸 2(자경단 미포함). 보고서 `joestale-work/reports/장편 기획 반영 AB 테스트.md`, 판정 원문 `long-plan-input/판정/`.
Changed files: joestale-work/long-plan-input/**(신규, 하위 세션 산출 + 판정/), reports/장편 기획 반영 AB 테스트.md, ISSUES.md(I-25), ROADMAP.md.
Check / target / result: 통과 기준 P5 절반 이하 → 통과(4~8배 감소). 재발 2건 이하 → 미달(4건). 첫 판정 2회는 지시문 오독(태그당 1건 상한)으로 폐기하고 재실행.
Evidence: 판정/블라인드1_A먼저.md·블라인드2_B먼저.md·v1지적_재발대조.md, 공유 노트 joestale-ab-b.md.
Limits: 판정자(sonnet)와 작성자가 같은 모델 계열. B는 검수 2회·A는 0회라 절차 효과와 검수 효과가 섞임(검수 전 판 미보관). 1단계만. 커밋 안 함.
Required specialist verdict: not applicable.
Completion boundaries: 후속 후보 4건은 I-25.
Related issue / knowledge: T-034, I-23, I-25.
Record handoff gap: none.

## T-034 / 2026-11-02 / oh-story 차용 5건 스킬 반영: E 기획 유형, 6-C 장편 기획 절차, 설정 현실성, 기획 문서 검수 모드

Roadmap item: Next eligible work (0-3) 후속, (0-2) 장편 일관성 테스트의 전제.
Result: ISSUES I-23 닫음. decisions D1에 유형 E 기획(판별 0순위), D2에 장편 기획 절차·설정 현실성·설계 축 관문·기획 문서 검수 4행, D5 E 출력 형식, D6 기획 폴더, D7 설계 축 관문 예외. scene-design 1-B에 허구 요소·현실 기본값·수치 출처 3행, 6-C 장편 기획(4단계 필수 항목 표: 지식 범위표+독자 기지 열, 압력선·시계, 복선 대장, 금지 공개, 교차 대조; JSON `planning`). reviewer-prompt 기획 문서 모드(본문 항목 4·8·34~38 + P1 날짜 사슬·P2 지식 범위·P3 금지 공개·P4 복선 대장·P5 설정 현실성·P6 수량 모순), 항목 수 표기 37→38 교정. design.template.json `planning` 블록. SKILL description·0단계·1-E단계. 비교 보고서 `joestale-work/reports/장편 기획 비교 JOESTALE vs oh-story.md`.
Changed files: references/decisions.md·scene-design.md·reviewer-prompt.md·design.template.json, SKILL.md, ISSUES.md, ROADMAP.md, reports/장편 기획 비교….md.
Check / target / result: test_check_text.py ALL OK(검증기 미변경), design.template.json 파싱 OK. 반영 내용의 효과(같은 전제 1단계 재실행 시 사용자 지적 수 감소)는 미측정.
Evidence: 비교 보고서 "차용 목록" 1~5 ↔ 위 파일.
Limits: 가져오지 않은 것(중국어 양식·regex 검사기·상업 공식·에이전트 7종)은 보고서에 명시. 지식 범위·복선·날짜 사슬 기계 검사는 없음(검수자만). I-24("그립" 오탐)는 별도. 커밋 안 함.
Required specialist verdict: not applicable.
Completion boundaries: 재검증(round5 기획 재실행) 전까지 효과 미확인.
Related issue / knowledge: I-23, oh-story 비교 분석, T-033.
Record handoff gap: none.

## T-033 / 2026-11-02 / 장편 기획 라이브 테스트(세계관·인물·권별 개요·첫 10장 세부, 본문 없음) — oh-story 비교용

Roadmap item: Next eligible work (0-2) 장편 일관성 테스트의 전 단계(기획 산출), oh-story 비교 분석 후속.
Result: `joestale-work/live-test-long/` 4단계 산출 17파일 105,058자(세계관 8·인물 2·개요 2·세부 1·규칙·비교·교차 대조·design.json) + 원본_v1 보존. 스킬이 규정한 것은 설계서(setting·대장·6-B·stake·가정 표)와 패턴 31·34·36·38뿐이고 분권·장 개요·세부 항목·설정 현실성 점검은 작성자 결정(가정 표 v2~v13). 1단계에서 사용자 지적 11회(탄약 화폐·개조 단계표·K14/K6·AK 밀수·엽총 누락·자경단 소탕·5.56·부착물·대여 고정 등) → 현실성 규칙 S1~S10 작성 후 전 항목 재도출, WebSearch 6건 정정, v1 대비 비교표. 교차 대조 모순 6건 수정(07 장면 배치 10장 가정, 시점 D2 위반 2곳 등). 검수자 서브에이전트 2회 지적 41건 → 처리 40건(실제 달력 요일, 지식 범위 위반, 탄피 구분 사실 오류, 인물 위치 모순).
Changed files: `joestale-work/live-test-long/**`(신규), 공유 노트 `joestale-long-test.md`, `ISSUES.md`(I-23·I-24), `ROADMAP.md`(0-3). `skills/joestale/`은 손대지 않음(반영안은 live-test-long/00_설정_현실성_규칙.md §4).
Check / target / result: check_text.py를 기획 문서 2건에 적용 → 본문 규칙 오적용(R4 "그립"→"그립다" 9건, G3 전권 대장 ↔ 장 단위 23건), 기획 문서용 검사 없음. 검수자 38항목 중 7개만 적용 가능. 설정 문서는 S6 점검표 + 조사로만 확인.
Evidence: live-test-long/교차_대조_결과.md(모순·검수 1·2차), 비교_v1_대비.md, design.json assumptions, 공유 노트 (a)~(f).
Limits: 본문 미작성(과제 범위). (확인 필요) 18건 잔존. 사용자 결정 보류 3건(김도현 3권 생사·10권 결말 갈래·로맨스 결말). 에밀리 첫 등장을 추천 축(25장)과 달리 3장으로 둠(인물 카드 고정, 사용자에게 보고). oh-story 산출물은 읽지 않아 비교는 노트 기준. 커밋 안 함.
Required specialist verdict: not applicable.
Completion boundaries: 4단계 산출·검수 complete / 사용자 수락 pending(단계 확인 "계속" 3회는 진행 승인이지 수락 아님) / 스킬 반영 pending(사용자 결정).
Related issue / knowledge: I-23, I-24, 00_설정_현실성_규칙.md §4, reports/oh-story 비교.
Record handoff gap: none.

## T-032 / 2026-10-31 / round4 v3: 14차 피드백(감정 부재) → 패턴 38 걸린 것·온기, 단편 재작성

Roadmap item: Phase 0 user acceptance(round4).
Result: ISSUES I-22. principles 패턴 38(시점 인물에게 걸린 것: 원하는 것·위협 장면·잃기 전 온기 장면·바람/두려움 독백) + 검사법(35~38). reviewer 38항목. scene-design 6-B에 `structure.stake`(wants·threat·warmth·feeling_monologue), design.template.json 반영. decisions 1줄. SKILL 1단계·서열 문단(패턴 8~38). round4 D v3 1,847자 PASS(온기 장면·'할아버지?'·'할아버지는요'·결말 되받기). 검수(38항목) 12건 → 5건 반영(손등 주어, 첫 문단 사실화, 차가움 연어, 전언 표지, '주무시는 거겠지' 독백), 7건 보류(v2 수락 문장). 13차 피드백(35 문구·37 정의 교정)도 이 턴 직전에 반영.
Changed files: round4/D/* (v2 보관 *.v2.*), round4/README.md, references/principles.md·reviewer-prompt.md·scene-design.md·decisions.md·design.template.json, SKILL.md, ISSUES.md.
Check / target / result: PASS(수식어 비율 0.04), 테스트 ALL OK(검증기 미변경). note: W5 서술문 8개 연속(열다섯 장째~안 온 날 첫 두 문장, 사건 연속이라 유지), W1 5~6문장 문단 5개(사건 진행, 반복 묘사 아님).
Evidence: round4/README.md v3, review.md, chain.md v3, design.json structure.stake.
Limits: 패턴 38은 검수자만 봄(기계 검사 없음). 감정 유무는 사용자 판정 대상. 커밋 안 함.
Required specialist verdict: not applicable.
Completion boundaries: round4 v3 사용자 "통과"(2026-11-01) → examples/round4/D 승격. 커밋 pending.
Related issue / knowledge: I-22, 패턴 38.
Record handoff gap: none.
