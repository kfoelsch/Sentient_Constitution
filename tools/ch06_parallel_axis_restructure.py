#!/usr/bin/env python3
"""Restructure Chapter Six: §4 LEQU both axes (4.1/4.2); §5 classification both axes (5.1/5.2); drop §6.

ONE-TIME MIGRATION — do not re-run after cut is applied. Global ``section 5`` / ``section 6``
replacements corrupt other chapters' internal numbering. Use ``ch06_fix_crossref_corruption.py``
for targeted repairs instead.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CH06 = ROOT / "core_06-06_standing_assessment.md"

SECTION_4_START = "<a id=\"32-constitutional-outcome-baseline-for-slots\"></a>"
CONTINUATION = "\n\n---\n\n**Continuation.**"

NEW_SECTIONS_4_5 = r'''### 4. LEQU baseline — measuring impact in lifetime-equivalent units

<a id="32-constitutional-outcome-baseline-for-slots"></a>

*In plain terms: To decide which slot someone's contribution or violation belongs in, we measure impact using "LEQU" — Lifespan Equivalent Unit. One LEQU roughly equals saving or destroying one sentient's entire lifetime of wellbeing. This isn't about counting bodies or dollars; it's about understanding whether an action meaningfully changed our constitutional community's wellbeing. The same unit works for any sentient being, human or otherwise.*

The slot scale measures constitutional outcome magnitude and character. On the Contribution Axis, it measures verified constitutional benefit, not raw output, prestige, wealth, utilization, speed, or institutional scale. On the Violation Axis, it measures verified constitutional loss, harm, waste, foreclosure, or danger, not disfavored status, allegations, or moral dislike alone.

For this section, a **full-life-equivalent constitutional benefit** means verified benefit comparable to preserving, restoring, or freeing one full sentient lifespan of non-trivial, rights-consistent wellbeing. A **full-life-equivalent constitutional loss** means verified harm, waste, destruction, foreclosure, deprivation, or risk realization comparable to destroying, wrongfully consuming, or preventing one full-life-equivalent constitutional benefit. A **Lifespan Equivalent Unit** (**LEQU**) is the shorthand unit for that full-life-equivalent constitutional benefit or loss when adopted implementation needs a numeric calibration. The unit is substrate-agnostic. A current adopter may use an ordinary human lifespan as a calibration example for biological-human contexts, but the binding baseline is sentient and constitutional, not species-bound.

**Important limits on using LEQU:**

- **Not a net-score rule.** You cannot "cancel out" violations with contributions or vice versa. Each axis stands alone.
- **Not a mandatory human-life metric.** The LEQU is sentient-generic; it applies to any conscious being, not just humans.
- **Not an accusation metric.** Allegations, intake tags, routing decisions, reputation, disfavored status, or moral dislike do not supply Contribution Axis benefit or Violation Axis severity without verified inputs under **sections 2.3.2**, **5.1**, and **5.2**.
- **Not a license to trade rights.** Claims framed as efficiency, productive capacity, innovation, burden reduction, security, retaliation, emergency response, or institutional necessity must be discounted or rejected where they depend on coercion, discriminatory burden shifting, ecological depletion, hidden unpaid work, avoidable opacity, Rights-Floor narrowing, capture, misleading proxies, loss of contestability, or unreviewable aggregation.

<a id="41-lequ-contribution-calibration"></a>

#### 4.1 Contribution calibration

**Examples of what counts toward contribution (slot movement up):**

Each row ties verified contribution benefit to the [Constitutional Triad](core_00_preamble.md#constitutional-triad) and [Two Constitutional Aims](core_01_a_values_principles.md#two-constitutional-aims). **Triad leg(s)** name the dominant governance hook; **Primary aim(s)** name the dominant constitutional objective. Full slot assignment still requires **sections 2** and **5.1**.

| Type of Benefit | What It Looks Like | Triad leg(s) | Primary aim(s) |
| --- | --- | --- | --- |
| Survival & bodily maintenance | Ensuring someone has food, shelter, medical care, or safety | **Participation**, **Oversight** | **Flourishing** |
| Caretaking & teaching | Raising children, caring for elders, educating others | **Participation**, **Oversight** | **Flourishing**, **Continuity** |
| Trauma resolution | Helping someone recover from psychological harm that was blocking their wellbeing | **Participation**, **Accountability** | **Flourishing** |
| Removing severe burdens | Eliminating crushing debt, exploitative working conditions, or systemic barriers | **Participation**, **Oversight** | **Flourishing** |
| Restoring agency | Enabling someone to make meaningful choices about their own life | **Participation** | **Flourishing** |
| Expanding productive capacity | Creating tools, infrastructure, or opportunities that let others thrive independently | **Oversight**, **Participation** | **Flourishing**, **Continuity** |
| Improving time efficiency | Reducing avoidable waiting, administrative friction, or coordination overhead so sentient beings regain usable time for care, rest, agency, learning, or rights-consistent work | **Oversight**, **Participation** | **Flourishing** |
| Reducing ecological or infrastructure risk | Preventing environmental collapse or critical system failures | **Oversight**, **Accountability** | **Continuity**, **Flourishing** |
| Strengthening safety, truth, auditability, or challenge capacity | Building institutions that protect rights and hold power accountable | **Oversight**, **Participation**, **Accountability** | **Flourishing**, **Continuity** |

The claimed benefit counts only to the extent it remains traceable, non-externalized, and consistent with Safety, Truth, dignity, equal standing, substantive fairness, ecological integrity, intergenerational responsibility, auditability, and contestability. Externalized harms, coercive dependencies, Rights-Floor narrowing, or concealed burdens limit what may count as verified Contribution Axis benefit; they do not offset, reduce, or cure separate Violation Axis findings.

**How slots map to LEQU scale on the contribution side:**

Same [Constitutional Triad](core_00_preamble.md#constitutional-triad) and [Two Constitutional Aims](core_01_a_values_principles.md#two-constitutional-aims) discipline as the examples table above. Higher slots add **Continuity** and broader Triad legs as verified benefit scales across people, time, and institutions.

| `s` | Contribution Level | Roughly Equivalent To... | Triad leg(s) | Primary aim(s) |
| ---: | --- | --- | --- | --- |
| 1 | **Baseline contribution** | Meeting constitutional floor without violations | **Oversight**, **Participation** | **Flourishing** |
| 2 | **Strengthened baseline contribution** | Reliably exceeding the floor in a bounded, demonstrable way | **Oversight**, **Participation** | **Flourishing** |
| 3 | **Verified positive contribution** | Helping one sentient modestly beyond baseline | **Oversight**, **Participation** | **Flourishing** |
| 4 | **Material positive contribution** | Helping a small group or single community noticeably | **Oversight**, **Participation** | **Flourishing** |
| 5 | **Established stewardship-positive contribution** | Creating lasting benefit in a defined domain | **Oversight**, **Participation** | **Flourishing**, **Continuity** |
| 6 | **Major stewardship-positive contribution** | Approaching one LEQU in impact, or enabling many others to meet obligations | **Oversight**, **Participation**, **Accountability** | **Flourishing**, **Continuity** |
| 7 | **Recognized champion** | **At least one LEQU** — verifiably saved or transformed one lifetime-equivalent | **Oversight**, **Participation**, **Accountability** | **Flourishing**, **Continuity** |
| 8 | **Distinguished champion** | **Multiple LEQUs** — lasting institutional repair or prevention that outlives the actors | **Oversight**, **Participation**, **Accountability** | **Flourishing**, **Continuity** |
| 9 | **Exemplary champion** | **Rare, wide-scope gains** — intergenerational, ecosystem, or civilization-level benefit | **Oversight**, **Participation**, **Accountability** | **Continuity**, **Flourishing** |

<a id="42-lequ-violation-calibration"></a>

#### 4.2 Violation calibration

**Examples of what counts toward violation severity (slot movement up):**

Each row ties verified constitutional loss to the [Constitutional Triad](core_00_preamble.md#constitutional-triad) and [Two Constitutional Aims](core_01_a_values_principles.md#two-constitutional-aims). Full operative severity assignment still requires **sections 2** and **5.2**.

| Type of Loss or Danger | What It Looks Like | Triad leg(s) | Primary aim(s) |
| --- | --- | --- | --- |
| Survival or bodily-maintenance deprivation | Avoidable death, denied care, unsafe conditions, or material survival deprivation | **Accountability**, **Participation** | **Flourishing** |
| Severe avoidable burden | Crushing, imposed, or systematically shifted burdens that materially impair wellbeing or agency | **Accountability**, **Participation** | **Flourishing** |
| Coercive agency loss | Coercion, manipulation, credible threat, confinement, or liberty danger | **Accountability**, **Participation** | **Flourishing** |
| Rights-Floor defeat | Material violation of non-negotiable constitutional floors, supremacy, or challenge-and-remedy access | **Accountability**, **Oversight** | **Flourishing**, **Continuity** |
| Ecological or infrastructure damage | Damage to environmental, institutional, or technical conditions needed for constitutional wellbeing | **Accountability**, **Oversight** | **Continuity**, **Flourishing** |
| Destroyed productive capacity | Foreclosure of tools, capabilities, relationships, or resources needed for independent thriving | **Accountability** | **Flourishing** |
| Degraded Safety, Truth, or auditability | Concealment, misinformation, broken records, inaccessible challenge paths, or unreviewable aggregation | **Oversight**, **Accountability** | **Flourishing**, **Continuity** |
| System capture or dependency abuse | Structural enablement, dependency-asymmetry abuse, anti-evasion design, or capture of accountability pathways | **Accountability**, **Participation** | **Continuity**, **Flourishing** |

The claimed violation severity counts only to the extent it rests on verified violation findings that remain traceable, bounded, auditable, and contestable under **Chapters Two through Four**. Allegations, provisional tags, forum-phase narratives, and intake-only labels may support routing and triage under [Chapter Nine](core_09-09_forum.md#chapter-nine-forums-and-jurisdiction). They do not supply **violation nature** for standing unless they produce auditable, contestable findings. Positive contribution does not offset, average down, excuse, cure, or relabel adverse findings.

**How slots map to LEQU scale on the violation side:**

Same Triad and Aims discipline as the examples table above. Higher slots add **Continuity** emphasis and broader accountability hooks as verified loss scales across people, institutions, and time. Operative criteria for each level are in **section 5.2**; final **Violation Axis** `s` = 7, 8, and 9 assignment remains in **Chapter Eight**.

| `s` | Violation Level | Roughly Equivalent To... | Triad leg(s) | Primary aim(s) |
| ---: | --- | --- | --- | --- |
| 1 | **Formal non-compliance** | Process, records, or challenge-path problems without proven substantive harm | **Oversight**, **Participation** | **Flourishing** |
| 2 | **Remedial substantive non-compliance** | Real harm or rights failure requiring repair, restoration, or civil correction | **Accountability**, **Participation** | **Flourishing** |
| 3 | **Significant substantive non-compliance** | Material constitutional or Rights-Floor violation without aggravated or coercive features | **Accountability**, **Oversight** | **Flourishing**, **Continuity** |
| 4 | **Duty-based or negligent-harm violation** | Preventable harm from unmet duty, foreseeable risk, or neglect where capacity to act existed | **Accountability**, **Oversight** | **Flourishing** |
| 5 | **Aggravated violation** | Repeated, reckless, evasive, concealed, or structurally enabled failure | **Accountability** | **Flourishing**, **Continuity** |
| 6 | **Coercive or safeguard-process violation** | Coercion, liberty threat, or social danger requiring criminal-process or equivalent safeguards | **Accountability**, **Participation** | **Flourishing** |
| 7 | **Serious / critical non-compliance** | **At least one LEQU destroyed** or comparable critical constitutional harm | **Accountability**, **Oversight** | **Continuity**, **Flourishing** |
| 8 | **Grave anti-constitutional misconduct** | **Multiple LEQUs lost** or structural cross-institutional constitutional damage | **Accountability** | **Continuity** |
| 9 | **Pernicious anti-constitutional misconduct** | Worst-case systemic, intergenerational, or civilizational constitutional harm | **Accountability** | **Continuity** |

Adopted implementation may publish calibrated units, evidentiary methods, and examples for full-life-equivalent benefit or loss. Those materials must remain subordinate to this section, **sections 5.1 and 5.2**, **Table 2**, **Chapter One**, and the **Chapter Ten** Rights Floor.


<a id="33-primary-category-defaults-and-lequ-slot-baseline"></a>

### 5. Primary category defaults — Contribution Axis and Violation Axis

*In plain terms: This section translates the abstract nine-slot scale into operative categories on each axis — contribution under **§5.1**, violation under **§5.2** — using the LEQU calibration in **section 4**. The two subsections are parallel; read them side by side, not as a merged score.*

**Primary band keys.** Adopted implementation may use stable **C-** contribution-band interchange keys (**C-BL**, **C-PC**, **C-SP**, **C-CH**) and **V-** violation-label keys for interoperable records. Those keys support storage and exchange; operative meaning remains in this chapter's tables. See [CH06_NINE_SLOT_STANDING_SCALE.md](implementation/CH06_NINE_SLOT_STANDING_SCALE.md).

<a id="51-contribution-axis-bands-and-table-2"></a>

#### 5.1 Contribution Axis — bands and Table 2

**Table 2** connects **Table 1** display labels to operative Contribution Axis rules. Standing records under **sections 2.1** and **2.3** state how those categories have been applied in a particular scope and time.

The **Contribution Axis** is **positive-only**. It classifies verified constitutional benefit, baseline satisfaction, and demonstrable uplift; it does not classify adverse violation findings or non-compliance. Those belong to **violation nature** under **section 5.2** and, where applicable, process / response character under **Chapter Seven section 3**.

**Four primary bands** nest into the slot scale:

- **Baseline contribution** (**C-BL**; `s` = 1–2): required constitutional conditions are met without unresolved material violation under applicable definitions, rights, and evaluation scope; strengthened baseline contribution records bounded, demonstrable reliability above the floor that has not yet become positive contribution.
- **Positive contribution** (**C-PC**; `s` = 3–4): behavior demonstrably improves constitutional outcomes beyond minimum baseline obligations, including measurable reduction of systemic risk, restoration of harmed conditions, strengthened challenge rights, or durable improvement of environmental and informational integrity.
- **Stewardship-positive contribution** (**C-SP**; `s` = 5–6): sustained, verifiable contribution to collective constitutional resilience across system boundaries, including prevention investments, ecosystem-strengthening coordination, and improvements that increase others' ability to meet baseline obligations without dependency abuse.
- **Champion contribution** (**C-CH**; `s` = 7–9): sustained, verifiable stewardship whose scale, durability, or cross-institutional reach materially exceeds the stewardship-positive standard under the same auditability and contestability discipline. It includes durable reduction of systemic dependency or capture risk at material scope, structural repair or prevention that multiple communities or institutions rely on, or demonstrable constitutional-resilience gains that outlast the originating actors.

Column 1 uses the same `s` as **Table 1**. Read each row with **section 3**, **Table 1**, **section 4.1**, and **sections 2.1** and **2.2** for Standing Record requirements. For the Violation Axis display label paired with each `s`, see **Table 1** column 3 and **section 5.2**.


|  `s` | Contribution Axis — what it means in practice |
| ---: | --- |
|    1 | **basic baseline contribution** — You meet the basic constitutional floor for your scope. No major violations hiding under the surface. |
|    2 | **strengthened baseline contribution** — You reliably exceed the minimum floor in a bounded, demonstrable way while remaining within the baseline band. |
|    3 | **verified positive contribution** — You've made a real, demonstrable improvement beyond baseline obligations. |
|    4 | **material positive contribution** — You've delivered material, lasting, or repeated benefits within your scope, though not yet stewardship-positive contribution. |
|    5 | **established stewardship-positive contribution** — You've sustained contribution to collective constitutional resilience across system boundaries. |
|    6 | **major stewardship-positive contribution** — Broad or deeply embedded stewardship that materially improves others' capacity to meet baseline obligations without creating dependency. |
|    7 | **recognized champion** — Recognized stewardship whose scale, durability, or cross-institutional reach materially exceeds the stewardship-positive standard. |
|    8 | **distinguished champion** — Distinguished stewardship with durable cross-institutional reliance, structural repair, or prevention that outlasts you. |
|    9 | **exemplary champion** — Exemplary stewardship producing rare, durable constitutional-resilience gains at the widest material scope. |

Positive contribution may be recorded in a **contribution standing record** while a subject also holds a linked **violation standing record** under **section 5.2**, subject to the no-offset rules in **section 2.2** and **Chapter Seven section 4.2**. Contribution credit under this table does not require formal governance status, salaried office, licensed-program participation, designated filings, or other official-channel pedigree. Peer, neighbor, voluntary, mutual-aid, and other non-institutional stewardship may count when its effects are demonstrable under the same **auditability** and **contestability** discipline applied to institutional contribution.

<details>
<summary><strong><span style="color: #2563eb;">Implementation interop note</span></strong></summary>

> This widget contains implementation-facing interoperability material. It supports the chapter's operative categories; it does not create a parallel category system.

Machine-readable fields for slot display (`sub_tier`, `sub_tier_display`, and related display fields) are defined in [CH06_NINE_SLOT_STANDING_SCALE.md](implementation/CH06_NINE_SLOT_STANDING_SCALE.md) and [ch06_nine_slot_constants.json](implementation/ch06_nine_slot_constants.json). Use them with the four-band default map in **Table 2** above.

Adopted implementation may publish `C*` thresholds, `V(s)` weights, and keyed sub-tier labels. Those helpers must not replace the primary typing in **sections 5.1 and 5.2**, the default maps in **Table 1** and **Table 2**, or the Chapter Eight assignment rules for Violation Axis `s` = 7, 8, and 9, except through a **conforming instrument** change.

</details>

<a id="34-violation-axis-rules-violation-nature-adverse-findings-and-severity"></a>
<a id="52-violation-axis-severity-ladder"></a>
<a id="chapter-six-part-e-accountability-measure"></a>

#### 5.2 Violation Axis — severity ladder and application notes

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [§2](#2-standing-records) (*standing records, verified-input gate, and no-offset bridge*); [§3](#31-slot-grammar-and-display-labels) (*slot grammar and display labels*); [§4.2](#42-lequ-violation-calibration) (*violation LEQU calibration*); [§5.1](#51-contribution-axis-bands-and-table-2) (*Contribution Axis rules and **Table 2***); [Chapter Seven §3.9](core_07-07_standing_integration.md#73-stackable-harm-and-conduct-descriptors-violation-nature-supplement) (*Violation Axis supplements*).
- Downstream: [Chapter Seven §3](core_07-07_standing_integration.md#6-extended-axis-ii-legal-hybrid-duty-and-harm-descriptors) (*process / response character, hybrid, and duty material*); [Chapter Seven §4](core_07-07_standing_integration.md#8-cross-axis-coupling-and-escalation-constraints) (*standing integration and no-netting mechanics*); [Chapter Eight](core_08-08_misconduct.md#chapter-eight-anti-constitutional-misconduct) (*final Violation Axis **s = 7, 8, or 9** anti-constitutional misconduct assignment*).
- Read with: [Supremacy and Enforceability](core_05i_integrative_definitions.md#supremacy-and-enforceability), [Constitutional Constraint Violation](core_05i_integrative_definitions.md#constitutional-constraint-violation), [Harm](core_05a_accountability_definitions.md#harm), and [Materiality Determination](core_05o_oversight_definitions.md#materiality-determination).
- Triad leg(s): **accountability**. Primary aim(s): **Flourishing** and **Continuity**. [material stake](core_00_preamble.md#material-stake) scaling applies to severity and verification burden.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Definitions · Evaluation · Compliance</span></strong></summary>

- [Harm](core_05a_accountability_definitions.md#harm) · [O](core_05a_accountability_definitions.md#harm) · [E](core_05a_accountability_definitions.md#harm-e) · [C](core_05a_accountability_definitions.md#harm-c)
- [Materiality Determination](core_05o_oversight_definitions.md#materiality-determination) · [O](core_05o_oversight_definitions.md#materiality-determination) · [E](core_05o_oversight_definitions.md#materiality-determination-e) · [C](core_05o_oversight_definitions.md#materiality-determination-c)
- [Constitutional Constraint Violation](core_05i_integrative_definitions.md#constitutional-constraint-violation) · [O](core_05i_integrative_definitions.md#constitutional-constraint-violation) · [E](core_05i_integrative_definitions.md#constitutional-constraint-violation-e) · [C](core_05i_integrative_definitions.md#constitutional-constraint-violation-c)
- [Coercion and Manipulation](core_05p_participation_definitions.md#coercion-and-manipulation-constitutional) · [O](core_05p_participation_definitions.md#coercion-and-manipulation-constitutional) · [E](core_05p_participation_definitions.md#coercion-and-manipulation-constitutional-e) · [C](core_05p_participation_definitions.md#coercion-and-manipulation-constitutional-c)
- [Foreseeability Diligence](core_05o_oversight_definitions.md#foreseeability-diligence) · [O](core_05o_oversight_definitions.md#foreseeability-diligence) · [E](core_05o_oversight_definitions.md#foreseeability-diligence-e) · [C](core_05o_oversight_definitions.md#foreseeability-diligence-c)

</details>

<br>

*In plain terms: **Violation nature** is the adverse side of the model. To decide which slot a verified violation belongs in, apply **section 4.2** LEQU calibration on the loss side — roughly, whether conduct impaired, destroyed, wrongfully consumed, or foreclosed constitutional wellbeing. Accusations and routing labels do not count; only verified findings do.*

The slot scale measures verified constitutional loss, harm, waste, foreclosure, or danger, not disfavored status, allegation, retaliation preference, or moral dislike alone. **Violation nature** includes Violation Axis severity under this subsection, process / response character under **Chapter Seven section 3**, and hybrid, duty, diffusion, negligence, and descriptor material where facts warrant. Apply the **full-life-equivalent constitutional loss** definition and **Important limits on using LEQU** in **section 4** to all violation-side calibration.

**Operative Violation Axis severity ladder:**


| `s` | Violation Level | Operative criteria |
| ---: | --- | --- |
| 1 | <a id="41-formal-non-compliance"></a>**Formal Non-Compliance** | Process, records, verification, observability, accessibility, or challenge-path problems without proven substantive harm. Where binding obligations require operational capability, paper claims, unimplemented controls, or unobservable assertions are not enough when verification or challenge is materially impaired. |
| 2 | <a id="42-remedial-substantive-non-compliance"></a>**Remedial Substantive Non-Compliance** | Real-world duty, harm, rights, Ontological (O), Evaluative (E), or Compliance (C) failure requiring repair, restoration, compensation, injunction, or comparable civil correction. This includes direct, indirect, delayed, aggregated, cross-system, psychological, trauma, coercion-related, agency, wellbeing, dignity, or trust-condition harm where material. |
| 3 | <a id="43-constitutional-substantive-non-compliance"></a>**Significant Substantive Non-Compliance** | Material violation of constitutional constraints, Rights Floors, supremacy and enforceability, anti-evasion requirements, or challenge-and-remedy access, before aggravated, coercive or safeguard-process, critical, or final Chapter Eight top-slot criteria are met. |
|    4 | <a id="44-duty-based-or-negligent-harm-violation"></a>**Duty-Based or Negligent-Harm Violation** | Duty, foreseeability, and feasible capacity to prevent, mitigate, supervise, or escalate material harm existed, but preventable harm, risk, inadequate operational care, inadequate supervision, delayed escalation, or neglect is verified. This level may co-occur with other severity levels where their criteria also fit. |
|    5 | <a id="45-aggravated-violation"></a>**Aggravated Violation** | Formal, remedial substantive, significant substantive, or duty-based violation with worsening features such as evasion, concealment, strategic obstruction of audit, dishonest forum disclosure omission, intentional recusal-process failure, repetition after notice, reckless disregard, exploitative incentive design, structural enablement, or material dependency-asymmetry abuse. |
|    6 | <a id="46-coercive-or-safeguard-process-violation"></a>**Coercive or Safeguard-Process Violation** | Culpability, coercion, manipulation, violence, credible threat, liberty-threatening response, or comparable social danger serious enough to require criminal-process or equivalent constitutional protections where coercive or liberty-restricting response is in play. This severity may carry **Chapter Seven section 3.2** coercive or liberty-restricting safeguard character, but severity and process / response character remain separately traceable. |
| 7 | <a id="47-critical-non-compliance"></a>**Serious anti-constitutional misconduct** where Chapter Eight so assigns / **Critical Non-Compliance** | **At least one LEQU destroyed** or comparable critical harm: catastrophic, existential, irreversible, Rights-Floor-defeating, constitution-undermining, large-scale systemic, severe persistent trauma with durable agency impairment, or material violation of non-negotiable floors including Safety, Truth, and dignity-equality protections. Immediate containment and heightened oversight apply. |
| 8 | **Grave anti-constitutional misconduct** | **Multiple LEQUs lost**, structural or cross-institutional constitutional damage, or a final Chapter Eight finding establishing **s = 8** grave anti-constitutional misconduct. |
| 9 | **Pernicious anti-constitutional misconduct** | **Worst-case systemic harm**: rare, intentional, systemic, intergenerational, civilizational, constitution-subverting harm at the widest material scope, or a final Chapter Eight finding establishing **s = 9** pernicious anti-constitutional misconduct. |

This table is the operative Violation Axis severity ladder for Chapter Six. Display labels for each `s` appear in **Table 1** column 3. LEQU calibration for each level appears in **section 4.2**. Final anti-constitutional misconduct assignment for **s = 7**, **s = 8**, and **s = 9** remains in **Chapter Eight**. Process / response character attaches under **Chapter Seven section 3** and does not create a second severity ladder. **Violation standing records** under **§§2.1 and 2.3.2** must identify the finding authority or record basis and review status for the Violation Axis classification.

<a id="48-adjacent-level-application-notes"></a>

**Adjacent-level application.** Apply the highest **section 5.2** level whose criteria fit the verified findings. Formal defects remain at `s` = 1 unless substantive harm, rights burden, or material operational failure is found. Remedial or civil-correction character does not by itself prevent escalation where constitutional floors, supremacy, anti-evasion discipline, aggravating features, coercion, liberty danger, or critical harm are verified.

**Forum disclosure omission and recusal-process impact.** A verified knowing, reckless, or materially dishonest omission from a mandatory forum disclosure required before merits participation, or a verified intentional failure to follow a required recusal process, is a heightened process-integrity violation because it can distort the legality and independence of the adjudicative forum itself. Compared with otherwise similar deception or process violation outside a forum-constitution setting, evaluators must account for the added impact on panel lawfulness, recusal challenge, evidence integrity, remedy timing, backup routing, practical contestability, and public confidence in adjudication. This clause does not bypass the verified-input gate, does not automatically assign a top slot, and does not reduce Chapter Eight safeguards where anti-constitutional misconduct is alleged.

**Boundary with Contribution Axis.** **Violation nature** may co-occur with **positive-only** **contribution state** under **section 5.1**. Adverse **violation** findings are not "negative contribution," and positive contribution does not offset adverse findings.

**Supplements.** Read **Chapter Seven section 2.1** (domain cross-walk), **Chapter Seven section 2.2** (Contribution Axis supplements), **Chapter Seven section 3.9** (Violation Axis supplements), and **Chapter Seven §§3.1–3.8** (process / response character and duty material) with this severity ladder.

**What happens next.** Standing effects are in **Chapter Seven section 1**. Standing integration and no-netting mechanics are in **Chapter Seven section 4** (including standing-orientation by Violation Axis slot at section 4.3). Final top-slot anti-constitutional misconduct assignment is in **Chapter Eight**. Adopted implementation may publish LEQU-equivalent loss calibration only as subordinate support under **section 4.2** and this subsection.
'''


def restructure_ch06() -> None:
    text = CH06.read_text(encoding="utf-8")
    start = text.index(SECTION_4_START)
    # Replace from ### 4 heading (just before anchor) through end of §6
    heading_start = text.rfind("### 4. LEQU baseline", 0, start)
    if heading_start == -1:
        heading_start = start
    end = text.index(CONTINUATION, start)
    text = text[:heading_start] + NEW_SECTIONS_4_5 + text[end:]
    CH06.write_text(text, encoding="utf-8")
    print(f"Restructured {CH06}")


CH7_GUARD = "\u0001CH7SEC6\u0001"
CH9_GUARD = "\u0001CH9SEC6\u0001"
CH8_GUARD = "\u0001CH8SEC6\u0001"
CH11_GUARD = "\u0001CH11SEC6\u0001"
CH5SEC_GUARD = "\u0001CH5SEC\u0001"


def guard_other_chapters(text: str) -> str:
    """Temporarily mask Chapter Six §6 refs that collide with other chapters' §6."""
    text = re.sub(
        r"(\[Chapter Seven §6\]\(core_07-07_standing_integration\.md#[^)]+\))",
        CH7_GUARD + r"\1" + CH7_GUARD,
        text,
    )
    text = re.sub(
        r"(\[Chapter Six §6\]\(core_07-07_standing_integration\.md#[^)]+\))",
        CH7_GUARD + r"\1" + CH7_GUARD,
        text,
    )
    return text


def unguard(text: str) -> str:
    return text.replace(CH7_GUARD, "")


CORPUS_REPLACEMENTS = [
    # Reading order / section spans
    ("classification-layer-sections-3-6", "classification-layer-sections-3-5"),
    ("§§3–6", "§§3–5"),
    ("sections 3–6", "sections 3–5"),
    ("sections 1–6", "sections 1–5"),
    ("§§3–6):", "§§3–5):"),
    # Chapter six trace / orientation
    (
        "*Reading order (classification layer §§3–5):* **[§3](#3-slot-grammar-and-display-labels)** names the shared slot labels (**Table 1**) · **[§4](#32-constitutional-outcome-baseline-for-slots)** calibrates magnitude in LEQU · **[§5](#33-primary-category-defaults-and-lequ-slot-baseline)** classifies verified **contribution state** (**Table 2**) · **[§6](#34-violation-axis-rules-violation-nature-adverse-findings-and-severity)** classifies verified **violation nature**.",
        "*Reading order (classification layer §§3–5):* **[§3](#3-slot-grammar-and-display-labels)** names the shared slot labels (**Table 1**) · **[§4](#32-constitutional-outcome-baseline-for-slots)** calibrates magnitude in LEQU (**§4.1** contribution · **§4.2** violation) · **[§5](#33-primary-category-defaults-and-lequ-slot-baseline)** classifies verified records (**§5.1** contribution / **Table 2** · **§5.2** violation severity ladder).",
    ),
    (
        "| [§4](#32-constitutional-outcome-baseline-for-slots) | **Calibration layer** — LEQU constitutional-outcome baseline | **Oversight** (verified calibration discipline) | **Flourishing** + **Accountability** |\n"
        "| [§5](#33-primary-category-defaults-and-lequ-slot-baseline) | **Classification layer** — Contribution Axis bands and Table 2 | **Oversight** | **Flourishing** |\n"
        "| [§6](#34-violation-axis-rules-violation-nature-adverse-findings-and-severity) | **Classification layer** — Violation Axis severity ladder | **Accountability** | **Accountability** (Violation Axis) + **Continuity** (unresolved findings stay live) |",
        "| [§4](#32-constitutional-outcome-baseline-for-slots) | **Calibration layer** — LEQU baseline (**§4.1** contribution · **§4.2** violation) | **Oversight** (verified calibration discipline) | **Flourishing** + **Continuity** |\n"
        "| [§5](#33-primary-category-defaults-and-lequ-slot-baseline) | **Classification layer** — primary defaults (**§5.1** Contribution Axis · **§5.2** Violation Axis) | **Oversight** + **Accountability** | **Flourishing** + **Continuity** |",
    ),
    (
        "Flourishing-side contribution under **§§3–5**, Accountability-side violation under **§6**",
        "Contribution-side classification under **§§4.1 and 5.1**, Violation-side classification under **§§4.2 and 5.2**",
    ),
    (
        "Accountability measure at **§6***",
        "Accountability measure at **§5.2***",
    ),
    (
        "Flourishing measure at **§§3–5**, Accountability measure at **§6***",
        "Flourishing measure at **§§4.1 and 5.1**, Accountability measure at **§§4.2 and 5.2***",
    ),
    # §3 internal pointers
    ("under **sections 4 through 6**", "under **sections 4 and 5**"),
    ("Operative criteria for Violation Axis `s` = 7, 8, and 9 remain in **section 6** and **Chapter Eight**.", "Operative criteria for Violation Axis `s` = 7, 8, and 9 remain in **section 5.2** and **Chapter Eight**."),
    ("It does not replace the contribution rules in **section 5**.", "It does not replace the contribution rules in **section 5.1**."),
    ("The four Contribution Axis primary bands and their operative rules are stated in **section 5**. Violation Axis display labels pair with the operative severity ladder in **section 6**.", "The four Contribution Axis primary bands and their operative rules are stated in **section 5.1**. Violation Axis display labels pair with the operative severity ladder in **section 5.2**."),
    ("Operative Contribution Axis rules are in **section 5** (**Table 2**); operative Violation Axis severity is in **section 6**.", "Operative Contribution Axis rules are in **section 5.1** (**Table 2**); operative Violation Axis severity is in **section 5.2**."),
    ("Authoritative severity criteria remain in **section 6**.", "Authoritative severity criteria remain in **section 5.2**."),
    # §2 standing records
    ("classifies verified **contribution state** under **section 5**.", "classifies verified **contribution state** under **section 5.1**."),
    ("classifies verified **violation nature** under **section 6**", "classifies verified **violation nature** under **section 5.2**"),
    ("(*Contribution Axis primary category defaults*); [§6](#34-violation-axis-rules-violation-nature-adverse-findings-and-severity) (*Violation Axis severity ladder*)", "(*Contribution Axis primary category defaults*); [§5.2](#34-violation-axis-rules-violation-nature-adverse-findings-and-severity) (*Violation Axis severity ladder*)"),
    # Cross-chapter Ch6 refs — order matters (specific before general)
    ("Chapter Six section 6 severity", "Chapter Six section 5.2 severity"),
    ("Chapter Six section 6** severity", "Chapter Six section 5.2** severity"),
    ("Chapter Six section 6.", "Chapter Six section 5.2."),
    ("Chapter Six section 6,", "Chapter Six section 5.2,"),
    ("Chapter Six section 6 ", "Chapter Six section 5.2 "),
    ("Chapter Six **§§5–6**", "Chapter Six **§§5.1–5.2**"),
    ("Chapter Six **section 5**", "Chapter Six **section 5.1**"),
    ("Chapter Six **section 6**", "Chapter Six **section 5.2**"),
    ("Chapter Six section 5**", "Chapter Six section 5.1**"),
    ("Chapter Six section 5,", "Chapter Six section 5.1,"),
    ("Chapter Six section 5.", "Chapter Six section 5.1."),
    ("Chapter Six section 5 ", "Chapter Six section 5.1 "),
    ("Chapter Six §6", "Chapter Six §5.2"),
    ("Chapter Six — section 5", "Chapter Six — section 5.1"),
    ("Chapter Six — section 6", "Chapter Six — section 5.2"),
    ("Chapter Six §5", "Chapter Six §5.1"),
    ("[§6](core_06-06_standing_assessment.md#34-violation-axis-rules-violation-nature-adverse-findings-and-severity)", "[§5.2](core_06-06_standing_assessment.md#34-violation-axis-rules-violation-nature-adverse-findings-and-severity)"),
    ("sections 5 and 6", "sections 5.1 and 5.2"),
    ("**sections 5 and 6**", "**sections 5.1 and 5.2**"),
    ("section 6 severity", "section 5.2 severity"),
    ("section 6**", "section 5.2**"),
    ("section 6.", "section 5.2."),
    ("section 6,", "section 5.2,"),
    ("section 6 ", "section 5.2 "),
    ("under section 6", "under section 5.2"),
    ("under **section 6**", "under **section 5.2**"),
    ("in section 6", "in section 5.2"),
    ("in **section 6**", "in **section 5.2**"),
    ("section 5** into", "section 5.1** into"),
    ("section 5**,", "section 5.1**,"),
    ("section 5.", "section 5.1."),
    ("section 5,", "section 5.1,"),
    ("section 5 ", "section 5.1 "),
    ("under section 5", "under section 5.1"),
    ("under **section 5**", "under **section 5.1**"),
    ("in section 5", "in section 5.1"),
    ("in **section 5**", "in **section 5.1**"),
    ("**section 5**", "**section 5.1**"),
    ("§5](core_06-06_standing_assessment.md#33-primary-category-defaults-and-lequ-slot-baseline)", "§5.1](core_06-06_standing_assessment.md#51-contribution-axis-bands-and-table-2)"),
    ("primary slot defaults", "primary category defaults"),
    ("the Chapter Six **section 6** severity ladder", "the Chapter Six **section 5.2** severity ladder"),
    ("Chapter Six **section 6** severity ladder", "Chapter Six **section 5.2** severity ladder"),
]


def update_file(path: Path) -> bool:
    if not path.exists() or path.suffix not in {".md", ".json"}:
        return False
    original = path.read_text(encoding="utf-8")
    text = guard_other_chapters(original)
    for old, new in CORPUS_REPLACEMENTS:
        text = text.replace(old, new)
    text = unguard(text)
    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main() -> None:
    restructure_ch06()
    touched = []
    for path in sorted(ROOT.rglob("*")):
        if path.name.startswith(".") or "archive/" in str(path.relative_to(ROOT)):
            continue
        if path == CH06 or "tools/ch06_" in str(path):
            continue
        if update_file(path):
            touched.append(path.relative_to(ROOT))
    print("Updated:", *touched, sep="\n  ")


if __name__ == "__main__":
    main()
