# Chapter Six — nine-slot standing score scale (adopted implementation)

**Status:** Adopted implementation (non-core). **Authoritative** constitutional meaning for **contribution state**, **violation nature**, and **standing** remains in [core_06-06_standing_assessment.md](../core_06-06_standing_assessment.md) and [core_07-07_standing_integration.md](../core_07-07_standing_integration.md) (binding core). Standing classification uses axis-pure **contribution standing records** and **violation standing records** under core [§2.1](../core_06-06_standing_assessment.md#21-standing-records-as-the-unit-of-application), with related-record cross-references under [§2.3.1](../core_06-06_standing_assessment.md#231-related-record-cross-references). The default **slot** **nest** of implementation contribution keys to **s**, the default **1:1** **V-** to **s** **map** (through **V-CN**; **Violation** **Axis** **s** 8-9 **reserved** in the default map), and the **constitutional-outcome baseline** for Contribution Axis and Violation Axis slot movement are stated in the core [§3 — Slot grammar and display labels](../core_06-06_standing_assessment.md#31-slot-grammar-and-display-labels) (**Table** **1** = slot display labels), [§4 — LEQU baseline](../core_06-06_standing_assessment.md#32-constitutional-outcome-baseline-for-slots) ([§4.1](../core_06-06_standing_assessment.md#41-lequ-contribution-calibration) contribution · [§4.2](../core_06-06_standing_assessment.md#42-lequ-violation-calibration) violation), and [§5 — Primary category defaults](../core_06-06_standing_assessment.md#33-primary-category-defaults-and-lequ-slot-baseline) ([§5.1](../core_06-06_standing_assessment.md#51-contribution-axis-bands-and-table-2) **Table** **2** · [§5.2](../core_06-06_standing_assessment.md#34-violation-axis-rules-violation-nature-adverse-findings-and-severity) operative severity ladder). This file specifies a **numeric interoperable layer**: nine slots on each axis, with **Lifespan Equivalent Unit** (**LEQU**) contribution thresholds using a **5x** slot multiplier anchored at **s = 7**. It **must not** replace the constitutional-outcome baseline, **joint assessment**, **highest applicable** non-compliance, or the **no-offset / no-netting** rules in **Chapter Six** **sections 2.1–2.2, 4–5** and **Chapter Seven sections 4.1–4.3**.

**Slot groups and display roles (both axes).** The core model presents a four-band constitutional grouping for the Contribution Axis: **Baseline contribution** (`s = 1–2`), **Positive contribution** (`s = 3–4`), **Stewardship-positive contribution** (`s = 5–6`), and **Champion contribution** (`s = 7–9`). The Violation Axis remains a separate slot display scale under Chapter Six section 6.2 and Chapter Eight. Chapter Seven section 4.3 later groups verified Violation Axis slots for standing integration. The older three-tranche display roles remain legacy shorthand only. Existing implementation fields named **`category_tranche_display`** and **`category_tranche_role_display`** are retained as legacy-compatible display helpers; they must not be treated as independent constitutional categories and must not substitute for the **C-** primary bands or **V-** primary names in the ladder.

**Sub-tier** keys and display. The sub-tier **interchange** key is always **`minor`** | **`mid`** | **`major`** (field **`sub_tier`**) for legacy compatibility. On the Contribution Axis, display labels are **basic baseline contribution**, **strengthened baseline contribution**, **verified positive contribution**, **material positive contribution**, **established stewardship-positive contribution**, **major stewardship-positive contribution**, **recognized champion**, **distinguished champion**, and **exemplary champion**. On the Violation Axis, display labels follow the core Table 1 names: **formal**, **remedial substantive**, **significant substantive**, **duty-based or negligent-harm**, **aggravated**, **coercive or punitive-process**, **Serious**, **Grave**, and **Pernicious** while the stable interchange key remains **minor** / **mid** / **major**.

**Constitutional guardrails (summary)**

- **Verified inputs only** (demonstrable Contribution Axis; [verified violation findings](../core_05a_accountability_definitions.md#verified-violation-findings) for the Violation Axis) per [Verified inputs for standing](../core_06-06_standing_assessment.md#verified-inputs-for-standing).
- **Constitutional-outcome baseline controls.** Contribution and Violation slot movement are anchored in [Chapter Six §4](../core_06-06_standing_assessment.md#32-constitutional-outcome-baseline-for-slots), including the **1 LEQU** full-life-equivalent constitutional-benefit threshold for Contribution Axis **s = 7** and the full-life-equivalent constitutional-loss threshold for Violation Axis **s = 7**. Numeric LEQU credit and violation weights are implementation aids only; they must not count raw efficiency, output, prestige, wealth, utilization, burden shifting, allegations, or disfavored status as classification grounds.
- **Recency** applies **only** to **contribution** credit expressed in LEQU, per [contribution recency weighting](../core_07-07_standing_integration.md#contribution-recency-weighting) (`w(d)`, half-life ten years, no floor). Compute **`C*`** = sum of (credit × `w(d)`) per unit before slot assignment.
- **Unresolved** violation findings are **not** time-discounted for standing integration.
- **Do not** net **`C*`** against **`V*`**; **do not** **average** or **substitute** axes. **Violation-linked constraints** **must** **dominate** **contribution** **upside** where both apply, per [Chapter Seven section 4.1](../core_07-07_standing_integration.md#38-standing-integration-contribution-and-violation-nature).

**References:** [corpus_systems.md](../corpus_systems.md) (standing composites), [schemas/ch06_assessment.schema.json](schemas/ch06_assessment.schema.json) (optional `nine_slot` fields), [ch06_nine_slot_constants.json](ch06_nine_slot_constants.json) (precomputed table).

---

## 1. Structure (index `s` = 1…9)

| `s` | Contribution primary band | Contribution Axis display label | Violation Axis display label |
| ---: | --- | --- | --- |
| 1 | **C-BL** / Baseline contribution | **basic baseline contribution** | **formal** *non-compliance finding* |
| 2 | **C-BL** / Baseline contribution | **strengthened baseline contribution** | **remedial substantive** *non-compliance finding* |
| 3 | **C-PC** / Positive contribution | **verified positive contribution** | **significant substantive** *violation finding* |
| 4 | **C-PC** / Positive contribution | **material positive contribution** | **duty-based or negligent-harm** *violation finding* |
| 5 | **C-SP** / Stewardship-positive contribution | **established stewardship-positive contribution** | **aggravated** *violation finding* |
| 6 | **C-SP** / Stewardship-positive contribution | **major stewardship-positive contribution** | **coercive or punitive-process** *violation finding* |
| 7 | **C-CH** / Champion contribution | **recognized** *champion* | **Serious** *anti-constitutional misconduct* |
| 8 | **C-CH** / Champion contribution | **distinguished** *champion* | **Grave** *anti-constitutional misconduct* |
| 9 | **C-CH** / Champion contribution | **exemplary** *champion* | **Pernicious** *anti-constitutional misconduct* |

**Category** interchange key may be `I` | `II` | `III` (Roman) or `1` | `2` | `3` in existing data. In current constitutional presentation, those keys are legacy implementation grouping helpers only. The four-band Contribution Axis columns above are the constitutional grouping structure; storage and interchange keep category, sub-tier key, primary band, and display fields separate as below.

**Sub_tier** (interchange key) is always `minor` | `mid` | `major`. Use **`sub_tier_display`** in [ch06_nine_slot_constants.json](ch06_nine_slot_constants.json) for per-axis sub-tier display. Contribution Axis display uses the band-step labels shown above for **s = 1 through s = 6** and **recognized** / **distinguished** / **exemplary** for **s = 7 through s = 9**. Violation Axis display uses the core Table 1 labels: **formal** / **remedial substantive**, **significant substantive** / **duty-based or negligent-harm**, **aggravated** / **coercive or punitive-process**, and **Serious** / **Grave** / **Pernicious**.

---

## 2. Violation side — per-finding weight `V(s)`

For an event classified to **slot** `s` (1 through 9) through verified violation findings:

\[
V(s) = 3^{\,s-1}
\]

`V(s)` weights are ordinal analytics for verified constitutional loss under core **§4**. Violation Axis **s = 7** is anchored by at least one full-life-equivalent constitutional benefit destroyed, wasted, wrongfully consumed, or foreclosed, or by comparable critical constitutional harm. The numeric weight does not replace **section 5.2** severity typing, **Chapter Eight** final top-slot assignment where applicable, individualized evidence, LEQU-equivalent loss calibration where adopted, or process requirements.

| `s` | `V(s)` |
| --- | ---: |
| 1 | 1 |
| 2 | 3 |
| 3 | 9 |
| 4 | 27 |
| 5 | 81 |
| 6 | 243 |
| 7 | 729 |
| 8 | 2,187 |
| 9 | 6,561 |

**Aggregate (optional, reporting only).** A **sum of weights** over **multiple** open findings (each with its own `s` and `V(s)`) may be reported as `V_star_sum` for analytics. **Standing integration** in law still turns on **primary** **Violation Axis** typing and **highest applicable** **severity**; do not treat `V_star_sum` as a substitute for **Chapter Seven subsection 4.2** classification.

**Default map from Chapter Six** **Violation Axis** **ladder** **labels** to **slot** `s` (when no finer nine-slot label set exists): **1:1** — **V-FN** → 1, **V-RSN** → 2, **V-CSN** → 3, **V-DHN** → 4, **V-AN** → 5, **V-CPP** → 6, **V-CN** → 7. **V-CSN** is retained as the stable interchange key for **Significant Substantive Non-Compliance**. **Slots 8–9** are not free implementation slots: they are available only where a conforming Chapter Eight or other adopted authority supplies a valid grave / pernicious top-slot assignment or a compatible registered sub-split. If no such authority exists, do not assign **s = 8** or **s = 9**.

Legacy records with **V-CGN** **must** map to **V-CPP** / slot **6** per Chapter Six **interoperable shorthand** note.

---

## 3. Contribution side — cumulative `C*` LEQU thresholds

Let **`C*`** = **recency-weighted** **sum** of **verified** **contribution** **credit** in **LEQU** (disclosed **per** **adoption**; **per**-unit `w(d)` as in Chapter Seven **4.1**). Let **`C\_unit` > 0** be a display scalar, with default **`C_unit = 1 LEQU`**.

`C*` units must be calibrated to constitutional-outcome benefit under core **§4.2**. **1 LEQU** means one substrate-agnostic full-life-equivalent constitutional benefit. An implementation may use a current ordinary human lifespan as a biological-human calibration example, but the operative benchmark is the substrate-agnostic **full-life-equivalent constitutional benefit** stated in the core. Claims based on efficiency, burden reduction, productive capacity, or innovation must be discounted or rejected when they depend on rights-floor narrowing, Safety or Truth degradation, discriminatory burden shifting, ecological depletion, opacity, capture, or loss of contestability.

**Minimum** **`C*`** to **qualify** for **at least** **slot** `s`:

\[
C_{\min}(1) = 0
\]

\[
C_{\min}(s) = C_{\text{unit}} \cdot 5^{\,s-7} \quad \text{for } s \in \{2,\dots,9\}
\]

This anchors **s = 7** at **1 LEQU** and applies a **5x** multiplier per slot. For example, **s = 8** requires **5 LEQU**. With an 80-year biological-human calibration example, **s = 6** requires **0.2 LEQU**, or **16 years** of full-life-equivalent constitutional benefit.

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

**Slot assignment from `C*`.** The **realized** **contribution** **slot** is the **largest** `s` in **1…9** such that **`C*`** ≥ `C_min(s)`.

**Default nest** **of** **Chapter Six** **Contribution Axis** **primary** **bands** (four bands) **into** **slot** **ranges**:

| Primary band | Slot range (inclusive) |
| --- | ---: |
| **C-BL** | 1–2 |
| **C-PC** | 3–4 |
| **C-SP** | 5–6 |
| **C-CH** | 7–9 |

A **record** that **only** has **primary** **band** **typing** may set **`nine_slot.contribution_slot`** to the **top** of the **band**’s **range** **only** **if** `C*`-based slot is **unavailable**; if **`C*`** is **available**, the **`C*`** **rule** **wins** **for** **the** **numeric** **grid**.

---

## 4. No single net score

Implementations **may** **publish** **pairs** `(C*, V(s))` or `(C*, V_star_sum)` for **transparency**; they **must not** **define** **standing** **as** **C* minus V** or **reconcile** **axes** **into** **one** **number** for **gating** **that** **contradicts** **Chapter Six** **§2.2** and **§5**.

---

## 5. File and schema interop

- [ch06_nine_slot_constants.json](ch06_nine_slot_constants.json) — one JSON object per slot with **precomputed** `c_min_over_c_unit`, `v_weight`, legacy-compatible **category**, interchange key **`sub_tier`**, **`sub_tier_display`**, and display-role helper fields retained for implementations that already consume them.
- [schemas/ch06_assessment.schema.json](schemas/ch06_assessment.schema.json) — optional **`nine_slot`** on **assessment** snapshots; **unchanged** **Contribution Axis** / **Violation Axis** **enum** **fields** **remain** **required** **where** **already** **required** **for** **portability**.
