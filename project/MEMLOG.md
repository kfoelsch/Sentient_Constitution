# MEMLOG

## Purpose

Session memory log for current project context, decisions, and next actions. Keep this file lean; archive completed detail rather than carrying full session history forward.

## Current State

**2026-10-21 — Merged implementation batches:** Chapter Seven §4 / CF-5.9 work merged in [PR #107](https://github.com/kfoelsch/Sentient_Constitution/pull/107), chapter-numbering migration in [PR #108](https://github.com/kfoelsch/Sentient_Constitution/pull/108), and translation updates plus pre-announcement resync tooling in [PR #109](https://github.com/kfoelsch/Sentient_Constitution/pull/109). Completed details are in [TODO_RESOLVED_2026-10-21.md](../archive/TODO_RESOLVED_2026-10-21.md). The translation audit still reports missing and stale definition-index entries and stale source snapshots; it is backlog, not translation certification.

**2026-10-20 — Announcement review batches:** B04 reviewed CJS-2, CJS-1.9–1.11, and CI-9 (542 source lines); 72 files remain in the larger review inventory. D04 on hybrid scope and exception boundaries was approved and applied; independent re-review is not claimed. Review record: [announcement_interlocks_B04_2026-10-20.md](reviews/announcement_interlocks_B04_2026-10-20.md). The completed B02/B03 desk walkthrough is archived in [TODO_RESOLVED_2026-10-21.md](../archive/TODO_RESOLVED_2026-10-21.md); fresh-session execution of the [case packet](trials/agent_cooperative_2026-10-20/CASE_PACKET.md) and separate human-operator evidence remain pending.

**2026-10-20 — Announcement plan:** [Working plan](plans/announcement_readiness_2026-10-20.md) and [523-path non-core review inventory](plans/announcement_review_inventory_2026-10-20.md) govern work through December 31. Core wording stays with the steward; Codex handles non-core passes and focused decision questions. Seventy-five implementation-family files still need whole-file review, and affected portions must reopen when governing core changes. No release or adoption decision has been made.

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
