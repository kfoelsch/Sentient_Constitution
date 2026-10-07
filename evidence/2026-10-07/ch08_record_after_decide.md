# Chapter Eight: Record after Decide, Operate phase added (2026-10-07)

Architectural rule: **CH8-PROCESS-ORDER-01** in [doc_architecture.md](../../doc_architecture.md#chapter-eight-process-order-ch8-process-order-01). Follows [ch08_process_order_reorder.md](ch08_process_order_reorder.md).

## Decision

The record states the outcome, so the decision now comes before the record. A certification that is in force also needs a phase of its own for being kept current. Chapter Eight now runs in six phases. Only order, labels, links, and reader aids changed. No obligation was added, dropped, or reworded; the new §8 opening and the rewritten §6 opening are non-operative trace and plain-terms text.

## Six phases

| Phase | Sections | File |
|-------|----------|------|
| I. Frame | §2 System Class Evaluation; §3 Challenging a Certification | Part A |
| II. Evaluate | §4 | Part A |
| III. Review | §5 Forum Process | Part B |
| IV. Decide | §6 Certification Outcomes | Part B |
| V. Record | §7 System Certification Record | Part B |
| VI. Operate | §8 Recertification and Reopening; §9 Relationship to Standing | Part B |

## Old to new numbers (Part B; Parts A and C unchanged)

| Old | New | Title |
|-----|-----|-------|
| 6, 6.1, 6.2 | 7, 7.1, 7.2 | System Certification Record; Minimum record contents; Record integrity |
| 7 and 7.1 | 6 | Certification Outcomes (old §7 introduction and §7.1 merged; retitled) |
| 7.2 | 8 | Recertification and Reopening (promoted; new Trace and plain-terms opening) |
| 7.2.1 | 8.1 | Provisional and full recognition |
| 7.3 | 8.2 | Non-evasion |
| 8 | 9 | Relationship to Standing |

## Changes beyond renumbering (all non-operative)

- §6: Trace reduced to the outcome's own upstream and downstream; plain-terms gloss rewritten for the Decide phase.
- §8: new Trace and plain-terms gloss (text taken from the old §7 ones).
- Part B intro, Part A §1.1 (prose, redrawn chart, phase table), hub (phase table, run sheet steps 8–11, intro text).
- `doc_architecture.md`, `project/MEMLOG.md`.

## Tool

`tools/ch8_record_after_decide.py`: mapping-driven rewrite of links, anchors, bare cites, and Part B composition. Hand-edited, not rewritten by the tool: `doc_architecture.md`, `project/MEMLOG.md`, `corpus_systems/cs_02_b_data_classifications.md`, `evaluation/external_audit_2026-08/FINDINGS.md`.

## Verification

- `make -k regression`: green after `make plain-terms-edition`, `make boundary-chunks`, and `make ai-corpus-sync` (before those, only the fragment, section-label, and manifest-freshness checks failed, on stale generated files and two hand-edited links).
- `tools/obligation_inventory_diff.py` over Parts A, B, and C against `HEAD`: 295 obligations before, 295 after, every obligation matched 1:1.
