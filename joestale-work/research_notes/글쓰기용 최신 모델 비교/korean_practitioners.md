# 한국어 소설·창작 산문용 최신 프런티어 모델 비교 — 한국 실무자·커뮤니티·리더보드 조사 (기준일 2026-11-01)

> 조사 범위: OpenAI GPT-5.6 계열(Codex "Sol"/"Terra"/"Luna") 및 GPT-6 계열("Astra", "Sol", "6.1 Sol") vs Anthropic Claude Opus 5.5 / Fable 5.1 (+ 이전 세대 Opus 5, Sonnet 5.5, Opus 4.x 비교 보강).
> 모든 주장은 **일화(anecdote)** 와 **측정(measurement)** 을 구분해 표기했고, 인용은 원문 그대로다.

## 0. 모델 명칭·세대 정리 (조사 중 확인된 사실 — 보고서 작성 시 반드시 반영)

### Takeaway
과제 지시문의 "GPT-5.6 Astra/Sol"은 실제 명명과 어긋난다. 2026-11-01 기준 OpenAI 라인업은 **GPT-5.6 계열(Sol·Terra·Luna, 2026-06/07 출시)** 과 **GPT-6 계열(Astra 2026-09-03/04, GPT-6 Sol 2026-09-22/23, GPT-6.1 Sol 2026-09-29/30)** 두 세대다. "Astra"는 GPT-6 세대 이름이며 GPT-5.6에는 Astra가 없다. 커뮤니티 글들도 "GPT-6 Sol", "GPT Sol 6.1"처럼 세대 표기가 뒤섞여 있어 아래 노트에서는 각 출처가 쓴 표기를 그대로 두고 괄호로 세대를 붙였다.

### Cited Findings
- GPT-5.6 계열은 Sol(플래그십)·Terra(일상용)·Luna(저가·고속) 3티어이며 API ID는 `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-5.6`은 `gpt-5.6-sol`의 별칭. "the number identifies a model's generation" — [continuumcode.ai Codex models guide](https://continuumcode.ai/guides/codex-models/) (3rd-party 가이드, 2026). 제한 프리뷰 2026-06-26 — [9to5Mac 2026-06-26](https://9to5mac.com/2026/06/26/openai-upgrading-chatgpt-and-codex-with-new-gpt-5-6-models-in-limited-release/); 나무위키는 "GPT-5.6 (2026년 7월 10일 KST 공개)" — [나무위키 GPT-5](https://namu.wiki/w/GPT-5).
- GPT-6 Astra: 2026-09-03(PST) 제한 공개, 09-04(KST) 일반 출시 — [CNBC 2026-09-03](https://www.cnbc.com/2026/09/03/open-ai-astra-gpt-6-cyber.html); [인공지능신문](https://www.aitimes.kr/news/articleView.html?idxno=41756); [나무위키 GPT-6](https://namu.wiki/w/GPT-6).
- GPT-6 Sol 2026-09-23(KST), GPT-6.1 Sol 2026-09-30(KST, DevDay) — [나무위키 GPT-6](https://namu.wiki/w/GPT-6).
- Claude 측 출시일(나무위키 기준): Opus 4.7 2026-04-16, Opus 4.8 2026-05-29, Fable 5 2026-06-10, Opus 5 2026-07-25, Fable 5.1 2026-09-01, Opus 5.5 2026-09-23(KST; Anthropic 발표 09-22), Sonnet 5.5 2026-09-29 — [나무위키 Claude/모델](https://namu.wiki/w/Claude/%EB%AA%A8%EB%8D%B8); Opus 5.5 09-22 출시 — [Anthropic](https://www.anthropic.com/claude-opus-5-5), [litmers 2026-10-07](https://litmers.com/blog/claude-opus-5-5-%EC%B6%9C%EC%8B%9C-%EC%B4%9D%EC%A0%95%EB%A6%AC-%EA%B0%80%EA%B2%A9-%EB%B2%A4%EC%B9%98%EB%A7%88%ED%81%AC-%EC%8B%A4%EC%A0%9C-%ED%9B%84%EA%B8%B0).

### Inferences
- "GPT-5.6 Sol"은 Codex CLI에서 실제로 선택 가능한 모델이고(oh-story PR #494가 사용), "Astra"는 ChatGPT/API의 GPT-6 플래그십이다. 파이프라인에서 Codex 쪽 모델 선택을 논할 때는 GPT-5.6 Sol ↔ GPT-6 Sol/6.1 Sol 교체 시점(2026-09-23 이후)을 구분해야 한다.

### Gaps
- OpenAI 공식 문서로 Codex 기본 모델이 11월 현재 `gpt-5.6-sol`인지 `gpt-6.1-sol`인지 확인하지 못했다(3rd-party 가이드만 확인).

---

## 1. 한국 작가·커뮤니티는 GPT-5.6/GPT-6와 Claude 5.x를 한국어 소설에서 어떻게 비교하는가?

### Takeaway
2026년 가을 한국 커뮤니티의 공통 서사는 (a) GPT는 5.5→5.6에서 한국어가 크게 좋아져 "예전 Claude급"에 근접했지만 스토리 구성·분량/페이스 조절은 여전히 약하고, (b) Claude는 한국어 이해도·전개·감정선이 가장 낫다는 평이 지속되나 Opus 4.7~5에서 **번역체가 오히려 악화**됐고 Opus 5.5에서 "간만에 작문 개선"·"해요체 과다"·"사족/반박 끼워넣기"가 보고된다. 모두 **익명 커뮤니티 일화** 이며 표본 수가 없는 체감 보고다. 문피아·조아라 작가 커뮤니티의 직접 발언은 공개 검색으로 찾지 못했다.

### Cited Findings

**(일화) 나무위키 — 커뮤니티 편집 위키, 사용자 체감 집약 (문서 자체가 부정확 가능성 명시)**
- GPT 전반(대조 서술, Claude 문서 내): "GPT-5.5, GPT-5.6부터 예전 Claude에 버금갈 정도로 상당히 자연스러운 한국어를 구사할 정도로 바뀐 것과 대조된다." — [나무위키 Claude/모델](https://namu.wiki/w/Claude/%EB%AA%A8%EB%8D%B8)
- GPT-5(2025-08): "글쓰기, 특히 소설 부분에선 오히려 4o이나 4.5보다 더 심각하게 퇴화됐다는 비판이 많다." / "문장 조합실력은 GPT-3급으로 처참해졌고" — [나무위키 GPT-5](https://namu.wiki/w/GPT-5)
- GPT-5.2(2025-12): "'영어 번역투'가 섞인 한국어를 사용한다." / "작문 성능은 GPT-5 시리즈 중에서도 상당히 안 좋다는 평가가 많다." — 같은 문서
- GPT-5.4(2026-03): "글짓기 성능이 향상됐다는 체감평이 많다." 다만 Gemini·Claude에는 못 미친다는 서술. 서브컬처·소설 사용자 불만(짧아진 이어쓰기, 포맷 무시, 약한 캐릭터성)이 가장 컸다는 서술 — 같은 문서
- GPT-5.5(2026-04-24 KST): "GPT-5 시리즈 중에서 가장 유창한 한국어를 구사한다." / "한국어로는 물리적인 의미로만 통용되는 비유를 아주 높은 확률로 사용한다." / "응답 퀄리티, 언어 표현 능력과 이해력이 매우 좋아졌고" — 같은 문서
- GPT-5.6(2026-07-10 KST): "GPT 5.6에서 한국어가 크게 개선되어" / 영어식 은유 잔존: "예를 들어 'X를 가르면/나누면' 같은 식의 표현은 아직도 사용한다." / 거절: "방어적 설명, 중립병에 의한 억까가 아주 심하다." / "사실판단의 질문도 모르쇠로 일관한다." — 같은 문서. 5.6의 소설/글쓰기 전용 서술은 없음.
- GPT-6 Astra(2026-09-04 KST): "한국어 이해 능력이나 지시 준수 능력이 GPT-5 시리즈에 비해 높아졌다." 소설·번역체 서술 없음. — [나무위키 GPT-6](https://namu.wiki/w/GPT-6)
- GPT-6 Sol(2026-09-23 KST): "작업을 계획하고 진행할 때에는 신중하고 효율적인 데에 반해 결과물을 검토할 때의 꼼꼼함이 줄어들어 후속 작업을 필요로 하는 경우가 늘었다." — 같은 문서
- Claude Opus 4.7(2026-04-16): "한국어 유창성이 좀 회복된 성능을 보이기도 했다." 그러나 "마치 의료 차트마냥 대화에서 영어로 된 전문 용어를 막 섞어 써서 가독성이 매우 나쁘다." / "이 훈련이 오히려 GPT-5.2 같은 계산기화된 말투를 낳는 문제가 되었다." — [나무위키 Claude/모델](https://namu.wiki/w/Claude/%EB%AA%A8%EB%8D%B8)
- Claude Opus 4.8(2026-05-29): "말도 안 되는 한국어를 구사하는 일은 거의 사라졌으나, 대신 GPT 5 계열 모델의 번역체나 중립화를 위한 사용자 억지 비판을 할 확률이 Opus 4.6보다는 매우 높다." / 번역체: "4.7부터는 스타일로도 교정이 안 될 정도로 심각해졌다." — 같은 문서
- Claude Opus 5(2026-07-25): "GPT 5.4틱하게 번역체가 더 심해졌으며" / "말투는 이전 모델들과 달리 딱딱한 쪽으로 세팅된 편." — 같은 문서
- Claude Fable 5(2026-06-10): "그러나 한국어 이해도가 아주 높음에 반해서, 의외로 번역체는 꽤나 심하다." — 같은 문서
- Claude Fable 5.1(2026-09-01): "사용자의 번역체 회피 지시에 비교적 잘 따르는 편이라는 정도의 차이점이 있다." / "실질적으로는 Fable 5에 비해 검열이 줄어든 점이 체감되는 모델이다." — 같은 문서
- Claude Opus 5.5(2026-09-23 KST): "한국어 지시 이해도는 GPT-6 Astra를 넘는다는 평이다." / "해요체 사용이 타사 AI보다 많은 편이다." / "작문 성능 측면에서 간만에 개선을 이루었다고 평가받는다." / "대신 사족, 묻지도 않은 반박 끼워넣기가 다소 불편한 정도로 나올 수는 있다." — 같은 문서
- Claude Sonnet 5.5(2026-09-29): "한국어의 유창성으로 따지면 그나마 요근래 가장 유창한 모델 중 하나이지만" / 각주: Opus·Fable 계열보다 Sonnet의 한국어 구사력이 더 안정적 / 모호 주제에 "단정할 수 없습니다"류 답변이 잦아 "대화용으로는 쓰기 어렵다" — 같은 문서

**(일화) 디시인사이드 특이점이 온다 갤러리 / AI 활용 갤러리**
- [2026-04-24, 하늘바라기, "gpt 5.5 글쓰기(소설) 후기"](https://gall.dcinside.com/mgallery/board/view/?id=thesingularity&no=1136781) (조회 2,360 · 추천 3 · 댓글 0): GPT-5.5는 "Gemini 3.1, Claude 4.6 Sonnet, GPT 5.4를 약 1:1:3 비율로 섞은 느낌"; 문체는 GPT-4.5나 Claude Opus만큼 유려하지 않지만 "gpt 5~5.4에 비하면 진짜 일취월장했음"; "정작 스토리 짜는 능력이랑 분량/페이스 조절 능력은 AI답게 형편없음" — 이 부분은 Claude Opus가 가장 잘한다고 평가; 한국적 내용·표현 다양성은 개선(한국어 학습 개선 추정); 예시·설정을 주면 개선되고 옛 소설을 넣어 이어쓰게 하면 문체를 어느 정도 흉내 냄. 생각 모드를 켜도 실제 추론 없이 바로 출력하는 문제로 헤비 모드 사용.
- [2026-09-23, hehee9, "GPT-6 / Opus 5.5 실사용 후기 모음(요약)"](https://gall.dcinside.com/mgallery/board/view/?id=thesingularity&no=1436382) (조회 8,020 · 추천 22): GPT-6 Sol "말투가 개선됨", "이상한 용어 / 전문용어 사용 감소", "환각이 상당히 줄었음", "더 읽기 좋아졌으나, 중요 사항/디테일 누락도 간혹 늘어남 (프롬프트로 잡히려나?)"; Opus 5.5 "글이 읽기 편하고 말투가 더 부드러워짐. Opus 5의 혼내는 듯한 말투 감소", "산문 주석 문제가 개선됨", "종료 조건 등 제약을 안 걸면 모델이 알아서 일을 너무 많이 하는 경향이 있음", "max 추론은 웬만하면 피하기". 소설·검열 전용 서술은 없음.
- [AI 활용 갤러리 "GPT Sol 6.1하고 Opus 5.5 체감"](https://gall.dcinside.com/mgallery/board/view/?id=ai_utilize&no=100947): 검색 스니펫상 "Sol 6.1은 짧고 명확한 작업에, Opus 5.5는 애매하고 긴 프로젝트에 강하다"는 구분 — 원문 fetch는 404로 실패해 **스니펫 기반, 미검증**.
- [특이점 갤 "GPT 소설 프롬"](https://gall.dcinside.com/mgallery/board/view/?id=thesingularity&no=1148723): 인사말 없이 본문만 출력, 캐릭터가 감정을 대사로 설명하지 않게 하는 지시를 담은 소설 프롬프트 공유(스니펫).

**(일화) 클리앙 — [2026-01-11, 박패기, "요즘 AI로 소설 쓰는 이야기. AI 3개 모델 비교"](https://www.clien.net/service/board/park/19124206)** (이전 세대: 챗GPT 5.2 / Claude Sonnet 4.5 / Gemini 3)
- ChatGPT 5.2: "영한 번역투가 심하고 본인이 스스로 정의한 생소한 단어를 남발하여 기계적인 느낌이 강하게 듭니다." / "실제 집필을 맡기면 아쉬움이 큽니다." / "특정 성별의 심리 묘사를 강화해달라는 요청을 거절하기도 합니다."(작성자는 정책보다 표현력 부족으로 해석)
- Gemini 3: "세 모델 중 소설 문장 자체는 가장 잘 씁니다." 그러나 "전체 맥락이나 고증을 체크하는 부분이 부족해, 세부 내용을 정해주지 않으면 창의적으로(?) 서사를 망가뜨리곤 합니다."
- Claude Sonnet 4.5: 분량·아웃라인 설계와 브레인스토밍에 최강. Opus는 주간 사용량 제한이 빡빡해 회피.
- 댓글 fiat: "소설의 전개만보면 클로드 오푸스가 가장 나았습니다." / "GPT는 너무 딱딱하게 내놓고."
- 작성자 워크플로: ChatGPT(구조·리서치) → Sonnet(시놉시스) → Gemini(최종 집필). 원글은 디시 글을 Gemini로 다듬어 옮긴 것이라는 댓글 지적.

**(소표본 실험) AI실험실 블로그 — [2026-04-25 "AI 웹소설·스토리 쓰기"](https://www.aivelolab.com/2026/04/ai-webnovel-story-writing-guide.html)** (이전 세대: ChatGPT GPT-4o / Claude Sonnet 4.6, 테스트 2026-03~04)
- 표본: 세계관·프롬프트 비교 동일 프롬프트 모델당 5회; 집필 비교 로맨스 5회차 + 헌터물 5회차(총 10회차) 3가지 방식; 조건 유무 비교 각 3회 반복.
- 결과(표): 회차 초안 — ChatGPT "사건 전개 명확", Claude "감정선·문체 자연스러움"; 대화문 — ChatGPT "정보 전달형 대화 자연스러움", Claude "감정·뉘앙스 대화 우수"; 장르 문체 유지 — ChatGPT "반복 프롬프트 시 이탈 발생", Claude "긴 세션 문체 유지 상대적 우수". "ChatGPT(GPT-4o)는 세계관·플롯 구조·캐릭터 시트처럼 설계 단계의 구조화 작업에서 일관성이 높고, 회차 초안 집필·감정선 묘사·대화문 생성에는 Claude Sonnet 4.6을 우선 사용합니다."
- 한계: 회차 누적 시 앞 설정 일관성 유지 실패는 AI 전반의 한계로 서술. 어미/번역투·검열 항목 없음.

**(기사) 테크42 — [2026-02-09 "클로드 로맨스 소설 집필 도구로 부상…감정 표현 챗GPT보다 우수"](https://www.tech42.co.kr/%ED%81%B4%EB%A1%9C%EB%93%9C-%EB%A1%9C%EB%A7%A8%EC%8A%A4-%EC%86%8C%EC%84%A4-%EC%A7%91%ED%95%84-%EB%8F%84%EA%B5%AC%EB%A1%9C-%EB%B6%80%EC%83%81-%EA%B0%90%EC%A0%95-%ED%91%9C%ED%98%84-%EC%B1%97gpt/)** — NYT 보도 재인용(영어권 로맨스 작가 대상, 모델 버전 미명시): "특히 감정 표현과 캐릭터 개발 측면에서 챗GPT보다 우수하다고 평가하고 있다" / "더 자연스러운 대화체를 구사하고 섬세한 감정 묘사를 제공한다고 밝혔다". 한국어 전용 근거 아님.

**(일화·국내 개발자) litmers 2026-10-07 종합 기사** — [litmers](https://litmers.com/blog/claude-opus-5-5-%EC%B6%9C%EC%8B%9C-%EC%B4%9D%EC%A0%95%EB%A6%AC-%EA%B0%80%EA%B2%A9-%EB%B2%A4%EC%B9%98%EB%A7%88%ED%81%AC-%EC%8B%A4%EC%A0%9C-%ED%9B%84%EA%B8%B0): 국내 개발자 블로그(10-06) "Opus 5.5가 Opus 5.0에 비해 간만에 장점만 존재하는 버전업이라는 생각이 들 정도로 쾌적합니다."; "대화 상대로서의 맛은 구버전이 낫다는 평가가 있고"; Daniel Nest(Why Try AI) 대화형 과제 9개(톤 맞추기·반론·짧은 소설 포함) 점수 Opus 4.6 6점 / Opus 5.5 4점 / Opus 5 0점(n=9 과제, 평가자 1인).

### Inferences
- 한국 커뮤니티 평가의 축은 "문장 유려함(Claude/Gemini 우세) vs 구조·설계(GPT 우세) vs 전개·페이스(Claude Opus 우세)"로 2026-01(5.2/4.5 세대)부터 2026-09(GPT-6/Opus 5.5 세대)까지 일관된다.
- 번역체 문제는 2026년 들어 GPT→Claude로 역전되는 흐름(GPT 5.5/5.6 개선, Claude 4.7~5 악화)이 나무위키에 기록되며, Opus 5.5·Fable 5.1에서 부분 회복됐다는 체감이 있다. 단 전부 체감 보고다.
- 문피아·조아라·네이버카페 등 "현업 웹소설 작가"의 공개 비교 발언은 거의 유통되지 않는다(AI 사용 공개 자체에 대한 위험 때문으로 추정; 테크42 기사도 "윤리적 우려와 창작의 진정성 문제" 언급).

### Gaps
- 문피아·조아라 작가 커뮤니티, 네이버 카페, 유튜브 리뷰에서 GPT-5.6/GPT-6 vs Opus 5.5/Fable 5.1 **직접 비교** 글은 찾지 못했다.
- 어미·조사 오류, 존댓말 일관성에 대한 **정량 비교** 는 한국어 자료에 없다(해요체 과다라는 Opus 5.5 체감만 존재).
- arca.live 소설 감평 비교 글(https://arca.live/b/characterai/164025382)은 403으로 열지 못함(스니펫: Claude "훌륭한 분석력", 답변 짧아 세부 누락).

---

## 2. 이 모델들을 포함한 한국어 리더보드·벤치마크 (점수·날짜)

### Takeaway
2026-11-01 기준 **GPT-5.6/GPT-6/Opus 5.5/Fable 5.1 점수를 공개한 한국어 전용 리더보드는 확인되지 않았다.** 호랑이(Horangi) 리더보드 4는 2025-12-01 최종 갱신(오픈 모델 중심, 창작 카테고리 없음), KMMLU-Pro 공개 점수 없음, LMArena 한국어 카테고리 점수는 집계 사이트에 노출되지 않음. 한국어 창작 품질을 평가한 2026년 논문도 없고 탐지(detection) 연구만 있다.

### Cited Findings
- **Horangi(W&B 한국어 LLM 리더보드) 4**: "Last updated: December 1, 2025." 평가 축 GLP(기초 언어·응용 언어·지식QA·추론·앱 개발) + ALT(제어·윤리·유해 방지·편향 방지·환각 방지). 창작/생성 카테고리 없음. 모델 테이블은 인터랙티브라 텍스트로 추출 불가 — [W&B 리포트](https://wandb.ai/justintenuto/kn-jp-translations/reports/Horangi-W-B-Korean-LLM-Leaderboard-4--VmlldzoxNTIzNDgxOQ) (forge.coreweave.com으로 리다이렉트). 검색 스니펫상 수록 모델은 GPT OSS 20B/120B, Qwen3, Llama 4, Kimi K2, DeepSeek V3.1, GLM 4.5 등 — Anthropic/GPT-5.x 항목 미확인.
- Horangi v3(wandb-korea/llm-leaderboard3, 모델 77개, 실행 2024-10~2025-10): 벤치마크별 1위에 claude-3-7-sonnet(Ko-TruthfulQA), gpt-4.5-preview(KLUE-NER) — [lablup/llm-benchmark-inventory PR #17](https://github.com/lablup/llm-benchmark-inventory/pull/17). 구세대.
- **KMMLU-Pro**: Opus 5 / GPT-5.5 / Opus 5.5 점수 검색 결과 없음. 영어 MMLU-Pro(Vals): Fable 5.1 92.38% 1위, Opus 5 91.59% (2026-09-01 기준) — [Vals MMLU Pro](https://www.vals.ai/benchmarks/mmlu_pro); GPT-5.5 88.1% — [BenchLM 비교](https://benchlm.ai/compare/claude-opus-5-vs-gpt-5-5) (집계 사이트, 2차).
- **LMArena**: 언어별 리더보드(한국어 포함) 운영, "Korean exhibits weaker correlations with the other languages" — [Arena 카테고리 안내](https://news.lmarena.ai/arena-category/). 한국어 카테고리의 Opus 5.5/GPT-5.6 점수는 어느 집계 사이트에도 없음. 전체 텍스트 보드: Opus 5.5 1,504점 4위(2026-10-02, 1위 Gemini 4 Argon 1,525, 오차 ±9) — [litmers 재인용](https://litmers.com/blog/claude-opus-5-5-%EC%B6%9C%EC%8B%9C-%EC%B4%9D%EC%A0%95%EB%A6%AC-%EA%B0%80%EA%B2%A9-%EB%B2%A4%EC%B9%98%EB%A7%88%ED%81%AC-%EC%8B%A4%EC%A0%9C-%ED%9B%84%EA%B8%B0); GPT-5.6 패밀리는 2026-07-31 Arena 등재 — [swfte 집계](https://www.swfte.com/lmarena) (2차, 수치 불일치 다수).
- **LMArena Creative Writing(영어 중심, 인간 투표)**: 2026-09-29 BenchLeader 기준 Opus 5.5 1521, Fable 5 1501 — [BenchLeader](https://www.benchleader.com/benchmarks/lmarena_text_creative); 2026-07-20 기준 claude-fable-5 1512.8 1위 — [Intellectual Lead](https://intellectualead.com/best-llm-writing/); writewithpaige(2026-10-23)는 Gemini 4 Argon 1위로 기재 — [writewithpaige](https://writewithpaige.com/blog/best-ai-model-for-writing-fiction-2026). **집계 사이트 간 불일치**.
- **Lech Mazur 단편 벤치마크(영어, LLM 심사, 요소 10개/600–800단어)**: Opus 5.5 3.767 vs Fable 5.1 3.796 — [NovelMage 2026-10-05](https://novelmage.com/blog/claude-opus-55-for-creative-writing-draft-with-taste) 재인용; 원 저장소 [lechmazur/writing](https://github.com/lechmazur/writing).
- **Graphite "AI Tells: Opus 5.5 Update" (2026-10-01, 영어 기사 생성 n=9,974 토픽, mannered-prose는 1,000 토픽 서브샘플, Opus 5로 0–100 채점)**: Opus 5.5 tell 2,548(Opus 5 2,666, Opus 4 3,746); 유니그램 발산 Opus 5.5 0.052 / Opus 5 0.064 / GPT-5.6 Sol 0.101 / GPT-6 Astra 0.109; mannered-prose Opus 5.5 10.57 / Opus 5 16.75 / 인간 6.65 / Astra ≈1.2×인간; 엠대시 Opus 5.5 0.015/1000단어 vs Opus 5 2.92. "Opus 5.5 still has many tells. AI tells change between models and versions, but do not go away." — [Graphite](https://graphite.io/five-percent/research/ai-tells-opus-5-5-update). **영어 측정** — 한국어 전이 미검증.
- 한국어 창작 관련 2026 논문: 한국어 시 LLM 생성 탐지(형식 특징) — [arXiv 2608.28986](https://arxiv.org/pdf/2608.28986); KoLing 한국어 LLM 텍스트 탐지 벤치마크(창작 글짓기 하위 유형 포함, 품질 평가 아님) — [arXiv 2610.22940](https://arxiv.org/html/2610.22940); 한국어 학술 초록의 LLM 어휘 전이(2018–2026) — [arXiv 2609.07447](https://arxiv.org/pdf/2609.07447). KorNAT은 2024 논문으로 신모델 미포함 — [arXiv 2402.13605](https://arxiv.org/pdf/2402.13605).

### Inferences
- 한국어 산문 품질에 대한 **측정 데이터는 사실상 부재** 하므로, 보고서는 "한국어 품질 = 커뮤니티 체감 + 영어 측정의 간접 추정"임을 명시해야 한다.
- Graphite 수치는 "Opus 5.5가 Opus 5보다 AI 티가 줄었으나 GPT-6 Astra가 인간 어휘 분포에 더 가깝다"는 영어 결과로, 나무위키의 "GPT 5.6 한국어 크게 개선" 체감과 방향이 일치하지만 인과 연결은 추정이다.

### Gaps
- Horangi 4의 실제 모델/점수 표(인터랙티브) 미추출; Anthropic/GPT-5.x 신모델 포함 여부 불명.
- KMMLU/KoBEST/KMMLU-Pro에 Opus 5.5·GPT-6 공식 점수 없음(Anthropic·OpenAI 시스템카드 미확인).
- LMArena 한국어 카테고리 현황은 arena.ai/leaderboard 직접 조회가 필요(이번 조사에서 미조회).

---

## 3. 엄격한 스타일 제약(부사 금지·보여주기·고정 시점/시제) 준수와 장편 일관성

### Takeaway
스타일 제약 준수와 장편 일관성에 대한 **한국어 측정 자료는 없다.** 영어권 리뷰·소표본 테스트에 따르면 Opus 5.5는 Opus 5의 "길어질수록 스타일 가이드 무시"와 장황함을 상당히 고쳤으나 장면 끝 과잉 설명(telling)과 "핵심을 뒤에 묻는" 습관이 남고, Fable 5.1은 스타일 지시 준수와 Claude 상투어 감소에서 가장 좋은 평을 받는다. GPT-6 Astra는 구조·아이디어에 강하고 문장 리듬이 균일하다는 평. 디시 후기는 Opus 5.5가 제약을 안 걸면 과잉 작업하고, GPT-6 Sol은 디테일 누락이 늘었다고 보고한다.

### Cited Findings
- (일화·종합) Opus 5 "ignored style guides as a piece got longer"(StashBase 라운드업 인용); Opus 5.5 산문은 "plainer", "more obedient"; 그러나 "still over-explains the end of scenes", "buries the point", "drafts better than it edits"; Opus 5 평균 응답 510단어 vs Opus 4.5 158단어(Arena 8월 분석 재인용); Box 보고 Opus 5.5 토큰 ≈ Opus 5의 1/3; 장편 일관성은 미테스트, 1M 컨텍스트에도 "story bible을 매 요청에 포함" 권고 — [NovelMage 2026-10-05](https://novelmage.com/blog/claude-opus-55-for-creative-writing-draft-with-taste) (제품 판매 블로그; 자체 테스트는 프롬프트 1개·테스터 1인·Sonnet 5.5 대비 1회).
- (소표본 측정) 소설 문장 조이기 테스트: Opus 5.5·GPT-5.6 Sol 모두 "She noticed that", "felt that she", "really" 제거, Opus는 "very"도 제거; 단어 보존율 Opus 5.5 93% / GPT-5.6 Sol 94% — 결과 "close to identical" — [StashBase Opus 5.5 writing](https://stashbase.ai/blog/claude-opus-5-5-writing/) (검색 스니펫 기반; 표본 미상). 같은 글: "nobody has published a fiction review of 5.5 yet"(10월 초 기준).
- (라운드업) writewithpaige 2026-10-23: Novelmint 블라인드 패널에서 Opus 5.5가 Opus 5에 11개 스토리 비트 중 8개 승, 로맨스 최고점; EQ-Bench 단편(AI 심사) Astra 1위·Fable 5.1 2위; Intellectual Lead 스타일 벤치에서 Astra 약 29위, 문장 길이 "unusually uniform"; Fable 톤 테스트에서 Astra 차가운 리라이트 "reads like a report"; 결론 "Opus 5.5: the default choice for prose work", "Fable 5.1: fewer AI tells", "Astra: Strong at ideas and structure. Weaker at making a paragraph sing.", "There is no single best model." 자체 모델 비교는 안 함("didn't run our own model shoot-out"); 부사/시점/시제/장편 일관성 테스트 없음 — [writewithpaige](https://writewithpaige.com/blog/best-ai-model-for-writing-fiction-2026).
- (일화) Fable 5.1: HN 댓글 "It sounds a lot less stereotypically like other Claude models, has (imho) a much more natural style, and responds to my style instructions more reliably."; Zvi: "Writing is greatly improved. The Claudisms seem to have improved, although some are very much still there."; 일부 사용자 "its prose is denser than Claude Fable 5's: sentences run longer and there are fewer paragraph breaks", "more token hungry by 25-50%" — [HN](https://news.ycombinator.com/item?id=49525378), [Zvi](https://thezvi.substack.com/p/claude-mythos-51-and-fable-51-capabilities).
- (일화·이전 세대) NovelCrafter: Opus 5에서 문장 품질 저하·긴 출력일수록 흐트러짐 → 작가는 Opus 4.6 유지 — [Novelcrafter](https://www.novelcrafter.com/blog/opus-5-for-writers) (Opus 5.5 이전 글).
- (일화·한국) Opus 5.5 "종료 조건 등 제약을 안 걸면 모델이 알아서 일을 너무 많이 하는 경향이 있음"; GPT-6 Sol "중요 사항/디테일 누락도 간혹 늘어남" — [디시 특이점갤 2026-09-23](https://gall.dcinside.com/mgallery/board/view/?id=thesingularity&no=1436382).
- (일화·한국) Opus 5.5 "사족, 묻지도 않은 반박 끼워넣기", GPT-5.5 "특정 표현을 반복하는 경향", Fable 5.1 "번역체 회피 지시에 비교적 잘 따르는 편" — [나무위키 Claude/모델](https://namu.wiki/w/Claude/%EB%AA%A8%EB%8D%B8), [나무위키 GPT-5](https://namu.wiki/w/GPT-5).
- (측정·영어) Graphite: Opus 5.5의 과장체 10.57 vs 인간 6.65(≈1.6×), Astra ≈1.2×인간; 특정 패턴 명시 금지가 범용 "AI 티 피하라"보다 효과적이라는 가이드 — [Graphite](https://graphite.io/five-percent/research/ai-tells-opus-5-5-update), [remio 요약](https://www.remio.ai/post/claude-opus-5-5-writing-tells-changed-but-they-did-not-disappear).
- (일화·한국, 이전 세대) Claude Sonnet 4.6 "긴 세션 문체 유지 상대적 우수", GPT-4o "반복 프롬프트 시 이탈 발생" — [AI실험실 2026-04-25](https://www.aivelolab.com/2026/04/ai-webnovel-story-writing-guide.html).

### Inferences
- "부사 금지/보여주기"류 네거티브 제약은 두 진영 모두 **구체 패턴을 명시**해야 효과가 있고(Graphite), Claude는 장면 말미 설명(telling) 재발, GPT는 균일한 문장 길이·보고서체 경향이 각각 약점으로 보인다.
- 장편 일관성은 어느 진영도 모델 단독으로 보장하지 못해 파이프라인(스토리 바이블·파일 기반 연속성 추적)이 대안이라는 데 영어·한국 실무자 모두 수렴한다.

### Gaps
- 고정 시점/시제 유지, 어미 통일(예: '-다' 종결 고정), 존댓말 일관성에 대한 측정은 어느 언어에서도 찾지 못했다.
- Opus 5.5 vs GPT-6 Astra/6.1 Sol 직접 소설 대결(blind)은 Novelmint 패널(Opus 5.5 vs Opus 5)만 있고 OpenAI 모델과의 블라인드 비교는 없다.

---

## 4. 소설 관련 거절·가드레일 차이 (폭력·로맨스·범죄)

### Takeaway
소설용 폭력·로맨스·범죄 장면의 거절률을 비교한 측정은 없다. 한국 체감으로는 (a) GPT-5.2까지 "과도한 검열·훈계"가 최악, GPT-5.5에서 훈계조 소멸, GPT-5.6에서 "중립병 억까·모르쇠", GPT-6 Astra는 시스템카드상 "무해한 요청 거절 가능성 감소"지만 사이버 안전장치로 오탐 증가; (b) Claude는 Opus 5(2026-08) 분류기 검열 과강화 → Opus 5.5 출시 수일 후 완화, **Claude Code에서는 검열 거의 없음 vs 웹 앱은 검열 심함**이라는 채널 차가 보고되며, Fable 5는 생물학 키워드만 나와도 모델 강제 전환, Fable 5.1은 검열 감소 체감.

### Cited Findings
- GPT-5(2025-08): "민감성 판단이 과도하게 이루어져 다른 모델을 사용하는 도중에도 GPT-5 모델로 강제 라우팅되어" — 안전 라우팅은 2026-02-13 Plus에서 사실상 제거 — [나무위키 GPT-5](https://namu.wiki/w/GPT-5)
- GPT-5.2(2025-12): "과도한 검열, 잦은 훈계와 진정성 없는 대처"; 2026-02 기준 경쟁사 대비 가장 강한 검열 — 같은 문서
- GPT-5.5(2026-04): "불쾌한 훈계조가 사라지고"; 결론을 중간으로 되돌리는 경향 잔존 — 같은 문서
- GPT-5.6(2026-07): "방어적 설명, 중립병에 의한 억까가 아주 심하다." / "사실판단의 질문도 모르쇠로 일관한다." — 같은 문서
- GPT-6 Astra(2026-09): 시스템카드 "무해한 요청을 거절하거나 과도하거나 불필요하게 비판적인 조건을 덧붙일 가능성이 적다."; "다만" 같은 완충 표현 잦음; "과도한 검열을 방지하기 위해 바로 작업을 완전히 중지하기보다는" 응답 검토 강화 선택; 사이버 안전장치로 일반 작업 오탐 증가, "API로 사용 시 완전히 작업이 중단된다." — [나무위키 GPT-6](https://namu.wiki/w/GPT-6); Astra는 OpenAI 내부 사이버 "Critical" 임계치 최초 도달 — [CNBC 2026-09-03](https://www.cnbc.com/2026/09/03/open-ai-astra-gpt-6-cyber.html)
- Claude Opus 5(2026-07): "2026년 8월에 들어서는 분류기의 검열이 지나칠 정도로 강화되어" / "무조건적으로 작업을 거부하는 등" — [나무위키 Claude/모델](https://namu.wiki/w/Claude/%EB%AA%A8%EB%8D%B8)
- Claude Opus 5.5(2026-09): 출시 초 엄격 → 며칠 뒤 조정, Claude Code에서는 "검열이 거의 걸리지 않는다", 공식 홈페이지는 "검열이 상당히 심하다" — 같은 문서. HN 사용자: 본인 웹앱 인증 모듈 점검 거절, "자기가 직접 짠 코드라고 설명해도 통하지 않아" Opus 4.8로 전환; "기존 사이버 보안 분류기에 생물학 분류기가 더해져" — [litmers 2026-10-07](https://litmers.com/blog/claude-opus-5-5-%EC%B6%9C%EC%8B%9C-%EC%B4%9D%EC%A0%95%EB%A6%AC-%EA%B0%80%EA%B2%A9-%EB%B2%A4%EC%B9%98%EB%A7%88%ED%81%AC-%EC%8B%A4%EC%A0%9C-%ED%9B%84%EA%B8%B0)
- Claude Fable 5(2026-06): "아예 생물학 관련 키워드가 눈꼽만큼이라도 등장하면 그 즉시 Opus 4.8로 모델을 바꿔버린다"; 재개 후 "사이버 요청, 디버깅, 생명공학과 관련된 모든 질문은 예외 없이" 중단/전환 — [나무위키 Claude/모델](https://namu.wiki/w/Claude/%EB%AA%A8%EB%8D%B8)
- Claude Fable 5.1(2026-09): "실질적으로는 Fable 5에 비해 검열이 줄어든 점이 체감되는 모델이다." — 같은 문서
- Claude Opus 4.8: "심리 상담 용도로는 정말로 자신에게 피해를 입힌 가해자도 옹호하게 되어 꽤 위험한 편이다."(중립화 편향) — 같은 문서
- (에세이·일화) 브런치 2026-04-23: "GPT 스타일의 명시적인 거절은 적어도 검열임이 바로 드러난다." / "사용자는 거절당하는 대신에 대화가 계속되는 척하며 이루어지는 통제를 겪게 된다."(Claude의 우회 통제 비판; 소설 맥락 아님) — [브런치 @liminality](https://brunch.co.kr/@liminality/94)
- (일화·이전 세대) ChatGPT 5.2 "특정 성별의 심리 묘사를 강화해달라는 요청을 거절하기도 합니다." — [클리앙 2026-01-11](https://www.clien.net/service/board/park/19124206)
- 루리웹 안전 평가 글은 탈옥 저항성 테스트("클로드 오푸스와 gpt가 낮고 제미니와 그록이 높은 점수")로 소설 검열과 무관 — [루리웹](https://m.ruliweb.com/community/board/300143/read/73869727) (스니펫).

### Inferences
- 2026년 하반기 거절 문제의 중심은 **창작 주제(폭력·로맨스) 자체보다 사이버/생물 분류기 오탐과 "중립화" 태도**다. 소설 파이프라인에서 Claude를 쓸 때 Claude Code(API/에이전트 경로)가 웹 앱보다 거절이 적다는 체감은 도구 선택의 실질적 근거가 된다.
- GPT 측은 명시적 거절·훈계가 줄었지만 "다만"·중립 회피가 서사 톤을 흐릴 수 있고, Claude 측은 거절 대신 톤 완화/우회로 지시를 희석할 수 있다(브런치 비판) — 둘 다 소설에서는 "지시 희석" 형태로 나타날 가능성.

### Gaps
- 폭력·범죄·성애 장면별 거절률 비교 측정(한국어·영어 모두) 없음.
- 한국 서브컬처·성인 웹소설 작가 집단의 2026-09 이후 Opus 5.5/GPT-6 검열 체감 글(디시 AI 창작갤 등)은 검색에 노출되지 않았다.

---

## 5. AI 소설 파이프라인의 기본 모델 선택과 이유

### Takeaway
공개 파이프라인들은 **모델을 고정하지 않고 "호스트 에이전트의 모델을 그대로 쓴다"** 는 설계가 지배적이다(oh-story-claudecode, rocodrama/novel, awesome-novel-studio). oh-story 메인테이너는 문서 정제에 Codex(gpt-5.6-sol)를, PR 생성/코어 작업에 Claude Code(Opus 5.5)를 함께 썼지만 **선택 이유를 명시하지 않았다**. 한국 파이프라인(rocodrama/novel)은 Claude Code 집필 + Codex 교차 검수라는 역할 분담을 택했고, 이는 커뮤니티의 "Claude 집필·GPT 검토/구조" 통념과 일치하나 역시 이유는 미기재다. 노벨AI·카카오·문피아의 기반 모델 공개 정보는 없다.

### Cited Findings
- **zenstory-ai/oh-story-claudecode** (중국 웹소설용, Claude Code · Codex CLI · Antigravity · OpenCode · ZCode · OpenClaw · Reasonix 7개 호스트): "写作用的模型就是该 Agent 的模型，不需要 GPU，也不需要另外配模型。"(집필 모델 = 호스트 에이전트의 모델); "Codex 会直接扫描仓库内 `.agents/skills` 发现 14 个 skill，用 `$story-setup` 调用"; "OpenCode 需要 2.x，1.x 加载不了写正文守卫插件"; 去AI味 목표 "优化目标是读感；朱雀等外部检测只作自测参考。"; 표지 생성은 "它调用 GPT-Image-2（Codex 内置用量或 API 回退）。" 모델 간 품질 벤치 없음, 한국어 언급 없음 — [GitHub README](https://github.com/zenstory-ai/oh-story-claudecode)
- oh-story PR #494 (2026-10-18, 커밋 2026-10-17): "精修由 codex（gpt-5.6-sol）分 6 组执行"; 커밋 트레일러 "Co-Authored-By: Claude Opus 5.5"; "🤖 Generated with Claude Code"; 6명 리뷰어 의미 검토로 의심 71곳 중 27곳 확정·복원; 집필 규칙 파일 변경 시 "会影响正文，要先做对比试写". **모델 선택 이유 미기재, 모델 간 비교 없음** — [PR #494](https://github.com/zenstory-ai/oh-story-claudecode/pull/494). (과제 지시문의 "bench가 gpt-5.6-sol 사용" 표현은 이 PR의 문서 정제 작업을 가리키는 것으로 보이며, 별도 벤치 파일은 README에서 확인되지 않음.)
- gpt-5.6-sol을 Claude Code에서 구동하는 3rd-party 브리지 claudecodex는 이를 "OpenAI's strongest coding model", 컨텍스트 372K로 기재(OpenAI 공식 미확인) — [karem505/claudecodex](https://github.com/karem505/claudecodex)
- **rocodrama/novel** (한국 웹소설용 Claude Code 스킬 모음): "웹소설 작업에 공통으로 쓰는 Claude Code 스킬 모음입니다."; `episode-finish`: "분량(5,000자 이상)·AI 티 점검(스크립트 + humanize-scan), Codex 교차 검수"; `character-design`: "Codex 병렬 생성"; 요구사항 "Codex CLI(ChatGPT 로그인)"; 선택 의존성 "humanize-korean 플러그인(선택)". Codex 모델명·선택 이유 미기재 — [GitHub](https://github.com/rocodrama/novel)
- **MJbae/awesome-novel-studio** (한국 플랫폼 기준 Claude Code 플러그인, 에이전트 18·스킬 10): 폴리시 축 TRANS "Translationese, AI tone, semantic literal translation detection", BANNED "Banned expressions (time-skip cliches, meta-commentary)", SILENCE "Silence pattern overuse (max 4 per episode)", VOICE "Character dialogue consistency (checked against voice table)"; 커스텀 축 예 "Domain knowledge should be hinted at through dialogue, never explained". 모델 배정·Codex 사용 미기재 — [GitHub](https://github.com/MJbae/awesome-novel-studio)
- zenstory-ai/novel-to-game: Claude Code·Codex·Kimi Code 동시 지원(각색 도구) — [GitHub](https://github.com/zenstory-ai/novel-to-game)
- 한국 Codex 스킬 큐레이션 — [J-nowcow/awesome-korean-agent-skills](https://github.com/J-nowcow/awesome-korean-agent-skills)
- 영어권 작가 워크플로 통념: 초안은 Claude, 아웃라인/구조는 GPT — [fable.la 블로그](https://www.fable.la/blog/claude-vs-chatgpt-creative-writing), [Entangled Text](https://www.entangledtext.com/best-ai-models-for-writing); Opus 5.5를 "default choice for prose work"로 지칭 — [writewithpaige 2026-10-23](https://writewithpaige.com/blog/best-ai-model-for-writing-fiction-2026)
- 비용: Fable 5.1 토큰 단가 ≈ Opus 5.5의 2.5배; Anthropic은 Fable을 고난도 추론·장기 에이전트용으로 포지셔닝 — [NovelMage 2026-10-05](https://novelmage.com/blog/claude-opus-55-for-creative-writing-draft-with-taste); Opus 5.5는 Opus 5보다 일반 작업 비용 40% 절감(Anthropic 발표) — [Anthropic](https://www.anthropic.com/claude-opus-5-5)
- 한국 상용 도구(노벨AI·카카오·문피아·NovBie·펜시브)의 기반 모델 공개 정보: 검색 결과 없음 — [NovBie](https://novbie.com/), [펜시브 비교글 2026-05](https://pensiv.so/ko/blog/writing-program-comparison)

### Inferences
- 파이프라인 설계자들이 모델을 고정하지 않는 이유는 (1) 호스트 구독(Claude Code/Codex) 과금 활용, (2) 모델 세대 교체 속도(2026년 하반기 3개월간 GPT-5.6→6→6.1 Sol, Opus 5→5.5)로 추정된다 — 출처들이 이유를 밝히지 않아 **추정**.
- oh-story가 코어는 Claude Code(Opus 5.5), 문서 정제는 Codex(gpt-5.6-sol)로 나눈 것은 Codex의 저렴한 포함 사용량과 "편집/검토에는 두 모델 차이가 작다"는 StashBase류 관찰과 부합하나, 메인테이너 발언은 없다.
- 한국 파이프라인이 "번역투/AI 톤 탐지 축"(TRANS, humanize-korean)을 별도 후처리로 둔다는 사실 자체가, 어느 모델도 한국어 번역투를 기본 출력에서 해결하지 못한다는 실무 판단의 증거다.

### Gaps
- oh-story-claudecode 저장소 내 별도 "bench" 디렉터리/문서가 `gpt-5.6-sol`과 Claude를 비교했는지는 README·PR #494에서 확인되지 않음(저장소 내부 파일 미열람).
- rocodrama/novel이 Codex 교차 검수를 택한 이유, 사용 모델(gpt-5.6-sol vs gpt-6.1-sol) 미확인.
- 노벨AI(Anlatan 자체 모델)·카카오·문피아의 AI 집필 도구 모델 공개 정보 없음.

---

## 부록: 자료 신뢰도 등급
- **측정(영어)**: Graphite AI Tells(n≈10k 토픽, 자동 채점), Lech Mazur 단편 벤치(LLM 심사), LMArena creative(인간 투표; 집계 사이트 간 수치 불일치), StashBase 조이기 테스트(표본 미상).
- **소표본 실험(한국어, 이전 세대)**: AI실험실 2026-04(10회차, GPT-4o vs Sonnet 4.6).
- **일화(한국어, 현세대)**: 나무위키(익명 집단 편집), 디시 특이점갤 2026-09-23(추천 22), 디시 2026-04-24(추천 3), litmers 재인용 개발자 블로그.
- **일화(한국어, 이전 세대)**: 클리앙 2026-01-11, 브런치 2026-04-23, 테크42(NYT 재인용) 2026-02-09.
- 열지 못한 원문: 디시 AI활용갤 100947(404), arca.live 164025382(403), orcarouter Opus 5.5 글(본문 미노출).
