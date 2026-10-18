# MEMLOG

## Purpose

Session memory log for current project context, decisions, and next actions. Keep this file lean; archive detail snapshots rather than carrying full session history forward.

## Current State

**2026-10-18 — Time windows (committed on branch `docs/time-windows-ref-audit-cs4-rewrite`; the scale, levels, and office merged earlier in PRs #79 and #80):** tier outer bounds are 7, 14, 30, 60, and 90 days (Tiers A, B, C, L, P); certification intervals are calendar periods (3 months, 6 months, 1 year, 2 years, 3 years) and the review unit is retired. Time-scale levels (Standard, Coordinated, Heavy) lengthen only on a Chapter Thirteen §6.1 showing; an Emergency level (Tier A only, 3-day bound, protective steps hard) shortens. Restricted evidence never slows the clock; access disputes go first to the restricted information office (CF-5.8). Windows are named by TIME-NAME-01 and CJS-0.4 (tier window, prompt-review window as the matching tier's intake target and a hard line, restore-challenge window, hold lapse date, and others); CUL and NUL levels take the tier columns. A "reasonable" period is 14 days (the Tier B outer bound); "promptly" is not a length; record updates in CS-2 §8.5 and CS-3 §7.5 ride the certification interval. The TIME-REF-01 audit (`make time-reference-audit`, registry `tools/time_reference_registry.json`) checks that every time reference names its bound kind and its tier or class; older references sit in a shrink-only baseline (92 entries). Thirty-second to forty-sixth moves in [doc_architecture.md](../doc_architecture.md). Test 1 note: [evidence/2026-10-18/time-window-test-1-self-check.md](../evidence/2026-10-18/time-window-test-1-self-check.md). Records: project docs `claude/archive/promptly-alignment-with-time-windows-evaluation.md`, `claude/archive/time-window-urgency-complexity-matrix-evaluation.md`, `claude/archive/time-window-names-evaluation.md`, `claude/dissolution-procedure-draft.md`. The wording needs the steward's sign-off (core text); follow-ups are in [TODO.md](../TODO.md).

**2026-10-18 — Document at Action (Chapter One §16.4):** new stewardship principle: the act makes its own record, by automated capture where feasible; what is not lawfully restricted is available when the act is taken; what is restricted still leaves a marker, a stated ground, and a release path; the system, not the steward, carries the recording burden. It sets no deadline and does not open anyone's inner life (§17.3). Applied in CF-11.3.2 (publication; fallback bound is the tier outer bound) and CF-12.6 (continuity-mode communications); pointers from CS-4.10.3, CJS-0.4, the Accountability and Oversight rows of the Chapter One aim table, and the Chapter Five Accountability leg and Attributable Action Trace. No Chapter Five definition, as for §17.3. Forty-fifth and forty-sixth moves.

**2026-10-18 — CS-4 rewritten for plain readers:** CS-4.1 to CS-4.20, with CS-4.10.1 to CS-4.10.8; headings match content and bullets replace dense paragraphs. The custom anchor on CS-4.10.3 is gone: the link target is the heading slug `#cs-4103-inspectable-attributable-action` (about 22 files retargeted; `tools/steward_door_lockstep_audit.py` checks it). Forty-third move.

**2026-10-14 to 2026-10-17 (merged earlier):** Domain-Specific Materiality is the one nine-question test for a material act and for Class L (Class P split into a private unit and ordinary community activity); Chapter Seven follows the order of its one chart; CI-13.1 to CI-13.10 give the consequence ladder (directed correction to dissolution, contraction to below Class L, Systems counterpart); Charter Pointer is a defined term; Backup Record Authority (CF-5.7) and operator and stakeholder standing records; verifiers outside the operator (Chapter Nine Part B §6.1.1, Part D §13.1). Full entries are in [archive/MEMLOG_SNAPSHOT_2026-10-18.md](../archive/MEMLOG_SNAPSHOT_2026-10-18.md).

Earlier session narratives (2026-06-15 through 2026-09-27: Chapter Six restructures, Articles X and XI restructure, institutional secularism move, Hard Content term, plain-language backlog, link and archive cleanups, Pages build, reader entry pages, new Chapter Five terms, segregation of duties, seat catalog, evaluation follow-ups) are in [archive/MEMLOG_SNAPSHOT_2026-09-27.md](../archive/MEMLOG_SNAPSHOT_2026-09-27.md) and [archive/MEMLOG_SNAPSHOT_2026-10-03.md](../archive/MEMLOG_SNAPSHOT_2026-10-03.md); the 2026-10-01 to 2026-10-13 entries (Chapter One reorganization; Chapter Nine reorder, go-live gate, certification-status rename, process alignment and cause finding; sibling audit modes; influence-contact rules and the pilot section; Chapter Seven, the Charter Role Map and the Charter rename; Chapter Nine Part D and the formation check) are in [archive/MEMLOG_SNAPSHOT_2026-10-13.md](../archive/MEMLOG_SNAPSHOT_2026-10-13.md). The steward signed off the wording in those entries on 2026-10-13. The 2026-10-14 to 2026-10-17 entries (Domain-Specific Materiality and Class P, Chapter Seven order, the dissolution procedure, Charter Pointer and review cadence, standing records) are in [archive/MEMLOG_SNAPSHOT_2026-10-18.md](../archive/MEMLOG_SNAPSHOT_2026-10-18.md).

## Standing Decisions

**Constitutional Constraints bind globally (steward decision, 2026-10-14):** every system, institution, and other body is bound at every class and in every context, including Class P and sandboxed scope. Class scales the intensity, form, and machinery that carry a constraint, never whether it applies.

**Burden of proof falls to the claimant (steward decision, 2026-10-14):** a body claiming to be below a line shows it with a short written statement; a challenger names a specific crossing in a named domain, and the body then shows it is below that line (Chapter Four §1).

**Time windows (custodian decisions, 2026-10-17 and 2026-10-18):** restricted evidence never slows the clock and is never a ground for a slower column or a longer window; a "reasonable" period is 14 days; "promptly" is not a length, and review of a measure in force, intake, and notice name their windows instead; record duties follow Document at Action (Chapter One §16.4), a design default and not a window; window names live in CJS-0.4 and the numbers stay with their owners (Chapter Thirteen §6, CF-11.3.1); no Chapter Five definitions for window names or for the new principle unless a core rule needs to cite them.

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
