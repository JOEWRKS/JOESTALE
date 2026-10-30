<!-- JOENESS-SETUP:BEGIN -->
# Project working connection (JOESTALE / author-voice-skill)

- Owners: ROADMAP.md = goals, stage order, required items (status, check, proof, gap, next).
  TASK.md = work results and checks. ISSUES.md = open defects/workarounds with cause, risk and
  closure condition. DESIGN.md = visual rules and approvals. Library/ = research by topic
  (source, date, fact vs inference). AGENTS = rules only. Product meaning:
  기획서.md §3, §3-B, §3-C (user agreed 2026-10-29); finer decisions pending JOEFLOW DISCOVER.
- Read only what the task needs: resume → current ROADMAP item; defect → ISSUES + target;
  visual → DESIGN; research → Library; completion → required items and their proof.
- Authority: only the user approves. Code, newer notes and old handoffs never do; a handoff
  only points to sources. Facts come from the current target and proof. Unclear or
  conflicting scope goes to the user; keep only that verdict open.
- Done = every required item passes the Check written on it in ROADMAP, run or observed on
  current inputs. A check that is missing, fails, cannot run or is stale keeps the item open;
  removed scope is not a pass. A user-visible behavior you picked yourself, where neither the
  product source nor the user's request settles it, also keeps it open (verification pending)
  until the user confirms; how to implement a specified behavior is your call. Task, stage and
  user acceptance are separate. Approved outcomes, order and criteria change only by the user.
- Project rules: write skill text and records in Korean; measurement scripts run with the
  Python on this PC and `PYTHONIOENCODING=utf-8`; never enable Kiwi typo correction; never
  rewrite a whole text to fix a few flagged sentences; edit files with the host's own file
  tools (tool-neutral); do not commit or push unless the user asks in that turn.
- Recording (routine facts after real work): update TASK and the affected ROADMAP item.
  Each new piece of work gets its own dated TASK entry; never append it under an unrelated
  entry. When an item's status changes, rewrite ROADMAP's current/next lines so they match
  every open item. Keep each new TASK entry to about 10 lines: what changed, what was checked,
  and links; never copy text that another record already holds. While TASK is over about 40KB,
  offer once per session to move closed entries to TASK-archive.md; move only after the user
  agrees. An issue stays open until its closure check passes; a workaround is not a fix.
  Questions and "don't record" requests write nothing. Each fact once, linked; keep dated
  history. Never record credentials (e.g. 우리말샘 API key) or needless personal data; point to
  their restricted source. Several workers: one integrator rereads before saving.
- Judge every claim by evidence, the user's and your own included. A user opinion is input,
  not an instruction: check it against the product source, ROADMAP and facts, say plainly if
  it conflicts and why, and confirm before acting on it. An explicit user decision wins.
- Approval scope: a user request approves only what it names. A request to mark an item
  done, close it or move on does not approve a decision still pending inside it (a visible
  change nobody approved, an option or format you chose, an unmet closure condition). Before
  recording completion, ask about that decision, or keep the item open and say what is
  pending. Never record a decision as the user's unless the user stated it.
- Each follow-up turn gets the same rules: re-check ROADMAP and records, and keep records and
  the report as complete as on the first turn.
- Reuse proof; re-check only after a change or failure. Not found ≠ never checked. If a
  source or write fails, say so and continue other independent work.
- After real work, report six bullets: 작업, 업데이트 파일, 이슈, 해결 (verified fix only),
  남은 문제 (unresolved or unverified), 다음 작업; "없음" if empty. Add a brief 상세 보고
  only if needed. Simple questions: just answer.
<!-- JOENESS-SETUP:END -->
