# MEMLOG

## Purpose

Session memory log for current project context, decisions, and next actions. Keep this file lean; archive detail snapshots rather than carrying full session history forward.

## Current State

**2026-10-20 — Standing-record seats and custody (uncommitted, on branch `docs/ownership-statements-sweep`, which also holds the committed, unmerged ownership-statement sweep and CS-5 / CS-13 split, sixty-sixth and sixty-seventh moves):** Chapter Seven §4 restructured into §4.1 What the seats are, §4.2 What makes a placement valid (with the Material Control Line and Independence bullets), §4.3 What a System Charter or Institutional Charter owes the map (missing map, dead pointer, out-of-date map), §4.4 to §4.7 (§4.5 is now *Changing seat rules and seat holders*; §4.6 splits into §4.6.1 and §4.6.2). New **CF-5.9 Backup Record Custodian** (custody twin of CF-5.7), eligible-custodian list and tests in CI-3.6.3 field 10, Chapter Ten §3.7 fallbacks, and Chapter Five entries *Record-Opening Authority* and *Record Custodian*. Sixty-eighth and sixty-ninth moves in [doc_architecture.md](../doc_architecture.md). Custodian decisions: Institutional family keeps both backup bodies with separate staff; eligible list is open and the tests decide; reciprocal hosting is banned outright; the pre-announcement corpus is a sandbox, so core additions go in now. The steward signed off the wording on 2026-10-20 (archived in [archive/TODO_RESOLVED_2026-10-20.md](../archive/TODO_RESOLVED_2026-10-20.md)), adding a notice and contest path for holder changes in Chapter Seven §4.5. Chapter Seventeen §1 heightened review is open; follow-ups are in [TODO.md](../TODO.md).

**2026-10-18 to 2026-10-19 (merged into `origin/main`):** the CI-13 split into CI-13 (*Institutional failure and dissolution*, CI-13.1 to CI-13.4) and CI-28 (*Institutional accountability and sanctions*, CI-28.1 to CI-28.6); time windows and Document at Action (Chapter One §16.4); the CS-4 rewrite; Chapter Seven §1.3 to §1.7, §2.1 to §2.4, §3.1 to §3.5 and §4.1 to §4.7; the Dissolution Reformation Lock (Chapter Eleven §5.5); the TIME-REF-01 registry audit (shrink-only baseline, 78 entries); and the ban on the word "instrument" (Chapter Seventeen §10.2 is now **Adoption Document**). Full entries are in [archive/MEMLOG_SNAPSHOT_2026-10-20.md](../archive/MEMLOG_SNAPSHOT_2026-10-20.md); the time-window decisions are under Standing Decisions below. The open follow-ups (Chapter Seventeen §1 heightened review, the operative sign-off of CI-13 and CI-28, the Adoption Document name, translations) are in [TODO.md](../TODO.md).

**2026-10-14 to 2026-10-17 (merged earlier):** Domain-Specific Materiality is the one nine-question test for a material act and for Class L (Class P split into a private unit and ordinary community activity); Chapter Seven follows the order of its one chart; CI-13.1 to CI-13.10 give the consequence ladder (directed correction to dissolution, contraction to below Class L, Systems counterpart); Charter Pointer is a defined term; Backup Record Authority (CF-5.7) and operator and stakeholder standing records; verifiers outside the operator (Chapter Nine Part B §6.1.1, Part D §13.1). Full entries are in [archive/MEMLOG_SNAPSHOT_2026-10-18.md](../archive/MEMLOG_SNAPSHOT_2026-10-18.md).

Earlier session narratives (2026-06-15 through 2026-09-27: Chapter Six restructures, Articles X and XI restructure, institutional secularism move, Hard Content term, plain-language backlog, link and archive cleanups, Pages build, reader entry pages, new Chapter Five terms, segregation of duties, seat catalog, evaluation follow-ups) are in [archive/MEMLOG_SNAPSHOT_2026-09-27.md](../archive/MEMLOG_SNAPSHOT_2026-09-27.md) and [archive/MEMLOG_SNAPSHOT_2026-10-03.md](../archive/MEMLOG_SNAPSHOT_2026-10-03.md); the 2026-10-01 to 2026-10-13 entries (Chapter One reorganization; Chapter Nine reorder, go-live gate, certification-status rename, process alignment and cause finding; sibling audit modes; influence-contact rules and the pilot section; Chapter Seven, the Charter Role Map and the Charter rename; Chapter Nine Part D and the formation check) are in [archive/MEMLOG_SNAPSHOT_2026-10-13.md](../archive/MEMLOG_SNAPSHOT_2026-10-13.md). The steward signed off the wording in those entries on 2026-10-13. The 2026-10-14 to 2026-10-17 entries (Domain-Specific Materiality and Class P, Chapter Seven order, the dissolution procedure, Charter Pointer and review cadence, standing records) are in [archive/MEMLOG_SNAPSHOT_2026-10-18.md](../archive/MEMLOG_SNAPSHOT_2026-10-18.md).

## Standing Decisions

**Constitutional Constraints bind globally (steward decision, 2026-10-14):** every system, institution, and other body is bound at every class and in every context, including Class P and sandboxed scope. Class scales the intensity, form, and machinery that carry a constraint, never whether it applies.

**Burden of proof falls to the claimant (steward decision, 2026-10-14):** a body claiming to be below a line shows it with a short written statement; a challenger names a specific crossing in a named domain, and the body then shows it is below that line (Chapter Four §1).

**Time windows (custodian decisions, 2026-10-17 and 2026-10-18):** restricted evidence never slows the clock and is never a ground for a slower column or a longer window; a "reasonable" period is 14 days; "promptly" is not a length, and review of a measure in force, intake, and notice name their windows instead; record duties follow Document at Action (Chapter One §16.4), a design default and not a window; window names live in CJS-0.4 and the numbers stay with their owners (Chapter Thirteen §6, CF-11.3.1); no Chapter Five definitions for window names or for the new principle unless a core rule needs to cite them.

**The word "instrument" is not used (custodian decision, 2026-10-19):** name the thing (System Charter, Institutional Charter, rule set, record, act), or write "document" or "text"; for the Constitution itself, "this Constitution". The audit rule `avoid-instrument` enforces it on live files; dated records and translations keep their wording.

**Chapter Nine order (editor decision, 2026-10-07):** Chapter Nine sections follow the order the certification work is done. New sections go in the phase where the work happens, not at the end of a file. Renumbered before the announcement so no redirect anchors are needed later.

**Go-live gate (editor decision, 2026-10-08):** No system goes live, pilot or full, before it is certified. A pilot is certified on its own record, scaled by class and substitutability. Systems already operating at an adopter's effective date are excepted only for the Article XXVIII-A transition clock. The published record challenge path opens when the outcome is published, or is already open for a system already operating.

**Translations paused (editor decision, 2026-09-23):** Translations under [translations/](../translations/) may fall out of date while the English edit pass continues; do not resync after each English change. The English numbered `core_*` files govern. At the restart, resync fully against the English source. Known gaps: translated files still use pre-renumbering chapter filenames (e.g. `translations/es/core_07_system_alignment_certification.md` holds Chapter Nine), which accounts for nearly all remaining broken links in the repo; translated text still uses the published-edition article labels (only links into English files were re-anchored). Chapter Six has been renumbered several times since; the old → new label mapping is in the 2026-09-25 through 2026-09-27 entries of [archive/MEMLOG_SNAPSHOT_2026-09-27.md](../archive/MEMLOG_SNAPSHOT_2026-09-27.md). Translation lane: [CONTRIBUTING.md](../CONTRIBUTING.md#lane-f).

**Pages build:** `_pages_site/` is a local preview only; CI rebuilds it on each deploy. `make pages-deploy-gate` runs in `pages.yml` before every build; `.github/workflows/checks.yml` runs `make regression` on every push and PR. Do not list "Regenerated `_pages_site`" in editing passes. **Open:** switch **Settings → Pages → Source** to *GitHub Actions* before the announcement.

**Reader entry pages:** **README** is the one public door for all readers (timed reading paths at `README.md#reading-paths`); **START_HERE** is the start page for would-be adopters and operators; [guides/CONCEPTUAL_OVERVIEW.md](../guides/CONCEPTUAL_OVERVIEW.md) is the second-step big-picture map.

**Link rules:** Binding corpus links only by relative path or `#fragment` (LINK-OFF-CORPUS-15, `make external-link-audit`) and never deep-links into a README section (SUPPORT-DOC-POINTER-01). A pasted `https://file+.vscode-resource.vscode-cdn.net/…` link is the VS Code Markdown preview rewriting a correct relative link, not corpus text.

**Scenarios catalog:** `tools/architecture/regression_scenarios.json` is the source of truth for [CONSTITUTIONAL_REGRESSION_SCENARIOS.md](CONSTITUTIONAL_REGRESSION_SCENARIOS.md). Edit the catalog, then run `python3 tools/emit_regression_scenarios.py`; `make regression` runs `--check` and fails on drift. If you edit the markdown by hand, port the change to the catalog or the next run will undo it.

## Active Threads

**Evaluation:** I1 (human evidence) remains open in [TODO.md](../TODO.md); resolved follow-ups are in [archive/TODO_RESOLVED_2026-09-17.md](../archive/TODO_RESOLVED_2026-09-17.md).

**Regression scenarios:** `CONSTITUTIONAL_REGRESSION_SCENARIOS.md` is present; active validation and dated evidence publication remain deferred unless reinstatement is requested. Open P1 path in [TODO.md](../TODO.md).

**Architecture process:** [doc_architecture.md](../doc_architecture.md) remains the stable ownership and editing map. Optional AI corpus follow-ups remain in [plans/ai_corpus_optimization_plan.md](plans/ai_corpus_optimization_plan.md).

## Archive Index

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
- **Older MEMLOG/TODO snapshots:** removed 2026-06-17; retrieve from git history if needed

## Operating Rule

Add new session entries above the archive index only when they carry forward current context, decisions, verification status, or next actions. For detailed closure narratives, create a dated archive snapshot and leave a one-line pointer here.

Standard closeout order: commit substantive corpus/source changes first; then snapshot active meta files (`TODO.md`, `MEMLOG.md`, and living worklists) into `archive/`; then slim the active meta files to pointers and current open work.
