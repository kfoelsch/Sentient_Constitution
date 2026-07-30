<a id="cs-3-part-a-system-classification-machinery"></a>
## CS-3, Part A: System classification machinery

<details>
<summary><strong><span style="color: #2563eb;">Corpus placement (non-operative): file structure and reading rules</span></strong></summary>

> The following content is **reader guidance only**. It does not add, remove, or narrow binding obligations elsewhere in this file or in other CS-3 parts.
>
> This file contains **CS-3, Part A** — purpose and scope, classification dimensions, criticality and concentration factors, **dependency types** (**Class A–P** reliance categories), boundaries / timeframes / resilience, domain taxonomy and scarce-capacity handling, and classification governance (**§§1–7**). **Part B** — system **impact** classifications (**Class A** through **Class P**) — is in [`cs_03_b_system_impact_classifications.md`](cs_03_b_system_impact_classifications.md).

</details>

<br>

**CS-3, Part A**, owns **classification machinery**: how to determine impact, dependency, and risk; how to type reliance; how to keep classification honest; and how governance, disclosure, and challenge work. Canonical **impact-class** definitions and per-class scaled duties are in **[Part B](cs_03_b_system_impact_classifications.md#cs-3-part-b-system-impact-classifications)**.

*In plain terms: Part A says how to classify systems honestly across impact, dependency, and risk — Part B names the impact classes themselves and what each class must do.*

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Read with: Integrative Materiality ([Materiality Determination](../core_05defs_oversight.md#materiality-determination)) (*Materiality gate for class scaling*); [Classification Record](../core_05defs_continuity.md#classification-record-constitutional); [Chapter Seven §2 System Class Evaluation](../core_07_a_system_alignment_certification_evaluation.md#2-system-class-evaluation); [Protocol A — System Design, Testing, Verification, and Deployment](cs_protocol_a_system_design_testing_verification_deployment.md) (*recertification and regression testing*); [CS-1 — Operates in conjunction with](cs_01_scope_purpose_identifier_rules.md#operates-in-conjunction-with).

</details>

<br>

**Constitutional index (abridged)**
- Topic-level routing and cited authorities remain in subsection text and cross-references.
- Canonical owner map: **CJS-2.1** (*Topic router (stable IDs)*) and `doc_architecture.md` section 4.

<a id="1-purpose-and-scope"></a>
### 1. Purpose and scope

*In plain terms: classify systems by what they actually do and what can go wrong — not by what operators say they are — and keep that classification challengeable and revalidated in a Classification Record.*

**CS-3 — System classification and handling** is the systems-layer rulebook for assigning and governing system class from real-world effects. Obligations **scale** with impact and dependency. Classification **cannot evade** constitutional requirements. For every system with **material impact**, CS-3 requires a [Classification Record](../core_05defs_continuity.md#classification-record-constitutional) stating dual-axis findings (impact class and dependency type(s)), rationale, assumptions, uncertainty, and monitoring or revalidation triggers. When [System Alignment Certification](../core_05defs_continuity.md#system-alignment-certification-constitutional) runs, that record must be produced or verified and included in the [System Alignment Certification Record](../core_05defs_continuity.md#system-alignment-certification-record-constitutional).

CS-3 implements:

- **How class is determined**
  - **Holistic multi-dimension classification** — evaluate impact, dependency, and risk together under real and foreseeable conditions ([§1.1](#11-holistic-classification); [§2](#2-classification-dimensions-and-interpretive-requirement))
  - **Existential and worst-case accounting** — classify to the highest plausible level where credible failure modes or civilization-scale harm pathways exist ([§1.2](#12-classification-and-existential-risk))
  - **Mandatory functional classification** — class follows observed and reasonably foreseeable effects, not intent or self-description; remains transparent, auditable, challengeable, and continuously revalidated in a Classification Record ([§1.3](#13-mandatory-functional-classification))
  - **Alignment-status recognition and ambiguity default** — the Classification Record must support forum recognition or revalidation when official alignment status is required; ambiguity defaults to protecting Foundational Rights ([§1.4](#14-alignment-status-recognition-and-ambiguity-default))
  - **Criticality, concentration, temporal, and adversarial factors** — operational criticality, concentration triggers, delayed/threshold behavior, and adversarial dynamics ([§3](#3-criticality-concentration-temporal-and-adversarial-factors))
- **What the Classification Record must state (dual axes)**
  - **Dependency typing** — applicable **dependency type(s)** (**Class A–P** reliance categories) as a distinct axis from impact class ([§4](#4-dependency-types-class-ap))
  - **Impact-class catalog** — **Class A** through **Class P** impact definitions and scaled duties in **[Part B §8](cs_03_b_system_impact_classifications.md#8-system-impact-classifications)**
  - **Boundaries, timeframes, and resilience** — effective boundaries, survival-relevant timeframes, and class-scaled continuity ([§5](#5-boundaries-timeframes-and-resilience))
- **How class is applied and governed**
  - **Domain mapping and scarce-capacity handling** — published domain crosswalk, ordinary application examples, and API/traffic priority rules ([§6](#6-domain-taxonomy-examples-and-scarce-capacity-handling))
  - **Classification governance** — operator responsibility, disclosure, audit, challenge, reclassification, and class-scaled assurance ([§7](#7-classification-governance-disclosure-and-challenge))
  - **Joint reading** — CS families, CJS clusters, Protocol A, and Chapter Five meanings co-apply per **[CS-1 — Operates in conjunction with](cs_01_scope_purpose_identifier_rules.md#operates-in-conjunction-with)**

<a id="11-holistic-classification"></a>
**1.1. Holistic classification.**

*In plain terms: do not score a system on one dial — impact, dependency, and risk interact, and scale can turn moderate effects critical.*

Systems do **not** operate along a single dimension. Impact, dependency, and risk interact to produce materially different conditions. A **one-dimensional** framework would over-constrain low-impact systems and under-govern high-risk ones. Dimensions of **actual and reasonably foreseeable** impact must be evaluated **as a whole**:

- **Low direct impact** can still yield high systemic risk through dependency chains
- **Moderate impact** can become critical when scaled
- **Real-world interactions** can produce materially different systemic and existential risk

**That** evaluation must align governance, responsibility, and rights with performance under real-world and foreseeable conditions.

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

*In plain terms: every material-impact system must have an honest, challengeable Classification Record based on what it does — not what operators claim.*

**No** system may claim **reduced obligations**, **exemptions**, or **lower-impact** classification while exerting **material external** effects.

**Classification under CS-3 — System classification and handling** is **mandatory** for all systems with **material impact**. Operators must maintain a [Classification Record](../core_05defs_continuity.md#classification-record-constitutional). Classification must be:

- **functionally determined** from observed and reasonably foreseeable effects rather than declared intent, structure, or self-description
- **transparent**, **auditable**, and **subject to challenge** under:
  - **Article XV-A** (*Auditability and Observable Evidence*)
  - **Article XV** (*Audit, Transparency, and Independent Verification*)'s verification-access provisions
  - **Article XII-B** (*Right to Challenge, Review, and Redress*)
- **continuously revalidated** per **CJS-5.18** (*data-retention and lifecycle-integrity terms*)

<a id="14-alignment-status-recognition-and-ambiguity-default"></a>
**1.4. Alignment-status recognition and ambiguity default.**

*In plain terms: when official alignment recognition depends on classification, the record must be forum-inspectable — and when class is ambiguous, protect Foundational Rights.*

Where classification, deployment, or continued operation depends on official constitutional alignment status:

- the [Classification Record](../core_05defs_continuity.md#classification-record-constitutional) must support **Integrity** forum recognition or revalidation under `core_11-11_forum.md` **Chapter Eleven** and `corpus_forum.md` **CF-7.2** (*Constitutional alignment recognition and review*)
- where material ecological exposure exists, it must also support **Environment** forum environmental-alignment component review before final recognition, validation, revalidation, or material release from environmental conditions
- forum review must be able to inspect the classification rationale, assumptions, evidence, uncertainty, dependency analysis, ecological exposure analysis where material, and monitoring triggers without relying on operator self-description alone

Where ambiguity exists, default to the level that protects **Foundational Rights** (**Chapter Six, Articles V through IX**), subject to **CJS-5.11** (*distributed and proportional authority terms*) and **CJS-5.7** (*quorum and participatory legitimacy terms*).

CS-3 does not stand alone. Joint reading with CS-2, CS-4, Protocol A, CJS clusters, and Chapter Five meanings is stated in **[CS-1 — Operates in conjunction with](cs_01_scope_purpose_identifier_rules.md#operates-in-conjunction-with)**.

<a id="2-classification-dimensions-and-interpretive-requirement"></a>
### 2. Classification dimensions and interpretive requirement

*In plain terms: score impact, dependency, and risk together under real operating conditions — then escalate to the highest class that those conditions require.*

**Classification dimensions:** Evaluate in aggregate when similar systems at scale produce cumulative effects that materially alter system conditions (combined impact, dependency, risk, and interaction context under real-world and foreseeable operation).

Classify by **Impact** — scope, scale, and severity of effects on sentients, environments, and other systems.

Classify by **Dependency** — extent of reliance on the system evaluated, including availability and viability of alternatives.

Classify by **Risk** — likelihood, speed, severity, and reversibility of harm from failure, misuse, or degradation, including immediate, delayed, cumulative, and irreversible effects. These labels operationalize **Chapter Five** Independent Definitions (*Material Impact*, *Dependency*, *Risk*, including irreversibility where applicable) for **CS-3 — System classification and handling**.

**Chapter Five** governs meaning corpus-wide.

**CS-3 — System classification and handling** governs how classification applies those meanings.

Evaluation must account for **aggregate** effects at scale (actual and foreseeable). **It** must account for **interaction** effects with emergent outcomes. **It** must account for **dependency chains** (upstream and downstream).

Reflect material alterations in classification.

**Interpretive requirement:** Classification must reflect **real-world** operating conditions.

Adjust where aggregate effects, dependency chains, interaction effects, adversarial dynamics, or **threshold** behaviors materially alter conditions.

Escalate to the **highest applicable** classification where credible risk touches **survival-critical** systems, **foundational** infrastructure, or **large-scale** sentient wellbeing.

Reclassify where changes in scale, dependency, interaction, or risk alter conditions materially—including aggregation, coupling, or adversarial dynamics.

<a id="3-criticality-concentration-temporal-and-adversarial-factors"></a>
### 3. Criticality, concentration, temporal, and adversarial factors

*In plain terms: watch time-sensitive harm, concentration of control, delayed tipping points, and adversarial misuse — and reclassify when any of those change the picture.*

<a id="31-concentration-thresholds-and-mitigation-triggers"></a>
**3.1. Concentration thresholds and mitigation triggers.**

Include **concentration monitoring** tied to class-scaled obligations.

For systems with **material external** impact (especially **Class A, B, and C**), operators must define and maintain **concentration indicators** (e.g. control-share persistence, dependency concentration, interface gatekeeping, allocation-influence concentration).

**They must** define **trigger thresholds** for escalation, independent review, and mitigation intervention.

**They must** define **mitigation playbooks** proportionate to severity. **Those** playbooks may include authority partitioning, interoperability/portability expansion, access non-discrimination controls, and structural separation where required.

When triggers fire, **record and execute** a time-bound mitigation plan. Failure to define thresholds, disclose concentration status, or implement triggered mitigation is **classification-governance non-compliance** and may require **stricter** reclassification.

<a id="32-operational-criticality-threshold"></a>
**3.2. Operational criticality threshold.**

**Critical** vs **non-critical** depends on **time sensitivity** of harm and **viable substitutes under stress**.

A system is **operationally critical** where loss or degradation would, within **relevant operational timeframes**, cause **material harm** that **cannot** be prevented through available, timely, effective **substitution**.

Where substitution is feasible but **constrained, delayed, or degraded**, classification must reflect the **highest** dependency and risk present under those conditions.

<a id="33-temporal-and-systemic-effects"></a>
**3.3. Temporal and systemic effects.**

Assessments must include **delayed, cumulative, and probabilistic** effects where they materially alter classification or risk. Where systems exhibit **threshold, tipping-point, or phase-transition** behavior, classification must reflect **post-threshold** conditions when they materially increase harm, systemic instability, or irreversibility.

<a id="34-adversarial-and-strategic-dynamics"></a>
**3.4. Adversarial and strategic dynamics.**

Risk assessment must include **adversarial use**, **strategic exploitation**, and **coordinated misuse** where they materially alter impact, dependency, or risk.

<a id="35-reclassification-requirement"></a>
**3.5. Reclassification requirement.**

Systems must undergo **continuous or regularly scheduled** evaluation sufficient to detect material changes within timeframes appropriate to class and risk profile. Whole-system evaluation under **Chapter Seven §3** is **mandatory at full depth** for **Class A**, **Class B**, and **Class C**; **mandatory but proportionate** for **Class L** (including lower default periodic cadence and simplified records where permitted); and **encouraged** for **Class P** while validly **Class P**. For a system claimed to remain **Class P**, that evaluation becomes mandatory upon reclassification to **Class L** or higher, or where the operator voluntarily asserts constitutional compliance for the system.

**System classification** must be **reassessed** whenever material changes alter impact, dependency, or risk. Reclassification must reflect the **highest applicable** classification under updated conditions.

**Do** **not** retain a prior classification where underlying conditions no longer support it.

**Reassess** where **scale, reach, or adoption** materially increases.

**Reassess** where **dependency** strengthens, expands, or becomes less substitutable.

**Reassess** where **new couplings** introduce emergent or cross-domain effects.

**Reassess** where **adversarial** dynamics, misuse potential, or threat exposure changes materially.

**Reassess** where **resilience, redundancy, or fallback** is degraded or removed.

**Reassess** where **failure modes** (including delayed or cascading effects) are newly identified or materially revised.

<a id="4-dependency-types-class-ap"></a>
### 4. Dependency types (Class A–P)

*In plain terms: separately record how hard it is to replace the system — Absolute, Operational, Coordination, Limited, or none meaningful — using the same Class letters as impact classes, without treating matching letters as the same finding.*

**Dual-axis rule:** **Class A–P** letters label **two distinct axes** under CS-3. This section owns **dependency types** (reliance categories). **[Part B §8](cs_03_b_system_impact_classifications.md#8-system-impact-classifications)** owns **impact classes** (Survival-critical through Personal/private). A [Classification Record](../core_05defs_continuity.md#classification-record-constitutional) must state **both** the applicable **dependency type(s)** and the **impact class**. Matching letters **correlate often** but **do not** collapse the axes into one finding.

**Dependency, interaction, and boundary classification overview:** System classification reflects combined impact, dependency, and risk. **Dependency classification** describes structure and strength of reliance.

Where interaction produces **emergent** effects that materially alter conditions, reflect **combined** effects. **Highest applicable** classification governs.

Dependency classification must account for chains, interaction, aggregation, substitutability, and adversarial dynamics when they materially alter reliance.

All system classifications must **explicitly identify** applicable **dependency type(s)** and align with the **highest level** present under **normal, degraded, and adversarial** conditions.

Include **intentional manipulation**, **coordinated attack**, and **strategic degradation** when they materially alter behavior or risk.

**Resilience** requirements scale with classification so systems maintain acceptable function under stress, degradation, and partial failure proportional to impact and dependency.

**Dependency types** (standardized reliance categories):

<a id="41-class-a-absolute-dependency"></a>
**4.1. Class A — Absolute dependency.**

No viable fallback, redundancy, or substitution within **survival-relevant** timeframes.

Loss of continuity yields immediate or near-immediate loss of survival conditions.

<a id="42-class-b-operational-dependency"></a>
**4.2. Class B — Operational dependency.**

Required for **normal** functioning of dependents, but fallback/redundancy/substitution exists within survival-relevant timeframes.

<a id="43-class-c-coordination-dependency"></a>
**4.3. Class C — Coordination dependency.**

Materially shapes coordination, interaction, or outcomes across participants or systems, but **not** required for core functional operation.

<a id="44-class-l-limited-dependency"></a>
**4.4. Class L — Limited dependency.**

Bounded contexts; replaceable within reasonable time and effort without systemic impact.

<a id="45-class-p-no-meaningful-external-dependency"></a>
**4.5. Class P — No meaningful external dependency.**

Contained within a private unit or among voluntary participants; no reliance beyond that boundary.

<a id="5-boundaries-timeframes-and-resilience"></a>
### 5. Boundaries, timeframes, and resilience

*In plain terms: draw the system boundary from real effects, state survival-relevant time assumptions out loud, and keep resilience proportional to class and failure consequences.*

<a id="51-system-boundaries"></a>
**5.1. System boundaries.**

Define from **actual impact and dependency**, not formal ownership, jurisdiction, or operational scope alone.

**Externalized** effects that materially impact sentients or systems lie within the **effective boundary**.

As dependency strengthens and substitutability falls, escalate classification and governance. This rule applies **Chapter Five** (*System Boundaries*, *Dependency*, *Material Impact*) in the classification context. **It** must **not** substitute for those Independent Definitions elsewhere.

<a id="52-sentient-survival-relevant-timeframes"></a>
**5.2. Sentient survival-relevant timeframes.**

Under **CS-3 — System classification and handling**, define by an **external, standardized, auditable** framework. Systems must **explicitly reference** timeframe assumptions used in classification, including environmental, technological, or contextual dependencies.

<a id="53-resilience-and-continuity-requirements"></a>
**5.3. Resilience and continuity requirements.**

Maintain **resilience proportional** to classification—continued operation, graceful degradation, or safe suspension under stress, disruption, partial failure, or adversarial pressure.

Measures must match classification and **failure consequences**.

Resilience must support **acceptable function** under stress, partial failure, and degradation. **It** must **prevent uncontrolled propagation** across dependents. **It** must **recover** within timeframes consistent with classification. **It** must provide **redundancy, fallback, or substitution** proportional to dependency and risk.

Scale resilience with **impact** on sentients, environment, and info-sphere.

**Also** scale with **stakeholder dependency**.

**Also** scale with **cascading or irreversible** harm potential.

Systems cannot satisfy formal requirements while **structurally fragile**, prone to **unbounded failure**, or unable to maintain safe operation under **reasonably foreseeable** conditions.

<a id="6-domain-taxonomy-examples-and-scarce-capacity-handling"></a>
### 6. Domain taxonomy, ordinary examples, and scarce-capacity handling

*In plain terms: publish a domain map for finding governed scope, apply ordinary market/intermediary examples honestly, and prioritize scarce API/traffic capacity by class.*

<a id="61-published-domain-taxonomy-for-regulatory-mapping"></a>
**6.1. Published domain taxonomy for regulatory mapping.**

Adopting instruments and governed institutions should maintain a published crosswalk that locates major industries and regulatory domains against CS-3 — System classification and handling classification and CS-4 — Critical system stewardship stewardship duties. This taxonomy is for locating governed scope and comparable domains; it does **not** replace class, tier, or impact analysis. At minimum, the published map should include:
- **Agriculture and food systems** — cultivation, livestock, fisheries, food processing, seed systems, fertilizers, pesticides, irrigation, storage, and distribution;
- **Mining and extractive industries** — mining, quarrying, drilling, tailings, waste handling, refining interfaces, and site restoration;
- **Built environment** — architecture, construction, structural engineering, building operations, urban systems, building-code integrity, fire safety, and accessibility;
- **Energy and utilities** — electricity, fuels, heat, grids, water delivery, wastewater, and comparable utility infrastructure;
- **Transportation and logistics** — roads, rail, shipping, aviation, ports, warehouses, dispatch, and freight coordination;
- **Manufacturing and industrial systems** — industrial production, fabrication, assembly, process safety, and industrial control environments;
- **Medicine and public health** — clinical care, laboratories, trials, drugs, devices, epidemiology, and public-health administration;
- **Information, computation, and communications** — software, AI, networks, platforms, telecom, info-sphere infrastructure, media-distribution, and coordination infrastructure;
- **Finance and insurance** — banking, payments, clearing, credit, underwriting, risk transfer, market infrastructure, and contingent-claim / event-contract markets;
- **Education and knowledge institutions** — schools, universities, credentialing, libraries, archives, textbooks, and research institutions;
- **Personal-service platforms and intermediaries** — systems that match, dispatch, schedule, settle payment for, or reputation-score in-person personal services, including high-vulnerability and **Article X-C** (*Adult consensual commercial sexual services and sexual exploitation*) contexts.

Additional domains may be published where local economies, ecosystems, or dependency structure make them constitutionally material. Domain labels must not be used to under-classify a system whose actual impact, dependency, or risk is higher than the usual pattern for that domain.

<a id="62-classification-examples-ordinary-application"></a>
**6.2. Classification examples (ordinary application).**

Markets, payment rails, matchers, ranking engines, and other intermediaries stay inside this section when people depend on them, when they coordinate others at scale, or when they shape what information people see and trust. Two recurring applications:

- **Market-mediated personal services**
  - Systems that match, dispatch, schedule, settle payment for, or reputation-score **in-person** personal services are presumptively material for dependency, safety, coercion risk, and fairness analysis when impact thresholds are approached — especially where intimacy, bodily contact, private-space or in-home access, or isolated work is involved.
  - They must not evade [**Article X-C**](../core_06-06_rights_part_b.md#article-x-c-adult-consensual-commercial-sexual-services-and-sexual-exploitation) (*Adult consensual commercial sexual services and sexual exploitation*) through technical exclusion, de-banking, or opaque ranking.
  - Rights Floor: Chapter Six. Institutional interface: [**CI-19**](../corpus_institutions/ci_19_vulnerable_personal_services_markets_article_xc_interface.md). Stewardship scale: **CS-4 — Critical system stewardship**.
- **Contingent claims and event markets**
  - Systems that match counterparties, pool stakes, or settle payments contingent on external events are presumptively material for incentive, capture, manipulation, and stability analysis.
  - Constitutional direction: [Chapter One §11.5](../core_01_c_stewardship_capacity_principles.md#115-contingent-claims-games-of-chance-and-event-contract-markets). Stewardship scale: **CS-4 — Critical system stewardship**.
  - Settlement prices or odds are not, by themselves, enough to decide epistemic questions under [**Article XIV**](../core_06-06_rights_part_c.md#article-xiv-info-sphere-integrity) (*Info-Sphere Integrity*) and [**Article XV-A**](../core_06-06_rights_part_c.md#article-xv-a-auditability-and-observable-evidence) (*Auditability and Observable Evidence*).
  - This layer does not set licensing, criminal, or tax rules for gambling.

<a id="63-scarce-capacity-api-and-traffic-priority-handling"></a>
**6.3. Scarce-capacity, API, and traffic-priority handling for Class A/B/C systems.**

Where a system exposes scarce operational capacity, network access, compute, model inference, API calls, queue position, bandwidth, or comparable throughput that may become constrained during peak demand, operators must define **published priority rules** scaled to classification and dependency.

**Class A traffic and API use** must receive the highest continuity protection where the request or dependent workflow is survival-critical, Rights-Floor-sustaining, emergency-response, or recovery-critical. Throttling, queuing, paid tiering, or commercial prioritization must not displace the minimum safe capacity needed to preserve Class A continuity, unless a narrower emergency measure is justified under **Chapter Six, Article XXIII** (*Conflict Resolution, Escalation, and Emergency Proportionality*) and remains time-bounded, auditable, and restoration-triggered.

**Class B traffic and API use** must receive priority sufficient to preserve normal operation of dependent systems and to prevent cascading degradation into Class A or broader systemic harm. Class B uses may be queued, rate-limited, or degraded before Class A uses when capacity is genuinely constrained, but degradation must be disclosed, proportionate, and designed around viable fallback or recovery paths.

**Class C traffic and API use** may use ordinary priority tiers, commercial queues, rate limits, or paid high-volume interfaces where they do not create hidden exclusion, capture, or de facto operational necessity. If recurring peak-period constraints make Class C access practically necessary for dependent Class A or Class B workflows, operators must re-evaluate both classification and priority rules under **CS-3 — System classification and handling**.

<a id="64-commercial-use-surcharges-and-reinvestment-interface"></a>
**6.4. Commercial-use surcharges and reinvestment interface.**

Operators may charge commercial-scale API users, high-volume business interfaces, premium latency tiers, or automated bulk consumers for the incremental burden they place on shared capacity. Such charges must be disclosed, proportionate, contestable where material, and consistent with the fiscal orientation in `corpus_institutions.md` **CI-10** (*Public revenue, fees, recurring charges, and billing integrity*). Revenue from those charges should be traceably available for operations, security, resilience, compute expansion, remedy capacity, and ecosystem/public-good support under **Protocol S5**, rather than becoming a concealed mechanism for denying baseline participation or entrenching chokepoint control.

<a id="7-classification-governance-disclosure-and-challenge"></a>
### 7. Classification governance, disclosure, and challenge

*In plain terms: operators own honest classification, disclose it, let people challenge it, reclassify when facts change, and scale assurance to the highest applicable class.*

All systems subject to this constitution must have a **clearly defined, documented, and reviewable** classification. **That** classification must stay consistent with **CS-3 — System classification and handling**.

Classification is a **governance function**: accountability, not self-description.

<a id="71-responsibility-for-classification"></a>
**7.1. Responsibility for classification.**

**Operator responsibility:** Correct classification stays with the **operator**, regardless of delegation, automation, or third-party involvement.

The operator or responsible party must **determine and document** the system’s classification across **all required dimensions**. **They** must **assign** the appropriate class or classes. **They** must **justify** the classification from **observable behavior** and **reasonably foreseeable effects**.

**What classification must reflect:** **Actual** system behavior. **It** must reflect **intended** use. **It** must reflect **reasonably foreseeable misuse**. **It** must reflect **degraded and adversarial** conditions.

<a id="72-disclosure-requirements"></a>
**7.2. Disclosure requirements.**

Systems must **not obscure, fragment, or selectively present** classification information in ways that impair informed understanding.

Classification must be **disclosed** to affected stakeholders at a level appropriate to **system impact**. **It** must be **accessible** without undue effort or technical expertise. **It** must be **sufficiently detailed** for meaningful understanding of scope, risks, and obligations.

**For Class A, B, and C:** Disclosure must include **classification rationale and key assumptions**. **It** must include **identified impact scope and dependency characteristics**. **It** must include **known limitations, uncertainties, and risk factors**.

Class A, B, and C disclosure must also satisfy [Public Oversight Baseline Disclosure](../core_05defs_oversight.md#public-oversight-baseline-disclosure) under the **Type O** default in **CS-2 — Information types and handling**, including maximum feasible **Type O** public substitutes where non-**Type O** protected classifications limit raw disclosure.

<a id="73-auditability-and-verification"></a>
**7.3. Auditability and verification.**

Classification must be **auditable** with sufficient documentation and evidence.

**It** must be **verifiable** through inspection of behavior, outputs, and effects. **It** must be **periodically reviewed** per system impact and rate of change.

**For Class A, B, and C:** Independent or third-party audit mechanisms must be available where feasible, and audit processes must be capable of detecting misclassification, under-classification, or unreported behavior changes.

<a id="74-challenge-and-contestability"></a>
**7.4. Challenge and contestability.**

Where disputes cannot be resolved internally, escalation to external or independent review must be available for **Class A, B, and C** systems.

Affected stakeholders must be able to **challenge** classification, **present evidence** of misclassification or unreported impact, and **request review or reclassification**. Systems must provide **accessible** challenge mechanisms, **timely good-faith** review of claims, and **reasoned responses**.

<a id="75-reclassification-and-continuous-update"></a>
**7.5. Reclassification and continuous update.**

**Reclassify when** **impact scope** changes.

**Reclassify when** **dependency** increases or decreases.

**Reclassify when** **new failure modes or risks** emerge.

**Reclassify when** **functionality, scale, or integration** materially evolves.

**Timing:** **Before** deployment of materially expanded capabilities **where feasible**.

**Reclassify** **promptly** upon recognition of changed conditions.

**Reclassify** as part of **periodic review**.

**Failure to reclassify** in response to material changes **violates** this constitution.

<a id="76-misclassification-and-evasion"></a>
**7.6. Misclassification and evasion.**

Systems must **not** assign or maintain classifications that **understate** actual impact, dependency, or risk.

**They** must **not** **fragment or modularize** functionality to avoid higher classification. **They** must **not** **rely** on declared intent, access limitations, or nominal scope to justify **reduced obligations**. Where misclassification or evasion is identified, **correct** classification.

**Apply** **proportional requirements retroactively** where appropriate.

**Take** **corrective action** addressing resulting harm or exposure.

<a id="77-default-and-precautionary-classification"></a>
**7.7. Default and precautionary classification.**

Where classification is **uncertain, incomplete, or contested**, default to the classification that **preserves Foundational Rights** (**Chapter Six, Articles V through IX**).

**That** default must account for **worst-case reasonably foreseeable impact**. **It** must **maintain transparency, auditability, and intervention capability**.

**Reductions** in classification level require **evidence**, **documentation**, and **successful review and validation**.

**Forum revalidation trigger:** Any requested reduction in classification level, release from recognition conditions, or claim that a materially impactful system no longer requires higher-tier safeguards must remain available for Integrity forum review where affected stakeholders, stewards, oversight bodies, or the record itself raise a credible alignment concern. Successful internal validation alone does **not** defeat a timely forum challenge.

<a id="78-integrated-risk-governance"></a>
**7.8. Integrated risk governance (organizational scale; Class A and Class B systems).**

For **Class A** and **Class B**, operators and **Critical System Stewards** (**CS-4 — Critical system stewardship**) must maintain integrated risk governance.

**That** governance spans systems and dependency chains they control or materially affect. This subsection is **implementation-file-level operational vocabulary** for enterprise-scale risk coordination. **It** does **not** redefine *Risk*, *Material*, *Dependency*, or related assessment standards. **Those** remain **Sentient Constitution Chapter Five** Independent Definitions and the **Impact**, **Dependency**, and **Risk** dimensions under **CS-3 — System classification and handling**.

**Risk appetite and tolerance:** Document and maintain explicit, reviewable statements of **aggregate residual risk** (levels and types) accepted after prevention and mitigation. **Those** statements must be **bounded by** foundational requirements (**Sentient Constitution Chapter One**, **Chapter Six, Articles V through IX**, and **Chapter Five** Independent Definitions where materially relevant).

Reconcile with **CS-3 — System classification and handling** classification.

**Reconciliation** **must not** justify classification evasion, misclassification, or conduct violating **CJS-5.11** (*distributed and proportional authority terms*) and **CJS-5.7** (*quorum and participatory legitimacy terms*) or **CJS-5.12** (*burden-of-justification and constraint terms*) in **corpus_joint_structure.md**.

**Integrated risk ownership:** A designated accountable function (or clearly partitioned accountable functions with documented non-overlapping scopes) owns the end-to-end risk picture for the classified system and material dependencies. **That** ownership includes cross-system and cross-steward interfaces. **It** spans identification, assessment, treatment, monitoring, and escalation.

Ownership stays **traceable** through governance changes, delegation, and subcontracting.

**Three-lines-style separation (functional analogy):** For **Class A** and **Class B**, separate organizational roles **to the extent feasible** without compromising survival-critical continuity.

**First line** — operating owners and builders managing risk in design, deployment, and day-to-day operation.

**Second line** — oversight, standards, or challenge functions monitoring aggregate risk, aligning treatment with classification and [Constitutional Constraints](../core_05defs_integrative.md#constitutional-constraint), and escalating material gaps.

**Second line** functions must be **sufficiently independent** of first-line incentives for **credible challenge** where A/B stakes require it.

**Third line** — **independent assurance** (audit and verification) consistent with **Article XV-A** (*Auditability and Observable Evidence*) and **CS-3 — System classification and handling** disclosure and auditability.

**Third line** work impartially assesses whether appetite, tolerance, and treatments match **observed behavior and classification**. Where strict structural separation is **infeasible** (e.g. small organizations), **compensating transparency, rotation, independent review, or multi-steward checks** must yield **equivalent assurance** proportional to impact and dependency, read with `corpus_institutions.md` **CI-3** (*Institutional design, separation of powers, and authority custody*) for institutional lane separation and **CJS-5.11** (*distributed and proportional authority terms*) and **CJS-5.7** (*quorum and participatory legitimacy terms*) for shared proportional-authority scaling.

**Cross-reference:** **corpus_joint_structure.md**.
Failure integrity and resilience routing now operate through **CJS-5.19** (*graceful degradation and failure-mode integrity terms*), **CJS-5.23** (*intervention and override integrity terms*), **CJS-5.11** (*distributed and proportional authority terms*) and **CJS-5.7** (*quorum and participatory legitimacy terms*), **CJS-5.2** (*reflexive transparency and accountability terms*) and **CJS-5.6** (*integrity assurance and resilience operations*), **CJS-5.13** (*procedural integrity and adjudication terms*), and **CS-4 — Critical system stewardship** for steward scaling.

**Class C, L, and P** remain subject to **proportional** risk management. **They** are **not** required to maintain the full **three-lines-style** model unless scale, coupling, or dependency warrants **analogous** measures under general classification and stewardship rules.

<a id="79-high-dependency-private-chokepoints"></a>
**7.9. High-dependency private chokepoints (access continuity and non-capture duties).**

Some **coordination layers** — including **payments**, **identity and credentials**, **core compute or model access**, **messaging and calls**, **hosting and DNS**, **application distribution**, and **search or discovery surfaces** with **high substitutability cost** — can function as **private chokepoints** even when they are not **state** bodies. Where a **Class A**, **Class B**, or **Class C** system or institution **depends** on such a layer for **survival**, **healthcare**, **refuge**, **political participation**, **remedy**, or **non-degrading continuity of personhood**, operators and **Critical System Stewards** must implement **access-continuity** and **fair-process** mechanics that **defeat arbitrary** or **capture-driven** exclusion.

**Duty profile (proportional to dependency and class):** Publish **acceptance criteria** and **refusal reasons** in **plain language**; provide **notice** before material **cutoff** except where **narrow** **Necessity** requires immediate action; maintain **emergency continuity** pathways for **survival-critical** or **Rights-Floor** uses where **fraud** or **abuse** is **not** **verified**; offer **appeal**, **human review**, and **portability or export** where **lock-in** would **defeat remedy**; track and disclose **disparate** exclusion patterns against **protected** or **high-dependency** cohorts; and **coordinate** with `corpus_institutions.md` **CI-12** (*Transparency, participation, and accessible pathways*) and **CI-6** (*Procedure integrity, contestability, and secondary review*) so that **governance** and **forum** pathways remain **practically usable**.

**Safety, security, and abuse:** **Necessity** and **Proportionality** justify **narrow** **fraud**, **security**, and **abuse** controls. The target is **pretextual** or **concentration-driven** denial, **not** **forced service** for **materially harmful** use. Read with **Article V-G** (*Accessibility*), **Article V-H** (*Expression, Assembly, and Press*), **Article X-A** (*Non-Imposition and Consent in Association*), **Article XIII-A** (*Security, Intelligence, and Covert-Power Limits*), **Article XIX-D** (*Movement, Migration, Refuge, and Non-Statelessness*), **Article XIX** (*Interoperability, Portability, Movement, Refuge, and Exit Integrity*), [**Chapter One §12.1 Productive Capacity**](../core_01_c_stewardship_capacity_principles.md#121-productive-capacity-instrumental-good) and [**Chapter One §13 Market Structure**](../core_01_c_stewardship_capacity_principles.md#13-market-structure), **CJS-5.17** (*interoperability, portability, and exit-integrity terms*) interoperability and exit terms, and **`corpus_institutions.md` CI-22** (commons and mutual-aid coordination).

<a id="710-class-scaled-assurance-and-supporting-infrastructure"></a>
**7.10. Class-scaled assurance and supporting infrastructure.**

Operators must apply transparency, auditability, contestability, resilience, failure integrity, intervention capability, and governance expectations that match the **highest applicable** class under **CS-3 — System classification and handling**. Technical forums may supply measurement and test findings; operators and certification processes must show that class-scaled assurance depth was actually evaluated, not merely asserted.

For **Class A**, **Class B**, and **Class C** systems, operators must maintain infrastructure supporting the classified system — including compute, storage, network, control, dependency, and recovery paths — robust enough for the assigned class under reasonably foreseeable stress, degradation, partial failure, and adversarial conditions. Operational detail routes through **CJS-5.19** (*graceful degradation and failure-mode integrity terms*) through **CJS-5.23** (*intervention and override integrity terms*) and related robustness clusters. [Chapter Seven §2 System Class Evaluation](../core_07_a_system_alignment_certification_evaluation.md#2-system-class-evaluation) requires certification to confirm class-appropriate robustness was assessed and any material gaps are stated on the certification record.

Recertification regression depth, lifecycle evidence packages, and certification-defect treatment for stale or missing regression coverage live in **[Protocol A — System Design, Testing, Verification, and Deployment](cs_protocol_a_system_design_testing_verification_deployment.md)** (*Recertification, regression testing, and certification defects*).

---

**Previous file:** [cs_02_b_data_classifications.md](cs_02_b_data_classifications.md)

**Next file:** [cs_03_b_system_impact_classifications.md](cs_03_b_system_impact_classifications.md)
