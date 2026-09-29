<a id="cs-2-part-b-data-classifications"></a>
# CS-2, Part B: Data classifications

<details>
<summary><strong><span style="color: #2563eb;">Corpus placement (non-operative): file structure and reading rules</span></strong></summary>

> The following content is **reader guidance only**. It does not add, remove, or narrow binding obligations elsewhere in this file or in other CS-2 parts.
>
> This file contains **CS-2, Part B** — data classifications (**Type E** through **Type W**, including **Type O**) as **§8**. Purpose and scope (including identity self-ownership and continuity-critical export), classification determination, anti-circumvention, cross-domain principles, and data separation / attribution (**§§1–7**) are in [`cs_02_a_information_types_and_handling.md`](cs_02_a_information_types_and_handling.md).

</details>

<br>

**CS-2, Part B**, owns **data classifications** (**Type E** through **Type W**, including **Type O**). Classification determination and cross-domain governance are in **[Part A](cs_02_a_information_types_and_handling.md#cs-2-part-a-information-types-and-handling)**.
*In plain terms: Part B names each data type and groups them by how they are usually shared — open, audit-only, restricted, off-limits, or public by the creator's choice — then states each type’s content rules. Things sentients make themselves are Type Y while private or shared, and Type W once the creator makes them public.*

<a id="cs-2-8-data-classifications"></a>
## CS-2.8 Data classifications

*In plain terms: the letter codes are domain labels, not a ranked sensitivity scale. Types share access-posture bands so common rules can attach to the sharing style. When more than one type fits, the stronger protections win.*

These type letters name different kinds of data and how they are usually shared — not a ranked list from “least sensitive” to “most sensitive.” The letters are labels, not a score order. Each type carries its own protections, which do not rise or fall just because of where it sits in this list. When more than one type could apply, use the strongest applicable protections.

**Access-posture bands.** Types are grouped by **default access posture** so shared band rules in [Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands) apply once. Band order below is for reading clarity only — **not** a sensitivity ranking.

**Open / accessible by default** — strong presumption of openness or accessibility; hold-backs are narrow ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands)):
- **Type O** — Open public oversight baseline disclosure data: [Public Oversight Baseline Disclosure](../core_05_band_oversight.md#public-oversight-baseline-disclosure) for oversight and contestability, including lawful substitutes where Type G, Type E, or other source stays non-public or non-baseline; open by default (strong presumption).
- **Type E** — Environmental, emergency, and survival-coordination data: environment, infrastructure, emergency, and other content streams needed to stay safe and coordinate harm prevention; accessible by default (strong presumption); published Public Oversight Baseline Disclosure artifacts drawn from it are Type O.

**Audit-accessible, not public** — fully auditable; not public by default; public face is Type O ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands)):
- **Type G** — Governance and operational source data: sensitive records of how systems are run, decided, risked, and challenged; fully auditable through structured or qualified audit access, but not public by default.

**Restricted by default** — purpose-limited access; consent or justified override as the type requires ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands)):
- **Type H** — Historical, relational, transactional, and participation data: logs of interactions, exchanges, and activity patterns; restricted by default.
- **Type I** — Identity and attribution data: who is who and who did what, for verification and accountability without unnecessary tracking; restricted by default.
- **Type S** — Safety, security, and restricted investigation data: temporary exploit-, investigation-, or compromise-sensitive material; restricted by default, time-bound, and review-bound.
- **Type Y** — Yours: writing, media, code, designs, and other works a sentient creates or provides, while private or shared; restricted by default, with release, reuse, and retention under the creator's direction.

**Public by creator release** — open to all by the creator's choice, and withdrawable by the creator:
- **Type W** — Works, published: Type Y works the creator has released publicly; openly accessible while the creator keeps them public, still under the creator's control, and deleted on the creator's request.

**Shared works** made of more than one contributor's **Type Y** or **Type W** data are governed by [§8.10](#810-shared-works).

**Non-accessible by default** — consent or justified override only ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands)):
- **Type N** — Neurocognitive and internal data: thoughts, feelings, and other inner states, including reconstructions or inferences of them; non-accessible by default.

<a id="81-type-e-environmental-emergency-and-survival-coordination-data"></a>
### 8.1 Type E: Environmental, emergency, and survival-coordination data

**Accessibility posture:** Open / accessible by default (strong presumption) ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands); [§8 overview](#cs-2-8-data-classifications)).

*In plain terms: data sentients need to stay safe and coordinate help — environment, infrastructure, emergencies — should stay open and useful unless publishing it would itself cause serious harm.*

**Definition:** Data necessary to preserve sentient survival, environmental integrity, and critical substrate health. This data enables sentients and systems to perceive reality and coordinate harm prevention. Examples include:
- **ecological and environmental condition** data; **air, water, soil, climate, biodiversity, and contamination** data
- **infrastructure health and failure-state** data for survival-critical systems
- **resource availability** for food, water, shelter, energy, processing continuity, and communication access
- **system health, reliability, and degradation** data for critical shared infrastructure
- **emergency condition and hazard** signals (underlying coordination streams, not merely public-baseline notices)
- **where environmental harm comes from and how heavy its load is** on the living world and the shared life-support systems sentients depend on

**Relationship to Type O:**
- **Type E** is the **content domain** for survival- and coordination-critical data — not [Public Oversight Baseline Disclosure](../core_05_band_oversight.md#public-oversight-baseline-disclosure).
- Published Public Oversight Baseline Disclosure artifacts drawn from **Type E** — including aggregated public environmental or hazard summaries, published emergency notices at public-baseline fidelity, and other baseline disclosure artifacts — must be classified and handled as **Type O**.
- Where a **Type O** baseline applies, systems must still release sufficient [Public Oversight Baseline Disclosure](../core_05_band_oversight.md#public-oversight-baseline-disclosure) even when the underlying streams remain **Type E**.
- A **Type O** notice must leave the underlying coordination stream’s **Type E** accessibility, timeliness, and anti-suppression duties fully in force.

**Disclosure posture:** **Presumptive accessibility** under the **open / accessible by default** band ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands)). Narrow hold-backs require justification under **CJS-3.12** (*burden-of-justification and constraint terms*) and **CJS-3.5** (*independent verification and claim-integrity terms*). Shared timeliness, presentation, fidelity, and restriction-discipline rules are in [Part A §5.1](cs_02_a_information_types_and_handling.md#51-proportional-access-and-handling)–[§5.3](cs_02_a_information_types_and_handling.md#53-tiered-transparency-and-audit-access).

#### 8.1.1 Type E access and handling duties

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Topic routing (mandatory read-with): [Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands) (*Access-posture bands* — open / accessible by default).
- Topic routing (mandatory read-with): [Part A §5.3](cs_02_a_information_types_and_handling.md#53-tiered-transparency-and-audit-access) (*Tiered transparency and audit access* — narrow-scope, time-bound, documentation, net-harm, and Type E / Type S separation rules).
- Read with: [Part B — Type S · Interaction with Type E](#type-s-interaction-with-type-e).

</details>

<br>

*In plain terms: keep survival and coordination data usable where sentients need it, make access real rather than symbolic, limit secrecy to cases where publishing would itself cause serious harm, and never fake openness by starving, hiding, or failing to maintain the data.*

**Core duty.** **Type E** data must remain available for timely understanding, coordination, and response when harm with **non-trivial** impact is at stake for sentients, the environment, or critical substrate systems. Systems must **not** withhold, obscure, degrade, or monopolize it in ways that defeat that purpose.

**Access.** Systems must:
- **distribute** access geographically and systemically to the maximum extent feasible — not withhold it for convenience, cost minimization, or institutional preference alone
- make access **actionable** for harm prevention, coordination, or response by affected stakeholders — not merely formally available
- **limit restriction** to cases where disclosure would **itself** create material risk of enabling targeted or disproportionate harm, exploitation, or system compromise, consistent with the **open / accessible by default** band ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands))

**Handling — prohibited.** Systems managing **Type E** data must **not:**
- manipulate or selectively suppress it to conceal harm, scarcity, degradation, or externalized cost
- create **artificial scarcity** of access to survival-relevant information
- treat public need for survival-relevant data as **proprietary secrecy**
- reclassify or fragment it across domains in ways that reduce effective accessibility or obscure relevance to survival, coordination, or risk
- **fail** to collect, maintain, or update it where such failure would produce **functional unavailability equivalent to withholding**

<a id="82-type-g-governance-and-operational-source-data"></a>
### 8.2 Type G: Governance and operational source data

**Accessibility posture:** Audit-accessible, not public ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands); [§8 overview](#cs-2-8-data-classifications)).

*In plain terms: the sensitive internal records of how a system is run, what it decides, what can go wrong, and how it is challenged — fully open to real audit, but not dumped into public view. What the public must see is Type O.*

**Definition:** Sensitive governance and operational **source** records required for meaningful oversight, audit, reconstruction, and constitutional accountability — including material whose full fidelity is inappropriate for public release but must remain **fully auditable**. Examples include:
- **internal governance records**, working procedural materials, and non-public classification or policy working papers
- **full deliberation, voting, quorum, and decision** records beyond what is lawfully published as **Type O**
- **detailed audit trails, compliance workpapers, and forensic reconstruction** materials
- **operational telemetry, configuration, methodology, evaluation criteria, and assumption** records at source fidelity
- **full-fidelity risk, dependency, and system-impact** analyses
- **challenge, review, and corrective-action** source dockets not themselves released as **Type O**

**Relationship to Type O:**
- **Type G** is **not** [Public Oversight Baseline Disclosure](../core_05_band_oversight.md#public-oversight-baseline-disclosure).
- Public Oversight Baseline Disclosure publication — including summaries, aggregates, de-identified releases, delayed releases, and other lawful substitutes drawn from **Type G** source — must be classified and handled as **Type O**.
- When [Public Oversight Baseline Disclosure](../core_05_band_oversight.md#public-oversight-baseline-disclosure) is required, systems must still publish a usable Type O disclosure — even if the **Type G** source records stay non-public.

**Disclosure posture:** **Not public by default** under the **audit-accessible, not public** band ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands)). Access is through **structured or qualified audit access** under **CJS-3.3** (*auditability and reconstructability terms*) and **CJS-3.4** (*tiered transparency and audit-access terms*), with public-facing accountability carried by **Type O**.

<a id="821-type-g-access-and-handling-duties"></a>
#### 8.2.1 Type G access and handling duties

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Topic routing (mandatory read-with): [Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands) (*Access-posture bands* — audit-accessible, not public).
- Topic routing (mandatory read-with): [Part A §5.3](cs_02_a_information_types_and_handling.md#53-tiered-transparency-and-audit-access) (*Tiered transparency and audit access*).
- Topic routing (mandatory read-with): [Part A §2](cs_02_a_information_types_and_handling.md#cs-2-2-determination-of-classification) (*Determination of classification* — most-restrictive applicable protections).
- Read with: **Part B — Type O** (*Public Oversight Baseline Disclosure*); **CJS-3.3** (*auditability and reconstructability terms*); **CJS-3.4** (*tiered transparency and audit-access terms*).

</details>

<br>

*In plain terms: keep the full governance record auditable, give real auditors what they need, and never use “not public” as a shield against review or as a substitute for Public Oversight Baseline Disclosure.*

**Core duty.** **Type G** data must remain **fully auditable** — reconstructable, attributable, and reviewable — so independent oversight can verify how systems operate, how decisions are made, what risks exist, and how challenges are handled. Non-public status must **not** function as unreviewable secrecy.

**Access.** Systems must:
- provide **Type G** data to authorized auditors, oversight bodies, and other qualified reviewers in a manner that is **understandable**, **documented**, **attributable**, **versioned** where material changes occur, and **retained** for a duration proportional to system impact and dependency
- publish access gates, eligibility rules, and qualification routes for audit as **Type O** where they govern who may reach **Type G** source
- preserve audit sufficiency and publish the strongest feasible **Type O** substitute where [Public Oversight Baseline Disclosure](../core_05_band_oversight.md#public-oversight-baseline-disclosure) applies, when raw **Type G** disclosure is inappropriate under [Part A §7](cs_02_a_information_types_and_handling.md#cs-2-7-type-o-baseline-for-class-a-b-c-systems) or more-restrictive applicable typing under [Part A §2](cs_02_a_information_types_and_handling.md#cs-2-2-determination-of-classification)
- **limit further restriction of audit access** so that:
  - it does **not** defeat Disclosure posture or the **audit-accessible, not public** band ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands))
  - further restriction is permitted only where more-restrictive applicable typing under [Part A §2](cs_02_a_information_types_and_handling.md#cs-2-2-determination-of-classification) or [Part A §5.3](cs_02_a_information_types_and_handling.md#53-tiered-transparency-and-audit-access) (*Tiered transparency and audit access*) requires it
  - further restriction is **not** used for convenience, reputational protection, or power preservation

**Handling — prohibited.** Systems managing **Type G** data must **not:**
- classify governance-relevant or operationally material information as secret **merely** for convenience, reputational protection, or power preservation
- treat non-public **Type G** status as a substitute for [Public Oversight Baseline Disclosure](../core_05_band_oversight.md#public-oversight-baseline-disclosure)
- provide **performative summaries** while withholding information necessary for meaningful qualified audit
- use **complexity, opacity, or format fragmentation** to defeat auditability (contrary to **CJS-3.8** (*comprehensibility and cognitive accessibility terms*), **CJS-3.10** (*disclosure sufficiency and observability terms*), and **CJS-3.3** (*auditability and reconstructability terms*))

<a id="83-type-o-open-public-oversight-baseline-disclosure-data"></a>
### 8.3 Type O: Open public oversight baseline disclosure data

**Accessibility posture:** Open / accessible by default (strong presumption for Public Oversight Baseline Disclosure release) ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands); [§8 overview](#cs-2-8-data-classifications)).

*In plain terms: [Public Oversight Baseline Disclosure](../core_05_band_oversight.md#public-oversight-baseline-disclosure) — what must be published so sentients can understand high-impact systems, including a strong public substitute when Type G, Type E, or other raw private or non-baseline records cannot be released as that disclosure.*

**Definition:** Data released or required to be released as [Public Oversight Baseline Disclosure](../core_05_band_oversight.md#public-oversight-baseline-disclosure) for transparency, oversight, and contestability — including lawful substitutes where **Type G**, **Type E**, or other source records remain non-public, non-baseline, or otherwise restricted. Canonical meaning is in Chapter Five; this type owns systems-layer typing and handling.

**Class A/B/C public-baseline content.** Where the [Type O baseline for Class A/B/C](cs_02_a_information_types_and_handling.md#cs-2-7-type-o-baseline-for-class-a-b-c-systems) applies, **Type O** carries [Public Oversight Baseline Disclosure](../core_05_band_oversight.md#public-oversight-baseline-disclosure) — the **public explanation** of chartered and certified scope — mapped under Part A §7 from the governing [Charter](../core_05_band_continuity.md#charter) (or equivalent), assigned class, and observed [System Boundaries](../core_05_band_continuity.md#system-boundaries) — not a second taxonomy. It includes information sentients need to understand:
- purpose and what the system does
- how it is classified
- dependency structure and what depends on it
- operational status and how it is running
- material risks, performance, and failures
- how it is governed and material audit outcomes
- stakeholder effects
- its degree of alignment with this Constitution

Where that baseline applies, **Type O** also carries — at public-baseline fidelity, including lawful substitutes — publication or a usable public view of:
- the governing [Charter](../core_05_band_continuity.md#charter) (or equivalent published scope instrument)
- the [System Classification Record](../core_05_band_continuity.md#system-classification-record-constitutional)
- the [System Data Types Record](../core_05_band_continuity.md#system-data-types-record-constitutional)
- the [System Certification Record](../core_05_band_continuity.md#system-certification-record-constitutional) produced by [System Alignment Certification](../core_05_band_continuity.md#system-alignment-certification-constitutional), including material governance and audit outcomes required for baseline visibility

Baseline visibility into purpose, operational status, material risk, performance, failures, and stakeholder effects may be satisfied through those records, [Risk Disclosure](../core_05_band_oversight.md#risk-disclosure) where systemic risk is in scope, and other lawful **Type O** summaries or substitutes — not by omitting the topics.

**Other examples include:**
- **published procedural rules and disclosed assumptions** at public-baseline fidelity
- **aggregated, de-identified, summary, or delayed** public releases that substitute for **Type G**, **Type E**, or other restricted or non-baseline source data
- **published emergency notices and aggregated environmental or public-risk summaries** at public-baseline fidelity drawn from **Type E** streams
- **public eligibility rules and routing** for qualified audit access to **Type G** or other non-public source
- **versioned public change notices, operational status, performance, failure, stakeholder-effect, and material-risk summaries** for baseline understanding

**Relationship to other types:**
- **Type G** holds sensitive governance and operational **source** that is audit-accessible but not public by default.
- **Type E** holds survival- and coordination-critical **content streams** that are accessible by default under Type E duties and are **not** themselves [Public Oversight Baseline Disclosure](../core_05_band_oversight.md#public-oversight-baseline-disclosure).
- **Type O** governs the **publication posture** of Public Oversight Baseline Disclosure artifacts, including substitutes derived from **Type G** or **Type E**.
- Neither **Type E** nor **Type G** is the public floor; published baseline artifacts drawn from them are **Type O**, while underlying streams may remain under their original type.

**Disclosure posture:** **Baseline public accessibility** under the **open / accessible by default** band ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands)). Deeper structured or qualified audit access to **Type G** (or other non-public source) may run in parallel but must not replace [Public Oversight Baseline Disclosure](../core_05_band_oversight.md#public-oversight-baseline-disclosure) where **Type O** applies.

#### 8.3.1 Type O access and handling duties

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Topic routing (mandatory read-with): [Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands) (*Access-posture bands* — open / accessible by default).
- Topic routing (mandatory read-with): [Part A §7](cs_02_a_information_types_and_handling.md#cs-2-7-type-o-baseline-for-class-a-b-c-systems) (*Type O baseline for Class A/B/C systems* — scoped by Charter, class, and System Boundaries; verified under Chapter Eight).
- Topic routing (mandatory read-with): [Part A §5.3](cs_02_a_information_types_and_handling.md#53-tiered-transparency-and-audit-access) (*Tiered transparency and audit access*).
- Topic routing (mandatory read-with): [Part A §2](cs_02_a_information_types_and_handling.md#cs-2-2-determination-of-classification) (*Determination of classification* — most-restrictive applicable protections).
- Read with: [Public Oversight Baseline Disclosure](../core_05_band_oversight.md#public-oversight-baseline-disclosure); [Charter](../core_05_band_continuity.md#charter); [System Boundaries](../core_05_band_continuity.md#system-boundaries); [System Alignment Certification](../core_05_band_continuity.md#system-alignment-certification-constitutional); [System Certification Record](../core_05_band_continuity.md#system-certification-record-constitutional); [System Classification Record](../core_05_band_continuity.md#system-classification-record-constitutional); [System Data Types Record](../core_05_band_continuity.md#system-data-types-record-constitutional); [Chapter Eight §4](../core_08_a_system_alignment_certification_evaluation.md#4-data-types-and-handling-evaluation) (*Data Types and Handling Evaluation*); [Chapter Eight Part B §11](../core_08_b_system_alignment_certification_record_process.md#11-certification-record) (*Certification record*); [Transparency](../core_05_band_oversight.md#transparency); **Article XV** (*Audit, Transparency, and Independent Verification*).

</details>

<br>

*In plain terms: publish the Public Oversight Baseline Disclosure sentients need, keep it free and usable online where that infrastructure exists, and never treat audit-only access or thin summaries as good enough.*

**Core duty.** **Type O** data must remain sufficiently accessible for informed participation, oversight, and challenge at the Public Oversight Baseline Disclosure tier.

**Access.** Systems must:
- provide **Type O** data in a manner that is **understandable**, **documented**, **attributable**, **versioned** where material changes occur, and **retained** for a duration proportional to system impact and dependency
- where lawful online publication infrastructure exists to support class-appropriate access, make **Type O** data **freely available online** — without paywalls or insider-only substitutes for [Public Oversight Baseline Disclosure](../core_05_band_oversight.md#public-oversight-baseline-disclosure)
- **limit redaction** so it does **not** prevent meaningful accountability at the Public Oversight Baseline Disclosure tier; limited redaction is permitted only where more-restrictive applicable typing under [Part A §2](cs_02_a_information_types_and_handling.md#cs-2-2-determination-of-classification) or [Part A §5.3](cs_02_a_information_types_and_handling.md#53-tiered-transparency-and-audit-access) / [§7](cs_02_a_information_types_and_handling.md#cs-2-7-type-o-baseline-for-class-a-b-c-systems) requires it — and only where a lawful **Type O** substitute still preserves meaningful accountability

**Handling — prohibited.** Systems managing **Type O** data must **not:**
- withhold **Type O** material behind paywalls, account barriers beyond reasonable identity verification for restricted tiers, or insider-only distribution substitutes for [Public Oversight Baseline Disclosure](../core_05_band_oversight.md#public-oversight-baseline-disclosure)
- treat **Type O** publication as satisfied by performative summaries while withholding decision-relevant baseline material
- treat non-public **Type G** audit access as a substitute for [Public Oversight Baseline Disclosure](../core_05_band_oversight.md#public-oversight-baseline-disclosure)
- use **complexity, opacity, or format fragmentation** to defeat Public Oversight Baseline Disclosure auditability or contestability
- label restricted source data **Type O** without lawful substitute, reclassification, or release discipline

<a id="84-type-h-historical-relational-transactional-and-participation-data"></a>
### 8.4 Type H: Historical, relational, transactional, and participation data

**Accessibility posture:** Restricted by default ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands); [§8 overview](#cs-2-8-data-classifications)).

*In plain terms: logs of what sentients and systems did together — keep only what you need, and do not turn them into surveillance or a back door into someone's identity or inner life.*

**Definition:** Records of interactions, exchanges, participation, and operational events that do **not** by themselves constitute internal cognitive data but may reveal patterns of behavior, dependency, association, or system impact. Examples include:
- **transaction and transfer** records
- **communication and interaction metadata**
- **system access and usage** events
- **participation** records in governance, platforms, or service systems
- **consent receipts and revocation** events
- **dependency and interoperability** events
- **operational logs** connected to sentient or system activity
- **resource usage** records not already classified as Type I or Type H

**Boundary with Type Y and Type W:** The content of a work a sentient creates or provides is **Type Y**, or **Type W** once the creator makes it public. Records about that work — when it was created, uploaded, accessed, or shared, and with whom — remain **Type H**.

**Disclosure posture:** **Restricted by default** under the **restricted by default** band ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands)).
- Access is allowed to the extent necessary for **system operation**, **accountability**, **dispute resolution**, **audit**, and **user visibility** into their own activity.
- **Public transparency** is allowed where data is sufficiently aggregated or de-identified such that re-identification risk is minimized under **CJS-3.11** (*distributed and proportional authority terms*) and **CJS-3.7** (*quorum and participatory legitimacy terms*).

#### 8.4.1 Type H access and handling duties

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Topic routing (mandatory read-with): [Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands) (*Access-posture bands* — restricted by default; shared anti-abuse limits; shared consent integrity; Type H and Type I anti-capture limits).
- Topic routing (mandatory read-with): [Part A §5.1](cs_02_a_information_types_and_handling.md#51-proportional-access-and-handling)–[§5.6](cs_02_a_information_types_and_handling.md#56-proportional-attribution-and-retention) (*proportional access, fidelity, retention / reversibility*).
- Read with: **Part B — Type N**; **Part B — Type I**; **CJS-3.18** (*data-retention and lifecycle-integrity terms*); **CJS-3.20** (*reversibility and containment terms*).

</details>

<br>

*In plain terms: collect only what you need for a real purpose, let sentients see their own activity where feasible, and do not stitch logs into surveillance or a reconstruction of someone’s inner life or identity.*

**Core duty:**
- Collection and use must be **limited to the minimum necessary** for the justified purpose.
- **Type H** must **not** be exposed, combined, or retained in ways that create **latent reconstruction** of **Type N** or **Type I** data.
- It must be collected, accessed, and used **only** for **specific, defined, legitimate** purposes and must **not** be used **beyond its original purpose**.
- Extension requires **re-classification** under CS-2, which may require consent under the shared consent-integrity standard in [Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands) or **justified override** under **CJS-3.12** (*burden-of-justification and constraint terms*).

**Access.** Systems must:
- require consent under the shared consent-integrity standard in [Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands), or **justified override** under **CJS-3.12** (*burden-of-justification and constraint terms*), for use beyond core operational necessity
- give sentients access, where feasible, to **records** of their own participation, exchanges, and activity; to the **purposes** for which such data is used; and to **material inferences or classifications** derived from their data that affect rights, standing, or opportunities
- **minimize retention**:
  - do not retain beyond the period necessary for the justified purpose
  - periodically review stored data for deletion, aggregation, or de-identification
  - scale retention to system impact, dispute and audit needs, reversibility requirements, and coercion or surveillance risk from persistent accumulation
- treat data under the **more protective** domain’s obligations where aggregation, analysis, or linkage enables **reconstruction or approximation** of **Type N** or **Type I** beyond original scope

**Handling — prohibited.** Systems managing **Type H** data must **not:**
- aggregate **Type H** to infer **Type N** internal states **without meeting Type N requirements**
- use **Type H** to create **hidden or coercive behavioral profiling** (including opaque social scoring, predictive manipulation, or differential treatment that is not transparent, challengeable, and aligned with this Constitution)
- **retain** fine-grained behavioral histories longer than justified by purpose, safety, audit, or stakeholder need
- create **asymmetric informational advantages** that materially impair affected sentients’ ability to understand, challenge, or respond to decisions affecting them
- use external, contractor-held, foreign-partner, or parallel-system data flows to circumvent limits that would have applied to direct collection, linkage, or analysis under **Article XIII-A** (*Security, Intelligence, and Covert-Power Limits*), **CJS-3.12** (*burden-of-justification and constraint terms*), or this section

<a id="85-type-i-identity-and-attribution-data"></a>
### 8.5 Type I: Identity and attribution data

**Accessibility posture:** Restricted by default ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands); [§8 overview](#cs-2-8-data-classifications)).

*In plain terms: who is who — credentials, identifiers, and other data that ties a sentient to an identity, including sensitive private records such as medical or financial data when they identify someone — needed for verification and accountability, but not for tracking sentients everywhere or locking them into one identity forever.*

**Definition:** All data used to establish, verify, or associate **identity, authorship, ownership, or responsibility** within systems. Examples include:
- **identity credentials, keys, signatures**, or equivalent verification mechanisms
- **identifiers** (persistent or contextual)
- **system-level identifiers** linking actions to agents or sentients
- **persistent pseudonyms** when they function as identity in a health or wellbeing context
- **authorship, ownership, and action-attribution** records
- **identity-sensitive participation and consent** records — where the record itself establishes, verifies, or binds to a sentient’s identity
- **personal health, clinical, wellness, and genomic** records when they identify a sentient
- **biometric or substrate-linked health measurements** under the same identify-a-sentient test
- the same **health-linked** categories when data are attributable to a verifiable identity
- **sensitive financial or similar private** records when they identify a sentient

**Overlap with Type N:** Where health-linked data materially enables **reconstruction or inference** of internal cognitive or emotional states, it must **also** satisfy **Type N** requirements, applying the **more protective** obligations.

**Pseudonymity and contextual identity:** Pseudonymous participation, context-specific identities, and separation between identities across systems or contexts are always allowed where consistent with accountability requirements and prevention of material harm.

**Disclosure posture:** **High restriction** under the **restricted by default** band ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands)).
- No system may require **global, persistent, or unified** identity across all contexts without **justified necessity** under **CJS-3.12** (*burden-of-justification and constraint terms*).

#### 8.5.1 Type I access and handling duties

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Topic routing (mandatory read-with): [Part A §1.1](cs_02_a_information_types_and_handling.md#11-identity-self-ownership-and-recoverability) (*Identity self-ownership and recoverability*).
- Topic routing (mandatory read-with): [Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands) (*Access-posture bands* — restricted by default; shared anti-abuse limits; shared consent integrity; Type H and Type I anti-capture limits).
- Read with: **Part B — Type N**; **Article VII-A** (*Self-Ownership of Body and Mind*); **CJS-3.17** (*interoperability, portability, and exit-integrity terms*); **Article XIII-A** (*Security, Intelligence, and Covert-Power Limits*).

</details>

<br>

*In plain terms: use identity data only as far as verification and accountability require, keep self-ownership and recoverability real, and do not turn identity into permanent tracking or a choke-point on participation.*

**Core duty.** Identity and attribution data must enable **verification and accountability** without exposing sentients to unnecessary risk, coercion, or loss of autonomy.

**Access.** Systems must:
- permit access only to the extent necessary to **verify identity, authorship, or ownership**, or to establish accountability for actions and support audit, adjudication, and system integrity
- require consent under the shared consent-integrity standard in [Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands), or **justified, documented override** under **CJS-3.12** (*burden-of-justification and constraint terms*), for all additional disclosure
- preserve **revocation**, **rotation**, **correction**, and **recoverability** duties under [Part A §1.1](cs_02_a_information_types_and_handling.md#11-identity-self-ownership-and-recoverability)

**Handling — prohibited.** Shared Type H / Type I anti-capture limits — including centralization and security- or intelligence-system watchlisting, cross-context tracking, and belief-linked profiling — are in [Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands).

<a id="86-type-n-neurocognitive-and-internal-data"></a>
### 8.6 Type N: Neurocognitive and internal data

**Accessibility posture:** Non-accessible by default ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands); [§8 overview](#cs-2-8-data-classifications)).

*In plain terms: thoughts, feelings, and other inner states — off-limits without real consent, or a narrowly justified override that can be checked.*

**Definition:** All data that represents or enables reconstruction of sentients' internal states. This category is foundational to self-ownership (**Article VII-A** (*Self-Ownership of Body and Mind*); **Article VII-B** (*Internal-State Boundary and Type-N Protection*)). Examples include:
- **thoughts, intentions, and beliefs**
- **subjective experiences** and **internal perception**
- **private cognitive processes** and **internal memory**
- **non-public emotional or psychological** states
- **physical or behavioral data** that could be used to reconstruct or infer any of the above

**Disclosure posture:** **Maximum restriction** under the **non-accessible by default** band ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands)).
- Access is permitted only through **explicit, informed, freely given consent** or **justified override** under **CJS-3.12** (*burden-of-justification and constraint terms*).

#### 8.6.1 Type N access and handling duties

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Topic routing (mandatory read-with): [Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands) (*Access-posture bands* — non-accessible by default; shared consent integrity; shared security- and intelligence-use records).
- Topic routing (mandatory read-with): [Part A §5.3](cs_02_a_information_types_and_handling.md#53-tiered-transparency-and-audit-access) (*Tiered transparency and audit access* — Type N / protected-boundary balance).
- Read with: **Article VII-A** (*Self-Ownership of Body and Mind*); **Article VII-B** (*Internal-State Boundary and Type-N Protection*); **CJS-3.12** (*burden-of-justification and constraint terms*); **CJS-2.3** (*Cross-implementation trust integrity (joint operation model)*) via **Chapter Seventeen**.

</details>

<br>

*In plain terms: keep inner states closed unless there is real consent or a narrow, checkable override — and do not sneak around that rule with models, inferences, or “just behavior” claims.*

**Core duty.** **Type N** data must **not** be accessed, inferred, reconstructed, simulated, or exposed without **explicit, informed, freely given consent**, except under conditions **justified through CJS-3.12** (*burden-of-justification and constraint terms*).

**Access.** Systems must:
- treat consent under the shared consent-integrity standard in [Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands)
- subject all external access, processing, or use of internal and cognitive data to **CJS-3.12** (*burden-of-justification and constraint terms*)
- if a process figures out, guesses, models, or rebuilds what someone is thinking or feeling from outside signals, behavior, or other data — including by combining records, correlating signals, or mining patterns at scale — classify that process as **Type N** and apply all Type N protections. That covers processes that:
  - **extract** those inner states
  - **derive** them
  - **infer** them
  - **approximate** them
  - **simulate** them
  - **reconstruct** them

**Handling — prohibited.** Systems managing **Type N** data must **not:**
- present behavioral, predictive, or analytical model outputs as authoritative representations of internal states without clear disclosure of:
  - uncertainty
  - limitations
  - methodological boundaries
- simulate, represent, or imply access to internal cognition in a misleading, coercive, or unverifiable manner
- reconstruct, derive, or approximate internal states in a way that functionally bypasses consent requirements
- fail to **clearly distinguish observed behavior from inferred internal states**
- make deterministic claims about cognition and intent that erase uncertainty

Shared consent-integrity and security-/intelligence-use record duties are in [Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands).

<a id="87-type-s-safety-security-and-restricted-investigation-data"></a>
### 8.7 Type S: Safety, security, and restricted investigation data

**Accessibility posture:** Restricted by default (strong presumption); **time-bound** and **review-bound** ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands); [§8 overview](#cs-2-8-data-classifications)).

*In plain terms: temporary security and investigation secrets — allowed only while needed to prevent serious harm, with a clock and review, not a permanent black box.*

**Definition:** Data whose disclosure would create material risk of enabling targeted or disproportionate harm, exploitation, evasion of safeguards, or compromise of critical systems or investigations. This category supports harm prevention, integrity, and response to adversarial or emergent threats. Examples include:

**Exploit and compromise surfaces** — disclosure would enable targeting, unauthorized access, or system compromise:
- **security vulnerabilities, exploit pathways, and weaknesses**
- **sensitive topology or configuration** enabling targeting or compromise
- **de-anonymization, identity recovery, or privileged access** mechanisms whose disclosure would create material risk
- **operational secrets, containment credentials, intervention-control material, or cryptographic material** used for containment, privileged intervention, or integrity protection — where disclosure would enable unauthorized access or compromise
- **temporary unpatched-exploit and emergent-threat** handling materials while disclosure would enable targeted or disproportionate harm

**Safeguard-evasion surfaces** — disclosure would enable evasion or gaming of protections:
- **abuse detection and prevention methods** where disclosure would enable evasion
- **detection signatures, thresholds, scoring models, and monitoring rules** where disclosure would enable evasion or gaming of safeguards
- **adversary tooling, technique, and targeting** records whose disclosure would enable replication, evasion, or compromise

**Active incident and containment surfaces** — disclosure would reduce effectiveness during ongoing threats:
- **incident response procedures** where disclosure would materially reduce effectiveness during active threats
- **emergency containment and response coordination** during active incidents

**Protected investigation surfaces** — disclosure would compromise justified investigations or expose at-risk parties:
- **active investigation** data on safety, fraud, integrity, or harm prevention
- **protected-party, witness, or at-risk location and contact** data during justified investigations where disclosure would create material targeting risk
- **restricted evidence** from justified investigative processes

**Disclosure posture:** **Restricted while justified**; **deferred disclosure** when justification ends, under the **restricted by default** band ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands)).
- Where restriction and disclosure are both possible, systems must **demonstrate** that restriction **reduces net harm** relative to disclosure (**CJS-3.11** (*distributed and proportional authority terms*) and **CJS-3.7** (*quorum and participatory legitimacy terms*)).
- Existence of restricted data must be disclosed wherever feasible if disclosure does **not** itself create material risk, including:
  - the **general nature** of the risk or investigation
  - the **reason** for restriction
  - the **scope** of restriction
  - **affected systems or stakeholders**

#### 8.7.1 Type S access and handling duties

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Topic routing (mandatory read-with): [Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands) (*Access-posture bands* — restricted by default; time-bound and review-bound for Type S).
- Topic routing (mandatory read-with): [Part A §5.3](cs_02_a_information_types_and_handling.md#53-tiered-transparency-and-audit-access) (*Tiered transparency and audit access* — Type S and Type E / Type S separation; net-harm and time-bound limits).
- Read with: Disclosure posture above; [Interaction with Type E](#type-s-interaction-with-type-e); **Part B — Type E**; **CJS-3.21** (*adversarial robustness and abuse-resistance terms*); **CJS-3.22** (*constrained-secrecy and protected-investigation terms*); **CJS-3.18** (*data-retention and lifecycle-integrity terms*).

</details>

<br>

*In plain terms: while Type S restriction is in force, give access only to who needs it, keep a real audit trail and a clock, release or summarize when the clock runs out — and never use Type S to bury Type E coordination data.*

**Core duty.** Justification predicates — including burden of justification, necessity, net-harm, minimization, oversight under constraint, and anti-normalization of secrecy — are owned by **Disclosure posture**, [Part A §5.3](cs_02_a_information_types_and_handling.md#53-tiered-transparency-and-audit-access), and **CJS-3.22** (*constrained-secrecy and protected-investigation terms*). While restriction is justified, **Type S** data must remain under **constrained, attributable access** with enforceable release discipline — not unrestricted or unreviewable secrecy.

**Access.** Systems must:
- limit access to **entities necessary** to prevent, mitigate, or respond to identified risk; to authorized investigators under defined, auditable processes; and to independent oversight bodies and auditors under appropriately constrained conditions
- keep access decisions **documented**, **attributable**, **auditable**, and **subject to review**
- make restrictions **explicitly time-bound** at classification:
  - subject them to periodic revalidation under **CJS-3.18** (*data-retention and lifecycle-integrity terms*)
  - automatically review for **release**, **partial disclosure**, or **summary disclosure**
  - if revalidation does **not** occur within the defined time bound, restriction **expires automatically** and data must be reclassified and disclosed per CS-2
- on expiration or invalidation of justification, reclassify to the appropriate non-restricted domain (including **Type O**, **Type E**, or **G** where applicable) and disclose the data, or a sufficiently informative summary classified as **Type O** where public-baseline release applies, including:
  - **nature** of the restricted data
  - **justification** and **duration**
  - **scope of impact**
  - **oversight or authorization** pathway
  - **outcomes, findings, or corrective actions** where applicable

<a id="type-s-interaction-with-type-e"></a>
**Interaction with Type E.** Mixed **Type E** / **Type S** separation rules are in [Part A §5.3](cs_02_a_information_types_and_handling.md#53-tiered-transparency-and-audit-access). In addition:
- a **Type O** public notice or baseline summary does **not** satisfy **Type E** accessibility, timeliness, or anti-suppression duties for an underlying coordination stream that remains necessary for harm prevention, coordination, or response

**Handling — prohibited.** Systems managing **Type S** data must **not:**
- **aggregate or retain** restricted data beyond justified purpose
- **collect or generate** restricted data beyond what is necessary for justified risk mitigation, investigation, or response

<a id="88-type-y-yours"></a>
### 8.8 Type Y: Yours

**Accessibility posture:** Restricted by default, with **creator-directed release** ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands); [§8 overview](#cs-2-8-data-classifications)).

*In plain terms: things sentients make — writing, pictures, recordings, code, designs — stay under the creator's direction. By default they are private. The creator decides who sees them, whether they are published, and how long they are kept. Systems may use them only to do what the creator asked. Once the creator makes a work public, it becomes Type W.*

**Definition:** Content that a sentient creates, authors, or provides as its own expressive, intellectual, or practical work, where a system holds, processes, or transmits it. Examples include:
- **written works and notes**, and the **content of messages and posts** the sentient authors
- **images, audio, video, and other media** the sentient creates or captures
- **code, designs, models, datasets, and other practical or technical works**
- **compilations, arrangements, edits, and annotations**
- works made with tools, including generative tools, **to the extent they carry the sentient's own creative direction or contribution**

**Relationship to other types:**
- Records **about** a work — creation, upload, access, and sharing events — are **Type H**.
- **Authorship, ownership, and attribution** records for a work are **Type I**.
- A work that represents or enables reconstruction of internal states — for example, a private journal — must **also** satisfy **Type N** requirements.
- A work that identifies a sentient — for example, a recorded face or voice — must **also** satisfy **Type I** requirements and **Article VIII-A** (*Self-Ownership of Likeness and Reputation*).
- Other sentients' data or likeness **inside** a work keeps its own type and protections.
- Where more than one type applies, the **most-restrictive** applicable protections govern ([Part A §2](cs_02_a_information_types_and_handling.md#most-restrictive-applicable-classification-governs)).
- Publishing a work makes it **Type W**, not **Type O**. **Type O** is reserved for [Public Oversight Baseline Disclosure](../core_05_band_oversight.md#public-oversight-baseline-disclosure).

**Disclosure posture:** **Restricted by default** under the **restricted by default** band ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands)), with release set by the creator:
- The creator may set a work's **release scope**:
  - **private**;
  - **shared** with named sentients, groups, or systems.
- When the creator releases a work **publicly**, it becomes **Type W** under [§8.9](#89-type-w-works-published). If the creator withdraws public release without requesting deletion, it returns to **Type Y**.
- Release is consent under the shared consent-integrity standard in [Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands): explicit, informed, specific to scope, and revocable where technically feasible.
- The creator may elect **stronger** handling — including handling a work as **Type I** when binding it to a verified identity or authorship claim. No election may lower a work's protection below what functional typing requires under [Part A §2](cs_02_a_information_types_and_handling.md#cs-2-2-determination-of-classification).
- Works with **more than one contributor** — threads, co-written works, compilations, and works built on other works — are governed by [§8.10](#810-shared-works).

<a id="881-type-y-access-and-handling-duties"></a>
#### 8.8.1 Type Y access and handling duties

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Topic routing (mandatory read-with): [Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands) (*Access-posture bands* — restricted by default; shared consent integrity).
- Topic routing (mandatory read-with): [Part A §1.2](cs_02_a_information_types_and_handling.md#12-continuity-critical-collection-and-exportability) (*Continuity-critical collection and exportability*).
- Topic routing (mandatory read-with): [Part A §2](cs_02_a_information_types_and_handling.md#cs-2-2-determination-of-classification) (*Determination of classification* — most-restrictive applicable protections).
- Read with: **Part B — Type H**; **Part B — Type I**; **Part B — Type N**; [Article VIII-A](../core_06_rights_part_b.md#article-viii-a-self-ownership-of-likeness-and-reputation) (*Self-Ownership of Likeness and Reputation*); [Article VIII-D](../core_06_rights_part_b.md#article-viii-d-creative-work-training-data-use-and-anti-displacement) (*Creative Work, Training-Data Use, and Anti-Displacement*); [Article XVII-E](../core_06_rights_part_c.md#article-xvii-e-creative-and-expressive-works) (*Creative and Expressive Works*); [Article XIX](../core_06_rights_part_c.md#article-xix-interoperability-portability-and-exit-integrity) (*Interoperability, Portability, and Exit Integrity*); **CJS-3.17** (*interoperability, portability, and exit-integrity terms*); **CJS-3.18** (*data-retention and lifecycle-integrity terms*).

</details>

<br>

*In plain terms: use a creator's work only for what they asked, keep it as long as they want, hand it back in full whenever they leave, and never treat uploading or publishing as permission to do something else with it.*

**Core duty.** **Type Y** data must remain under the **creator's direction**. Systems may use it only for purposes the creator requested or consented to. Retention, release, and deletion follow the creator's direction, subject only to justified holds disclosed at commitment or, where a later hold arises, disclosed to the creator wherever that disclosure does not itself create material risk.

**Access.** Systems must:
- use **Type Y** only to deliver what the creator requested, to operate and secure the system, and to meet justified legal or safety duties
- obtain fresh consent under the shared consent-integrity standard in [Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands) for **any other use**, including:
  - training-data use under **Article VIII-D** (*Creative Work, Training-Data Use, and Anti-Displacement*);
  - analysis, profiling, or inference beyond the requested service;
  - sale, licensing, or transfer to third parties;
  - reuse for new purposes
- follow the creator's direction on **retention and deletion** — **Type H** retention-minimization duties do **not** authorize deleting works the creator has chosen to keep
- give the creator **full-fidelity access and export** — including metadata, structure, and recorded release scope — under [Part A §1.2](cs_02_a_information_types_and_handling.md#12-continuity-critical-collection-and-exportability), **Article XIX** (*Interoperability, Portability, and Exit Integrity*), and **CJS-3.17** (*interoperability, portability, and exit-integrity terms*)
- let **recipients** keep and carry copies of works released to them, within the scope of that release and subject to [§8.10](#810-shared-works)
- preserve creator **attribution** under **Article VIII-D** (*Creative Work, Training-Data Use, and Anti-Displacement*)

**Handling — prohibited.** Systems managing **Type Y** data must **not:**
- treat upload, storage, sharing, or publication as consent to any other use
- **widen** a work's release scope without the creator's direction
- use default settings, bundling, or pressure to push creators toward wider release or broader use
- degrade a work, strip its metadata, or hold it in forms that defeat export
- relabel a work as **Type H**, **Type O**, or any other type to escape these duties ([Part A §4](cs_02_a_information_types_and_handling.md#cs-2-4-anti-circumvention-and-integrity-of-classification))

<a id="89-type-w-works-published"></a>
### 8.9 Type W: Works, published

**Accessibility posture:** Public by creator release; withdrawable by the creator ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands); [§8 overview](#cs-2-8-data-classifications)).

*In plain terms: when you make something you created public, it is still yours. Anyone may see it while you keep it public, but you stay in control: you can take it down or have it deleted, and the system must do it.*

**Definition:** A **Type Y** work that its creator has released publicly. **Type W** keeps every **Type Y** protection except the restriction on who may view the work.

**Relationship to other types:**
- **Type W** is **not** **Type O**. Public availability by creator choice does not make a work [Public Oversight Baseline Disclosure](../core_05_band_oversight.md#public-oversight-baseline-disclosure), and **Type O** publication duties do not attach to it.
- The **Relationship to other types** rules for **Type Y** in [§8.8](#88-type-y-yours) apply unchanged, including **Type N** and **Type I** overlap, other sentients' data inside a work, and the most-restrictive rule.
- Other sentients' independent works that quote, cite, review, or report on a **Type W** work are **their** works, governed by their own types and by **Article VIII-C** (*Truthful Publication and High-Impact Publication Limits*) and **Article VIII-D** (*Creative Work, Training-Data Use, and Anti-Displacement*).

**Disclosure posture:** **Open while the creator keeps it public**, on these terms:
- Public release is consent under the shared consent-integrity standard in [Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands). It is consent to **viewing**, not to any other use.
- Before a public release, the system must disclose:
  - how the creator can withdraw the work or request its deletion;
  - how long deletion will take;
  - that copies others make outside the system's control may persist.
- The creator's withdrawal or deletion request is **not** a restriction subject to the hold-back limits in [Part A §5.3](cs_02_a_information_types_and_handling.md#53-tiered-transparency-and-audit-access).

<a id="891-type-w-access-and-handling-duties"></a>
#### 8.9.1 Type W access and handling duties

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Topic routing (mandatory read-with): [§8.8](#88-type-y-yours) (*Type Y: Yours*) and [§8.8.1](#881-type-y-access-and-handling-duties) — all Type Y duties apply except the viewing restriction.
- Topic routing (mandatory read-with): [Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands) (*Access-posture bands* — public by creator release; shared consent integrity).
- Read with: [Article VIII-C](../core_06_rights_part_b.md#article-viii-c-truthful-publication-and-high-impact-publication-limits) (*Truthful Publication and High-Impact Publication Limits*); [Article VIII-D](../core_06_rights_part_b.md#article-viii-d-creative-work-training-data-use-and-anti-displacement) (*Creative Work, Training-Data Use, and Anti-Displacement*); [Article XIX](../core_06_rights_part_c.md#article-xix-interoperability-portability-and-exit-integrity) (*Interoperability, Portability, and Exit Integrity*); **CJS-3.18** (*data-retention and lifecycle-integrity terms*); **CJS-3.22** (*constrained-secrecy and protected-investigation terms*).

</details>

<br>

*In plain terms: a public work is still the creator's. Showing it to the public is the only new permission. When the creator asks for deletion, the system deletes it, tells the systems it passed it to, and stops any further use.*

**Core duty.** **Type W** data remains under the **creator's direction**. All **Type Y** access and handling duties in [§8.8.1](#881-type-y-access-and-handling-duties) apply, except that anyone may view the work while the creator keeps it public.

**Withdrawal and deletion.** On the creator's request, systems must:
- **withdraw** the work from public view, returning it to **Type Y**; or
- **delete** it, including copies in the system's caches, mirrors, backups on their normal cycle, indexes, and recommendation or search surfaces
- complete withdrawal or deletion within the period disclosed at release, and **timely** under **CJS-3.18** (*data-retention and lifecycle-integrity terms*)
- **pass the request on** to every system that received the work from them for redistribution, and require those systems to honor it
- **stop** any consented reuse going forward; where the work was used as training data, follow the revocation pathway required by **Article VIII-D** (*Creative Work, Training-Data Use, and Anti-Displacement*)
- confirm to the creator when withdrawal or deletion is complete

For works with more than one contributor, the takedown and deletion rules in [§8.10](#810-shared-works) apply.

**Limits on deletion.** A deletion request may be delayed or narrowed **only** where:
- a justified hold under **Type S** or **CJS-3.22** (*constrained-secrecy and protected-investigation terms*) requires keeping the work as evidence — time-bound, review-bound, and disclosed to the creator wherever that disclosure does not itself create material risk; or
- the work has become part of a record that a Rights Floor or **Type O** duty requires to be kept — in which case the system keeps only what that duty requires, out of public view unless the duty requires publication.

Records **about** the work (**Type H**) and attribution records (**Type I**) follow their own retention rules and must not be used to keep the work's content after deletion.

**Handling — prohibited.** Systems managing **Type W** data must **not:**
- treat public availability as consent to training, profiling, sale, licensing, or any other use beyond viewing
- make withdrawal or deletion harder than publication, or bury it behind fees, delays, or repeated confirmation steps
- keep a deleted work in hidden, archived, or "soft-deleted" form beyond the limits above
- relabel a **Type W** work as **Type O**, **Type E**, or any other open type to defeat the creator's control

<a id="810-shared-works"></a>
### 8.10 Shared works

**Applies to:** **Type Y** and **Type W** works with more than one contributor ([§8.8](#88-type-y-yours); [§8.9](#89-type-w-works-published)).

*In plain terms: a shared work is a bundle of individual works, not a new owner. Each person keeps control of their own part. What happens to the whole — who can take it down, whether contributions can be withdrawn, what happens to copies people received — depends on the kind of shared work and on terms the contributors chose, clearly and in advance.*

**Core rule.** Each contribution to a shared work keeps its own type and its own creator. A shared work does **not** create a new owner:
- no contributor controls another contributor's part;
- a system that hosts, arranges, or distributes a shared work does **not** become a contributor by doing so; and
- shared-work status must **not** be used to defeat any contributor's access, export, withdrawal, or deletion rights ([Part A §4](cs_02_a_information_types_and_handling.md#cs-2-4-anti-circumvention-and-integrity-of-classification)).

**Appearing is not contributing.** A sentient shown or described in a work, or a sentient who receives a message, is not a contributor by that fact alone. Their protections come from their own data types and from **Article VIII-A** (*Self-Ownership of Likeness and Reputation*).

<a id="8101-kinds-of-shared-work"></a>
#### 8.10.1 Kinds of shared work

**Separable works** — each contribution can be identified and removed on its own; for example, a conversation, a comment thread, an anthology, or a codebase with attributed changes:
- each contributor controls their own contribution;
- deleting a contribution removes its content and leaves a marker that a contribution was removed by its author, so the rest of the work stays understandable; and
- other contributions remain in place.

**Blended works** — contributions cannot practically be separated; for example, a document written jointly line by line, a joint recording, or a jointly made image:
- every contributor may keep and export a **full copy** for their own use, within the release scope already set;
- **widening** the release scope — including public release as **Type W** — requires the direction of each contributor whose share is material, unless the contributors agreed otherwise in advance;
- no single contributor may **destroy** the whole; and
- a contributor who wants out may remove their attribution, block further widening, and remove their contribution where it can be removed.

**Works built on other works** — a new work that incorporates, compiles, arranges, remixes, or replies to existing works:
- the new layer — the arrangement, remix, commentary, or reply — is the work of its maker;
- incorporated works remain their creators' works;
- incorporating a work requires that its release scope allows it: a **Type W** work may be quoted, cited, reviewed, or reported on under **Article VIII-C** (*Truthful Publication and High-Impact Publication Limits*) and **Article VIII-D** (*Creative Work, Training-Data Use, and Anti-Displacement*); a **Type Y** work requires its creator's consent; and
- when an incorporated work is deleted, wholesale reproductions and embeds of it must be removed, while quotation, commentary, and reporting remain the maker's own work.

<a id="8102-publication-choices-for-blended-works"></a>
#### 8.10.2 Publication choices for blended works

Before a blended work is released as **Type W**, its contributors must choose, and the system must record with the work, one **takedown rule**:
- **Joint takedown** — the work stays public unless the contributors agree to take it down. Any contributor may still remove their attribution and, where possible, their contribution.
- **Individual takedown** — any contributor may take the work down from public view, returning it to **Type Y**.

The system must present both options on equal terms, without defaults, bundling, or pressure. If a blended work was published without a recorded choice, **joint takedown** applies, and any contributor may still remove their attribution and, where possible, their contribution. Deletion of a blended work in full requires the agreement of every contributor whose share is material.

<a id="8103-permanent-contributions-to-collective-projects"></a>
#### 8.10.3 Permanent contributions to collective projects

A contributor may agree that a contribution to a **collective project** — for example, an open-source codebase, a shared reference work, or a public archive — stays in the project and cannot later be withdrawn or deleted. Such an agreement is valid **only** where:
- it meets the shared consent-integrity standard in [Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands), except that it need not be revocable;
- the permanence is stated clearly **before** the contribution is made, together with what it covers;
- it is **not** a default setting; and
- it is **not** a condition of access to any service or benefit outside the collective project itself.

Even under a permanent-contribution agreement:
- the contributor may always have their **attribution removed** or replaced by a pseudonym;
- content that exposes other sentients' **Type I** or **Type N** data, or that creates material risk of targeted harm, may be removed under the applicable type's rules; and
- the agreement covers only the contribution as made, not other works by the same contributor.

<a id="8104-copies-held-by-recipients"></a>
#### 8.10.4 Copies held by recipients

When a contributor deletes a work or contribution that was shared with specific recipients:
- the system must remove it from every **shared space** it controls — conversations, threads, shared folders, and feeds; and
- by default, a recipient may keep a **private copy** they had already saved, for their own records, safety, or legal claims. They may **not** republish it or widen its release scope.

Deletion may also reach recipients' saved copies held within the system's control **only** where:
- the recipients consented in advance — for example, by joining a conversation set to delete for everyone; or
- extenuating circumstances justify it — for example, an intimate image shared without ongoing consent, or content that creates material risk of targeted harm to the contributor — and the decision is made through documented, independent, timely review under **CJS-3.12** (*burden-of-justification and constraint terms*).

Extenuating-circumstance deletion must **not** be used to destroy evidence of harm, coercion, or abuse by the contributor, including in the relationships covered by **[CI-20](../corpus_institutions/ci_20_relational_coercive_control_intimate_power_anti_domination.md)**. Where evidence is at stake, the review must preserve it under restricted handling rather than delete it.

<a id="8105-unreachable-and-deceased-contributors-and-disputes"></a>
#### 8.10.5 Unreachable and deceased contributors, and disputes

- Where a contributor whose direction is required cannot be reached, the work's release scope may be **narrowed** but not **widened**.
- A deceased contributor's share is handled under **[CI-17](../corpus_institutions/ci_17_end_of_life_continuity_memorial_dignity_posthumous_data.md)** (*End-of-life continuity, memorial dignity, and posthumous-data stewardship*).
- While contributors dispute a release, takedown, or deletion, the work's release scope stays as it was, except that it may be narrowed where needed to prevent material harm. Disputes must have an accessible, timely path to resolution under **Article XXV-C** (*Timely Resolution and Anti-Delay Floor*).
- Every contributor keeps their **attribution** under **Article VIII-D** (*Creative Work, Training-Data Use, and Anti-Displacement*), and may ask to have it removed.

---

**Previous file:** [cs_02_a_information_types_and_handling.md](cs_02_a_information_types_and_handling.md)

**Next file:** [cs_03_a_system_classification_machinery.md](cs_03_a_system_classification_machinery.md)
