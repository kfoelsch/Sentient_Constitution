# Article Split Migration Map (Draft)

Date: 2026-04-10  
Scope: `core_constitution.md` Chapter Nine (**Articles V–XXIV**)  
Intent: deterministic old-to-new split map for one-wave structural rewrite, then one global reference migration.

**Update (2026-04-11):** Chapter Nine uses **planet-first presentation** (**Parts A-D**).
**Part A** covers **Articles I**, **II**, **III** (**III-A**, **III-B**), and **IV**.
**Part B** covers **Article V**, **VI**, **VII-IX**, and **X**.
**Part C** covers **Articles XII-XXI**.
**Part D** covers **Articles XXII-XXIV** for justice, evolution, and transition.
See **Reading order and fulfillment** in [core_constitution.md](../core_constitution.md) Chapter Nine. The table below is **archaeology only** and should not be cited for current Roman targets.

## Rules for this map

- This is a structural/readability migration aid, not a doctrinal source.
- Top-level Roman article anchors are preserved; split IDs use suffixes (`I-A`, `I-B`, ...).
- References should migrate to the most specific new target available.
- Where a legacy citation is broad and context is unclear, map to the `-A` entry for that article and flag for manual review.

## Canonical old-to-new map

| Legacy Article | New Split IDs | Canonical focus clusters for migration |
| --- | --- | --- |
| Article V | I-A through I-D | Dignity and equal moral standing; nondiscrimination; full inclusion and equality in adjudication and operations; freedom of conscience, religion, and comparable worldview |
| *(current)* **Article III** | V-A, V-B | Survival and education access |
| *(current)* **Article I** | VI-A–VI-C | Environmental survival |
| *(current)* **Article II** | VII-A–VII-E | Material stewardship and durable-use integrity |
| *(current)* **Article XIII** | VIII-A–VIII-C | Info-sphere integrity |
| *(current)* **Article XII** | IX-A–IX-D | Reliable and trustworthy systems |
| *(current)* **Article VII** | II-A–II-E | Self-ownership |
| *(current)* **Article VIII** | III-A–III-D | Self-determination and agency |
| *(current)* **Article IX** | IV-A–IV-C | Cooperative interaction |
| *Articles IX, VI, X, and XIII–XXIII* | *—* | *See [core_constitution.md](../core_constitution.md) headings; Roman numerals **X** onward shifted when **Article II** (material) was inserted and **IV–XXII** were each bumped +1.* |

## Migration protocol (for implementation phase)

1. Split article bodies in `core_constitution.md` according to this map without normative rewrites.
2. Add temporary transition labels under each new split heading: `Formerly Article <Roman>`.
3. Execute one global citation pass across corpus and governance docs:
   - `core_constitution.md`
   - `corpus_primitives.md`
   - `corpus_systems.md`
   - `doc_architecture.md`
   - `CONSTITUTIONAL_REGRESSION_SCENARIOS.md`
4. Resolve ambiguous legacy references:
   - Promote to the most specific split ID if local context is clear.
   - Otherwise map to `-A` and log in a manual-review table.
5. Run reference integrity audit and update regression scenarios for material structural changes.

## Manual-review table template (populate during migration)

| File | Legacy citation | Candidate target | Reason for ambiguity | Final decision |
| --- | --- | --- | --- | --- |
| _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ |

## Execution status (2026-04-10)

One-wave fallback migration executed for singular legacy citations (`Article <Roman>` -> `Article <Roman>-A`) outside top-level article headings.

Replacement counts:
- `core_constitution.md`: 74
- `corpus_primitives.md`: 148
- `corpus_systems.md`: 104
- `doc_architecture.md`: 50
- `CONSTITUTIONAL_REGRESSION_SCENARIOS.md`: 56

Post-pass check:
- Legacy singular `Article <Roman>` references in the target set now remain only at top-level chapter-five article headings (`### Article V` ... `### Article XX`), which were intentionally preserved.

## Precision refinement status (2026-04-10)

A conservative second-stage semantic refinement pass was applied after fallback migration.

Refinement rules used:
- Upgrade `Article X-A` to:
  - `Article X-B` where text is specifically about participation weighting or threshold proportionality.
  - `Article X-C` where text is specifically about high-impact legitimacy-gate/binding-effect conditions.
  - `Article XI-D` where text is specifically about internal roles/material responsibility and anti-token process posture.
  - `Article XI-A/Article XI-B` where both representation scope and weighting constraints are implicated.
- Governance participation and voting entitlement: **Article IX-C** (*Governance Participation and Voting Entitlement*). Stakeholder role floors: **Article IX-B** (*Stakeholder Role and Participation Rights*).
- Upgrade `Article XXII-A` to:
  - `Article XXII-D` for emergency-specific references.
  - `Article XXII-F` for rights-collision-specific references.

Files refined in this stage:
- `core_constitution.md`
- `corpus_primitives.md`
- `corpus_systems.md`
- `doc_architecture.md`
- `CONSTITUTIONAL_REGRESSION_SCENARIOS.md`

Verification after refinement:
- Targeted stale-phrase scans: no matches for corrected patterns.
- `make reference-audit`: `PASS`.
- Lint diagnostics on touched files: no errors.
