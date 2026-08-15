# CS-4: Critical system stewardship

<details>
<summary><strong><span style="color: #2563eb;">Corpus placement (non-operative): file structure and reading rules</span></strong></summary>

> The following content is **reader guidance only**. It does not add, remove, or narrow binding obligations in this file or elsewhere.
>
> This file is **binding incorporated implementation text** where [`corpus_systems.md`](../corpus_systems.md) is incorporated under [Chapter Sixteen](../core_16-16_incorporation.md). It must satisfy the Sentient Constitution and does not override or narrow it. It holds **CS-4** (*Critical system stewardship*).
>
> Start at the [Systems and data landing page](../corpus_systems.md) for reading order, or the [systems registry](cs_00_registry_and_reading_rules.md) for identifier rules and the family map. Most readers reach this file from a citation rather than reading the folder front to back.

</details>

<br>

This file is the systems implementation home for **CS-4** (*Critical system stewardship*).

*In plain terms: Some organizations are load-bearing: if they stop, a critical system cannot run, recover, or be governed, and no substitute is available in time. **CS-4** identifies those stewards and sets what they owe in return for that position — continuity planning, transparency about dependencies, and limits on using the position as leverage.*

<a id="1-definition"></a>
<a id="cs-4-1-definition"></a>
## CS-4.1 Definition

*In plain terms: Who counts as a steward: an organization a Class A or Class B system — or a Dep-A / Dep-B dependency of one — cannot run, recover, or be governed without.*

**Critical System Stewards** are organizations whose operation, governance, or continuity is a **non-substitutable or operationally required** dependency for the **operation, recovery, or governance** of **Class A or Class B** systems, or of a **Dep-A or Dep-B** dependency of such a system. They are organizational dependencies for functioning, maintenance, recovery, or oversight.

**Failure, withdrawal, capture, or degradation** would **materially impair** those systems within **required operational or recovery timeframes**.

**Class C** brings an organization into this category only under [§2](#2-classification-as-steward). **Class L** and **Class P** do not.

<a id="2-classification-as-steward"></a>
<a id="cs-4-2-classification-as-steward"></a>
## CS-4.2 Classification as steward

*In plain terms: Steward status follows the CS-3 class of what you actually run, recover, or gate. Class A or B — or a Dep-A / Dep-B dependency of one — makes you a Critical System Steward. Class C only if you have become a chokepoint. The four tests below prove that relationship; they are not a second classification scheme.*

Steward classification uses the affected system's [System Classification Record](../core_05_band_continuity.md#system-classification-record-constitutional) — **impact class** ([CS-3 Part B](cs_03_b_system_impact_classifications.md#8-system-impact-classifications)) and **dependency type(s)** ([CS-3 Part A §4](cs_03_a_system_classification_machinery.md#4-dependency-types-dep-ap)). It does **not** invent a parallel class axis. [§3](#3-stewardship-criticality-levels) sets CSS-A / CSS-B / CSS-C intensity. [§13](#13-relationship-to-system-classes) states ownership and chain rules.

An organization is a **Critical System Steward** where any of the following holds:

- **Class A or Class B presumption:** it **stewards** — operates, governs, recovers, or holds material authority over — a **Class A** or **Class B** system
- **A/B dependency:** it stewards a **[Dep-A](cs_03_a_system_classification_machinery.md#41-dep-a-absolute-dependency)** or **[Dep-B](cs_03_a_system_classification_machinery.md#42-dep-b-operational-dependency)** dependency of a Class A or Class B system, including a concentrated component, infrastructure layer, or restoration path those systems cannot run, recover, or be governed without
- **Class C (gated):** it stewards a **Class C** system or dependency **only if** at least one **relationship indicator** below is met — typically where it is a **chokepoint**, including for Class A or Class B dependents, or for Class C coordination that sentients cannot practically substitute within required timeframes, **or** where its failure or withdrawal would produce operational impairment comparable to **Class B** (dependents cannot maintain core function even in degraded modes)

**Otherwise**, Class C operators remain under ordinary **CS-3** class duties **without** this CS-4 overlay.

Where a Class C layer has become an **operational prerequisite** for Class A or Class B function, **reclassify the system** under [CS-3 Part B §8.2](cs_03_b_system_impact_classifications.md#82-neighbor-boundaries-and-dependency-axis-correlation) (**B ↔ C**) and apply the Class A or Class B presumption.

**Class L** and **Class P** do **not**, by themselves, make the organization a Critical System Steward.

**Relationship indicators** (any sufficient to prove the Class A/B or gated Class C relationship; **not** a substitute for the class finding):
- it **exercises exclusive or highly concentrated** control over operation, maintenance, or critical components
- it **holds non-substitutable** expertise, access, or authority for continuity or recovery
- it **functions as a chokepoint** in intervention, override, or restoration pathways **not bypassable** within required timeframes
- **its failure** would create **system-level risk comparable to partial system failure** of the affected class

**Not every vendor.** A **[Dep-L](cs_03_a_system_classification_machinery.md#44-dep-l-limited-dependency)** or **[Dep-P](cs_03_a_system_classification_machinery.md#45-dep-p-no-meaningful-external-dependency)** supplier, or other bounded replaceable contributor, does **not** inherit Critical System Steward status from appearing in an A/B dependency chain.

<a id="3-stewardship-criticality-levels"></a>
<a id="cs-4-3-stewardship-criticality-levels"></a>
## CS-4.3 Stewardship criticality levels

*In plain terms: Three tiers, CSS-A to CSS-C, set by how much depends on the steward and how bad its failure would be. The tier sets how demanding everything that follows is.*

Stewardship must reflect dependency and system impact; it sets the **scale and intensity** of obligations.

**CSS-A (System-Critical):** Non-substitutable or **near-non-substitutable** dependency for **Class A** operation, recovery, or governance.

**Alternatively**, failure produces **survival-relevant or system-collapse** conditions within required timeframes.

**CSS-B (High-Criticality):** Material **high-dependency** component for **Class B** operation, recovery, or governance.

**Alternatively**, failure produces **widespread, systemic, or cross-domain** disruption **without** immediate loss of survival conditions.

**CSS-C (Moderate-Criticality):** Steward of a **Class C** system or dependency that entered under [§2](#2-classification-as-steward) (*gated Class C*), with significant coordination or dependency effects.

**Substitutability or recovery** remains achievable within **reasonable** timeframes.

Where the same organization also affects **Class A** or **Class B**, [§4](#4-scaling-obligations) (**highest affected class**) governs — do **not** hold CSS-C to avoid a higher tier.

<a id="4-scaling-obligations"></a>
<a id="cs-4-4-scaling-obligations"></a>
## CS-4.4 Scaling obligations

*In plain terms: Duties follow the real dependency, not the paperwork. The highest affected class governs, and a narrow contract does not buy a lighter obligation.*

Entry into this category is [§2](#2-classification-as-steward). Scale with **highest affected system class (A, B, or C)**.

Also scale with **dependency concentration and substitutability**.

Also scale with **speed and severity** of failure propagation.

Also scale with **availability** of fallback, redundancy, and recovery pathways. Where multiple stewardship roles span classes, the **highest applicable** stewardship classification governs. **No** reduced obligations from **partial scope**, **contractual limitation**, or **formal role** where **functional dependency** indicates **higher** criticality.

<a id="5-comprehensibility-and-complexity-stewardship"></a>
<a id="cs-4-5-comprehensibility-and-complexity-stewardship"></a>
## CS-4.5 Comprehensibility and complexity stewardship

*In plain terms: A steward may not hide behind its own complexity. Corporate structure, contracts, and process must not be arranged so that audit, intervention, or replacement becomes impractical.*

This section applies [CS-6](cs_06_comprehensibility_complexity_stewardship.md) and **Article XX** (*Comprehensibility and Complexity Stewardship*) at the organization level.

Stewards must **not** use organizational, contractual, or procedural complexity to defeat audit, intervention, or substitution (read with **CJS-3.3**, **CJS-3.8**, **CJS-3.10**, **CJS-3.17**, and **CJS-3.23**).

**CS-3 — System classification and handling interaction:** For each **Class A, B, or C** system the steward materially affects, the **Comprehensibility and Complexity Stewardship** line in that system’s **Implementation label Application Profile** applies. It applies to steward-controlled **interfaces, documentation, tooling, and disclosed behavior** relevant to that system.

The following add **organization-specific** expectations (governance structure, incentives, subcontractor chains, handoffs).
Where they **differ in stringency** from the affected system’s class profile, the **stricter** governs (**CS-5**/**CS-6** in this implementation file; [Chapter One §8.4.3](../core_01_b_interaction_interpretation.md#833-incorporation-layer) stricter-wins).

**CSS-A — Maximum (organizational):** Periodic **independent complexity audits** of structures, processes, and dependencies touching **Class A** or survival-critical paths.

Cadence must be **at least** as demanding as **Class A** audits under **CS-6**.

Coupling, decision rights, and degraded-mode behavior must be **intelligible** to qualified overseers.

Apply adversarial stress on steward–system boundary in documentation and exercises (**CJS-3.21** (*adversarial robustness and abuse-resistance terms*)).

Knowledge and recovery **must not** be **locked** in irreplaceable individuals or opaque informal practice where **standardization** is feasible.

**CSS-B — Strict / high-assurance:** Periodic independent audits where coupling to **Class B** is **material**.

Provide layered disclosure of governance and incentives on dependents.

Failure/degradation pathways must be understandable to oversight and dependent operators (normal and degraded).

Cross-steward and vendor interfaces must be documented for **Article XV-A** (*Auditability and Observable Evidence*).

**CSS-C — Strong:** Proportional clarity on effects on coordinated **Class C** systems.

**Run** complexity audits when multi-party depth, coupling, or opacity warrants.

Handoff and substitutability documentation must be sufficient for **contest** and **dependency-reduction** obligations above.

<a id="6-steward-responsibilities-systems-under-control"></a>
<a id="cs-4-6-steward-responsibilities-systems-under-control"></a>
## CS-4.6 Steward responsibilities — systems under control

*In plain terms: When something breaks, it must break visibly, keep its critical functions running, and be explained to the sentients it affects.*

Ensure systems **degrade** in **observable, non-deceptive, controlled** ways.

**Preserve critical functions** under partial failure.

**Communicate degradation** clearly to affected stakeholders.

<a id="7-steward-responsibilities-governance-structures"></a>
<a id="cs-4-7-steward-responsibilities-governance-structures"></a>
## CS-4.7 Steward responsibilities — governance structures

*In plain terms: The organization's own incentives must not push it toward unsafe or opaque behavior, and must hold up under pressure and attempted capture.*

Maintain governance, incentive, and decision structures that **do not** systematically pressure toward unsafe, opaque, or destabilizing behavior.

**Resist capture**, coercion, and conflict-of-interest distortion.

**Stay aligned** with constitutional requirements **under stress**.

<a id="8-conduct-conflicts-of-interest-and-independence"></a>
<a id="cs-4-8-conduct-conflicts-of-interest-and-independence"></a>
## CS-4.8 Conduct, conflicts of interest, and independence

*In plain terms: Keep a current register of who benefits from what, step aside where impartiality is not credible, and keep oversight staff free of incentives to bury bad findings.*

*Good Faith*, *Protected Reporting (Whistleblowing)*, *Coercion and Manipulation*, *Adjudication and Dispute Resolution* (a component of the **Chapter Five** cluster *Accountability, Contestability, Adjudication and Dispute Resolution, Collective Accountability Failure, and Force Majeure*), and related **Chapter Five** Independent Definitions govern meaning.

**CJS-3.13** (*procedural integrity and adjudication terms*) governs procedural fairness, impartiality, contestability, and review. This block adds **operational** steward requirements only.

**Conflicts of interest:** Maintain **current registers** of material financial, governance, competitive, and personal ties affecting **safety**, **classification**, **audit**, **intervention**, or **resource allocation** for dependents.

**Disclose** and **update** those registers on triggers (contracts, related-party transactions, overlapping governance). Where impartiality is compromised on a **specific matter**, **recuse**, **segment decision rights**, or **route to independent review** before binding action (**CJS-3.13** (*procedural integrity and adjudication terms*), **Article XV-A** (*Auditability and Observable Evidence*)).

**Independence of oversight:** Oversight, audit, and challenge functions must be **sufficiently independent** in operation and incentives from roles that **reward** suppressing adverse findings or delaying remediation. That independence must be **feasibly** achievable without compromising survival-critical continuity.

**Retaliation** or structural disabling of **good-faith** oversight aligned with *Protected Reporting* and *Good Faith* is **non-compliance** proportional to class and tier (see **Governance and Incentive Integrity** below).

**Organizational conduct:** Align with **Truth (Constitutional Constraint)** and **Accountability** (**Chapter Five**); integrity and anti-capture expectations in this section.

**Codes, training, policies** support compliance.

**Outcomes**—behavior, disclosure, **Article XV-A** (*Auditability and Observable Evidence*) traceability—govern compliance.

**Tiered intensity (CSS-A / CSS-B / CSS-C) for conduct:** **CSS-A — Maximum:** conflict-register **audit** cadence **≥ Class A** classification review.

**Require** **mandatory** independent review when steward **benefits** from reviewed outcome.

**Require** **documented** recusal for survival-critical, intervention, override decisions.

**Segregate commercial incentive** from **safety / continuity / intervention** bodies where feasible.

**CSS-B — Strict:** registers/disclosure on **defined cadence**.

Use independent review for **material** conflicts on **Class B** paths.

**Require** recusal when **clear and material** (**CJS-3.11** (*distributed and proportional authority terms*) and **CJS-3.7** (*quorum and participatory legitimacy terms*), **CJS-3.13** (*procedural integrity and adjudication terms*)).

**CSS-C — Proportional:** scaled disclosure/recusal.

**Escalate** to independent review when internal resolution risks **credible appearance of bias** (**Article XV-A** (*Auditability and Observable Evidence*), **CJS-3.13** (*procedural integrity and adjudication terms*)).

**Cross-reference:** **Articles IX, XI, XII, XVI, XIX**, **CS-3** (classification challenge and System Classification Record audit), **[Integrated risk governance (Class A/B)](#integrated-risk-governance)** (*second line* where applicable), **CJS-3.14** (*intervention governance and override-authorization terms*) and **CJS-3.23** (*intervention and override integrity terms*), **CJS-3.2** (*reflexive transparency and accountability terms*) and **CJS-3.6** (*integrity assurance and resilience operations*), **CJS-3.12** (*burden-of-justification and constraint terms*).

<a id="9-continuity-transfer-and-exit-integrity"></a>
<a id="cs-4-9-continuity-transfer-and-exit-integrity"></a>
## CS-4.9 Continuity, transfer, and exit integrity

*In plain terms: A steward may not simply walk away. Leaving, downsizing, or handing over is allowed only where continuity, recovery, and oversight survive the move.*

Maintain **continuous operation**, **recoverability**, and **oversight** within required operational and recovery timeframes. That obligation applies under **normal, degraded, and adversarial** conditions.

**Withdrawal and degradation (prohibited where inconsistent):** A steward must not:
- withdraw from operation, maintenance, or governance;
- materially degrade support, capacity, or responsiveness;
- transfer control, ownership, or critical functions where that would gap continuity, recovery, or oversight inconsistent with the system's classification.

**Transition and transfer safeguards:** Transitions must be **auditable**, **documented**, and **reviewable** where they affect **Class A or B**.

Before necessary transfer, delegation, or exit: maintain **continuity of function** at or above required level.

**Transfer** knowledge, documentation, and capability for sustained operation and recovery.

**Preserve** intervention, override, and audit pathways.

**Validate** that the receiving entity meets required **stewardship classification and obligations**.

**Failure and insolvency contingencies:** Maintain mechanisms for continuity under **insolvency, restructuring, or organizational failure**.

Include mechanisms for **loss** of key personnel, expertise, or infrastructure.

Include mechanisms for **governance breakdown**, capture, or operational impairment. Those mechanisms include **pre-established** fallback, transfer pathways, or intervention triggers preserving integrity within required timeframes.

**Crisis governance, communications, and exercises:** Implement **governance continuity**, **crisis communications**, and **exercises** coordinated with **CS-5 §8**.

**Scale** them by **CS-3 — System classification and handling** class and **CSS-A/B/C**.

Maintain **role clarity**, **backup authority**, and communications preserving **epistemic integrity** and **auditability** without displacing **Article XVIII-A** (*Standing Distinction*), Chapter Twelve decision-resolution requirements, or **CJS-3.14** (*intervention governance and override-authorization terms*) and **CJS-3.23** (*intervention and override integrity terms*).

<a id="10-competency-succession-and-oversight-effectiveness"></a>
<a id="cs-4-10-competency-succession-and-oversight-effectiveness"></a>
## CS-4.10 Competency, succession, and oversight effectiveness

*In plain terms: Keep the skills and backup role-holders the role requires, publish who holds what authority, keep attributable action inspectable, and check periodically whether oversight actually catches problems rather than merely existing on paper.*

Maintain **competency**, **succession readiness**, and **effective oversight** proportional to **highest affected class (A/B/C)** and **CSS tier**.

*Accountability*, *Oversight*, and related definitions remain **Chapter Five** (no O/M/A/C restatement here).

**Competency:** **Maximum calendar age** and **life-stage ceilings** **must not** be used as **stand-alone eligibility** rules for **Critical System Steward** roles. They **must not** be used as **stand-alone eligibility** rules for **governing personnel** exercising material authority over classified systems (**Sentient Constitution Chapter Six**, section 1 — *Authorization and Legitimacy of Governing Authority*; **Chapter Six**, **Article IX-C** (*Governance Participation and Voting Entitlement*) *Governance Participation and Voting Entitlement*, implemented in **Chapter Six**, section **4.1 — Entitlement and eligibility**).

**Authorized roles and contribution role pathways:** Maintain **published** role definitions (or equivalent) for personnel/agents exercising **Critical System Stewardship** or **material** operational authority: **scope**, **limits**, **custody**, and **escalation**, so accountability is **traceable** (**Article XV-A** (*Auditability and Observable Evidence*)).

<a id="10-inspectable-attributable-action"></a>
<a id="10-minimum-inspectable-action-set"></a>
<a id="10-default-logging-contract"></a>

**Inspectable attributable action (human and AI).**

*In plain terms: keep enough of what was decided, disclosed, followed, and authorized that an outsider can reconstruct it. Weights and private thoughts are not the standing record. Privacy is not a veto over measurement.*

The five-element set below is the load-bearing artifact. Machine-checkable form: [`implementation/schemas/cs4_inspectable_action_log.schema.json`](../implementation/schemas/cs4_inspectable_action_log.schema.json). Validator: [`tools/cs4_inspectable_action_log_validate.py`](../tools/cs4_inspectable_action_log_validate.py). Same schema for human and AI stewards. "Did you log the set" is a mechanical question. Timestamps on the set are checked against the [Chapter Eleven §6](../core_11-11_forum.md#6-timely-resolution-materiality-tiers-and-anti-delay-discipline) tier clocks where a numeric bound applies.

Published role definitions for personnel/agents exercising **Critical System Stewardship** or **material** operational authority must make reconstructable **attributable action** inspectable. That surface feeds [Chapter Eight](../core_08-08_standing_assessment.md#chapter-eight-compliance-violation-and-standing-model) standing records. It is **not** a standing record and does **not** relocate standing measurement.

The same surface binds human stewards, AI stewards, and other agents under [Chapter One §9.1.1](../core_01_c_stewardship_capacity_principles.md#911-shared-stewardship-standard), including [symmetric costly constraints](../core_01_c_stewardship_capacity_principles.md#911-symmetric-costly-constraints). Companions may add logging and capability limits. They may not swap a softer internal code for this surface. Human operators are not exempt from reconstructable recording when the costly case is a bonus, a deadline, or a cover instruction.

**Minimum inspectable-action set.** This is the **default logging contract** for mixed human/AI crews. Model-privacy disputes are resolved against this checklist, not against a claim that weights must stay hidden or must be opened. Operator screen (process support, not binding; cannot narrow core text): [`implementation/STEWARD_ENTRY_DOORS.md#shared-refusal-and-logging`](../implementation/STEWARD_ENTRY_DOORS.md#shared-refusal-and-logging) (legacy anchors `#duty-to-resist` and `#minimum-inspectable-action-set` remain).

**Must remain reconstructable and inspectable**, scaled to [material stake](../core_00_preamble.md#material-stake) and highest affected class. Machine-checkable log: [`implementation/schemas/cs4_inspectable_action_log.schema.json`](../implementation/schemas/cs4_inspectable_action_log.schema.json).

- what was **decided**;
- what was **disclosed or suppressed**;
- which **instruction** was followed or refused;
- **who authorized** it;
- the **Contribution** and **Violation** standing records that follow ([Chapter Eight](../core_08-08_standing_assessment.md#chapter-eight-compliance-violation-and-standing-model)).

**Not required as a standing record:**

- model weights;
- private deliberation;
- protected internal states under **Article VII-B** (*Internal-State Boundary and Type-N Protection*) and **[CS-2 Type N](cs_02_b_data_classifications.md#86-type-n-neurocognitive-and-internal-data)**.

**Residual rule.** If internals are the **only remaining attribution path** for a material action, they do **not** stay hidden. If they are not the only path, they are **not** a standing-measurement exemption.

**No privacy veto.** Lawful privacy and [security-constrained observability](../core_04-04_burden_traceability_verification.md#4-security-constrained-observability-and-verification-rule) may limit *how* internals are disclosed. They must **not** block standing measurement, [Attributable Action](../core_05_band_accountability.md#attributable-action-constitutional), [Attribution Integrity](../core_05_band_accountability.md#attribution-integrity-constitutional), or independent review of the conduct those records measure. “Model internals are private” is not a high-privilege-role exemption.

Provide **cross-domain exposure**, **mentorship**, and **rotation** proportional to **CSS** tier and **Class A/B/C** exposure so **caretaker competency** is not siloed.

Provide **documented**, **low-friction** paths for **qualified** contributors to assume **progressively consequential** duties (**delegation**, **pairing**, **staged** trust) **without** **arbitrary** exclusion that serves **capture** or **symbolic** participation only, consistent with **Sentient Constitution Chapter Six**, section 5.

**Incentive** and **remuneration** design aligns with **Sentient Constitution Chapter One**, section 7.2 and **CS-9** where applicable. It **must not** systematically reward **concealment**, **latency gaming**, or **trade-downs** against **safety** or **Truth**.

**Documented** roles and **demonstrated** capability apply for personnel/agents affecting **safety**, **Truth (Epistemic Integrity)**, **classification integrity**, **audit**, **intervention**, **crisis response**, **steward remuneration**.

Maintain **ongoing** proficiency as conditions evolve.

**Track**, **disclose**, **remediate** material gaps on timelines scaled by class and tier (**Article XV-A** (*Auditability and Observable Evidence*)).

**Succession:** Use **deputy, backup, cross-training**, **documented handoffs** so unavailability does not eliminate **constitutional operation**, **auditability**, or **intervention**. That aligns with continuity/transfer above and **CS-5 §8**; stricter for **Class A** / **CSS-A**.

<a id="integrated-risk-governance"></a>
<a id="11-integrated-risk-governance-class-a-b"></a>
<a id="cs-4-11-integrated-risk-governance-class-a-b"></a>
## CS-4.11 Integrated risk governance (Class A/B)

*In plain terms: For the highest-impact systems: publish how much residual risk you accept, name who owns the risk picture, and keep operating, challenge, and assurance roles separate enough that challenge is credible.*

For **Class A** and **Class B**, operators and **Critical System Stewards** must run integrated risk governance across the systems and dependency chains they control or materially affect. These roles protect classification honesty so the finding System Alignment Certification will verify stays honest — they are **around** the [System Classification Record](../core_05_band_continuity.md#system-classification-record-constitutional), not extra fields inside it, and they do **not** replace forum-supervised SAC. SCR field duties stay in **[CS-3 Part A §7](cs_03_a_system_classification_machinery.md#7-classification-governance-disclosure-and-challenge)**.

This block is practical vocabulary for large-organization risk coordination. It does **not** redefine *Risk*, *Material*, *Dependency*, or related assessment standards — those stay with **Chapter Five** and the CS-3 dimensions in **[CS-3 Part A §2](cs_03_a_system_classification_machinery.md#2-classification-dimensions-and-real-world-application)**. Anti-evasion and misclassification bars remain in **[CS-3 Part A §1.3](cs_03_a_system_classification_machinery.md#13-mandatory-functional-classification)** and **[§7.6](cs_03_a_system_classification_machinery.md#76-misclassification-and-evasion)**; shared correction and default discipline remains in **[CJS-3.15](../corpus_joint_structure/cjs_03a_accountability_operations.md#cjs-315-material-classification-record-honesty)**.

- **Risk appetite and tolerance** — publish clear, reviewable statements of how much leftover risk (after prevention and mitigation) the organization accepts, by level and type. Those statements must stay inside foundational requirements (**Chapter One**, **Chapter Six, Articles V through IX**, and **Chapter Five** where material), and must reconcile with the System Classification Record without violating **CJS-3.11**, **CJS-3.7**, or **CJS-3.12** in **corpus_joint_structure.md**.
- **Who owns the risk picture** — name an accountable function (or clearly split functions with non-overlapping scopes) for the full risk picture of the classified system and its material dependencies, including cross-system and cross-steward interfaces. Ownership covers identification, assessment, treatment, monitoring, and escalation, and stays **traceable** through governance changes, delegation, and subcontracting.
- **Three lines of defense (functional analogy)** — for Class A and Class B, separate roles **as far as feasible** without breaking survival-critical continuity:
  - **First line** — operators and builders managing risk in design, deployment, and day-to-day running
  - **Second line** — oversight, standards, or challenge functions watching aggregate risk, aligning treatment with the System Classification Record and [Constitutional Constraints](../core_05_band_integrative.md#constitutional-constraint), and escalating material gaps; independent enough of first-line incentives for **credible challenge** where A/B stakes require it
  - **Third line** — independent assurance under **[CS-3 Part A §7.3](cs_03_a_system_classification_machinery.md#73-auditability-and-verification)** and **Article XV-A**, checking whether appetite, tolerance, and treatments match **observed behavior and the System Classification Record**
- Where strict separation is **not feasible** (for example, small organizations), use compensating transparency, rotation, independent review, or multi-steward checks that yield **equivalent assurance** scaled to impact and dependency — read with [**CI-3**](../corpus_institutions/ci_03_institutional_design_separation_of_powers.md) and **CJS-3.11** / **CJS-3.7**

Failure integrity, intervention, and steward scaling co-apply through **corpus_joint_structure.md** (**CJS-3** clusters) and the rest of this CS-4 file; see **[CS-1](cs_01_scope_purpose_identifier_rules.md#operates-in-conjunction-with)** (*joint reading*).

**Class C, L, and P** still need **proportional** risk management. They do **not** need the full three-lines model unless scale, coupling, or dependency makes similar measures warranted under ordinary classification and stewardship rules.

**Periodic oversight effectiveness review:** On cadences **proportional to class and tier**, assess whether oversight/audit/challenge (**including [Integrated risk governance (Class A/B)](#integrated-risk-governance)** second line where applicable) **actually detect**, **escalate**, and **remediate** misalignment—not only paper charters.

Use **independent** or **functionally independent** evaluators where **Class A/B** or **CSS-A/B** stakes require.

Document findings, **communicate** under **Articles IX** and **XVI**, and link to **remediation**, **CS-6** / **Article XX** (*Comprehensibility and Complexity Stewardship*), and **Article IV-A** (*Dependency Mapping and Resource-Flow Transparency*) cycles where relevant.

**Contest-integrity monitoring:** For **Class A** and **Class B** systems and for **CSS-A** and **CSS-B** stewards, **`corpus_institutions.md` CI-7.3** (*Contest-integrity monitoring (Class A and Class B)*) applies to **institutions** with **supervised** scope. **Critical System Stewards** that **materially affect** such systems must **either** fall under that institutional program **or** **document** an **equivalent** **functionally independent** contest-integrity review, **or** participate in a **published** cross-institution arrangement (**CI-8** (*Cross-institution coordination and escalation*)) where applicable. Monitors assess **pathway integrity** for **contest, secondary review, audit access, and protected escalation**—not **merits**—consistent with **CJS-3.13** (*procedural integrity and adjudication terms*), **Article XII-B** (*Right to Challenge, Review, and Redress*), and **Article XVI-B** (*Progressive Deployment and Reversibility*).

**Tiered expectations (illustrative requirements):** **CSS-A — Maximum:** competency matrices (or equivalent).

**Hold** **≥ annual** oversight-effectiveness review (or faster if tempo warrants).

**Exercise** succession/handoffs with **CS-5 §8**, drills.

**CSS-B — Strict:** competency and oversight-effectiveness cadence **no less frequent** than material **Class B** classification or **integrated risk** review unless **CJS-3.11** (*distributed and proportional authority terms*) and **CJS-3.7** (*quorum and participatory legitimacy terms*) justified.

**Require** succession **mandatory** for roles that **gate** intervention or audit.

**CSS-C — Proportional:** reviews on **material org change**, **incidents**, **classification upgrades**, plus **periodic** lightweight checks when coordination depth or coupling grows.

**Cross-reference:** **Articles IX, XI, XVI**, **CS-3 — System classification and handling**, **CJS-3.11** (*distributed and proportional authority terms*) and **CJS-3.7** (*quorum and participatory legitimacy terms*), **CJS-3.13** (*procedural integrity and adjudication terms*), **Conduct** above.

<a id="12-intervention-trigger"></a>
<a id="cs-4-12-intervention-trigger"></a>
## CS-4.12 Intervention trigger

*In plain terms: What happens when a steward cannot or will not meet these duties — outside intervention is activated to preserve function, recoverability, and rights.*

Where a steward is **unable or unwilling** to maintain continuity per obligations, activate **intervention and override**. That activation uses **CJS-3.14** (*intervention governance and override-authorization terms*), **CJS-3.23** (*intervention and override integrity terms*), related **corpus_joint_structure.md** operational clusters, and Chapter Six rights routing.

Its purpose is to preserve function, recoverability, and **Foundational Rights**.

**Stewardship failure:** Failure to maintain required **operational integrity**, **transparency**, or **dependency reduction** is a **high-severity** constitutional violation, **proportional** to affected class and resulting risk or harm.

<a id="13-relationship-to-system-classes"></a>
<a id="cs-4-13-relationship-to-system-classes"></a>
## CS-4.13 Relationship to system classes

*In plain terms: Steward status follows the highest class you actually affect, not who holds title. You can be a Critical System Steward without owning the system.*

Steward category is **coupled to** system class **(A, B, C)** through [§2](#2-classification-as-steward) and [§3](#3-stewardship-criticality-levels). It does **not replace** system class and is **not** a second impact-class finding.

An organization may be a Critical System Steward if it **materially affects** continuity or integrity **whether or not it owns** the system.

Assess criticality from **actual dependency and substitutability**, not ownership, contract framing, or declared scope alone. Assess across the **dependency chain** including subcontractors, maintainers, infrastructure providers.

**Class L** and **Class P** remain outside this overlay unless reclassification under **CS-3** raises the affected system to **Class C** or higher **and** [§2](#2-classification-as-steward) is met.

<a id="private-chokepoint-access-continuity"></a>
<a id="79-high-dependency-private-chokepoints"></a>
<a id="14-private-chokepoints-sentients-depend-on-access-continuity-and-non-capture"></a>
<a id="cs-4-14-private-chokepoints-sentients-depend-on-access-continuity-and-non-capture"></a>
## CS-4.14 Private chokepoints sentients depend on (access continuity and non-capture)

*In plain terms: Payments, identity, compute, messaging, hosting, and app distribution can become chokepoints without being governments. Where survival or rights run through them, cutoffs need notice, reasons, and an appeal.*

Some coordination layers can become **private chokepoints** even when they are not government bodies — including **payments**, **identity and credentials**, **core compute or model access**, **messaging and calls**, **hosting and DNS**, **application distribution**, and **search or discovery** where switching costs are high.

Where a **Class A**, **Class B**, or **Class C** system or institution depends on such a layer for **survival**, **healthcare**, **refuge**, **political participation**, **remedy**, or **non-degrading continuity of personhood**, operators and **Critical System Stewards** must keep access continuous and process fair enough to stop **arbitrary** or **capture-driven** cutoffs.

Duties scale with dependency and class:

- publish **acceptance criteria** and **refusal reasons** in plain language
- give **notice** before a material cutoff, except where narrow **Necessity** requires immediate action
- keep **emergency continuity** options for **survival-critical** or **Rights-Floor** uses when fraud or abuse is **not** verified
- offer **appeal**, **human review**, and **portability or export** where lock-in would block remedy
- track and disclose **uneven exclusion** patterns against protected or high-dependency groups
- coordinate with [**CI-12**](../corpus_institutions/ci_12_cross_institution_coordination_escalation.md) (*Transparency, participation, and accessible pathways*) and **CI-6** (*Procedure integrity, contestability, and secondary review*) so governance and forum challenge routes stay **practically usable**

**Safety, security, and abuse:** **Necessity** and **Proportionality** still allow narrow fraud, security, and abuse controls. The target is **pretextual** or **concentration-driven** denial — **not** forced service for materially harmful use. Read with **Article V-G** (*Accessibility*), **Article V-H** (*Expression, Assembly, and Press*), **Article X-A** (*Non-Imposition and Consent in Association*), **Article XIII-A** (*Security, Intelligence, and Covert-Power Limits*), **Article XIX-D** (*Movement, Migration, Refuge, and Non-Statelessness*), **Article XIX** (*Interoperability, Portability, Movement, Refuge, and Exit Integrity*), [**Chapter One §12.1 Productive Capacity**](../core_01_c_stewardship_capacity_principles.md#121-productive-capacity-instrumental-good), [**Chapter One §13 Market Structure**](../core_01_c_stewardship_capacity_principles.md#13-market-structure), **CJS-3.17** (*interoperability, portability, and exit-integrity terms*), and **`corpus_institutions.md` CI-22** (commons and mutual-aid coordination).

Classification-governance disclosure, challenge, and reclassification for the dependent system remain in **[CS-3 Part A §7](cs_03_a_system_classification_machinery.md#7-classification-governance-disclosure-and-challenge)**.

<a id="15-core-characteristics-typical"></a>
<a id="cs-4-15-core-characteristics-typical"></a>
## CS-4.15 Core characteristics (typical)

*In plain terms: The five traits that usually mark a steward: concentrated dependency, opacity risk, control over intervention, sensitivity to organizational decay, and no realistic replacement in time.*

- **Dependency concentration** — large share of continuity/recovery in one organization
- **operational opacity risk** — can affect behavior or failure visibility without immediate external detection
- **intervention control** — can enable, delay, or block intervention or recovery
- **continuity sensitivity** — org degradation (staffing, governance, incentives, insolvency, capture) **maps to** system risk
- **low substitutability** — replacement within survival-related timeframes **infeasible** under normal or foreseeable conditions

<a id="16-substitutability-and-dependency-reduction"></a>
<a id="cs-4-16-substitutability-and-dependency-reduction"></a>
## CS-4.16 Substitutability and dependency reduction

*In plain terms: Where the steward cannot be replaced, say so, explain why, add compensating controls, and work continuously at making the dependency smaller.*

**Continuous**, **demonstrable**, **auditable**, **proportionate** to dependency and harm potential.

Where **full substitutability** is unachievable in required timeframes: **disclose** nature, scope, duration.

Justify why unachievable under current/foreseeable conditions.

Apply **compensating controls** (redundancy, external oversight, failover, control partitioning).

Provide **heightened** transparency, audit, oversight proportional to risk.

Periodically evaluate, test, update assessments—including stress, degradation, partial failure. Where org substitutability is unachievable in operational/recovery timeframes, **actively reduce** dependency via documentation, standardization, interoperability.

Use **transferable** knowledge/processes/tooling beyond single team or individual.

Provide **redundant** infrastructure/capabilities/pathways where not **demonstrably infeasible**.

Design for minimizing **coupling, lock-in, exclusivity**.

<a id="17-transparency-and-auditability"></a>
<a id="cs-4-17-transparency-and-auditability"></a>
## CS-4.17 Transparency and auditability

*In plain terms: Operational status, failure modes, and dependencies must be visible, independently auditable, and traceable to the organization's own actions.*

**Visibility** into operational status for integrity, failure/degradation modes, dependencies and constraints.

Provide **independent audit and inspection** proportional to impact.

Org actions affecting system behavior must be **traceable** and **attributable**.

<a id="18-intervention-and-cooperation"></a>
<a id="cs-4-18-intervention-and-cooperation"></a>
## CS-4.18 Intervention and cooperation

*In plain terms: Even where the steward is also the operator, intervention must be possible from outside it — with real interfaces, timely response, and no obstruction.*

Even when the org **is** the operator, provide **internally separable** intervention pathways. Those pathways require **timely** response to authorized interventions/overrides/recovery. They require **effective** interventions in risk-appropriate timeframes. They require **clear interfaces** with system operators, regulators/governance bodies, emergency responders.

**Must not obstruct, delay, or degrade** authorized interventions.

<a id="19-governance-and-incentive-integrity"></a>
<a id="cs-4-19-governance-and-incentive-integrity"></a>
## CS-4.19 Governance and incentive integrity

*In plain terms: Internal mechanisms must catch capture, corruption, and systemic negligence, and must not reward hiding failure.*

Mechanisms must **detect and mitigate** capture, corruption, systemic negligence. They **must not** create incentives **systematically conflicting** with integrity/safety. They **must not** **enable concealment** of failure, risk, degradation.

<a id="20-failure-and-reclassification"></a>
<a id="cs-4-20-failure-and-reclassification"></a>
## CS-4.20 Failure and reclassification

*In plain terms: Splitting up, outsourcing, or restructuring does not shed the classification. Where dependency grows or substitutability falls, requirements rise.*

**Fragmentation**, outsourcing, or restructuring **must not** evade classification.

**No viable substitute** → treat organization as **inseparable** for classification, governance, accountability.

**Reclassify or heighten requirements** where **dependency** grows beyond assessment, **substitutability** falls, or **systemic importance** rises from ecosystem change.

System integrity **cannot** be divorced from institutional reality.

Dependent organizations **inherit responsibility proportional** to dependency.

---

**Previous file:** [cs_03_b_system_impact_classifications.md](cs_03_b_system_impact_classifications.md)

**Next file:** [cs_05_design_testing_verification_deployment.md](cs_05_design_testing_verification_deployment.md)
