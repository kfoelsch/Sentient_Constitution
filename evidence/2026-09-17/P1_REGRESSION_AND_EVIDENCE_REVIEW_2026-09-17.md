# P1 Regression and Evidence Review — 2026-09-17

**Run ID:** `p1-regression-review-2026-09-17-01`

## Scope

This review addresses the P1 workflow-reinstatement item in [TODO.md](../../project/TODO.md). It checks the scenario catalog, the dated evidence convention, and readiness of the separately scoped Humanity/Individual/Cross-layer stress pack. It does not treat a structural audit as evidence of institutional or human performance.

## Verification

- `make scenario-audit` — **PASS**.
  - Matrix: 189 rows; 131 `pass`, 58 `draft`, 0 `partial`, 0 `fail`, 0 unknown.
  - Seed blocks: 192 defined IDs; every matrix ID has a local seed block.
  - Section 10.5: `SCORING-v1`, six dimensions at `8.4`, weighted score `8.4`; snapshot is internally consistent.
- `make regression` — **PASS**. The full repository regression target completed, including the scenario audit above.
- Dated evidence convention — **PASS**. This artifact is recorded under `evidence/2026-09-17/`; the earlier reinstatement artifact remains at [evidence/2026-04-23/REGRESSION_REINSTATEMENT_2026-04-23.md](../2026-04-23/REGRESSION_REINSTATEMENT_2026-04-23.md).
- Regression suspension rule — **RECONCILED**. `.cursor/rules/testing.mdc` is absent from the checkout. The active rule at [`.cursor/rules/sentient-constitution.mdc`](../../.cursor/rules/sentient-constitution.mdc) directs operators to run `make regression`; the reviewed policy surfaces contain no suspended-regression instruction.
- Queued observations — **NONE FOUND**. No separate observation queue was identified in the reviewed TODO, scenario catalog, evidence, implementation, or editor-rule paths, so no additional `RS-*` rows were required.

## Stress-pack disposition

The catalog contains 35 stress-pack rows: `RS-HUM-001..015`, `RS-IND-001..015`, and `RS-XD-001..005`. All remain `draft`. Their corresponding blocks are catalog placeholders and do not provide scenario-specific procedure, expected result, or dated execution evidence. They therefore remain open and were not converted to `pass`.

The existing family note identifies the intended cross-layer checks: Chapters Eleven–Thirteen versus Chapter Eight measurement authority, rights-layer process creep, custody-chain integrity, emergency controls, and evidence gates. Those are useful routing pointers, but they are not a completed first-pass validation record.

## Disposition

The workflow-reinstatement P1 item is closed by this review. The Humanity/Individual stress-pack P1 item remains open pending substantive scenario definitions and first-pass evidence. The authored `SCORING-v1` snapshot remains a consistency snapshot, not a score of live institutional performance.
