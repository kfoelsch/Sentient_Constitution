# MEMLOG

## Purpose

Session memory log for current project context, decisions, and next actions. Keep this file lean; archive detail snapshots rather than carrying full session history forward.

## Current State

**2026-10-19 — CI-13 split (uncommitted):** CI-13 is now *Institutional failure and dissolution* (CI-13.1 to CI-13.4) and the new CI-28 is *Institutional accountability and sanctions* (CI-28.1 to CI-28.6), placed after CI-13 in reading order. Old 13.4 to 13.6 are 28.1 to 28.3, 13.7 is 13.4, 13.8 to 13.10 are 28.4 to 28.6; 13.1 to 13.3 are unchanged. Text moved verbatim, cites repointed corpus-wide, `make audit-report` passes. Details in `doc_architecture.md` sixty-fifth move.

**2026-10-18 to 2026-10-19 — Time windows, Document at Action, CS-4, and Chapter Seven (committed on branch `docs/ch11-dissolution-reformation-lock`, which stacks the earlier time-windows branch; not yet merged):** the time-window decisions are under Standing Decisions below. Document at Action is Chapter One §16.4 (applied in CF-11.3.2 and CF-12.6). CS-4 is rewritten for plain readers, with the CS-4.10.3 link target now the heading slug. Chapter Seven: §1.3 is split (§1.3 to §1.7); the response and resolution windows take the matching tier's intake target and outer bound (Tier L lengthens, response 7 to 8 days and resolution 30 to 60); the TIME-LOCK-01 audit keeps the tier-window copies in step with their owners (`make time-window-lockstep-audit`); a repeat request that shows a material change or new evidence is handled as a new request with its own windows; chart boxes put the section number first (VIS-CHART-SECNUM-09, `make chart-section-number-audit`); locks can sit on institutions, and a Dissolution Reformation Lock bars a dissolved Chartered Party from re-forming (Chapter Eleven §5.5; permanent locks limited to two grounds, §8); §2 is split into §2.1 to §2.4 and §3 into §3.1 to §3.5. TIME-REF-01 is a registry audit with a shrink-only baseline (78 entries). Thirty-second to fiftieth moves in [doc_architecture.md](../doc_architecture.md). Test 1 note: [evidence/2026-10-18/time-window-test-1-self-check.md](../evidence/2026-10-18/time-window-test-1-self-check.md) (covers the 30 / 60 / 90-day scale, not yet the Chapter Seven window lengths). The wording is core text and needs the steward's sign-off; follow-ups are in [TODO.md](../TODO.md). The earlier detail is in [archive/MEMLOG_SNAPSHOT_2026-10-19.md](../archive/MEMLOG_SNAPSHOT_2026-10-19.md).

**2026-10-19 — Chapter Seven §4 subsections, and the word "instrument" (committed on the same branch):** §4 is split into §4.1 to §4.7 with the §4 anchor kept. The word "instrument" is on the do-not-use list: the entry in `tools/architecture/lexical_guardrails.json` is advisory, and the `avoid-instrument` rule in `tools/lexical_vocabulary_audit.py` enforces it on the numbered `core_*` and `corpus_*` files, `implementation/`, README, START_HERE, `guides/`, `docs/`, `evaluation/` and `project/`. Dated records (file names with a date at the start or end, the 2026-08 external audit folder) and `project/translation_drafts/` are exempt. About 500 uses were swept without changing meaning; Chapter Seventeen §10.2 is renamed **Adoption Document** (anchor `#102-adoption-document`, links updated). Notes: project docs `claude/ch07-section4-subsections-implementation.md` and `claude/instrument-word-ban-sweep-implementation.md`. Translations, dated records and `doc_architecture.md` keep the old wording. The Adoption Document name needs the custodian's confirmation.

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
