# MEMLOG

## Purpose

Session memory log for current project context, decisions, and next actions. Keep this file lean; archive detail snapshots rather than carrying full session history forward.

## Current State

**2026-10-13 — Chapter Nine hold lifted (steward decision):** the 2026-10-04 hold on core changes to Chapters Nine and Thirteen is removed. The announcement will not be made until the corpus is complete, so core changes are not timed around it. TODO.md updated.

**2026-10-13 — State of the Chapter Seven and Chapter Nine Part D work (steward signed off):** New Chapter Seven (System, Institutional and Constitutional Charters, Charter Role Map, formation check), Chapter Nine Part D (institutional alignment certification, remediation readiness, denial and revocation), the Interim Hold standard, and the influence-contact and pilot wording are committed on branch `docs/ch09-institutional-alignment-certification`. Remaining work is in [TODO.md](../TODO.md): the Chapter Seventeen §1 heightened review for Article XI-E and the Interim Hold, the "Not done" lists, the open questions carried over from these entries, and translations. Entries: [archive/MEMLOG_SNAPSHOT_2026-10-13.md](../archive/MEMLOG_SNAPSHOT_2026-10-13.md).

Earlier session narratives (2026-06-15 through 2026-09-27: Chapter Six restructures, Articles X and XI restructure, institutional secularism move, Hard Content term, plain-language backlog, link and archive cleanups, Pages build, reader entry pages, new Chapter Five terms, segregation of duties, seat catalog, evaluation follow-ups) are in [archive/MEMLOG_SNAPSHOT_2026-09-27.md](../archive/MEMLOG_SNAPSHOT_2026-09-27.md) and [archive/MEMLOG_SNAPSHOT_2026-10-03.md](../archive/MEMLOG_SNAPSHOT_2026-10-03.md); the 2026-10-01 to 2026-10-13 entries (Chapter One reorganization; Chapter Nine reorder, go-live gate, certification-status rename, process alignment and cause finding; sibling audit modes; influence-contact rules and the pilot section; Chapter Seven, the Charter Role Map and the Charter rename; Chapter Nine Part D and the formation check) are in [archive/MEMLOG_SNAPSHOT_2026-10-13.md](../archive/MEMLOG_SNAPSHOT_2026-10-13.md). The steward signed off the wording in those entries on 2026-10-13.

## Standing Decisions

**Chapter Nine order (editor decision, 2026-10-07):** Chapter Nine sections follow the order the certification work is done. New sections go in the phase where the work happens, not at the end of a file. Renumbered before the announcement so no redirect anchors are needed later.

**Go-live gate (editor decision, 2026-10-08):** No system goes live, pilot or full, before it is certified. A pilot is certified on its own record, scaled by class and substitutability. Systems already operating at an adopter's effective date are excepted only for the Article XXVIII-A transition clock. The published record challenge path opens when the outcome is published, or is already open for a system already operating.

**Translations paused (editor decision, 2026-09-23):** Translations under [translations/](../translations/) may fall out of date while the English edit pass continues; do not resync after each English change. The English numbered `core_*` files govern. At the restart, resync fully against the English source. Known gaps: translated files still use pre-renumbering chapter filenames (e.g. `translations/es/core_07_system_alignment_certification.md` holds Chapter Nine), which accounts for nearly all remaining broken links in the repo; translated text still uses the published-edition article labels (only links into English files were re-anchored). Chapter Six has been renumbered several times since; the old → new label mapping is in the 2026-09-25 through 2026-09-27 entries of [archive/MEMLOG_SNAPSHOT_2026-09-27.md](../archive/MEMLOG_SNAPSHOT_2026-09-27.md). Translation lane: [CONTRIBUTING.md](../CONTRIBUTING.md#lane-f).

**Pages build:** `_pages_site/` is a local preview only; CI rebuilds it on each deploy. `make pages-deploy-gate` runs in `pages.yml` before every build; `.github/workflows/checks.yml` runs `make regression` on every push and PR. Do not list "Regenerated `_pages_site`" in editing passes. **Open:** switch **Settings → Pages → Source** to *GitHub Actions* before the announcement.

**Reader entry pages:** **README** is the one public door for all readers (timed reading paths at `README.md#reading-paths`); **START_HERE** is the start page for would-be adopters and operators; [guides/CONCEPTUAL_OVERVIEW.md](../guides/CONCEPTUAL_OVERVIEW.md) is the second-step big-picture map.

**Link rules:** Binding corpus links only by relative path or `#fragment` (LINK-OFF-CORPUS-15, `make external-link-audit`) and never deep-links into a README section (SUPPORT-DOC-POINTER-01). A pasted `https://file+.vscode-resource.vscode-cdn.net/…` link is the VS Code Markdown preview rewriting a correct relative link, not corpus text.

**Warning:** `tools/emit_regression_scenarios.py` is stale against the hand-maintained [CONSTITUTIONAL_REGRESSION_SCENARIOS.md](CONSTITUTIONAL_REGRESSION_SCENARIOS.md) (running it drops rows and flips draft/pass). Do not run it until its catalog is resynced.

## Active Threads

**Evaluation:** I1 (human evidence) remains open in [TODO.md](../TODO.md); resolved follow-ups are in [archive/TODO_RESOLVED_2026-09-17.md](../archive/TODO_RESOLVED_2026-09-17.md).

**Regression scenarios:** `CONSTITUTIONAL_REGRESSION_SCENARIOS.md` is present; active validation and dated evidence publication remain deferred unless reinstatement is requested. Open P1 path in [TODO.md](../TODO.md).

**Architecture process:** [doc_architecture.md](../doc_architecture.md) remains the stable ownership and editing map. Optional AI corpus follow-ups remain in [plans/ai_corpus_optimization_plan.md](plans/ai_corpus_optimization_plan.md).

**2026-10-14 Chapter Seven new §2:** The right to form and the two narrow Article XI-E limits now sit in a short new §2 (No Licence, and Two Narrow Limits), stated once; the formation check (now §6) points back to it. Old §2 to §8 are now §3 to §9; no rule changed. Decision-path chart moved to the end of the new §2. Citations retargeted, indexes rebuilt. See [doc_architecture.md](../doc_architecture.md) (Eighteenth move).

**2026-10-14 Chapter Seven §2 and §6 overlap:** Chapter Seven §6 (formation check) stays a separate section. Its two Result bullets that repeated §2 are now one pointer, and the founder-authenticity limit of the right to form moved into §2. No renumbering or citation changes.

**2026-10-14 Chapter Seven one chart:** The two charts are now one, at the end of §2, with a single Reader guidance widget. The §1 chart and its text were removed. No renumbering.

**2026-10-14 Chapter Seven section order:** Sections reordered to follow the path a body takes (required, stated, role map, formation check, kept true, cannot do, relationships), matching the two charts now in §1. Old §4 to §6, §5 to §7, §6 to §4, §7 to §5; no rule changed. Citations in other chapters retargeted and indexes rebuilt; dated records and translations keep the old numbers. See [doc_architecture.md](../doc_architecture.md) (Seventeenth move).

**2026-10-13 Article XI-E gates and Institutional Authority Standing Lock:** Article XI-E still bars any gate on forming or operating, and now adds two narrow gates on a named sentient's authority: an outstanding lock, and an interim hold on probable cause of misalignment (forum-issued, specific verified facts, more likely than not, narrow, time-bound, not a lock or finding). New Institutional Authority Standing Lock in Chapter Eleven §5.5 for verified use of an institution as a vehicle for a violation. Chapter Seven §7, Part D, and CI-3.6 aligned. Committed on branch `docs/ch09-institutional-alignment-certification`. Needs Chapter Seventeen §1 heightened review. See [doc_architecture.md](../doc_architecture.md) Fourteenth move.

**2026-10-13 Interim Hold standard:** Corpus sweep for interim measures, then built one general standard: Chapter Five entry *Interim Hold*, Chapter Thirteen §5 subsection (owner), Chapter Eleven §5.6 (not a lock, no standing effect, time counts toward a later lock's bound), CF-4.15, and applications in Article XI-E, Chapter Seven §7, CI-4.2, CF-7.3.2, Article XII-D. Committed on branch `docs/ch09-institutional-alignment-certification`. Needs Chapter Seventeen §1 heightened review. See [doc_architecture.md](../doc_architecture.md) Fifteenth move.

## Archive Index

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
