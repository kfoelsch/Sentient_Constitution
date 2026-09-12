# Chapter One integration relocation — cut list and migration spec

**Status:** Applied (2026-06-24) — §2 and §§10–14 moved to Part A; §§6–9 remain Part B; full renumber to Part A §§1–10 / Part B §§11–14.  
**Scope:** Relocate integration layer from `core_01_b_stewardship_capacity_principles.md` to `core_01_a_values_principles.md`; renumber operational block §§11–9 → §§11–14.

---

## 1. Target reading order

`core_00_preamble.md` → **Part A complete (§§1–10)** → **Part B (§§11–14)** → `core_02-04_definition_mechanics.md`

**Part A arc:** Purpose → Wellbeing → Safety/Truth → Trust → Interaction/tradeoffs → Evaluation → Freedom → Override limits → Interpretation → Integrated Application (capstone).

**Part B arc:** Stewardship → Governance → Capacity → Market Structure.

---

## 2. Section renumber map

| Old § | New § | Title | File |
|------|------|-------|------|
| §1 | §1 | Purpose and Role | A |
| §14 | §14 | Foundational Objective: Wellbeing | A |
| §14 | §14 | Non-Negotiable Constraints: Safety and Truth | A |
| §14 | §14 | Trust | A |
| §14 | §14 | Interaction and Conflict Resolution | A |
| §11 | §11 | Systemic Evaluation Requirement | A |
| §12 | §12 | Freedom (Bounded Agency) | A |
| §13 | §13 | Prohibition on Absolute Override | A |
| §14 | §9 | Constitutional Interpretation | A |
| §14 | §14 | Integrated Application | A |
| §11 | §11 | Stewardship and Distributed Understanding | B |
| §12 | §12 | Governance Under Stewardship Discipline | B |
| §13 | §13 | Shared-System Capacity | B |
| §9 | §14 | Market Structure | B |

---

## 3. Subsection renumber

| Old | New |
|-----|-----|
| §14.1–§14.3 | §14.1–§14.3 |
| §14.1–§14.2 | §14.1–§14.2 |
| §14.1–§14.4 (+ §14.4.x) | §14.1–§14.4 (+ §14.4.x) |
| §14.1 | §14.1 |
| §14.1–§14.4 | §14.1–§14.4 |
| §14.1.1–§14.1.4 | §14.1.1–§14.1.4 |
| §14.2.1–§14.2.2 | §14.2.1–§14.2.2 |
| §14.3.1–§14.3.2 | §14.3.1–§14.3.2 |
| Chapter One §6.4.1–Chapter One §6.4.2 | Chapter One §6.4.1–Chapter One §6.4.2 |
| §11.1–§11.2 | §11.1–§11.2 |
| §11.1.1–§11.1.5 | §11.1.1–§11.1.5 |
| §11.1–§11.4 | §11.1–§11.4 |
| §12.1–§12.4 (+ §12.3.x) | §12.1–§12.4 (+ §12.3.x) |
| §13.1–§13.2 | §13.1–§13.2 |
| §14.1–§14.3 (+ §14.3.3) | §14.1–§14.3 (+ §14.3.3) |

---

## 4. Primary anchor migrations (old → new canonical)

| Old anchor | New anchor |
|------------|------------|
| `#14-constitutional-interpretation` | `#14-constitutional-interpretation` |
| `#81-definitional-layer-and-required-disciplines` | `#81-definitional-layer-and-required-disciplines` |
| `#82-ambiguity-resolution` | `#82-ambiguity-resolution` |
| `#83-conflict-resolution-procedure` | `#83-conflict-resolution-procedure` |
| `#14-foundational-objective-wellbeing` | `#14-foundational-objective-wellbeing` |
| `#31-safety-harm-constraint` | `#31-safety-harm-constraint` |
| `#32-truth-epistemic-integrity-constraint` | `#32-truth-epistemic-integrity-constraint` |
| `#3-system-stability-enabler-trust-coordination-integrity` | `#3-system-stability-enabler-trust-coordination-integrity` |
| `#3-interaction-and-conflict-resolution` | `#3-interaction-and-conflict-resolution` |
| `#611-proportionality` | `#611-proportionality` |
| `#641-rights-collision-decision-test` | `#641-rights-collision-decision-test` |
| `#632-time-consistency-constraint` | `#632-time-consistency-constraint` |
| `#141-required-evaluation-factors` | `#141-required-evaluation-factors` |
| `#5-freedom-bounded-agency` | `#5-freedom-bounded-agency` |
| `#7-prohibition-on-absolute-override` | `#7-prohibition-on-absolute-override` |
| `#3-integrated-application` | `#3-integrated-application` |
| `#9-stewardship-and-distributed-understanding` | `#9-stewardship-and-distributed-understanding` |
| `#10-market-structure` | `#10-market-structure` |
| `#1433-ceiling-crossing-rebuttal-and-remedies` | `#1433-ceiling-crossing-rebuttal-and-remedies` |

**Legacy rule:** retain every superseded anchor as empty `<a id="…"></a>` stub for one edition cycle in Part A or Part B redirect blocks.

---

## 5. Migration script

`tools/ch1_integration_relocation.py` — physical cut, renumber, corpus-wide link pass, legacy stubs.

---

## 6. Post-migration prose fixes

- Part A §1: Interaction precedence cite → §14
- Part A §14.1: Interaction / rights-collision → Part A §14
- Part A §14: forward refs to Part B §§11–14
- Part B §14: downstream Interaction → Part A §14
- Vocabulary reference block → Part A tail (after §14)
