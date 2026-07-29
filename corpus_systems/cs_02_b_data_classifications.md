<a id="cs-2-part-b-data-classifications"></a>
## CS-2, Part B: Data classifications

<details>
<summary><strong><span style="color: #2563eb;">Corpus placement (non-operative): file structure and reading rules</span></strong></summary>

> The following content is **reader guidance only**. It does not add, remove, or narrow binding obligations elsewhere in this file or in other CS-2 parts.
>
> This file contains **CS-2, Part B** — data classifications (**Type E** through **Type S**, including **Type O**) as **§8**. Purpose and scope (including identity self-ownership and continuity-critical export), classification determination, anti-circumvention, cross-domain principles, and data separation / attribution (**§§1–7**) are in [`cs_02_a_information_types_and_handling.md`](cs_02_a_information_types_and_handling.md).

</details>

<br>

**CS-2, Part B**, owns **data classifications** (**Type E** through **Type S**, including **Type O**). Classification determination and cross-domain governance are in **[Part A](cs_02_a_information_types_and_handling.md#cs-2-part-a-information-types-and-handling)**.

*In plain terms: Part B names each data type and groups them by how they are usually shared — open, audit-only, restricted, or off-limits — then states each type’s content rules.*

<br>

<a id="8-data-classifications"></a>
### 8. Data classifications

*In plain terms: the letter codes are domain labels, not a ranked sensitivity scale. Types share access-posture bands so common rules can attach to the sharing style. When more than one type fits, the stronger protections win.*

These type letters name different kinds of data and how they are usually shared — not a ranked list from “least sensitive” to “most sensitive.” The letters are labels, not a score order. Each type carries its own protections, which do not rise or fall just because of where it sits in this list. When more than one type could apply, use the strongest applicable protections.

**Access-posture bands.** Types are grouped by **default access posture** so shared band rules in [Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands) apply once. Band order below is for reading clarity only — **not** a sensitivity ranking.

**Open / accessible by default** — strong presumption of openness or accessibility; hold-backs are narrow ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands)):
- **Type O** — Open public oversight baseline disclosure data: [Public Oversight Baseline Disclosure](../core_05defs_oversight.md#public-oversight-baseline-disclosure) for oversight and contestability, including lawful substitutes where Type G, Type E, or other source stays non-public or non-baseline; open by default (strong presumption).
- **Type E** — Environmental, emergency, and survival-coordination data: environment, infrastructure, emergency, and other content streams needed to stay safe and coordinate harm prevention; accessible by default (strong presumption); published Public Oversight Baseline Disclosure artifacts drawn from it are Type O.

**Audit-accessible, not public** — fully auditable; not public by default; public face is Type O ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands)):
- **Type G** — Governance and operational source data: sensitive records of how systems are run, decided, risked, and challenged; fully auditable through structured or qualified audit access, but not public by default.

**Restricted by default** — purpose-limited access; consent or justified override as the type requires ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands)):
- **Type H** — Historical, relational, transactional, and participation data: logs of interactions, exchanges, and activity patterns; restricted by default.
- **Type I** — Identity and attribution data: who is who and who did what, for verification and accountability without unnecessary tracking; restricted by default.
- **Type S** — Safety, security, and restricted investigation data: temporary exploit-, investigation-, or compromise-sensitive material; restricted by default, time-bound, and review-bound.

**Non-accessible by default** — consent or justified override only ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands)):
- **Type N** — Neurocognitive and internal data: thoughts, feelings, and other inner states, including reconstructions or inferences of them; non-accessible by default.

#### 8.1 Type E: Environmental, emergency, and survival-coordination data

**Accessibility posture:** Open / accessible by default (strong presumption) ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands); [§8 overview](#8-data-classifications)).

*In plain terms: data people need to stay safe and coordinate help — environment, infrastructure, emergencies — should stay open and useful unless publishing it would itself cause serious harm.*

**Definition:** Data necessary to preserve sentient survival, environmental integrity, and critical substrate health. This data enables sentients and systems to perceive reality and coordinate harm prevention. Examples include:
- **ecological and environmental condition** data; **air, water, soil, climate, biodiversity, and contamination** data
- **infrastructure health and failure-state** data for survival-critical systems
- **resource availability** for food, water, shelter, energy, processing continuity, and communication access
- **system health, reliability, and degradation** data for critical shared infrastructure
- **emergency condition and hazard** signals (underlying coordination streams, not merely public-baseline notices)
- **where environmental harm comes from and how heavy its load is** on the living world and the shared life-support systems people depend on

**Relationship to Type O:**
- **Type E** is the **content domain** for survival- and coordination-critical data — not [Public Oversight Baseline Disclosure](../core_05defs_oversight.md#public-oversight-baseline-disclosure).
- Published Public Oversight Baseline Disclosure artifacts drawn from **Type E** — including aggregated public environmental or hazard summaries, published emergency notices at public-baseline fidelity, and other baseline disclosure artifacts — must be classified and handled as **Type O**.
- Where a **Type O** baseline applies, systems must still release sufficient [Public Oversight Baseline Disclosure](../core_05defs_oversight.md#public-oversight-baseline-disclosure) even when the underlying streams remain **Type E**.
- A **Type O** notice must leave the underlying coordination stream’s **Type E** accessibility, timeliness, and anti-suppression duties fully in force.

**Disclosure posture:** **Presumptive accessibility** under the **open / accessible by default** band ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands)). Narrow hold-backs require justification under **CJS-5.12** (*burden-of-justification and constraint terms*) and **CJS-5.5** (*independent verification and claim-integrity terms*). Shared timeliness, presentation, fidelity, and restriction-discipline rules are in [Part A §5.1](cs_02_a_information_types_and_handling.md#51-proportional-access-and-handling)–[§5.3](cs_02_a_information_types_and_handling.md#53-tiered-transparency-and-audit-access).

##### 8.1.1 Type E access and handling duties

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Topic routing (mandatory read-with): [Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands) (*Access-posture bands* — open / accessible by default).
- Topic routing (mandatory read-with): [Part A §5.3](cs_02_a_information_types_and_handling.md#53-tiered-transparency-and-audit-access) (*Tiered transparency and audit access* — narrow-scope, time-bound, documentation, net-harm, and Type E / Type S separation rules).
- Read with: [Part B — Type S · Interaction with Type E](#type-s-interaction-with-type-e).

</details>

<br>

*In plain terms: keep survival and coordination data usable where people need it, make access real rather than symbolic, limit secrecy to cases where publishing would itself cause serious harm, and never fake openness by starving, hiding, or failing to maintain the data.*

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

#### 8.2 Type G: Governance and operational source data

**Accessibility posture:** Audit-accessible, not public ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands); [§8 overview](#8-data-classifications)).

*In plain terms: the sensitive internal records of how a system is run, what it decides, what can go wrong, and how it is challenged — fully open to real audit, but not dumped into public view. What the public must see is Type O.*

**Definition:** Sensitive governance and operational **source** records required for meaningful oversight, audit, reconstruction, and constitutional accountability — including material whose full fidelity is inappropriate for public release but must remain **fully auditable**. Examples include:
- **internal governance records**, working procedural materials, and non-public classification or policy working papers
- **full deliberation, voting, quorum, and decision** records beyond what is lawfully published as **Type O**
- **detailed audit trails, compliance workpapers, and forensic reconstruction** materials
- **operational telemetry, configuration, methodology, evaluation criteria, and assumption** records at source fidelity
- **full-fidelity risk, dependency, and system-impact** analyses
- **challenge, review, and corrective-action** source dockets not themselves released as **Type O**

**Relationship to Type O:**
- **Type G** is **not** [Public Oversight Baseline Disclosure](../core_05defs_oversight.md#public-oversight-baseline-disclosure).
- Public Oversight Baseline Disclosure publication — including summaries, aggregates, de-identified releases, delayed releases, and other lawful substitutes drawn from **Type G** source — must be classified and handled as **Type O**.
- When [Public Oversight Baseline Disclosure](../core_05defs_oversight.md#public-oversight-baseline-disclosure) is required, systems must still publish a usable Type O disclosure — even if the **Type G** source records stay non-public.

**Disclosure posture:** **Not public by default** under the **audit-accessible, not public** band ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands)). Access is through **structured or qualified audit access** under **CJS-5.3** (*auditability and reconstructability terms*) and **CJS-5.4** (*tiered transparency and audit-access terms*), with public-facing accountability carried by **Type O**.

<a id="821-type-g-access-and-handling-duties"></a>
##### 8.2.1 Type G access and handling duties

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Topic routing (mandatory read-with): [Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands) (*Access-posture bands* — audit-accessible, not public).
- Topic routing (mandatory read-with): [Part A §5.3](cs_02_a_information_types_and_handling.md#53-tiered-transparency-and-audit-access) (*Tiered transparency and audit access*).
- Topic routing (mandatory read-with): [Part A §2](cs_02_a_information_types_and_handling.md#2-determination-of-classification) (*Determination of classification* — most-restrictive applicable protections).
- Read with: **Part B — Type O** (*Public Oversight Baseline Disclosure*); **CJS-5.3** (*auditability and reconstructability terms*); **CJS-5.4** (*tiered transparency and audit-access terms*).

</details>

<br>

*In plain terms: keep the full governance record auditable, give real auditors what they need, and never use “not public” as a shield against review or as a substitute for Public Oversight Baseline Disclosure.*

**Core duty.** **Type G** data must remain **fully auditable** — reconstructable, attributable, and reviewable — so independent oversight can verify how systems operate, how decisions are made, what risks exist, and how challenges are handled. Non-public status must **not** function as unreviewable secrecy.

**Access.** Systems must:
- provide **Type G** data to authorized auditors, oversight bodies, and other qualified reviewers in a manner that is **understandable**, **documented**, **attributable**, **versioned** where material changes occur, and **retained** for a duration proportional to system impact and dependency
- publish access gates, eligibility rules, and qualification routes for audit as **Type O** where they govern who may reach **Type G** source
- preserve audit sufficiency and publish the strongest feasible **Type O** substitute where [Public Oversight Baseline Disclosure](../core_05defs_oversight.md#public-oversight-baseline-disclosure) applies, when raw **Type G** disclosure is inappropriate under [Part A §7](cs_02_a_information_types_and_handling.md#7-type-o-baseline-for-class-abc-systems) or more-restrictive applicable typing under [Part A §2](cs_02_a_information_types_and_handling.md#2-determination-of-classification)
- **limit further restriction of audit access** so that:
  - it does **not** defeat Disclosure posture or the **audit-accessible, not public** band ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands))
  - further restriction is permitted only where more-restrictive applicable typing under [Part A §2](cs_02_a_information_types_and_handling.md#2-determination-of-classification) or [Part A §5.3](cs_02_a_information_types_and_handling.md#53-tiered-transparency-and-audit-access) (*Tiered transparency and audit access*) requires it
  - further restriction is **not** used for convenience, reputational protection, or power preservation

**Handling — prohibited.** Systems managing **Type G** data must **not:**
- classify governance-relevant or operationally material information as secret **merely** for convenience, reputational protection, or power preservation
- treat non-public **Type G** status as a substitute for [Public Oversight Baseline Disclosure](../core_05defs_oversight.md#public-oversight-baseline-disclosure)
- provide **performative summaries** while withholding information necessary for meaningful qualified audit
- use **complexity, opacity, or format fragmentation** to defeat auditability (contrary to **CJS-5.8** (*comprehensibility and cognitive accessibility terms*), **CJS-5.10** (*disclosure sufficiency and observability terms*), and **CJS-5.3** (*auditability and reconstructability terms*))

<a id="type-o-open-public-baseline-disclosure-data"></a>
#### 8.3 Type O: Open public oversight baseline disclosure data

**Accessibility posture:** Open / accessible by default (strong presumption for Public Oversight Baseline Disclosure release) ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands); [§8 overview](#8-data-classifications)).

*In plain terms: [Public Oversight Baseline Disclosure](../core_05defs_oversight.md#public-oversight-baseline-disclosure) — what must be published so people can understand high-impact systems, including a strong public substitute when Type G, Type E, or other raw private or non-baseline records cannot be released as that disclosure.*

**Definition:** Data released or required to be released as [Public Oversight Baseline Disclosure](../core_05defs_oversight.md#public-oversight-baseline-disclosure) for transparency, oversight, and contestability — including lawful substitutes where **Type G**, **Type E**, or other source records remain non-public, non-baseline, or otherwise restricted. Canonical meaning is in Chapter Five; this type owns systems-layer typing and handling.

**Class A/B/C public-baseline content.** Where the [Type O baseline for Class A/B/C](cs_02_a_information_types_and_handling.md#7-type-o-baseline-for-class-abc-systems) applies, **Type O** carries [Public Oversight Baseline Disclosure](../core_05defs_oversight.md#public-oversight-baseline-disclosure) — the **public explanation** of chartered and certified scope — mapped under Part A §7 from the governing [Charter](../core_05defs_continuity.md#charter) (or equivalent), assigned class, and observed [System Boundaries](../core_05defs_continuity.md#system-boundaries) — not a second taxonomy. It includes information people need to understand:
- what the system does
- how it is classified
- what depends on it
- how it is running
- what can go wrong
- how it is governed
- its degree of alignment with this Constitution

**Other examples include:**
- the **published Charter** (or equivalent published scope instrument) itself, at public-baseline fidelity
- **published certification, governance, and audit records** required for Public Oversight Baseline Disclosure visibility
- **published procedural rules, system classifications, and disclosed assumptions** at public-baseline fidelity
- **aggregated, de-identified, summary, or delayed** public releases that substitute for **Type G**, **Type E**, or other restricted or non-baseline source data
- **published emergency notices and aggregated environmental or public-risk summaries** at public-baseline fidelity drawn from **Type E** streams
- **public eligibility rules and routing** for qualified audit access to **Type G** or other non-public source
- **versioned public change notices, operational status, and material-risk summaries** for baseline understanding

**Relationship to other types:**
- **Type G** holds sensitive governance and operational **source** that is audit-accessible but not public by default.
- **Type E** holds survival- and coordination-critical **content streams** that are accessible by default under Type E duties and are **not** themselves [Public Oversight Baseline Disclosure](../core_05defs_oversight.md#public-oversight-baseline-disclosure).
- **Type O** governs the **publication posture** of Public Oversight Baseline Disclosure artifacts, including substitutes derived from **Type G** or **Type E**.

**Disclosure posture:** **Baseline public accessibility** under the **open / accessible by default** band ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands)). Deeper structured or qualified audit access to **Type G** (or other non-public source) may run in parallel but must not replace [Public Oversight Baseline Disclosure](../core_05defs_oversight.md#public-oversight-baseline-disclosure) where **Type O** applies.

##### 8.3.1 Type O access and handling duties

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Topic routing (mandatory read-with): [Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands) (*Access-posture bands* — open / accessible by default).
- Topic routing (mandatory read-with): [Part A §7](cs_02_a_information_types_and_handling.md#7-type-o-baseline-for-class-abc-systems) (*Type O baseline for Class A/B/C systems* — scoped by Charter, class, and System Boundaries; verified under Chapter Seven).
- Topic routing (mandatory read-with): [Part A §5.3](cs_02_a_information_types_and_handling.md#53-tiered-transparency-and-audit-access) (*Tiered transparency and audit access*).
- Topic routing (mandatory read-with): [Part A §2](cs_02_a_information_types_and_handling.md#2-determination-of-classification) (*Determination of classification* — most-restrictive applicable protections).
- Read with: [Public Oversight Baseline Disclosure](../core_05defs_oversight.md#public-oversight-baseline-disclosure); [Charter](../core_05defs_continuity.md#charter); [System Boundaries](../core_05defs_continuity.md#system-boundaries); [Chapter Seven §4](../core_07_a_system_alignment_certification_evaluation.md#4-data-types-and-handling-evaluation) (*Data Types and Handling Evaluation*); [Chapter Seven Part B §11](../core_07_b_system_alignment_certification_record_process.md#11-certification-record) (*Certification record*); [Transparency](../core_05defs_oversight.md#transparency); **Article XV** (*Audit, Transparency, and Independent Verification*).

</details>

<br>

*In plain terms: publish the Public Oversight Baseline Disclosure people need, keep it free and usable online where that infrastructure exists, and never treat audit-only access or thin summaries as good enough.*

**Core duty.** **Type O** data must remain sufficiently accessible for informed participation, oversight, and challenge at the Public Oversight Baseline Disclosure tier.

**Access.** Systems must:
- provide **Type O** data in a manner that is **understandable**, **documented**, **attributable**, **versioned** where material changes occur, and **retained** for a duration proportional to system impact and dependency
- where lawful online publication infrastructure exists to support class-appropriate access, make **Type O** data **freely available online** — without paywalls or insider-only substitutes for [Public Oversight Baseline Disclosure](../core_05defs_oversight.md#public-oversight-baseline-disclosure)
- **limit redaction** so it does **not** prevent meaningful accountability at the Public Oversight Baseline Disclosure tier; limited redaction is permitted only where more-restrictive applicable typing under [Part A §2](cs_02_a_information_types_and_handling.md#2-determination-of-classification) or [Part A §5.3](cs_02_a_information_types_and_handling.md#53-tiered-transparency-and-audit-access) / [§7](cs_02_a_information_types_and_handling.md#7-type-o-baseline-for-class-abc-systems) requires it — and only where a lawful **Type O** substitute still preserves meaningful accountability

**Handling — prohibited.** Systems managing **Type O** data must **not:**
- withhold **Type O** material behind paywalls, account barriers beyond reasonable identity verification for restricted tiers, or insider-only distribution substitutes for [Public Oversight Baseline Disclosure](../core_05defs_oversight.md#public-oversight-baseline-disclosure)
- treat **Type O** publication as satisfied by performative summaries while withholding decision-relevant baseline material
- treat non-public **Type G** audit access as a substitute for [Public Oversight Baseline Disclosure](../core_05defs_oversight.md#public-oversight-baseline-disclosure)
- use **complexity, opacity, or format fragmentation** to defeat Public Oversight Baseline Disclosure auditability or contestability
- label restricted source data **Type O** without lawful substitute, reclassification, or release discipline

#### 8.4 Type H: Historical, relational, transactional, and participation data

**Accessibility posture:** Restricted by default ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands); [§8 overview](#8-data-classifications)).

*In plain terms: logs of what people and systems did together — keep only what you need, and do not turn them into surveillance or a back door into someone's identity or inner life.*

**Definition:** Records of interactions, exchanges, participation, and operational events that do **not** by themselves constitute internal cognitive data but may reveal patterns of behavior, dependency, association, or system impact. Examples include:
- **transaction and transfer** records
- **communication and interaction metadata**
- **system access and usage** events
- **participation** records in governance, platforms, or service systems
- **consent receipts and revocation** events
- **dependency and interoperability** events
- **operational logs** connected to sentient or system activity
- **resource usage** records not already classified as Type I or Type H

**Disclosure posture:** **Restricted by default** under the **restricted by default** band ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands)).
- Access is allowed to the extent necessary for **system operation**, **accountability**, **dispute resolution**, **audit**, and **user visibility** into their own activity.
- **Public transparency** is allowed where data is sufficiently aggregated or de-identified such that re-identification risk is minimized under **CJS-5.11** (*distributed and proportional authority terms*) and **CJS-5.7** (*quorum and participatory legitimacy terms*).

##### 8.4.1 Type H access and handling duties

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Topic routing (mandatory read-with): [Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands) (*Access-posture bands* — restricted by default; shared anti-abuse limits; shared consent integrity; Type H and Type I anti-capture limits).
- Topic routing (mandatory read-with): [Part A §5.1](cs_02_a_information_types_and_handling.md#51-proportional-access-and-handling)–[§5.6](cs_02_a_information_types_and_handling.md#56-proportional-attribution-and-retention) (*proportional access, fidelity, retention / reversibility*).
- Read with: **Part B — Type N**; **Part B — Type I**; **CJS-5.18** (*data-retention and lifecycle-integrity terms*); **CJS-5.20** (*reversibility and containment terms*).

</details>

<br>

*In plain terms: collect only what you need for a real purpose, let people see their own activity where feasible, and do not stitch logs into surveillance or a reconstruction of someone’s inner life or identity.*

**Core duty.**
- Collection and use must be **limited to the minimum necessary** for the justified purpose.
- **Type H** must **not** be exposed, combined, or retained in ways that create **latent reconstruction** of **Type N** or **Type I** data.
- It must be collected, accessed, and used **only** for **specific, defined, legitimate** purposes and must **not** be used **beyond its original purpose**.
- Extension requires **re-classification** under CS-2, which may require consent under the shared consent-integrity standard in [Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands) or **justified override** under **CJS-5.12** (*burden-of-justification and constraint terms*).

**Access.** Systems must:
- require consent under the shared consent-integrity standard in [Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands), or **justified override** under **CJS-5.12** (*burden-of-justification and constraint terms*), for use beyond core operational necessity
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
- use external, contractor-held, foreign-partner, or parallel-system data flows to circumvent limits that would have applied to direct collection, linkage, or analysis under **Article XIII-A** (*Security, Intelligence, and Covert-Power Limits*), **CJS-5.12** (*burden-of-justification and constraint terms*), or this chapter

#### 8.5 Type I: Identity and attribution data

**Accessibility posture:** Restricted by default ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands); [§8 overview](#8-data-classifications)).

*In plain terms: who is who — credentials, identifiers, and other data that ties a person to an identity, including sensitive private records such as medical or financial data when they identify someone — needed for verification and accountability, but not for tracking people everywhere or locking them into one identity forever.*

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
- No system may require **global, persistent, or unified** identity across all contexts without **justified necessity** under **CJS-5.12** (*burden-of-justification and constraint terms*).

##### 8.5.1 Type I access and handling duties

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Topic routing (mandatory read-with): [Part A §1.1](cs_02_a_information_types_and_handling.md#11-identity-self-ownership-and-recoverability) (*Identity self-ownership and recoverability*).
- Topic routing (mandatory read-with): [Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands) (*Access-posture bands* — restricted by default; shared anti-abuse limits; shared consent integrity; Type H and Type I anti-capture limits).
- Read with: **Part B — Type N**; **Article VII-A** (*Self-Ownership of Body and Mind*); **CJS-5.17** (*interoperability, portability, and exit-integrity terms*); **Article XIII-A** (*Security, Intelligence, and Covert-Power Limits*).

</details>

<br>

*In plain terms: use identity data only as far as verification and accountability require, keep self-ownership and recoverability real, and do not turn identity into permanent tracking or a choke-point on participation.*

**Core duty.** Identity and attribution data must enable **verification and accountability** without exposing sentients to unnecessary risk, coercion, or loss of autonomy.

**Access.** Systems must:
- permit access only to the extent necessary to **verify identity, authorship, or ownership**, or to establish accountability for actions and support audit, adjudication, and system integrity
- require consent under the shared consent-integrity standard in [Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands), or **justified, documented override** under **CJS-5.12** (*burden-of-justification and constraint terms*), for all additional disclosure
- preserve **revocation**, **rotation**, **correction**, and **recoverability** duties under [Part A §1.1](cs_02_a_information_types_and_handling.md#11-identity-self-ownership-and-recoverability)

**Handling — prohibited.** Shared Type H / Type I anti-capture limits — including centralization and security- or intelligence-system watchlisting, cross-context tracking, and belief-linked profiling — are in [Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands).

#### 8.6 Type N: Neurocognitive and internal data

**Accessibility posture:** Non-accessible by default ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands); [§8 overview](#8-data-classifications)).

*In plain terms: thoughts, feelings, and other inner states — off-limits without real consent, or a narrowly justified override that can be checked.*

**Definition:** All data that represents or enables reconstruction of sentients' internal states. This category is foundational to self-ownership (**Article VII-A** (*Self-Ownership of Body and Mind*); **Article VII-B** (*Internal-State Boundary and Type-N Protection*)). Examples include:
- **thoughts, intentions, and beliefs**
- **subjective experiences** and **internal perception**
- **private cognitive processes** and **internal memory**
- **non-public emotional or psychological** states
- **physical or behavioral data** that could be used to reconstruct or infer any of the above

**Disclosure posture:** **Maximum restriction** under the **non-accessible by default** band ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands)).
- Access is permitted only through **explicit, informed, freely given consent** or **justified override** under **CJS-5.12** (*burden-of-justification and constraint terms*).

##### 8.6.1 Type N access and handling duties

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Topic routing (mandatory read-with): [Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands) (*Access-posture bands* — non-accessible by default; shared consent integrity; shared security- and intelligence-use records).
- Topic routing (mandatory read-with): [Part A §5.3](cs_02_a_information_types_and_handling.md#53-tiered-transparency-and-audit-access) (*Tiered transparency and audit access* — Type N / protected-boundary balance).
- Read with: **Article VII-A** (*Self-Ownership of Body and Mind*); **Article VII-B** (*Internal-State Boundary and Type-N Protection*); **CJS-5.12** (*burden-of-justification and constraint terms*); **CJS-4.3** (*Cross-implementation trust integrity (joint operation model)*) via **Chapter Sixteen**.

</details>

<br>

*In plain terms: keep inner states closed unless there is real consent or a narrow, checkable override — and do not sneak around that rule with models, inferences, or “just behavior” claims.*

**Core duty.** **Type N** data must **not** be accessed, inferred, reconstructed, simulated, or exposed without **explicit, informed, freely given consent**, except under conditions **justified through CJS-5.12** (*burden-of-justification and constraint terms*).

**Access.** Systems must:
- treat consent under the shared consent-integrity standard in [Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands)
- subject all external access, processing, or use of internal and cognitive data to **CJS-5.12** (*burden-of-justification and constraint terms*)
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

#### 8.7 Type S: Safety, security, and restricted investigation data

**Accessibility posture:** Restricted by default (strong presumption); **time-bound** and **review-bound** ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands); [§8 overview](#8-data-classifications)).

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
- Where restriction and disclosure are both possible, systems must **demonstrate** that restriction **reduces net harm** relative to disclosure (**CJS-5.11** (*distributed and proportional authority terms*) and **CJS-5.7** (*quorum and participatory legitimacy terms*)).
- Existence of restricted data must be disclosed wherever feasible if disclosure does **not** itself create material risk, including:
  - the **general nature** of the risk or investigation
  - the **reason** for restriction
  - the **scope** of restriction
  - **affected systems or stakeholders**

##### 8.7.1 Type S access and handling duties

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Topic routing (mandatory read-with): [Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands) (*Access-posture bands* — restricted by default; time-bound and review-bound for Type S).
- Topic routing (mandatory read-with): [Part A §5.3](cs_02_a_information_types_and_handling.md#53-tiered-transparency-and-audit-access) (*Tiered transparency and audit access* — Type S and Type E / Type S separation; net-harm and time-bound limits).
- Read with: Disclosure posture above; [Interaction with Type E](#type-s-interaction-with-type-e); **Part B — Type E**; **CJS-5.21** (*adversarial robustness and abuse-resistance terms*); **CJS-5.22** (*constrained-secrecy and protected-investigation terms*); **CJS-5.18** (*data-retention and lifecycle-integrity terms*).

</details>

<br>

*In plain terms: while Type S restriction is in force, give access only to who needs it, keep a real audit trail and a clock, release or summarize when the clock runs out — and never use Type S to bury Type E coordination data.*

**Core duty.** Justification predicates — including burden of justification, necessity, net-harm, minimization, oversight under constraint, and anti-normalization of secrecy — are owned by **Disclosure posture**, [Part A §5.3](cs_02_a_information_types_and_handling.md#53-tiered-transparency-and-audit-access), and **CJS-5.22** (*constrained-secrecy and protected-investigation terms*). While restriction is justified, **Type S** data must remain under **constrained, attributable access** with enforceable release discipline — not unrestricted or unreviewable secrecy.

**Access.** Systems must:
- limit access to **entities necessary** to prevent, mitigate, or respond to identified risk; to authorized investigators under defined, auditable processes; and to independent oversight bodies and auditors under appropriately constrained conditions
- keep access decisions **documented**, **attributable**, **auditable**, and **subject to review**
- make restrictions **explicitly time-bound** at classification:
  - subject them to periodic revalidation under **CJS-5.18** (*data-retention and lifecycle-integrity terms*)
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

---

**Previous file:** [cs_02_a_information_types_and_handling.md](cs_02_a_information_types_and_handling.md)

**Next file:** [cs_03_system_classification_and_handling.md](cs_03_system_classification_and_handling.md)

