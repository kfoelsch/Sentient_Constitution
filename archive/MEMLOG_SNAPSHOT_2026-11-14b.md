# MEMLOG

Keep this file to standing decisions and current context. Completed session detail remains in dated archives; open actions are tracked in [TODO.md](../TODO.md). The pre-cleanup state is preserved in [MEMLOG_SNAPSHOT_2026-11-02.md](../archive/MEMLOG_SNAPSHOT_2026-11-02.md).

## Purpose

Session memory log for current project context, decisions, and next actions. Keep this file lean; archive completed detail rather than carrying full session history forward.

## Current State

**Announcement readiness:** The [working plan](plans/announcement_readiness_2026-10-20.md) and [non-core review inventory](plans/announcement_review_inventory_2026-10-20.md) govern work through December 31. Core wording stays with the steward; Codex handles non-core passes and focused decision questions. The inventory records remaining review batches and affected portions must reopen when governing core changes. No release or adoption decision has been made. Completed implementation batches, B04/D04, and the B02/B03 walkthrough are recorded in [MEMLOG_RESOLVED_2026-10-23.md](../archive/MEMLOG_RESOLVED_2026-10-23.md) and prior dated archives.

Earlier completed session detail is preserved in [MEMLOG_SNAPSHOT_2026-10-21.md](../archive/MEMLOG_SNAPSHOT_2026-10-21.md) and the dated snapshots indexed below. Open actions remain in [TODO.md](../TODO.md).

## Standing Decisions

**Constitutional Constraints bind globally (steward decision, 2026-10-14):** every system, institution, and other body is bound at every class and in every context, including Class P and sandboxed scope. Class scales the intensity, form, and machinery that carry a constraint, never whether it applies.

**Burden of proof falls to the claimant (steward decision, 2026-10-14):** a body claiming to be below a line shows it with a short written statement; a challenger names a specific crossing in a named domain, and the body then shows it is below that line (Chapter Four §1).

**Time windows (custodian decisions, 2026-10-17 and 2026-10-18):** restricted evidence never slows the clock and is never a ground for a slower column or a longer window; a "reasonable" period is 14 days; "promptly" is not a length, and review of a measure in force, intake, and notice name their windows instead; record duties follow Document at Action (Chapter One §16.4), a design default and not a window; window names live in CJS-0.4 and the numbers stay with their owners (Chapter Thirteen §6, CF-11.3.1); no Chapter Five definitions for window names or for the new principle unless a core rule needs to cite them.

**The word "instrument" is not used (custodian decision, 2026-10-19):** name the thing (System Charter, Institutional Charter, rule set, record, act), or write "document" or "text"; for the Constitution itself, "this Constitution". The audit rule `avoid-instrument` enforces it on live files; dated records and translations keep their wording.

**Chapter Nine order (editor decision, 2026-10-07):** Chapter Nine sections follow the order the certification work is done. New sections go in the phase where the work happens, not at the end of a file. Renumbered before the announcement so no redirect anchors are needed later.

**Go-live gate (editor decision, 2026-10-08):** No system goes live, pilot or full, before it is certified. A pilot is certified on its own record, scaled by class and substitutability. Systems already operating at an adopter's effective date are excepted only for the Article XXVIII-A transition clock. The published record challenge path opens when the outcome is published, or is already open for a system already operating.

**Translation scheduling (steward planning decision, 2026-10-20):** Prepare translations chapter by chapter once the steward identifies settled English text and its revision, followed by a final synchronization and fidelity review. Do not treat any chapter as settled without that identification. The [announcement plan](plans/announcement_readiness_2026-10-20.md) tracks readiness. Historical pause details and known gaps are in [MEMLOG_SNAPSHOT_2026-10-20.md](../archive/MEMLOG_SNAPSHOT_2026-10-20.md); PR #109's updates did not certify translations.

**Pages build:** `_pages_site/` is a local preview only; CI rebuilds it on each deploy. `make pages-deploy-gate` runs in `pages.yml` before every build; `.github/workflows/checks.yml` runs `make regression` on every push and PR. Do not list "Regenerated `_pages_site`" in editing passes. **Open:** switch **Settings → Pages → Source** to *GitHub Actions* before the announcement.

**Reader entry pages:** **README** is the one public door for all readers (timed reading paths at `README.md#reading-paths`); **START_HERE** is the start page for would-be adopters and operators; [guides/CONCEPTUAL_OVERVIEW.md](../guides/CONCEPTUAL_OVERVIEW.md) is the second-step big-picture map.

**Link rules:** Binding corpus links only by relative path or `#fragment` (LINK-OFF-CORPUS-15, `make external-link-audit`) and never deep-links into a README section (SUPPORT-DOC-POINTER-01). A pasted `https://file+.vscode-resource.vscode-cdn.net/…` link is the VS Code Markdown preview rewriting a correct relative link, not corpus text.

**Scenarios catalog:** `tools/architecture/regression_scenarios.json` is the source of truth for [CONSTITUTIONAL_REGRESSION_SCENARIOS.md](../CONSTITUTIONAL_REGRESSION_SCENARIOS.md). Edit the catalog, then run `python3 tools/emit_regression_scenarios.py`; `make regression` runs `--check` and fails on drift. If you edit the markdown by hand, port the change to the catalog or the next run will undo it.

## Active Threads

**Evaluation:** I1 human evidence remains open in [TODO.md](../TODO.md); earlier resolved evaluation items are in [TODO_RESOLVED_2026-09-17.md](../archive/TODO_RESOLVED_2026-09-17.md).

**Regression scenarios:** active validation and dated evidence publication remain deferred unless reinstatement is requested. The open P1 validation is in [TODO.md](../TODO.md).

**Architecture process:** [doc_architecture.md](../doc_architecture.md) remains the stable ownership and editing map. Optional AI corpus follow-ups remain in [plans/ai_corpus_optimization_plan.md](plans/ai_corpus_optimization_plan.md).

## Archive Index

- **2026-11-14 archive run:** [archive/MEMLOG_SNAPSHOT_2026-11-14.md](../archive/MEMLOG_SNAPSHOT_2026-11-14.md) (pre-cleanup; no MEMLOG entry was complete, so none moved), [archive/TODO_SNAPSHOT_2026-11-14.md](../archive/TODO_SNAPSHOT_2026-11-14.md) (no TODO item was complete), [archive/DOC_ARCHITECTURE_MOVES_488-497_ARCHIVED_2026-11-14.md](../archive/DOC_ARCHITECTURE_MOVES_488-497_ARCHIVED_2026-11-14.md) (moves 488–497)
- **2026-11-12 archive run:** [archive/MEMLOG_SNAPSHOT_2026-11-12.md](../archive/MEMLOG_SNAPSHOT_2026-11-12.md) (pre-cleanup; no MEMLOG entry was complete, so none moved), [archive/TODO_SNAPSHOT_2026-11-12.md](../archive/TODO_SNAPSHOT_2026-11-12.md) (no TODO item was complete), [archive/DOC_ARCHITECTURE_MOVES_466-487_ARCHIVED_2026-11-12.md](../archive/DOC_ARCHITECTURE_MOVES_466-487_ARCHIVED_2026-11-12.md); two open decisions were carried into `TODO.md` (Chapter Fourteen Part B catch-all coverage and the "Chapters Two through Four" wording).
- **2026-11-11 archive run:** [archive/MEMLOG_SNAPSHOT_2026-11-11.md](../archive/MEMLOG_SNAPSHOT_2026-11-11.md) (pre-cleanup; no MEMLOG entry was complete, so none moved), [archive/TODO_SNAPSHOT_2026-11-11.md](../archive/TODO_SNAPSHOT_2026-11-11.md) (no TODO item was complete), [archive/DOC_ARCHITECTURE_MOVES_370-465_ARCHIVED_2026-11-11.md](../archive/DOC_ARCHITECTURE_MOVES_370-465_ARCHIVED_2026-11-11.md); five open items from the archived move log were carried into TODO.md
- **2026-11-08 archive run:** [archive/MEMLOG_SNAPSHOT_2026-11-08.md](../archive/MEMLOG_SNAPSHOT_2026-11-08.md) (pre-cleanup; no MEMLOG entry was complete, so none moved), [archive/TODO_RESOLVED_2026-11-08.md](../archive/TODO_RESOLVED_2026-11-08.md), [archive/DOC_ARCHITECTURE_MOVES_244-369_ARCHIVED_2026-11-08.md](../archive/DOC_ARCHITECTURE_MOVES_244-369_ARCHIVED_2026-11-08.md)
- **2026-11-02 pre-cleanup snapshot:** [archive/MEMLOG_SNAPSHOT_2026-11-02.md](../archive/MEMLOG_SNAPSHOT_2026-11-02.md)
- **2026-11-03 completed translation instruction:** [archive/MEMLOG_RESOLVED_2026-11-03_TRANSLATIONS.md](../archive/MEMLOG_RESOLVED_2026-11-03_TRANSLATIONS.md)
- **2026-11-01 applied drafts:** [archive/LOBBYING_BOUNDARIES_DRAFT_APPLIED_2026-11-01.md](../archive/LOBBYING_BOUNDARIES_DRAFT_APPLIED_2026-11-01.md) (now Article XII-E), [archive/RECORD_INTEGRITY_PRINCIPLE_DRAFT_APPLIED_2026-11-01.md](../archive/RECORD_INTEGRITY_PRINCIPLE_DRAFT_APPLIED_2026-11-01.md) (now Record Integrity, Chapter Five), [archive/PRINCIPLE_TERM_ALIGNMENT_ANALYSIS_APPLIED_2026-11-01.md](../archive/PRINCIPLE_TERM_ALIGNMENT_ANALYSIS_APPLIED_2026-11-01.md), [archive/RECORD_OVERVIEW_PLAN_APPLIED_2026-11-01.md](../archive/RECORD_OVERVIEW_PLAN_APPLIED_2026-11-01.md) (now `guides/RECORD_OVERVIEW.md`)
- **2026-11-01 superseded draft:** [archive/ARTICLE_VIII_PLAIN_LANGUAGE_DRAFT_ARCHIVED_2026-11-01.md](../archive/ARTICLE_VIII_PLAIN_LANGUAGE_DRAFT_ARCHIVED_2026-11-01.md) (the Article's own *In plain terms* lines and the generated plain-terms edition cover it)
- **2026-10-23 resolved work:** [archive/MEMLOG_RESOLVED_2026-10-23.md](../archive/MEMLOG_RESOLVED_2026-10-23.md)

- **2026-10-21 completed work:** [archive/TODO_RESOLVED_2026-10-21.md](../archive/TODO_RESOLVED_2026-10-21.md)
- **2026-10-21 MEMLOG snapshot:** [archive/MEMLOG_SNAPSHOT_2026-10-21.md](../archive/MEMLOG_SNAPSHOT_2026-10-21.md)
- **2026-10-20 prune:** [archive/MEMLOG_SNAPSHOT_2026-10-20.md](../archive/MEMLOG_SNAPSHOT_2026-10-20.md)
- **2026-10-19 prune:** [archive/MEMLOG_SNAPSHOT_2026-10-19.md](../archive/MEMLOG_SNAPSHOT_2026-10-19.md)
- **2026-10-18 prune:** [archive/MEMLOG_SNAPSHOT_2026-10-18.md](../archive/MEMLOG_SNAPSHOT_2026-10-18.md)
- **2026-10-14 prune:** [archive/MEMLOG_SNAPSHOT_2026-10-14.md](../archive/MEMLOG_SNAPSHOT_2026-10-14.md)
- **2026-10-13 prune:** [archive/MEMLOG_SNAPSHOT_2026-10-13.md](../archive/MEMLOG_SNAPSHOT_2026-10-13.md)
- **2026-10-03 prune:** [archive/MEMLOG_SNAPSHOT_2026-10-03.md](../archive/MEMLOG_SNAPSHOT_2026-10-03.md)
- **2026-09-27 prune:** [archive/MEMLOG_SNAPSHOT_2026-09-27.md](../archive/MEMLOG_SNAPSHOT_2026-09-27.md)
- **Architecture process (canonical):** [archive/ARCHITECTURE_PRIMER_ARCHIVED_2026-05-08.md](../archive/ARCHITECTURE_PRIMER_ARCHIVED_2026-05-08.md), [archive/ARCHITECTURE_ADOPTION_APPENDIX_ARCHIVED_2026-05-08.md](../archive/ARCHITECTURE_ADOPTION_APPENDIX_ARCHIVED_2026-05-08.md), [archive/ARCHITECTURE_WORKLIST_ARCHIVED_2026-05-08.md](../archive/ARCHITECTURE_WORKLIST_ARCHIVED_2026-05-08.md) — see [README.md](../README.md)
- **2026-06-18 Chapter Five closeout:** [archive/MEMLOG_SNAPSHOT_2026-06-18.md](../archive/MEMLOG_SNAPSHOT_2026-06-18.md), [archive/TODO_SNAPSHOT_2026-06-18.md](../archive/TODO_SNAPSHOT_2026-06-18.md)
- **2026-05-01 root retirement:** [archive/MEMLOG_ROOT_RETIRED_2026-05-01.md](../archive/MEMLOG_ROOT_RETIRED_2026-05-01.md), [archive/TODO_ROOT_RETIRED_2026-05-01.md](../archive/TODO_ROOT_RETIRED_2026-05-01.md)
- Older snapshots removed 2026-06-17 can be retrieved from Git history.

## Operating Rule

Add new session entries above the archive index only when they carry forward current context, decisions, verification status, or next actions. For detailed closure narratives, create a dated archive snapshot and leave a pointer here.

Standard closeout order: commit substantive corpus/source changes first; then snapshot active meta files (`TODO.md`, `MEMLOG.md`, and living worklists) into `archive/`; then slim the active meta files to pointers and current open work.

**Archive (standard procedure, custodian decision, 2026-11-08):** when the custodian says "archive", move every completed entry out of `project/MEMLOG.md`, `TODO.md`, and `doc_architecture.md`, as follows. (1) Work on a branch from `main`. (2) Snapshot the pre-cleanup `TODO.md` and `project/MEMLOG.md` as `archive/TODO_SNAPSHOT_<date>.md` and `archive/MEMLOG_SNAPSHOT_<date>.md`. (3) `TODO.md`: move sections and checked items with no open work to `archive/TODO_RESOLVED_<date>.md`. (4) `project/MEMLOG.md`: move completed session detail to `archive/MEMLOG_RESOLVED_<date>.md`; standing decisions and open threads stay. (5) `doc_architecture.md`: move the dated move-log entries that are complete and merged to `archive/DOC_ARCHITECTURE_MOVES_<first>-<last>_ARCHIVED_<date>.md`, leave a pointer, and keep the `**Next file:**` footer at the end. (6) Before moving anything, read each candidate for "not done", "open", or "pending" language and carry any genuinely open item into `TODO.md`. (7) Add pointers in the Archives lists and log the run as the next move in `doc_architecture.md`. (8) Run `make preflight` and `make audit-report`, and check `git status` for evidence-file deletions that `audit-report` makes. Nothing is deleted without being archived first, and no rule or decision changes.

**Merge (standard procedure, custodian decision, 2026-11-09):** when the custodian says "merge", that is the request to commit, push, and merge on git in one run; it is the ask that [AGENTS.md](../AGENTS.md) and GIT-PUSH-CL-01 require before a session pushes or merges. (1) Commit the current work on a branch named for it, cut from current `main` (GIT-BRANCH-NAME-01); if the work sits on another branch, say so and use that branch only when it is the custodian's. Stage only the files the work changed plus its generated files; leave untracked scratch (`.vscode/`, `_to_delete/`, dated `evidence/` folders, translation drafts) out. (2) Before committing, make sure the move-log entry exists and run `make preflight` and `make corpus-markdown-audit`; run `make audit-report` for larger changes. Watch `git status` for evidence deletions that `audit-report` makes, and do not restore them with `git checkout -- evidence`. (3) End the commit message with the attribution lines the session was given. (4) Push from the Claude Code workspace by the route in AGENTS.md (*Pushing and merging from a Claude Code session*): bundle on the device, `device_stage_files`, fetch the bundle into the clone, `git push -u origin <branch>`. (5) Open the pull request with `gh api` (GraphQL is blocked) and an accurate body. (6) Wait for the `regression` check and compare any failing target with `main`; merge with a merge commit (`merge_method=merge`) only when the pull request adds no failing target that `main` lacks. If the check fails, stop and report; never force-push. (7) Sync the custodian's checkout (`python3 tools/sync_local.py`, or `git merge --ff-only origin/main` when it declines only because of leftover evidence deletions that the merge itself removes). (8) Report the commit, the pull request number and link, the merge commit, and the move number.
