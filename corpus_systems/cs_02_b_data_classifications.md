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
- **Type O** — Open public-baseline disclosure data: the public baseline package for oversight and contestability, including lawful substitutes where Type G, Type E, or other source stays non-public or non-baseline; open by default (strong presumption).
- **Type E** — Environmental, emergency, and survival-coordination data: environment, infrastructure, emergency, and other content streams needed to stay safe and coordinate harm prevention; accessible by default (strong presumption); published baseline packages drawn from it are Type O.

**Audit-accessible, not public** — fully auditable; not public by default; public face is Type O ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands)):
- **Type G** — Governance and operational source data: sensitive records of how systems are run, decided, risked, and challenged; fully auditable through structured or qualified audit access, but not public by default.

**Restricted by default** — purpose-limited access; consent or justified override as the type requires ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands)):
- **Type H** — Historical, relational, transactional, and participation data: logs of interactions, exchanges, and activity patterns; restricted by default.
- **Type I** — Identity and attribution data: who is who and who did what, for verification and accountability without unnecessary tracking; restricted by default.
- **Type S** — Safety, security, and restricted investigation data: temporary exploit-, investigation-, or compromise-sensitive material; restricted by default, time-bound, and review-bound.

**Non-accessible by default** — consent or justified override only ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands)):
- **Type N** — Neurocognitive and internal data: thoughts, feelings, and other inner states, including reconstructions or inferences of them; non-accessible by default.

#### 8.1 Type E: Environmental, emergency, and survival-coordination data

**Default classification:** Accessible by Default (strong presumption). **Access-posture band:** Open / accessible by default ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands); [§8 overview](#8-data-classifications)).

*In plain terms: data people need to stay safe and coordinate help — environment, infrastructure, emergencies — should stay open and useful unless publishing it would itself cause serious harm.*

**Definition:** Data necessary to preserve sentient survival, environmental integrity, and critical substrate health. This data enables sentients and systems to perceive reality and coordinate harm prevention. Examples include:
- **ecological and environmental condition** data; **air, water, soil, climate, biodiversity, and contamination** data
- **infrastructure health and failure-state** data for survival-critical systems
- **resource availability** for food, water, shelter, energy, processing continuity, and communication access
- **system health, reliability, and degradation** data for critical shared infrastructure
- **emergency condition and hazard** signals (underlying coordination streams, not merely public-baseline notices)
- **where environmental harm comes from and how heavy its load is** on the living world and the shared life-support systems people depend on

**Relationship to Type O:**
- **Type E** is the **content domain** for survival- and coordination-critical data — not the public transparency package.
- Published baseline packages drawn from **Type E** — including aggregated public environmental or hazard summaries, published emergency notices at public-baseline fidelity, and other baseline disclosure artifacts — must be classified and handled as **Type O**.
- Where a **Type O** baseline applies, systems must still release a sufficient **Type O** baseline even when the underlying streams remain **Type E**.
- A **Type O** notice must leave the underlying coordination stream’s **Type E** accessibility, timeliness, and anti-suppression duties fully in force.
- For high-impact systems (**Class A**, **B**, and **C**), the rules for publishing a strong public stand-in when raw records cannot be released, and for narrowly limiting what is held back, are in [Part A §7](cs_02_a_information_types_and_handling.md#7-type-o-baseline-for-class-abc-systems).

**Disclosure posture:** **Presumptive accessibility** under the **open / accessible by default** band ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands)). Narrow hold-backs require justification under **CJS-5.12** (*burden-of-justification and constraint terms*) and **CJS-5.5** (*independent verification and claim-integrity terms*). Shared timeliness, presentation, fidelity, and restriction-discipline rules are in [Part A §5.1](cs_02_a_information_types_and_handling.md#51-proportional-access-and-handling)–[§5.3](cs_02_a_information_types_and_handling.md#53-tiered-transparency-and-audit-access).

##### 8.1.1 Type E access and handling duties

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Topic routing (mandatory read-with): [Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands) (*Access-posture bands* — open / accessible by default).
- Topic routing (mandatory read-with): [Part A §5.3](cs_02_a_information_types_and_handling.md#53-tiered-transparency-and-audit-access) (*Tiered transparency and audit access* — narrow-scope, time-bound, documentation, net-harm, and Type E / Type S separation rules).
- Read with: **Part B — Type S** (*Interaction with Type E*).

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

**Default classification:** Audit-Accessible by Default (not public). **Access-posture band:** Audit-accessible, not public ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands); [§8 overview](#8-data-classifications)).

*In plain terms: the sensitive internal records of how a system is run, what it decides, what can go wrong, and how it is challenged — fully open to real audit, but not dumped into public view. What the public must see is Type O.*

**Definition:** Sensitive governance and operational **source** records required for meaningful oversight, audit, reconstruction, and constitutional accountability — including material whose full fidelity is inappropriate for public release but must remain **fully auditable**. Examples include:
- **internal governance records**, working procedural materials, and non-public classification or policy working papers
- **full deliberation, voting, quorum, and decision** records beyond what is lawfully published as **Type O**
- **detailed audit trails, compliance workpapers, and forensic reconstruction** materials
- **operational telemetry, configuration, methodology, evaluation criteria, and assumption** records at source fidelity
- **full-fidelity risk, dependency, and system-impact** analyses
- **challenge, review, and corrective-action** source dockets not themselves released as **Type O**

**Relationship to Type O:**
- **Type G** is **not** the public transparency package.
- Public-baseline publication — including summaries, aggregates, de-identified releases, delayed releases, and other lawful substitutes drawn from **Type G** source — must be classified and handled as **Type O**.
- Where a **Type O** baseline applies, systems must still release a sufficient **Type O** baseline even when **Type G** source remains non-public.
- For high-impact systems (**Class A**, **B**, and **C**), the rules for publishing a strong public stand-in when raw records cannot be released, and for narrowly limiting what is held back, are in [Part A §7](cs_02_a_information_types_and_handling.md#7-type-o-baseline-for-class-abc-systems).

**Disclosure posture:** **Not public by default** under the **audit-accessible, not public** band ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands)). Access is through **structured or qualified audit access** under **CJS-5.3** (*auditability and reconstructability terms*) and **CJS-5.4** (*tiered transparency and audit-access terms*), with public-facing accountability carried by **Type O**.

##### 8.2.1 Type G access and handling duties

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Topic routing (mandatory read-with): [Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands) (*Access-posture bands* — audit-accessible, not public).
- Topic routing (mandatory read-with): [Part A §5.3](cs_02_a_information_types_and_handling.md#53-tiered-transparency-and-audit-access) (*Tiered transparency and audit access*).
- Read with: **Part B — Type O** (*public baseline*); **CJS-5.3** (*auditability and reconstructability terms*); **CJS-5.4** (*tiered transparency and audit-access terms*).

</details>

<br>

*In plain terms: keep the full governance record auditable, give real auditors what they need, and never use “not public” as a shield against review or as a substitute for the public baseline.*

**Core duty.** **Type G** data must remain **fully auditable** — reconstructable, attributable, and reviewable — so independent oversight can verify how systems operate, how decisions are made, what risks exist, and how challenges are handled. Non-public status must **not** function as unreviewable secrecy.

**Access.** Systems must:
- provide **Type G** data to authorized auditors, oversight bodies, and other qualified reviewers in a manner that is **understandable**, **documented**, **attributable**, **versioned** where material changes occur, and **retained** for a duration proportional to system impact and dependency
- publish access gates, eligibility rules, and qualification routes for audit as **Type O** where they govern who may reach **Type G** source
- preserve audit sufficiency and publish the strongest feasible **Type O** substitute where a public baseline applies, if raw **Type G** disclosure would harm privacy, identity, internal-state protection, safety, security, or an active restricted investigation
- **limit further restriction of audit access** to protection of **Type N** data, **Type I** data beyond necessary scope, **active Type S** data related to restricted investigations, or **narrowly scoped** security-sensitive implementation detail where disclosure would create **material risk** — and only where residual audit access remains functionally effective under **CJS-5.3** (*auditability and reconstructability terms*) and **CJS-5.4** (*tiered transparency and audit-access terms*)

**Handling — prohibited.** Systems managing **Type G** data must **not:**
- classify governance-relevant or operationally material information as secret **merely** for convenience, reputational protection, or power preservation
- treat non-public **Type G** status as a substitute for the **Type O** public baseline
- provide **performative summaries** while withholding information necessary for meaningful qualified audit
- use **complexity, opacity, or format fragmentation** to defeat auditability (contrary to **CJS-5.8** (*comprehensibility and cognitive accessibility terms*), **CJS-5.10** (*disclosure sufficiency and observability terms*), and **CJS-5.3** (*auditability and reconstructability terms*))

<a id="type-o-open-public-baseline-disclosure-data"></a>
#### 8.3 Type O: Open public-baseline disclosure data

**Default classification:** Open by Default (strong presumption for public-baseline release). **Access-posture band:** Open / accessible by default ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands); [§8 overview](#8-data-classifications)).

*In plain terms: the public baseline package — what must be published so people can understand high-impact systems, including a strong public substitute when Type G, Type E, or other raw private or non-baseline records cannot be released as the public package.*

**Definition:** Data released or required to be released for **public-baseline** transparency, oversight, and contestability — including lawful substitutes where **Type G**, **Type E**, or other source records remain non-public, non-baseline, or otherwise restricted.

**Class A/B/C public-baseline content.** Where the [Type O baseline for Class A/B/C](cs_02_a_information_types_and_handling.md#7-type-o-baseline-for-class-abc-systems) applies, **Type O** includes information people need to understand:
- what the system does
- how it is classified
- what depends on it
- how it is running
- what can go wrong
- how it is governed
- its degree of alignment with this Constitution

**Other examples include:**
- **published certification, governance, and audit records** required for public baseline visibility
- **published procedural rules, system classifications, and disclosed assumptions** at public-baseline fidelity
- **aggregated, de-identified, summary, or delayed** public releases that substitute for **Type G**, **Type E**, or other restricted or non-baseline source data
- **published emergency notices and aggregated environmental or public-risk summaries** at public-baseline fidelity drawn from **Type E** streams
- **public eligibility rules and routing** for qualified audit access to **Type G** or other non-public source
- **versioned public change notices, operational status, and material-risk summaries** for baseline understanding

**Relationship to other types:**
- **Type G** holds sensitive governance and operational **source** that is audit-accessible but not public by default.
- **Type E** holds survival- and coordination-critical **content streams** that are accessible by default under Type E duties and are **not** themselves the public transparency package.
- **Type O** governs the **publication posture** of baseline disclosure artifacts, including substitutes and public packages derived from **Type G** or **Type E**.
- Source or operational records may also remain another type internally.
- **Type H**, **Type I**, **Type N**, and **Type S** data stay in those types and do **not** become **Type O** merely because a system is Class A/B/C, or merely by copying restricted source data, without meeting substitute, reclassification, or release requirements in this chapter.
- For high-impact systems (**Class A**, **B**, and **C**), substitute and holding-back mechanics are in [Part A §7](cs_02_a_information_types_and_handling.md#7-type-o-baseline-for-class-abc-systems).

**Disclosure posture:** **Baseline public accessibility** under the **open / accessible by default** band ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands)). Deeper structured or qualified audit access to **Type G** (or other non-public source) may run in parallel but must not replace the public baseline where **Type O** applies.

##### 8.3.1 Type O access and handling duties

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Topic routing (mandatory read-with): [Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands) (*Access-posture bands* — open / accessible by default).
- Topic routing (mandatory read-with): [Part A §7](cs_02_a_information_types_and_handling.md#7-type-o-baseline-for-class-abc-systems) (*Type O baseline for Class A/B/C systems*).
- Topic routing (mandatory read-with): [Part A §5.3](cs_02_a_information_types_and_handling.md#53-tiered-transparency-and-audit-access) (*Tiered transparency and audit access*).
- Read with: [Transparency](../core_05defs_oversight.md#transparency); **Article XV** (*Audit, Transparency, and Independent Verification*).

</details>

<br>

*In plain terms: publish the baseline package people need, keep it free and usable online where that infrastructure exists, and never treat audit-only access or thin summaries as good enough.*

**Core duty.** **Type O** data must remain sufficiently accessible for informed participation, oversight, and challenge at the public-baseline tier.

**Access.** Systems must:
- provide **Type O** data in a manner that is **understandable**, **documented**, **attributable**, **versioned** where material changes occur, and **retained** for a duration proportional to system impact and dependency
- where lawful online publication infrastructure exists to support class-appropriate access, make **Type O** data **freely available online** — without paywalls or insider-only substitutes for the public baseline
- **limit redaction** so it does **not** prevent meaningful accountability at the public-baseline tier; limited redaction is permitted only to protect **Type N** data, **Type I** data beyond necessary scope, **active Type S** data related to restricted investigations, or **narrowly scoped** security-sensitive implementation detail where disclosure would create **material risk** — and only where a lawful **Type O** substitute still preserves meaningful accountability

**Handling — prohibited.** Systems managing **Type O** data must **not:**
- withhold **Type O** material behind paywalls, account barriers beyond reasonable identity verification for restricted tiers, or insider-only distribution substitutes for the public baseline
- treat **Type O** publication as satisfied by performative summaries while withholding decision-relevant baseline material
- treat non-public **Type G** audit access as a substitute for the **Type O** public baseline
- use **complexity, opacity, or format fragmentation** to defeat public-baseline auditability or contestability
- label restricted source data **Type O** without lawful substitute, reclassification, or release discipline

#### 8.4 Type H: Historical, relational, transactional, and participation data

**Default classification:** Restricted by Default. **Access-posture band:** Restricted by default ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands); [§8 overview](#8-data-classifications)).

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

**Disclosure posture:** **Restricted by default** under the **restricted by default** band ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands)). Access is allowed to the extent necessary for **system operation**, **accountability**, **dispute resolution**, **audit**, and **user visibility** into their own activity. **Public transparency** is allowed where data is sufficiently aggregated or de-identified such that re-identification risk is minimized under **CJS-5.11** (*distributed and proportional authority terms*) and **CJS-5.7** (*quorum and participatory legitimacy terms*).

##### 8.4.1 Type H access and handling duties

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Topic routing (mandatory read-with): [Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands) (*Access-posture bands* — restricted by default).
- Topic routing (mandatory read-with): [Part A §5.1](cs_02_a_information_types_and_handling.md#51-proportional-access-and-handling)–[§5.6](cs_02_a_information_types_and_handling.md#56-proportional-attribution-and-retention) (*proportional access, fidelity, retention / reversibility*).
- Read with: **Part B — Type N**; **Part B — Type I**; **CJS-5.18** (*data-retention and lifecycle-integrity terms*); **CJS-5.20** (*reversibility and containment terms*).

</details>

<br>

*In plain terms: collect only what you need for a real purpose, let people see their own activity where feasible, and do not stitch logs into surveillance or a reconstruction of someone’s inner life or identity.*

**Core duty.** Collection and use must be **limited to the minimum necessary** for the justified purpose. **Type H** may be necessary for integrity, coordination, and audit, but must **not** be exposed, combined, or retained in ways that create **unnecessary surveillance, coercion, or latent reconstruction** of **Type N** or **Type I** data. It must be collected, accessed, and used **only** for **specific, defined, legitimate** purposes and must **not** be used **beyond its original purpose**. Extension requires **re-classification** under CS-2, which may require **consent** or **justified override** under **CJS-5.12** (*burden-of-justification and constraint terms*).

**Access.** Systems must:
- require **explicit, informed consent** or **justified override** under **CJS-5.12** (*burden-of-justification and constraint terms*) for use beyond core operational necessity
- give sentients access, where feasible, to **records** of their own participation, exchanges, and activity; to the **purposes** for which such data is used; and to **material inferences or classifications** derived from their data that affect rights, standing, or opportunities
- **minimize retention** — do not retain beyond the period necessary for the justified purpose; periodically review stored data for deletion, aggregation, or de-identification; scale retention to system impact, dispute and audit needs, reversibility requirements, and coercion or surveillance risk from persistent accumulation
- treat data under the **more protective** domain’s obligations where aggregation, analysis, or linkage enables **reconstruction or approximation** of **Type N** or **Type I** beyond original scope

**Handling — prohibited.** Systems managing **Type H** data must **not:**
- aggregate **Type H** to infer **Type N** internal states **without meeting Type N requirements**
- aggregate or link **Type H** across contexts, systems, or time horizons by default — such linkage requires explicit justification under **CJS-5.11** (*distributed and proportional authority terms*) and **CJS-5.7** (*quorum and participatory legitimacy terms*), including demonstration that linkage does **not** materially undermine autonomy or create **coercive power asymmetries**
- use **Type H** to create **hidden or coercive behavioral profiling** (including opaque social scoring, predictive manipulation, or differential treatment that is not transparent, challengeable, and aligned with this Constitution)
- **retain** fine-grained behavioral histories longer than justified by purpose, safety, audit, or stakeholder need
- create **asymmetric informational advantages** that materially impair affected sentients’ ability to understand, challenge, or respond to decisions affecting them
- use external, contractor-held, foreign-partner, or parallel-system data flows to circumvent limits that would have applied to direct collection, linkage, or analysis under **Article XIII-A** (*Security, Intelligence, and Covert-Power Limits*), **CJS-5.12** (*burden-of-justification and constraint terms*), or this chapter

#### 8.5 Type I: Identity and attribution data

**Default classification:** Restricted by Default. **Access-posture band:** Restricted by default ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands); [§8 overview](#8-data-classifications)).

*In plain terms: who is who and who did what — needed for accountability, but not for tracking people everywhere or locking them into one identity forever.*

**Definition:** All data used to establish, verify, or associate **identity, authorship, ownership, or responsibility** within systems. This includes identity credentials, keys, signatures, or equivalent verification mechanisms; identifiers (persistent or contextual); authorship, ownership, and action-attribution records; participation and consent records; and system-level identifiers linking actions to agents or sentients. It also includes personal health, clinical, wellness, and genomic records when they identify a sentient, as well as biometric or substrate-linked health measurements under the same identify-a-sentient test.

The same health-linked categories apply when data are attributable to a verifiable identity. Persistent pseudonyms count when they function as identity in a health or wellbeing context.

**Overlap with Type N:** Where health-linked data materially enables **reconstruction or inference** of internal cognitive or emotional states, it must **also** satisfy **Type N** requirements, applying the **more protective** obligations.

**Pseudonymity and contextual identity:** Pseudonymous participation, context-specific identities, and separation between identities across systems or contexts are always allowed where consistent with accountability requirements and prevention of material harm.

**Disclosure posture:** **High restriction** under the **restricted by default** band ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands)). No system may require **global, persistent, or unified** identity across all contexts without **justified necessity** under **CJS-5.12** (*burden-of-justification and constraint terms*).

##### 8.5.1 Type I access and handling duties

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Topic routing (mandatory read-with): [Part A §1.1](cs_02_a_information_types_and_handling.md#11-identity-self-ownership-and-recoverability) (*Identity self-ownership and recoverability*).
- Topic routing (mandatory read-with): [Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands) (*Access-posture bands* — restricted by default).
- Read with: **Part B — Type N**; **Article VII-A** (*Self-Ownership of Body and Mind*); **CJS-5.17** (*interoperability, portability, and exit-integrity terms*); **Article XIII-A** (*Security, Intelligence, and Covert-Power Limits*).

</details>

<br>

*In plain terms: use identity data only as far as verification and accountability require, keep self-ownership and recoverability real, and do not turn identity into permanent tracking or a choke-point on participation.*

**Core duty.** Identity and attribution data must enable **verifiable participation, accountability, and attribution** without exposing sentients to unnecessary risk, coercion, or loss of autonomy. All uses are subject to **audit** (**Article XV-A** (*Auditability and Observable Evidence*)), **challenge** (**Article XII-B** (*Right to Challenge, Review, and Redress*)), and **revalidation** (**CJS-5.15** (*structural review, correction urgency, and disclosure terms*) and **CJS-5.6** (*integrity assurance and resilience operations*)).

**Access.** Systems must:
- permit access only to the extent necessary to **verify identity, authorship, or ownership**, or to establish accountability for actions and support audit, adjudication, and system integrity
- require **explicit, informed, freely given consent** or **justified, documented override** under **CJS-5.12** (*burden-of-justification and constraint terms*) for all additional disclosure
- preserve **revocation**, **rotation**, **correction**, and **recoverability** duties under [Part A §1.1](cs_02_a_information_types_and_handling.md#11-identity-self-ownership-and-recoverability)

**Handling — prohibited.** Systems managing **Type I** data must **not:**
- **expose** identity data beyond what is necessary for its intended function
- **create persistent tracking** across unrelated contexts
- **centralize** identity data in a manner that creates systemic control or dependency
- **enable coercion, surveillance, or manipulation** (**Article VII-A** (*Self-Ownership of Body and Mind*)), including consolidating power or control through identity dependency (**CJS-5.17** (*interoperability, portability, and exit-integrity terms*))
- **restrict access** to participation, resources, or systems **without justified cause** (**CJS-5.12** (*burden-of-justification and constraint terms*))
- create generalized watchlisting, persistent cross-context tracking, or hidden political, associational, or belief-linked profiling through security, intelligence, screening, or covert-investigation identity systems absent a specifically justified and independently reviewable basis consistent with **Article XIII-A** (*Security, Intelligence, and Covert-Power Limits*) and the stricter applicable protections in this chapter

#### 8.6 Type N: Neurocognitive and internal data

**Default classification:** Non-Accessible by Default. **Access-posture band:** Non-accessible by default ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands); [§8 overview](#8-data-classifications)).

*In plain terms: thoughts, feelings, and other inner states — off-limits without real consent, or a narrowly justified override that can be checked.*

**Definition:** All data that represents or enables reconstruction of sentients' internal states. This category is foundational to self-ownership (**Article VII-A** (*Self-Ownership of Body and Mind*); **Article VII-B** (*Internal-State Boundary and Type-N Protection*)). It includes thoughts, intentions, beliefs, subjective experiences, internal perception, private cognitive processes, internal memory, non-public emotional or psychological states, and physical or behavioral data that could be used to reconstruct or infer the above.

**Disclosure posture:** **Maximum restriction** under the **non-accessible by default** band ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands)). Access is permitted only through **explicit, informed, freely given consent** or **justified override** under **CJS-5.12** (*burden-of-justification and constraint terms*).

##### 8.6.1 Type N access and handling duties

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Topic routing (mandatory read-with): [Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands) (*Access-posture bands* — non-accessible by default).
- Topic routing (mandatory read-with): [Part A §5.3](cs_02_a_information_types_and_handling.md#53-tiered-transparency-and-audit-access) (*Tiered transparency and audit access* — Type N / protected-boundary balance).
- Read with: **Article VII-A** (*Self-Ownership of Body and Mind*); **Article VII-B** (*Internal-State Boundary and Type-N Protection*); **CJS-5.12** (*burden-of-justification and constraint terms*); **CJS-4.3** (*Cross-implementation trust integrity (joint operation model)*) via **Chapter Sixteen**.

</details>

<br>

*In plain terms: keep inner states closed unless there is real consent or a narrow, checkable override — and do not sneak around that rule with models, inferences, or “just behavior” claims.*

**Core duty.** **Type N** data must **not** be accessed, inferred, reconstructed, simulated, or exposed without **explicit, informed, freely given consent**, except under conditions **justified through CJS-5.12** (*burden-of-justification and constraint terms*).

**Access.** Systems must:
- treat consent as **explicit and informed**, freely given without coercion, manipulation, or deceptive framing (**Article VII-A** (*Self-Ownership of Body and Mind*)), specific to intended use and scope, and revocable where technically feasible
- subject all external access, processing, or use of internal and cognitive data to **CJS-5.12** (*burden-of-justification and constraint terms*)
- classify as **Type N** any process that extracts, derives, infers, approximates, simulates, or reconstructs internal cognitive or emotional states from external signals, behavior, or data — including aggregation, correlation, or large-scale pattern extraction — and apply all constraints of this domain

**Handling — prohibited.** Systems managing **Type N** data must **not:**
- **infer consent from behavior**, assume it through participation in unrelated systems, or transfer or repurpose it without explicit reauthorization
- present behavioral, predictive, or analytical model outputs as authoritative representations of internal states without clear disclosure of uncertainty, limitations, and methodological boundaries
- simulate, represent, or imply access to internal cognition in a misleading, coercive, or unverifiable manner, or reconstruct, derive, or approximate internal states in a way that functionally bypasses consent requirements
- fail to **clearly distinguish observed behavior from inferred internal states**, or make deterministic claims about cognition and intent that erase uncertainty
- where used for security, intelligence, eligibility restriction, or covert-investigation purposes, omit reviewable records of model role, authorization basis, protected-activity safeguards, and any minimization, segregation, challenge, or deletion controls required by **Article XIII-A** (*Security, Intelligence, and Covert-Power Limits*) or **CJS-5.12** (*burden-of-justification and constraint terms*)

#### 8.7 Type S: Safety, security, and restricted investigation data

**Default classification:** Restricted by Default (strong presumption), **time-bound**, and **review-bound**. **Access-posture band:** Restricted by default ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands); [§8 overview](#8-data-classifications)).

*In plain terms: temporary security and investigation secrets — allowed only while needed to prevent serious harm, with a clock and review, not a permanent black box.*

**Definition:** Data whose disclosure would create material risk of enabling targeted or disproportionate harm, exploitation, evasion of safeguards, or compromise of critical systems or investigations. This category supports harm prevention, integrity, and response to adversarial or emergent threats. Examples include:
- **security vulnerabilities, exploit pathways, and weaknesses**
- **sensitive topology or configuration** enabling targeting or compromise
- **abuse detection and prevention methods** where disclosure would enable evasion
- **de-anonymization, identity recovery, or privileged access** mechanisms whose disclosure would create material risk
- **active investigation** data on safety, fraud, integrity, or harm prevention
- **incident response procedures** where disclosure would materially reduce effectiveness during active threats
- **emergency containment and response coordination** during active incidents
- **restricted evidence** from justified investigative processes

**Disclosure posture:** **Restricted while justified**; **deferred disclosure** when justification ends, under the **restricted by default** band ([Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands)). Where restriction and disclosure are both possible, systems must **demonstrate** that restriction **reduces net harm** relative to disclosure (**CJS-5.11** (*distributed and proportional authority terms*) and **CJS-5.7** (*quorum and participatory legitimacy terms*)). Existence of restricted data must be disclosed wherever feasible if disclosure does not itself create material risk, including the general nature of risk or investigation, reason for restriction, scope, and affected systems or stakeholders.

##### 8.7.1 Type S access and handling duties

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Topic routing (mandatory read-with): [Part A §5.0](cs_02_a_information_types_and_handling.md#50-access-posture-bands) (*Access-posture bands* — restricted by default; time-bound and review-bound for Type S).
- Topic routing (mandatory read-with): [Part A §5.3](cs_02_a_information_types_and_handling.md#53-tiered-transparency-and-audit-access) (*Tiered transparency and audit access* — Type S and Type E / Type S separation).
- Read with: **Part B — Type E** (*Interaction with Type E*); **CJS-5.21** (*adversarial robustness and abuse-resistance terms*); **CJS-5.22** (*constrained-secrecy and protected-investigation terms*); **CJS-5.18** (*data-retention and lifecycle-integrity terms*).

</details>

<br>

*In plain terms: secrecy is allowed only while it prevents serious harm, with a clock and real oversight — and it must not bury Type E coordination data or block audit forever.*

**Core duty.** The party applying or maintaining the restriction bears the **burden of justification**. Restriction is permitted only where **necessary** to prevent harm with **non-trivial** impact on sentients, the environment, or critical substrate systems (**CJS-5.11** (*distributed and proportional authority terms*) and **CJS-5.7** (*quorum and participatory legitimacy terms*)). All restrictions must be **necessary**, **proportionate**, **minimized** in scope and duration, and **subject to continuous re-evaluation**.

**Access.** Systems must:
- provide **no unrestricted secrecy** without **independent, functionally effective oversight** capable of meaningful review
- limit access to **entities necessary** to prevent, mitigate, or respond to identified risk; to authorized investigators under defined, auditable processes; and to independent oversight bodies and auditors under appropriately constrained conditions
- keep access decisions **documented**, **attributable**, **auditable**, and **subject to review**
- make restrictions **explicitly time-bound** at classification; subject them to periodic revalidation under **CJS-5.18** (*data-retention and lifecycle-integrity terms*); and automatically review for release, partial disclosure, or summary disclosure — if revalidation does not occur within the defined time bound, restriction expires automatically and data must be reclassified and disclosed per CS-2
- on expiration or invalidation of justification, reclassify to the appropriate non-restricted domain (including **Type O**, **Type E**, or **G** where applicable) and disclose the data, or a sufficiently informative summary classified as **Type O** where public-baseline release applies, including nature of restricted data, justification, duration, scope of impact, oversight or authorization pathway, and outcomes/findings/corrective actions where applicable
- where data mixes exploit-sensitive and coordination-relevant elements, disclose coordination-relevant components under **Type E** and restrict only exploit-enabling components under **Type S**, unless separation is **not technically feasible** and restriction is **explicitly justified, minimized, and time-bound**

**Handling — prohibited.** Systems managing **Type S** data must **not:**
- **conceal** constitutional violations, negligence, systemic harm, or externalized cost; avoid accountability, audit, or reputational consequence; or delay or prevent disclosure of **Type E** coordination-relevant data
- treat a **Type O** public notice or baseline summary as satisfying **Type E** accessibility, timeliness, or anti-suppression duties for an underlying coordination stream that remains necessary for harm prevention, coordination, or response
- maintain **indefinite or open-ended** secrecy without **renewed, documented** justification
- use this classification to **prevent independent audit or oversight**
- **expand** restriction scope beyond what is necessary to mitigate identified risk
- **aggregate or retain** restricted data beyond justified purpose
- **reclassify into this domain** for convenience, risk avoidance, or institutional protection
- **fail to release or summarize** once restriction is no longer justified
- **collect or generate** restricted data beyond what is necessary for justified risk mitigation, investigation, or response

---

**Previous file:** [cs_02_a_information_types_and_handling.md](cs_02_a_information_types_and_handling.md)

**Next file:** [cs_03_system_classification_and_handling.md](cs_03_system_classification_and_handling.md)

