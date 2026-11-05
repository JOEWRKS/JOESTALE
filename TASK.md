# Work results

닫힌 항목 T-001~T-031은 [TASK-archive.md](TASK-archive.md)로 이동(2026-11-02). 여기에는 열린 항목만 둔다.

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
