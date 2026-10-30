# JOESTALE — 작가의 어휘로 쓰는 한국어 작문 스킬

JOESTALE은 Claude Code용 한국어 작문 스킬이다. 완성 문장, 단순 아이디어, 러프한 의견, "이런 글 써줘" 요청을 받아 **정도부사·상태형용사를 줄이고 사물·행동·감각으로 장면을 보여주는** 글을 쓰고, 조사 오류·어미 반복·번역투·수식어 비율·인물 대장 불일치를 스크립트로 검증한다.

원칙의 출처는 허관 작가(@huh_kwan)의 Threads 글 「글쓰기팁(어휘)」·「소재를 낚는 5단계」이며, 원칙과 예문만 출처를 밝혀 인용한다. 문체 복제는 하지 않는다.

## 구성

| 경로 | 내용 |
|---|---|
| `skills/joestale/SKILL.md` | 스킬 본문: 1원칙, 규칙 12개, 절차 0~5단계 |
| `skills/joestale/references/decisions.md` | 입력 분류·기본값·임계값·실패 동작·출력 형식 (회색지대 없음) |
| `skills/joestale/references/lexicon.json` | 정도부사·감정어·번역투·감각 어휘장(6감각 36~50개)·사물 시드 |
| `skills/joestale/scripts/check_text.py` | 3단계 기계 검증기 (kiwipiepy) |
| `skills/joestale/scripts/lookup_synonyms.py` | 우리말샘 오픈 API 관계어 조회 (`OPENDICT_KEY` 환경변수) |
| `skills/joestale/examples/` | 작가 예문 재현 수치, A·B·C 유형 실전 예 |
| `joestale-work/live-test-D/` | 새 세션 실전 테스트(D 유형 단편) 산출물 |
| `기획서.md`, `Library/` | 기획·조사 기록 |
| `ROADMAP.md`, `TASK.md`, `ISSUES.md` | JOENESS 관리 문서 |

## 사용

```bash
pip install kiwipiepy
PYTHONIOENCODING=utf-8 python skills/joestale/scripts/check_text.py <본문.txt> --design <설계서.json> --length 400-700
```

Claude Code에서는 이 저장소 폴더를 열면 `.claude/skills/joestale`로 로드된다. 다른 프로젝트에서 쓰려면 `skills/joestale/scripts/install.ps1 -Apply`.

## 데이터 출처

- 우리말샘(국립국어원) 오픈 API — 텍스트 CC BY-SA 2.0 KR. 뜻풀이·관계어만 사용, 문학 용례는 사용하지 않음.
- 측정은 kiwipiepy 0.24 품사 태그 기준.

## 상태

Phase 0·1·1.5 완료(2026-10-30). Phase 2(사전 API 연결)는 인증키 대기, Phase 3(저작권 만료 작가 코퍼스로 임계값 보정) 준비 중. 자세한 진행은 `ROADMAP.md`.
