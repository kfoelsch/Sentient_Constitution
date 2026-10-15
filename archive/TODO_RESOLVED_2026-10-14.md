# Resolved TODO items — archived 2026-10-14

This archive records completed items removed from the active [TODO.md](../TODO.md) on 2026-10-14, kept verbatim and grouped by their original section. Normative meaning remains in the binding corpus; this file is a process-history record.

## 2026-10-04 — Process-level granularity: Option A drafted, Option B outlined (completed items)

- [x] **Check `MINIMUM_VIABLE_ADOPTER.md` §4.1** against `adoption/ANNOUNCEMENT.md` so the outline never reads as a promised feature. **Checked 2026-10-14:** `implementation/adoption/ANNOUNCEMENT.md`, `README.md`, `START_HERE.md`, `llms.txt` and `docs/index.md` do not mention standard-process recognition, and §4.1 itself says "Outline only", "not binding, not adopted", and that it cannot start earlier than the first certification cycle. Nothing to change.

## 2026-10-14 — Domain-Specific Materiality: open decisions (completed)

- [x] **Class L capacity load is not modeled.** Resolved 2026-10-14: the Challenge route in Domain-Specific Materiality now keeps the load light with six structural rules (the body answers first; a challenge naming no crossing is returned, not decided; related challenges are heard once; a finding stands until something changes; a challenge does not stop the body; forums plan surge capacity under CF-16.2). CS-3 §7.4, Chapter Nine Part D §14.4 and CF-16.2 point at it. Core sets no numbers. Seed `RS-CH5-DSM-010`. Record: project doc `claude/challenge-route-sizing-implementation.md`.
- [x] **Scenario catalog drift check.** Resolved 2026-10-14: `make scenario-catalog-check` (`python3 tools/emit_regression_scenarios.py --check`) is part of `make regression`.

## 2026-10-01 to 2026-10-03 — Chapter One relocation and numbering: open follow-ups (completed items)

- [x] **Bare untitled "§N" Chapter One cites** are unchecked by any audit. Resolved 2026-10-14: the unnamed cites in Chapter One (13 in Part C, 6 in Part A), Chapter Nine Part D (11) and Chapter Six Part B (1) were given titles, and `make section-cite-name-audit` now scans the whole binding corpus in `make regression` (it passes with no findings).
