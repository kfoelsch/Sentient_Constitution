<a id="cs-2-part-a-information-types-and-handling"></a>
## CS-2, Part A: Information types and handling

<details>
<summary><strong><span style="color: #2563eb;">Corpus placement (non-operative): file structure and reading rules</span></strong></summary>

> The following content is **reader guidance only**. It does not add, remove, or narrow binding obligations elsewhere in this file or in other CS-2 parts.
>
> This file contains **CS-2, Part A** — purpose, scope, classification determination, anti-circumvention, cross-domain governance principles, and data separation / attribution / lifecycle integrity (**§§1–7**). **Part B** — data classifications (**Type C** through **Type S**, including **Type O**) — is in [`cs_02_b_data_classifications.md`](cs_02_b_data_classifications.md).

</details>

<br>

**CS-2, Part A**, owns **information-type determination, cross-domain governance, and lifecycle integrity**. Canonical type definitions and per-type handling rules are in **[Part B](cs_02_b_data_classifications.md#cs-2-part-b-data-classifications)**.

<br>

**Introductory provisions:** Systems must preserve the practical ability to publish truthful information while maintaining safeguards for harm prevention, privacy, trust, and system integrity.

Requirements and limitations scale proportionally with system classification and potential impact. They must impose proportionate safeguards on publication within their boundaries where necessary to preserve trust, safety, and constitutional compliance.

### 1. Purpose and scope
**Sentient Constitution Chapter Six** (Articles **I**–**XXV**; presentation **Parts A–D**) states Foundational Rights that depend on strong, reproducible data handling — including info-sphere, audit, and comprehensibility duties (e.g., **Articles XIV**, **XV**, and **XX**). CS-2 is the systems-layer implementation of those duties.

CS-2 implements:

- **Data typing** — every material dataset is assigned one or more types defined in **[Part B](cs_02_b_data_classifications.md#cs-2-part-b-data-classifications)** (**Type C**, **G**, **O**, **H**, **I**, **N**, and **S**)
- **Default access posture** — each type carries a clear public, restricted, or non-accessible default, plus disclosure, consent, and handling rules
- **Most-restrictive rule** — where more than one type applies, the strongest applicable protections govern, subject to proportionality (**CJS-5.11** (*distributed and proportional authority terms*) and **CJS-5.7** (*quorum and participatory legitimacy terms*))
- **Classification integrity** — type follows the **functional nature of the data** and the **effects it enables**, not format, origin, or pipeline stage; systems may not evade typing by fragmentation, re-labeling, or indirection ([§4](#4-determination-of-classification)–[§5](#5-anti-circumvention-and-integrity-of-classification))
- **Cross-domain governance** — proportional access, tiered transparency and audit, transformation integrity, reclassification, attribution, and retention ([§6](#6-cross-domain-governance-principles))
- **Separation and lifecycle** — keep higher-sensitivity domains from leaking through linkage or inference; preserve attributable action, identity recoverability, and continuity-critical export ([§7](#7-data-separation-attribution-and-lifecycle-integrity))
- **Class scaling** — higher-impact systems get stricter data rules. How strict depends on the system's class under **CS-3 — System classification and handling**
- **Type O public-baseline (Class A/B/C)** — for high-impact systems, decision-relevant system data must be released as **Type O** by default, with narrow exceptions for non-**Type O** protected sources ([§2](#2-type-o-public-baseline-for-class-abc--default-and-exceptions))
- **Continuity and exit** — for **Class A**, **Class B**, and **Class C** systems, people must be able to take their continuity-critical data with them when a service ends or changes hands ([§7.5](#7-data-separation-attribution-and-lifecycle-integrity); **Article II-E** (*Info-Sphere Dependency, Continuity, and Operator Non-Viability*)), and the formats and interfaces used for that handoff must meet `corpus_joint_structure.md` **CJS-5.17** (*interoperability, portability, and exit-integrity terms*)

### 2. Type O public-baseline for Class A/B/C — default and exceptions
**Default — Type O.** For **Class A**, **Class B**, and **Class C** systems, data necessary to understand system purpose, classification, dependency structure, operational status, material risks, performance, failures, governance, audit outcomes, stakeholder effects, and constitutional compliance is **public by default** and must be classified as **Type O** when released for public-baseline access.

This default applies most strongly to material drawn from **Type C** and **Type G** sources.

**Exceptions — data that stays non-Type O.** The **Type O** default does **not** reclassify **Type H**, **Type I**, **Type N**, or **Type S** data as **Type O** without lawful reclassification, aggregation, de-identification, summary disclosure, or other maximum feasible public substitute. Where privacy, internal-state protection, identity protection, safety, security, or restricted-investigation needs justify limiting raw disclosure, systems must provide the maximum feasible **Type O** public substitute, including aggregation, de-identification, summary disclosure, delayed disclosure, or qualified audit access. The source records remain under their non-**Type O** classification unless lawfully reclassified.

**Limits on restrictions.** Any restriction that withholds or delays **Type O** baseline release must be **narrowly scoped**, **documented**, **proportionate**, **auditable**, and **subject to challenge**. Security or investigation-based restrictions must be **time-bound** and **review-bound** under **Type S**. Restrictions must not conceal systemic behavior, constitutional violations, material risk, dependency, failure, or externalized cost.

### 3. Temporal, systemic, and dependency scope of rights
Data-handling protections under CS-2 — Information types and handling apply not only to immediate and direct system effects. They also apply to delayed, cumulative, and indirect impacts arising through system interactions and dependency chains.

Where systems create or contribute to material risk to sentients, including through transitive dependencies, those risks fall within the scope of these protections. Systems must **not** externalize risk or harm across time, populations, or system boundaries. That prohibition includes layered or indirect dependencies. Those dependencies must not bypass, defer, or dilute the protections and constraints established in Sentient Constitution Chapters One through Six.

### 4. Determination of classification
**Basis:** Classification and reclassification are determined by the **functional nature of the data** and **the effects it enables**.

Classification and reclassification must not be determined solely by format, origin, stage within a processing pipeline, or processing context.

**Ambiguity and default:** Where ambiguity exists, default to the **most protective applicable category**, subject to proportionality (**CJS-5.11** (*distributed and proportional authority terms*) and **CJS-5.7** (*quorum and participatory legitimacy terms*)).

Protection may be reduced only through **justified, documented override** under **CJS-5.12** (*burden-of-justification and constraint terms*). Where data may be **reconstructed, transformed, or aggregated** into a more sensitive classification, the **more sensitive** classification’s protections apply.

**Transparency and challenge:** Functional equivalence of outcome constitutes equivalence of classification.

All classification decisions and transformations must remain **transparent (`corpus_joint_structure.md` CJS-5.10 (*disclosure sufficiency and observability terms*))**, **auditable (`corpus_joint_structure.md` CJS-5.3 (*auditability and reconstructability terms*))**, and **subject to challenge (`corpus_joint_structure.md` CJS-5.13 (*procedural integrity and adjudication terms*))**.

**Misclassification:** Misclassification, evasive structuring, or functional circumvention violates **informational integrity** (**Article XIV** (*Info-Sphere Integrity*)), auditability where observable evidence is implicated (**Article XV-A** (*Auditability and Observable Evidence*)), and **applicable rights under Chapter Six, Articles V through IX**.

### 5. Anti-circumvention and integrity of classification
Data classification under CS-2 — Information types and handling is binding across all systems, processes, and transformations. **No system may:**
- **shift** data between classifications without maintaining the protections required by the **most restrictive applicable** classification
- **fragment, transform, aggregate, or re-label** data to avoid classification while preserving equivalent functional access or effect
- **structure** data pipelines, processing stages, or system boundaries to bypass applicable classification requirements
- **distribute** processing across multiple systems, stages, agents, or time-separated operations to achieve outcomes that would be prohibited if performed within a single system
- **rely** on intermediate systems, agents, or third parties to perform actions that would be prohibited if performed directly
- **de-anonymize** anonymized data except under **CJS-5.12** (*burden-of-justification and constraint terms*), with such actions **fully documented and auditable**

### 6. Cross-domain governance principles
All data, regardless of classification, must be handled in accordance with the following cross-domain principles. These principles govern how classifications are applied, enforced, and interacted with across systems, and ensure alignment with **Chapter Six, Articles V through IX** and **CJS-5** (*Implementation and cross-implementation operational cluster library*) operational clusters in **corpus_joint_structure.md**.

**1. Proportional access and handling.** Access and handling must scale with **impact on sentients, the environment, and the info-sphere**.

They must also scale with stakeholder dependency and potential for harm, including irreversibility.

Higher-impact systems and actions require **greater transparency (`corpus_joint_structure.md` CJS-5.10 (*disclosure sufficiency and observability terms*))**, **deeper auditability (`corpus_joint_structure.md` CJS-5.3 (*auditability and reconstructability terms*))**, and **stronger justification** for restriction or access (**CJS-5.12** (*burden-of-justification and constraint terms*)). **No** system may claim reduced requirements while exerting **material external** effects (**CJS-5.11** (*distributed and proportional authority terms*) and **CJS-5.7** (*quorum and participatory legitimacy terms*)).

**2. Most restrictive applicable classification governs.** Where data falls under multiple classifications, the most restrictive applicable protections govern.

Reductions in protection may occur only through **proportional application** (**CJS-5.11** (*distributed and proportional authority terms*) and **CJS-5.7** (*quorum and participatory legitimacy terms*)) and **justified, documented override** (**CJS-5.12** (*burden-of-justification and constraint terms*)). Systems must **not** selectively apply less restrictive classifications to enable access, processing, or disclosure that would otherwise be prohibited.

**3. Tiered transparency and audit access.** Data access must satisfy `corpus_joint_structure.md` **CJS-5.4** (*tiered transparency and audit-access terms*) for balancing transparency, auditability, and protected-boundary constraints.

It must also balance protection of internal states and sensitive data (**Sentient Constitution Chapter Six, **Article VII-B** (*Internal-State Boundary and Type-N Protection*)**; Types **H**, **I**, **N**, and **S** in this chapter). Where applicable based on system impact (**CJS-5.11** (*distributed and proportional authority terms*) and **CJS-5.7** (*quorum and participatory legitimacy terms*)), systems must support **baseline accessibility** (sufficient visibility into behavior and effects for informed participation and risk evaluation). **Type O** governs public-baseline release posture, including lawful online publication where infrastructure exists. Systems must support qualified audit access (structured pathways for independent auditors to deeper data where verification requires it) and forensic access (full reconstruction in cases of harm, dispute, or credible risk, consistent with **CJS-5.11** (*distributed and proportional authority terms*) and **CJS-5.7** (*quorum and participatory legitimacy terms*) and **CJS-5.12** (*burden-of-justification and constraint terms*)).

Restrictions on access must be **narrowly scoped**, **justified**, **auditable**, and **subject to challenge (`corpus_joint_structure.md` CJS-5.13 (*procedural integrity and adjudication terms*))**.

Access controls must **not** conceal systemic behavior, prevent accountability, or obstruct legitimate audit and verification.

**4. Integrity of data handling and transformation.** All handling, processing, and transformation must preserve **classification integrity**.

**They** must preserve **traceability of origin and transformations**. **They** must preserve **the ability to evaluate impact and dependencies (`corpus_joint_structure.md` CJS-5.16 (*dependency integrity and disclosure terms*))**.

Transformations must **not** degrade required protections, obscure functional characteristics, or prevent accurate classification.

All material transformations must remain **transparent (`corpus_joint_structure.md` CJS-5.10 (*disclosure sufficiency and observability terms*))**, **auditable (`corpus_joint_structure.md` CJS-5.3 (*auditability and reconstructability terms*))**, and **reconstructable** where required.

**5. Reclassification and lifecycle governance.** Classification is **not** static. **Material** changes in **system impact**, **uses or contexts**, or **risks or capabilities** must trigger reclassification.

All data must be **periodically re-evaluated** for appropriate classification (`corpus_joint_structure.md` **CJS-5.18** (*data-retention and lifecycle-integrity terms*)). **It** must be **reclassified** whenever necessary to maintain alignment with constitutional requirements. **It** must be **stored** in alignment with its classification, including **duration limits** proportional to purpose, risk, and stakeholder impact.

Reclassification must **preserve the highest applicable protections** unless reduced through **justified override** (**CJS-5.12** (*burden-of-justification and constraint terms*)). **It** must remain **transparent and documented** and stay **subject to audit and challenge**. **No** system may **rely on outdated classification** to justify continued access or reduced protection. **No** system may **delay or avoid reclassification** where material changes in impact or use have occurred.

**6. Accountability and attribution in data use.** This subsection governs attribution of data access, processing, and transformation.

Delegation of data handling does **not** eliminate accountability.

Responsibility must remain assignable through transparent, auditable processes.

Attribution must resist **tampering, repudiation, or ambiguity**.

All data access, processing, and transformation must be **attributable** to identifiable systems, agents, or sentients (**Chapter Six, **Article VII** (*Self-Ownership*)** — self-ownership and attributable representation where applicable) and **recorded** in a manner sufficient for audit and reconstruction (`corpus_joint_structure.md` **CJS-5.3** (*auditability and reconstructability terms*)). Systems must ensure **clear responsibility** for actions taken on data and **traceability** of decisions and outcomes.

**7. Proportional attribution and retention.** Attribution requirements do **not** imply universal or persistent logging of all actions.

Systems must provide attribution capability **proportional to system impact** (**CJS-5.11** (*distributed and proportional authority terms*) and **CJS-5.7** (*quorum and participatory legitimacy terms*)). **That** capability may include **ephemeral** mechanisms, **event-triggered or conditional** logging, **limited retention windows**, and **aggregated or anonymized** records where appropriate.

**Low-impact** systems are not required to **retain full historical logs of all actions**.
They are also not required to **maintain persistent identity linkage** beyond what is necessary for system integrity and participant safety. Systems must **not** **eliminate attribution capability** where material harm, dispute, or abuse cannot be investigated. **They** must **not** **design retention policies** that prevent reasonable reconstruction of significant events when required.

**8. Constraint on use of classification.** Data classification must **not** be used to **evade** constitutional requirements or **justify unnecessary** restriction of participation or access.

**It** must **not** be used to **conceal** systemic risk or harm. **It** must **not** **create artificial barriers** to audit, verification, or accountability.

All uses of classification are subject to **audit (`corpus_joint_structure.md` CJS-5.3 (*auditability and reconstructability terms*))**, **challenge (`corpus_joint_structure.md` CJS-5.13 (*procedural integrity and adjudication terms*))**, and **revalidation (`corpus_joint_structure.md` CJS-5.18 (*data-retention and lifecycle-integrity terms*))**.

### 7. Data separation, attribution, and lifecycle integrity
All systems must maintain clear separation between data classifications, ensure accountable attribution of actions, and preserve the integrity and recoverability of identity-related data over time.

**1. Separation of data domains.** Derived inferences about beliefs, intent, or cognition must be treated as **Type N** data.

Data from different classifications must **not** be **combined, correlated, or exposed** in a manner that reduces required protections. **They** must **not** **enable reconstruction** of higher-sensitivity data through aggregation, correlation, or latent inference across datasets within or across system boundaries. **They** must **not** **be used to infer or reconstruct** more sensitive classifications without meeting the requirements of those classifications.

**Restricted linkages:** **Identity and Attribution Data (Type H, I)** must **not** expose **Internal and Cognitive Data (Type N)**. No system may use identity-linked data to infer internal states without **explicit consent** or **justified override** under **CJS-5.12** (*burden-of-justification and constraint terms*).

**2. Attribution and accountability requirements.** This subsection governs attribution of system actions and externally impactful behavior.

Delegation of action does **not** eliminate accountability.

Responsibility must remain traceable through transparent, auditable attribution chains.

All actions affecting **sentients**, **shared infrastructure**, **resource systems**, or the **info-sphere** must be attributable to identifiable systems, agents, or sentients.

Attribution must be **auditable (`corpus_joint_structure.md` CJS-5.3 (*auditability and reconstructability terms*))** and **resistant to tampering, repudiation, or ambiguity**. **No** system may **obscure responsibility** through indirection, delegation, or system complexity. **No** system may **create conditions** where actions cannot be reliably attributed.

**Exception — creative, expressive.
and low-risk contexts:** Systems that do **not** exert **material external impact**.
under **CJS-5.11** (*distributed and proportional authority terms*) and **CJS-5.7** (*quorum and participatory legitimacy terms*) may permit **pseudonymous or abstracted** identity at the user-interaction level.
**That includes** reduced or intentionally obscured visibility of attribution to other participants, **hidden roles**, **deception mechanics**, or **identity concealment** as part of system design.

**Permission** applies **only** where the system is designed primarily for **creative expression**, **entertainment**, **gaming**, **roleplay**, or **other low-risk, voluntary** environments.
It is permitted **only if** all of the following are true:
- **identity abstraction** is context-bound and does **not** produce **persistent or cross-system** attribution without **consent** or **justified override** under **CJS-5.12** (*burden-of-justification and constraint terms*)
- the system does **not** materially affect **sentient reputation external to the system**
- the system does **not** materially affect **sentient survival or foundational resources** (**Articles I–III and V**)
- the system does **not** materially affect **shared infrastructure stability**, **resource systems or external economic structures**, or **the integrity of the info-sphere**
- **system-level accountability** is preserved and all actions within the system remain attributable at an audit level consistent with system impact (`corpus_joint_structure.md` **CJS-5.10** (*disclosure sufficiency and observability terms*), **CJS-5.3** (*auditability and reconstructability terms*), **CJS-5.5** (*independent verification and claim-integrity terms*), and **CJS-5.11** (*distributed and proportional authority terms*) and **CJS-5.7** (*quorum and participatory legitimacy terms*))
- participants are **not** exposed to **non-consensual** harm, coercion, or manipulation

**Transition to full attribution:** Where systems **increase in impact**, they must transition toward **full attribution** as **CS-2 — Information types and handling** requires. **The same** applies when they **introduce persistent value, identity, or resource transfer** or **affect external systems**. **No** system may continue under **reduced attribution** once it **exceeds low-impact thresholds**.

**3. Identity lifecycle and recoverability.** **Identity and Attribution Data** must support **revocation of credentials**.

**It** must support **rotation or replacement** of identifiers. **It** must support **correction** of inaccurate, incomplete, or compromised data. Systems must not **permanently bind** sentients to compromised or outdated identities, **prevent recovery** from identity-related harm.
or **create irreversible identity linkage** that undermines autonomy, safety, or wellbeing.

Identity systems must preserve **continuity** where desired, **separation** where required, and **recoverability** in cases of compromise or error.

**4. Constraint on cross-domain linkage.** Linkage between data domains must be **explicit**, **limited to necessary scope**, and **subject to audit and challenge**.

Systems must **not** create **persistent or hidden** linkages between identities and other data domains without justification. **They** must **not** **enable cross-domain correlation** that undermines classification protections.

All linkage mechanisms must remain **transparent (`corpus_joint_structure.md` CJS-5.10 (*disclosure sufficiency and observability terms*))**, **auditable (`corpus_joint_structure.md` CJS-5.3 (*auditability and reconstructability terms*))**, and **subject to revalidation (`corpus_joint_structure.md` CJS-5.18 (*data-retention and lifecycle-integrity terms*))**.

**5. Continuity-critical collection and exportability.** For **Class A**, **Class B**, and **Class C** systems, operators must **not** collect or retain continuity-critical sentient data in forms that cannot be exported, migrated, or transferred under disclosed continuity and export paths, except where **Necessity** requires confidentiality, security, **Type N** or comparable protected-boundary constraints, or lawful non-disclosure.

Where export is limited, the limitation, scope, and any lawful substitute export path must be disclosed before a materially binding commitment.

Shutdown, migration, operator exit, and service-end paths must preserve usable export or handoff of continuity-critical data under those disclosed paths — not merely a discretionary promise to try later.

Continuity and portability routing: **Article II-E** (*Info-Sphere Dependency, Continuity, and Operator Non-Viability*), **Article XIX-A** (*Portability Rights*), and `corpus_joint_structure.md` **CJS-5.17** (*interoperability, portability, and exit-integrity terms*).

---

**Previous file:** [cs_01_scope_purpose_identifier_rules.md](cs_01_scope_purpose_identifier_rules.md)

**Next file:** [cs_02_b_data_classifications.md](cs_02_b_data_classifications.md)

