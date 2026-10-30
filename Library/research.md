# 조사 자료 — JOESTALE

상세 본문은 [기획서.md](../기획서.md)에 한 번만 둔다. 여기는 주제별 색인과 확인일·사실/추론 구분.

## 작가 원칙 (허관 @huh_kwan)

- 「글쓰기팁(어휘)」 https://www.threads.com/share/F2snI4M8r/ — 확인 2026-10-29. 사실: 주장 3개, 예문 4쌍 원문. 추론: 변환 패턴 6개(기획서 §1.2).
- 「소재를 낚는 5단계」 https://www.threads.com/share/JCOilU5AV/ — 확인 2026-10-29. 사실: 절차 5단계, 작가·댓글 예시. 추론: 0단계 소재 낚기 설계(기획서 §3-B).
- 범위: 작가 글은 원칙·예문 인용(출처 명시)만. 문체 복제 학습 대상 아님.

## AI 창작 한계·검증기 연구

- Hicke et al., The Zero Body Problem, arXiv 2504.06393 (2025) — 초록만 확인. 사실: 대부분 모델이 사람보다 감각어 적음, 선형 프로브로 식별 가능, instruction tuning 억제 예비 증거.
- Shrinking Landscape of Linguistic Diversity, arXiv 2502.11266 (2025) — 검색 요약 기준. 사실: LLM 윤문이 지배 문체로 수렴.
- StoryScope arXiv 2604.03136 / 중국 웹소설 arXiv 2603.14430 (2026) / 반론 arXiv 2512.13697 — 검색 요약 기준, 원문 미열람.
- Verifier-Assisted Generation (ICML 2025) / Iterative Refinement arXiv 2504.10391 — 검색 요약 기준. 추론: 측정기=검증기 구조 정당화. 한계: 문학 품질은 측정 안 함.

## 한국어 데이터·도구

- 우리말샘 오픈 API https://opendict.korean.go.kr/service/openApiInfo — 확인 2026-10-29. 사실: search/view 엔드포인트, view의 relation_info, JSON 지원, 32자 키. 미확인: 호출 제한(ISSUES I-1).
- 우리말샘 약관·저작권 — 확인 2026-10-30 (https://kdict.korean.go.kr/info/terms, /info/copyright). 사실: 텍스트는 **CC BY-SA 2.0 대한민국**(저작자 표시, 동일조건변경허락; 상업적 이용·변경 허용). 출처 표기된 문학 용례는 원저작자 권리 → 도구에서 **용례(exam) 미사용**. 멀티미디어는 항목별 정책. 약관 12조①11 "서비스를 이용한 상업 활동 금지"가 저작권 정책의 상업 이용 허용과 긴장 → 개인 작문 보조는 문제없고, 유료 서비스화 시 국립국어원 문의 필요. 호출 한도·캐시 규정은 두 문서에 없음. 키 신청 페이지(/service/openApiRegister)는 kdict 계정 로그인 필수(ID/비밀번호만, 소셜 로그인 없음).
- ETRI 다의어 API https://data.go.kr/data/15144928/openapi.do — 검색 요약 기준.
- 모두의 말뭉치 — 약정서 승인제. 2019 웅진북센 사건·2022 판결(https://bizhankook.com/articles/woongjin-loses-ai-copyright-lawsuit.html). 추론: 현대 소설 말뭉치는 상업 사용 시 약관 필수.
- 저작권 만료 작가(김유정·이상·현진건, 1937~1943 사망) — 일반 지식, 공유마당 미확인.
- 음성상징어 4,622개 연구 https://dspace.ewha.ac.kr/handle/2015.oak/190066 ; 감각표현 형태론 https://www.earticle.net/Article/A301344 — 검색 요약 기준.
- kiwipiepy 0.24.1 (Python 3.14, 이 PC 설치) — 실측 2026-10-29. 사실: 형용사 VA-I/VA-R, 파생형용사 XR+XSA, 일반부사 MAG, 관형사 MM. 오타 모드 부적합(ISSUES I-4). 태그 안내 https://wikidocs.net/313963.

## 실측 기록

- 수식어 비율 전→후: 기획서 §1.3 표. 스크립트 `prototype/modifier_ratio.py`.
- 조사 오류 검출: 기획서 §3-C 표. 스크립트 `prototype/josa_check.py`. 결과 4/5, 오탐 0, ㄹ받침 버그(ISSUES I-3).

## JOE 도구

- 최신본 클론 `D:\JOEWRKS\.local\joe-latest-20261029\` (JOENESS 1.1.0 @2fa204b, JOEFLOW 1.2.0 @134a13c, JOEDESIGN 1.0.0 @ce20826) — 2026-10-29.
- 사용 마찰 기록: `D:\JOEWRKS\.claude-worktrees\_data\joe-tools-friction-log.md` — JOEFLOW FREEZE 비용, Windows 인코딩, 서브에이전트 규칙 충돌.
