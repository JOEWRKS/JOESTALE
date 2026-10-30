# 사용자 작업 안내 (2026-10-30)

스킬이 스스로 못 하는 세 가지. 각각 왜 필요한지, 어떻게 하는지, 끝나면 무엇을 하는지.

## 1. 우리말샘 오픈 API 인증키 발급 → Phase 2 (ISSUES I-1)

왜: 소재 낚기의 "두 단어가 관계 없음" 판정과 리라이트 시 유의어·하위어 조회를 기계화하려면 사전 API가 필요하다. 키가 없으면 지금은 LLM 판단으로 대신한다.

어떻게:
1. https://opendict.korean.go.kr 접속 → 로그인(회원가입 필요, 네이버·카카오 연동 가능).
2. 하단 또는 「우리말샘 소개」 메뉴의 **오픈 API** → 「오픈 API 사용 신청」(https://opendict.korean.go.kr/service/openApiRegister, kdict 계정 로그인 필요). 기입값: 서비스명 **JOESTALE**, 서비스 URL **https://github.com/JOEWRKS/JOESTALE**, 사용 목적 "개인 작문 보조 도구에서 단어의 비슷한말·반대말·상위어를 조회해 어휘 선택을 돕는 용도(개인·비영리)". "AI 학습" 표현은 쓰지 않는다(용도는 조회).
3. 발급된 32자 키를 **파일에 적지 말고** 환경변수로 등록:
   ```powershell
   [Environment]::SetEnvironmentVariable('OPENDICT_KEY', '<발급키>', 'User')
   ```
   새 터미널·새 세션부터 적용된다.
4. 같은 페이지의 **이용 약관·저작권 정책** 두 링크를 읽고, 다음 두 가지만 확인해 알려 주면 된다: (a) 일일 호출 한도가 있는지 (b) 조회 결과를 도구 안에서 사용·캐시하는 것이 허용되는지.

끝나면: "우리말샘 키 등록했어"라고 말하면 `lookup_synonyms.py 경첩`으로 실제 응답을 받아 필드명을 검증하고 P2-1을 닫는다.

## 2. 공유마당에서 저작권 만료 작가 텍스트 확보 → Phase 3

왜: 지금 수식어 비율 상한 0.18은 작가 예문 4쌍만으로 정한 값이다. 실제 소설 수십 편으로 보정해야 하고, 저작권 문제 없이 쓸 수 있는 텍스트는 사후 70년이 지난 작가 것뿐이다.

어떻게:
1. https://gongu.copyright.or.kr (공유마당) 접속 → 검색창에 **김유정**, **이상**, **현진건**(또는 채만식·이효석; 1956년 이전 사망 확인).
2. 결과에서 「어문」 유형, 이용 조건이 **만료저작물** 또는 **CC BY**인 것만 고른다. 각 작품 페이지에서 텍스트(TXT·PDF·HWP) 다운로드.
3. 작가별 폴더로 저장: `D:\JOEWRKS\author-voice-skill\corpus\<작가명>\<작품명>.txt` (UTF-8). PDF·HWP는 그대로 두면 변환은 스킬 쪽에서 한다.
4. 작품마다 출처 URL과 이용 조건을 `corpus/SOURCES.md`에 한 줄씩. 공유마당에서 못 찾으면 국립중앙도서관 디지털컬렉션(https://www.nl.go.kr)도 같은 기준으로 확인.

최소량: 작가 3인 × 단편 3편 이상. 끝나면: "코퍼스 넣었어"라고 말하면 측정표를 만들고 임계값을 보정한다(P3-1).

## 3. Phase 0·1 수락 판정

왜: 기술 검증은 끝났지만 "작가의 어휘로 썼는가"는 사용자가 읽고 판단할 일이다. 이 판정이 Phase 4 블라인드 비교의 첫 기준점이 된다.

어떻게: 아래 넷을 읽고 각각 한 줄만 답한다. 좋다/아니다와 걸리는 문장 하나.
- `skills/joestale/examples/before-after.md` (작가 예문 4쌍 재현)
- `skills/joestale/examples/worked-B/final.txt` (비 오는 날 재회)
- `joestale-work/live-test-D/final.txt` (짧은 단편, 밥솥)
- `skills/joestale/examples/worked-A/draft.txt`, `worked-C/draft.txt` (리라이트, 의견→장면)

끝나면: 답을 ROADMAP "User acceptance"에 기록하고, "아니다"로 꼽힌 문장은 규칙 보강 후보가 된다.

## 하지 않아도 되는 것

- Codex 쪽 JOENESS 개인 설치 갱신(I-2): Claude 세션에는 영향 없음.
- `~/.claude/skills`로 joestale 개인 설치: 다른 프로젝트에서 쓸 때만. 이 프로젝트 안에서는 정션으로 이미 로드됨.
