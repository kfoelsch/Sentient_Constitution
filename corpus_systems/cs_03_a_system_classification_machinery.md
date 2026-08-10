<a id="cs-3-part-a-system-classification-machinery"></a>
# CS-3, Part A: System classification machinery

<details>
<summary><strong><span style="color: #2563eb;">Corpus placement (non-operative): file structure and reading rules</span></strong></summary>

> The following content is **reader guidance only**. It does not add, remove, or narrow binding obligations elsewhere in this file or in other CS-3 parts.
>
> This file contains **CS-3, Part A** — purpose and scope, classification dimensions, criticality and concentration factors, **dependency types** (**Dep-A–P** reliance categories), boundaries / timeframes / resilience, domain taxonomy and scarce-capacity handling, and classification governance (**§§1–7**). **Part B** — system **impact** classifications (**Class A** through **Class P**), including aspect-comparative matrices and per-class cards — is in [`cs_03_b_system_impact_classifications.md`](cs_03_b_system_impact_classifications.md).

</details>

<br>

**CS-3, Part A**, owns **classification machinery**: how to determine impact, dependency, and risk; how to type reliance; how to keep classification honest; and how governance, disclosure, and challenge work. Canonical **impact-class** definitions and per-class scaled duties are in **[Part B](cs_03_b_system_impact_classifications.md#cs-3-part-b-system-impact-classifications)**.

*In plain terms: Part A says how to classify systems honestly across impact, dependency, and risk — Part B names the impact classes themselves and what each class must do.*

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Read with: Integrative Materiality ([Materiality Determination](../core_05_band_oversight.md#materiality-determination)) (*Materiality gate for class scaling*); [System Classification Record](../core_05_band_continuity.md#system-classification-record-constitutional); [System Alignment Certification](../core_05_band_continuity.md#system-alignment-certification-constitutional); [System Certification Record](../core_05_band_continuity.md#system-certification-record-constitutional); [Chapter Seven §2 System Class Evaluation](../core_07_a_system_alignment_certification_evaluation.md#2-system-class-evaluation); [Chapter Seven Part B §11.1](../core_07_b_system_alignment_certification_record_process.md#111-minimum-record-contents) (*System Classification Record as certification-record component*); [Chapter Seven Part B §12](../core_07_b_system_alignment_certification_record_process.md#12-transparency-auditability-and-contestability) and [§14](../core_07_b_system_alignment_certification_record_process.md#14-supervisory-sequence-and-contestability-chain) (*contest when class is inside an active certification record*); [Chapter Seven Part B §16](../core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) (*reopening on system-class misalignment*); [Protocol A — System Design, Testing, Verification, and Deployment](cs_protocol_a_system_design_testing_verification_deployment.md) (*recertification and regression testing*); [CS-1 — Operates in conjunction with](cs_01_scope_purpose_identifier_rules.md#operates-in-conjunction-with).

</details>

<br>

<a id="1-purpose-and-scope"></a>
## 1. Purpose and scope

*In plain terms: classify systems by what they actually do and what can go wrong — not by what operators say they are — keep that class in a System Classification Record that audits can check, and keep the record challengeable and up to date.*

**CS-3 — System classification and handling** is how systems get a class from what they actually do and what can go wrong — not from what operators call them. Class is **material audited information**: auditing processes require it, and System Classification Record audits check it between and beside [System Alignment Certification](../core_05_band_continuity.md#system-alignment-certification-constitutional) cycles ([§1.3](#13-mandatory-functional-classification); [§7.3](#73-auditability-and-verification)).

- **Duties scale:** Stronger impact and dependency mean stronger obligations.
- **No evasion:** Classification **cannot evade** constitutional requirements.
- **Record required:** For every system with **material impact**, CS-3 requires a [System Classification Record](../core_05_band_continuity.md#system-classification-record-constitutional) that states both findings — impact class and dependency type(s) — along with the reasons, assumptions, remaining uncertainty, and when the class must be checked or updated.
- **Certification bridge:** When System Alignment Certification runs, that record must be produced or verified and included in the [System Certification Record](../core_05_band_continuity.md#system-certification-record-constitutional).

CS-3 implements:

- **How class is determined**
  - **Holistic multi-dimension classification** — evaluate impact, dependency, and risk together under real and foreseeable conditions ([§1.1](#11-holistic-classification); [§2.1](#21-classification-dimensions); [§2.2](#22-real-world-application))
  - **Existential and worst-case accounting** — classify to the highest plausible level where credible failure modes or civilization-scale harm pathways exist ([§1.2](#12-classification-and-existential-risk))
  - **Mandatory functional classification** — class follows observed and reasonably foreseeable effects, not intent or self-description; remains transparent, auditable, challengeable, and continuously revalidated in a System Classification Record ([§1.3](#13-mandatory-functional-classification))
  - **Alignment-status recognition and ambiguity default** — the System Classification Record must support forum recognition or revalidation when official alignment status is required; ambiguity defaults to protecting Foundational Rights ([§1.4](#14-alignment-status-recognition-and-ambiguity-default))
  - **Criticality, concentration, temporal, and adversarial factors** — operational criticality, concentration triggers, delayed/threshold behavior, and adversarial dynamics ([§3](#3-criticality-concentration-temporal-and-adversarial-factors))
- **What the System Classification Record must state (dual axes)**
  - **Dependency typing** — applicable **dependency type(s)** (**Dep-A–P** reliance categories) as a distinct axis from impact class ([§4](#4-dependency-types-dep-ap))
  - **Impact-class catalog** — **Class A** through **Class P** impact definitions and scaled duties in **[Part B §§8–13](cs_03_b_system_impact_classifications.md#8-system-impact-classifications)**
  - **Boundaries, timeframes, and resilience** — effective boundaries, survival-relevant timeframes, and class-scaled continuity ([§5](#5-boundaries-timeframes-and-resilience))
- **How class is applied and governed**
  - **Domain mapping and scarce-capacity handling** — published domain crosswalk, ordinary application examples, and API/traffic priority rules ([§6](#6-domain-taxonomy-examples-and-scarce-capacity-handling))
  - **Classification governance** — own, disclose, audit, challenge, update, and correct the System Classification Record; prove the class it states; Class A/B org risk roles live in **[CS-4 — Integrated risk governance (Class A/B)](cs_04_critical_system_stewardship.md#integrated-risk-governance)** ([§7](#7-classification-governance-disclosure-and-challenge))
  - **Joint reading** — CS families, CJS clusters, Protocol A, and Chapter Five meanings co-apply per **[CS-1 — Operates in conjunction with](cs_01_scope_purpose_identifier_rules.md#operates-in-conjunction-with)**

<a id="11-holistic-classification"></a>
**1.1. Holistic classification.**

*In plain terms: do not score a system on one dial — impact, dependency, and risk interact, and scale can turn moderate effects critical.*

Systems do **not** operate along a single dimension. Impact, dependency, and risk interact to produce materially different conditions. A **one-dimensional** framework would over-constrain low-impact systems and under-govern high-risk ones. Dimensions of **actual and reasonably foreseeable** impact must be evaluated **as a whole**:

- **Low direct impact** can still yield high systemic risk through dependency chains
- **Moderate impact** can become critical when scaled
- **Real-world interactions** can produce materially different systemic and existential risk

That evaluation must align governance, responsibility, and rights with performance under real-world and foreseeable conditions.

<a id="12-classification-and-existential-risk"></a>
**1.2. Classification and existential risk.**

*In plain terms: classify for credible worst cases in the system's real environment — and treat irreversible or civilization-scale harm pathways as highest-class stakes.*

Account for expected and credible worst-case conditions in the system's realistic environment:

- Where credible failure modes produce materially higher impact, dependency, or risk, classification must reflect them unless they are **demonstrably excluded** through robust, verifiable constraints
- Where classification is **uncertain**, govern at the **highest plausible** classification until resolved
- Where failure, combination, or aggregation creates credible pathways to irreversible or civilization-scale harm — including collapse of critical system layers or loss of ecological recovery capacity — treat as existential risk
- Systems contributing materially to such risk must be classified and governed at the **highest applicable** level regardless of isolated impact

<a id="13-mandatory-functional-classification"></a>
**1.3. Mandatory, functional classification.**

*In plain terms: every material-impact system must have an honest, challengeable System Classification Record based on what it does — not what operators claim.*

**No** system may claim **reduced obligations**, **exemptions**, or **lower-impact** classification while exerting **material external** effects.

**Classification under CS-3 — System classification and handling** is **mandatory** for all systems with **material impact**. Operators must maintain a [System Classification Record](../core_05_band_continuity.md#system-classification-record-constitutional). That record is **material audited information**: it is independently checked as a sibling audit mode under the **[CJS-3.3 audit process home](../corpus_joint_structure/cjs_03_audit_process.md#cjs-33-audit-process-home)**, between and beside [System Alignment Certification](../core_05_band_continuity.md#system-alignment-certification-constitutional) cycles. Scaled System Classification Record audit duties live in [§7.3](#73-auditability-and-verification). Classification must be:

- **functionally determined** from observed and reasonably foreseeable effects rather than declared intent, structure, or self-description
- **transparent**, **auditable**, and **subject to challenge** under:
  - **Article XV-A** (*Auditability and Observable Evidence*)
  - **Article XV** (*Audit, Transparency, and Independent Verification*)'s verification-access provisions
  - **Article XII-B** (*Right to Challenge, Review, and Redress*)
- **continuously revalidated** per **CJS-3.18** (*data-retention and lifecycle-integrity terms*)

<a id="14-alignment-status-recognition-and-ambiguity-default"></a>
**1.4. Alignment-status recognition and ambiguity default.**

*In plain terms: when official alignment recognition depends on classification, the record must be forum-inspectable — and when class is ambiguous, protect Foundational Rights.*

Where classification, deployment, or continued operation depends on official constitutional alignment status:

- the [System Classification Record](../core_05_band_continuity.md#system-classification-record-constitutional) must support **Integrity** forum recognition or revalidation under `core_11-11_forum.md` **Chapter Eleven** and `corpus_forum.md` **CF-7.2** (*Constitutional alignment recognition and review*)
- where material ecological exposure exists, it must also support **Environment** forum environmental-alignment component review before final recognition, validation, revalidation, or material release from environmental conditions
- forum review must be able to inspect the classification rationale, assumptions, evidence, uncertainty, dependency analysis, ecological exposure analysis where material, and monitoring triggers without relying on operator self-description alone

Where ambiguity exists, default to the level that protects **Foundational Rights** (**Chapter Six, Articles V through IX**), subject to **CJS-3.11** (*distributed and proportional authority terms*) and **CJS-3.7** (*quorum and participatory legitimacy terms*).

CS-3 does not stand alone. Joint reading with CS-2, CS-4, Protocol A, CJS clusters, and Chapter Five meanings is stated in **[CS-1 — Operates in conjunction with](cs_01_scope_purpose_identifier_rules.md#operates-in-conjunction-with)**.

<a id="2-classification-dimensions-and-real-world-application"></a>
## 2. Classification dimensions and real-world application

*In plain terms: first score dependency, risk, and impact together — then interpret that score under real operating conditions and escalate to the highest class those conditions require.*

<a id="21-classification-dimensions"></a>
**2.1. Classification dimensions.**

*In plain terms: rate the system on dependency, risk, and impact together — including dependency chains, interactions, and scale effects — not one dial at a time.*

Classify every material-impact system on these together under real-world and foreseeable operation:

- **Dependency** — how much others rely on the system, and whether workable alternatives exist
  - **dependency chains** upstream and downstream
- **Risk** — harm from failure, misuse, or degradation, including:
  - how **likely** it is
  - how **fast** it arrives
  - how **severe** it is
  - whether it can be **undone**
  - **immediate**, **delayed**, **cumulative**, and **irreversible** effects
- **Impact** — how wide, how large, and how severe the effects are on sentients, environments, and other systems
  - **interaction** effects that produce emergent outcomes
- **Aggregate** effects at scale (actual and foreseeable), including when many similar systems produce cumulative effects that materially change conditions

These labels apply the **Chapter Five** Independent Definitions (*Dependency*, *Risk*, *Material Impact*, including irreversibility where applicable) inside **CS-3 — System classification and handling**. **Chapter Five** owns the meanings corpus-wide. **CS-3** owns how classification uses those meanings.

Where any of those factors materially change the picture, the classification must reflect that change.

<a id="22-real-world-application"></a>
**2.2. Real-world application.**

*In plain terms: read the dimensions against how the system actually runs — then escalate or reclassify when real conditions raise the stakes.*

Classification must match how the system actually operates — not a best-case lab picture. Adjust the finding when dependency chains, interaction effects, aggregate effects, adversarial dynamics, or **threshold** behaviors materially alter conditions.

Use the **highest applicable** classification where credible risk touches **survival-critical** systems, **foundational** infrastructure, or **large-scale** sentient wellbeing. Reclassify when dependency, risk, impact, interaction, or scale changes conditions materially — including through aggregation, coupling, or adversarial dynamics.

<a id="3-criticality-concentration-temporal-and-adversarial-factors"></a>
## 3. Criticality, concentration, temporal, and adversarial factors

*In plain terms: watch time-sensitive harm, concentration of control, delayed tipping points, and adversarial misuse — and reclassify when any of those change the picture.*

<a id="31-concentration-thresholds-and-mitigation-triggers"></a>
**3.1. Concentration thresholds and mitigation triggers.**

Operators must maintain **concentration monitoring** tied to class-scaled obligations, including the following:

- For systems with **material external** impact (especially **Class A, B, and C**), define and maintain **concentration indicators** (e.g. control-share persistence, dependency concentration, interface gatekeeping, allocation-influence concentration)
- Define **trigger thresholds** for escalation, independent review, and mitigation intervention
- Define **mitigation playbooks** proportionate to severity, which may include:
  - authority partitioning
  - interoperability/portability expansion
  - access non-discrimination controls
  - structural separation where required
- When triggers fire, **record and execute** a time-bound mitigation plan
- Failure to define thresholds, disclose concentration status, or implement triggered mitigation is **classification-governance non-compliance** and may require **stricter** reclassification

<a id="32-operational-criticality-threshold"></a>
**3.2. Operational criticality threshold.**

**Critical** vs **non-critical** depends on **time sensitivity** of harm and **viable substitutes under stress**:

- A system is **operationally critical** where loss or degradation would, within **relevant operational timeframes**, cause **material harm** that **cannot** be prevented through available, timely, effective **substitution**
- Where substitution is feasible but **constrained, delayed, or degraded**, classification must reflect the **highest** dependency and risk present under those conditions

<a id="33-temporal-and-systemic-effects"></a>
**3.3. Temporal and systemic effects.**

Assessments must account for the following where they materially alter classification or risk:

- **delayed, cumulative, and probabilistic** effects
- **threshold, tipping-point, or phase-transition** behavior, with classification reflecting **post-threshold** conditions when they materially increase harm, systemic instability, or irreversibility

<a id="34-adversarial-and-strategic-dynamics"></a>
**3.4. Adversarial and strategic dynamics.**

Risk assessment must include the following where they materially alter impact, dependency, or risk:

- **adversarial use**
- **strategic exploitation**
- **coordinated misuse**

<a id="35-reclassification-requirement"></a>
**3.5. Reclassification requirement.**

Systems must undergo **continuous or regularly scheduled** evaluation sufficient to detect material changes within timeframes appropriate to class and risk profile. Whole-system evaluation under **[Chapter Seven §3](../core_07_a_system_alignment_certification_evaluation.md#3-whole-system-certification-evaluation)** is:

- **mandatory at full depth** for **Class A**, **Class B**, and **Class C**
- **mandatory but proportionate** for **Class L** (including lower default periodic cadence and simplified records where permitted)
- **encouraged** for **Class P** while validly **Class P**

For a system claimed to remain **Class P**, that evaluation becomes mandatory upon reclassification to **Class L** or higher, or where the operator voluntarily asserts constitutional compliance for the system.

**System classification** must be **reassessed** whenever material changes alter impact, dependency, or risk. Reclassification must reflect the **highest applicable** classification under updated conditions, including the following:

- **Do** **not** retain a prior classification where underlying conditions no longer support it
- **Reassess** where **scale, reach, or adoption** materially increases
- **Reassess** where **dependency** strengthens, expands, or becomes less substitutable
- **Reassess** where **new couplings** introduce emergent or cross-domain effects
- **Reassess** where **adversarial** dynamics, misuse potential, or threat exposure changes materially
- **Reassess** where **resilience, redundancy, or fallback** is degraded or removed
- **Reassess** where **failure modes** (including delayed or cascading effects) are newly identified or materially revised

Classification reassessment under this subsection must be:

- **verified** on each materially impactful [System Alignment Certification](../core_05_band_continuity.md#system-alignment-certification-constitutional) or revalidation cycle under **[Chapter Seven §2](../core_07_a_system_alignment_certification_evaluation.md#2-system-class-evaluation)** (*System Class Evaluation*) and recorded under **[Chapter Seven Part B §11.1](../core_07_b_system_alignment_certification_record_process.md#111-minimum-record-contents)**
- **reopened** under **[Chapter Seven Part B §16](../core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion)** where a material reassess trigger fires, or where a prior class is retained after underlying conditions no longer support it

Governance timing for acting on these triggers — including prompt reclassification, pre-deployment reassessment where feasible, and failure-to-reclassify non-compliance — is in [§7.5](#75-reclassification-and-continuous-update).

<a id="4-dependency-types-class-ap"></a>
<a id="4-dependency-types-dep-ap"></a>
## 4. Dependency types (Dep-A–P)

*In plain terms: separately record how hard it is to replace the system — Absolute, Operational, Coordination, Limited, or none meaningful — using Dep-A through Dep-P so the dependency axis stays distinct from impact Class A–P, even when the letter bands match.*

**Dual-axis rule:** **Impact classes** use **Class A–P**. **Dependency types** use **Dep-A–P** (same letter band, `Dep-` prefix). This section owns **dependency types** (reliance categories). **[Part B §§8–13](cs_03_b_system_impact_classifications.md#8-system-impact-classifications)** owns **impact classes** (Survival-critical through Personal/private). A [System Classification Record](../core_05_band_continuity.md#system-classification-record-constitutional) must state **both** the applicable **dependency type(s)** and the **impact class**. Matching letter bands **correlate often** but **do not** collapse the axes into one finding.

**Dependency, interaction, and boundary classification overview:** System classification reflects combined impact, dependency, and risk. **Dependency classification** describes structure and strength of reliance, and must account for the following when they materially alter reliance:

- dependency **chains**
- **interaction** and **emergent** effects (reflect **combined** effects; **highest applicable** classification governs)
- **aggregation**
- **substitutability**
- **adversarial** dynamics, including **intentional manipulation**, **coordinated attack**, and **strategic degradation** when they materially alter behavior or risk

All system classifications must:

- **explicitly identify** applicable **dependency type(s)**
- align with the **highest level** present under **normal, degraded, and adversarial** conditions

**Resilience** requirements scale with classification so systems maintain acceptable function under stress, degradation, and partial failure proportional to impact and dependency.

<a id="41-dependency-types-standardized"></a>
**4.1. Dependency types (standardized reliance categories).**

Standardized reliance categories:

- <a id="41-class-a-absolute-dependency"></a><a id="41-dep-a-absolute-dependency"></a>**Dep-A — Absolute dependency** — no viable fallback, redundancy, or substitution within **survival-relevant** timeframes; loss of continuity yields immediate or near-immediate loss of survival conditions
- <a id="42-class-b-operational-dependency"></a><a id="42-dep-b-operational-dependency"></a>**Dep-B — Operational dependency** — required for **normal** functioning of dependents; fallback, redundancy, or substitution exists within survival-relevant timeframes
- <a id="43-class-c-coordination-dependency"></a><a id="43-dep-c-coordination-dependency"></a>**Dep-C — Coordination dependency** — materially shapes coordination, interaction, or outcomes across participants or systems, but is **not** required for core functional operation
- <a id="44-class-l-limited-dependency"></a><a id="44-dep-l-limited-dependency"></a>**Dep-L — Limited dependency** — confined to **bounded** contexts; replaceable within reasonable time and effort without systemic impact
- <a id="45-class-p-no-meaningful-external-dependency"></a><a id="45-dep-p-no-meaningful-external-dependency"></a>**Dep-P — No meaningful external dependency** — contained within a private unit or among voluntary participants; no reliance beyond that boundary

<a id="5-boundaries-timeframes-and-resilience"></a>
## 5. Boundaries, timeframes, and resilience

*In plain terms: decide what counts as “the system” by what it actually affects, say out loud how much time sentients have when it fails, make it tough enough to take a hit, and able to keep going or recover in time.*

- <a id="51-system-boundaries"></a>**System boundaries**
  - Draw the boundary from what the system **actually does** to sentients and other systems — not from who owns it, which jurisdiction claims it, or what the operator’s org chart says
  - Harm or dependence that spills **outside** the operator’s nominal scope still counts as **inside** the system’s **effective boundary**
  - When more sentients or systems depend on it, and substitutes get harder to find, raise the classification and the governance that goes with it
  - Classification uses the **Chapter Five** meanings (*System Boundaries*, *Dependency*, *Material Impact*); it does **not** replace those definitions elsewhere
- <a id="52-sentient-survival-relevant-timeframes"></a>**Sentient survival-relevant timeframes**
  - Use a published, shared, checkable way to define how much time matters for survival when this system fails
  - State those time assumptions in the classification — including any environmental, technological, or local conditions they depend on
- <a id="53-resilience-and-continuity-requirements"></a>**Resilience**
  - Build toughness that matches the class under stress, disruption, partial failure, or attack
  - Match the measures to how bad failure would be
  - Keep the system working well enough under stress and partial failure
  - Stop failure from cascading through systems that depend on it
  - Include backup, fallback, or replacement options scaled to how much others depend on it and how risky failure is
  - Passing a checklist is not enough if the system is brittle, can fail without bound, or cannot stay safe under conditions that should have been expected
- <a id="54-continuity"></a>**Continuity**
  - Keep running, degrade safely, or shut down safely — whichever fits the class and the situation
  - Recover in timeframes that match the class
  - Scale continuity with how much sentients, environments, and the info-sphere are affected; how much others depend on it; and whether harm could cascade or become permanent

<a id="6-domain-taxonomy-examples-and-scarce-capacity-handling"></a>
## 6. Domain taxonomy, ordinary examples, and scarce-capacity handling

*In plain terms: publish a map of real-world domains so sentients can find what is governed, apply ordinary market and intermediary examples honestly, and when capacity is scarce put survival-critical traffic first.*

<a id="61-published-domain-taxonomy-for-regulatory-mapping"></a>
**6.1. Published domain map.**

Adopters and governed institutions should keep a published crosswalk that places major industries and regulatory domains against **CS-3 — System classification and handling** and **CS-4 — Critical system stewardship**. The map helps sentients locate governed scope and compare similar domains — it does **not** replace class, tier, or impact analysis.

At minimum, publish entries for:
- **Agriculture and food** — growing, livestock, fisheries, processing, seeds, fertilizers, pesticides, irrigation, storage, and distribution
- **Mining and extraction** — mining, quarrying, drilling, tailings, waste handling, refining interfaces, and site restoration
- **Built environment** — architecture, construction, structural engineering, building operations, urban systems, building-code integrity, fire safety, and accessibility
- **Energy and utilities** — electricity, fuels, heat, grids, water delivery, wastewater, and comparable utilities
- **Transportation and logistics** — roads, rail, shipping, aviation, ports, warehouses, dispatch, and freight coordination
- **Manufacturing and industry** — production, fabrication, assembly, process safety, and industrial control
- **Medicine and public health** — clinical care, laboratories, trials, drugs, devices, epidemiology, and public-health administration
- **Information, computation, and communications** — software, AI, networks, platforms, telecom, info-sphere infrastructure, media distribution, and coordination infrastructure
- **Finance and insurance** — banking, payments, clearing, credit, underwriting, risk transfer, market infrastructure, and contingent-claim / event-contract markets
- **Education and knowledge** — schools, universities, credentialing, libraries, archives, textbooks, and research institutions
- **Personal-service platforms and intermediaries** — systems that match, dispatch, schedule, settle payment for, or reputation-score in-person personal services, including high-vulnerability contexts

Add more domains where local economies, ecosystems, or dependency make them constitutionally material. Do **not** use a domain label to under-classify a system whose real impact, dependency, or risk is higher than that domain’s usual pattern.

<a id="62-classification-examples-ordinary-application"></a>
**6.2. Ordinary application examples.**

Markets, payment rails, matchers, ranking engines, and other intermediaries stay in scope when sentients depend on them, when they coordinate others at scale, or when they shape what information sentients see and trust.

- **Market-mediated personal services**
  - Systems that match, dispatch, schedule, settle payment for, or reputation-score **in-person** personal services are presumptively material for dependency, safety, coercion risk, and fairness analysis when impact thresholds are approached — especially where intimacy, bodily contact, private-space or in-home access, or isolated work is involved
  - Rights Floor: Chapter Six. Institutional interface: [**CI-19**](../corpus_institutions/ci_19_vulnerable_personal_services_markets_article_xc_interface.md). Stewardship scale: **CS-4 — Critical system stewardship**
- **Contingent claims and event markets**
  - Systems that match counterparties, pool stakes, or settle payments based on outside events are presumptively material for incentive, capture, manipulation, and stability analysis
  - Constitutional direction: [Chapter One §11.5](../core_01_c_stewardship_capacity_principles.md#115-contingent-claims-games-of-chance-and-event-contract-markets). Stewardship scale: **CS-4 — Critical system stewardship**
  - Settlement prices or odds alone are **not** enough to settle truth questions under [**Article XIV**](../core_06-06_rights_part_c.md#article-xiv-info-sphere-integrity) (*Info-Sphere Integrity*) and [**Article XV-A**](../core_06-06_rights_part_c.md#article-xv-a-auditability-and-observable-evidence) (*Auditability and Observable Evidence*)
  - This layer does **not** set licensing, criminal, or tax rules for gambling

<a id="63-scarce-capacity-api-and-traffic-priority-handling"></a>
**6.3. Scarce capacity, APIs, and traffic priority (Class A/B/C).**

When a system offers scarce capacity — network access, compute, model inference, API calls, queue position, bandwidth, or similar throughput that can run short at peak demand — operators must publish **priority rules** scaled to classification and dependency.

- **Class A** traffic and API use gets the highest continuity protection when the request or dependent workflow is survival-critical, Rights-Floor-sustaining, emergency-response, or recovery-critical
  - Throttling, queuing, paid tiers, or commercial prioritization must **not** crowd out the minimum safe capacity Class A continuity needs
  - A narrower emergency cut is allowed only under **Chapter Six, Article XXIII** (*Conflict Resolution, Escalation, and Emergency Proportionality*), and only if it stays time-bounded, auditable, and restoration-triggered
- **Class B** traffic and API use gets enough priority to keep dependent systems running normally and to stop cascading degradation into Class A or broader systemic harm
  - Class B may be queued, rate-limited, or degraded **before** Class A when capacity is genuinely short
  - That degradation must be disclosed, proportionate, and designed around workable fallback or recovery paths
- **Class C** traffic and API use may use ordinary priority tiers, commercial queues, rate limits, or paid high-volume interfaces where they do not create hidden exclusion, capture, or de facto operational necessity
  - If recurring peak shortages make Class C access practically necessary for dependent Class A or Class B workflows, re-evaluate both classification and priority rules under **CS-3 — System classification and handling**

<a id="64-commercial-use-surcharges-and-reinvestment-interface"></a>
**6.4. Commercial-use surcharges and reinvestment.**

- Operators may charge commercial-scale API users, high-volume business interfaces, premium latency tiers, or automated bulk consumers for the extra burden they put on shared capacity
- Those charges must be disclosed, proportionate, contestable where material, and consistent with `corpus_institutions.md` **CI-10** (*Public revenue, fees, recurring charges, and billing integrity*)
- Revenue should be traceably available for operations, security, resilience, compute expansion, remedy capacity, and ecosystem/public-good support under **Protocol S5**
- Charges must **not** become a hidden way to deny baseline participation or lock in chokepoint control

<a id="7-classification-governance-disclosure-and-challenge"></a>
## 7. Classification governance, disclosure, and challenge

*In plain terms: when certification runs, it must produce or verify the System Classification Record and put that file in the certification case file — then operators must keep owning, disclosing, auditing, challenging, updating, and proving that same file. System Classification Record audits under this section are a sibling audit mode; system alignment certification is one especially large audit process that consumes this file when SAC runs — not the sole home of auditing.*

**System alignment certification (SAC) bridge.** When [System Alignment Certification](../core_05_band_continuity.md#system-alignment-certification-constitutional) runs for a materially impactful system, **[Chapter Seven §2](../core_07_a_system_alignment_certification_evaluation.md#2-system-class-evaluation)** (*System Class Evaluation*) must **produce or verify** the [System Classification Record](../core_05_band_continuity.md#system-classification-record-constitutional) and include it (or its required contents) in the [System Certification Record](../core_05_band_continuity.md#system-certification-record-constitutional) under **[Part B §11.1](../core_07_b_system_alignment_certification_record_process.md#111-minimum-record-contents)**. Under the **oversight** Tetrad leg, that SAC cycle is one especially large audit process among others; [§7.3](#73-auditability-and-verification) System Classification Record audits continue between and beside certification cycles.

Operators must maintain that System Classification Record for every system with **material impact**. It is the CS-3 class file — not a marketing label, and **not** the full System Certification Record. Dual-axis contents, functional determination, transparency baseline, and ambiguity defaults are owned in [§1](#1-purpose-and-scope) ([§1.3](#13-mandatory-functional-classification), [§1.4](#14-alignment-status-recognition-and-ambiguity-default)).

Certification must check that:

- the assigned class matches observed and reasonably foreseeable **impact**, **dependency**, and **risk**
- reassessment under [§3.5](#35-reclassification-requirement) has been applied where triggers fire
- class-scaled assurance matches CS-3 and **[Protocol A](cs_protocol_a_system_design_testing_verification_deployment.md)**

The following are **certification defects** under Chapter Seven §2 and **[Part B §16](../core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion)** — not paperwork nits:

- misclassification (understating impact, dependency, or risk)
- modularization to dodge a higher class
- keeping a stale class after conditions change
- failure to reassess when [§3.5](#35-reclassification-requirement) triggers fire

Where the facts support it, those defects may also supply verified input toward adverse standing findings in [Chapter Eight](../core_08-08_standing_assessment.md#chapter-eight-compliance-violation-and-standing-model).

This section owns what operators must **do with** the System Classification Record between and during those certification cycles:

| Duty | Acts on the System Classification Record by… |
| --- | --- |
| [§7.1](#71-responsibility-for-classification) | **Owning** it |
| [§7.2](#72-disclosure-requirements) | **Disclosing** it |
| [§7.3](#73-auditability-and-verification) | **Auditing** it |
| [§7.4](#74-challenge-and-contestability) | **Challenging** it |
| [§7.5](#75-reclassification-and-continuous-update) | **Updating** it |
| [§7.6](#76-misclassification-and-evasion) | **Correcting** it |
| [§7.7](#77-default-and-precautionary-classification) | **Defaulting** uncertain fields / barring quiet lowering |
| [§7.8](#78-integrated-risk-governance) | **Pointing** Class A/B org risk roles to CS-4 |
| [§7.9](#79-class-scaled-assurance-and-supporting-infrastructure) | **Proving** the class it states |

<a id="71-responsibility-for-classification"></a>
**7.1. Own the System Classification Record.**

*System Classification Record duty:* keep one accountable owner for the file so System Alignment Certification always has a responsible party to verify against — forum supervision does not absorb that ownership.

The **operator** stays responsible for a correct System Classification Record:

- even when work is delegated, automated, or done by a third party
- even when a forum is supervising certification

The operator (or other responsible party) must:

- decide and document the class across **all required dimensions**
- assign the right class or classes
- justify the finding **in the System Classification Record**

Forum verification under Chapter Seven §2 does **not** transfer ownership of the System Classification Record away from the operator.

<a id="72-disclosure-requirements"></a>
**7.2. Disclose the System Classification Record.**

*System Classification Record duty:* publish a usable view of the file so oversight and System Alignment Certification can inspect class honestly — when SAC runs, that view is what **[Part B §12](../core_07_b_system_alignment_certification_record_process.md#12-transparency-auditability-and-contestability)** reconstructability rests on.

- Do **not** hide, scatter, or cherry-pick the System Classification Record so sentients cannot understand it
- Disclose the record (or an equivalent public view of it) to affected sentients:
  - at a depth that matches **system impact**
  - reachable without expert tools or heroic effort

**For Class A, B, and C**, disclosure of the System Classification Record must also meet:

- [Public Oversight Baseline Disclosure](../core_05_band_oversight.md#public-oversight-baseline-disclosure) under the **Type O** default in **CS-2 — Information types and handling**
- the strongest feasible **Type O** public substitutes when protected (non-**Type O**) classifications block raw disclosure

<a id="73-auditability-and-verification"></a>
**7.3. Audit the System Classification Record.**

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Read with: **[CJS-3.3 audit process home](../corpus_joint_structure/cjs_03_audit_process.md#cjs-33-audit-process-home)** (*shared process — what / why / how / when*); **[CJS-3.4](../corpus_joint_structure/cjs_03o_oversight_operations.md#cjs-34-audit-process-output-disclosure)** (*access tiers and output disclosure*); **CJS-3.5** (*claim checking*); **[CS-2 — Information types and handling](cs_02_a_information_types_and_handling.md)** (*typing*).
- This subsection does **not** relocate the process home or Rights Floor (**Article XV** / **Article XV-A**).

</details>

<br>

*System Classification Record duty:* run the independent **System Classification Record audit** named in the **[CJS-3.3 audit process home](../corpus_joint_structure/cjs_03_audit_process.md#cjs-33-sibling-modes)**.

- **Required:** Auditability of the System Classification Record is required under [§1.3](#13-mandatory-functional-classification).
- **What to check:** the class on file matches how the system actually behaves — inspect real behavior, outputs, and effects, not only claims in the file.
- **Why (when SAC runs):** so System Alignment Certification under **[Chapter Seven §2](../core_07_a_system_alignment_certification_evaluation.md#2-system-class-evaluation)** can verify substance.
- **Why (between cycles):** so class honesty stays checkable outside those SAC cycles too.
- **When:** On a schedule that matches impact and how fast the system changes, including the triggers in the process home and in [§3.5](#35-reclassification-requirement) / [§7.5](#75-reclassification-and-continuous-update).
- **For Class A, B, and C:** System Classification Record audits must be able to catch misclassification, under-classification, and unreported behavior changes. Independent or third-party audit paths must remain available under **CJS-3.4**; "where feasible" does **not** make those paths soft-optional at these classes.

<a id="74-challenge-and-contestability"></a>
**7.4. Challenge the System Classification Record.**

*System Classification Record duty:* let affected sentients contest the file.

- **Required:** The right to challenge the System Classification Record is required under [§1.3](#13-mandatory-functional-classification) (**Article XII-B**).
- **What systems must offer:** challenge routes sentients can actually use; good-faith, timely review; and reasoned answers — including evidence of misclassification or hidden impact, and requests for review or reclassification of the record.
- **Why:** so class findings that feed System Alignment Certification stay challengeable under **Article XII-B** and, when inside an active certification record, under **[Part B §§12 and 14](../core_07_b_system_alignment_certification_record_process.md#12-transparency-auditability-and-contestability)**.
- **For Class A, B, and C:** if an internal dispute about the System Classification Record cannot be resolved, escalation to external or independent review must remain available.
- **When the challenge concerns classification assumptions, class assignment, or related evidence inside an active System Certification Record:** the contestability chain in **[Chapter Seven Part B §12](../core_07_b_system_alignment_certification_record_process.md#12-transparency-auditability-and-contestability)** and **[§14](../core_07_b_system_alignment_certification_record_process.md#14-supervisory-sequence-and-contestability-chain)** applies, and material challenges may reopen review under **[Part B §16](../core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion)**.

<a id="75-reclassification-and-continuous-update"></a>
**7.5. Update the System Classification Record.**

*System Classification Record duty:* revise the file when conditions change — and keep the revalidation cadence stated on it current — so each System Alignment Certification or revalidation cycle under **[Chapter Seven §2](../core_07_a_system_alignment_certification_evaluation.md#2-system-class-evaluation)** can verify an honest class.

What triggers a fresh look, and how deep the look must go, live in [§3.5](#35-reclassification-requirement). This subsection owns **when** operators must update the System Classification Record:

- **before** rolling out materially bigger capabilities, **where feasible**
- **promptly** once changed conditions are recognized
- as part of **periodic review**, including each materially impactful [System Alignment Certification](../core_05_band_continuity.md#system-alignment-certification-constitutional) or revalidation cycle under **[Chapter Seven §2](../core_07_a_system_alignment_certification_evaluation.md#2-system-class-evaluation)**

The System Classification Record must state a **revalidation cadence scaled to class** (and monitoring triggers). How certification verifies that cadence and §3.5 reassessment, and treats failure to update after material change as a **certification defect**, live under **[Chapter Seven §2](../core_07_a_system_alignment_certification_evaluation.md#2-system-class-evaluation)** and **[Part B §16](../core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion)** — see also the [§7 SAC bridge](#7-classification-governance-disclosure-and-challenge).

<a id="76-misclassification-and-evasion"></a>
**7.6. Correct the System Classification Record.**

*System Classification Record duty:* correct the file when misclassification or evasion is found.

Shared correction, precautionary-default, and no-quiet-lowering discipline live in **[CJS-3.15 — Material classification-record honesty](../corpus_joint_structure/cjs_03a_accountability_operations.md#cjs-315-material-classification-record-honesty)**. This subsection applies that discipline to the System Classification Record:

- Understatement of impact, dependency, or risk, and claims of lighter duties from intent or nominal scope, are already barred under [§1.3](#13-mandatory-functional-classification).
- Do **not** split or modularize a system just to dodge a higher class on the System Classification Record.
- When misclassification or evasion is found, **correct** the System Classification Record.

How those failures count as **certification defects**, and any standing bridge, live under **[Chapter Seven §2](../core_07_a_system_alignment_certification_evaluation.md#2-system-class-evaluation)**, **[Part B §§15–16](../core_07_b_system_alignment_certification_record_process.md#15-relationship-to-standing)**, and the [§7 SAC bridge](#7-classification-governance-disclosure-and-challenge).

<a id="77-default-and-precautionary-classification"></a>
**7.7. Default uncertain System Classification Record fields.**

*System Classification Record duty:* when the file is incomplete or contested, apply the precautionary default and state any precautionary class relied on — do not quietly lower class.

Shared discipline lives in **[CJS-3.15 — Material classification-record honesty](../corpus_joint_structure/cjs_03a_accountability_operations.md#cjs-315-material-classification-record-honesty)**. CS-3 ambiguity and uncertainty defaults (Foundational Rights protection; highest-plausible / worst-case accounting) are owned in [§1.2](#12-classification-and-existential-risk) and [§1.4](#14-alignment-status-recognition-and-ambiguity-default). This subsection applies them to the System Classification Record:

- State any **precautionary class** relied on, and any conditions pending resolution, **in the System Classification Record**.
- **Lowering** a class on the System Classification Record requires evidence, documentation, and successful review under **CJS-3.15** (*Accountability: structural review, correction urgency, and disclosure terms*):
  - stays open to Integrity forum review under [§1.4](#14-alignment-status-recognition-and-ambiguity-default), Chapter Eleven, and `corpus_forum.md` **CF-7.2** (*Constitutional alignment recognition and review*) when a credible alignment concern is raised
  - Passing an internal check alone does **not** defeat a timely forum challenge
  - Where recognition or continued reliance already rests on a System Certification Record, a material request to lower class must also reopen certification review under **[Chapter Seven Part B §16](../core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion)** — it is not a System Classification Record-only change

<a id="78-integrated-risk-governance"></a>
**7.8. Org roles that protect the System Classification Record (Class A/B).**

*System Classification Record duty:* Class A/B org risk roles that protect classification honesty live in **[CS-4 — Integrated risk governance (Class A/B)](cs_04_critical_system_stewardship.md#integrated-risk-governance)**. Those roles surround the System Classification Record; they are **not** extra fields inside it, and they do **not** replace forum-supervised SAC or the SCR field duties in [§7.1](#71-responsibility-for-classification)–[§7.7](#77-default-and-precautionary-classification) and [§7.9](#79-class-scaled-assurance-and-supporting-infrastructure).

<a id="79-class-scaled-assurance-and-supporting-infrastructure"></a>
<a id="710-class-scaled-assurance-and-supporting-infrastructure"></a>
**7.9. Prove the class stated in the System Classification Record.**

*System Classification Record duty:* show that assurance depth matching the record’s class was **actually evaluated**, not merely claimed, so **[Chapter Seven §2](../core_07_a_system_alignment_certification_evaluation.md#2-system-class-evaluation)** can verify that proof on the System Certification Record.

Who must do what:

- **Operator** — prove the class the System Classification Record states:
  - show that assurance depth matching that class was **actually evaluated**, not merely claimed
  - scale resilience, continuity, and supporting-infrastructure toughness to that class under [§5](#5-boundaries-timeframes-and-resilience)
  - do **not** treat technical-forum measurements or tests as a substitute for that evaluation duty
- **Technical forums** — may supply measurements and tests that feed the proof; they do **not** absorb the operator’s evaluation duty
- **Certification under Chapter Seven §2** — when System Alignment Certification runs, confirm and record:
  - that class-scaled assurance, infrastructure robustness, and regression coverage match CS-3 and Protocol A for the assigned class
  - any material gaps on the System Certification Record under **[Part B §11.1](../core_07_b_system_alignment_certification_record_process.md#111-minimum-record-contents)**
- **Protocol A** — owns regression scope, results, known failures, remediations, and accepted residual risk for each recertification or revalidation cycle (**[Protocol A — System Design, Testing, Verification, and Deployment](cs_protocol_a_system_design_testing_verification_deployment.md)** (*Recertification, regression testing, and certification defects*)), read with **corpus_joint_structure.md** (**CJS-3.19** through **CJS-3.23** and related clusters)
- **Defects** — skipping required regression, relying on outdated results, or leaving known breaks unfixed are certification defects under Protocol A and Chapter Seven §2 — distinct from, but often concurrent with, System Classification Record defects under [§7.6](#76-misclassification-and-evasion)

<a id="79-high-dependency-private-chokepoints"></a>
Private chokepoint access-continuity duties (payments, identity, compute, messaging, hosting, distribution, discovery, and similar layers) live in **[CS-4 — Critical system stewardship](cs_04_critical_system_stewardship.md#private-chokepoint-access-continuity)** (relocated from former §7.9).

---

**Previous file:** [cs_02_b_data_classifications.md](cs_02_b_data_classifications.md)

**Next file:** [cs_03_b_system_impact_classifications.md](cs_03_b_system_impact_classifications.md)
