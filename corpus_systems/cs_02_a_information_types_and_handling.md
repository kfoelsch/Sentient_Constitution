<a id="cs-2-part-a-information-types-and-handling"></a>
## CS-2, Part A: Information types and handling

<details>
<summary><strong><span style="color: #2563eb;">Corpus placement (non-operative): file structure and reading rules</span></strong></summary>

> The following content is **reader guidance only**. It does not add, remove, or narrow binding obligations elsewhere in this file or in other CS-2 parts.
>
> This file contains **CS-2, Part A** — purpose and scope (including identity self-ownership and continuity-critical export), classification determination, anti-circumvention, cross-domain governance principles, and data separation / attribution (**§§1–7**). **Part B** — data classifications (**Type C** through **Type S**, including **Type O**) — is in [`cs_02_b_data_classifications.md`](cs_02_b_data_classifications.md).

</details>

<br>

**CS-2, Part A**, owns **information-type determination, foundational identity and continuity controls, cross-domain governance, and separation / attribution**. Canonical type definitions and per-type handling rules are in **[Part B](cs_02_b_data_classifications.md#cs-2-part-b-data-classifications)**.

*In plain terms: Part A says how to type data, keep those types honest across systems, and protect separation, attribution, and exit — Part B names the types themselves.*

<br>

**Introductory provisions:**

*In plain terms: tell the truth in public where you can, but keep safeguards that protect people, privacy, trust, and system integrity — and make those safeguards stronger when impact is higher.*

Systems must preserve the practical ability to publish truthful information while maintaining safeguards for harm prevention, privacy, trust, and system integrity.

Requirements and limitations scale proportionally with system classification and potential impact. They must impose proportionate safeguards on publication within their boundaries where necessary to preserve trust, safety, and constitutional compliance.

<a id="1-purpose-and-scope"></a>
### 1. Purpose and scope

*In plain terms: Chapter Six rights need trustworthy data handling; CS-2 is the systems rulebook that makes typing, access defaults, integrity, identity self-ownership, and Class A/B/C continuity real.*

**Sentient Constitution Chapter Six** (Articles **I**–**XXV**; presentation **Parts A–D**) states Foundational Rights that depend on strong, reproducible data handling — including info-sphere, audit, and comprehensibility duties (e.g., **Articles XIV**, **XV**, and **XX**). CS-2 is the systems-layer implementation of those duties.

CS-2 implements:

- **Data typing** — every material dataset is assigned one or more types defined in **[Part B](cs_02_b_data_classifications.md#cs-2-part-b-data-classifications)** (**Type C**, **G**, **O**, **H**, **I**, **N**, and **S**)
- **Default access posture** — each type carries a clear public, restricted, or non-accessible default, plus disclosure, consent, and handling rules
- **Most-restrictive rule** — where more than one type applies, the strongest applicable protections govern ([§2](#2-determination-of-classification) *When it is unclear*), subject to proportionality (**CJS-5.11** (*distributed and proportional authority terms*) and **CJS-5.7** (*quorum and participatory legitimacy terms*))
- **Classification integrity** — type follows the **functional nature of the data** and the **effects it enables**, not format, origin, or pipeline stage; systems may not evade typing by fragmentation, re-labeling, or indirection ([§2](#2-determination-of-classification)–[§4](#4-anti-circumvention-and-integrity-of-classification))
- **Identity self-ownership** — identity and attribution data remain under sentient control through revocation, rotation, correction, and recoverability ([§1.1](#11-identity-self-ownership-and-recoverability); **Article VII** (*Self-Ownership*))
- **Continuity and exit** — for **Class A**, **Class B**, and **Class C** systems, people must be able to take their continuity-critical data with them when a service ends or changes hands ([§1.2](#12-continuity-critical-collection-and-exportability); **Article II-E** (*Info-Sphere Dependency, Continuity, and Operator Non-Viability*)), and the formats and interfaces used for that handoff must meet **CJS-5.17** (*interoperability, portability, and exit-integrity terms*)
- **Cross-domain governance** — proportional access, reclassification and lifecycle, tiered transparency and audit, transformation traceability, attribution, and retention ([§5](#5-cross-domain-governance-principles)); typing integrity and anti-evasion remain in [§2](#2-determination-of-classification)–[§4](#4-anti-circumvention-and-integrity-of-classification)
- **Separation and attribution** — keep higher-sensitivity domains from leaking through linkage or inference, and preserve attributable action ([§6](#6-data-separation-and-attribution))
- **Class scaling** — higher-impact systems get stricter data rules. How strict depends on the system's class under **CS-3 — System classification and handling**
- **Type O public-baseline (Class A/B/C)** — for high-impact systems, the **Type O** public baseline defined in **[Part B — Type O](cs_02_b_data_classifications.md#type-o-open-public-baseline-disclosure-data)** must be released by default, with substitute and holding-back limits in [§7](#7-type-o-baseline-for-class-abc-systems)

<a id="11-identity-self-ownership-and-recoverability"></a>

**1.1. Identity self-ownership and recoverability.**

*In plain terms: your identity data is yours to control — systems must let you revoke, replace, and correct credentials, and must not trap you forever in a broken or compromised identity.*

This subsection is foundational to how typed data is handled under CS-2 and to self-ownership of identity and attribution data under **Article VII** (*Self-Ownership*), including **Article VII-A** (*Self-Ownership of Body and Mind*).

**Identity and Attribution Data** must support:
- **revocation of credentials**
- **rotation or replacement** of identifiers
- **correction** of inaccurate, incomplete, or compromised data

Systems must **not**:
- **permanently bind** sentients to compromised or outdated identities
- **prevent recovery** from identity-related harm
- **create irreversible identity linkage** that undermines autonomy, safety, or wellbeing

Identity systems must preserve **continuity** where desired, **separation** where required, and **recoverability** in cases of compromise or error.

<a id="12-continuity-critical-collection-and-exportability"></a>

**1.2. Continuity-critical collection and exportability.**

*In plain terms: for Class A/B/C systems, do not lock people's continuity-critical data in a form they cannot take with them when the service ends or changes hands — and disclose any lawful limits up front.*

This subsection is foundational to continuity and exit under CS-2. It implements:
- **Article II-E** (*Info-Sphere Dependency, Continuity, and Operator Non-Viability*)
- **Article XIX-A** (*Portability Rights*)
- **CJS-5.17** (*interoperability, portability, and exit-integrity terms*)

For **Class A**, **Class B**, and **Class C** systems, operators must **not** collect or retain continuity-critical sentient data in forms that cannot be exported, migrated, or transferred under disclosed continuity and export paths, except where **Necessity** requires:
- confidentiality
- security
- **Type N** or comparable protected-boundary constraints
- lawful non-disclosure

Where export is limited, operators must disclose before a materially binding commitment:
- the **limitation**
- its **scope**
- any lawful **substitute export path**

Shutdown, migration, operator exit, and service-end paths must:
- preserve usable **export or handoff** of continuity-critical data under those disclosed paths
- **not** rely on a discretionary promise to try later


<a id="2-determination-of-classification"></a>
### 2. Determination of classification

*In plain terms: type data by what it does and enables — not by format or pipeline stage. When unsure, protect more; weaken protection only with a documented justification; and do not dodge typing by rearranging the same outcome.*

**What counts.** Type the data by **what it is for** and **what it lets someone do** — not by file format, where it came from, or which step of a pipeline it sits in. The same rule applies when retyping data later.

<a id="most-restrictive-applicable-classification-governs"></a>
**When it is unclear.** If more than one type could fit, the **most protective** applicable protections govern. Use the most protective type that still fits, scaled to impact under:
- **CJS-5.11** (*distributed and proportional authority terms*)
- **CJS-5.7** (*quorum and participatory legitimacy terms*)

Weaker protection is allowed only with a **justified, documented override** under **CJS-5.12** (*burden-of-justification and constraint terms*). Systems must **not** selectively apply less restrictive classifications to enable access, processing, or disclosure that would otherwise be prohibited.

If pieces of data can be rebuilt, transformed, or combined into something more sensitive, treat them under that **more sensitive** type.

**Same outcome, same type.** If two arrangements work the same way in practice, they get the same classification. Typing decisions and material changes must stay:
- **transparent** (**CJS-5.10** (*disclosure sufficiency and observability terms*))
- **auditable** (**CJS-5.3** (*auditability and reconstructability terms*))
- **open to challenge** (**CJS-5.13** (*procedural integrity and adjudication terms*))

**Wrong typing is a violation.** Mislabeling data, arranging it to dodge the rules, or achieving the same harmful access through a different structure violates:
- **informational integrity** (**Article XIV** (*Info-Sphere Integrity*))
- auditability where evidence is implicated (**Article XV-A** (*Auditability and Observable Evidence*))
- applicable rights under **Chapter Six, Articles V through IX**

<a id="3-temporal-systemic-and-dependency-scope-of-rights"></a>
### 3. Temporal, systemic, and dependency scope of rights

*In plain terms: protections cover delayed, stacked, and indirect harm too — including harm passed through other systems. You cannot push risk onto other people, times, or systems to dodge the rules.*

Data-handling protections under CS-2 — Information types and handling apply not only to immediate and direct system effects. They also apply to delayed, cumulative, and indirect impacts arising through system interactions and dependency chains.

Where systems create or contribute to material risk to sentients, including through transitive dependencies, those risks fall within the scope of these protections. Systems must **not** externalize risk or harm across time, populations, or system boundaries. That prohibition includes layered or indirect dependencies. Those dependencies must not bypass, defer, or dilute the protections and constraints established in Sentient Constitution Chapters One through Six.

<a id="4-anti-circumvention-and-integrity-of-classification"></a>
### 4. Anti-circumvention and integrity of classification

*In plain terms: you may not break, relabel, split, outsource, or pipeline data just to escape its type — and you may not use typing itself to block participation, hide risk, or shut down audit. Keep the strongest applicable protections, and document any de-anonymization.*

Data classification under CS-2 — Information types and handling is binding across all systems, processes, and transformations. **No system may:**
- **shift** data between classifications without maintaining the protections required by the **most restrictive applicable** classification
- **fragment, transform, aggregate, or re-label** data to avoid classification while preserving equivalent functional access or effect
- **structure** data pipelines, processing stages, or system boundaries to bypass applicable classification requirements
- **distribute** processing across multiple systems, stages, agents, or time-separated operations to achieve outcomes that would be prohibited if performed within a single system
- **rely** on intermediate systems, agents, or third parties to perform actions that would be prohibited if performed directly
- **de-anonymize** anonymized data except under **CJS-5.12** (*burden-of-justification and constraint terms*), with such actions **fully documented and auditable**
- **use** classification to **evade** constitutional requirements, **justify unnecessary** restriction of participation or access, **conceal** systemic risk or harm, or **create artificial barriers** to audit, verification, or accountability

<a id="5-cross-domain-governance-principles"></a>
### 5. Cross-domain governance principles

*In plain terms: these are the shared rules for how typed data is accessed, transformed, retyped, attributed, and retained across systems — stricter where impact is higher. Typing integrity and anti-evasion live in [§2](#2-determination-of-classification)–[§4](#4-anti-circumvention-and-integrity-of-classification).*

All data, regardless of classification, must be handled in accordance with the following cross-domain principles. These principles govern how classifications are applied, enforced, and interacted with across systems, and ensure alignment with **Chapter Six, Articles V through IX** and **CJS-5** (*Implementation and cross-implementation operational cluster library*) operational clusters in **corpus_joint_structure.md**.

<a id="51-proportional-access-and-handling"></a>

**5.1. Proportional access and handling.**

*In plain terms: bigger impact means stricter access, more transparency, deeper audit, and stronger justification — you cannot claim light rules while causing heavy outside effects.*

Access and handling must scale with:
- **impact on sentients, the environment, and the info-sphere**
- stakeholder dependency
- potential for harm, including irreversibility

Higher-impact systems and actions require:
- **greater transparency** (**CJS-5.10** (*disclosure sufficiency and observability terms*))
- **deeper auditability** (**CJS-5.3** (*auditability and reconstructability terms*))
- **stronger justification** for restriction or access (**CJS-5.12** (*burden-of-justification and constraint terms*))

**No** system may claim reduced requirements while exerting **material external** effects under:
- **CJS-5.11** (*distributed and proportional authority terms*)
- **CJS-5.7** (*quorum and participatory legitimacy terms*)

<a id="52-reclassification-and-lifecycle-governance"></a>

**5.2. Reclassification and lifecycle governance.**

*In plain terms: types are not forever — recheck them when impact, use, or risk changes, keep the strongest protections unless justified, and do not hide behind an outdated label.*

Classification is **not** static. **Material** changes in any of the following must trigger reclassification:
- **system impact**
- **uses or contexts**
- **risks or capabilities**

All data must be:
- **periodically re-evaluated** for appropriate classification (**CJS-5.18** (*data-retention and lifecycle-integrity terms*)) — verified on each materially impactful system alignment certification or revalidation cycle under **[Chapter Seven §4](../core_07_a_system_alignment_certification_evaluation.md#4-data-types-and-handling-evaluation)** (*Data Types and Handling Evaluation*) and recorded under **[Chapter Seven Part B §11.1](../core_07_b_system_alignment_certification_record_process.md#111-minimum-record-contents)**
- **reclassified** whenever necessary to maintain alignment with constitutional requirements
- **stored** in alignment with its classification, including **duration limits** proportional to purpose, risk, and stakeholder impact

Reclassification must:
- **preserve the highest applicable protections** unless reduced through **justified override** (**CJS-5.12** (*burden-of-justification and constraint terms*))
- remain **transparent and documented**
- stay **subject to audit and challenge**

**No** system may:
- **rely on outdated classification** to justify continued access or reduced protection
- **delay or avoid reclassification** where material changes in impact or use have occurred

<a id="53-tiered-transparency-and-audit-access"></a>

**5.3. Tiered transparency and audit access.**

*In plain terms: people need enough visibility to understand risk; auditors need deeper access when needed; and hiding system behavior behind access controls is not allowed.*

Data access must satisfy **CJS-5.4** (*tiered transparency and audit-access terms*) for balancing transparency, auditability, and protected-boundary constraints.

It must also balance protection of internal states and sensitive data (**Sentient Constitution Chapter Six, **Article VII-B** (*Internal-State Boundary and Type-N Protection*)**; Types **H**, **I**, **N**, and **S** in this chapter). Where applicable based on system impact (**CJS-5.11** (*distributed and proportional authority terms*) and **CJS-5.7** (*quorum and participatory legitimacy terms*)), systems must support:

- **Identity Data Protection.** [Identity Data Protection](core_05defs_continuity.md#identity-data-protection) governs the restricted-linkages ban (Type H/I → Type N) in this subsection. See [§6.1](#61-separation-of-data-domains) for the domain-separation mechanics.
- **baseline accessibility** — sufficient visibility into behavior and effects for informed participation and risk evaluation
- **qualified audit access** — structured pathways for independent auditors to deeper data where verification requires it
- **forensic access** — full reconstruction in cases of harm, dispute, or credible risk, consistent with **CJS-5.11**, **CJS-5.7**, and **CJS-5.12** (*burden-of-justification and constraint terms*)
- **access-control integrity** — access controls must **not** conceal systemic behavior, prevent accountability, or obstruct legitimate audit and verification

For **Class A**, **Class B**, and **Class C** systems, the **Type O** public baseline defined in **[Part B — Type O](cs_02_b_data_classifications.md#type-o-open-public-baseline-disclosure-data)** is **public by default**, subject to the substitute and holding-back rules in [§7](#7-type-o-baseline-for-class-abc-systems).

Any limit on who may see or use data must be:
- **narrow in scope** — only as broad as needed for the stated lawful purpose
- **justified** — with reasons that can be checked
- **auditable**
- **open to challenge** (**CJS-5.13** (*procedural integrity and adjudication terms*))

<a id="54-integrity-of-data-handling-and-transformation"></a>

**5.4. Integrity of data handling and transformation.**

*In plain terms: keep a usable trail of where data came from and what changed, so impact and dependencies can still be checked and material transformations can be reconstructed.*

All material handling, processing, and transformation must preserve:

- **traceability of origin and transformations**
- **the ability to evaluate impact and dependencies** (**CJS-5.16** (*dependency integrity and disclosure terms*))
- **transparency, auditability, and reconstructability** where required (**CJS-5.10** (*disclosure sufficiency and observability terms*); **CJS-5.3** (*auditability and reconstructability terms*))

If a material transform changes what the data enables, how it can be used, or its sensitivity — including by rebuild, combination, or aggregation — the resulting data must be **re-evaluated and retyped** under [§2](#2-determination-of-classification) and [§5.2](#52-reclassification-and-lifecycle-governance), and that type change must remain on the same transparent, auditable trail.

Anti-degradation and anti-obscurity duties for classification integrity are stated in [§2](#2-determination-of-classification)–[§4](#4-anti-circumvention-and-integrity-of-classification).

<a id="55-accountability-and-attribution-in-data-use"></a>

**5.5. Accountability and attribution in data use.**

*In plain terms: someone identifiable must be responsible for material data actions — handing the work off does not erase accountability.*

This subsection governs attribution of data access, processing, and transformation.

- Delegation of data handling does **not** eliminate accountability
- Responsibility must remain assignable through transparent, auditable processes
- Attribution must resist **tampering, repudiation, or ambiguity**

All data access, processing, and transformation must be:
- **attributable** to identifiable systems, agents, or sentients (**Chapter Six, **Article VII** (*Self-Ownership*)** — self-ownership and attributable representation where applicable)
- **recorded** in a manner sufficient for audit and reconstruction (**CJS-5.3** (*auditability and reconstructability terms*))

Systems must ensure:
- **clear responsibility** for actions taken on data
- **traceability** of decisions and outcomes

<a id="56-proportional-attribution-and-retention"></a>

**5.6. Proportional attribution and retention.**

*In plain terms: you do not need forever-logs for everything, but you must keep enough attribution to investigate serious harm, dispute, or abuse.*

Attribution requirements do **not** imply universal or persistent logging of all actions.

Systems must provide attribution capability **proportional to system impact** sufficient to support [Attributable Action](core_05defs_accountability.md#attributable-action-constitutional) and [Attribution Integrity](core_05defs_accountability.md#attribution-integrity-constitutional) under:
- **CJS-5.11** (*distributed and proportional authority terms*)
- **CJS-5.7** (*quorum and participatory legitimacy terms*)

That capability may include:
- **short-lived** mechanisms — attribution that exists only long enough for the immediate purpose, then expires
- **event-triggered or conditional** logging
- **limited retention windows**
- **aggregated or anonymized** records where appropriate

**Low-impact** systems are **not** required to:
- **retain full historical logs of all actions**
- **maintain persistent identity linkage** beyond what is necessary for system integrity and participant safety

Systems must **not**:
- **eliminate attribution capability** where material harm, dispute, or abuse cannot be investigated
- **design retention policies** that prevent reasonable reconstruction of significant events when required

<a id="6-data-separation-and-attribution"></a>
### 6. Data separation and attribution

*In plain terms: keep sensitive data domains from leaking into each other, and keep actions attributable. Identity self-ownership and continuity-critical export are foundational and live in [§1.1](#11-identity-self-ownership-and-recoverability)–[§1.2](#12-continuity-critical-collection-and-exportability).*

All systems must maintain clear separation between data classifications and ensure accountable attribution of actions. Identity self-ownership and continuity-critical export obligations are stated in [§1.1](#11-identity-self-ownership-and-recoverability) and [§1.2](#12-continuity-critical-collection-and-exportability).

<a id="61-separation-of-data-domains"></a>

**6.1. Separation of data domains.**

*In plain terms: do not combine or correlate datasets in ways that weaken protections or reconstruct more sensitive data — especially do not use identity data to infer inner thoughts without consent or justified override.*

Derived inferences about beliefs, intent, or cognition must be treated as **Type N** data.

Across domain boundaries, systems must preserve separation such that:
- combining, correlation, aggregation, or reconstruction does **not** reduce required protections
- combining, correlation, aggregation, or reconstruction does **not** bypass more sensitive handling requirements

General anti-circumvention and retyping rules for:
- reconstruction
- aggregation
- functional-equivalence outcomes

are governed by [§2](#2-determination-of-classification), [§4](#4-anti-circumvention-and-integrity-of-classification), and [§5.4](#54-integrity-of-data-handling-and-transformation).

**Restricted linkages** are governed by [Identity Data Protection](core_05defs_continuity.md#identity-data-protection); this subsection applies the domain-separation mechanics above.

<a id="62-constraint-on-cross-domain-linkage"></a>

**6.2. Constraint on cross-domain linkage.**

*In plain terms: links between identity and other data domains must be open, limited, and reviewable — no hidden cross-domain stitching that undercuts type protections.*

Linkage between data domains must be:
- **explicit**
- **limited to necessary scope**
- **subject to audit and challenge**

Systems must **not**:
- create **persistent or hidden** linkages between identities and other data domains without justification
- **enable cross-domain correlation** that undermines classification protections

All linkage mechanisms must remain:
- **transparent** (CJS-5.10 (*disclosure sufficiency and observability terms*))
- **auditable** (CJS-5.3 (*auditability and reconstructability terms*))
- **subject to revalidation** (CJS-5.18 (*data-retention and lifecycle-integrity terms*))

<a id="63-attribution-and-accountability-requirements"></a>

**6.3. Attribution and accountability requirements.**

*In plain terms: actions that affect people or shared systems must be traceable to someone or something responsible. If impact grows — or value, identity, or resources start moving outside the system — reduced attribution must end and full attribution must take over.*

This subsection applies [Attribution Integrity](core_05defs_accountability.md#attribution-integrity-constitutional) and [Attributable Action](core_05defs_accountability.md#attributable-action-constitutional) to system actions that affect the outside world:

- **No** system may **obscure responsibility** through indirection, delegation, or system complexity ([Attribution Integrity](core_05defs_accountability.md#attribution-integrity-constitutional))
- **No** system may **create conditions** where actions cannot be reliably attributed ([Attribution Integrity](core_05defs_accountability.md#attribution-integrity-constitutional))
- Delegation of action does **not** eliminate accountability
- Responsibility must remain traceable through transparent, auditable attribution chains

**Attributable action scope and audit-resistance.**

- All actions affecting **sentients**, **shared infrastructure**, **resource systems**, or the **info-sphere** must satisfy [Attributable Action](core_05defs_accountability.md#attributable-action-constitutional) through identifiable systems, agents, or sentients
- Attribution must satisfy [Attribution Integrity](core_05defs_accountability.md#attribution-integrity-constitutional), including **auditability (CJS-5.3 (*auditability and reconstructability terms*))** and resistance to tampering, repudiation, or ambiguity

**Transition to full attribution.** Where systems **increase in impact**, they must transition toward **full attribution**. The same applies when they:
- **introduce persistent value, identity, or resource transfer**
- **affect external systems**

**No** system may continue under **reduced attribution** once it **exceeds low-impact thresholds**. Narrow reduced-attribution permission for creative and low-risk contexts is stated in [§6.4](#64-creative-expressive-and-low-risk-attribution-exception).

<a id="64-creative-expressive-and-low-risk-attribution-exception"></a>

**6.4. Creative, expressive, and low-risk attribution exception.**

*In plain terms: low-risk creative spaces may hide who you are from other users — but only while audit-level accountability stays intact and impact stays low.*

Systems that do **not** exert **material external impact** under **CJS-5.11** (*distributed and proportional authority terms*) and **CJS-5.7** (*quorum and participatory legitimacy terms*) may permit **pseudonymous or abstracted** identity at the user-interaction level. That includes:
- reduced or intentionally obscured visibility of attribution to other participants
- **hidden roles**
- **deception mechanics**
- **identity concealment** as part of system design

**Permission** applies **only** where the system is designed primarily for **creative expression**, **entertainment**, **gaming**, **roleplay**, or **other low-risk, voluntary** environments.
It is permitted **only if** all of the following are true:
- **identity abstraction** is context-bound and does **not** produce **persistent or cross-system** attribution without **consent** or **justified override** under **CJS-5.12** (*burden-of-justification and constraint terms*)
- the system does **not** materially affect **sentient reputation external to the system**
- the system does **not** materially affect **sentient survival or foundational resources** (**Articles I–III and V**)
- the system does **not** materially affect **shared infrastructure stability**, **resource systems or external economic structures**, or **the integrity of the info-sphere**
- **system-level accountability** is preserved and all actions within the system remain attributable at an audit level consistent with:
  - [Attributable Action](core_05defs_accountability.md#attributable-action-constitutional)
  - [Attribution Integrity](core_05defs_accountability.md#attribution-integrity-constitutional)
  - system impact
  - **CJS-5.10** (*disclosure sufficiency and observability terms*)
  - **CJS-5.3** (*auditability and reconstructability terms*)
  - **CJS-5.5** (*independent verification and claim-integrity terms*)
  - **CJS-5.11** (*distributed and proportional authority terms*)
  - **CJS-5.7** (*quorum and participatory legitimacy terms*)
- participants are **not** exposed to **non-consensual** harm, coercion, or manipulation

<a id="7-type-o-baseline-for-class-abc-systems"></a>
### 7. Type O baseline for Class A/B/C systems

*In plain terms: high-impact systems must publish the Type O public baseline by default; where raw protected data cannot be released, publish the strongest feasible public substitute; and holding data back must be narrow and challengeable.*

For **Class A**, **Class B**, and **Class C** systems, the **Type O** public-baseline content defined in **[Part B — Type O](cs_02_b_data_classifications.md#type-o-open-public-baseline-disclosure-data)** is **public by default** and must be released as **Type O**, subject to the substitute and holding-back rules below.

**Substitutes for restricted source data.** If raw disclosure would harm privacy, identity, internal-state protection, safety, security, or an active restricted investigation, publish the strongest feasible **Type O** substitute instead — for example:
- aggregation
- de-identification
- summary or delayed disclosure
- qualified audit access

Keep the underlying records under their original type unless lawfully reclassified.

**Holding back.** Any limit on **Type O** baseline release must be:
- narrow
- documented
- proportionate
- auditable
- challengeable

Security or investigation limits must also be time-bound and review-bound under **Type S**. No restriction may hide:
- systemic behavior
- constitutional violations
- material risk
- dependency
- failure
- externalized cost


---

**Previous file:** [cs_01_scope_purpose_identifier_rules.md](cs_01_scope_purpose_identifier_rules.md)

**Next file:** [cs_02_b_data_classifications.md](cs_02_b_data_classifications.md)

