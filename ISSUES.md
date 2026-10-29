# Open problems and workarounds

Active issues: I-1, I-2, I-4. (I-3 closed 2026-10-29)

## I-1 / 우리말샘 오픈 API 약관·호출 제한 미확인

Status: open.
Affected roadmap item: ROADMAP.md P2-1.
Cause: API 안내 페이지에 라이선스 본문·호출 제한이 없고 별도 약관 페이지를 아직 읽지 않음.
Workaround: none. Phase 2 착수 전 확인.
Residual risk: 상업·재배포 조건에 따라 로컬 사전 덤프로 대체해야 할 수 있음.
Closure condition: 약관·저작권 정책 확인 결과를 Library/research.md에 기록하고 인증키 발급.
Verification: missing.
Next action: 사용자가 opendict.korean.go.kr에서 키 신청, 약관 요지 확인.

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
