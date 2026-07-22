# Chapter Eight — nine-slot standing score scale (adopted implementation)

**Status:** Adopted implementation (non-core). **Authoritative** meaning remains in [Chapter Eight](../core_08-08_standing_assessment.md) and [Chapter Nine](../core_09-09_standing_integration.md). Separate contribution and violation standing records use the same [§7 unified proportional LEQU scale](../core_08-08_standing_assessment.md#7-unified-proportional-lequ-scale): nine impact slots, a **5x** progression, and **s = 7 = 1 LEQU**. The axes remain separate and may not offset.

**Slot groups and display roles (both axes).** The Contribution Axis retains its four constitutional bands. The Violation Axis uses neutral impact labels on the same LEQU bands. Conduct character and any Chapter Ten anti-constitutional designation are separate fields, not slot inputs. Older tranche and violation-character keys remain legacy shorthand only.

**Sub-tier** keys and display. The stable interchange key remains **`minor`** | **`mid`** | **`major`** for compatibility. Violation display labels are **Minimal**, **Limited**, **Material**, **Significant**, **Major**, **Severe**, **Serious**, **Grave**, and **Catastrophic Constitutional Impact**.

**Constitutional guardrails (summary)**

- **Verified inputs only** (demonstrable Contribution Axis; [verified violation findings](../core_05defs_accountability.md#verified-violation-findings) for the Violation Axis) per [Verified inputs for standing](../core_08-08_standing_assessment.md#verified-inputs-for-standing).
- **Constitutional-outcome baseline controls.** Both axes use the unified Chapter Eight thresholds. Numeric estimates must not count raw efficiency, output, prestige, wealth, utilization, burden shifting, allegations, or disfavored status as impact.
- **Recency and currentness** apply only at **Question 3** as gate/readiness inputs under [Chapter Nine §6.1](../core_09-09_standing_integration.md#61-recency-and-currentness). They must not alter a Chapter Eight contribution standing record, Contribution Axis slot, LEQU measurement, descriptor, or historical recognition. Any stored recency-weighted `C*` value is legacy interoperability data only and must not derive a slot.
- **Unresolved** violation findings are **not** time-discounted for standing integration.
- **Do not** net contribution against violation; **do not** **average** or **substitute** axes. Decide violation remedy, correction, and locks before contribution currentness and competency bars and clearances, per [Chapter Nine §2](../core_09-09_standing_integration.md#2-integration-record-and-decision-order). An applicable lock controls.

**References:** [corpus_systems.md](../corpus_systems.md) (standing composites), [schemas/ch06_assessment.schema.json](schemas/ch06_assessment.schema.json) (optional `nine_slot` fields), [ch06_nine_slot_constants.json](ch06_nine_slot_constants.json) (precomputed table).

---

## 1. Structure (index `s` = 1…9)

| `s` | Contribution primary band | Contribution Axis display label | Violation Axis display label |
| ---: | --- | --- | --- |
| 1 | **C-BL** / Baseline contribution | **Basic Baseline Contribution** | **Minimal Constitutional Impact** |
| 2 | **C-BL** / Baseline contribution | **Strengthened Baseline Contribution** | **Limited Constitutional Impact** |
| 3 | **C-PC** / Positive contribution | **Verified Positive Contribution** | **Material Constitutional Impact** |
| 4 | **C-PC** / Positive contribution | **Material Positive Contribution** | **Significant Constitutional Impact** |
| 5 | **C-SP** / Stewardship-positive contribution | **Established Stewardship-Positive Contribution** | **Major Constitutional Impact** |
| 6 | **C-SP** / Stewardship-positive contribution | **Major Stewardship-Positive Contribution** | **Severe Constitutional Impact** |
| 7 | **C-CH** / Champion contribution | **Recognized Champion** | **Serious Constitutional Impact** |
| 8 | **C-CH** / Champion contribution | **Distinguished Champion** | **Grave Constitutional Impact** |
| 9 | **C-CH** / Champion contribution | **Exemplary Champion** | **Catastrophic Constitutional Impact** |

**Category** interchange key may be `I` | `II` | `III` (Roman) or `1` | `2` | `3` in existing data. In current constitutional presentation, those keys are legacy implementation grouping helpers only. The four-band Contribution Axis columns above are the constitutional grouping structure; storage and interchange keep category, sub-tier key, primary band, and display fields separate as below.

**Sub_tier** (interchange key) is always `minor` | `mid` | `major`. Use **`sub_tier_display`** in [ch06_nine_slot_constants.json](ch06_nine_slot_constants.json) for per-axis display. These keys do not encode impact character.

---

## 2. Shared LEQU impact thresholds

Let `x` be the absolute integrated verified constitutional benefit or loss in LEQU on the axis being measured:

\[
T(1)=0,\qquad T(s)=5^{\,s-7}\text{ LEQU for }s\in\{2,\dots,9\}
\]

Assign the highest `s` for which `x ≥ T(s)`. Equivalently, each slot below `s = 9` ends at the next threshold. The same thresholds apply to both axes. Proportionality determines the integrated LEQU estimate; conduct character does not adjust the slot.

| `s` | LEQU band |
| ---: | --- |
| 1 | `0 ≤ x < 0.00032` |
| 2 | `0.00032 ≤ x < 0.0016` |
| 3 | `0.0016 ≤ x < 0.008` |
| 4 | `0.008 ≤ x < 0.04` |
| 5 | `0.04 ≤ x < 0.2` |
| 6 | `0.2 ≤ x < 1` |
| 7 | `1 ≤ x < 5` |
| 8 | `5 ≤ x < 25` |
| 9 | `x ≥ 25` |

**No character multiplier.** Negligence, concealment, coercion, violence, recurrence, and intent remain separately recorded. They may affect safeguards, attribution, remedy, or Chapter Ten designation, but they do not multiply `x`.

Legacy **V-FN**, **V-RSN**, **V-CSN**, **V-DHN**, **V-AN**, **V-CPP**, **V-CGN**, and **V-CN** values describe former character-based mappings only. They must not derive a slot in new records. New records store the numeric violation slot and neutral impact label directly.

Chapter Ten may attach a corresponding anti-constitutional-misconduct designation to an existing `s` = 7–9 violation; it does not assign or alter that slot.

---

## 3. Contribution measurement and baseline requirements

Let **`C_measure`** be the Chapter Eight integrated verified contribution benefit in **LEQU**, without Chapter Nine recency or currentness adjustment. Let **`C\_unit` > 0** be a display scalar, with default **`C_unit = 1 LEQU`**. Existing fields or records named **`C*`** remain readable for interoperability, but if they contain recency weighting they are legacy analytics only and must not derive, raise, or lower a Chapter Eight slot.

`C_measure` units must be calibrated to constitutional-outcome benefit under core **Chapter Eight §§4 and 5.2**. **1 LEQU** means one substrate-agnostic full-life-equivalent constitutional benefit. An implementation may use a current ordinary human lifespan as a biological-human calibration example, but the operative benchmark is the substrate-agnostic **full-life-equivalent constitutional benefit** stated in the core. Claims based on efficiency, burden reduction, productive capacity, or innovation must be discounted or rejected when they depend on rights-floor narrowing, Safety or Truth degradation, discriminatory burden shifting, ecological depletion, opacity, capture, or loss of contestability.

**Minimum** **`C_measure`** to qualify for at least slot `s` follows the shared `T(s)` formula above:

\[
C_{\min}(1) = 0
\]

\[
C_{\min}(s) = C_{\text{unit}} \cdot 5^{\,s-7} \quad \text{for } s \in \{2,\dots,9\}
\]

This anchors **s = 7** at **1 LEQU** and applies a **5x** multiplier per slot on both axes.

| `s` | `C_min(s) / C_unit` (LEQU, default) | 80-year calibration example |
| --- | ---: | ---: |
| 1 | 0 | 0 years |
| 2 | 0.00032 | 9.3 days |
| 3 | 0.0016 | 46.7 days |
| 4 | 0.008 | 0.64 years |
| 5 | 0.04 | 3.2 years |
| 6 | 0.2 | 16 years |
| 7 | 1 | 80 years |
| 8 | 5 | 400 years |
| 9 | 25 | 2,000 years |

**Contribution requirements.** `C_measure` supplies the numeric candidate impact band, while contribution recognition also requires the applicable baseline-state, traceability, non-externalization, and constitutional-alignment findings in core **Chapter Eight §7**. No numeric threshold turns constitutionally defeated output into contribution. Chapter Nine currentness affects only a named gate or readiness decision after violation consequences are decided.

**Default nest** **of** **Chapter Eight** **Contribution Axis** **primary** **bands** (four bands) **into** **slot** **ranges**:

| Primary band | Slot range (inclusive) |
| --- | ---: |
| **C-BL** | 1–2 |
| **C-PC** | 3–4 |
| **C-SP** | 5–6 |
| **C-CH** | 7–9 |

A **record** that **only** has **primary** **band** **typing** may set **`nine_slot.contribution_slot`** to the **top** of the **band**’s **range** **only** **if** neither a `C_measure` candidate threshold nor finer core-criteria assignment is available. Where unweighted `C_measure` is available, it constrains the numeric candidate but does not replace core **Chapter Eight §7** criteria. A legacy recency-weighted `C*` value cannot constrain or derive the slot.

---

## 4. No single net score

Implementations may publish pairs `(C_measure, L*)`, where `L*` is verified violation loss in LEQU. They must not define standing as `C_measure - L*` or reconcile the axes into one gating number. In Question 3 processing, violation consequences are recorded first; contribution currentness and competency bars and clearances are evaluated only for pathways not blocked by a lock.

---

## 5. File and schema interop

- [ch06_nine_slot_constants.json](ch06_nine_slot_constants.json) — one JSON object per slot with shared LEQU lower bounds, neutral displays, and legacy-compatible helper fields.
- [schemas/ch06_assessment.schema.json](schemas/ch06_assessment.schema.json) — optional **`nine_slot`** on **assessment** snapshots; **unchanged** **Contribution Axis** / **Violation Axis** **enum** **fields** **remain** **required** **where** **already** **required** **for** **portability**.
