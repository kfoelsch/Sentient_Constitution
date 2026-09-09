# MEMLOG

## Purpose

Session memory log for current project context, decisions, and next actions. Keep this file lean; archive detail snapshots rather than carrying full session history forward.

## Current State

**2026-09-09 — AI evaluation follow-ups (backlog in [TODO.md](TODO.md) *2026-09-09* section):** R1–R3 core text landed (Chapter Eight §2.1 *Silence is the default*; Chapter Nine §4.4 remedy parity, §7.1–§7.2 anti-aggregation and plain statement; Chapter One §9.1.1 role-scoped observability; Article V-E independent representation / shield-for-the-entity; Chapter Eleven §5 intake-gate audit and capacity-failure routing; Article XXVI-A preservation over deletion). Process-support items landed: eval item 19 (over-inclusion red team; pack `eval-pack-2026-09-09`), vignettes 6–7, audit weight classes in `implementation/AUTOMATED_REFERENCE_CHECKING.md`, `make plain-terms-edition`. Companion follow-through landed: CS-4 §10 role-scoped observability pointers; CI-27.5 / CF-11 / CF-5.4 remedy-parity and capacity-failure; CF-4.14 independent-representative appointment; CJS-R20 / CJS-R21; I4(b) schema version 2 (`independent_representative`, `intake_decline_log`). Open: I1 human evidence, I2 adopter profile and cost, I3 LEQU calibration, I7 thin CI companions, apply-test of vignette 6. Live publication sequence stays in [VISION.md §4](VISION.md#path) and [implementation/PRE_PUBLICATION_SPEC.md](implementation/PRE_PUBLICATION_SPEC.md).

**2026-06-18 — Chapter Five constitutional band reorganization:** Part B/C retired to [archive/core_ch5_retired/](archive/core_ch5_retired/README.md); five band files (`core_05{o,p,a,c,i}_*_definitions.md`) are operative homes; Part A holds compass + directory + §3.0 meta; §3 clusters renumbered **Chapter One §8.2–Chapter One §8.16** (hard cut). Edition **`SC-Corpus-2026.06.18`**. `make regression` and `make alignment-audit` pass; evidence in [evidence/2026-06-18/](evidence/2026-06-18/). Pre-closeout meta snapshot: [archive/TODO_SNAPSHOT_2026-06-18.md](archive/TODO_SNAPSHOT_2026-06-18.md), [archive/MEMLOG_SNAPSHOT_2026-06-18.md](archive/MEMLOG_SNAPSHOT_2026-06-18.md).

**2026-06-17 — Non-corpus housecleaning:** Aggressive archive prune (keep canonical architecture anchors + root retirement snapshots only). Retired migration scripts moved to `archive/tools_retired/`; completed implementation plans to `archive/implementation_retired/`. No corpus doctrine changed.

**2026-06-15 — Meta-file archive cleanup:** Restored slim root `TODO.md` and `MEMLOG.md` after the 2026-05-07 root retirement. CI→CJS/CS relocation and P3 redundancy sweep closed; detail removed from `archive/` in 2026-06-17 pass — retrieve from git history if needed.

## Active Threads

**2026-09-09 evaluation backlog:** open items I1, I2, I3, I7 and apply-test of vignette 6 in [TODO.md](TODO.md). Companion follow-through and I4(b) schema fields landed 2026-09-09. Regression baseline at that date carried three pre-existing findings (fossil fragment ids, a Def.P2 `§3.3`/`§4.3` label, id-resolver fossil aliases) that also fail at `HEAD`.

**P2 capitalization:** Partially landed (`71984fe`, `doc_architecture.md` rule, lexical audit checks). Open acceptance in [TODO.md](TODO.md).

**Regression scenarios:** `CONSTITUTIONAL_REGRESSION_SCENARIOS.md` is present; active validation and dated evidence publication remain deferred unless reinstatement is requested. Open P1 path in [TODO.md](TODO.md).

**Architecture process:** [doc_architecture.md](doc_architecture.md) remains the stable ownership and editing map. Optional AI corpus follow-ups remain in [plans/ai_corpus_optimization_plan.md](plans/ai_corpus_optimization_plan.md).

## Archive Index

- **Architecture process (canonical):** [archive/ARCHITECTURE_PRIMER_ARCHIVED_2026-05-08.md](archive/ARCHITECTURE_PRIMER_ARCHIVED_2026-05-08.md), [archive/ARCHITECTURE_ADOPTION_APPENDIX_ARCHIVED_2026-05-08.md](archive/ARCHITECTURE_ADOPTION_APPENDIX_ARCHIVED_2026-05-08.md), [archive/ARCHITECTURE_WORKLIST_ARCHIVED_2026-05-08.md](archive/ARCHITECTURE_WORKLIST_ARCHIVED_2026-05-08.md) — see [README.md](README.md)
- **2026-06-18 Chapter Five closeout:** [archive/MEMLOG_SNAPSHOT_2026-06-18.md](archive/MEMLOG_SNAPSHOT_2026-06-18.md), [archive/TODO_SNAPSHOT_2026-06-18.md](archive/TODO_SNAPSHOT_2026-06-18.md)
- **2026-05-01 root retirement:** [archive/MEMLOG_ROOT_RETIRED_2026-05-01.md](archive/MEMLOG_ROOT_RETIRED_2026-05-01.md), [archive/TODO_ROOT_RETIRED_2026-05-01.md](archive/TODO_ROOT_RETIRED_2026-05-01.md)
- **Older MEMLOG/TODO snapshots:** removed 2026-06-17; retrieve from git history if needed

## Operating Rule

Add new session entries above the archive index only when they carry forward current context, decisions, verification status, or next actions. For detailed closure narratives, create a dated archive snapshot and leave a one-line pointer here.

Standard closeout order: commit substantive corpus/source changes first; then snapshot active meta files (`TODO.md`, `MEMLOG.md`, and living worklists) into `archive/`; then slim the active meta files to pointers and current open work.
