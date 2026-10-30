# Open problems and workarounds

Active issues: I-2, I-4. (I-3 closed 2026-10-29; I-5~I-9 closed 2026-10-30 T-006; I-10~I-11 closed 2026-10-30 T-007; I-1 closed 2026-10-30 T-009)

## I-10 / 검수 프롬프트 항목 7이 "구절이 없다"를 지적하게 만듦

Status: closed. Closed reference: 2026-10-30 worked-A·C 1차 검수에서 검수자가 작가 예문 9구절이 "본문에 없다"고 지적(의도의 반대). reviewer-prompt.md 항목 7을 "복제 금지 검사. 들어 있으면 지적, 없는 것이 정상"으로 고치고, 세부 위치(창가·승강장)와 간접 인용 시제는 지적 대상이 아님을 명시. 2차 검수에서 확인 (TASK T-007).

## I-11 / 검증기 G1이 사전 단어 "창가"를 창+가로 오인

Status: closed. Closed reference: 2026-10-30 어절 전체가 명사 한 토큰이면 제외. 회귀 테스트 추가 (TASK T-007).

## I-1 / 우리말샘 오픈 API 약관·호출 제한 미확인

Status: closed. Closed reference: 2026-10-30 키 발급(환경변수 OPENDICT_KEY, 기록 없음)·약관 확인·실제 응답으로 lookup_synonyms.py 검증(TASK T-009). 호출 한도는 문서에 없고 실측 20회 연속 정상. 출처 표기 규칙은 README 데이터 출처 절.
Affected roadmap item: ROADMAP.md P2-1.
Cause: API 안내 페이지에 라이선스 본문·호출 제한이 없음.
Workaround: 약관·저작권 정책은 2026-10-30 확인(Library/research.md): 텍스트 CC BY-SA 2.0 KR, 개인 작문 보조 사용 가능, 문학 용례는 미사용. 호출 한도는 문서에 없어 키 발급 후 실제 응답(오류 코드 021 일시 정지)으로 확인.
Residual risk: 유료 서비스화 시 약관 12조 상업 활동 금지 조항 해석 필요. 호출 한도 미확인.
Closure condition: 인증키 발급 + 첫 실제 응답 3건 캡처(P2-1) + 리포트에 출처 표기("우리말샘, 국립국어원, CC BY-SA 2.0 KR") 규칙 추가.
Verification: Library/research.md 2026-10-30 항목.
Next action: 사용자가 kdict 계정으로 로그인 후 /service/openApiRegister 신청 → OPENDICT_KEY 환경변수 등록.

## I-2 / JOENESS 개인 설치본 소유권 불일치

Status: mitigated.
Affected roadmap item: no stage impact.
Cause: `~/.codex/skills/joeness-setup`이 `작업하네스` 소스 패키지와 다른 패키지에서 설치됨. `JOENESS.ps1 -Check` → blocked.
Workaround: 이 프로젝트는 GitHub 최신본 클론(`D:\JOEWRKS\.local\joe-latest-20261029`)을 `D:\JOEWRKS\.claude\skills` 정션으로 사용. 개인 설치본은 건드리지 않음.
Residual risk: Codex 세션은 구버전 개인 설치본을 계속 사용.
Closure condition: 문서 절차(백업 → 기존 패키지 -Remove → 최신 패키지 -Apply)로 개인 설치 갱신.
Verification: TASK T-002.
Next action: 사용자 결정 후 진행.

## I-3 / 조사 검사 ㄹ받침 뒤 "으로" 미검출

Status: closed.
Affected roadmap item: P0-2.
Cause: `prototype/josa_check.py`가 ㄹ받침 뒤 "으로"를 정상으로 처리하는 분기 오류.
Workaround: none.
Residual risk: none.
Closure condition: `scripts/check_text.py`에서 수정 후 주입 오류 5/5 검출.
Verification: TASK T-003, examples/before-after.md (5/5).
Next action: none.
Closed reference: 2026-10-29 `check_text.py` josa_errors에서 ㄹ받침+으로를 오류로 분기. `prototype/josa_check.py`는 이력으로 보존.

## I-4 / Kiwi 오타 교정 모드가 문학 어휘를 오타로 오인

Status: mitigated.
Affected roadmap item: P0-2.
Cause: `typos='basic'`이 "녹슨"을 "녹+쓰"로 분석.
Workaround: 오타 모드 사용 금지. 띄어쓰기는 `kiwi.space()` 결과를 보고만 하고 자동 수정하지 않음.
Residual risk: 실제 오타는 2층 검수자(LLM)에 의존.
Closure condition: 대안 오타 검사기 평가 또는 범위 밖 확정.
Verification: TASK T-001.
Next action: Phase 1에서 결정.

## I-5 / check_text.py 오탐 2종: 관형사형 어미를 조사로, 의성어를 고유명사로

Status: closed. Closed reference: 2026-10-30 G1은 어절 분석에 어미(E*)·용언(V*)·XSV/XSA가 있으면 제외(XSM은 유지해 "손톱로" 검출 보존). G3 미등록 이름은 2회 이상·2글자 이상·허용 부사/감각어 제외로 한정. 회귀 테스트 3건 추가, draft.v0 재검사에서 오탐 0 (TASK T-006).
Affected roadmap item: P0-2, P1-2.
Cause: G1이 정규식으로 "잡는"의 "-는"(관형사형 어미)을 조사로 보고 받침 규칙 위반 판정. G3가 Kiwi NNP 태그를 그대로 믿는데 Kiwi 0.24.1이 "치익", "웅"을 NNP로 태깅.
Workaround: 문장을 바꿔 피함("쉭", "웅웅", "비워 두는 버릇"). 원칙과 무관한 수정이라 본문을 비틀게 됨.
Residual risk: 조사 검사를 Kiwi 형태소 태그 기반으로 바꾸지 않는 한 동사 어간+는/은 문장마다 오탐. 의성어·의태어를 쓰는 글마다 G3 오탐.
Closure condition: G1을 조사(J*) 태그 토큰에만 적용, G3는 NNP 중 1~2음절 의성어(또는 lexicon 허용 목록)를 제외. test_check_text.py에 두 사례 추가 후 오탐 0.
Verification: TASK T-005, joestale-work/live-test-D/check.round1.json.
Next action: Phase 1 보강 시 check_text.py 수정(사용자 승인 후).

## I-6 / G3가 본문 숫자의 대장 누락을 못 잡음

Status: closed. Closed reference: 2026-10-30 `number_expressions()`가 NR·SN·수관형사+단위를 모아 대장과 양방향 대조(`number_not_in_ledger`). 수량 1(한 번, 하나)은 제외하기로 결정(scene-design.md 대장 규칙 갱신). 회귀 테스트 2건 (TASK T-006).
Affected roadmap item: P0-2.
Cause: G3는 대장 → 본문 포함 여부와 미등록 NNP만 검사. 본문에 나온 수치("둘째 날", "한 칸")가 대장에 없는 경우는 검사하지 않음. scene-design.md는 "본문에 나올 수치 전부"를 대장에 요구.
Workaround: 5단계 검수자가 체크리스트 4로 잡음(이번에 2건).
Residual risk: 검수가 DEGRADED일 때 대장과 본문의 숫자 불일치가 남음.
Closure condition: G3가 본문의 NR·SN·수관형사+단위 토큰을 모아 대장 numbers와 대조하고 누락을 보고.
Verification: TASK T-005, report.json review.items.
Next action: I-5와 함께 수정.

## I-7 / decisions.md D2 분량 규칙 모호: "짧은 단편", 글자 수 단위

Status: closed. Closed reference: 2026-10-30 D2에 충돌 시 작은 범위 우선, 공백 포함·줄바꿈 제외, 범위 밖은 위반 아님(리포트 표기)으로 고정. check_text.py가 글자 수를 출력 (TASK T-006).
Affected roadmap item: P1-3.
Cause: D2 분량(D)에 "단편"(1,500~2,500)과 "짧게"(400~700)가 둘 다 걸릴 때 우선순위가 없고, 글자 수의 공백 포함 여부가 없음.
Workaround: T-005에서 "단편 범위 하한 약 1,500자"로 가정하고 가정 표에 적음. 결과는 공백 포함 1,229자.
Residual risk: 같은 요청에 세션마다 분량이 다름.
Closure condition: D2에 충돌 시 우선순위(예: 작은 범위 우선)와 글자 수 단위를 적는다.
Verification: TASK T-005.
Next action: 사용자 결정.

## I-8 / 0단계 사물 시드: D 유형 입력에 구체 명사가 없을 때 규칙 없음

Status: closed. Closed reference: 2026-10-30 lexicon.json `seed_objects` 30개 추가, D2에 "입력 길이 mod 30 번째" 결정적 선택과 결합 시드 키워드 집계 기준(경로 문장의 senses 키워드 수) 명시 (TASK T-006).
Affected roadmap item: P1-3.
Cause: SKILL.md 0단계 ①은 "입력 속 구체 명사 1개"를 요구하나 "짧은 단편 하나 써줘"에는 구체 명사가 없음. D2 결합 시드 선택 기준 "비시각 감각 키워드 수"도 무엇(경로 문장/후보 단어)을 세는지 없음.
Workaround: 작가 5단계(눈앞 사물)로 대체해 임의 선택(전기밥솥), 감각 키워드는 경로 문장에서 셈. 가정 표에 기록.
Residual risk: 시드 선택이 재현되지 않음.
Closure condition: decisions.md에 "입력에 구체 명사가 없으면 lexicon senses 또는 고정 사물 목록에서 고른다"와 키워드 집계 기준을 적는다.
Verification: TASK T-005, design.json assumptions.
Next action: 사용자 결정.

## I-9 / 4·5단계 처리 규칙 공백: 검증기 오탐, 설계서 수정형 지적, 재검수

Status: closed. Closed reference: 2026-10-30 D4에 오탐 보고(문장 불변, `PASS(오탐 n건 제외)`), 설계서 수정형 지적(design.json 수정 후 3단계 재실행), 재검수 기준(지적 3건 이상이면 1회, 최대 2회), 검수자 설계서 범위(ledger·banned_targets·assumptions) 추가. D5 리포트에 회차별 위반 수·오탐 보고·재검수 행 추가. reviewer-prompt.md 처리 규칙 동기화 (TASK T-006).
Affected roadmap item: P1-3.
Cause: 4단계는 "위반 문장만 고친다"뿐이라 오탐(I-5)도 문장을 바꾸게 됨. 5단계 지적 중 설계서(대장) 수정으로 끝나는 것(I-6 사례)의 처리, 반영 후 재검수 여부, 검수자에게 주는 설계서의 형식·범위(JSON 전체/표, 가정 표 포함 여부)가 없음. D5 리포트의 "초고/최종" 2열에 중간 회차 수치 자리가 없음.
Workaround: T-005에서 오탐은 문장 교체, 대장 지적은 design.json 수정, 재검수 생략, 설계서는 JSON 축약본, 중간 회차는 report.json `rounds`에 기록.
Residual risk: 세션마다 처리가 달라짐.
Closure condition: decisions.md D4·D5와 reviewer-prompt.md 처리 규칙에 네 경우를 적는다.
Verification: TASK T-005, report.json grey_zones.
Next action: 사용자 결정.
