# MEMLOG

## Purpose

Session memory log for current project context, decisions, and next actions. Keep this file lean; archive detail snapshots rather than carrying full session history forward.

## Current State

**2026-10-14 — Domain-Specific Materiality, Class P, and Chapter Seven (committed on branch `docs/ch09-institutional-alignment-certification`):** [Domain-Specific Materiality](../core_05_band_oversight.md#domain-specific-materiality) is the one nine-question test for whether an act is material (the Materially Binding Act test) and whether a body is at least Class L and so needs a System Charter or Institutional Charter. One yes is enough; related bodies aggregate by common power to direct or override, not by funding; adopter numbers are guides only; challenges use the existing routes (CS-3 §7.4; Chapter Nine Part D §14.2 and §14.4). Class P is split into a private unit and ordinary community activity below every line. CS-3 Part B, Chapter Seven, Article XVII-A, XVIII-A and X-D, the adopter pages and `RS-CH5-DSM-001` to `-010` match. Chapter Seven was also restructured (new §2 *No Licence, and Two Narrow Limits*, one chart, sections resequenced). New rule **FILE-COPY-SUFFIX-01** in `doc_architecture.md`: copy-suffixed duplicate files (`name 2.ext`) are not corpus and may be deleted freely. The scenarios markdown is now generated from `tools/architecture/regression_scenarios.json`. Edition `SC-Corpus-2026.10.14`. Records: project docs `claude/domain-specific-materiality-evaluation.md`, `claude/domain-specific-materiality-followthrough-implementation.md`, `claude/domain-specific-materiality-outstanding-issues-implementation.md`, `claude/class-p-constraints-and-burden-implementation.md`, `claude/dsm-scenario-seeds-and-copy-suffix-rule-implementation.md`. The day's entries are in [archive/MEMLOG_SNAPSHOT_2026-10-14.md](../archive/MEMLOG_SNAPSHOT_2026-10-14.md). The Class L challenge load is handled by six structural rules in the entry's Challenge route (body answers first; a challenge naming no crossing is returned, not decided; related challenges heard once; a finding stands until something changes; a challenge does not stop the body; forums plan surge capacity under CF-16.2), seed `RS-CH5-DSM-010`, record in project doc `claude/challenge-route-sizing-implementation.md`. `make regression` now checks the scenario catalog against the generated file and scans the whole corpus for unnamed section cites.

**2026-10-15 — Chapter Seven follows the chart (uncommitted on branch `docs/ch07-formation-check-clocks-and-small-business-seats`):** the chapter now reads in the order of its one chart: purpose and chart (§1), no licence (§2), when required (§3), what it must state (§4), the Charter Role Map (§5), the formation check (§6), when a holder fails the check (§7, new), keeping it true (§8), what it cannot do (§9), relationship to other chapters (§10). The chart is 8 boxes. Twenty-fifth move in [doc_architecture.md](../doc_architecture.md); evaluation and implementation note in the project docs `claude/ch07-streamline-chart-and-process-evaluation.md` and `claude/ch07-sections-follow-chart-implementation.md`. Process simplifications in the evaluation (one list, one office table, one clock) await steward sign-off.

**2026-10-15 — Dissolution and forced-contraction procedure (uncommitted, same branch):** CI-13.1 to CI-13.10 now give the consequence ladder (directed correction, constrained authority, contraction order to below Class L, supervised operation, receivership or separation, dissolution last), with findings, a 7-day response and 30-day cure, two-key concurrence at rungs 5 and 6, continuity-first and remedy-first dissolution, a Systems counterpart with sealed custody for credible-sentience systems, and review and enforcement. The Chapter Seven chart gained two boxes for it. Draft and open decisions are in the Project doc `claude/dissolution-procedure-draft.md`. See the Twenty-sixth move in `doc_architecture.md`.

Earlier session narratives (2026-06-15 through 2026-09-27: Chapter Six restructures, Articles X and XI restructure, institutional secularism move, Hard Content term, plain-language backlog, link and archive cleanups, Pages build, reader entry pages, new Chapter Five terms, segregation of duties, seat catalog, evaluation follow-ups) are in [archive/MEMLOG_SNAPSHOT_2026-09-27.md](../archive/MEMLOG_SNAPSHOT_2026-09-27.md) and [archive/MEMLOG_SNAPSHOT_2026-10-03.md](../archive/MEMLOG_SNAPSHOT_2026-10-03.md); the 2026-10-01 to 2026-10-13 entries (Chapter One reorganization; Chapter Nine reorder, go-live gate, certification-status rename, process alignment and cause finding; sibling audit modes; influence-contact rules and the pilot section; Chapter Seven, the Charter Role Map and the Charter rename; Chapter Nine Part D and the formation check) are in [archive/MEMLOG_SNAPSHOT_2026-10-13.md](../archive/MEMLOG_SNAPSHOT_2026-10-13.md). The steward signed off the wording in those entries on 2026-10-13.

## Standing Decisions

**Constitutional Constraints bind globally (steward decision, 2026-10-14):** every system, institution, and other body is bound at every class and in every context, including Class P and sandboxed scope. Class scales the intensity, form, and machinery that carry a constraint, never whether it applies.

**Burden of proof falls to the claimant (steward decision, 2026-10-14):** a body claiming to be below a line shows it with a short written statement; a challenger names a specific crossing in a named domain, and the body then shows it is below that line (Chapter Four §1).

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
