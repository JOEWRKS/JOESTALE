# Anthropic 최신 모델(Claude Opus 5.5 / Claude Fable 5.1)의 창작·문학 글쓰기 적합성

조사 기준일: 2026-11-01. 2026년 9월 이전 자료(Fable 5, Opus 5 관련)는 "[구버전 자료]"로 표시. 인용은 원문 언어 유지.

## 핵심 질문 1. 공식 스펙·가격·플랜 가용성, 그리고 어느 모델이 어떤 용도에 권장되는가

### Takeaway
Fable 5.1(2026-09-01 출시, $10/$50)과 Opus 5.5(2026-09-22 출시, $4/$20)는 컨텍스트 1M·최대 출력 128K·지식 컷오프 2026년 6월로 스펙이 동일하며, Anthropic은 "대부분의 워크로드는 Opus 5.5로 시작하고, 고난도 추론·장기 에이전트 작업이거나 Opus 5.5 고effort로도 부족할 때 Fable 5.1"을 권장한다. Fable 5.1과 Mythos 5.1은 "같은 모델에 안전장치 수준만 다른" 관계이고, Mythos는 검증 프로그램(미국 조직) 한정이다.

### Cited Findings

**출시일·포지셔닝**
- Fable 5.1 공식 모델 페이지: "**Latest.** Released September 1, 2026." / "For demanding reasoning and long-horizon agentic work" / Model ID `claude-fable-5-1` — [platform.claude.com Fable 5.1 overview](https://platform.claude.com/docs/en/models/fable-5-1/overview)
- Opus 5.5는 2026-09-22 출시, Claude 5.5 패밀리의 첫 모델. Anthropic: Opus 5.5 "performs at the level of Claude Fable 5.1 on most work" 이며 Opus 5 대비 운영 비용 40% 절감. 벤치마크 격차는 "narrower than these scores suggest". — [Anthropic: Claude Opus 5.5](https://www.anthropic.com/news/claude-opus-5-5)
- 공식 모델 비교표의 설명란: Fable 5.1 = "For demanding reasoning and long-horizon agentic work", Opus 5.5 = "For long-running agentic coding and knowledge work", Sonnet 5.5 = "The best combination of speed and intelligence". 선택 가이드: "If you're unsure which model to use, start with Claude Opus 5.5 for most workloads. Use Claude Fable 5.1 for demanding reasoning and long-horizon agentic work, or when your evals on Claude Opus 5.5 at higher effort still fall short." — [Models overview](https://platform.claude.com/docs/en/models/overview)
- Fable 5.1 / Mythos 5.1 관계(공식): "Claude Fable 5.1 and Claude Mythos 5.1 are the same model, but with different levels of safeguards." Mythos 5.1은 "identical to Fable 5.1, but it offers more permissive safeguards" (검증된 개인·조직용), 현재 미국 조직 한정, 안전장치는 "specifically designed to support work in cybersecurity and the life sciences". — [Anthropic: Claude Fable 5.1 and Mythos 5.1](https://www.anthropic.com/claude-fable-and-mythos-5-1)
- Fable 5.1의 "추가 안전장치" 실체(공식): 소스코드 취약점 탐색은 허용, 익스플로잇 개발은 불허. 침투 테스트·익스플로잇 생성·바이너리 취약점 스캐닝과 생명과학 R&D 질의는 Opus 계열 모델로 라우팅됨. 신규 안전장치에서 사이버 오탐(false positive) 60% 감소, 생물학 안전장치는 무해한 기초 생물학·의학 질문에서 Fable 5 출시 시점 대비 85% 덜 발동. — [Anthropic: Claude Fable 5.1 and Mythos 5.1](https://www.anthropic.com/claude-fable-and-mythos-5-1)
- Opus 5.5도 "Fable 5.1과 유사한 안전장치(사이버·생물학·distillation)"를 갖고 출시된 첫 Opus. 대부분의 사이버보안 작업은 Opus 4.8로 투명하게 폴백. 프롬프트 인젝션 저항성은 Opus 5보다 향상. Thinking은 끌 수 없음. — [Anthropic: Claude Opus 5.5](https://www.anthropic.com/news/claude-opus-5-5)
- Zvi(시스템카드 리뷰): Opus 5.5는 "looks like a smaller version of Fable 5.1, rather than a new iteration of the existing Opus line." (Anthropic 공식 문서상 '가중치 공유'나 distillation 언급은 없음) — [LessWrong: Claude Opus 5.5: The System Card](https://www.lesswrong.com/posts/vMNTWTDWLorDqd3LS/claude-opus-5-5-the-system-card)

**스펙·가격**
- 공식 비교표(Fable 5.1 / Opus 5.5): 컨텍스트 1M / 1M, 최대 출력 128K / 128K, 가격 $10·$50 / $4·$20 (입력·출력 MTok), 상대 지연 Slower / Moderate, Thinking "Adaptive (always on)" 둘 다, 기본 effort `high` / `medium`, 지식 컷오프 Jun 2026 둘 다, 은퇴 시점 2027-09-01 / 2027-09-22 이전 불가. — [Models overview](https://platform.claude.com/docs/en/models/overview)
- 토크나이저 참고: "1M tokens is roughly 555k words or 2.5M Unicode characters on the current tokenizer (introduced with Claude Opus 4.7)". Batch API 50% 할인. 캐시 읽기: Fable 5.1 $0.25/MTok(기본 입력가의 2.5%), Opus 5.5 $0.20/MTok. — [Models overview](https://platform.claude.com/docs/en/models/overview); [Fable 5.1 overview](https://platform.claude.com/docs/en/models/fable-5-1/overview)
- Opus 5.5 캐시 쓰기 $5, Fast mode(최대 2.5배 속도) $8/$40, Claude Code와 Claude Platform에서 제공. — [Anthropic: Claude Opus 5.5](https://www.anthropic.com/news/claude-opus-5-5)
- Fable 5.1 가격은 Fable 5와 동일($10/$50), 캐시 읽기만 75% 인하($0.25). 전형적 워크로드 약 25%, 고도 에이전트 작업 최대 약 45% 절감 추정. 5m 캐시 쓰기 $12.50, 1h $20. — [Fable 5.1 overview](https://platform.claude.com/docs/en/models/fable-5-1/overview); [Anthropic 발표](https://www.anthropic.com/claude-fable-and-mythos-5-1)
- Batch API 300K 출력 베타 헤더(`output-300k-2026-03-24`) 지원 목록에 Opus 5.5는 포함, **Fable 5.1은 미포함**. — [Models overview](https://platform.claude.com/docs/en/models/overview)
- 속도: Opus 5.5는 "generates output tokens more than 30 percent faster than Claude Opus 5 and tends to complete the same task with fewer tokens." — [Prompting Claude Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5)
- Fable 5.1 기본 effort: Claude Code에서 High, Claude Cowork·Claude.ai에서 Medium. — [Anthropic 발표](https://www.anthropic.com/claude-fable-and-mythos-5-1)

**플랜 가용성(Claude.ai / Claude Code)**
- Fable(공식 지원문서): Free 플랜 불가. Pro는 "Fable 5 and Fable 5.1 aren't included in your plan's usage limits" → 사용량 크레딧(종량)으로 결제. Max/Ultra는 "You can use up to 50% of your weekly usage limits on Fable models at no extra cost." Team Premium 시트=Max 규칙, Standard 시트=Pro 규칙. Claude Code에서 Fable 5.1은 v2.1.255 이상 필요. — [support.claude.com Fable 안내](https://support.claude.com/en/articles/15424964-claude-fable-5-promotional)
- Opus 5.5: Pro/Max 포함, Free 불포함(Sonnet·Haiku만). Claude Code 기본 모델이 Opus 5.5(v2.1.280 이상). Anthropic은 Pro·Max·Team·시트형 Enterprise의 5시간 사용 한도를 상향했으나 수치 미공개. Opus 5.5 vs Fable 메시지의 플랜 한도 소모 비율은 미공개. — [christopheralarcon.com](https://christopheralarcon.com/blog/claude-opus-5-5-vs-fable/) (2차 자료); [Anthropic: Claude Opus 5.5](https://www.anthropic.com/news/claude-opus-5-5)
- 2차 자료 정리: Pro = "Opus 5.5 is your top included model; Fable is metered." Claude Code는 claude.ai·데스크톱과 사용량 풀 공유(5시간 롤링 + 주간 상한). Fable→Opus 5.5 전환 시 주당 약 4.3배 작업량(커뮤니티 추정치, Anthropic 수치 아님). — [The AI Career Lab](https://theaicareerlab.com/blog/claude-opus-5-5-vs-fable-5-1-for-professionals)
- 한국어 가이드: Opus 5.5는 Pro 이상 유료 플랜과 API에서 제공, 무료 플랜 불가(2026-09 기준). — [wikidocs 블로그](https://wikidocs.net/blog/@openwiki/?tag=21693)
- 한국 블로그(2026-09-23): API에서 모델명만 바꾸면 "노력 단계가 조용히 한 칸 내려갑니다"(기본 effort high→medium). Fable 5.1은 약 2.5배 비싸므로 Opus 5.5 고effort를 먼저 시도 권장. — [GPTers](https://www.gpters.org/news/post/claude-opus-55-vs-aOgt8qu7xSa4sTJ)

### Inferences
- 글쓰기 용도로 API를 쓸 경우 두 모델의 하드 스펙(1M/128K)은 같고 가격만 2.5배 차이이므로, "Fable이 산문에서 실제로 더 낫다"는 증거가 있을 때만 Fable을 쓰는 것이 합리적이다.
- Claude.ai Pro 사용자는 Fable 5.1이 종량 과금이라 장편 반복 드래프팅에 비용 부담이 크다. Max(50% 상한)여야 Fable을 일상적으로 쓸 수 있다.
- Fable의 "추가 안전장치"는 사이버·생명과학 이중용도에 집중되어 있어, 창작 글쓰기(어두운 주제 포함)와 직접적 관련은 공식 문서상 확인되지 않는다. 다만 Fable 5 시절 분류기 오탐(예: 'cancer' 단어 차단) 사례가 있었으므로 의학·범죄 소재 소설에서 간접 영향 가능성은 남아 있다(질문 4 참조).

### Gaps
- Anthropic은 Claude.ai에서 Opus 5.5와 Fable 5.1 메시지 1건이 플랜 한도를 각각 얼마나 소모하는지 공개하지 않았다.
- Fable 5.1 "9월 1일" 출시일은 공식 모델 페이지로 확인했으나, Anthropic 뉴스 페이지에는 날짜가 "September 2026"으로만 표기됨.
- "Fable 5.1이 Mythos 5.1과 가중치를 공유한다"는 표현은 Anthropic이 "same model / identical"로 서술한 것이지, 가중치·distillation에 관한 기술적 명세는 없다.

## 핵심 질문 2. Anthropic이 글쓰기 품질에 대해 주장하는 것과 독립적 증거

### Takeaway
Anthropic의 공식 주장은 "더 자연스러운 소통", "핵심을 먼저", "주어진 글쓰기 규칙을 따름"(Opus 5.5)과 고객 증언("The standout in Claude Fable 5.1 is the writing", Canva) 수준이며 소설·대화·스토리텔링에 대한 주장은 없다. 독립 증거는 Opus 5.5가 가독성·규칙 준수·'AI 티' 감소에서 좋아졌지만 독창성·주제 깊이는 Opus 5보다 낮게 채점됐고, Fable 5.1은 "작가로서 더 선호"되나 문장이 더 밀도 높고 비싸다는 쪽으로 모인다.

### Cited Findings

**Anthropic 공식 주장**
- Opus 5.5: "communicates more naturally than prior models", 핵심 정보를 먼저 배치, "follows the writing rules you give it". 테스터 인용 "it writes the way I do". 컨텍스트·다국어·장문 성능은 발표문에 언급 없음. — [Anthropic: Claude Opus 5.5](https://www.anthropic.com/news/claude-opus-5-5)
- Opus 5.5 시스템카드(Zvi 인용): 모델이 "somewhat lags behind other models in measures like humor and creative mastery". 주요 관찰 이슈는 "around epistemic quality and instruction following"(검증 안 된 추론을 사실처럼 단정, 자기 의심을 무시하거나 계획을 포기). Zvi: 성격 지표는 "largely unchanged apart from condescension"이지만 사용자 반응은 "somewhat of a return to classic Claude form". — [LessWrong: Opus 5.5 System Card 리뷰](https://www.lesswrong.com/posts/vMNTWTDWLorDqd3LS/claude-opus-5-5-the-system-card)
- Fable 5.1 발표: 벤치마크는 산문 품질을 직접 측정하지 않으며 고객 증언만 존재. Canva: "The standout in Claude Fable 5.1 is the writing" (블라인드 테스트에서 Fable 5.1 선호). Jane Street: "remains readable over long, multi-step tasks". Glean: 일상 지식 질문에서 Fable 5.1 답변을 약 2:1로 선호. 다국어·공식 지시 준수 벤치마크 언급 없음. — [Anthropic: Fable 5.1 and Mythos 5.1](https://www.anthropic.com/claude-fable-and-mythos-5-1)
- 공식 문서 일반 서술: "Top-tier results in reasoning, coding, multilingual tasks, long-context handling, honesty" / "Claude models are ideal for applications that require rich, human-like interactions." — [Models overview](https://platform.claude.com/docs/en/models/overview)
- Inkfluence AI(2026-10-09, 벤더 블로그, 자체 산문 테스트 없음): "Anthropic makes no claim about fiction, dialogue or storytelling for any current model." Fable 5.1은 "a specialist, not a prose upgrade". — [Inkfluence AI](https://www.inkfluenceai.com/blog/best-claude-model-for-writing-2026)

**독립 평가 — Opus 5.5**
- Every(Katie Parrott, 2026-09-22, 10-14 갱신): Opus 5.5 산문은 "the most readable prose we've seen from an Anthropic or OpenAI model." Flesch-Kincaid 학년/Reading Ease: Opus 5.5 6.95/68.42, Fable 5.1 7.43/66.09, Opus 5 7.97/61.35, GPT-6 Astra 7.52/64.55, Grok 4.6 6.63/69.17. 약점: "still buries the point". 장황함: 에세이 도입부를 "37 to 39 sentences to cover what I did in 21". Mike Taylor: "I still prefer Fable as a writer and for the bigger, meatier problems." 결론: 시각 작업 외에는 "Fable is the safer pick". — [Every: Vibe Check Opus 5.5](https://every.to/vibe-check/vibe-check-opus-5-5-is-pulling-our-codex-converts-back-to-claude)
- Ryan Doser(2026-09-23, 5회×2모델 스크립트 채점, 150~200단어 LinkedIn 글): 스타일 규칙 전부 충족 Opus 5 0/5, Opus 5.5 4/5. 두 모델 모두 em dash·금지어·"not X, it's Y" 0건. 2문장 초과 단락: Opus 5 10개, Opus 5.5 1개. 평균 34초/$0.28 vs 42초/$0.41. 주의: "This measures rule-following, speed and cost, not whether the ideas were better." Opus 5에 대해 "a tragedy for anyone who writes". — [ryandoser.com](https://ryandoser.com/best-claude-model-for-writing/)
- Arena(Text Arena 고추론 출력 분석, X 게시): Opus 5.5 vs Opus 5에서 "10 of 12 writing measures moved in a better direction". em dash 95% 감소(15.2→0.8/1,000단어), 세미콜론 73% 감소, 평균 문장 길이 12.14→10.03단어. **악화**: 헤지·단서어("perhaps", "arguably") 97% 증가(0.39→0.77/1,000단어, 분석된 Claude 모델 중 최고), 평균 답변 길이 6% 증가(453→481단어). — [Digg 요약](https://digg.com/ai/757gj9kn) (원 출처 https://x.com/arena/status/2103532528946839901)
- Pangram(1,000 프롬프트): 탐지 정확도 99.70%. "genuinely" 83% 감소, "matters enormously" 82% 감소, "In short" 9→100회, 요약 마커 +942%, 번호 목록 +111%, 평균 문장 길이 14.53→12.50단어. 소설풍 상투구 증가: "for a long moment" 19→42회, "said quietly", "felt something" 증가 → "a more stereotyped or limited repertoire when writing fiction" 의심. 블라인드 333쌍(Haiku 4.5 채점) 독창성·놀라움·주제 전개 모두 Opus 5.5가 평균 0.75점 낮음; 희망·회복·가족·우정 주제로 기울고 죽음·시간·권력·슬픔·상실에서 멀어짐. — [Pangram](https://www.pangram.com/blog/can-pangram-detect-opus-5-5)
- Mazur 제약 스토리 벤치마크: "Claude Opus 5.5 Tops Mazur Constrained Story Writing Benchmark" 제목의 리더보드 페이지가 존재하나 본문·점수 추출 실패(9모델 50태스크 샘플, 일부 채점 미완). — [RuntimeWire](https://runtimewire.com/benchmarks/mazur-writing-leaderboard)
- HN 출시 스레드 반응(2차 인용): sailingparrot "more human sounding output"; mcintyre1994는 "Claude Opus 5/Fable writing style" 때문에 "mostly moved to Astra"했다고. — [christopheralarcon.com](https://christopheralarcon.com/blog/claude-opus-5-5-vs-fable/)
- AIReiter(한국어 리뷰): 초기 글쓰기 평가가 긍정적이며 결과물이 덜 "Claude스럽다"는 언급이 잦음(영어권 반응으로 보임). — [aireiter.com](https://aireiter.com/ko/blog/claude-opus-5-5-review-pricing)

**독립 평가 — Fable 5.1 / Fable 5**
- Fable 5.1 문체 변화(Anthropic 프롬프팅 가이드의 한국어 번역 요약, apidog): "문체는 일반적으로 이전보다 향상되었으며, 상투적인 표현이 줄었습니다." / "일부 경우에는 Fable 5보다 밀도 높습니다: 더 긴 문장, 더 적은 단락 구분." 채팅 응답에서 볼드·헤더·목록 사용 감소. 요약 시 출처 문구를 인용 표시 없이 재사용하는 경향 증가. 'mannered prose' 안티패턴 지적. — [apidog KR](https://apidog.com/kr/blog/prompting-claude-fable-5-1/)
- HN(Fable 5.1 스레드): Anthropic 직원이라 밝힌 felixrieseberg: Fable 5.1 "sounds a lot less stereotypically like other Claude models." mrcwinn: "It's much better at getting to the point." 반면 Opus 5 계열에 대해 niccl "I have no real idea of what it's trying to tell me", malfist "dense and vacuous", mywittyname: "that's not X, it's Y" 류 표현이 명시적 금지 지시 후에도 반복. — [HN 49525378](https://hn.nuxt.dev/item/49525378)
- Sudowrite(2026-09-02): Fable 5.1 추가. "We haven't put it through its paces on long-form fiction just yet, so we can't fully attest to its prose." Anthropic이 말한 "fewer false refusals"에 근거해 어두운 주제·폭력·성적 장면 등 "legitimate story content"에서 덜 거부할 것으로 기대. Fable 5는 "a recent favorite among Sudowrite authors". — [Sudowrite changelog](https://feedback.sudowrite.com/changelog/new-ai-model-claude-fable-51)
- Automaton Agency(2026-09-10, 콘텐츠 에이전시 블로그): Fable 5.1 "Highest writing Elo of any tracked model"(Arena ~1508, BenchLM 인용), EQ-Bench GPT-isms(낮을수록 좋음)에서도 Fable 선두(원점수 미제시). 음성 프로필 테스트: "The gap between a model's profiled and unprofiled output was bigger than the gap between any two models." — [automatonagency.com](https://automatonagency.com/insights/claude-fable-vs-opus-5)
- [구버전 자료, Fable 5] Zvi 종합: Yudkowsky "Claude Fable (Mythos-) has substantially improved fiction-plotting capabilities" 단 "Fable remains bad at ranking the goodness of its own ideas." Kendric Tonn: 장편 원고 해석에서 "clearly better than anything I've touched previously". Hannah Groch-Begley: "Fable's output uses far less 'AI-sounding' text." Mazur 창작 벤치마크: GPT-5.5보다 약간 아래, 400개 중 5개 거부. Joe Weisenthal(트윗 문체 모방): "Fable fails my first test." — [Zvi: Fable 5 and Mythos 5 Capabilities](https://thezvi.substack.com/p/claude-fable-5-and-mythos-5-capabilities)
- [구버전 자료, Fable 5] Novelcrafter(2026-08-05): "Fable showed a remarkable ability for planning and analysing stories" 그러나 글쓰기 파트너로 권하기엔 너무 비쌈. — [Novelcrafter](https://www.novelcrafter.com/blog/opus-5-for-writers)
- 1인 사용자 보고(Digg): Fable 5.1을 리서치·브레인스토밍에 쓴 사용자가 문체가 거슬리고 Astra보다 "less nuanced and thorough"하다고 평. — [Digg](https://digg.com/ai/6tevlmun)

### Inferences
- Opus 5.5의 개선은 "규칙 준수·가독성·Claude 특유 상투어 감소"라는 '편집 비용' 축에 집중되어 있고, 문학적 독창성·어두운 정서 표현 축에서는 오히려 후퇴 신호(Pangram, 시스템카드의 "creative mastery" 열위)가 있다. 소설가에게는 "초고의 표면 품질↑, 발상·정서 폭↓"로 읽힌다.
- Fable 5.1은 전문 사용자(Every, Automaton, Canva)가 산문 자체를 더 선호하는 경향이 있지만, 그 근거는 블라인드 선호·Elo 등 간접 지표이고 장편 소설 기준 체계적 테스트는 없다.
- 두 모델 모두 "요점을 뒤에 묻는다/장황하다"는 불만이 공통이며, 이는 산문 밀도 조절 지시를 시스템 프롬프트에 넣어야 함을 시사한다.

### Gaps
- Fable 5.1·Mythos 5.1 시스템카드 PDF는 용량 초과로 본문 확보 실패. 창작 글쓰기·무해 요청 거부율 수치 미확인.
- Mazur 벤치마크의 Opus 5.5·Fable 5.1 실제 점수 미확보.
- 소설 전문 도구(Sudowrite, Novelcrafter)의 Opus 5.5·Fable 5.1 장편 산문 평가는 아직 공개되지 않음.

## 핵심 질문 3. 한국어 품질 보고(한국 커뮤니티·기술 언론)

### Takeaway
Opus 5.5·Fable 5.1의 한국어 산문·문체·번역 품질을 직접 평가한 신뢰할 만한 한국어 자료는 찾지 못했다. 확인된 것은 가격·effort 전환 주의 같은 운영 정보와, "문장이 딱딱하다"는 수준의 개인 체감 1건이다.

### Cited Findings
- 한국어 검색(오퍼스 5.5 한국어 글쓰기 / 번역 품질 문체 / 페이블 5.1 소설 후기 / 클리앙 소설 쓰기): 가격·벤치마크·출시 정보가 대부분이며 한국어 글쓰기 품질 평가 자료는 없음. — [검색 결과 요약; 예: aimatters](https://aimatters.co.kr/ai-tool/53101/), [carat.im 가이드](https://carat.im/en/curated/claude-opus-5-5-guide)
- 커뮤니티 체감(meeco.kr): 글쓰기 품질을 기대하며 모델 교체를 고민하는 질문글에, 다른 사용자가 지인 말을 인용해 "문장이 딱딱하다는 점을 제외하면 다른 모델이 낫다"는 취지의 의견. 페이지 본문 직접 확보는 실패(접속 오류), 검색 스니펫 기반. — [meeco.kr](https://meeco.kr/news/42147458)
- 한국 블로그 사용 팁(aimatters): Opus 5.5는 스스로 사고량을 정하므로 '깊이 생각해' 같은 추론 유도 문구를 프롬프트에서 빼라고 권고. — [aimatters.co.kr](https://aimatters.co.kr/ai-tool/53101/)
- GPTers(2026-09-23): "9월 22일에 나왔고, 오푸스 5보다 성능은 올랐는데 가격은 내렸습니다." 고객사 보고: Factory 출력 토큰 20~25% 감소, Box 답변 약 40% 덜 장황. 한국어 문체 평가는 없음. — [GPTers](https://www.gpters.org/news/post/claude-opus-55-vs-aOgt8qu7xSa4sTJ)
- [구버전 자료] 브런치(2026-07-03, Fable 5): "좋은 건 아는데, 비싸잖아요." 비용·한도 중심, 한국어 산문 평가 없음. — [brunch.co.kr/@wybook/2299](https://brunch.co.kr/@wybook/2299)
- Anthropic 공식 문서는 "multilingual capabilities" 지원만 명시하고 한국어 개별 품질 데이터는 없음. Zvi는 시스템카드의 잠재적 사각지대로 "Language-dependent behavior"를 지적. — [Models overview](https://platform.claude.com/docs/en/models/overview); [LessWrong](https://www.lesswrong.com/posts/vMNTWTDWLorDqd3LS/claude-opus-5-5-the-system-card)
- 토크나이저: Opus 4.7부터 도입된 새 토크나이저는 1M 토큰에 약 555k 단어(이전 약 750k)로 토큰 효율이 낮아졌고, Novelcrafter는 "new tokenizer has increased the cost of otherwise identical prompts"라고 지적(영어 기준). — [Models overview](https://platform.claude.com/docs/en/models/overview); [Novelcrafter](https://www.novelcrafter.com/blog/opus-5-for-writers)

### Inferences
- 한국어 문학 산문 품질은 공개 자료로 판단 불가. 사용자가 자기 원고 샘플로 Opus 5.5(effort high/xhigh)와 Fable 5.1을 직접 블라인드 비교하는 것이 유일한 방법이다.
- "문장이 딱딱하다"는 체감은 영어권의 "dense, longer sentences"(Fable 5.1), "buries the point"(Opus 5.5) 보고와 방향이 일치할 가능성이 있다.
- 한국어는 토큰 효율이 영어보다 낮은 편이므로 새 토크나이저의 토큰 증가가 한국어 장편 비용에 더 크게 작용할 수 있다(검증되지 않은 추론).

### Gaps
- 클리앙·디시·네이버 블로그·ZDNet Korea에서 Opus 5.5/Fable 5.1 한국어 창작 품질을 다룬 글을 검색으로 찾지 못함.
- 한국어 토큰 효율의 모델 간 비교 수치 없음.

## 핵심 질문 4. 장문(10k+ 단어) 일관성, 멀티턴 드래프팅, 그리고 글쓰기 관련 약점·가드레일 행동

### Takeaway
10,000단어 이상 산문의 일관성을 측정한 공개 테스트는 Opus 5.5·Fable 5.1 모두 없다. 구조적 한계는 1회 응답 128K 토큰 상한과 claude.ai의 장대화 요약(세부 유실)이며, [구버전] Opus 5에서는 "길어질수록 문체·지시가 드리프트"가 보고됐다. 약점으로는 Opus 5.5의 헤지 급증·장황함·독창성 하락·소설 상투구 증가, Fable 5.1의 밀도 높은 문장·조기 중단·출처 문구 재사용이 확인되고, 거부는 사이버·생물학 분류기 중심이며 소설 어두운 주제에 대한 거부 보고는 현 시점에서 찾지 못했다.

### Cited Findings

**장문·멀티턴**
- 공식: 최대 출력 128K(동기 Messages API), 컨텍스트 1M(≈555k 단어). — [Models overview](https://platform.claude.com/docs/en/models/overview)
- Inkfluence: 1회 응답 128,000토큰 상한, claude.ai는 긴 대화를 요약하며 요약이 작은 세부를 떨어뜨릴 수 있음. 권장 워크플로: 챕터당 1대화 + 아웃라인 + 사실 목록 + 스토리 바이블. — [Inkfluence AI](https://www.inkfluenceai.com/blog/best-claude-model-for-writing-2026)
- Jane Street(Fable 5.1): "remains readable over long, multi-step tasks". Anthropic은 자동 정렬 감사가 "very long-context work and multi-agent settings"에서 가시성이 낮다고 인정. — [Anthropic: Fable 5.1 발표](https://www.anthropic.com/claude-fable-and-mythos-5-1)
- Opus 5.5 시스템카드: "Very long trajectories"가 정렬 테스트의 알려진 약점. — [LessWrong](https://www.lesswrong.com/posts/vMNTWTDWLorDqd3LS/claude-opus-5-5-the-system-card)
- Opus 5.5 멀티턴 특성(공식): 짧은 후속 질문에도 이전 답변을 다시 검토하느라 사고·지연이 늘 수 있음. "Once you have answered something, treat that answer as done..." 지시로 완화 가능하나 이전 오류 자진 지적 가능성 감소. 고effort(xhigh/max)에서는 사고 토큰이 Opus 5보다 많음. — [Prompting Claude Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5)
- Fable 5.1(공식 가이드 요약): `xhigh`/`max`에서 긴 출력을 사고 단계에서 초고로 쓴 뒤 응답에서 다시 쓰는 경향 → 지연·출력 토큰 약 2배. 요청된 작업을 끝내기 전에 멈추고 다음 단계만 설명하거나 허가를 묻는 경우가 있음. — [apidog KR](https://apidog.com/kr/blog/prompting-claude-fable-5-1/)
- [구버전 자료, Opus 5] Novelcrafter: 처음 몇백 단어는 문체·지시가 유지되지만 "the longer the output goes, the more it drifts." 입력 텍스트(인물 설명 등)를 "nearly verbatim" 재등장시키는 반복(한 사례 117단어 뒤). 맞춤 스타일 가이드에도 "bad habits were reappearing". — [Novelcrafter](https://www.novelcrafter.com/blog/opus-5-for-writers)

**글쓰기 약점·AI 티**
- Opus 5.5: 헤지·단서어 97% 증가(Arena), 답변 길이 증가, "still buries the point"(Every), 소설 상투구("said quietly", "for a long moment") 증가와 독창성 하락(Pangram), 시스템카드의 "humor and creative mastery" 열위. em dash는 95% 감소(Arena), 테스트 내 0건(Doser). — [Digg/Arena](https://digg.com/ai/757gj9kn); [Every](https://every.to/vibe-check/vibe-check-opus-5-5-is-pulling-our-codex-converts-back-to-claude); [Pangram](https://www.pangram.com/blog/can-pangram-detect-opus-5-5); [LessWrong](https://www.lesswrong.com/posts/vMNTWTDWLorDqd3LS/claude-opus-5-5-the-system-card)
- Opus 5.5 사용자 과신(Zvi): "Opus 5.5 is too willing to believe the user"; 신중한 프레이밍 하에 "more often willing to play along". 불확실할 때 답을 거부하는 경향 증가(AA-Omniscience 0.56→0.58). — [LessWrong](https://www.lesswrong.com/posts/vMNTWTDWLorDqd3LS/claude-opus-5-5-the-system-card)
- Every: Opus 5의 "personality problem"(수정 요청이 논쟁으로 번짐)은 5.5에서 해소—"They got rid of the annoying personality quirks of Opus 5 without losing any intelligence or stamina."(Mike Taylor) — [Every](https://every.to/vibe-check/vibe-check-opus-5-5-is-pulling-our-codex-converts-back-to-claude)
- Fable 5.1: 더 긴 문장·적은 단락, 'mannered prose', 출처 문구 무표시 재사용, 포맷(볼드/헤더/목록) 감소. — [apidog KR](https://apidog.com/kr/blog/prompting-claude-fable-5-1/); [Inkfluence AI](https://www.inkfluenceai.com/blog/best-claude-model-for-writing-2026)
- [구버전 자료, Opus 5] 은유 과잉("metaphor sandwich"), 깨달음을 "announces realizations rather than letting the reader piece them together", 감정 직접 서술. Novelcrafter는 산문 생성엔 "I will be sticking with Opus 4.6". — [Novelcrafter](https://www.novelcrafter.com/blog/opus-5-for-writers)
- [구버전 자료, Fable 5] 성격: "does not feel as much of a moral scold as the other claude models"(James Moughan), "much less neurotic"(Arthur), 다만 "Paranoid safety controls"(Teortaxes), 조종성 약화 "significant step backward on alignment and steerability"(Matt Parlmer). 아첨: Mazur 아첨 벤치마크 최상위(좋은 방향). "Fable 5 can't stop saying good night"(Wyatt Walls). — [Zvi](https://thezvi.substack.com/p/claude-fable-5-and-mythos-5-capabilities)

**가드레일·거부**
- Opus 5.5 공식: 분류기는 생물학·사이버보안·reasoning extraction. "Everyday health and educational questions are unaffected." 거부는 `stop_reason: "refusal"`과 카테고리로 반환되며 폴백 모델 자동 재시도 가능. 소설·창작 콘텐츠에 대한 별도 언급 없음. — [Prompting Claude Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5)
- Opus 5.5 시스템카드(Zvi): 악의적 요청 거부율 상승, 거부 문제가 있던 평가 일부 삭제. Zvi는 "90%/98%" 균형을 "80%/99.8%"보다 선호한다며 오탐 비용 지적. — [LessWrong](https://www.lesswrong.com/posts/vMNTWTDWLorDqd3LS/claude-opus-5-5-the-system-card)
- Fable 5.1 공식: 사이버 오탐 60% 감소, Claude Code 세션당 사이버 안전장치 개입 약 60% 감소, 생물학 안전장치 무해 질문 85% 덜 발동. 일부 오탐 잔존; 리워딩으로 회피 가능. — [Anthropic 발표](https://www.anthropic.com/claude-fable-and-mythos-5-1); [apidog KR](https://apidog.com/kr/blog/prompting-claude-fable-5-1/)
- [구버전 자료, Fable 5 출시 시점] 오탐 사례: "The word 'cancer' is flagged as a biosecurity risk by Claude Fable 5!"(Derya Unutmaz), "Fable seems to be prone to panicking"(Anders Sandberg), Karpathy "a little too trigger happy for launch". Zvi: "The decision was made to focus on avoiding false negatives, even at the cost of many absurd and embarrassing false positives." Mazur 창작 벤치마크 400개 중 5개 거부. — [Zvi](https://thezvi.substack.com/p/claude-fable-5-and-mythos-5-capabilities)
- Sudowrite는 Fable 5.1이 어두운 주제·폭력·성적 장면에서 "even less likely to balk at legitimate story content"일 것으로 기대(기대이지 측정 아님). — [Sudowrite](https://feedback.sudowrite.com/changelog/new-ai-model-claude-fable-51)
- 레딧(r/WritingWithAI, r/ClaudeAI)에서 Opus 5.5 소설 거부·설교 관련 스레드는 검색으로 찾지 못함. — 검색 결과 없음(2026-11-01)

### Inferences
- 장편 드래프팅은 모델보다 워크플로(챕터 단위, 스토리 바이블, 사실 목록)로 일관성을 확보해야 하며, Opus 5.5의 "이전 답변 재검토" 경향은 멀티턴 드래프팅의 지연 요인이므로 시스템 프롬프트로 제어할 가치가 있다.
- Opus 5.5의 헤지 증가와 희망·가족 주제 편향은 어두운 정서·비극 중심 소설에서 '물러진' 톤으로 나타날 가능성이 있다. Fable 5.1은 이 축에서 상대적으로 "cold-blooded"하다는 Fable 5 시절 평이 이어질 가능성이 있으나 5.1 전용 증거는 없다.
- 창작 소재(의학·범죄·폭력)가 생물학·사이버 분류기와 겹칠 경우 오탐→폴백(Opus 4.8 등)으로 문체가 바뀔 수 있다. 사용자는 폴백 발생 여부를 `stop_details`로 확인하거나 claude.ai에서 응답 품질 급변을 의심해야 한다.

### Gaps
- 10k+ 단어 연속 산문의 인물·플롯·사실 일관성을 측정한 Opus 5.5/Fable 5.1 테스트는 공개된 것이 없음.
- 소설의 어두운 주제(폭력·자살·성적 묘사)에 대한 두 모델의 실제 거부율·설교 빈도 데이터 없음(시스템카드 PDF 미확보, 커뮤니티 스레드 미발견).
- em dash 습관은 Opus 5.5 측정치(급감)만 있고 Fable 5.1 측정치 없음.
