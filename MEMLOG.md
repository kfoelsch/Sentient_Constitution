# MEMLOG

## Purpose

Session memory log for current project context, decisions, and next actions. Keep this file lean; archive detail snapshots rather than carrying full session history forward.

## Current State

**2026-04-30:** [architecture_primer.md](architecture_primer.md) marked **Locked** (`2026-04-30`) with cross-reference alignment in **Chapters Eleven–Fourteen** routing. Publish prep for public GitHub: reconciled drifted **Corpus edition** / **Effective date** stamps to **`SC-Corpus-2026.04.32`** / **2026-04-24**; README companion list deduped. **`make regression`** and **`make best-practices-check`** green; **`make regression-full`** still fails **`readability-audit`** (`very-long-sentence` findings—see [README.md](README.md)). **P3** holistic redundancy sweep **waived** for this cut ([TODO.md](TODO.md)). **LICENSE** (CC BY 4.0) and **`.gitignore`** added. Earlier continuation narrative: `1819cbc` → [archive/MEMLOG_ARCHIVED_2026-04-30.md](archive/MEMLOG_ARCHIVED_2026-04-30.md). Deferred **P1** in [TODO.md](TODO.md).

## Active Threads

**P3 holistic redundancy sweep:** Waived for edition **`SC-Corpus-2026.04.32`** GitHub publication cut; resume post-release per [TODO.md](TODO.md).

**Regression scenarios:** `CONSTITUTIONAL_REGRESSION_SCENARIOS.md` is present; validation and evidence publication stay deferred unless reinstatement is requested. See P1 items in [TODO.md](TODO.md).

**Architecture process:** [doc_architecture.md](doc_architecture.md) remains the stable ownership map. [implementation/ARCHITECTURE_WORKLIST.md](implementation/ARCHITECTURE_WORKLIST.md) tracks recurring open obligations.

## Archive Index

- [archive/MEMLOG_ARCHIVED_2026-04-30.md](archive/MEMLOG_ARCHIVED_2026-04-30.md) — active MEMLOG before the 2026-04-30 post-commit slim pass.
- [archive/MEMLOG_SNAPSHOT_2026-04-30.md](archive/MEMLOG_SNAPSHOT_2026-04-30.md), [archive/MEMLOG_SNAPSHOT_2026-04-30_POST_COMMIT.md](archive/MEMLOG_SNAPSHOT_2026-04-30_POST_COMMIT.md) — earlier 2026-04-30 layers.
- [archive/MEMLOG_SNAPSHOT_2026-04-29.md](archive/MEMLOG_SNAPSHOT_2026-04-29.md) — prior session snapshot.
- [archive/MEMLOG_SNAPSHOT_2026-04-26.md](archive/MEMLOG_SNAPSHOT_2026-04-26.md) and [archive/MEMLOG_ARCHIVED_2026-04-26.md](archive/MEMLOG_ARCHIVED_2026-04-26.md) — older layers.

## Operating Rule

Add new session entries above the archive index only when they carry forward current context, decisions, verification status, or next actions. For detailed closure narratives, create a dated archive snapshot and leave a one-line pointer here.

Standard closeout order: commit substantive corpus/source changes first; then snapshot active meta files (`TODO.md`, `MEMLOG.md`, and living worklists) into `archive/`; then slim the active meta files to pointers and current open work.
