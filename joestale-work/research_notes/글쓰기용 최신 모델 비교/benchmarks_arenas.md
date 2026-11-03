# 창작 글쓰기 벤치마크·아레나 비교: GPT-5.6/6 계열(Sol, Astra) vs Claude Opus 5.5 / Claude Fable 5.1

기준일: 2026-11-01. 모든 수치는 해당 소스의 스냅샷 날짜를 함께 표기. 모델명·점수는 소스 표기 그대로.

**모델명에 관한 사전 주의**: 과제에서는 "GPT-5.6 계열의 Astra/Sol"로 지칭했으나, 공개 리더보드와 리뷰에서 실제로 쓰이는 이름은 다음과 같다.
- **GPT-5.6 Sol** — 2026-07-31 Text Arena 등재 ([검색 결과 요약](https://benchlm.ai/llm-leaderboard-history)); Codex 기본 모델이었음 ([WolframRvnwlf, Codex 지시문 비교](https://x.com/WolframRvnwlf/article/2096018047538450580)).
- **GPT-6 Astra** — 2026-09-05 Lech Mazur 벤치마크 추가 기준 ([lechmazur/writing](https://github.com/lechmazur/writing)); 리뷰에서 "5.6-Sol의 큰 업그레이드"로 묘사 ([Dan Shipper](https://x.com/danshipper/status/2095593705214300394)).
- **GPT-6 Sol**, **GPT-6.1 Sol** — Astra 이후 출시된 저가·고속 변형 ([Dan Shipper](https://x.com/danshipper/status/2102461471716483208); [Arena Korean](https://arena.ai/leaderboard/text/korean)).
- 어떤 소스에서도 "GPT-5.6 Astra"라는 표기는 발견되지 않음. 아래에서는 Astra = GPT-6 Astra, Sol = GPT-5.6 Sol(및 후속 GPT-6/6.1 Sol)로 각각 명시한다.
- Claude Fable 5.1 출시: 2026-09-01 ([Claude Platform Docs 한국어](https://platform.claude.com/docs/ko/models/fable-5-1/overview)); Claude Opus 5.5 출시: 2026-09-22 ([myclaw 블로그](https://myclaw.ai/de/blog/opus-5-5-for-creative-writing), 벤더 발표 인용).

---

## KQ1. 각 리더보드에서 네 모델의 창작 글쓰기 순위는? (정확한 수치·날짜)

### Takeaway
LLM 심판 기반 벤치마크(EQ-Bench CW v3, Lech Mazur 단편)에서는 **GPT-6 Astra 또는 Claude Fable 5.1**이 1위이고 Opus 5.5는 중상위(EQ-Bench 7~8위, Mazur 2위)에 머문다. 반대로 **인간 투표 기반 Arena 창작 글쓰기**에서는 Opus 5.5가 1위(1520), Fable 5.1은 8위(1489), GPT-5.6 Sol은 18위(1470), GPT-6 Astra는 40위(1450)로 OpenAI 모델이 크게 뒤진다. 심판 종류(LLM vs 인간)에 따라 순위가 뒤집히는 점이 핵심.

### Cited Findings

**A. Arena (구 LMArena) Text — Creative Writing 카테고리** (페이지 날짜 2026-10-27, 총 1,450,312표, 417모델, Bradley-Terry·스타일 컨트롤)
- 1위 Claude Opus 5.5 (High) 1520 ±13 (2,672표) — [arena.ai/leaderboard/text/creative-writing](https://arena.ai/leaderboard/text/creative-writing)
- 2위 Gemini 4 Argon (High) 1517 ±13; 3위 Gemini 4 Carbon (High) 1515 ±20 (Preliminary); 4위 Claude Fable 5 (High) 1501 ±7 (9,760표) — [arena.ai](https://arena.ai/leaderboard/text/creative-writing)
- 8위 Claude Fable 5.1 (Max) 1489 ±11 (3,884표) — [arena.ai](https://arena.ai/leaderboard/text/creative-writing)
- 15위 Claude Opus 5 (Max) 1474 ±8; 16위 Claude Opus 5 (High) 1472 ±6 — [arena.ai](https://arena.ai/leaderboard/text/creative-writing)
- 18위 GPT-5.6 Sol (xHigh) 1470 ±7 (9,174표) — [arena.ai](https://arena.ai/leaderboard/text/creative-writing)
- 38위 GPT-5.5 (High) 1451 ±7; 40위 GPT-6 Astra (Max) 1450 ±11 (3,323표); 42위 GPT-5.5 1448 ±7 — [arena.ai](https://arena.ai/leaderboard/text/creative-writing)
- 66위 GPT-6 Sol (Max) 1435 ±11 (3,302표) — [arena.ai](https://arena.ai/leaderboard/text/creative-writing); BenchLeader 미러(2026-10-28 결과)는 같은 자리에 "GPT-6.1 Sol (max) 35위 1454"를 두고 "GPT-6 Sol" 항목이 없다고 기록 — [BenchLeader](https://www.benchleader.com/benchmarks/lmarena_text_creative). 두 소스가 다른 변형을 수록한 것으로 보이며, 어느 쪽이 Codex의 현행 Sol인지 확정 불가.
- 이전 세대(참고): Claude Opus 4.6 (High) 5위 1499; Opus 4.7 (High) 7위 1489; Opus 4.8 (High) 21위 1469 — [arena.ai](https://arena.ai/leaderboard/text/creative-writing)
- 2026-10-15 투표 기준 미러: Opus 5.5 1519 #1, Gemini 4 Argon 1516 #2 (통계적 동률), Fable 5.1 1485 #9, GPT-6 Astra 1450 #38, GPT-6 Sol 1438 #61; 10월 8일 집계에서는 1·2위가 반대였음 — [felloai (2026-10-30 갱신)](https://felloai.com/best-ai-for-writing/)
- 다른 미러는 Opus 5.5를 1534(약 290개 구성 중, 2026-10-28)로 표기; 블로그는 1520~1534 범위에 Elo 변동이 있다고 명시 — [myclaw](https://myclaw.ai/de/blog/opus-5-5-for-creative-writing)
- Arena 공식 페이지에는 "last updated" 필드가 없고 "Oct 27, 2026" 날짜만 표시 — [arena.ai](https://arena.ai/leaderboard/text/creative-writing)

**B. EQ-Bench Creative Writing v3** (Sam Paech; LLM 심판 pairwise Elo; 영어만)
- 공식 페이지(eqbench.com/creative_writing.html)는 표가 동적 로딩이라 직접 수치 추출 실패; 아래 수치는 미러 사이트 기준 — [eqbench.com](https://eqbench.com/creative_writing.html)
- 스냅샷 2026-10-12 (vibecodingnav): 1위 GPT-6 Astra 2173.3; 2위 Claude Fable 5.1 2162.0; 3위 Claude Opus 5 2132.6; 4위 GPT-6 Sol 2124.7; 5위 Kimi K3 2082.3; 6위 GLM-5.3 2075.0; **7위 Claude Opus 5.5 2050.1**; 8위 Grok 4.7 2006.7; 10위 GPT-5.6 Sol 1971.6; 11위 Claude Fable 5 1943.1; 14위 Claude Opus 4.7 1914.3; 17위 GPT-5.6 Terra 1854.9; 18위 GPT-5.5 1843.9 — [vibecodingnav](https://www.vibecodingnav.com/benchmarks/eqbench-creative-writing/)
- "마지막 결과 추가 2026-10-25" 스냅샷 (llmlearner): GPT-6 Astra 2174; Fable 5.1 2163; Opus 5 2134; GPT-6 Sol 2125; Kimi K3 2084; GLM-5.3 2077; Opus 5.5 2051; Grok 4.7 2012; Muse Wonder 2007; GPT-5.6 Sol 1974; Fable 5 1944; Opus 4.7 1915; GPT-5.6 Terra 1856; GPT-5.5 1845(16위) — [llmlearner](https://llmlearner.com/rankings/creative-writing)
- 2026-10-29 읽음(felloai): GPT-6 Astra 2176.9 #1; Fable 5.1 2155.3 #3; GPT-6 Sol 2126.0 #5; Opus 5.5 2050.9 #8; Gemini 4 Argon 1757.8 #32 — [felloai](https://felloai.com/best-ai-for-writing/). (Kimi K3.1 Pro가 2위로 끼어든 10월 하순 스냅샷 — [myclaw](https://myclaw.ai/de/blog/opus-5-5-for-creative-writing))
- 심판 변경 이력: "News 2026-10-25" — 루브릭 심판을 GLM 5.3(OpenRouter, low reasoning)으로, pairwise Elo 심판을 **Claude Opus 5**(Anthropic API)로 변경 — [eqbench.com/about](https://eqbench.com/about.html). 2026-10-12 스냅샷 미러는 심판을 "Claude 4 Sonnet(루브릭) / Claude Sonnet 4.6(pairwise)"로 기재 — [vibecodingnav](https://www.vibecodingnav.com/benchmarks/eqbench-creative-writing/). 즉 **10월 25일 전후로 심판이 바뀌었으나 상위 순위는 거의 변동 없음**(Astra 2173→2177, Fable 5.1 2162→2155, Opus 5.5 2050→2051).
- 구 스냅샷(2026-09-24 데이터, 신모델 미수록): Claude Opus 4.7 2206(2026-04-16), GPT-5.5 2035(2026-04-23), Claude Opus 4.8 2031(2026-05-28) — [evals.report](https://evals.report/benchmarks/eq-bench?tab=scores). 심판/정규화가 다른 시기 수치이므로 현행 표와 직접 비교 불가.
- Sophon 미러는 같은 모델에 1741.5(Astra)~1640.7(Opus 5.5) 같은 다른 스케일 값을 표시하며 페이지 자체가 "최고 2177"과 불일치 — [sophon](https://sophon.at/evals/eqbench-creative-writing). 신뢰도 낮음, 참고만.
- 슬롭·반복 지표: 공식 페이지 컬럼은 Model, Abilities, Style, Slop, Repetition, Length, Rubric Score, Elo Score. Repetition = "가장 흔한 단어·bigram·trigram 빈도 합", Slop = "다수 모델 출력에서 과대표집된 단어·구문 마스터 리스트와 매칭" — [eqbench.com](https://eqbench.com/creative_writing.html). **모델별 슬롭·반복 수치는 어느 미러에도 없어 확보 실패.**

**C. EQ-Bench Longform Creative Writing** (8장 × ~1,000단어 중단편; 0–100점)
- 공식 페이지 v1.11 (2026-02-19): 심판 **Claude Sonnet 4.6**(Sonnet 4에서 업그레이드); 14개 루브릭 차원(긍정 8, 부정 6), "forced metaphor" 가중; 짧은 한 문장 단락 남용 시 degradation 페널티; Length·Slop은 점수에 미반영; 보통 OpenRouter temp 0.7, min_p 0.1 — [eqbench.com/creative_writing_longform](https://eqbench.com/creative_writing_longform.html). 표 데이터는 동적 로딩으로 추출 실패.
- Sophon 미러(날짜 미표기): 1위 Claude Opus 5 69.0; 2위 **Claude Fable 5.1 68.2**; 3위 **Claude Opus 5.5 67.7**; 4위 Grok 4.7 66.0; 5위 Claude Fable 5 66.0; 6위 **GPT-6 Astra 66.2**; 8위 GPT-6 Sol 66.2; 9위 Claude Opus 4.7 65.4; 11위 **GPT-5.6 Sol 65.4**; 14위 Opus 4.8 64.6; 21위 GPT-5.5 62.6 — [sophon longform](https://sophon.at/evals/eqbench-longform-creative-writing). 페이지 상단 "최고 86.3(Opus 5)"와 차트 69.0이 불일치 → 수치 신뢰도 낮음, 공식 페이지 재확인 필요.

**D. Lech Mazur — Short-Story Creative Writing Benchmark** (10개 필수 요소 통합 단편, 400 프롬프트/모델, pairwise Thurstone 모델)
- 1위 **Claude Fable 5.1 (high) 3.745** (승률 추정 93%, 95% CI 3.663–3.829); 2위 **Claude Opus 5.5 (high) 3.693** (93%, 3.586–3.776); 3위 Claude Opus 5 (xhigh) 3.685; 4위 **GPT-6 Astra (high) 3.416** (91%); 5위 Opus 5 (high) 3.322; 7위 Fable 5 (high) 2.810; 9위 **GPT-5.6 Sol (xhigh) 2.425** (82%); 10위 GPT-5.5 (xhigh) 2.390; 12위 GPT-5.6 Sol (high) 2.237; 16위 Opus 4.7 (high) 1.720; 21위 Opus 4.8 (xhigh) 0.717 — [lechmazur/writing](https://github.com/lechmazur/writing)
- 추가 일자: Fable 5.1 2026-09-02; GPT-6 Astra 2026-09-05; Opus 5.5·Opus 5(high) 2026-09-26; Gemini 4 Argon·Muse Wonder 2026-10-13; Kimi K3.1 Pro 2026-10-23 — [lechmazur/writing](https://github.com/lechmazur/writing)
- "Fable 5.1 takes first place" (2026-09-02 게시) — [Lech Mazur on X](https://x.com/LechMazur/status/2095269905834619106); Fable 5(high)는 Opus 4.8·4.7을 이기고 GPT-5.5(xhigh)에 이어 2위, 400개 중 5개 프롬프트 거부 — [Lech Mazur on X](https://x.com/LechMazur/status/2064503575577821458)

**E. Braintrust — "Opus 5.5 vs new GPT-6 models for writing quality"** (2026-09-22; 창작 아님, 수학 튜터링 175과제)
- Writing quality: Opus 5.5 84.4% (83.3–85.6); GPT-6 Sol 84.1%; GPT-6 Luna 83.8%; GPT-5.6 Sol 83.2%; Fable 5.1 82.1% — 상위 차이는 통계적으로 유의하지 않음; 심판 GLM-5.3-Flash; GPT-6 Astra 미포함 — [Braintrust](https://www.braintrust.dev/evals/opus-55-vs-gpt-6)
- "Assistant tics"(낮을수록 좋음): Fable 5.1 1%, Opus 5.5 ~6%, GPT-6 Sol ~10%, GPT-5.6 Sol 14% — [Braintrust](https://www.braintrust.dev/evals/opus-55-vs-gpt-6)

**F. 미발견/미수록**
- **WritingBench**: Opus 5.5·GPT-5.6·Fable 5.1 결과 검색에서 발견되지 않음 — [검색 결과](https://www.datacamp.com/blog/gpt-6-sol-vs-claude-opus-5-5) 등 코딩·지식노동 벤치마크만 확인.
- **Artificial Analysis**: 창작 글쓰기 전용 지수 없음; AA-LCR(장문 추론, ~100k 토큰)은 2026-10-28 미러 기준 Kimi K3 88.7% 1위이며 Opus 5.5·Fable 5.1·Astra 수치는 검색에서 확인되지 않음 — [benchlm AA-LCR](https://benchlm.ai/benchmarks/lcr)

### Inferences
- LLM 심판(EQ-Bench, Mazur)과 인간 투표(Arena)의 괴리가 매우 크다. GPT-6 Astra는 EQ-Bench 1위이지만 Arena 창작에서 40위(1450)이고, 반대로 Opus 5.5는 Arena 1위이나 EQ-Bench 7~8위다. Arena는 짧은 1턴 응답·스타일 컨트롤·대중 취향을, EQ-Bench는 4,000자 절단 후 전문 루브릭을 반영한다는 방법론 차이로 설명 가능(해석).
- Fable 5.1은 세 종류 평가(EQ-Bench 2~3위, Mazur 1위, Longform 2위) 모두 상위권으로 가장 일관된 반면, GPT-5.6 Sol은 모든 보드에서 네 모델 중 최하위(EQ-Bench 10위, Mazur 9위, Arena 18위, Longform 11위).
- EQ-Bench의 pairwise 심판이 2026-10-25부터 Claude Opus 5로 바뀌었음에도 OpenAI Astra가 1위를 유지한 점은 심판 자기선호 편향이 Anthropic에 유리하게만 작용하지는 않았음을 시사(단, 저자 스스로 통제하지 않았다고 명시).

### Gaps
- EQ-Bench 공식 페이지의 모델별 Slop·Repetition·Length·Rubric 수치는 동적 로딩으로 어느 소스에서도 확보하지 못함.
- EQ-Bench Longform 공식 수치 미확보(미러 수치 자체 불일치).
- "GPT-6 Sol"과 "GPT-6.1 Sol"이 Arena에서 서로 다른 항목으로 등장하며, Codex 현행 Sol이 어느 것인지 소스에서 확정 불가.
- Arena 점수는 10월 8일 → 15일 → 27일 사이에 1·2위가 뒤바뀔 정도로 변동하며 CI(±13)가 격차(3점)보다 크다.

---

## KQ2. 한국어/비영어 산문을 포함한 평가와 결과

### Takeaway
한국어 창작 글쓰기 전용 벤치마크는 없다. 유일한 정량 자료는 **Arena Text 한국어(🇰🇷) 카테고리**(전체 프롬프트 기준, 창작 한정 아님)로, 2026-10-27 기준 Claude Fable 5 (High) 1497 1위, Fable 5.1 (Max) 1494 3위이고 GPT-5.6 Sol (xHigh)은 20위 1455, GPT-6 Astra (Max) 21위, **Opus 5.5는 표에 없음**. EQ-Bench·Mazur·ConStory-Bench는 모두 영어 전용.

### Cited Findings
- Arena Text — Korean 리더보드 (2026-10-27, 139,643표, 287모델): 1위 Claude Fable 5 (High) 1497 ±22 (839표); 2위 Claude Opus 5 (Max) 1495 ±24; 3위 **Claude Fable 5.1 (Max) 1494 ±37 (264표)**; 4위 Claude Opus 5 (High) 1493 ±18 (1,392표); 9위 Claude Opus 4.7 1471; 11위 GPT-6.1 Sol (Max) 1467 ±44 (182표); 15위 Opus 4.6 1463; **20위 GPT-5.6 Sol (xHigh) 1455 ±22 (838표)**; **21위 GPT-6 Astra (Max)**; 22위 GPT-5.5 (Instant); 25위 Opus 4.8 (High); 29위 GPT-5.5 (High); 69위 GPT-6 Sol (Max) — [arena.ai/leaderboard/text/korean](https://arena.ai/leaderboard/text/korean)
- **Claude Opus 5.5는 한국어 리더보드 가시 영역(~148위까지)에 없음** — [arena.ai korean](https://arena.ai/leaderboard/text/korean). 한 트래커가 "Claude Opus 5.5 (High) Korean +146 Elo" 태그를 표시하나 의미 불명 — [검색 결과](https://benchlm.ai/llm-leaderboard-history)
- Arena 한국어 보드의 상위권 CI는 ±22~±44로 매우 넓어(Fable 5.1 264표) 1~5위는 통계적 동률 — [arena.ai korean](https://arena.ai/leaderboard/text/korean)
- Arena Creative Writing 카테고리는 언어 필터가 없고, 29개 카테고리 중 언어별 보드는 별도 — [arena.ai creative-writing](https://arena.ai/leaderboard/text/creative-writing)
- EQ-Bench CW v3: "Multilingual. It only tests writing in English." — [eqbench.com/about](https://eqbench.com/about.html)
- ConStory-Bench: "English fiction following Western narrative conventions"에 한정 — [arXiv 2603.05890](https://arxiv.org/html/2603.05890v1)
- 한국어 커뮤니티: "오퍼스 5.5 GPT-5.6 소설 글쓰기 비교" 및 "Fable 5.1 한국어 소설 테스트" 검색에서 한국어 소설 직접 비교 자료 미발견; AI매터스 기사(2026-10-02)는 Graphite의 **영어** AI-tell 분석을 한국어로 보도한 것 — [AI매터스](https://aimatters.co.kr/news-report/53972/)
- 일본어 블로그(IT navi)의 "Fable 5 / Opus 4.6 / GPT-5.6 Sol / Grok 4.5 단편 비교"는 "일본어 창작 중심"이라 밝히지만 게시된 본문은 영어; 단편 100점 만점 — GPT-5.6 Sol 심판: Fable 5 95, GPT-5.6 Sol 89, Opus 4.6 88, Grok 4.5 70; Fable 5 심판: Fable 5 92, Opus 4.6 84, GPT-5.6 Sol 83, Grok 4.5 60; 모델당 1편, AI 심판 자기선호 명시 — [IT navi](https://note.com/it_navi/n/nae74e5bf0ecd?hl=en). (이전 세대 Opus 4.6 기준, Opus 5.5·Fable 5.1 미포함.)

### Inferences
- 한국어 보드에서 Claude 계열(Fable 5/5.1, Opus 5)이 1~4위를 차지하고 GPT 계열이 11위 이하인 패턴은 영어 창작 보드와 방향이 같다. 다만 창작 한정이 아니라 한국어 전체 프롬프트의 결과라는 점에 유의.
- Opus 5.5의 한국어 부재는 Arena 등재 지연(투표 수 부족)일 가능성이 높으나 소스에서 확인되지 않음.

### Gaps
- 한국어 소설·산문 품질을 측정한 독립 벤치마크·블라인드 비교는 어느 모델에 대해서도 발견되지 않음.
- Opus 5.5의 한국어 Arena 점수 없음.
- GPT-6 Astra (Max) 한국어 점수 수치는 순위(21위)만 확보, 점수 미확보.

---

## KQ3. 장편 일관성(플롯·인물 유지)을 측정한 평가와 결과

### Takeaway
장문 일관성 측정 벤치마크로는 EQ-Bench Longform(8장 중단편, degradation 지표)과 ConStory-Bench(8,000~10,000단어, 일관성 오류 밀도)가 있다. Longform에서는 Claude Opus 5 69.0 > Fable 5.1 68.2 > Opus 5.5 67.7 > GPT-6 Astra/Sol 66.2 > GPT-5.6 Sol 65.4(미러 수치, 날짜 미표기, 신뢰도 낮음). **ConStory-Bench는 2026-03-05 이후 갱신이 없어 네 모델 모두 미수록.**

### Cited Findings
- EQ-Bench Longform 방법론: 최소 프롬프트 → 브레인스토밍·계획 → 성찰·수정 → 8장 × ~1,000단어 작성; 전체 장 평균 + 최종 평가의 0–100 점수; Degradation = 8장 평균의 스파크라인과 "마지막 장이 첫 장 대비 얼마나 떨어졌는가"; 짧은 단문 단락 남용 시 장 점수 축소; 심판 Claude Sonnet 4.6 (v1.11, 2026-02-19) — [eqbench.com/creative_writing_longform](https://eqbench.com/creative_writing_longform.html)
- Longform 미러 수치(날짜 미표기): Claude Opus 5 69.0; Claude Fable 5.1 68.2; Claude Opus 5.5 67.7; Grok 4.7 66.0; Fable 5 66.0; GPT-6 Astra 66.2; Muse Spark 1.3 66.2; GPT-6 Sol 66.2; Opus 4.7 65.4; GLM 5.3 65.4; GPT-5.6 Sol 65.4; Gemini 4 Argon 64.7; Opus 4.8 64.6; GPT-5.5 62.6(21위) — [sophon longform](https://sophon.at/evals/eqbench-longform-creative-writing). 미러 내부 불일치(86.3 vs 69.0) 존재.
- 모델별 Degradation·Slop·Repetition 수치는 미확보 (공식 페이지 동적 로딩) — [eqbench.com/creative_writing_longform](https://eqbench.com/creative_writing_longform.html)
- ConStory-Bench ("Lost in Stories", arXiv 2603.05890, 2026-03 제출): 4개 과제 시나리오, 5개 오류 범주·19개 세부 유형, 7개 공개 코퍼스에서 프롬프트 수집, 8,000–10,000단어 서사 유도; Consistency Error Density(CED, 1만 단어당 오류) 최저는 GPT-5 (reasoning) 0.113; 심판(ConStory-Checker) o4-mini; 표 최종 갱신 2026-03-05; Claude Opus 5/5.5, Fable 5/5.1, GPT-5.5/5.6/6 **모두 미수록** — [ConStory-Bench](https://picrew.github.io/constory-bench.github.io/); [arXiv](https://arxiv.org/html/2603.05890v1)
- NCP-Bench (arXiv 2608.08160, ICML 2026): 영화 시놉시스 기반 100개 인터랙티브 서사 환경, 최고 모델 GPT-5.2가 20턴 후 생존률 42% — [arXiv 2608.08160](https://arxiv.org/abs/2608.08160). 고정 소설이 아닌 인터랙티브 환경이며 네 모델 미포함.
- WSE-bench (arXiv 2608.15654): 개방형 세계 시뮬레이션에서 "Consistency와 Richness가 매끄러운 트레이드오프를 형성하지 않음" — [arXiv 2608.15654](https://arxiv.org/abs/2608.15654). 네 모델 미포함.
- NovelQA: 2026년 네 모델 결과 검색에서 발견되지 않음(독해 벤치마크로 창작 일관성과 직접 관련 없음).

### Inferences
- 장편 일관성에서 네 모델을 직접 비교할 수 있는 유일한 자료는 EQ-Bench Longform이며, 그 격차(67.7 vs 66.2 vs 65.4)는 2점 미만으로 심판 노이즈 범위일 가능성이 있다(해석).
- 2026년 상반기 학계 벤치마크들은 모두 GPT-5 세대에서 멈춰 있어, 현 세대의 장편 일관성은 사실상 측정되지 않은 상태로 봐야 한다.

### Gaps
- Opus 5.5·Fable 5.1·GPT-6 Astra·GPT-5.6 Sol의 CED(일관성 오류 밀도) 수치 없음.
- EQ-Bench Longform의 모델별 degradation(첫 장→마지막 장 하락폭) 수치 미확보.
- 8장(~8,000단어)을 넘는 장편(novel-length) 평가는 어느 모델에도 없음.

---

## KQ4. 벤치마크 저자들이 밝힌 한계(LLM 심판 편향, 슬롭)

### Takeaway
EQ-Bench 저자는 심판 자기선호·긍정성·슬롭 편향을 "통제하지 않는다"고 명시하고, 길이 편향은 4,000자 절단으로 처리하며, 영어 전용임을 밝힌다. Lech Mazur는 "심판 간 일치가 심판 정확도를 입증하지 않는다"고 적고, 누락 스토리와 심판 교체가 점수에 미칠 영향을 신뢰구간이 반영하지 못한다고 경고한다. 슬롭 측정은 학계(COLM 2026)에서도 "합의된 정의가 없다"는 단계다.

### Cited Findings
- EQ-Bench CW v3 저자 명시 한계: "do not control for the judge possibly preferring its own outputs"(자기선호); 길이 편향은 pairwise 전 4,000자 절단으로 처리하며 순위에 영향 없다고 봄; 긍정성 편향 방향 불명·미통제; NSFW 튠 모델 불리("smut bias"); 슬롭·스타일·내용 편향 경험적 미통제; 롤플레이 평가 아님; 영어 전용 — [eqbench.com/about](https://eqbench.com/about.html)
- EQ-Bench Elo 방식: 32 프롬프트 × 3회(96개) temp 0.7, min_p 0.1; 루브릭 점수로 초기 Elo 시드 → 인접 모델과 희소 pairwise → 최종 인접 모델과 전면 pairwise; Glicko 변형(승리 마진을 "+" 승리로 가산); 각 기준을 양방향 제시 순서로 판정 후 평균; DeepSeek-R1 = 1500, ministral-3b = 200 고정 — [eqbench.com/about](https://eqbench.com/about.html)
- EQ-Bench Longform: "forced metaphor"를 심판이 잘 감지하지 못해 가중치를 높임 — [eqbench.com/creative_writing_longform](https://eqbench.com/creative_writing_longform.html)
- Lech Mazur: 심판 일치가 "does not establish evaluator accuracy"; 단어 수(600–800 목표)는 "measures length rather than writing quality"; Opus 4.7은 400편 중 347편만 완료, Opus 4.8(high) 399편 — 구간은 "do not account for how missing stories or judgments might change the scores"; 신규 심판만의 결과는 다를 수 있고 구간 중첩 시 순위 차는 불확실; 사전 선별된 요소 조합이라 자유 창작을 측정하지 않음; 공개 점수는 "not an average 0-10 grade" — [lechmazur/writing](https://github.com/lechmazur/writing)
- Lech Mazur는 심판 모델명을 "earlier/newer evaluator"로만 표기, 구체 모델 미공개 — [lechmazur/writing](https://github.com/lechmazur/writing)
- IT navi(일본어 블로그): Fable 5 심판이 자기 가족 모델을 평가했고, 두 AI 심판 모두 장면 라운드에서 자기 작품을 1위로 놓았음을 명시 — [IT navi](https://note.com/it_navi/n/nae74e5bf0ecd?hl=en)
- Braintrust: "small run", 상위 차이 통계적으로 유의하지 않음, 심판은 모델이고 인간 아님 — [Braintrust](https://www.braintrust.dev/evals/opus-55-vs-gpt-6)
- Arena: 2025~2026 창작 보드 1·2위는 ±13 CI 안의 통계적 동률이며 집계 시점에 따라 순서가 바뀜 — [felloai](https://felloai.com/best-ai-for-writing/); [arena.ai](https://arena.ai/leaderboard/text/creative-writing)
- 슬롭 측정 학계 현황: COLM 2026 "Measuring AI 'Slop' in Text" — "no agreed upon definition of this term nor a means to measure its occurrence"; 이진 슬롭 판정은 "(somewhat) subjective"이나 coherence·relevance 등 잠재 차원과 상관; density 지표(토큰 엔트로피·명제 밀도) 제안 — [arXiv 2509.19163](https://arxiv.org/html/2509.19163)
- Graphite AI-tell 분석(2026-10-01, 영어; TechCrunch 경유, 한국어 보도 AI매터스 2026-10-02): 9,974편의 ChatGPT 이전 인간 기사 대비 2배 이상 과용된 단어·구문·구조를 "AI tell"로 분류. **Claude Opus 5.5**: 과용 tell 2,548개(Opus 5의 2,666개보다 약 4% 감소); "this matters" 116배, "why ○○ matters" 92배, "is more than a ○○" 98배, "looking ahead the" 40배, "dependable" 23배; 인간 대비 분포 격차 Opus 5보다 19% 감소; 수사적 과장 점수 16.75→10.57(인간 6.65, 여전히 1.6배); 엠대시 1,000단어당 2.92→0.015(-99%). **GPT-6 Astra**의 분포 격차는 GPT-5.6 Sol보다 8% 커짐(반대 방향); Opus 5.5는 "the most powerful"을 Astra보다 24배 더 사용, Astra는 "may provide" 류 헤지 더 사용. Graphite CAIO Gregory Druck: Claude는 인간 분포로 수렴, GPT는 멀어지는 추세 — [AI매터스](https://aimatters.co.kr/news-report/53972/). Fable 5.1 미포함, 기사 재작성 과제라 소설 적용성 제한.
- Every 가독성 측정(2026-09-22, 프롬프트 수 미공개): Flesch-Kincaid 학년/Reading Ease — Opus 5.5 6.95/68.42; Fable 5.1 7.43/66.09; GPT-6 Astra 7.52/64.55; Opus 5 7.97/61.35; GPT-5.6 Sol 8.74/56.62 — [Every](https://every.to/vibe-check/vibe-check-opus-5-5-is-pulling-our-codex-converts-back-to-claude)
- Codex 시스템 지시문 차이: Astra 템플릿은 글쓰기에 명시적 anti-slop 정책을 추가, Sol은 "clear communication and minimal formatting" 중심 — [WolframRvnwlf](https://x.com/WolframRvnwlf/article/2096018047538450580)

### Inferences
- EQ-Bench의 pairwise 심판이 Claude Opus 5(2026-10-25~)인 상태에서 Fable 5.1·Opus 5가 2~3위라는 점은 같은 가족 심판의 자기선호 가능성을 배제할 수 없으나, Opus 5.5는 7~8위에 머물러 단순한 "Anthropic 편향"으로 설명되지는 않는다.
- Graphite 자료는 Opus 5.5의 "슬롭"이 어휘 다양성 면에서 줄었지만 특정 강조 구문("this matters")이 극단적으로 과용되는 새 패턴을 보였음을 시사 — 소설에서 "설명조 강조"로 나타날 수 있음(해석).

### Gaps
- EQ-Bench 공식 Slop Index·Repetition 모델별 수치 없음.
- Lech Mazur 심판 모델 정체 미공개.
- Fable 5.1에 대한 AI-tell 밀도 분석(Graphite류) 없음.

---

## KQ5. 네 모델 소설에 대한 직접 인간 블라인드 비교

### Takeaway
네 모델(Opus 5.5, Fable 5.1, GPT-6 Astra, GPT-5.6 Sol)의 **소설**을 동일 조건에서 인간이 블라인드로 비교한 공개 연구는 발견되지 않았다. 가장 가까운 것은 Arena 창작 카테고리의 대규모 익명 투표(Opus 5.5 1위, Fable 5.1 8위, GPT-5.6 Sol 18위, Astra 40위)와, Noren의 6인 패널 블라인드 테스트(GPT-5.6 Sol vs GPT-5.5만, 2026-07)이다. 나머지는 리뷰어 개인의 비블라인드 평가다.

### Cited Findings
- Arena Creative Writing: 익명 쌍대 인간 투표(1,450,312표) — Opus 5.5 (High) 1520 1위; Fable 5.1 (Max) 1489 8위; GPT-5.6 Sol (xHigh) 1470 18위; GPT-6 Astra (Max) 1450 40위 (2026-10-27) — [arena.ai](https://arena.ai/leaderboard/text/creative-writing). 창작 카테고리이나 소설 전용은 아니며 짧은 응답 위주.
- Noren 블라인드 테스트(2026-07-10 게시, 07-31 갱신): 동일 에픽 판타지 프롬프트, GPT-5.6 Sol/Terra/Luna + GPT-5.5, raw/프로필 2조건 × 3편 = 24편, Sample A~X로 익명화, 6인 리뷰어가 산문·장면·감정도덕 복잡성·충실도·출판 가능성 채점; 1라운드에서 GPT-5.5가 50% 더 길게 써서 이겨 길이 통일 후 재실행. 평균 순위(24편 중, 낮을수록 좋음): Sol+Noren 5.56; GPT-5.5 raw 7.50; GPT-5.5+Noren 8.72; Sol raw 11.61; Terra+Noren 14.00; Luna+Noren 16.06; Terra raw 16.72; Luna raw 19.83. 모델 평균: GPT-5.5 8.11, Sol 8.58, Terra 15.36, Luna 17.94. 단일 프롬프트, 저자가 Noren 공동창업자(이해상충 미고지) — [Noren GPT-5.6 Writing Test](https://usenoren.ai/blog/gpt-5-6-writing-test). Claude 모델 미포함.
- Lenny's Newsletter(Claire Vo, 2026-09-22) "Opus 5.5 vs GPT-6 Sol 블라인드 테이스트 테스트": 이메일·PRD·프론트엔드·에이전트 등 업무 과제, 모델을 모르고 채점; 소설 결과 없음; 결론 "Astra won my heart", Opus 5.5 "won my week", Sol은 "clear writing, readable PRDs, and price"; 별도 LLM 심판은 저자와 다른 순위; Fable 미언급 — [Lenny's Newsletter](https://www.lennysnewsletter.com/p/opus-55-vs-gpt-6-sol-which-model)
- Anthropic Fable 5.1 발표문: 작가 Dwight Temple이 Fable 5 대비 블라인드 테스트에서 Fable 5.1을 선호했다는 인용(벤더 제공, 방법 미공개) — [Anthropic](https://www.anthropic.com/claude-fable-and-mythos-5-1)
- Every(비블라인드): Astra "the best writing model I've tried", Opus 5.5는 편집자로서 Opus 5·GPT-5.6 Sol·Astra보다 아래, Astra가 헤드라인·첫 문장·아이디어 순서에서 승리; Katie Parrott는 Opus 5.5 산문을 "most readable"이라면서도 "still buries the point"(21문장 분량을 37~39문장으로); Mike는 작가로서 Fable 5.1 선호 — [Every Opus 5.5 vibe check](https://every.to/vibe-check/vibe-check-opus-5-5-is-pulling-our-codex-converts-back-to-claude); Astra가 "very little slop"이지만 "turning everything into a landing page" 습관 — [Dan Shipper](https://x.com/danshipper/status/2095593705214300394)
- Zvi(2026-09-05) Fable 5.1 리뷰: 창작 벤치마크·블라인드 비교 없음; "Writing is greatly improved", "Claudisms seem to have improved, although some are very much still there"; Dan Shipper "clearer prose, fewer AI tells"; Seth Lazar는 Astra가 스토리에 대한 반응을 불필요하게 검열하는 반면 Fable은 문제없다고 언급 — [Zvi](https://thezvi.substack.com/p/claude-mythos-51-and-fable-51-capabilities)
- 한국어 사용자 평(비블라인드, X): "Astra's creative writing capabilities have improved significantly compared to GPT-5.6 Sol… responds very well to feedback" — [NomoreID/Hangsiin on X](https://x.com/Hangsiin/status/2096506933683666955)

### Inferences
- 리뷰어 개인 평가(Every, Lenny)는 비소설·업무 글쓰기에서 Astra를 선호하는 반면, 대중 익명 투표(Arena 창작)는 Opus 5.5·Claude 계열을 강하게 선호한다. 이는 "에디터·전문가 취향"과 "대중 취향"의 차이이거나, Arena의 짧은 1턴 포맷이 Claude에 유리한 구조일 수 있다(해석).
- 네 모델 소설의 통제된 인간 블라인드 비교는 공백이며, 현재 가장 견고한 인간 신호는 Arena 투표다.

### Gaps
- Opus 5.5·Fable 5.1·GPT-6 Astra·GPT-5.6 Sol 소설을 인간 패널이 블라인드로 직접 비교한 연구 없음.
- Noren의 Claude Fable 5 writing test(usenoren.ai/blog/claude-fable-5-writing-test)는 Fable 5·Sonnet·Opus 비교로 추정되지만 본 조사에서 미열람.
- Every의 checks.every.to 원 데이터 미확인.
