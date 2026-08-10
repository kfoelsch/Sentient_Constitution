<a id="cs-2-part-a-information-types-and-handling"></a>
# CS-2, Part A: Information types and handling

<details>
<summary><strong><span style="color: #2563eb;">Corpus placement (non-operative): file structure and reading rules</span></strong></summary>

> The following content is **reader guidance only**. It does not add, remove, or narrow binding obligations elsewhere in this file or in other CS-2 parts.
>
> This file contains **CS-2, Part A** — purpose and scope (including identity self-ownership and continuity-critical export), classification determination, anti-circumvention, cross-domain governance principles, data separation / attribution, Type O baseline, and **System Data Types Record** governance (**§§1–8**). **Part B** — data classifications (**Type E** through **Type S**, including **Type O**) — is in [`cs_02_b_data_classifications.md`](cs_02_b_data_classifications.md).

</details>

<br>

**CS-2, Part A**, owns **information-type determination, foundational identity and continuity controls, cross-domain governance, separation / attribution, and the [System Data Types Record](../core_05_band_continuity.md#system-data-types-record-constitutional)**. Canonical type definitions and per-type handling rules are in **[Part B](cs_02_b_data_classifications.md#cs-2-part-b-data-classifications)**.
*In plain terms: Part A says how to type data, keep those types honest across systems, protect separation, attribution, and exit, and keep a System Data Types Record that audits can check — Part B names the types themselves.*

**Introductory provisions:**
*In plain terms: tell the truth in public where you can, but keep safeguards that protect sentients, privacy, trust, and system integrity — and make those safeguards stronger when impact is higher.*

Systems must preserve the practical ability to publish truthful information while maintaining safeguards for harm prevention, privacy, trust, and system integrity.
Requirements and limitations scale proportionally with system classification and potential impact. They must impose proportionate safeguards on publication within their boundaries where necessary to preserve trust, safety, and constitutional compliance.
<a id="1-purpose-and-scope"></a>

## 1. Purpose and scope

*In plain terms: Chapter Six rights need trustworthy data handling; CS-2 is the systems rulebook that makes typing, access defaults, integrity, identity self-ownership, and Class A/B/C continuity real.*

**Sentient Constitution Chapter Six** (Articles **I**–**XXV**; presentation **Parts A–D**) states Foundational Rights that depend on strong, reproducible data handling — including info-sphere, audit, and comprehensibility duties (e.g., **Articles XIV**, **XV**, and **XX**). CS-2 is the systems-layer implementation of those duties.

CS-2 implements:

- **Data typing** — every material dataset is assigned one or more types defined in **[Part B](cs_02_b_data_classifications.md#cs-2-part-b-data-classifications)** (**Type E**, **G**, **O**, **H**, **I**, **N**, and **S**)
- **System Data Types Record** — for every system with **material impact**, operators must maintain a [System Data Types Record](../core_05_band_continuity.md#system-data-types-record-constitutional) stating types in scope, handling posture, and re-evaluation status. That record is **material audited information**: auditing processes require it, and System Data Types Record audits check it between and beside [System Alignment Certification](../core_05_band_continuity.md#system-alignment-certification-constitutional) cycles ([§8](#8-system-data-types-record-governance)). When System Alignment Certification runs, **[Chapter Seven §4](../core_07_a_system_alignment_certification_evaluation.md#4-data-types-and-handling-evaluation)** must produce or verify the record and include it in the [System Certification Record](../core_05_band_continuity.md#system-certification-record-constitutional) under **[Part B §11.1](../core_07_b_system_alignment_certification_record_process.md#111-minimum-record-contents)**
- **Default access posture** — each type belongs to one of four **access-posture bands** defined in **[Part B §8](cs_02_b_data_classifications.md#8-data-classifications)** (*open / accessible by default*; *audit-accessible, not public*; *restricted by default*; *non-accessible by default*), plus type-specific disclosure, consent, and handling rules. Bands group shared defaults; they are **not** a ranked sensitivity score
- **Most-restrictive rule** — where more than one type applies, the strongest applicable protections govern ([§2](#2-determination-of-classification) *When it is unclear*), subject to proportionality (**CJS-3.11** (*distributed and proportional authority terms*) and **CJS-3.7** (*quorum and participatory legitimacy terms*))
- **Classification integrity** — type follows the **functional nature of the data** and the **effects it enables**, not format, origin, or pipeline stage; systems may not evade typing by fragmentation, re-labeling, or indirection ([§2](#2-determination-of-classification)–[§4](#4-anti-circumvention-and-integrity-of-classification))
- **Identity self-ownership** — identity and attribution data remain under sentient control through revocation, rotation, correction, and recoverability ([§1.1](#11-identity-self-ownership-and-recoverability); **Article VII** (*Self-Ownership*))
- **Continuity and exit** — for **Class A**, **Class B**, and **Class C** systems, sentients must be able to take their continuity-critical data with them when a service ends or changes hands ([§1.2](#12-continuity-critical-collection-and-exportability); **Article II-E** (*Info-Sphere Dependency, Continuity, and Operator Non-Viability*)), and the formats and interfaces used for that handoff must meet **CJS-3.17** (*interoperability, portability, and exit-integrity terms*)
- **Cross-domain governance** — proportional access, reclassification and lifecycle, tiered transparency and audit, transformation traceability, attribution, and retention ([§5](#5-cross-domain-governance-principles)); typing integrity and anti-evasion remain in [§2](#2-determination-of-classification)–[§4](#4-anti-circumvention-and-integrity-of-classification)
- **Separation and attribution** — keep higher-sensitivity domains from leaking through linkage or inference, and preserve attributable action ([§6](#6-data-separation-and-attribution))
- **Class scaling** — higher-impact systems get stricter data rules. How strict depends on the system's class under **CS-3 — System classification and handling**
- **Type O public-baseline (Class A/B/C)** — for high-impact systems, [Public Oversight Baseline Disclosure](../core_05_band_oversight.md#public-oversight-baseline-disclosure) must be released by default as **Type O** data defined in **[Part B — Type O](cs_02_b_data_classifications.md#type-o-open-public-baseline-disclosure-data)**, with substitute and holding-back limits in [§7](#7-type-o-baseline-for-class-abc-systems)

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

*In plain terms: for Class A/B/C systems, do not lock sentients' continuity-critical data in a form they cannot take with them when the service ends or changes hands — and disclose any lawful limits up front.*

This subsection is foundational to continuity and exit under CS-2. It implements:
- **Article II-E** (*Info-Sphere Dependency, Continuity, and Operator Non-Viability*)
- **Article XIX-A** (*Portability Rights*)
- **CJS-3.17** (*interoperability, portability, and exit-integrity terms*)

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
## 2. Determination of classification

*In plain terms: type data by what it does and enables — not by format or pipeline stage. When unsure, protect more; weaken protection only with a documented justification; and do not dodge typing by rearranging the same outcome.*

**What counts.** Type the data by **what it is for** and **what it lets someone do** — not by file format, where it came from, or which step of a pipeline it sits in. The same rule applies when retyping data later.

<a id="most-restrictive-applicable-classification-governs"></a>
**When it is unclear.** If more than one type could fit, the **most protective** applicable protections govern. Use the most protective type that still fits, scaled to impact under:
- **CJS-3.11** (*distributed and proportional authority terms*)
- **CJS-3.7** (*quorum and participatory legitimacy terms*)

Weaker protection is allowed only with a **justified, documented override** under **CJS-3.12** (*burden-of-justification and constraint terms*). Systems must **not** selectively apply less restrictive classifications to enable access, processing, or disclosure that would otherwise be prohibited.

If pieces of data can be rebuilt, transformed, or combined into something more sensitive, treat them under that **more sensitive** type.

**Same outcome, same type.** If two arrangements work the same way in practice, they get the same classification. Typing decisions and material changes must stay:
- **transparent** (**CJS-3.10** (*disclosure sufficiency and observability terms*))
- **auditable** (**CJS-3.3** (*auditability and reconstructability terms*))
- **open to challenge** (**CJS-3.13** (*procedural integrity and adjudication terms*))

**Wrong typing is a violation.** Mislabeling data, arranging it to dodge the rules, or achieving the same harmful access through a different structure violates:
- **informational integrity** (**Article XIV** (*Info-Sphere Integrity*))
- auditability where evidence is implicated (**Article XV-A** (*Auditability and Observable Evidence*))
- applicable rights under **Chapter Six, Articles V through IX**

<a id="3-temporal-systemic-and-dependency-scope-of-rights"></a>
## 3. Temporal, systemic, and dependency scope of rights

*In plain terms: protections cover delayed, stacked, and indirect harm too — including harm passed through other systems. You cannot push risk onto other sentients, times, or systems to dodge the rules.*

Data-handling protections under CS-2 — Information types and handling apply not only to immediate and direct system effects. They also apply to delayed, cumulative, and indirect impacts arising through system interactions and dependency chains.

Where systems create or contribute to material risk to sentients, including through transitive dependencies, those risks fall within the scope of these protections. Systems must **not** externalize risk or harm across time, populations, or system boundaries. That prohibition includes layered or indirect dependencies. Those dependencies must not bypass, defer, or dilute the protections and constraints established in Sentient Constitution Chapters One through Six.

<a id="4-anti-circumvention-and-integrity-of-classification"></a>
## 4. Anti-circumvention and integrity of classification

*In plain terms: you may not break, relabel, split, outsource, or pipeline data just to escape its type — and you may not use typing itself to block participation, hide risk, or shut down audit. Keep the strongest applicable protections, and document any de-anonymization.*

Data classification under CS-2 — Information types and handling is binding across all systems, processes, and transformations. **No system may:**
- **shift** data between classifications without maintaining the protections required by the **most restrictive applicable** classification
- **fragment, transform, aggregate, or re-label** data to avoid classification while preserving equivalent functional access or effect
- **structure** data pipelines, processing stages, or system boundaries to bypass applicable classification requirements
- **distribute** processing across multiple systems, stages, agents, or time-separated operations to achieve outcomes that would be prohibited if performed within a single system
- **rely** on intermediate systems, agents, or third parties to perform actions that would be prohibited if performed directly
- **de-anonymize** anonymized data except under **CJS-3.12** (*burden-of-justification and constraint terms*), with such actions **fully documented and auditable**
- **use** classification to **evade** constitutional requirements, **justify unnecessary** restriction of participation or access, **conceal** systemic risk or harm, or **create artificial barriers** to audit, verification, or accountability
- **treat** restricted source data (including **Type H**, **Type I**, **Type N**, or **Type S**) as reclassified to **Type O** merely because a system is Class A/B/C or merely by copying that data, without meeting the substitute, reclassification, or release requirements in §7 and [Part B §8](cs_02_b_data_classifications.md#8-data-classifications)

<a id="5-cross-domain-governance-principles"></a>
## 5. Cross-domain governance principles

*In plain terms: these are the shared rules for how typed data is accessed, transformed, retyped, attributed, and retained across systems — stricter where impact is higher. Typing integrity and anti-evasion live in [§2](#2-determination-of-classification)–[§4](#4-anti-circumvention-and-integrity-of-classification).*

All data, regardless of classification, must be handled in accordance with the following cross-domain principles. These principles govern how classifications are applied, enforced, and interacted with across systems, and ensure alignment with **Chapter Six, Articles I through IX** and **CJS-3** (*Implementation and cross-implementation operational cluster library*) operational clusters in **corpus_joint_structure.md**. Survival-, environment-, and substrate-critical data handling remains grounded in **Articles I–III and V**; participation, oversight, and protected-boundary duties run through **Articles V through IX**.

Part B type sections state type-specific defaults, definitions, and handling rules. They do **not** restate this cross-domain alignment unless a type needs an additional, type-specific pointer.

<a id="50-access-posture-bands"></a>

**5.0. Access-posture bands.**

*In plain terms: types share a default sharing style — open, audit-only, restricted, or off-limits — so common rules can attach to that style. The letter codes are still not a least-to-most sensitive ranking.*

Each type belongs to one **access-posture band**. Bands define shared default access and restriction posture. They are **labels for shared defaults**, not a ranked list from “least sensitive” to “most sensitive.” Type-specific content and deltas are in **[Part B §8](cs_02_b_data_classifications.md#8-data-classifications)**.

| Band | Types | Shared default posture |
|---|---|---|
| **Open / accessible by default** | **Type O**, **Type E** | Strong presumption of openness or accessibility; hold-backs are narrow |
| **Audit-accessible, not public** | **Type G** | Fully auditable through structured or qualified audit access; not public by default; public face is [Public Oversight Baseline Disclosure](../core_05_band_oversight.md#public-oversight-baseline-disclosure) (**Type O**) |
| **Restricted by default** | **Type H**, **Type I**, **Type S** | Access only for defined legitimate purposes, consent, or justified override as the type requires; **Type S** is also time-bound and review-bound |
| **Non-accessible by default** | **Type N** | Access only through explicit, informed, freely given consent or justified override under **CJS-3.12** (*burden-of-justification and constraint terms*) |

**Band-level rules:**
- **Open / accessible by default.** Presumptive accessibility or open release applies. Restrictions that withhold otherwise-accessible or disclosable material must satisfy [§5.3](#53-tiered-transparency-and-audit-access). For **Type E**, restriction is permitted only when disclosure would **itself** create material risk of enabling targeted or disproportionate harm, exploitation, or system compromise, unless a narrower type-specific rule applies.
- **Audit-accessible, not public.** Non-public status must **not** function as unreviewable secrecy. Structured or qualified audit access must remain functionally effective under **CJS-3.3** (*auditability and reconstructability terms*) and **CJS-3.4** (*tiered transparency and audit-access terms*). [Public Oversight Baseline Disclosure](../core_05_band_oversight.md#public-oversight-baseline-disclosure) is **Type O**, not a substitute satisfied by audit access alone.
- **Restricted by default.** Collection, access, and use must stay limited to the justified purpose. Broader use requires consent or justified override as the applicable type states. **Type S** restrictions must remain time-bound and review-bound under [§5.3](#53-tiered-transparency-and-audit-access). Systems managing restricted-by-default data must **not**:
  - **expose** that data beyond what is necessary for its justified purpose
  - **create persistent tracking** across unrelated contexts **by default** — any cross-context aggregation or linkage requires explicit justification under **CJS-3.11** (*distributed and proportional authority terms*) and **CJS-3.7** (*quorum and participatory legitimacy terms*), including demonstration that it does **not** materially undermine autonomy or create **coercive power asymmetries**
- **Non-accessible by default.** Maximum restriction. No access, inference, reconstruction, or exposure without consent or justified override under **CJS-3.12** (*burden-of-justification and constraint terms*).

**Shared anti-abuse limits.** Across all types, systems must **not**:
- use data handling to enable **coercion, surveillance, or manipulation** (**Article VII-A** (*Self-Ownership of Body and Mind*)), including consolidating power or control through data or identity dependency (**CJS-3.17** (*interoperability, portability, and exit-integrity terms*))
- **restrict access** to participation, resources, or systems **without justified cause** (**CJS-3.12** (*burden-of-justification and constraint terms*))

**Shared consent integrity.** Where access, use, or disclosure depends on consent, systems must treat consent as:
- **explicit and informed**
- freely given without coercion, manipulation, or deceptive framing (**Article VII-A** (*Self-Ownership of Body and Mind*))
- specific to intended use and scope
- revocable where technically feasible

Systems must **not**:
- **infer consent from behavior**
- assume consent through participation in unrelated systems
- transfer or repurpose consented data without **explicit reauthorization**

**Shared security- and intelligence-use records.** Where typed data is used for security, intelligence, eligibility restriction, or covert-investigation purposes, systems must keep reviewable records of:
- **model role**, where models are used
- **authorization basis**
- **protected-activity safeguards**
- any **minimization, segregation, challenge, or deletion** controls required by **Article XIII-A** (*Security, Intelligence, and Covert-Power Limits*) or **CJS-3.12** (*burden-of-justification and constraint terms*)

**Type H and Type I anti-capture limits.** In addition to the restricted-by-default band rules, systems managing **Type H** or **Type I** data must **not**:
- **centralize** that data in a manner that creates systemic control or dependency
- create, through security, intelligence, screening, or covert-investigation systems, any of the following absent a specifically justified and independently reviewable basis consistent with **Article XIII-A** (*Security, Intelligence, and Covert-Power Limits*) and the stricter applicable protections in this section:
  - generalized **watchlisting**
  - persistent **cross-context tracking**
  - hidden **political, associational, or belief-linked profiling**

Where more than one type applies, the **most-restrictive** applicable protections govern ([§2](#2-determination-of-classification)). Band membership does **not** displace **Type O** publication duties or **Type E** survival-coordination duties.

<a id="51-proportional-access-and-handling"></a>

**5.1. Proportional access and handling.**

*In plain terms: bigger impact means stricter access, more transparency, deeper audit, and stronger justification — you cannot claim light rules while causing heavy outside effects. When access is allowed or required, it must arrive in time to be useful.*

Access and handling must scale with:
- **impact on sentients, the environment, and the info-sphere**
- stakeholder dependency
- potential for harm, including irreversibility

Higher-impact systems and actions require:
- **greater transparency** (**CJS-3.10** (*disclosure sufficiency and observability terms*))
- **deeper auditability** (**CJS-3.3** (*auditability and reconstructability terms*))
- **stronger independent verification and claim integrity** (**CJS-3.5** (*independent verification and claim-integrity terms*))
- **more comprehensible presentation** where affected stakeholders must understand or act on the data (**CJS-3.8** (*comprehensibility and cognitive accessibility terms*))
- **stronger justification** for restriction or access (**CJS-3.12** (*burden-of-justification and constraint terms*))

Where access is **required or permitted** under the applicable type, it must be **timely enough for the lawful purpose**. That duty scales with impact under **CJS-3.11** (*distributed and proportional authority terms*) and **CJS-3.7** (*quorum and participatory legitimacy terms*). It does **not** create a duty of public availability for types that are restricted or non-accessible by default.

Where a type requires accessibility, disclosure, or audit access, systems must also:
- **preserve sufficient fidelity** for audit, lawful response, and long-term stewardship, proportionate to impact and dependency
- **not** aggregate, downsample, or reduce resolution in ways that **materially obscure** trends, risks, or localized impacts that affected stakeholders are entitled to see under that type

**No** system may claim reduced requirements while exerting **material external** effects under:
- **CJS-3.11** (*distributed and proportional authority terms*)
- **CJS-3.7** (*quorum and participatory legitimacy terms*)

<a id="52-reclassification-and-lifecycle-governance"></a>

**5.2. Reclassification and lifecycle governance.**

*In plain terms: types are not forever — recheck them when impact, use, or risk changes, keep the strongest protections unless justified, and do not hide behind an outdated label.*

Classification is **not** static. **Material** changes in any of the following must trigger reclassification:
- **system impact**
- **uses or contexts**
- **risks or capabilities**

All data must be:
- **periodically re-evaluated** for appropriate classification (**CJS-3.18** (*data-retention and lifecycle-integrity terms*)) — verified on each materially impactful system alignment certification or revalidation cycle under **[Chapter Seven §4](../core_07_a_system_alignment_certification_evaluation.md#4-data-types-and-handling-evaluation)** (*Data Types and Handling Evaluation*) and recorded in the [System Data Types Record](../core_05_band_continuity.md#system-data-types-record-constitutional) under **[Chapter Seven Part B §11.1](../core_07_b_system_alignment_certification_record_process.md#111-minimum-record-contents)** and [§8](#8-system-data-types-record-governance)
- **reclassified** whenever necessary to maintain alignment with constitutional requirements
- **stored** in alignment with its classification, including **duration limits** proportional to purpose, risk, and stakeholder impact

Reclassification must:
- **preserve the highest applicable protections** unless reduced through **justified override** (**CJS-3.12** (*burden-of-justification and constraint terms*))
- remain **transparent and documented** **in the System Data Types Record**
- stay **subject to audit and challenge**

**No** system may:
- **rely on outdated classification** to justify continued access or reduced protection
- **delay or avoid reclassification** where material changes in impact or use have occurred

This subsection owns **retype mechanics**. [§8](#8-system-data-types-record-governance) owns **when** operators must update the System Data Types Record after those retypes.

<a id="53-tiered-transparency-and-audit-access"></a>

**5.3. Tiered transparency and audit access.**

*In plain terms: sentients need enough visibility to understand risk; auditors need deeper access when needed; and hiding system behavior behind access controls is not allowed.*

Data access must satisfy **CJS-3.4** (*tiered transparency and audit-access terms*) for balancing transparency, auditability, and protected-boundary constraints. Public-baseline transparency duties also run through [Transparency](../core_05_band_oversight.md#transparency) and **Article XV** (*Audit, Transparency, and Independent Verification*).

It must also balance protection of internal states and sensitive data (**Sentient Constitution Chapter Six, **Article VII-B** (*Internal-State Boundary and Type-N Protection*)**; Types **H**, **I**, **N**, and **S** in this section), including cross-implementation trust integrity under **CJS-2.3** (*Cross-implementation trust integrity (joint operation model)*) where incorporated via **Chapter Sixteen**. Where applicable based on system impact (**CJS-3.11** (*distributed and proportional authority terms*) and **CJS-3.7** (*quorum and participatory legitimacy terms*)), systems must support:

- **Identity Data Protection.** [Identity Data Protection](core_05_band_continuity.md#identity-data-protection) governs the restricted-linkages ban (Type H/I → Type N) in this subsection. See [§6.1](#61-separation-of-data-domains) for the domain-separation mechanics.
- **baseline accessibility** — sufficient visibility into behavior and effects for informed participation and risk evaluation
- **qualified audit access** — structured pathways for independent auditors to deeper data where verification requires it
- **forensic access** — full reconstruction in cases of harm, dispute, or credible risk, consistent with **CJS-3.11**, **CJS-3.7**, and **CJS-3.12** (*burden-of-justification and constraint terms*)
- **access-control integrity** — access controls must **not** conceal systemic behavior, prevent accountability, or obstruct legitimate audit and verification

For **Class A**, **Class B**, and **Class C** systems, [Public Oversight Baseline Disclosure](../core_05_band_oversight.md#public-oversight-baseline-disclosure) defined in **[Part B — Type O](cs_02_b_data_classifications.md#type-o-open-public-baseline-disclosure-data)** is **public by default**, subject to the substitute and holding-back rules in [§7](#7-type-o-baseline-for-class-abc-systems).

**Audit-process outputs.** Findings, reports, eligibility rules for deeper access, and related artifacts from material audit, verification, or independent review follow the **[CJS-3.3 audit process home](../corpus_joint_structure/cjs_03_audit_process.md#cjs-33-audit-process-home)** and the disclosure preference in **[CJS-3.4](../corpus_joint_structure/cjs_03o_oversight_operations.md#cjs-34-audit-process-output-disclosure)** (*tiered transparency and audit-access terms*): **Type O** where feasible, then qualified **Type G** (or other non-public source) access, then forensic or more-restricted tiers only as justified. This subsection owns the CS-2 typing and access-tier mechanics those outputs use; it does not relocate audit-process ownership out of **CJS-3.3**–**CJS-3.5**.

Any limit on who may see or use data must be:
- **narrow in scope** — only as broad as needed for the stated lawful purpose
- **justified** — with reasons that can be checked
- **auditable**
- **open to challenge** (**CJS-3.13** (*procedural integrity and adjudication terms*))

Where the limit withholds information that would otherwise be accessible or disclosable under the applicable type, it must also be:
- **time-bound**
- **documented**, and subject to **delayed disclosure and audit** where delayed release is used
- shown to **reduce net harm** relative to fuller disclosure under **CJS-3.11** (*distributed and proportional authority terms*) and **CJS-3.7** (*quorum and participatory legitimacy terms*)
- shaped to preserve **maximum feasible** visibility into the **existence and character** of the risk, where public or baseline visibility applies

Where data mixes **Type E** coordination-relevant elements with **Type S** exploit-sensitive elements, systems must **disclose** the coordination-relevant components and **restrict only** exploit-enabling components unless separation is **not technically feasible**. If separation is not feasible, restriction must be **explicitly justified**, **minimized** in scope and duration, and **subject to post-release disclosure and audit**. Type-specific interaction rules are in [Part B — Type S · Interaction with Type E](cs_02_b_data_classifications.md#type-s-interaction-with-type-e).

Where **Type S** restricts disclosure for safety, security, or protected investigation, the restriction must also satisfy **CJS-3.21** (*adversarial robustness and abuse-resistance terms*) and **CJS-3.22** (*constrained-secrecy and protected-investigation terms*), remain **time-bound** and **review-bound**, and stay open to challenge under **CJS-3.13** (*procedural integrity and adjudication terms*).

<a id="54-integrity-of-data-handling-and-transformation"></a>

**5.4. Integrity of data handling and transformation.**

*In plain terms: keep a usable trail of where data came from and what changed, so impact and dependencies can still be checked and material transformations can be reconstructed.*

All material handling, processing, and transformation must preserve:

- **traceability of origin and transformations**
- **the ability to evaluate impact and dependencies** (**CJS-3.16** (*dependency integrity and disclosure terms*))
- **transparency, auditability, and reconstructability** where required (**CJS-3.10** (*disclosure sufficiency and observability terms*); **CJS-3.3** (*auditability and reconstructability terms*))

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
- **recorded** in a manner sufficient for audit and reconstruction (**CJS-3.3** (*auditability and reconstructability terms*))

Systems must ensure:
- **clear responsibility** for actions taken on data
- **traceability** of decisions and outcomes

<a id="56-proportional-attribution-and-retention"></a>

**5.6. Proportional attribution and retention.**

*In plain terms: you do not need forever-logs for everything, but you must keep enough attribution to investigate serious harm, dispute, or abuse.*

Attribution requirements do **not** imply universal or persistent logging of all actions.

Systems must provide attribution capability **proportional to system impact** sufficient to support [Attributable Action](core_05_band_accountability.md#attributable-action-constitutional) and [Attribution Integrity](core_05_band_accountability.md#attribution-integrity-constitutional) under:
- **CJS-3.11** (*distributed and proportional authority terms*)
- **CJS-3.7** (*quorum and participatory legitimacy terms*)

That capability may include:
- **short-lived** mechanisms — attribution that exists only long enough for the immediate purpose, then expires
- **event-triggered or conditional** logging
- **limited retention windows** under **CJS-3.18** (*data-retention and lifecycle-integrity terms*)
- **aggregated or anonymized** records where appropriate
- retention and disposition scaled to **reversibility and containment** needs under **CJS-3.20** (*reversibility and containment terms*)

**Low-impact** systems are **not** required to:
- **retain full historical logs of all actions**
- **maintain persistent identity linkage** beyond what is necessary for system integrity and participant safety

Systems must **not**:
- **eliminate attribution capability** where material harm, dispute, or abuse cannot be investigated
- **design retention policies** that prevent reasonable reconstruction of significant events when required

<a id="6-data-separation-and-attribution"></a>
## 6. Data separation and attribution

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

**Restricted linkages** are governed by [Identity Data Protection](core_05_band_continuity.md#identity-data-protection); this subsection applies the domain-separation mechanics above.

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
- **transparent** (CJS-3.10 (*disclosure sufficiency and observability terms*))
- **auditable** (CJS-3.3 (*auditability and reconstructability terms*))
- **subject to revalidation** (CJS-3.18 (*data-retention and lifecycle-integrity terms*))

<a id="63-attribution-and-accountability-requirements"></a>

**6.3. Attribution and accountability requirements.**

*In plain terms: actions that affect sentients or shared systems must be traceable to someone or something responsible. If impact grows — or value, identity, or resources start moving outside the system — reduced attribution must end and full attribution must take over.*

This subsection applies [Attribution Integrity](core_05_band_accountability.md#attribution-integrity-constitutional) and [Attributable Action](core_05_band_accountability.md#attributable-action-constitutional) to system actions that affect the outside world:

- **No** system may **obscure responsibility** through indirection, delegation, or system complexity ([Attribution Integrity](core_05_band_accountability.md#attribution-integrity-constitutional))
- **No** system may **create conditions** where actions cannot be reliably attributed ([Attribution Integrity](core_05_band_accountability.md#attribution-integrity-constitutional))
- Delegation of action does **not** eliminate accountability
- Responsibility must remain traceable through transparent, auditable attribution chains

**Attributable action scope and audit-resistance.**

- All actions affecting **sentients**, **shared infrastructure**, **resource systems**, or the **info-sphere** must satisfy [Attributable Action](core_05_band_accountability.md#attributable-action-constitutional) through identifiable systems, agents, or sentients
- Attribution must satisfy [Attribution Integrity](core_05_band_accountability.md#attribution-integrity-constitutional), including **auditability (CJS-3.3 (*auditability and reconstructability terms*))** and resistance to tampering, repudiation, or ambiguity

**Transition to full attribution.** Where systems **increase in impact**, they must transition toward **full attribution**. The same applies when they:
- **introduce persistent value, identity, or resource transfer**
- **affect external systems**

**No** system may continue under **reduced attribution** once it **exceeds low-impact thresholds**. Narrow reduced-attribution permission for creative and low-risk contexts is stated in [§6.4](#64-creative-expressive-and-low-risk-attribution-exception).

<a id="64-creative-expressive-and-low-risk-attribution-exception"></a>

**6.4. Creative, expressive, and low-risk attribution exception.**

*In plain terms: low-risk creative spaces may hide who you are from other users — but only while audit-level accountability stays intact and impact stays low.*

Systems that do **not** exert **material external impact** under **CJS-3.11** (*distributed and proportional authority terms*) and **CJS-3.7** (*quorum and participatory legitimacy terms*) may permit **pseudonymous or abstracted** identity at the user-interaction level. That includes:
- reduced or intentionally obscured visibility of attribution to other participants
- **hidden roles**
- **deception mechanics**
- **identity concealment** as part of system design

**Permission** applies **only** where the system is designed primarily for **creative expression**, **entertainment**, **gaming**, **roleplay**, or **other low-risk, voluntary** environments.
It is permitted **only if** all of the following are true:
- **identity abstraction** is context-bound and does **not** produce **persistent or cross-system** attribution without **consent** or **justified override** under **CJS-3.12** (*burden-of-justification and constraint terms*)
- the system does **not** materially affect **sentient reputation external to the system**
- the system does **not** materially affect **sentient survival or foundational resources** (**Articles I–III and V**)
- the system does **not** materially affect **shared infrastructure stability**, **resource systems or external economic structures**, or **the integrity of the info-sphere**
- **system-level accountability** is preserved and all actions within the system remain attributable at an audit level consistent with:
  - [Attributable Action](core_05_band_accountability.md#attributable-action-constitutional)
  - [Attribution Integrity](core_05_band_accountability.md#attribution-integrity-constitutional)
  - system impact
  - **CJS-3.10** (*disclosure sufficiency and observability terms*)
  - **CJS-3.3** (*auditability and reconstructability terms*)
  - **CJS-3.5** (*independent verification and claim-integrity terms*)
  - **CJS-3.11** (*distributed and proportional authority terms*)
  - **CJS-3.7** (*quorum and participatory legitimacy terms*)
- participants are **not** exposed to **non-consensual** harm, coercion, or manipulation

<a id="7-type-o-baseline-for-class-abc-systems"></a>
## 7. Type O baseline for Class A/B/C systems

*In plain terms: high-impact systems must publish [Public Oversight Baseline Disclosure](../core_05_band_oversight.md#public-oversight-baseline-disclosure) as Type O by default — scoped to what the Charter claims, what class the system is, and what the system actually does; checked each certification cycle. Where Type G, Type E, or other raw protected or non-baseline data cannot be released as that disclosure, publish the strongest feasible public substitute; and holding data back must be narrow and challengeable.*

For **Class A**, **Class B**, and **Class C** systems, [Public Oversight Baseline Disclosure](../core_05_band_oversight.md#public-oversight-baseline-disclosure) — the **Type O** public-baseline content defined in **[Part B — Type O](cs_02_b_data_classifications.md#type-o-open-public-baseline-disclosure-data)** — is **public by default** and must be released as **Type O**, subject to the substitute and holding-back rules below.

**Scope of the baseline.** What Public Oversight Baseline Disclosure must cover is **mapped from** the governing [Charter](../core_05_band_continuity.md#charter) (or equivalent published scope instrument), the assigned system class under **CS-3**, and observed [System Boundaries](../core_05_band_continuity.md#system-boundaries). Charter fields — purpose, in-scope and out-of-scope limits, affected communities and dependencies, and classification assumptions — are inputs to that coverage map; they are **not** the sole source of Type O content. Understated Charter text, paper-only scope, or a missing Charter where one is required must **not** shrink Type O publication duties. Sufficiency of Public Oversight Baseline Disclosure is verified on each materially impactful system alignment certification or revalidation cycle under **[Chapter Seven §4](../core_07_a_system_alignment_certification_evaluation.md#4-data-types-and-handling-evaluation)** (*Data Types and Handling Evaluation*) and recorded in the [System Data Types Record](../core_05_band_continuity.md#system-data-types-record-constitutional) under **[Chapter Seven Part B §11](../core_07_b_system_alignment_certification_record_process.md#11-certification-record)** and [§8](#8-system-data-types-record-governance).

**Substitutes for non-public or restricted source data.** If raw disclosure of **Type G**, **Type E**, or other protected source would harm privacy, identity, internal-state protection, safety, security, or an active restricted investigation, or if full release would exceed Public Oversight Baseline Disclosure, publish the strongest feasible **Type O** substitute instead — for example:
- aggregation
- de-identification
- summary or delayed disclosure

Keep the underlying records under their original type unless lawfully reclassified. Where full public release is inappropriate, **structured or qualified audit access** to **Type G** or other non-public source must remain available in parallel under **CJS-3.3** (*auditability and reconstructability terms*) and **CJS-3.4** (*tiered transparency and audit-access terms*), and must **not** replace [Public Oversight Baseline Disclosure](../core_05_band_oversight.md#public-oversight-baseline-disclosure).

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

<a id="8-system-data-types-record-governance"></a>
## 8. System Data Types Record governance

*In plain terms: keep a System Data Types Record that says what data the system touches and how it is handled — own it, publish a usable view, let audits and challenges check it, update it when types change, and fix understatement. When certification runs, that same file must be produced or verified and put in the certification case file.*

**System alignment certification (SAC) bridge.** When [System Alignment Certification](../core_05_band_continuity.md#system-alignment-certification-constitutional) runs for a materially impactful system, **[Chapter Seven §4](../core_07_a_system_alignment_certification_evaluation.md#4-data-types-and-handling-evaluation)** (*Data Types and Handling Evaluation*) must **produce or verify** the [System Data Types Record](../core_05_band_continuity.md#system-data-types-record-constitutional) and include it (or its required contents) in the [System Certification Record](../core_05_band_continuity.md#system-certification-record-constitutional) under **[Part B §11.1](../core_07_b_system_alignment_certification_record_process.md#111-minimum-record-contents)**. Under the **oversight** Tetrad leg, that SAC cycle is one especially large audit process among others; [§8.3](#83-audit-the-system-data-types-record) System Data Types Record audits continue between and beside certification cycles.

Operators must maintain that System Data Types Record for every system with **material impact**. It is the CS-2 type-and-handling file — not a marketing label, and **not** the full System Certification Record. Required contents are owned in the [System Data Types Record](../core_05_band_continuity.md#system-data-types-record-constitutional) definition; Part B names the types themselves.

This section owns what operators must **do with** the System Data Types Record between and during those certification cycles:

| Duty | Acts on the System Data Types Record by… |
| --- | --- |
| [§8.1](#81-own-the-system-data-types-record) | **Owning** it |
| [§8.2](#82-disclose-the-system-data-types-record) | **Disclosing** it |
| [§8.3](#83-audit-the-system-data-types-record) | **Auditing** it |
| [§8.4](#84-challenge-the-system-data-types-record) | **Challenging** it |
| [§8.5](#85-update-the-system-data-types-record) | **Updating** it |
| [§8.6](#86-correct-the-system-data-types-record) | **Correcting** it |
| [§8.7](#87-default-uncertain-system-data-types-record-fields) | **Defaulting** uncertain fields / barring quiet lowering |

<a id="81-own-the-system-data-types-record"></a>
**8.1. Own the System Data Types Record.**

*System Data Types Record duty:* keep one accountable owner for the file so System Alignment Certification always has a responsible party to verify against — forum supervision does not absorb that ownership.

The **operator** stays responsible for a correct System Data Types Record:

- even when work is delegated, automated, or done by a third party
- even when a forum is supervising certification

The operator (or other responsible party) must:

- identify data types materially in scope under Part B
- state handling, separation, lifecycle, and attribution posture
- justify ambiguous or multi-type findings **in the System Data Types Record**

Forum verification under Chapter Seven §4 does **not** transfer ownership of the System Data Types Record away from the operator.

<a id="82-disclose-the-system-data-types-record"></a>
**8.2. Disclose the System Data Types Record.**

*System Data Types Record duty:* publish a usable view of the file so oversight and System Alignment Certification can inspect typing honestly — when SAC runs, that view is what **[Part B §12](../core_07_b_system_alignment_certification_record_process.md#12-transparency-auditability-and-contestability)** reconstructability rests on.

- Do **not** hide, scatter, or cherry-pick the System Data Types Record so sentients cannot understand it
- Disclose the record (or an equivalent public view of it) to affected sentients:
  - at a depth that matches **system impact** and applicable access-posture bands
  - reachable without expert tools or heroic effort

**For Class A, B, and C**, disclosure of the System Data Types Record must also meet:

- [Public Oversight Baseline Disclosure](../core_05_band_oversight.md#public-oversight-baseline-disclosure) under the **Type O** default in [§7](#7-type-o-baseline-for-class-abc-systems)
- the strongest feasible **Type O** public substitutes when protected (non-**Type O**) classifications block raw disclosure

<a id="83-audit-the-system-data-types-record"></a>
**8.3. Audit the System Data Types Record.**

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Read with: **[CJS-3.3 audit process home](../corpus_joint_structure/cjs_03_audit_process.md#cjs-33-audit-process-home)** (*shared process — what / why / how / when*); **[CJS-3.4](../corpus_joint_structure/cjs_03o_oversight_operations.md#cjs-34-audit-process-output-disclosure)** (*access tiers and output disclosure*); **CJS-3.5** (*claim checking*); **[CS-3 — System classification and handling](cs_03_a_system_classification_machinery.md)** (*class scaling*).
- This subsection does **not** relocate the process home or Rights Floor (**Article XV** / **Article XV-A**).

</details>

<br>

*System Data Types Record duty:* this subsection owns the **System Data Types Record audit** sibling mode named in the **[CJS-3.3 audit process home](../corpus_joint_structure/cjs_03_audit_process.md#cjs-33-sibling-modes)** — an independent check that the type-and-handling file matches real data behavior, so System Alignment Certification under **[Chapter Seven §4](../core_07_a_system_alignment_certification_evaluation.md#4-data-types-and-handling-evaluation)** verifies substance when SAC runs, and so typing honesty stays checkable between and beside those cycles.

- **Required:** Auditability of the System Data Types Record is required under [§1](#1-purpose-and-scope).
- **What to verify:** Inspect real datasets, pipelines, access controls, and effects — not only claims in the file.
- **When:** On a schedule that matches impact and how fast data uses change, including the triggers in the process home and in [§5.2](#52-reclassification-and-lifecycle-governance) / [§8.5](#85-update-the-system-data-types-record).
- **For Class A, B, and C:** System Data Types Record audits must be able to catch mistyping, under-classification, unsafe linkage, and unreported behavior changes. Independent or third-party audit paths must remain available under **CJS-3.4**; "where feasible" does **not** make those paths soft-optional at these classes.

<a id="84-challenge-the-system-data-types-record"></a>
**8.4. Challenge the System Data Types Record.**

*System Data Types Record duty:* let affected sentients contest the file so type findings feeding System Alignment Certification stay challengeable under **Article XII-B** and, when inside an active certification record, under **[Part B §§12 and 14](../core_07_b_system_alignment_certification_record_process.md#12-transparency-auditability-and-contestability)**.

Systems must offer challenge routes sentients can actually use, review claims in good faith and on time, and give reasoned answers — including evidence of mistyping, hidden impact, unsafe linkage, or overdue re-evaluation, and requests for review or retyping of the record.

**For Class A, B, and C**, if an internal dispute about the System Data Types Record cannot be resolved, escalation to external or independent review must remain available.

When the challenge concerns typing assumptions, type assignment, or related evidence inside an active System Certification Record, the contestability chain in **[Chapter Seven Part B §12](../core_07_b_system_alignment_certification_record_process.md#12-transparency-auditability-and-contestability)** and **[§14](../core_07_b_system_alignment_certification_record_process.md#14-supervisory-sequence-and-contestability-chain)** applies, and material challenges may reopen review under **[Part B §16](../core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion)**.

<a id="85-update-the-system-data-types-record"></a>
**8.5. Update the System Data Types Record.**

*System Data Types Record duty:* revise the file when types, uses, or risks change — and keep the re-evaluation cadence stated on it current — so each System Alignment Certification or revalidation cycle under **[Chapter Seven §4](../core_07_a_system_alignment_certification_evaluation.md#4-data-types-and-handling-evaluation)** can verify honest typing.

What triggers a retype, and how protections must be preserved, live in [§5.2](#52-reclassification-and-lifecycle-governance). This subsection owns **when** operators must update the System Data Types Record:

- **before** rolling out materially bigger data uses or linkages, **where feasible**
- **promptly** once changed conditions are recognized
- as part of **periodic review**, including each materially impactful [System Alignment Certification](../core_05_band_continuity.md#system-alignment-certification-constitutional) or revalidation cycle under **[Chapter Seven §4](../core_07_a_system_alignment_certification_evaluation.md#4-data-types-and-handling-evaluation)**

The System Data Types Record must state a **re-evaluation cadence scaled to class** (and monitoring triggers). On each materially impactful SAC or revalidation cycle, certification must **verify** that reassessment under [§5.2](#52-reclassification-and-lifecycle-governance) was applied where triggers fired, and record the System Data Types Record under **[Part B §11.1](../core_07_b_system_alignment_certification_record_process.md#111-minimum-record-contents)**.

Failure to update the System Data Types Record after material change is non-compliance and a **certification defect** under [§5.2](#52-reclassification-and-lifecycle-governance), Chapter Seven §4, and **[Part B §16](../core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion)**.

<a id="86-correct-the-system-data-types-record"></a>
**8.6. Correct the System Data Types Record.**

*System Data Types Record duty:* correct the file when mistyping or evasion is found.

Shared correction, precautionary-default, and no-quiet-lowering discipline live in **[CJS-3.15 — Material classification-record honesty](../corpus_joint_structure/cjs_03a_accountability_operations.md#cjs-315-material-classification-record-honesty)**. This subsection applies that discipline to the System Data Types Record:

- do **not** fragment, re-label, or route data just to dodge a stronger type on the System Data Types Record ([§4](#4-anti-circumvention-and-integrity-of-classification))
- when mistyping or evasion is found, **correct** the System Data Types Record
- do **not** treat Charter text, vendor attestation, or self-description as the corrected file

How those failures count as **certification defects** live under **[Chapter Seven §4](../core_07_a_system_alignment_certification_evaluation.md#4-data-types-and-handling-evaluation)**, **[Part B §16](../core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion)**, and the [§8 SAC bridge](#8-system-data-types-record-governance).

<a id="87-default-uncertain-system-data-types-record-fields"></a>
**8.7. Default uncertain System Data Types Record fields.**

*System Data Types Record duty:* when the file is incomplete or contested, apply the precautionary default and state any precautionary typing relied on — do not quietly weaken protections.

Shared discipline lives in **[CJS-3.15 — Material classification-record honesty](../corpus_joint_structure/cjs_03a_accountability_operations.md#cjs-315-material-classification-record-honesty)**. CS-2 keeps the strongest applicable protections under [§2](#2-determination-of-classification)–[§4](#4-anti-circumvention-and-integrity-of-classification). This subsection applies them to the System Data Types Record:

- State any **precautionary typing** relied on, and any conditions pending resolution, **in the System Data Types Record**.
- **Lowering** typing protections on the System Data Types Record requires evidence, documentation, and successful review under the CJS-3.15 rule. Passing an internal check alone does **not** defeat a timely contest. Where recognition or continued reliance already rests on a System Certification Record, material requests also route through **[Part B §16](../core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion)**.

---

**Previous file:** [cs_01_scope_purpose_identifier_rules.md](cs_01_scope_purpose_identifier_rules.md)

**Next file:** [cs_02_b_data_classifications.md](cs_02_b_data_classifications.md)
