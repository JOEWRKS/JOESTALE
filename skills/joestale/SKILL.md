---
name: joestale
description: 한국어 글을 작가의 어휘로 쓰거나 고칠 때 사용. 완성 문장, 단순 아이디어, 러프한 의견, "이런 글 써줘" 요청 모두 해당. 정도부사·상태형용사를 줄이고 사물·행동·감각으로 장면을 제시하며, 조사 오류·어미 반복·번역투·수식어 비율·인물 대장을 스크립트로 검증한다. 소설·단편·수필·장면 묘사·문장 리라이트에 쓰고, 보고서·코드·번역에는 쓰지 않는다.
---

# JOESTALE — 작가의 어휘로 쓰기

원칙 출처: 허관 작가(@huh_kwan) 「글쓰기팁(어휘)」·「소재를 낚는 5단계」. 원칙·예문·변환 패턴은 [principles.md](references/principles.md). 기본값·임계값·실패 동작·출력 형식은 전부 [decisions.md](references/decisions.md)에 고정돼 있다. **그 표에 있는 것은 묻지 않는다.**

## 1원칙

부사와 형용사를 **줄인다. 없애지 않는다.** 줄어드는 이유는 명사·동사가 구체적이기 때문이어야 한다. 감정·성격·상황을 말하지 말고 그것이 남긴 **사물과 행동**을 보여준다.

## 규칙 요약 (스크립트가 검사, 값은 decisions.md D3)

R1 정도부사 0 · R2 수식어 비율 ≤ 0.18 · R3 "~한 성격이었다"류 0 · R4 감정 직설 0(대화문 예외) · R5 문단당 비시각 감각 ≥ 1 · R6 문단당 숫자·고유명사 또는 명사 3개 · G1 조사 받침 규칙 · G2 마지막 어절 3연속 금지 · G3 설계서 대장과 본문 일치 · T1 번역투·AI 관용구 상한 · T2 문단 첫 어절 3연속 금지 · X1 작가 예문 복제 금지. 허용: 동작부사(꾹, 나란히, 비로소), 수관형사(세, 두, 맨).

## 절차

### 0단계 입력 분류와 소재 낚기

decisions.md D1 규칙으로 A 완성 글 / B 아이디어 / C 의견 / D 써줘 중 하나로 분류한다. 빠진 재료는 D2 기본값으로 채우고 설계서의 가정 표에 적는다.

소재 낚기(B·C·D 필수, A는 원문에 사물이 없을 때): ① 사물 시드 1개(입력 속 구체 명사) ② 사물과 범주·반의 관계가 **없는** 단어 1개 ③ 둘을 잇는 감각 경로 1줄(소리 → 기억, 질감 → 성격) ④ 후보 3개를 D2의 선택 순서로 고른다. 우리말샘 키가 있으면 `scripts/lookup_synonyms.py <사물> --related-check <단어>`로 관계 있음(exit 2)을 배제한다.

### 1단계 장면 설계서

[scene-design.md](references/scene-design.md) 표를 채우고 같은 내용을 [design.template.json](references/design.template.json) 형식으로 `design.json`에 저장한다(위치는 D6). 사물 3·행동 2·비시각 감각 1·숫자 1·원인→결과 1, 인물·장소·숫자 대장, 금지 목표(원래 감정어 → 치환 계획), 가정 표.

### 2단계 초고

설계서의 사물·행동만으로 쓴다. 부사·형용사를 세지 않는다. 작가 예문의 명사구를 그대로 쓰지 않는다.

### 3단계 기계 검증

```bash
PYTHONIOENCODING=utf-8 python skills/joestale/scripts/check_text.py draft.txt --design design.json
```

위반 목록이 나온다. 위반이 있으면 4단계. 띄어쓰기 차이(`spacing_differs`)는 보고만 한다.

### 4단계 국소 리라이트

**위반 문장만** 고친다. 전체 윤문 금지. 형용사 → 그 상태가 남긴 사물, 부사 → 그 방식으로만 가능한 동사, 감정 → 행동과 숫자(principles.md 패턴 6개). 고친 뒤 3단계를 다시 돈다. 최대 3회, 그 뒤에도 남으면 D4대로 멈추고 리포트에 적는다.

### 5단계 독립 검수와 제출

[reviewer-prompt.md](references/reviewer-prompt.md)의 블록을 서브에이전트에게 본문·설계서만 넣어 준다. 지적은 4단계로 돌린다. 서브에이전트가 불가하면 같은 맥락에서 하고 `검수: DEGRADED`로 표기한다.

제출은 decisions.md D5 형식 고정: 본문 → 설계서 → 검증 리포트(초고/최종 수치, 남은 위반, 검수 결과).

## 하지 말 것

- 부사·형용사를 0으로 만들려고 문장을 비틀지 않는다.
- Kiwi 오타 교정 모드를 켜지 않는다. 띄어쓰기 자동 수정을 하지 않는다.
- 현대 작가의 문체를 흉내 내지 않는다. 원칙만 따른다.
- D7의 두 경우 외에는 사용자에게 묻지 않는다.

## 파일

| 파일 | 역할 |
|---|---|
| references/decisions.md | 기본값·임계값·실패 동작·출력 형식·파일 위치 |
| references/principles.md | 작가 원칙, 예문 4쌍, 변환 패턴 6개, 소재 낚기 5단계 |
| references/scene-design.md, design.template.json | 설계서 질문지와 JSON 형식 |
| references/lexicon.json | 정도부사·허용 부사·감정어·상태 패턴·번역투·감각 어휘장(6감각 각 36~50개) |
| references/cliche-list.md | 목록 해설과 검수 체크리스트 |
| references/reviewer-prompt.md | 5단계 검수 프롬프트와 처리 규칙 |
| scripts/check_text.py | 3단계 검증기 (`--lexicon-stats`로 어휘장 집계) |
| scripts/test_check_text.py | 검증기 회귀 테스트 |
| scripts/lookup_synonyms.py | 우리말샘 유의어·관계어 조회 (OPENDICT_KEY 필요) |
| examples/before-after.md | 작가 예문 재현 수치 |
