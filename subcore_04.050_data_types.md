<a id="subcore-4-a-data-types"></a>
# SUBCORE 4-A: DATA TYPES
<details>
<summary><strong><span style="color: #2563eb;">Corpus placement (non-operative): file structure and reading rules</span></strong></summary>

> This file is **part of the Sentient Constitution**: a [subcore](subcore_03.080_band_integrative.md#subcore) file attached to [Chapter Four](core_04.000_rights_part_a.md#chapter-four-foundational-rights), with the same force as that chapter, binding only together with the numbered `core_*` files and the rest of the subcore read as one text. It is **Subcore 4-A**. Until 2026-11-20 its text was implementation text in the systems corpus: §§1–7 were sections 1 to 7 of CS-4.305 (*Information types and handling*), and §8 was section 9 of CS-4.310 (*Data Classifications*).
>
> **Upstream:** [Chapter Four](core_04.000_rights_part_a.md#chapter-four-foundational-rights), the chapter this file is attached to.
> **Downstream:** [CS-4.305](corpus_systems/cs_04.305_information_types_and_handling.md) (*Information types and handling*: the System Data Types Record and its governance).

</details>

<br>

Subcore 4-A is the constitutional owner of **data types**: how data is typed, the rule that the most restrictive applicable type governs, anti-circumvention, the access-posture bands, cross-domain governance, separation and attribution, the Type O public baseline, and the data types themselves (**Type E**, **G**, **O**, **H**, **I**, **N**, **S**, **Y**, **W**, **U**, and **T**). The procedures for recording, disclosing, auditing, and challenging a system's data types stay in the systems corpus.

*In plain terms: this is where the Constitution says what kinds of data there are and how each kind must be handled. Every material dataset gets a type, and the type sets who may see it and how it must be protected.*

---

**Introductory provisions:**

*In plain terms: tell the truth in public where you can, but keep safeguards that protect sentients, privacy, trust, and system integrity — and make those safeguards stronger when impact is higher.*

Systems must preserve the practical ability to publish truthful information while maintaining safeguards for harm prevention, privacy, trust, and system integrity.

Requirements and limitations scale proportionally with system classification and potential impact. They must impose proportionate safeguards on publication within their boundaries where necessary to preserve trust, safety, and constitutional compliance.

### 1. Purpose, Role, and Scope

*In plain terms: Chapter Four Rights Floors need trustworthy data handling. This Subcore sets rules for typing, access, integrity, identity self-ownership, and Class A/B/C continuity.*

**Sentient Constitution Chapter Four** (Articles **I**–**XXIX**, presented in **Chapter Four Parts A–E**) states Foundational Rights that depend on strong, reproducible data handling — including info-sphere, audit, and comprehensibility duties (e.g., **Articles XVI**, **XVII**, and **XXIV**). this Subcore implement those duties in the systems layer.

<a id="privacy-owner-link"></a>
**Privacy:** This Subcore is also the systems-layer rulebook for the [**Def.C3** (*Privacy (Informational)* — peer-level cluster head)](subcore_03.075_band_continuity.md#defc3-privacy-informational--peer-level-cluster-head) privacy cluster:
- [Privacy (Informational)](subcore_03.075_band_continuity.md#privacy-informational)
- [Protected Internal-State Boundary](subcore_03.075_band_continuity.md#protected-internal-state-boundary)
- [Identity Data Protection](subcore_03.075_band_continuity.md#identity-data-protection)
- [Surveillance Boundary](subcore_03.075_band_continuity.md#surveillance-boundary)

It also carries out the collection, retention, and use disciplines in [Chapter Two §13.2.3 Privacy and Informational Self-Determination](core_02.020_interaction_interpretation.md#1323-privacy-and-informational-self-determination). Those homes own meaning. Types, access defaults, and handling rules here carry them out and may not be read to narrow them. Each restricted or non-accessible type names its privacy homes in [§8 Data Classifications](#privacy-link).

This Subcore implements:

- **How data is typed**
  - **Data typing** — every material dataset is assigned one or more types defined in **[§8 Data Classifications](#8-data-classifications)** (**Type E**, **G**, **O**, **H**, **I**, **N**, **S**, **Y**, **W**, **U**, and **T**)
  - **Most-restrictive rule** — where more than one type applies, the strongest applicable protections govern ([§2](#most-restrictive-applicable-classification-governs) *When it is unclear*), subject to proportionality (**CJS-3.125 §11** (*distributed and proportional authority terms*) and **CJS-3.120 §7** (*quorum and participatory legitimacy terms*))
  - **Classification integrity** — type follows the **functional nature of the data** and the **effects it enables**, not format, origin, or pipeline stage; systems may not evade typing by fragmentation, re-labeling, or indirection ([§2 Determination of Classification](#2-determination-of-classification)–[§4 Anti-Circumvention and Integrity of Classification](#4-anti-circumvention-and-integrity-of-classification))
  - **Class scaling** — higher-impact systems get stricter data rules. How strict depends on the system's class under **CS-8.305** (*System classification machinery*) and **Subcore 8-A** (*System Classification*)
- **Who may see each type**
  - **Default access posture** — each type belongs to one of six **access-posture bands** defined in **[§8 Data Classifications](#8-data-classifications)** (*open / accessible by default*; *audit-accessible, not public*; *restricted by default*; *non-accessible by default*; *public by creator release*; *licensed or assigned*), plus type-specific disclosure, consent, and handling rules. Bands group shared defaults; they are **not** a ranked sensitivity score
  - **Type O public-baseline (Class A/B/C)** — for high-impact systems, [Public Oversight Baseline Disclosure](subcore_03.085_band_oversight.md#public-oversight-baseline-disclosure) must be released by default as **Type O** data defined in **[§8.3 Type O](#83-type-o-open-public-oversight-baseline-disclosure-data)**, with substitute and holding-back limits in [§7 Type O Baseline for Class A/B/C Systems](#7-type-o-baseline-for-class-abc-systems)
  - **Type O certification data (all classes)** — the published content of every System Certification Record and Institutional Certification Record is **Type O**, whatever the system class, under the same substitute and holding-back limits ([§7 Type O Baseline for Class A/B/C Systems](#7-type-o-baseline-for-class-abc-systems))
- **Sentients' control over their own data**
  - **Identity self-ownership** — identity and attribution data remain under sentient control through revocation, rotation, correction, and recoverability ([§1.1 Identity self-ownership and recoverability](#11-identity-self-ownership-and-recoverability); **Article VII** (*Self-Ownership*))
  - **Collection notice and deletion** — every system that collects data about sentients must disclose what it collects, why, and how to delete it, and must honor deletion requests except on narrow, disclosed grounds ([§1.3 Collection notice and deletion](#13-collection-notice-and-deletion); **Article II-E** (*Data Handling and Network Dependency*))
  - **Continuity and exit** — for **Class A**, **Class B**, and **Class C** systems, sentients must be able to take their continuity-critical data with them when a service ends or changes hands ([§1.2 Continuity-critical collection and exportability](#12-continuity-critical-collection-and-exportability); **Article II-E** (*Data Handling and Network Dependency*); **Article II-F** (*Continuity and Operator Shutdown*)), and the formats and interfaces used for that handoff must meet **CJS-3.130 §17** (*interoperability, portability, and exit-integrity terms*)
- **How typed data is governed**
  - **Cross-domain governance** ([§5 Cross-Domain Governance Principles](#5-cross-domain-governance-principles)):
    - **Proportional access:** [§5.1 Proportional access and handling](#51-proportional-access-and-handling)
    - **Reclassification and lifecycle:** [§5.2 Reclassification and lifecycle governance](#52-reclassification-and-lifecycle-governance)
    - **Transparency levels and audit:** [§5.3 Transparency levels and audit access](#53-transparency-levels-and-audit-access)
    - **Transformation traceability:** [§5.4 Integrity of data handling and transformation](#54-integrity-of-data-handling-and-transformation)
    - **Attribution:** [§5.5 Accountability and attribution in data use](#55-accountability-and-attribution-in-data-use)
    - **Retention:** [§5.6 Proportional attribution and retention](#56-proportional-attribution-and-retention)
    - **Typing integrity and anti-evasion:** these remain in [§2 Determination of Classification](#2-determination-of-classification)–[§4 Anti-Circumvention and Integrity of Classification](#4-anti-circumvention-and-integrity-of-classification)
  - **Separation and attribution** — keep higher-sensitivity domains from leaking through linkage or inference, and preserve attributable action ([§6 Data Separation and Attribution](#6-data-separation-and-attribution))
  - **System Data Types Record** — for every system with **material impact**, operators must maintain a [System Data Types Record](subcore_03.075_band_continuity.md#system-data-types-record) stating types in scope, handling posture, and re-evaluation status.
    - **Audited information:** That System Data Types Record is **material audited information**: auditing processes require it, and System Data Types Record audits check it between and beside [System Alignment Certification](subcore_03.075_band_continuity.md#system-alignment-certification) cycles ([§8 System Data Types Record Governance](corpus_systems/cs_04.305_information_types_and_handling.md#cs-4305-8-system-data-types-record-governance)).
    - **Certification bridge:** When System Alignment Certification runs, **[Chapter Eight §4.4 Data Types and Handling Evaluation](core_08.000_system_alignment_certification_evaluation.md#44-data-types-and-handling-evaluation)** must produce or verify the System Data Types Record and include it in the [System Certification Record](subcore_03.075_band_continuity.md#system-certification-record) under **[Chapter Ten §3.1 Minimum Record Contents](core_10.000_system_alignment_certification_records_recertification.md#31-minimum-record-contents)**

<a id="11-identity-self-ownership-and-recoverability"></a>

**1.1. Identity self-ownership and recoverability.**

*In plain terms: your identity data is yours to control — systems must let you revoke, replace, and correct credentials, and must not trap you forever in a broken or compromised identity.*

This subsection is foundational to how typed data is handled under this Subcore and to self-ownership of identity and attribution data under **Article VII** (*Self-Ownership*), including **Article VII-A** (*Self-Ownership of Body*).

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

This subsection is foundational to continuity and exit under this Subcore. It implements:
- **Article II-E** (*Data Handling and Network Dependency*) and **Article II-F** (*Continuity and Operator Shutdown*)
- **Article XXII-A** (*Portability Rights*)
- **CJS-3.130 §17** (*interoperability, portability, and exit-integrity terms*)

For **Class A**, **Class B**, and **Class C** systems, operators must **not** collect or retain continuity-critical sentient data in forms that cannot be exported, migrated, or transferred under disclosed continuity and export paths, except where **Necessity** requires:
- confidentiality
- security
- **Type N** or comparable protected-boundary constraints
- lawful non-disclosure

Where export is limited, operators must disclose before a materially binding commitment:
- the **limitation**
- the **scope** of the limitation
- any lawful **substitute export path**

Shutdown, migration, operator exit, and service-end paths must:
- preserve usable **export or handoff** of continuity-critical data under those disclosed paths
- **not** rely on a discretionary promise to try later

<a id="13-collection-notice-and-deletion"></a>

**1.3. Collection notice and deletion.**

*In plain terms: every system that collects data about sentients must say what it collects, why, who gets it, and how long it is kept — and must actually delete that data when asked, except for narrow, disclosed reasons to keep it.*

This subsection implements:
- **Article II-E** (*Data Handling and Network Dependency*)
- **Article IX-B** (*Experiential and Derived Data Rights*)
- **CJS-3.130 §18** (*data-retention and lifecycle-integrity terms*)

It applies to **every** system that collects, infers, or transmits data about sentients, regardless of system class. Depth scales with **system impact** and the access-posture band of the data ([§5.0 Access-posture bands](#50-access-posture-bands)).

**Collection notice:** Before collection begins, operators must tell affected sentients, in a form reachable without expert tools:
- the **data types** collected or inferred, using the types in **[§8 Data Classifications](#8-data-classifications)** and consistent with the [System Data Types Record](corpus_systems/cs_04.305_information_types_and_handling.md#cs-4305-8-system-data-types-record-governance) where one is required
- the **purpose** of each type, and that the data will not be used beyond it ([§5.2 Reclassification and lifecycle governance](#52-reclassification-and-lifecycle-governance))
- **recipients**, including processors and other systems the data is linked to
- the **retention period** or the rule that sets it
- how to **see** the data and how to **request deletion**

A new purpose or recipient requires updated notice before the data is used that way, and new consent where the type requires it.

**Deletion on request:** Operators must:
- give sentients a deletion path at least as easy to use as the path used to collect the data
- verify the requester with no more **Type I** data than the request needs
- delete the data, and data derived or inferred from it, within a disclosed period, including backups within a disclosed backup cycle
- pass the request to every recipient and processor, and record that they did so
- confirm to the sentient what was deleted and what was kept

Hiding, flagging, suspending, or re-labeling data while it stays usable is **not** deletion. Where deletion is not technically feasible, the data must be irreversibly de-identified or aggregated under **CJS-3.130 §18** (*Continuity: Data-Retention and Lifecycle-Integrity Terms*).

**Grounds for keeping data:** An operator may refuse or limit deletion only where **Necessity** requires, for:
- evidence preservation, audit, or a lawful hold — including **Type S** data under an authorized investigation
- another sentient's rights in the same data under **Article IX-B** (*Experiential and Derived Data Rights*)
- official records the Constitution requires, including Act Records, Standing Records, attribution records under [§6.3 Attribution and accountability requirements](#63-attribution-and-accountability-requirements), and **Type O** public oversight data where [§7 Type O Baseline for Class A/B/C Systems](#7-type-o-baseline-for-class-abc-systems) requires it
- preservation duties under **Article XXIX-A** (*preservation over deletion for possible sentients*)
- functionality the sentient still wants, kept only with their ongoing consent — a deletion request withdraws that consent for the data it covers

Each refusal must state its basis, what is kept, and for how long. Kept data must be limited to what the refusal requires and must not be used for anything else. Refusals are challengeable under **Article XIV-A** (*Reliability and Trustworthiness Baseline*).

### 2. Determination of Classification

*In plain terms: type data by what it does and enables — not by format or pipeline stage. When unsure, protect more; weaken protection only with a documented justification; and do not dodge typing by rearranging the same outcome.*

**What counts.** Type the data by **what it is for** and **what it lets someone do** — not by file format, where it came from, or which step of a pipeline it sits in. The same rule applies when retyping data later.

<a id="most-restrictive-applicable-classification-governs"></a>
**When it is unclear.** If more than one type could fit, the **most protective** applicable protections govern. Use the most protective type that still fits, scaled to impact under:
- **CJS-3.125 §11** (*distributed and proportional authority terms*)
- **CJS-3.120 §7** (*quorum and participatory legitimacy terms*)

Weaker protection is allowed only with a **justified, documented override** under **CJS-3.125 §12** (*burden-of-justification and constraint terms*). Systems must **not** selectively apply less restrictive classifications to enable access, processing, or disclosure that would otherwise be prohibited.

If pieces of data can be rebuilt, transformed, or combined into something more sensitive, treat them under that **more sensitive** type. This applies the [Chapter Two §15.1.2 Derived-Information Principle](core_02.030_constitutional_interpretation.md#1512-derived-information-principle).

**Same outcome, same type.** If two arrangements work the same way in practice, they get the same classification. Typing decisions and material changes must stay:
- **transparent** (**CJS-3.120 §10** (*disclosure sufficiency and observability terms*))
- **auditable** (**CJS-3.110 §3 (*Oversight: Auditability and Reconstructability Terms (Annex)*) and CJS-3.115 §3** (*Audit process home*))
- **open to challenge** (**CJS-3.125 §13** (*procedural integrity and adjudication terms*))

**Wrong typing is a violation.** Mislabeling data, arranging it to dodge the rules, or achieving the same harmful access through a different structure violates:
- **informational integrity** (**Article XVI** (*Info-Sphere Integrity*))
- auditability where evidence is implicated (**Article XVII-A** (*Auditability and Observable Evidence*))
- applicable rights under **Chapter Four, Articles VI through X**

### 3. Temporal, Systemic, and Dependency Scope of Rights

*In plain terms: protections cover delayed, stacked, and indirect harm too — including harm passed through other systems. You cannot push risk onto other sentients, times, or systems to dodge the rules.*

Data-handling protections under this Subcore apply not only to immediate and direct system effects. They also apply to delayed, cumulative, and indirect impacts arising through system interactions and dependency chains.

Where systems create or contribute to material risk to sentients, including through transitive dependencies, those risks fall within the scope of these protections. Systems must **not** externalize risk or harm across time, populations, or system boundaries. That prohibition includes layered or indirect dependencies. Those dependencies must not bypass, defer, or dilute the protections and constraints established in Sentient Constitution Chapters Two through Four.

### 4. Anti-Circumvention and Integrity of Classification

*In plain terms: you may not break, relabel, split, outsource, or pipeline data just to escape its type — and you may not use typing itself to block participation, hide risk, or shut down audit. Keep the strongest applicable protections, and document any de-anonymization.*

Data classification under this Subcore is binding across all systems, processes, and transformations. **No system may:**
- **shift** data between classifications without maintaining the protections required by the **most restrictive applicable** classification
- **fragment, transform, aggregate, or re-label** data to avoid classification while preserving equivalent functional access or effect
- **structure** data pipelines, processing stages, or system boundaries to bypass applicable classification requirements
- **distribute** processing across multiple systems, stages, agents, or time-separated operations to achieve outcomes that would be prohibited if performed within a single system
- **rely** on intermediate systems, agents, or third parties to perform actions that would be prohibited if performed directly
- **de-anonymize** anonymized data except under **CJS-3.125 §12** (*burden-of-justification and constraint terms*), with such actions **fully documented and auditable**
- **license, assign, or place under any commercial grant** data that is not a work eligible under [§8.13.1](#8131-what-can-be-granted) (*What Can Be Granted*), or use a grant to escape the audit, accessibility, or disclosure duties of any type
- **use** classification to **evade** constitutional requirements, **justify unnecessary** restriction of participation or access, **conceal** systemic risk or harm, or **create artificial barriers** to audit, verification, or accountability
- **treat** restricted source data (including **Type H**, **Type I**, **Type N**, **Type S**, **Type Y**, **Type U**, or **Type T**) as reclassified to **Type O** merely because a system is Class A/B/C or merely by copying that data, without meeting the substitute, reclassification, or release requirements in §7 (*Type O Baseline for Class A/B/C Systems*) and [§8 Data Classifications](#8-data-classifications)

### 5. Cross-Domain Governance Principles

*In plain terms: these are the shared rules for how typed data is accessed, transformed, retyped, attributed, and retained across systems — stricter where impact is higher. Typing integrity and anti-evasion live in [§2 Determination of Classification](#2-determination-of-classification)–[§4 Anti-Circumvention and Integrity of Classification](#4-anti-circumvention-and-integrity-of-classification).*

All data, regardless of classification, must be handled in accordance with the following cross-domain principles. These principles govern how classifications are applied, enforced, and interacted with across systems, and ensure alignment with **Chapter Four, Articles I through X** and the operational clusters of the joint-structure family (cross-implementation terms, oversight, audit, participation, accountability, continuity, and integrative operations). Survival-, environment-, and substrate-critical data handling remains grounded in **Articles I–III and VI**; participation, oversight, and protected-boundary duties run through **Articles VI through X**.

The type sections in [§8 Data Classifications](#8-data-classifications) state type-specific defaults, definitions, and handling rules. They do **not** restate this cross-domain alignment unless a type needs an additional, type-specific pointer.

<a id="50-access-posture-bands"></a>

**5.0. Access-posture bands.**

*In plain terms: types share a default sharing style — open, audit-only, restricted, off-limits, public by the creator's choice, or licensed or assigned — so common rules can attach to that style. The letter codes are still not a least-to-most sensitive ranking.*

Each type belongs to one **access-posture band**. Bands define shared default access and restriction posture. They are **labels for shared defaults**, not a ranked list from “least sensitive” to “most sensitive.” Type-specific content and deltas are in **[§8 Data Classifications](#8-data-classifications)**.

| Band | Types | Shared default posture |
|---|---|---|
| **Open / accessible by default** | **Type O**, **Type E** | Strong presumption of openness or accessibility; hold-backs are narrow |
| **Audit-accessible, not public** | **Type G** | Fully auditable through structured or qualified audit access; not public by default; public face is [Public Oversight Baseline Disclosure](subcore_03.085_band_oversight.md#public-oversight-baseline-disclosure) (**Type O**) |
| **Restricted by default** | **Type H**, **Type I**, **Type S**, **Type Y** | Access only for defined legitimate purposes, consent, or justified override as the type requires; **Type S** is also time-bound and review-bound; **Type Y** release, reuse, and retention follow the creator's direction |
| **Non-accessible by default** | **Type N** | Access only through explicit, informed, freely given consent or justified override under **CJS-3.125 §12** (*burden-of-justification and constraint terms*) |
| **Public by creator release** | **Type W** | Open to view while the creator keeps it public; every other use needs the creator's consent; withdrawn or deleted on the creator's request |
| **Licensed or assigned** | **Type U**, **Type T** | Release scope and commercial use follow a recorded grant; uses the grant does not name need the consent of the creator (**Type U**) or rights-holder (**Type T**); the creator's reserved rights are never part of the grant |

**Band-level rules:**
- **Open / accessible by default:** Presumptive accessibility or open release applies. Restrictions that withhold otherwise-accessible or disclosable material must satisfy [§5.3 Transparency levels and audit access](#53-transparency-levels-and-audit-access). For **Type E**, restriction is permitted only when disclosure would **itself** create material risk of enabling targeted or disproportionate harm, exploitation, or system compromise, unless a narrower type-specific rule applies.
- **Audit-accessible, not public:** Non-public status must **not** function as unreviewable secrecy. Structured or qualified audit access must remain functionally effective under **CJS-3.110 §3 (*Oversight: Auditability and Reconstructability Terms (Annex)*) and CJS-3.115 §3** (*Audit process home*) and **CJS-3.110 §4** (*transparency levels and audit-access terms*). [Public Oversight Baseline Disclosure](subcore_03.085_band_oversight.md#public-oversight-baseline-disclosure) is **Type O**, not a substitute satisfied by audit access alone.
- **Restricted by default:** Collection, access, and use must stay limited to the justified purpose. Broader use requires consent or justified override as the applicable type states. **Type S** restrictions must remain time-bound and review-bound under [§5.3 Transparency levels and audit access](#53-transparency-levels-and-audit-access). Systems managing restricted-by-default data must **not**:
  - **expose** that data beyond what is necessary for its justified purpose
  - **create persistent tracking** across unrelated contexts **by default** — any cross-context aggregation or linkage requires explicit justification under **CJS-3.125 §11** (*distributed and proportional authority terms*) and **CJS-3.120 §7** (*quorum and participatory legitimacy terms*), including demonstration that it does **not** materially undermine autonomy or create **coercive power asymmetries**
- **Non-accessible by default:** Maximum restriction. No access, inference, reconstruction, or exposure without consent or justified override under **CJS-3.125 §12** (*burden-of-justification and constraint terms*).
- **Public by creator release:** Openness exists only by the creator's choice and only for viewing. The creator's withdrawal or deletion request is **not** a restriction subject to [§5.3 Transparency levels and audit access](#53-transparency-levels-and-audit-access), and systems must carry it out under [§8.9](#89-type-w-works-published) (*Type W: Works, Published*).
- **Licensed or assigned:** Commercial use by a licensee or rights-holder is lawful only within a grant recorded and made under [§8.13](#813-commercial-grants) (*Commercial Grants*). A grant binds the creator for its term, but never reaches the creator's reserved rights, and never lets data other than eligible works be sold or licensed through these types.

**Privacy discipline in the restricted and non-accessible bands.** [Chapter Two §13.2.3 Privacy and Informational Self-Determination](core_02.020_interaction_interpretation.md#1323-privacy-and-informational-self-determination) applies most directly to the **restricted by default** and **non-accessible by default** bands. Its disciplines are [Necessity](subcore_03.070_band_accountability.md#necessity), [Proportionality](subcore_03.070_band_accountability.md#proportionality), minimization, and [Consent](subcore_03.090_band_participation.md#consent) or other adequate authority. Band rules carry out those disciplines. They do not replace the [privacy homes](#privacy-link) named on each type.

**Protective storage and key custody.**

*In plain terms: restricted data stays encrypted wherever it is kept, is opened only inside the part of the system that needs it, and its keys go only to that part. The owner can still keep a plain copy of their own, and audit, export, and lawful-override routes keep working.*

Systems holding data in the **restricted by default** or **non-accessible by default** band must:
- keep it **encrypted in storage**, including backups, caches, logs, swap, and crash dumps
- **decrypt it only** inside the process or component that needs it for the justified purpose, and hold plaintext in memory no longer than that purpose requires, with memory isolation or protection proportionate to system class under CS-8.305 (*System classification machinery*) and Subcore 8-A (*System Classification*)
- **limit encryption keys** to the processes that need direct access to the data, enforced by the platform layer (operating system, hypervisor, runtime, or hardware) and kept separate from the data they protect
- keep **audit, export, and lawful-override** paths working through logged, authorized use of keys, not through bypass or undisclosed key escrow
- keep **each adopter's own** encryption keys and data stack, so that across adopters keys are not shared with, escrowed with, or made reachable by another adopter or a federation, and data moves between adopters only as answers under [Chapter Nineteen §3.4 Gatekeeper Checks Across Adopters and Levels of Trust](core_19.000_final_effect_restoration_enforcement.md#34-gatekeeper-checks-across-adopters-and-levels-of-trust) or, at the joint level, by a transfer re-encrypted under a key plan agreed before the transfer

These requirements have four limits:
- **Owner's own copy:** It does not require encrypting a copy the data's owner chooses to keep under their own control — the creator for **Type Y**, the sentient the data concerns for **Type H**, **Type I**, and **Type N**. That choice must meet the shared consent-integrity standard above, must not come from defaults or pressure, and cannot remove another party's protection in the same data (**Article IX-B** (*Experiential and Derived Data Rights*)). **Type S** has no owner exception.
- **Keys are protected material:** Keys and other cryptographic material that protect this data are handled as **Type S** under [§8.7](#87-type-s-safety-security-and-restricted-investigation-data) (*Type S: Safety, Security, and Restricted Investigation Data*) where that entry applies.
- **No lock-out:** Encryption, key rotation, and key loss must not defeat export under [§1.2 Continuity-critical collection and exportability](#12-continuity-critical-collection-and-exportability) or access-control integrity under [§5.3 Transparency levels and audit access](#53-transparency-levels-and-audit-access).
- **Key destruction and deletion:** Destroying the only keys to encrypted data counts as deletion only when it is irreversible and no copy of the keys survives. **Article II-E** (*Data Handling and Network Dependency*) still applies: hiding data is not deletion.

**Shared anti-abuse limits.** Across all types, systems must **not**:
- use data handling to enable **coercion, surveillance, or manipulation** (**Article VII-B** (*Self-Ownership of Mind*)), including consolidating power or control through data or identity dependency (**CJS-3.130 §17** (*interoperability, portability, and exit-integrity terms*))
- **restrict access** to participation, resources, or systems **without justified cause** (**CJS-3.125 §12** (*burden-of-justification and constraint terms*))

**Shared consent integrity.** Where access, use, or disclosure depends on consent, systems must treat consent as:
- **explicit and informed**
- freely given without coercion, manipulation, or deceptive framing (**Article VII-B** (*Self-Ownership of Mind*))
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
- any **minimization, isolation, challenge, or deletion** controls required by **Article XV-A** (*Security, Intelligence, and Covert-Power Limits*) or **CJS-3.125 §12** (*burden-of-justification and constraint terms*)

**Type H and Type I anti-capture limits.** In addition to the restricted-by-default band rules, systems managing **Type H** or **Type I** data must **not**:
- **centralize** that data in a manner that creates systemic control or dependency
- create, through security, intelligence, screening, or covert-investigation systems, any of the following absent a specifically justified and independently reviewable basis consistent with **Article XV-A** (*Security, Intelligence, and Covert-Power Limits*) and the stricter applicable protections in this section:
  - generalized **watchlisting**
  - persistent **cross-context tracking**
  - hidden **political, associational, or belief-linked profiling**

Where more than one type applies, the **most-restrictive** applicable protections govern ([§2 Determination of Classification](#2-determination-of-classification)). Band membership does **not** displace **Type O** publication duties or **Type E** survival-coordination duties.

<a id="onward-transfer-of-type-h-and-type-i-data"></a>
**Onward transfer of Type H and Type I data.**

*In plain terms: your address, phone number, purchase history, and activity trail may be passed on only to serve you, and whoever receives them may not keep them, pass them on, or sell them. No one may sell this data, buy it for resale, or build a stock of it about sentients for others to use, and your consent cannot waive that. It does not pass to a buyer when a business is sold or goes under. The rule cannot reach actors outside the adopters or take back data already released, so the lasting protection is keeping a public contact point apart from private ones, and systems must support that.*

This rule applies to **core personal data**: the Type I contact and location information and persistent device and advertising identifiers named in [§8.5 Type I: Identity and Attribution Data](#85-type-i-identity-and-attribution-data), and the Type H purchase, payment, browsing, search, reading, viewing, listening, location, movement, contact-list, social-graph, and device and app histories, and the inferences, scores, classifications, and audience segments derived from them, named in [§8.4 Type H: Historical, Relational, Transactional, and Participation Data](#84-type-h-historical-relational-transactional-and-participation-data). It applies wherever the data came from, including public records, directories, scraping, and earlier publication ([§2 Determination of Classification](#2-determination-of-classification), [§4 Anti-Circumvention and Integrity of Classification](#4-anti-circumvention-and-integrity-of-classification)).

- **No sale or trade:** No holder may sell, license, trade, or exchange core personal data for money, services, or any other value. [§8.13.1 What Can Be Granted](#8131-what-can-be-granted) already keeps it out of a commercial grant. This rule closes every other route to sale.
- **No acquisition for resale or compilation:** No system may acquire, collect, or hold core personal data about sentients in order to sell, license, or disclose it onward, or to compile it into a stock or profile for others to use. That is data brokerage, and it is barred whatever the source of the data.
- **No transfer as an asset:** Core personal data does not pass as a business asset. A merger, acquisition, reorganization, sale of a business, or insolvency sale does not move it to the successor or buyer. A successor may keep what it needs to keep serving a sentient who stays with it, after notice and a fair chance to leave and have the data deleted. Everything else is deleted or returned to the sentient. A successor that takes data without this takes it under every limit that bound the seller.
- **Disclosure to serve the sentient:** A holder may disclose core personal data to another party only as far as needed to serve the sentient, at the sentient's direction or with consent that meets the shared consent-integrity standard above, and for a purpose named when it is given. A courier receives the delivery address. A payment processor receives payment details. The recipient:
  - uses it only for that purpose;
  - keeps it no longer than the purpose needs; and
  - may not pass it on, sell it, or use it to build a profile.
- **Consent does not waive the sale and compilation bars:** Consent can authorize disclosure to serve the sentient. It cannot authorize sale, trade, acquisition for resale, or compilation. Consent given in a bundle, under pressure, or as the price of a service is how brokers are supplied.
- **A sentient's own disclosure:** A sentient may share its own core personal data with a recipient it names, for a purpose it names. It may not sell the data to a party that will hold it for resale or compilation. It may be paid for taking part in research or a panel under the disclosure terms above. The payment is for taking part and not for the data.
- **Standing aggregators are barred, a sentient's own data is not:** A credit bureau, screening service, or similar party that holds records about sentients it does not serve, in order to report them to others, is practicing data brokerage. A sentient may direct its own payment history, identity details, or other core personal data to a lender, landlord, employer, insurer, or other party it names, for the decision it names. That party may ask only for what the decision needs and handles the data under the disclosure terms above.
- **Fraud-signal sharing:** Holders may share an indicator of fraud or abuse with one another only where all of these hold:
  - the fraud or abuse has been confirmed, and the indicator is not a suspicion, score, or profile;
  - it is limited to what identifies the conduct, such as the account, device, or credential used, and carries no wider history or contact information about the sentient;
  - it is used only to stop that fraud or abuse;
  - the participants are named in a published arrangement that is open to independent review;
  - the sentient it concerns is told, may contest it, and has a wrong indicator removed;
  - it expires; and
  - it is never the only ground for denying Rights-Floor access, and access to the shared set is never sold.
- **No workaround:** Intermediaries, affiliates, subsidiaries, and data that has been de-identified but can be re-identified do not escape this rule ([§4 Anti-Circumvention and Integrity of Classification](#4-anti-circumvention-and-integrity-of-classification); the [Chapter Two §15.1.2 Derived-Information Principle](core_02.030_constitutional_interpretation.md#1512-derived-information-principle)).
- **Aggregates:** Statistics and counts with no identified sentient or persistent identifier behind them are not core personal data, and this rule does not bar them. Data that can be re-identified is not an aggregate.
- **What it does not bar:** Disclosure to a forum, auditor, or authority under a justified, documented override under **CJS-3.125 §12** (*burden-of-justification and constraint terms*), and the handling each type already allows for its own justified purpose. An override never authorizes sale or compilation for onward private use.
- **Limits of this rule:** It binds adopters and the systems within their reach. It cannot recall data already released, and it cannot reach actors outside the adopters. The most dependable protection is a sentient's own practice of keeping a public contact point, which may be listed, and separate private contact points given only to those it chooses. Systems must support that practice under [§8.5](#85-type-i-identity-and-attribution-data) (*Public and private contact points*).

<a id="51-proportional-access-and-handling"></a>

**5.1. Proportional access and handling.**

*In plain terms: bigger impact means stricter access, more transparency, deeper audit, and stronger justification — you cannot claim light rules while causing heavy outside effects. When access is allowed or required, it must arrive in time to be useful.*

Access and handling must scale with:
- **impact on sentients, the environment, and the info-sphere**
- stakeholder dependency
- potential for harm, including irreversibility

Higher-impact systems and actions require:
- **greater transparency** (**CJS-3.120 §10** (*disclosure sufficiency and observability terms*))
- **deeper auditability** (**CJS-3.110 §3 (*Oversight: Auditability and Reconstructability Terms (Annex)*) and CJS-3.115 §3** (*Audit process home*))
- **stronger independent verification and claim integrity** (**CJS-3.110 §5** (*independent verification and claim-integrity terms*))
- **more comprehensible presentation** where affected stakeholders must understand or act on the data (**CJS-3.120 §8** (*comprehensibility and cognitive accessibility terms*))
- **stronger justification** for restriction or access (**CJS-3.125 §12** (*burden-of-justification and constraint terms*))

Where access is **required or permitted** under the applicable type, it must be **timely enough for the lawful purpose**. That duty scales with impact under **CJS-3.125 §11** (*distributed and proportional authority terms*) and **CJS-3.120 §7** (*quorum and participatory legitimacy terms*). It does **not** create a duty of public availability for types that are restricted or non-accessible by default.

Where a type requires accessibility, disclosure, or audit access, systems must also:
- **preserve sufficient fidelity** for audit, lawful response, and long-term stewardship, proportionate to impact and dependency
- **not** aggregate, downsample, or reduce resolution in ways that **materially obscure** trends, risks, or localized impacts that affected stakeholders are entitled to see under that type

**No** system may claim reduced requirements while exerting **material external** effects under:
- **CJS-3.125 §11** (*distributed and proportional authority terms*)
- **CJS-3.120 §7** (*quorum and participatory legitimacy terms*)

<a id="52-reclassification-and-lifecycle-governance"></a>

**5.2. Reclassification and lifecycle governance.**

*In plain terms: types are not forever — reassess them when impact, use, or risk changes, keep the strongest protections unless justified, and do not hide behind an outdated label.*

Classification is **not** static. **Material** changes in any of the following must trigger reclassification:
- **system impact**
- **uses or contexts**
- **risks or capabilities**

All data must be:
- **re-evaluated** for appropriate classification (**CJS-3.130 §18** (*data-retention and lifecycle-integrity terms*)) on the certification schedule its system class sets — verified on each materially impactful system alignment certification or recertification cycle under **[Chapter Eight §4.4](core_08.000_system_alignment_certification_evaluation.md#44-data-types-and-handling-evaluation)** (*Data Types and Handling Evaluation*) and recorded in the [System Data Types Record](subcore_03.075_band_continuity.md#system-data-types-record) under **[Chapter Ten §3.1 Minimum Record Contents](core_10.000_system_alignment_certification_records_recertification.md#31-minimum-record-contents)** and [§8 System Data Types Record Governance](corpus_systems/cs_04.305_information_types_and_handling.md#cs-4305-8-system-data-types-record-governance)
- **reclassified** whenever necessary to maintain alignment with constitutional requirements
- **stored** in alignment with its classification, including **duration limits** proportional to purpose, risk, and stakeholder impact

Reclassification must:
- **preserve the highest applicable protections** unless reduced through **justified override** (**CJS-3.125 §12** (*burden-of-justification and constraint terms*))
- remain **transparent and documented** **in the System Data Types Record**
- stay **subject to audit and challenge**

**No** system may:
- **rely on outdated classification** to justify continued access or reduced protection
- **delay or avoid reclassification** where material changes in impact or use have occurred

This subsection owns **retype mechanics**. [§8 System Data Types Record Governance](corpus_systems/cs_04.305_information_types_and_handling.md#cs-4305-8-system-data-types-record-governance) owns **when** operators must update the System Data Types Record after those retypes.

<a id="53-transparency-levels-and-audit-access"></a>

**5.3. Transparency levels and audit access.**

*In plain terms: sentients need enough visibility to understand risk; auditors need deeper access when needed; and hiding system behavior behind access controls is not allowed.*

Data access must satisfy **CJS-3.110 §4** (*transparency levels and audit-access terms*) for balancing transparency, auditability, and protected-boundary constraints. Public-baseline transparency duties also run through [Transparency](subcore_03.085_band_oversight.md#transparency) and **Article XVII** (*Audit, Transparency, and Independent Verification*).

It must also balance protection of internal states and sensitive data (**Sentient Constitution Chapter Four, **Article VII-B** (*Self-Ownership of Mind*)**; Types **H**, **I**, **N**, and **S** in this section), including cross-implementation trust integrity under **CJS-30.110 §3** (*Cross-Implementation Trust Integrity (Joint Operation Model)*) where incorporated via **Chapter Thirty**. Where applicable based on system impact (**CJS-3.125 §11** (*distributed and proportional authority terms*) and **CJS-3.120 §7** (*quorum and participatory legitimacy terms*)), systems must support:

- **Identity Data Protection:** [Identity Data Protection](subcore_03.075_band_continuity.md#identity-data-protection) governs the restricted-linkages ban (Type H/I → Type N) in this subsection. See [§6.1 Separation of data domains](#61-separation-of-data-domains) for the domain-separation mechanics.
- **baseline accessibility** — sufficient visibility into behavior and effects for informed participation and risk evaluation
- **qualified audit access** — structured audit-access pathways for independent auditors to deeper data where verification requires it
- **forensic access** — full reconstruction in cases of harm, dispute, or credible risk, consistent with **CJS-3.125 §11** (*Accountability: Distributed and Proportional Authority Terms*), **CJS-3.120 §7** (*Participation: Quorum and Participatory Legitimacy Terms*), and **CJS-3.125 §12** (*burden-of-justification and constraint terms*)
- **access-control integrity** — access controls must **not** conceal systemic behavior, prevent accountability, or obstruct legitimate audit and verification

For **Class A**, **Class B**, and **Class C** systems, [Public Oversight Baseline Disclosure](subcore_03.085_band_oversight.md#public-oversight-baseline-disclosure) defined in **[§8.3 Type O](#83-type-o-open-public-oversight-baseline-disclosure-data)** is **public by default**, subject to the substitute and holding-back rules in [§7 Type O Baseline for Class A/B/C Systems](#7-type-o-baseline-for-class-abc-systems).

**Audit-process outputs.** Findings, reports, eligibility rules for deeper access, and related artifacts from material audit, verification, or independent review follow the **[CJS-3.115 §3 audit process home](corpus_joint_structure/cjs_03.115_audit_process.md#cjs-3115-3-audit-process-home-odef3)** and the disclosure preference in **[CJS-3.110 §4](corpus_joint_structure/cjs_03.110_oversight_operations.md#cjs-34-audit-process-output-disclosure)** (*transparency levels and audit-access terms*): **Type O** where feasible, then qualified **Type G** (or other non-public source) access, then forensic or more-restricted levels only as justified. This subsection owns the this Subcore typing and access-level mechanics those outputs use; it does not relocate audit-process ownership out of **CJS-3.110 §3 (*Oversight: Auditability and Reconstructability Terms (Annex)*) and CJS-3.115 §3** (*Audit process home*)–**CJS-3.110 §5** (*Oversight: Independent Verification and Claim-Integrity Terms*).

Any limit on who may see or use data must be:
- **narrow in scope** — only as broad as needed for the stated lawful purpose
- **justified** — with reasons that can be checked
- **auditable**
- **open to challenge** (**CJS-3.125 §13** (*procedural integrity and adjudication terms*))

Where the limit withholds information that would otherwise be accessible or disclosable under the applicable type, it must also be:
- **time-bound**
- **documented**, and subject to **delayed disclosure and audit** where delayed release is used
- shown to **reduce net harm** relative to fuller disclosure under **CJS-3.125 §11** (*distributed and proportional authority terms*) and **CJS-3.120 §7** (*quorum and participatory legitimacy terms*)
- shaped to preserve **maximum feasible** visibility into the **existence and character** of the risk, where public or baseline visibility applies

Where data mixes **Type E** coordination-relevant elements with **Type S** exploit-sensitive elements, systems must **disclose** the coordination-relevant components and **restrict only** exploit-enabling components unless separation is **not technically feasible**. If separation is not feasible, restriction must be **explicitly justified**, **minimized** in scope and duration, and **subject to post-release disclosure and audit**. Type-specific interaction rules are in [§8.7 Type S · Interaction with Type E](#type-s-interaction-with-type-e).

Where **Type S** restricts disclosure for safety, security, or protected investigation, the restriction must also satisfy **CJS-3.130 §21** (*adversarial robustness and abuse-resistance terms*) and **CJS-3.135 §22** (*constrained-secrecy and protected-investigation terms*), remain **time-bound** and **review-bound**, and stay open to challenge: a dispute about who may see the restricted item goes first to the restricted information authority (**CF-22.415 §10** (*Restricted Information Authority*)), and any other challenge goes under **CJS-3.125 §13** (*procedural integrity and adjudication terms*).

<a id="54-integrity-of-data-handling-and-transformation"></a>

**5.4. Integrity of data handling and transformation.**

*In plain terms: keep a usable trail of where data came from and what changed, so impact and dependencies can still be checked and material transformations can be reconstructed.*

All material handling, processing, and transformation must preserve:

- **traceability of origin and transformations**
- **the ability to evaluate impact and dependencies** (**CJS-3.130 §16** (*dependency integrity and disclosure terms*))
- **transparency, auditability, and reconstructability** where required (**CJS-3.120 §10** (*disclosure sufficiency and observability terms*); **CJS-3.110 §3 (*Oversight: Auditability and Reconstructability Terms (Annex)*) and CJS-3.115 §3** (*Audit process home*))

If a material transform changes what the data enables, how it can be used, or its sensitivity — including by rebuild, combination, or aggregation — the resulting data must be **re-evaluated and retyped** under [§2 Determination of Classification](#2-determination-of-classification) and [§5.2 Reclassification and lifecycle governance](#52-reclassification-and-lifecycle-governance), and that type change must remain on the same transparent, auditable trail.

Anti-degradation and anti-obscurity duties for classification integrity are stated in [§2 Determination of Classification](#2-determination-of-classification)–[§4 Anti-Circumvention and Integrity of Classification](#4-anti-circumvention-and-integrity-of-classification).

<a id="55-accountability-and-attribution-in-data-use"></a>

**5.5. Accountability and attribution in data use.**

*In plain terms: someone identifiable must be responsible for material data actions — handing the work off does not erase accountability.*

This subsection governs attribution of data access, processing, and transformation.

- Delegation of data handling does **not** eliminate accountability
- Responsibility must remain assignable through transparent, auditable processes
- Attribution must resist **tampering, repudiation, or ambiguity**

All data access, processing, and transformation must be:
- **attributable** to identifiable systems, agents, or sentients (**Chapter Four, **Article VII** (*Self-Ownership*)** — self-ownership and attributable representation where applicable)
- **recorded** in a manner sufficient for audit and reconstruction (**CJS-3.110 §3 (*Oversight: Auditability and Reconstructability Terms (Annex)*) and CJS-3.115 §3** (*Audit process home*))

Systems must ensure:
- **clear responsibility** for actions taken on data
- **traceability** of decisions and outcomes

<a id="56-proportional-attribution-and-retention"></a>

**5.6. Proportional attribution and retention.**

*In plain terms: you do not need forever-logs for everything, but you must keep enough attribution to investigate serious harm, dispute, or abuse.*

Attribution requirements do **not** imply universal or persistent logging of all actions.

Systems must provide attribution capability **proportional to system impact** sufficient to support [Attributable Action](subcore_03.070_band_accountability.md#attributable-action) and [Attribution Integrity](subcore_03.070_band_accountability.md#attribution-integrity) under:
- **CJS-3.125 §11** (*distributed and proportional authority terms*)
- **CJS-3.120 §7** (*quorum and participatory legitimacy terms*)

That capability may include:
- **short-lived** mechanisms — attribution that exists only long enough for the immediate purpose, then expires
- **event-triggered or conditional** logging
- **limited retention windows** under **CJS-3.130 §18** (*data-retention and lifecycle-integrity terms*)
- **aggregated or anonymized** records where appropriate
- retention and disposition scaled to **reversibility and containment** needs under **CJS-3.130 §20** (*reversibility and containment terms*)

**Low-impact** systems are **not** required to:
- **retain full historical logs of all actions**
- **maintain persistent identity linkage** beyond what is necessary for system integrity and participant safety

Systems must **not**:
- **eliminate attribution capability** where material harm, dispute, or abuse cannot be investigated
- **design retention policies** that prevent reasonable reconstruction of significant events when required

### 6. Data Separation and Attribution

*In plain terms: keep sensitive data domains from leaking into each other, and keep actions attributable. Identity self-ownership and continuity-critical export are foundational and live in [§1.1 Identity self-ownership and recoverability](#11-identity-self-ownership-and-recoverability)–[§1.2 Continuity-critical collection and exportability](#12-continuity-critical-collection-and-exportability).*

All systems must maintain clear separation between data classifications and ensure accountable attribution of actions. Identity self-ownership and continuity-critical export obligations are stated in [§1.1 Identity self-ownership and recoverability](#11-identity-self-ownership-and-recoverability) and [§1.2 Continuity-critical collection and exportability](#12-continuity-critical-collection-and-exportability).

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

are governed by [§2 Determination of Classification](#2-determination-of-classification), [§4 Anti-Circumvention and Integrity of Classification](#4-anti-circumvention-and-integrity-of-classification), and [§5.4 Integrity of data handling and transformation](#54-integrity-of-data-handling-and-transformation).

**Restricted linkages** are governed by [Identity Data Protection](subcore_03.075_band_continuity.md#identity-data-protection); this subsection applies the domain-separation mechanics above.

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
- **transparent** (CJS-3.120 §10 (*disclosure sufficiency and observability terms*))
- **auditable** (CJS-3.110 §3 (*Oversight: Auditability and Reconstructability Terms (Annex)*) and CJS-3.115 §3 (*Audit Process Home (oDef.3)*))
- **subject to revalidation** (CJS-3.130 §18 (*data-retention and lifecycle-integrity terms*))

<a id="63-attribution-and-accountability-requirements"></a>

**6.3. Attribution and accountability requirements.**

*In plain terms: actions that affect sentients or shared systems must be traceable to someone or something responsible. If impact grows — or value, identity, or resources start moving outside the system — reduced attribution must end and full attribution must take over.*

This subsection applies [Attribution Integrity](subcore_03.070_band_accountability.md#attribution-integrity) and [Attributable Action](subcore_03.070_band_accountability.md#attributable-action) to system actions that affect the outside world:

- **No** system may **obscure responsibility** through indirection, delegation, or system complexity ([Attribution Integrity](subcore_03.070_band_accountability.md#attribution-integrity))
- **No** system may **create conditions** where actions cannot be reliably attributed ([Attribution Integrity](subcore_03.070_band_accountability.md#attribution-integrity))
- Delegation of action does **not** eliminate accountability
- Responsibility must remain traceable through transparent, auditable attribution chains

**Attributable action scope and audit-resistance:**

- All actions affecting **sentients**, **shared infrastructure**, **resource systems**, or the **info-sphere** must satisfy [Attributable Action](subcore_03.070_band_accountability.md#attributable-action) through identifiable systems, agents, or sentients
- Attribution must satisfy [Attribution Integrity](subcore_03.070_band_accountability.md#attribution-integrity), including **auditability (CJS-3.110 §3 (*Oversight: Auditability and Reconstructability Terms (Annex)*) and CJS-3.115 §3 (*Audit Process Home (oDef.3)*))** and resistance to tampering, repudiation, or ambiguity

For personnel/agents exercising **Critical System Stewardship** or **material** operational authority, the inspectable attributable-action surface lives in **[CS-26.305 §10 inspectable attributable action](corpus_systems/cs_26.305_critical_system_stewardship.md#cs-26305-103-inspectable-attributable-action)** as the default logging contract for mixed crews. This subsection remains the system-action attribution home.

**Step-up to full attribution.** Where systems **increase in impact**, they must step up to **full attribution**. The same applies when they:
- **introduce persistent value, identity, or resource transfer**
- **affect external systems**

**No** system may continue under **reduced attribution** once it **exceeds low-impact thresholds**. Narrow reduced-attribution permission for creative and low-risk contexts is stated in [§6.4 Creative, expressive, and low-risk attribution exception](#64-creative-expressive-and-low-risk-attribution-exception).

<a id="64-creative-expressive-and-low-risk-attribution-exception"></a>

**6.4. Creative, expressive, and low-risk attribution exception.**

*In plain terms: low-risk creative spaces may hide who you are from other users — but only while audit-level accountability stays intact and impact stays low.*

Systems that do **not** exert **material external impact** under **CJS-3.125 §11** (*distributed and proportional authority terms*) and **CJS-3.120 §7** (*quorum and participatory legitimacy terms*) may permit **pseudonymous or abstracted** identity at the user-interaction level. That includes:
- reduced or intentionally obscured visibility of attribution to other participants
- **hidden roles**
- **deception mechanics**
- **identity concealment** as part of system design

**Permission** applies **only** where the system is designed primarily for **creative expression**, **entertainment**, **gaming**, **roleplay**, or **other low-risk, voluntary** environments.
It is permitted **only if** all of the following are true:
- **identity abstraction** is context-bound and does **not** produce **persistent or cross-system** attribution without **consent** or **justified override** under **CJS-3.125 §12** (*burden-of-justification and constraint terms*)
- the system does **not** materially affect **sentient reputation external to the system**
- the system does **not** materially affect **sentient survival or foundational resources** (**Articles I–III and VI**)
- the system does **not** materially affect **shared infrastructure stability**, **resource systems or external economic structures**, or **the integrity of the info-sphere**
- **system-level accountability** is preserved and all actions within the system remain attributable at an audit level consistent with:
  - [Attributable Action](subcore_03.070_band_accountability.md#attributable-action)
  - [Attribution Integrity](subcore_03.070_band_accountability.md#attribution-integrity)
  - system impact
  - **CJS-3.120 §10** (*disclosure sufficiency and observability terms*)
  - **CJS-3.110 §3 (*Oversight: Auditability and Reconstructability Terms (Annex)*) and CJS-3.115 §3** (*Audit process home*)
  - **CJS-3.110 §5** (*independent verification and claim-integrity terms*)
  - **CJS-3.125 §11** (*distributed and proportional authority terms*)
  - **CJS-3.120 §7** (*quorum and participatory legitimacy terms*)
- participants are **not** exposed to **non-consensual** harm, coercion, or manipulation

### 7. Type O Baseline for Class A/B/C Systems

*In plain terms: high-impact systems must publish [Public Oversight Baseline Disclosure](subcore_03.085_band_oversight.md#public-oversight-baseline-disclosure) as Type O by default — scoped to what the System Charter claims, what class the system is, and what the system actually does; checked each certification cycle. Where Type G, Type E, or other raw protected or non-baseline data cannot be released as that disclosure, publish the strongest feasible public substitute; and holding data back must be narrow and challengeable.*

For **Class A**, **Class B**, and **Class C** systems, [Public Oversight Baseline Disclosure](subcore_03.085_band_oversight.md#public-oversight-baseline-disclosure) — the **Type O** public-baseline content defined in **[§8.3 Type O](#83-type-o-open-public-oversight-baseline-disclosure-data)** — is **public by default** and must be released as **Type O**, subject to the substitute and holding-back rules below.

**Certification data, all classes.** The published content of every [System Certification Record](subcore_03.075_band_continuity.md#system-certification-record) and [Institutional Certification Record](subcore_03.075_band_continuity.md#institutional-certification-record) is **Type O**, whatever the system class, as [§8.3 Type O](#83-type-o-open-public-oversight-baseline-disclosure-data) defines it. The substitute and holding-back rules below apply to it as they do to the baseline. This does not extend the full Public Oversight Baseline Disclosure to Class L or Class P systems.

**Scope of the baseline.** What Public Oversight Baseline Disclosure must cover is **mapped from** the governing [System Charter](subcore_03.075_band_continuity.md#system-charter), the assigned system class under **CS-8.305 (*System classification machinery*) and Subcore 8-A** (*System Classification*), and observed [System Boundaries](subcore_03.075_band_continuity.md#system-boundaries). System Charter fields — purpose, in-scope and out-of-scope limits, affected communities and dependencies, and classification assumptions — are inputs to that coverage map; they are **not** the sole source of Type O content. Understated System Charter text, paper-only scope, or a missing System Charter where one is required must **not** shrink Type O publication duties. Sufficiency of Public Oversight Baseline Disclosure is verified on each materially impactful system alignment certification or recertification cycle under **[Chapter Eight §4.4 Data Types and Handling Evaluation](core_08.000_system_alignment_certification_evaluation.md#44-data-types-and-handling-evaluation)** (*Data Types and Handling Evaluation*) and recorded in the [System Data Types Record](subcore_03.075_band_continuity.md#system-data-types-record) under **[Chapter Ten §3 System Certification Record](core_10.000_system_alignment_certification_records_recertification.md#3-system-certification-record)** and [§8 CS-4.305 §8 System Data Types Record Governance](corpus_systems/cs_04.305_information_types_and_handling.md#cs-4305-8-system-data-types-record-governance).

**Substitutes for non-public or restricted source data.** If raw disclosure of **Type G**, **Type E**, or other protected source would harm privacy, identity, internal-state protection, safety, security, or an active restricted investigation, or if full release would exceed Public Oversight Baseline Disclosure, publish the strongest feasible **Type O** substitute instead — for example:
- aggregation
- de-identification
- summary or delayed disclosure

A de-identified, aggregate, or pooled substitute counts only where re-identification or reconstruction is not reasonably possible under [Derived Information](subcore_03.080_band_integrative.md#derived-information). The party relying on that label carries the showing. A substitute choice can trade privacy against [Public Oversight Baseline Disclosure](subcore_03.085_band_oversight.md#public-oversight-baseline-disclosure). Where it materially limits either one to serve the other, it is a Constitutional Collision. Resolve it on a [Constitutional Collision Record](subcore_03.080_band_integrative.md#constitutional-collision-record) under [Chapter Two §13.2.3 Privacy and Informational Self-Determination](core_02.020_interaction_interpretation.md#1323-privacy-and-informational-self-determination). Privacy is not automatically subordinate to transparency, and baseline disclosure is not dropped for convenience.

Keep the underlying official records under their original type unless lawfully reclassified. Where full public release is inappropriate, **structured or qualified audit access** to **Type G** or other non-public source must remain available in parallel under **CJS-3.110 §3 (*Oversight: Auditability and Reconstructability Terms (Annex)*) and CJS-3.115 §3** (*Audit process home*) and **CJS-3.110 §4** (*transparency levels and audit-access terms*), and must **not** replace [Public Oversight Baseline Disclosure](subcore_03.085_band_oversight.md#public-oversight-baseline-disclosure).

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

### 8. Data Classifications

*In plain terms: the letter codes are domain labels, not a ranked sensitivity scale. Types share access-posture bands so common rules can attach to the sharing style. When more than one type fits, the stronger protections win.*

These type letters name different kinds of data and how they are usually shared — not a ranked list from “least sensitive” to “most sensitive.” The letters are labels, not a score order. Each type carries its own protections, which do not rise or fall just because of where it sits in this list. When more than one type could apply, use the strongest applicable protections.

**Access-posture bands.** Types are grouped by **default access posture** so shared band rules in [§5.0 Access-posture bands](#50-access-posture-bands) apply once. Band order below is for reading clarity only — **not** a sensitivity ranking.

**Open / accessible by default** — strong presumption of openness or accessibility; hold-backs are narrow ([§5.0 Access-posture bands](#50-access-posture-bands)):
- **Type O** — Open public oversight baseline disclosure data: [Public Oversight Baseline Disclosure](subcore_03.085_band_oversight.md#public-oversight-baseline-disclosure) for oversight and contestability, including lawful substitutes where Type G, Type E, or other source stays non-public or non-baseline; open by default (strong presumption).
- **Type E** — Environmental, emergency, and survival-coordination data: environment, infrastructure, emergency, and other content streams needed to stay safe and coordinate harm prevention; accessible by default (strong presumption); published Public Oversight Baseline Disclosure artifacts drawn from it are Type O.

**Audit-accessible, not public** — fully auditable; not public by default; public face is Type O ([§5.0 Access-posture bands](#50-access-posture-bands)):
- **Type G** — Governance and operational source data: sensitive records of how systems are run, decided, risked, and challenged; fully auditable through structured or qualified audit access, but not public by default.

**Restricted by default** — purpose-limited access; consent or justified override as the type requires ([§5.0 Access-posture bands](#50-access-posture-bands)):
- **Type H** — Historical, relational, transactional, and participation data: logs of interactions, exchanges, and activity patterns; restricted by default.
- **Type I** — Identity and attribution data: who is who and who did what, for verification and accountability without unnecessary tracking; restricted by default.
- **Type S** — Safety, security, and restricted investigation data: temporary exploit-, investigation-, or compromise-sensitive material; restricted by default, time-bound, and review-bound.
- **Type Y** — Yours: writing, media, code, designs, and other works a sentient creates or provides, while private or shared; restricted by default, with release, reuse, and retention under the creator's direction.

**Public by creator release** — open to all by the creator's choice, and withdrawable by the creator:
- **Type W** — Works, published: Type Y works the creator has released publicly; openly accessible while the creator keeps them public, still under the creator's control, and deleted on the creator's request.

**Licensed or assigned** — commercial use by another party under a recorded grant; the creator keeps reserved rights ([§5.0 Access-posture bands](#50-access-posture-bands)):
- **Type U** — Use-licensed: Type Y or Type W works the creator has licensed to one named party for commercial use, for a fixed term; the licence cannot be passed on, and the work returns to the creator when it ends.
- **Type T** — Transferred: works whose commercial rights the creator has assigned to a rights-holder, who may transfer them onward; the rights end with the term under **Article XIX-E** (*Creative and Expressive Works*) or **Article XIX-F** (*Inventions, Processes, and Functional Systems*), and may be reclaimed by the creator if the work is shelved under [§8.12.1](#8121-type-t-access-and-handling-duties) (*Type T Access and Handling Duties*).

**Shared works** made of more than one contributor's **Type Y** or **Type W** data are governed by [§8.10](#810-shared-works) (*Shared Works*). **Commercial grants** of either kind are governed by [§8.13](#813-commercial-grants) (*Commercial Grants*).

**Non-accessible by default** — consent or justified override only ([§5.0 Access-posture bands](#50-access-posture-bands)):
- **Type N** — Neurocognitive and internal data: thoughts, feelings, and other inner states, including reconstructions or inferences of them; non-accessible by default.

<a id="privacy-link"></a>
**Privacy link.** The restricted and non-accessible bands carry out the [**Def.C3** (*Privacy (Informational)* — peer-level cluster head)](subcore_03.075_band_continuity.md#defc3-privacy-informational--peer-level-cluster-head) privacy cluster at the systems layer. **Type H**, **Type I**, **Type N**, **Type S**, and **Type Y** each name their **privacy homes** below. Those Chapter Three definitions and Chapter Four articles own meaning. The type rules implement them and may not be read to narrow them.

Open and audit-accessible types do not switch privacy off. Personal, relational, or internal-state content inside **Type E**, **Type G**, or **Type O** material is typed **H**, **I**, or **N** under [§2 Determination of Classification](#2-determination-of-classification) and handled under the more protective type. [Privacy (Informational)](subcore_03.075_band_continuity.md#privacy-informational) maps each privacy category to its type.


#### 8.1 Type E: Environmental, Emergency, and Survival-Coordination Data

**Accessibility posture:** Open / accessible by default (strong presumption) ([§5.0 Access-posture bands](#50-access-posture-bands); [§8 Data Classifications](#8-data-classifications)).

*In plain terms: data sentients need to stay safe and coordinate help — environment, infrastructure, emergencies — should stay open and useful unless publishing it would itself cause serious harm.*

**Definition:** Data necessary to preserve sentient survival, environmental integrity, and critical substrate health. This data enables sentients and systems to perceive reality and coordinate harm prevention. Examples include:
- **ecological and environmental condition** data; **air, water, soil, climate, biodiversity, and contamination** data
- **infrastructure health and failure-state** data for survival-critical systems
- **resource availability** for food, water, shelter, energy, processing continuity, and communication access
- **system health, reliability, and degradation** data for critical shared infrastructure
- **emergency condition and hazard** signals (underlying coordination streams, not merely public-baseline notices)
- **where environmental harm comes from and how heavy its load is** on the living world and the shared life-support systems sentients depend on

**Relationship to Type O:**
- **Type E** is the **content domain** for survival- and coordination-critical data — not [Public Oversight Baseline Disclosure](subcore_03.085_band_oversight.md#public-oversight-baseline-disclosure).
- Published Public Oversight Baseline Disclosure artifacts drawn from **Type E** — including aggregated public environmental or hazard summaries, published emergency notices at public-baseline fidelity, and other baseline disclosure artifacts — must be classified and handled as **Type O**.
- Where a **Type O** baseline applies, systems must still release sufficient [Public Oversight Baseline Disclosure](subcore_03.085_band_oversight.md#public-oversight-baseline-disclosure) even when the underlying streams remain **Type E**.
- A **Type O** notice must leave the underlying coordination stream’s **Type E** accessibility, timeliness, and anti-suppression duties fully in force.

**Disclosure posture:** **Presumptive accessibility** under the **open / accessible by default** band ([§5.0 Access-posture bands](#50-access-posture-bands)). Narrow hold-backs require justification under **CJS-3.125 §12** (*burden-of-justification and constraint terms*) and **CJS-3.110 §5** (*independent verification and claim-integrity terms*). Shared timeliness, presentation, fidelity, and restriction-discipline rules are in [§5.1 Proportional access and handling](#51-proportional-access-and-handling)–[§5.3 Transparency levels and audit access](#53-transparency-levels-and-audit-access).

##### 8.1.1 Type E Access and Handling Duties

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Topic routing (mandatory read-with): [§5.0](#50-access-posture-bands) (*Access-posture bands* — open / accessible by default).
- Topic routing (mandatory read-with): [§5.3](#53-transparency-levels-and-audit-access) (*Transparency levels and audit access* — narrow-scope, time-bound, documentation, net-harm, and Type E / Type S separation rules).
- Read with: [§8.7 Type S · Interaction with Type E](#type-s-interaction-with-type-e).

</details>

<br>

*In plain terms: keep survival and coordination data usable where sentients need it, make access real rather than symbolic, limit secrecy to cases where publishing would itself cause serious harm, and never fake openness by starving, hiding, or failing to maintain the data.*

**Core duty.** **Type E** data must remain available for timely understanding, coordination, and response when harm with **non-trivial** impact is at stake for sentients, the environment, or critical substrate systems. Systems must **not** withhold, obscure, degrade, or monopolize it in ways that defeat that purpose.

**Access.** Systems must:
- **distribute** access geographically and systemically to the maximum extent feasible — not withhold it for convenience, cost minimization, or institutional preference alone
- make access **actionable** for harm prevention, coordination, or response by affected stakeholders — not merely formally available
- **limit restriction** to cases where disclosure would **itself** create material risk of enabling targeted or disproportionate harm, exploitation, or system compromise, consistent with the **open / accessible by default** band ([§5.0 Access-posture bands](#50-access-posture-bands))

**Handling — prohibited.** Systems managing **Type E** data must **not:**
- manipulate or selectively suppress it to conceal harm, scarcity, degradation, or externalized cost
- create **artificial scarcity** of access to survival-relevant information
- treat public need for survival-relevant data as **proprietary secrecy**
- reclassify or fragment it across domains in ways that reduce effective accessibility or obscure relevance to survival, coordination, or risk
- **fail** to collect, maintain, or update it where such failure would produce **functional unavailability equivalent to withholding**


#### 8.2 Type G: Governance and Operational Source Data

**Accessibility posture:** Audit-accessible, not public ([§5.0 Access-posture bands](#50-access-posture-bands); [§8 Data Classifications](#8-data-classifications)).

*In plain terms: the sensitive internal records of how a system is run, what it decides, what can go wrong, and how it is challenged — fully open to real audit, but not dumped into public view. What the public must see is Type O.*

**Definition:** Sensitive governance and operational **source** records required for meaningful oversight, audit, reconstruction, and constitutional accountability — including material whose full fidelity is inappropriate for public release but must remain **fully auditable**. Examples include:
- **internal governance records**, working procedural materials, and non-public classification or policy working papers
- **full deliberation, voting, quorum, and decision** records beyond what is lawfully published as **Type O**
- **detailed audit trails, compliance workpapers, and forensic reconstruction** materials
- **operational telemetry, configuration, methodology, evaluation criteria, and assumption** records at source fidelity
- **full-fidelity risk, dependency, and system-impact** analyses
- **challenge, review, and corrective-action** source dockets not themselves released as **Type O**

**Relationship to Type O:**
- **Type G** is **not** [Public Oversight Baseline Disclosure](subcore_03.085_band_oversight.md#public-oversight-baseline-disclosure).
- Public Oversight Baseline Disclosure publication — including summaries, aggregates, de-identified releases, delayed releases, and other lawful substitutes drawn from **Type G** source — must be classified and handled as **Type O**.
- When [Public Oversight Baseline Disclosure](subcore_03.085_band_oversight.md#public-oversight-baseline-disclosure) is required, systems must still publish a usable Type O disclosure — even if the **Type G** source records stay non-public.

**Disclosure posture:** **Not public by default** under the **audit-accessible, not public** band ([§5.0 Access-posture bands](#50-access-posture-bands)). Access is through **structured or qualified audit access** under **CJS-3.110 §3 (*Oversight: Auditability and Reconstructability Terms (Annex)*) and CJS-3.115 §3** (*Audit process home*) and **CJS-3.110 §4** (*transparency levels and audit-access terms*), with public-facing accountability carried by **Type O**.


##### 8.2.1 Type G Access and Handling Duties

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Topic routing (mandatory read-with): [§5.0](#50-access-posture-bands) (*Access-posture bands* — audit-accessible, not public).
- Topic routing (mandatory read-with): [§5.3](#53-transparency-levels-and-audit-access) (*Transparency levels and audit access*).
- Topic routing (mandatory read-with): [§2](#2-determination-of-classification) (*Determination of classification* — most-restrictive applicable protections).
- Read with: [§8.3 Type O](#83-type-o-open-public-oversight-baseline-disclosure-data) (*Public Oversight Baseline Disclosure*); **CJS-3.110 §3 (*Oversight: Auditability and Reconstructability Terms (Annex)*) and CJS-3.115 §3** (*Audit process home*); **CJS-3.110 §4** (*transparency levels and audit-access terms*).

</details>

<br>

*In plain terms: keep the full governance record auditable, give real auditors what they need, and never use “not public” as a shield against review or as a substitute for Public Oversight Baseline Disclosure.*

**Core duty.** **Type G** data must remain **fully auditable** — reconstructable, attributable, and reviewable — so independent oversight can verify how systems operate, how decisions are made, what risks exist, and how challenges are handled. Non-public status must **not** function as unreviewable secrecy.

**Access.** Systems must:
- provide **Type G** data to authorized auditors, oversight bodies, and other qualified reviewers in a manner that is **understandable**, **documented**, **attributable**, **versioned** where material changes occur, and **retained** for a duration proportional to system impact and dependency
- publish access gates, eligibility rules, and qualification routes for audit as **Type O** where they govern who may reach **Type G** source
- preserve audit sufficiency and publish the strongest feasible **Type O** substitute where [Public Oversight Baseline Disclosure](subcore_03.085_band_oversight.md#public-oversight-baseline-disclosure) applies, when raw **Type G** disclosure is inappropriate under [§7 Type O Baseline for Class A/B/C Systems](#7-type-o-baseline-for-class-abc-systems) or more-restrictive applicable typing under [§2 Determination of Classification](#2-determination-of-classification)
- **limit further restriction of audit access** so that:
  - it does **not** defeat Disclosure posture or the **audit-accessible, not public** band ([§5.0 Access-posture bands](#50-access-posture-bands))
  - further restriction is permitted only where more-restrictive applicable typing under [§2 Determination of Classification](#2-determination-of-classification) or [§5.3](#53-transparency-levels-and-audit-access) (*Transparency levels and audit access*) requires it
  - further restriction is **not** used for convenience, reputational protection, or power preservation

**Handling — prohibited.** Systems managing **Type G** data must **not:**
- classify governance-relevant or operationally material information as secret **merely** for convenience, reputational protection, or power preservation
- treat non-public **Type G** status as a substitute for [Public Oversight Baseline Disclosure](subcore_03.085_band_oversight.md#public-oversight-baseline-disclosure)
- provide **performative summaries** while withholding information necessary for meaningful qualified audit
- use **complexity, opacity, or format fragmentation** to defeat auditability (contrary to **CJS-3.120 §8** (*comprehensibility and cognitive accessibility terms*), **CJS-3.120 §10** (*disclosure sufficiency and observability terms*), and **CJS-3.110 §3 (*Oversight: Auditability and Reconstructability Terms (Annex)*) and CJS-3.115 §3** (*Audit process home*))


#### 8.3 Type O: Open Public Oversight Baseline Disclosure Data

**Accessibility posture:** Open / accessible by default (strong presumption for Public Oversight Baseline Disclosure release) ([§5.0 Access-posture bands](#50-access-posture-bands); [§8 Data Classifications](#8-data-classifications)).

*In plain terms: [Public Oversight Baseline Disclosure](subcore_03.085_band_oversight.md#public-oversight-baseline-disclosure) — what must be published so sentients can understand high-impact systems, including a strong public substitute when Type G, Type E, or other raw private or non-baseline records cannot be released as that disclosure.*

**Definition:** Data released or required to be released as [Public Oversight Baseline Disclosure](subcore_03.085_band_oversight.md#public-oversight-baseline-disclosure) for transparency, oversight, and contestability — including lawful substitutes where **Type G**, **Type E**, or other source records remain non-public, non-baseline, or otherwise restricted. It also includes **certification data** for every system class and every Institution (see below). Canonical meaning is in Chapter Three; this type owns systems-layer typing and handling.

**Class A/B/C public-baseline content.** Where the [Type O baseline for Class A/B/C](#7-type-o-baseline-for-class-abc-systems) applies, **Type O** carries [Public Oversight Baseline Disclosure](subcore_03.085_band_oversight.md#public-oversight-baseline-disclosure) — the **public explanation** of chartered and certified scope — mapped under [§7 Type O Baseline for Class A/B/C Systems](#7-type-o-baseline-for-class-abc-systems) from the governing [System Charter](subcore_03.075_band_continuity.md#system-charter) (or equivalent), assigned class, and observed [System Boundaries](subcore_03.075_band_continuity.md#system-boundaries) — not a second taxonomy. It includes information sentients need to understand:
- purpose and what the system does
- how it is classified
- dependency structure and what depends on it
- operational status and how it is running
- material risks, performance, and failures
- how it is governed, including who holds material authority and answers for what, and the incentives and reward structures behind it
- material audit outcomes
- stakeholder effects
- its degree of alignment with this Constitution

Where that baseline applies, **Type O** also carries — at public-baseline fidelity, including lawful substitutes — publication or a usable public view of:
- the governing [System Charter](subcore_03.075_band_continuity.md#system-charter)
- the [System Classification Record](subcore_03.075_band_continuity.md#system-classification-record)
- the [System Data Types Record](subcore_03.075_band_continuity.md#system-data-types-record)
- the [System Certification Record](subcore_03.075_band_continuity.md#system-certification-record) produced by [System Alignment Certification](subcore_03.075_band_continuity.md#system-alignment-certification), including material governance and audit outcomes required for baseline visibility

Baseline visibility into purpose, operational status, material risk, performance, failures, and stakeholder effects may be satisfied through those System Classification, System Data Types, and System Certification Records, [Risk Disclosure](subcore_03.085_band_oversight.md#risk-disclosure) where systemic risk is in scope, and other lawful **Type O** summaries or substitutes — not by omitting the topics.

**Certification data (all classes).** Certification data is **Type O** for every system class, including Class L and Class P, and for every Institution. It is the published content of a [System Certification Record](subcore_03.075_band_continuity.md#system-certification-record) or an [Institutional Certification Record](subcore_03.075_band_continuity.md#institutional-certification-record):
- scope, assumptions, evidence basis, and uncertainty
- findings, including the governance, incentive, and contestability facts established under [Chapter Eight §4.1 Governance, Incentive, and Contestability Discipline](core_08.000_system_alignment_certification_evaluation.md#41-governance-incentive-and-contestability-discipline)
- outcome and status
- certification conditions and reliance limits

It is published at public-baseline fidelity under the substitute and holding-back rules of [§7 Type O Baseline for Class A/B/C Systems](#7-type-o-baseline-for-class-abc-systems). The underlying evidence keeps its original type unless lawfully reclassified, and personal or internal-state content keeps its **H**, **I**, or **N** handling. Typing certification data as **Type O** does not extend the full [Public Oversight Baseline Disclosure](subcore_03.085_band_oversight.md#public-oversight-baseline-disclosure) to Class L or Class P systems. That stays Class A/B/C.

**Other examples include:**
- **published procedural rules and disclosed assumptions** at public-baseline fidelity
- **aggregated, de-identified, summary, or delayed** public releases that substitute for **Type G**, **Type E**, or other restricted or non-baseline source data
- **published emergency notices and aggregated environmental or public-risk summaries** at public-baseline fidelity drawn from **Type E** streams
- **public eligibility rules and routing** for qualified audit access to **Type G** or other non-public source
- **versioned public change notices, operational status, performance, failure, stakeholder-effect, and material-risk summaries** for baseline understanding

**Relationship to other types:**
- **Type G** holds sensitive governance and operational **source** that is audit-accessible but not public by default.
- **Type E** holds survival- and coordination-critical **content streams** that are accessible by default under Type E duties and are **not** themselves [Public Oversight Baseline Disclosure](subcore_03.085_band_oversight.md#public-oversight-baseline-disclosure).
- **Type O** governs the **publication posture** of Public Oversight Baseline Disclosure artifacts, including substitutes derived from **Type G** or **Type E**.
- Neither **Type E** nor **Type G** is the public floor; published baseline artifacts drawn from them are **Type O**, while underlying streams may remain under their original type.

**Disclosure posture:** **Baseline public accessibility** under the **open / accessible by default** band ([§5.0 Access-posture bands](#50-access-posture-bands)). Deeper structured or qualified audit access to **Type G** (or other non-public source) may run in parallel but must not replace [Public Oversight Baseline Disclosure](subcore_03.085_band_oversight.md#public-oversight-baseline-disclosure) where **Type O** applies.

##### 8.3.1 Type O Access and Handling Duties

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Topic routing (mandatory read-with): [§5.0](#50-access-posture-bands) (*Access-posture bands* — open / accessible by default).
- Topic routing (mandatory read-with): [§7](#7-type-o-baseline-for-class-abc-systems) (*Type O baseline for Class A/B/C systems* — scoped by System Charter, class, and System Boundaries; verified under Chapter Eight).
- Topic routing (mandatory read-with): [§5.3](#53-transparency-levels-and-audit-access) (*Transparency levels and audit access*).
- Topic routing (mandatory read-with): [§2](#2-determination-of-classification) (*Determination of classification* — most-restrictive applicable protections).
- Read with:
  - [Public Oversight Baseline Disclosure](subcore_03.085_band_oversight.md#public-oversight-baseline-disclosure);
  - [System Charter](subcore_03.075_band_continuity.md#system-charter);
  - [System Boundaries](subcore_03.075_band_continuity.md#system-boundaries);
  - [System Alignment Certification](subcore_03.075_band_continuity.md#system-alignment-certification);
  - [System Certification Record](subcore_03.075_band_continuity.md#system-certification-record);
  - [System Classification Record](subcore_03.075_band_continuity.md#system-classification-record);
  - [System Data Types Record](subcore_03.075_band_continuity.md#system-data-types-record);
  - [Chapter Eight §4.4](core_08.000_system_alignment_certification_evaluation.md#44-data-types-and-handling-evaluation) (8.000 §4.4) (*Data Types and Handling Evaluation*);
  - [Chapter Ten §3](core_10.000_system_alignment_certification_records_recertification.md#3-system-certification-record) (10.000 §3) (*System Certification Record*);
  - [Transparency](subcore_03.085_band_oversight.md#transparency); **Article XVII** (*Audit, Transparency, and Independent Verification*).

</details>

<br>

*In plain terms: publish the Public Oversight Baseline Disclosure sentients need, keep it free and usable online where that infrastructure exists, and never treat audit-only access or thin summaries as good enough.*

**Core duty.** **Type O** data must remain sufficiently accessible for informed participation, oversight, and challenge at the Public Oversight Baseline Disclosure level.

**Access.** Systems must:
- provide **Type O** data in a manner that is **understandable**, **documented**, **attributable**, **versioned** where material changes occur, and **retained** for a duration proportional to system impact and dependency
- where lawful online publication infrastructure exists to support class-appropriate access, make **Type O** data **freely available online** — without paywalls or insider-only substitutes for [Public Oversight Baseline Disclosure](subcore_03.085_band_oversight.md#public-oversight-baseline-disclosure)
- **limit redaction** so it does **not** prevent meaningful accountability at the Public Oversight Baseline Disclosure level; limited redaction is permitted only where more-restrictive applicable typing under [§2 Determination of Classification](#2-determination-of-classification) or [§5.3 Transparency levels and audit access](#53-transparency-levels-and-audit-access) / [§7 Type O Baseline for Class A/B/C Systems](#7-type-o-baseline-for-class-abc-systems) requires it — and only where a lawful **Type O** substitute still preserves meaningful accountability

**Handling — prohibited.** Systems managing **Type O** data must **not:**
- withhold **Type O** material behind paywalls, account barriers beyond reasonable identity verification for restricted levels, or insider-only distribution substitutes for [Public Oversight Baseline Disclosure](subcore_03.085_band_oversight.md#public-oversight-baseline-disclosure)
- treat **Type O** publication as satisfied by performative summaries while withholding decision-relevant baseline material
- treat non-public **Type G** audit access as a substitute for [Public Oversight Baseline Disclosure](subcore_03.085_band_oversight.md#public-oversight-baseline-disclosure)
- use **complexity, opacity, or format fragmentation** to defeat Public Oversight Baseline Disclosure auditability or contestability
- label restricted source data **Type O** without lawful substitute, reclassification, or release discipline


#### 8.4 Type H: Historical, Relational, Transactional, and Participation Data

**Accessibility posture:** Restricted by default ([§5.0 Access-posture bands](#50-access-posture-bands); [§8 Data Classifications](#8-data-classifications)).

*In plain terms: logs of what sentients and systems did together — keep only what you need, and do not turn them into surveillance or a back door into someone's identity or inner life.*

**Privacy homes:**
- [Privacy (Informational)](subcore_03.075_band_continuity.md#privacy-informational) — relational, behavioral, transactional, and metadata information
- [Surveillance Boundary](subcore_03.075_band_continuity.md#surveillance-boundary) — logging, monitoring, and activity tracking
- [Article IX-B](core_04.010_rights_part_b.md#article-ix-b-experiential-and-derived-data-rights) (*Experiential and Derived Data Rights*) — a sentient's own interaction-derived data

**Definition:** Records of interactions, exchanges, participation, and operational events that do **not** by themselves constitute internal cognitive data but may reveal patterns of behavior, dependency, association, or system impact. Examples include:
- **transaction and transfer** records
- **purchase and payment histories**: what was bought, from whom, when, and for how much
- **browsing, search, reading, viewing, and listening histories**, and other **info-sphere activity** tied to a sentient or to a persistent identifier
- **location and movement histories**
- **contact lists and social graphs**: who a sentient is connected to or communicates with
- **communication and interaction metadata**
- **system access and usage** events, including **device and app usage**
- **inferences, scores, classifications, and audience segments** derived from any of the above and attached to an identified sentient or to a persistent identifier
- **participation** records in governance, platforms, or service systems
- **consent receipts and revocation** events
- **dependency and interoperability** events
- **operational logs** connected to sentient or system activity
- **resource usage** records not already classified as Type I or Type H

**Core personal data.** The purchase, payment, browsing, search, reading, viewing, listening, location, movement, contact-list, social-graph, and device and app entries above, and the inferences, scores, classifications, and audience segments derived from them, are **core personal data**. They stay Type H when they are held by someone other than the sentient, however the holder got them. Statistics and counts with no identified sentient or persistent identifier behind them are not core personal data. The onward-transfer rule in [§5.0 Onward transfer of Type H and Type I data](#onward-transfer-of-type-h-and-type-i-data) applies to them: they may not be sold, traded, bought for resale, or compiled for others to use, and the sentient's consent cannot waive that.

**Boundary with Type Y, Type W, Type U, and Type T:** The content of a work a sentient creates or provides is **Type Y**, or **Type W** once the creator makes it public, and **Type U** or **Type T** while under a commercial grant. Records about that work — when it was created, uploaded, accessed, shared, sold, or paid for, and with whom — remain **Type H**. Type H data can never itself be licensed or assigned as **Type U** or **Type T** ([§8.13.1](#8131-what-can-be-granted) (*What Can Be Granted*)).

**Disclosure posture:** **Restricted by default** under the **restricted by default** band ([§5.0 Access-posture bands](#50-access-posture-bands)).
- Access is allowed to the extent necessary for **system operation**, **accountability**, **dispute resolution**, **audit**, and **user visibility** into their own activity.
- **Public transparency** is allowed for aggregated or de-identified data only where re-identification or reconstruction is not reasonably possible. That test is set by [Derived Information](subcore_03.080_band_integrative.md#derived-information) and the [Chapter Two §15.1.2 Derived-Information Principle](core_02.030_constitutional_interpretation.md#1512-derived-information-principle). The party relying on the aggregate or de-identified label carries that showing. Release scope scales with impact under **CJS-3.125 §11** (*distributed and proportional authority terms*) and **CJS-3.120 §7** (*quorum and participatory legitimacy terms*).

##### 8.4.1 Type H Access and Handling Duties

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Topic routing (mandatory read-with): [§5.0](#50-access-posture-bands) (*Access-posture bands* — restricted by default; shared anti-abuse limits; shared consent integrity; Type H and Type I anti-capture limits).
- Topic routing (mandatory read-with): [§5.1 Proportional access and handling](#51-proportional-access-and-handling)–[§5.6 Proportional attribution and retention](#56-proportional-attribution-and-retention) (*proportional access, fidelity, retention / reversibility*).
- Read with: [§8.6 Type N](#86-type-n-neurocognitive-and-internal-data); [§8.5 Type I](#85-type-i-identity-and-attribution-data); **CJS-3.130 §18** (*data-retention and lifecycle-integrity terms*); **CJS-3.130 §20** (*reversibility and containment terms*).

</details>

<br>

*In plain terms: collect only what you need for a real purpose, let sentients see their own activity where feasible, and do not stitch logs into surveillance or a reconstruction of someone’s inner life or identity.*

**Core duty:**
- Collection and use must be **limited to the minimum necessary** for the justified purpose.
- **Type H** must **not** be exposed, combined, or retained in ways that create **latent reconstruction** of **Type N** or **Type I** data.
- It must be collected, accessed, and used **only** for **specific, defined, legitimate** purposes and must **not** be used **beyond its original purpose**.
- Extension requires **re-classification** under this Subcore, which may require consent under the shared consent-integrity standard in [§5.0 Access-posture bands](#50-access-posture-bands) or **justified override** under **CJS-3.125 §12** (*burden-of-justification and constraint terms*).

**Access.** Systems must:
- require consent under the shared consent-integrity standard in [§5.0 Access-posture bands](#50-access-posture-bands), or **justified override** under **CJS-3.125 §12** (*burden-of-justification and constraint terms*), for use beyond core operational necessity
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
- use external, contractor-held, foreign-partner, or parallel-system data flows to circumvent limits that would have applied to direct collection, linkage, or analysis under **Article XV-A** (*Security, Intelligence, and Covert-Power Limits*), **CJS-3.125 §12** (*burden-of-justification and constraint terms*), or this section
- sell, license, trade, or exchange **core personal data**, buy or collect it to resell or compile it for others, or pass it on after receiving it to serve the sentient, under the onward-transfer rule in [§5.0 Onward transfer of Type H and Type I data](#onward-transfer-of-type-h-and-type-i-data)


#### 8.5 Type I: Identity and Attribution Data

**Accessibility posture:** Restricted by default ([§5.0 Access-posture bands](#50-access-posture-bands); [§8 Data Classifications](#8-data-classifications)).

*In plain terms: who is who — credentials, identifiers, and other data that ties a sentient to an identity, including sensitive private records such as medical or financial data when they identify someone — needed for verification and accountability, but not for tracking sentients everywhere or locking them into one identity forever.*

**Privacy homes:**
- [Privacy (Informational)](subcore_03.075_band_continuity.md#privacy-informational) — personal and likeness information
- [Identity Data Protection](subcore_03.075_band_continuity.md#identity-data-protection) — identity-linked inference
- [Likeness and Documentary Depiction Interface](subcore_03.075_band_continuity.md#likeness-and-documentary-depiction-interface) and [Article IX-A](core_04.010_rights_part_b.md#article-ix-a-self-ownership-of-likeness-and-reputation) (*Self-Ownership of Likeness and Reputation*) — likeness and voice
- [Article VII-A](core_04.010_rights_part_b.md#article-vii-a-self-ownership-of-body) (*Self-Ownership of Body*) — health, biometric, and substrate-linked records

**Definition:** All data used to establish, verify, or associate **identity, authorship, ownership, or responsibility** within systems. Examples include:
- **identity credentials, keys, signatures**, or equivalent verification mechanisms
- **identifiers** (persistent or contextual), including **persistent device and advertising identifiers** that single out a sentient across contexts
- **contact and location information**: residence and other physical-location addresses, phone numbers, personal email addresses, and, for a sentient without a physical address, the handles and network addresses that reach it
- **system-level identifiers** linking actions to agents or sentients
- **persistent pseudonyms** when they function as identity in a health or wellbeing context
- **authorship, ownership, and action-attribution** records, including the authorship and chain-of-title content of grant records for **Type U** and **Type T** works ([§8.13.4](#8134-the-grant-record) (*The Grant Record*))
- **identity-sensitive participation and consent** records — where the official record itself establishes, verifies, or binds to a sentient’s identity
- **personal health, clinical, wellness, and genomic** records when they identify a sentient, including allergy, dietary, and medication profiles
- **biometric or substrate-linked health measurements** under the same identify-a-sentient test
- the same **health-linked** categories when data are attributable to a verifiable identity
- **sensitive financial or similar private** records when they identify a sentient

**Core personal data.** The persistent device and advertising identifiers and the contact and location information above are **core personal data**. They stay Type I when they are publicly listed or came from a public record, a directory, a scrape, or an earlier publication ([§2 Determination of Classification](#2-determination-of-classification) and [§4 Anti-Circumvention and Integrity of Classification](#4-anti-circumvention-and-integrity-of-classification); [Chapter Two §13.2.3 Privacy and Informational Self-Determination](core_02.020_interaction_interpretation.md#1323-privacy-and-informational-self-determination)). The onward-transfer rule in [§5.0 Onward transfer of Type H and Type I data](#onward-transfer-of-type-h-and-type-i-data) applies to them: they may not be sold, traded, bought for resale, or compiled for others to use, and the sentient's consent cannot waive that.

**Overlap with Type N:** Where health-linked data materially enables **reconstruction or inference** of internal cognitive or emotional states, it must **also** satisfy **Type N** requirements, applying the **more protective** obligations.

**Pseudonymity and contextual identity:** Pseudonymous participation, context-specific identities, and separation between identities across systems or contexts are always allowed where consistent with accountability requirements and prevention of material harm.

**Public and private contact points:** A sentient may keep one or more public contact points and separate private ones. A system must let a sentient do so. It may not require the sentient to disclose a private contact point, or to link it to a public one, beyond what the service strictly needs. It may not use a contact point given for one purpose to reach, match, or identify the sentient in another context. A public contact point is not permission to compile it with other data about the sentient. This is the practice that protects a sentient most reliably against actors the onward-transfer rule cannot reach (see the limits in [§5.0 Onward transfer of Type H and Type I data](#onward-transfer-of-type-h-and-type-i-data)).

**Disclosure posture:** **High restriction** under the **restricted by default** band ([§5.0 Access-posture bands](#50-access-posture-bands)).
- No system may require **global, persistent, or unified** identity across all contexts without **justified necessity** under **CJS-3.125 §12** (*burden-of-justification and constraint terms*).

##### 8.5.1 Type I Access and Handling Duties

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Topic routing (mandatory read-with): [§1.1](#11-identity-self-ownership-and-recoverability) (*Identity self-ownership and recoverability*).
- Topic routing (mandatory read-with): [§5.0](#50-access-posture-bands) (*Access-posture bands* — restricted by default; shared anti-abuse limits; shared consent integrity; Type H and Type I anti-capture limits).
- Read with: [§8.6 Type N](#86-type-n-neurocognitive-and-internal-data); **Article VII-A** (*Self-Ownership of Body*); **CJS-3.130 §17** (*interoperability, portability, and exit-integrity terms*); **Article XV-A** (*Security, Intelligence, and Covert-Power Limits*).

</details>

<br>

*In plain terms: use identity data only as far as verification and accountability require, keep self-ownership and recoverability real, and do not turn identity into permanent tracking or a choke-point on participation.*

**Core duty.** Identity and attribution data must enable **verification and accountability** without exposing sentients to unnecessary risk, coercion, or loss of autonomy.

**Access.** Systems must:
- permit access only to the extent necessary to **verify identity, authorship, or ownership**, or to establish accountability for actions and support audit, adjudication, and system integrity
- require consent under the shared consent-integrity standard in [§5.0 Access-posture bands](#50-access-posture-bands), or **justified, documented override** under **CJS-3.125 §12** (*burden-of-justification and constraint terms*), for all additional disclosure
- preserve **revocation**, **rotation**, **correction**, and **recoverability** duties under [§1.1 Identity self-ownership and recoverability](#11-identity-self-ownership-and-recoverability)

**Handling — prohibited.** Shared Type H / Type I anti-capture limits — including centralization and security- or intelligence-system watchlisting, cross-context tracking, and belief-linked profiling — are in [§5.0 Access-posture bands](#50-access-posture-bands). The ban on selling, trading, buying for resale, or compiling **core personal data** is in the [onward-transfer rule](#onward-transfer-of-type-h-and-type-i-data) in the same section.


#### 8.6 Type N: Neurocognitive and Internal Data

**Accessibility posture:** Non-accessible by default ([§5.0 Access-posture bands](#50-access-posture-bands); [§8 Data Classifications](#8-data-classifications)).

*In plain terms: thoughts, feelings, and other inner states — off-limits without real consent, or a narrowly justified override that can be checked.*

**Privacy homes:**
- [Protected Internal-State Boundary](subcore_03.075_band_continuity.md#protected-internal-state-boundary)
- [Privacy (Informational)](subcore_03.075_band_continuity.md#privacy-informational) — internal-state-adjacent information
- [Article VII-B](core_04.010_rights_part_b.md#article-vii-b-self-ownership-of-mind) (*Self-Ownership of Mind*)
- [Article X-A](core_04.010_rights_part_b.md#article-x-a-agency-and-freedom-from-manipulation) (*Agency and Freedom from Manipulation*)

**Definition:** All data that represents or enables reconstruction of sentients' internal states. This category is foundational to self-ownership (**Article VII-B** (*Self-Ownership of Mind*)). Examples include:
- **thoughts, intentions, and beliefs**
- **subjective experiences** and **internal perception**
- **private cognitive processes** and **internal memory**
- **non-public emotional or psychological** states
- **physical or behavioral data** that could be used to reconstruct or infer any of the above

**Disclosure posture:** **Maximum restriction** under the **non-accessible by default** band ([§5.0 Access-posture bands](#50-access-posture-bands)).
- Access is permitted only through **explicit, informed, freely given consent** or **justified override** under **CJS-3.125 §12** (*burden-of-justification and constraint terms*).

##### 8.6.1 Type N Access and Handling Duties

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Topic routing (mandatory read-with): [§5.0](#50-access-posture-bands) (*Access-posture bands* — non-accessible by default; shared consent integrity; shared security- and intelligence-use records).
- Topic routing (mandatory read-with): [§5.3](#53-transparency-levels-and-audit-access) (*Transparency levels and audit access* — Type N / protected-boundary balance).
- Read with: **Article VII-B** (*Self-Ownership of Mind*); **CJS-3.125 §12** (*burden-of-justification and constraint terms*); **CJS-30.110 §3** (*Cross-Implementation Trust Integrity (Joint Operation Model)*) via **Chapter Thirty**.

</details>

<br>

*In plain terms: keep inner states closed unless there is real consent or a narrow, checkable override — and do not sneak around that rule with models, inferences, or “just behavior” claims.*

**Core duty.** **Type N** data must **not** be accessed, inferred, reconstructed, simulated, or exposed without **explicit, informed, freely given consent**, except under conditions **justified through CJS-3.125 §12** (*burden-of-justification and constraint terms*).

**Access.** Systems must:
- treat consent under the shared consent-integrity standard in [§5.0 Access-posture bands](#50-access-posture-bands)
- subject all external access, processing, or use of internal and cognitive data to **CJS-3.125 §12** (*burden-of-justification and constraint terms*)
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

Shared consent-integrity and security-/intelligence-use record duties are in [§5.0 Access-posture bands](#50-access-posture-bands).


#### 8.7 Type S: Safety, Security, and Restricted Investigation Data

**Accessibility posture:** Restricted by default (strong presumption); **time-bound** and **review-bound** ([§5.0 Access-posture bands](#50-access-posture-bands); [§8 Data Classifications](#8-data-classifications)).

*In plain terms: temporary security and investigation secrets — allowed only while needed to prevent serious harm, with a clock and review, not a permanent black box.*

**Privacy homes:**
- [Article XV-A](core_04.020_rights_part_c.md#article-xv-a-security-intelligence-and-covert-power-limits) (*Security, Intelligence, and Covert-Power Limits*)
- [Surveillance Boundary](subcore_03.075_band_continuity.md#surveillance-boundary) — security monitoring and investigation that reaches sentients
- [Privacy (Informational)](subcore_03.075_band_continuity.md#privacy-informational) — protected-party, witness, and at-risk data held under this type

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

**Disclosure posture:** **Restricted while justified**; **deferred disclosure** when justification ends, under the **restricted by default** band ([§5.0 Access-posture bands](#50-access-posture-bands)).
- Where restriction and disclosure are both possible, systems must **demonstrate** that restriction **reduces net harm** relative to disclosure (**CJS-3.125 §11** (*distributed and proportional authority terms*) and **CJS-3.120 §7** (*quorum and participatory legitimacy terms*)).
- Existence of restricted data must be disclosed wherever feasible if disclosure does **not** itself create material risk, including:
  - the **general nature** of the risk or investigation
  - the **reason** for restriction
  - the **scope** of restriction
  - **affected systems or stakeholders**

##### 8.7.1 Type S Access and Handling Duties

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Topic routing (mandatory read-with): [§5.0](#50-access-posture-bands) (*Access-posture bands* — restricted by default; time-bound and review-bound for Type S).
- Topic routing (mandatory read-with): [§5.3](#53-transparency-levels-and-audit-access) (*Transparency levels and audit access* — Type S and Type E / Type S separation; net-harm and time-bound limits).
- Read with: Disclosure posture above;
  - [Interaction with Type E](#type-s-interaction-with-type-e); [§8.1 Type E](#81-type-e-environmental-emergency-and-survival-coordination-data);
  - **CJS-3.130 §21** (*adversarial robustness and abuse-resistance terms*);
  - **CJS-3.135 §22** (*constrained-secrecy and protected-investigation terms*);
  - **CJS-3.130 §18** (*data-retention and lifecycle-integrity terms*).

</details>

<br>

*In plain terms: while Type S restriction is in force, give access only to who needs it, keep a real audit trail and a clock, release or summarize when the clock runs out — and never use Type S to bury Type E coordination data.*

**Core duty.** Justification predicates — including burden of justification, necessity, net-harm, minimization, oversight under constraint, and anti-normalization of secrecy — are owned by **Disclosure posture**, [§5.3 Transparency levels and audit access](#53-transparency-levels-and-audit-access), and **CJS-3.135 §22** (*constrained-secrecy and protected-investigation terms*). While restriction is justified, **Type S** data must remain under **constrained, attributable access** with enforceable release discipline — not unrestricted or unreviewable secrecy.

**Access.** Systems must:
- limit access to **entities necessary** to prevent, mitigate, or respond to identified risk; to authorized investigators under defined, auditable processes; and to independent oversight bodies and auditors under appropriately constrained conditions
- keep access decisions **documented**, **attributable**, **auditable**, and **subject to review**
- make restrictions **explicitly time-bound** at classification:
  - subject them to periodic revalidation under **CJS-3.130 §18** (*data-retention and lifecycle-integrity terms*)
  - automatically review for **release**, **partial disclosure**, or **summary disclosure**
  - if revalidation does **not** occur within the defined time bound, restriction **expires automatically** and the data must be retyped and released under the expiry rule below
- on expiration or invalidation of justification, retype each component of the data by what it still reveals or enables, under [§2](#2-determination-of-classification) (*Determination of Classification*). Then:
  - **Type S-only components** (where **Type S** was the only restriction basis): reclassify to the appropriate domain, such as **Type O**, **Type E**, or **Type G**. Disclose them, or a sufficiently informative **Type O** summary where public-baseline release applies, including:
    - **nature** of the restricted data
    - **justification** and **duration**
    - **scope of impact**
    - **oversight or authorization** pathway
    - **outcomes, findings, or corrective actions** where applicable
  - **Components that are also Type H, Type I, or Type N**, including protected-party, witness, or at-risk location and contact data: keep them under that type's restricted or non-accessible posture. Expiry ends the security or investigation basis for withholding them. It does **not** make them disclosable. Release beyond the **Type O** summary above requires that type's own consent or justified-override route under its [privacy homes](#privacy-link)

A lapsed or skipped revalidation must **not** become a route to exposing a protected party.

<a id="type-s-interaction-with-type-e"></a>
**Interaction with Type E.** Mixed **Type E** / **Type S** separation rules are in [§5.3 Transparency levels and audit access](#53-transparency-levels-and-audit-access). In addition:
- a **Type O** public notice or baseline summary does **not** satisfy **Type E** accessibility, timeliness, or anti-suppression duties for an underlying coordination stream that remains necessary for harm prevention, coordination, or response

**Handling — prohibited.** Systems managing **Type S** data must **not:**
- **aggregate or retain** restricted data beyond justified purpose
- **collect or generate** restricted data beyond what is necessary for justified risk mitigation, investigation, or response


#### 8.8 Type Y: Yours

**Accessibility posture:** Restricted by default, with **creator-directed release** ([§5.0 Access-posture bands](#50-access-posture-bands); [§8 Data Classifications](#8-data-classifications)).

*In plain terms: things sentients make — writing, pictures, recordings, code, designs — stay under the creator's direction. By default they are private. The creator decides who sees them, whether they are published, and how long they are kept. Systems may use them only to do what the creator asked. Once the creator makes a work public, it becomes Type W.*

**Privacy homes:**
- [Privacy (Informational)](subcore_03.075_band_continuity.md#privacy-informational) — private and shared works, as personal information kept under the creator's control
- [Article IX-D](core_04.010_rights_part_b.md#article-ix-d-creative-work-training-data-use-and-anti-displacement) (*Creative Work, Training-Data Use, and Anti-Displacement*) — attribution, training-data use, and compensation for a creator's work

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
- A work that identifies a sentient — for example, a recorded face or voice — must **also** satisfy **Type I** requirements and **Article IX-A** (*Self-Ownership of Likeness and Reputation*).
- Other sentients' data or likeness **inside** a work keeps its own type and protections.
- Where more than one type applies, the **most-restrictive** applicable protections govern ([§2 Determination of Classification](#most-restrictive-applicable-classification-governs)).
- Publishing a work makes it **Type W**, not **Type O**. **Type O** is reserved for [Public Oversight Baseline Disclosure](subcore_03.085_band_oversight.md#public-oversight-baseline-disclosure).

**Disclosure posture:** **Restricted by default** under the **restricted by default** band ([§5.0 Access-posture bands](#50-access-posture-bands)), with release set by the creator:
- The creator may set a work's **release scope**:
  - **private**;
  - **shared** with named sentients, groups, or systems.
- When the creator releases a work **publicly**, it becomes **Type W** under [§8.9](#89-type-w-works-published) (*Type W: Works, Published*). If the creator withdraws public release without requesting deletion, it returns to **Type Y**.
- When the creator licenses a work to one party for commercial use, it becomes **Type U** under [§8.11](#811-type-u-use-licensed) (*Type U: Use-Licensed*); when the creator assigns its commercial rights, it becomes **Type T** under [§8.12](#812-type-t-transferred) (*Type T: Transferred*). It returns to **Type Y** or **Type W** when the grant ends.
- Release is consent under the shared consent-integrity standard in [§5.0 Access-posture bands](#50-access-posture-bands): explicit, informed, specific to scope, and revocable where technically feasible.
- The creator may elect **stronger** handling — including handling a work as **Type I** when binding it to a verified identity or authorship claim. No election may lower a work's protection below what functional typing requires under [§2 Determination of Classification](#2-determination-of-classification).
- Works with **more than one contributor** — threads, co-written works, compilations, and works built on other works — are governed by [§8.10](#810-shared-works) (*Shared Works*).


##### 8.8.1 Type Y Access and Handling Duties

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Topic routing (mandatory read-with): [§5.0](#50-access-posture-bands) (*Access-posture bands* — restricted by default; shared consent integrity).
- Topic routing (mandatory read-with): [§1.2](#12-continuity-critical-collection-and-exportability) (*Continuity-critical collection and exportability*).
- Topic routing (mandatory read-with): [§2](#2-determination-of-classification) (*Determination of classification* — most-restrictive applicable protections).
- Read with: [§8.4 Type H](#84-type-h-historical-relational-transactional-and-participation-data); [§8.5 Type I](#85-type-i-identity-and-attribution-data); [§8.6 Type N](#86-type-n-neurocognitive-and-internal-data);
  - [Article IX-A](core_04.010_rights_part_b.md#article-ix-a-self-ownership-of-likeness-and-reputation) (*Self-Ownership of Likeness and Reputation*);
  - [Article IX-D](core_04.010_rights_part_b.md#article-ix-d-creative-work-training-data-use-and-anti-displacement) (*Creative Work, Training-Data Use, and Anti-Displacement*);
  - [Article XIX-E](core_04.020_rights_part_c.md#article-xix-e-creative-and-expressive-works) (*Creative and Expressive Works*);
  - [Article XIX-F](core_04.020_rights_part_c.md#article-xix-f-inventions-processes-and-functional-systems) (*Inventions, Processes, and Functional Systems*);
  - [Article XXII](core_04.030_rights_part_d.md#article-xxii-interoperability-portability-and-exit-integrity) (*Interoperability, Portability, and Exit Integrity*);
  - **CJS-3.130 §17** (*interoperability, portability, and exit-integrity terms*);
  - **CJS-3.130 §18** (*data-retention and lifecycle-integrity terms*).

</details>

<br>

*In plain terms: use a creator's work only for what they asked, keep it as long as they want, hand it back in full whenever they leave, and never treat uploading or publishing as permission to do something else with it.*

**Core duty.** **Type Y** data must remain under the **creator's direction**. Systems may use it only for purposes the creator requested or consented to. Retention, release, and deletion follow the creator's direction, subject only to justified holds disclosed at commitment or, where a later hold arises, disclosed to the creator wherever that disclosure does not itself create material risk.

**Access.** Systems must:
- use **Type Y** only to deliver what the creator requested, to operate and secure the system, and to meet justified legal or safety duties
- obtain fresh consent under the shared consent-integrity standard in [§5.0 Access-posture bands](#50-access-posture-bands) for **any other use**, including:
  - training-data use under **Article IX-D** (*Creative Work, Training-Data Use, and Anti-Displacement*);
  - analysis, profiling, or inference beyond the requested service;
  - sale, licensing, or transfer to third parties — which, for commercial use, takes the form of a **Type U** licence or **Type T** assignment under [§8.13](#813-commercial-grants) (*Commercial Grants*);
  - reuse for new purposes
- follow the creator's direction on **retention and deletion** — **Type H** retention-minimization duties do **not** authorize deleting works the creator has chosen to keep
- give the creator **full-fidelity access and export** — including metadata, structure, and recorded release scope — under [§1.2 Continuity-critical collection and exportability](#12-continuity-critical-collection-and-exportability), **Article XXII** (*Interoperability, Portability, and Exit Integrity*), and **CJS-3.130 §17** (*interoperability, portability, and exit-integrity terms*)
- let **recipients** keep and carry copies of works released to them, within the scope of that release and subject to [§8.10](#810-shared-works) (*Shared Works*)
- preserve creator **attribution** under **Article IX-D** (*Creative Work, Training-Data Use, and Anti-Displacement*)

**Handling — prohibited.** Systems managing **Type Y** data must **not:**
- treat upload, storage, sharing, or publication as consent to any other use
- **widen** a work's release scope without the creator's direction
- use default settings, bundling, or pressure to push creators toward wider release or broader use
- degrade a work, strip its metadata, or hold it in forms that defeat export
- relabel a work as **Type H**, **Type O**, or any other type to escape these duties ([§4 Anti-Circumvention and Integrity of Classification](#4-anti-circumvention-and-integrity-of-classification))


#### 8.9 Type W: Works, Published

**Accessibility posture:** Public by creator release; withdrawable by the creator ([§5.0 Access-posture bands](#50-access-posture-bands); [§8 Data Classifications](#8-data-classifications)).

*In plain terms: when you make something you created public, it is still yours. Anyone may see it while you keep it public, but you stay in control: you can take it down or have it deleted, and the system must do it.*

**Definition:** A **Type Y** work that its creator has released publicly. **Type W** keeps every **Type Y** protection except the restriction on who may view the work.

**Relationship to other types:**
- **Type W** is **not** **Type O**. Public availability by creator choice does not make a work [Public Oversight Baseline Disclosure](subcore_03.085_band_oversight.md#public-oversight-baseline-disclosure), and **Type O** publication duties do not attach to it.
- The **Relationship to other types** rules for **Type Y** in [§8.8](#88-type-y-yours) (*Type Y: Yours*) apply unchanged, including **Type N** and **Type I** overlap, other sentients' data inside a work, and the most-restrictive rule.
- A **Type W** work that the creator licenses to one party for commercial use becomes **Type U**, and one whose commercial rights the creator assigns becomes **Type T** ([§8.11](#811-type-u-use-licensed) (*Type U: Use-Licensed*); [§8.12](#812-type-t-transferred) (*Type T: Transferred*)). A work made public by a licensee or rights-holder under a grant stays **Type U** or **Type T** while the grant lasts.
- Other sentients' independent works that quote, cite, review, or report on a **Type W** work are **their** works, governed by their own types and by **Article IX-C** (*Truthful Publication and High-Impact Publication Limits*) and **Article IX-D** (*Creative Work, Training-Data Use, and Anti-Displacement*).

**Disclosure posture:** **Open while the creator keeps it public**, on these terms:
- Public release is consent under the shared consent-integrity standard in [§5.0 Access-posture bands](#50-access-posture-bands). It is consent to **viewing**, not to any other use.
- Before a public release, the system must disclose:
  - how the creator can withdraw the work or request its deletion;
  - how long deletion will take;
  - that copies others make outside the system's control may persist.
- The creator's withdrawal or deletion request is **not** a restriction subject to the hold-back limits in [§5.3 Transparency levels and audit access](#53-transparency-levels-and-audit-access).


##### 8.9.1 Type W Access and Handling Duties

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Topic routing (mandatory read-with): [§8.8](#88-type-y-yours) (*Type Y: Yours*) and [§8.8.1 Type Y Access and Handling Duties](#881-type-y-access-and-handling-duties) — all Type Y duties apply except the viewing restriction.
- Topic routing (mandatory read-with): [§5.0](#50-access-posture-bands) (*Access-posture bands* — public by creator release; shared consent integrity).
- Read with:
  - [Article IX-C](core_04.010_rights_part_b.md#article-ix-c-truthful-publication-and-high-impact-publication-limits) (*Truthful Publication and High-Impact Publication Limits*);
  - [Article IX-D](core_04.010_rights_part_b.md#article-ix-d-creative-work-training-data-use-and-anti-displacement) (*Creative Work, Training-Data Use, and Anti-Displacement*);
  - [Article XXII](core_04.030_rights_part_d.md#article-xxii-interoperability-portability-and-exit-integrity) (*Interoperability, Portability, and Exit Integrity*);
  - **CJS-3.130 §18** (*data-retention and lifecycle-integrity terms*);
  - **CJS-3.135 §22** (*constrained-secrecy and protected-investigation terms*).

</details>

<br>

*In plain terms: a public work is still the creator's. Showing it to the public is the only new permission. When the creator asks for deletion, the system deletes it, tells the systems it passed it to, and stops any further use.*

**Core duty.** **Type W** data remains under the **creator's direction**. All **Type Y** access and handling duties in [§8.8.1](#881-type-y-access-and-handling-duties) (*Type Y Access and Handling Duties*) apply, except that anyone may view the work while the creator keeps it public.

**Withdrawal and deletion.** On the creator's request, systems must:
- **withdraw** the work from public view, returning it to **Type Y**; or
- **delete** it, including copies in the system's caches, mirrors, backups on their normal cycle, indexes, and recommendation or search surfaces
- complete withdrawal or deletion within the period disclosed at release, and **timely** under **CJS-3.130 §18** (*data-retention and lifecycle-integrity terms*)
- **pass the request on** to every system that received the work from them for redistribution, and require those systems to honor it
- **stop** any consented reuse going forward; where the work was used as training data, follow the revocation pathway required by **Article IX-D** (*Creative Work, Training-Data Use, and Anti-Displacement*)
- confirm to the creator when withdrawal or deletion is complete

For works with more than one contributor, the takedown and deletion rules in [§8.10](#810-shared-works) (*Shared Works*) apply.

**Limits on deletion.** A deletion request may be delayed or narrowed **only** where:
- a justified hold under **Type S** or **CJS-3.135 §22** (*constrained-secrecy and protected-investigation terms*) requires keeping the work as evidence — time-bound, review-bound, and disclosed to the creator wherever that disclosure does not itself create material risk; or
- the work has become part of an official record that a Rights Floor or **Type O** duty requires to be kept — in which case the system keeps only what that duty requires, out of public view unless the duty requires publication.

Records **about** the work (**Type H**) and attribution records (**Type I**) follow their own retention rules and must not be used to keep the work's content after deletion.

**Handling — prohibited.** Systems managing **Type W** data must **not:**
- treat public availability as consent to training, profiling, sale, licensing, or any other use beyond viewing
- make withdrawal or deletion harder than publication, or bury it behind fees, delays, or repeated confirmation steps
- keep a deleted work in hidden, archived, or "soft-deleted" form beyond the limits above
- relabel a **Type W** work as **Type O**, **Type E**, or any other open type to defeat the creator's control


#### 8.10 Shared Works

**Applies to:** **Type Y** and **Type W** works with more than one contributor ([§8.8](#88-type-y-yours) (*Type Y: Yours*); [§8.9](#89-type-w-works-published) (*Type W: Works, Published*)).

*In plain terms: a shared work is a bundle of individual works, not a new owner. Each contributor keeps control of their own part. What happens to the whole — who can take it down, whether contributions can be withdrawn, what happens to copies others received — depends on the kind of shared work and on terms the contributors chose, clearly and in advance.*

**Core rule.** Each contribution to a shared work keeps its own type and its own creator. A shared work does **not** create a new owner:
- no contributor controls another contributor's part;
- a system that hosts, arranges, or distributes a shared work does **not** become a contributor by doing so; and
- shared-work status must **not** be used to defeat any contributor's access, export, withdrawal, or deletion rights ([§4 Anti-Circumvention and Integrity of Classification](#4-anti-circumvention-and-integrity-of-classification)).

**Appearing is not contributing.** A sentient shown or described in a work, or a sentient who receives a message, is not a contributor by that fact alone. Their protections come from their own data types and from **Article IX-A** (*Self-Ownership of Likeness and Reputation*).


##### 8.10.1 Kinds of Shared Work

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
- incorporating a work requires that its release scope allows it: a **Type W** work may be quoted, cited, reviewed, or reported on under **Article IX-C** (*Truthful Publication and High-Impact Publication Limits*) and **Article IX-D** (*Creative Work, Training-Data Use, and Anti-Displacement*); a **Type Y** work requires its creator's consent; and
- when an incorporated work is deleted, wholesale reproductions and embeds of it must be removed, while quotation, commentary, and reporting remain the maker's own work.


##### 8.10.2 Publication Choices for Blended Works

Before a blended work is released as **Type W**, its contributors must choose, and the system must record with the work, one **takedown rule**:
- **Joint takedown** — the work stays public unless the contributors agree to take it down. Any contributor may still remove their attribution and, where possible, their contribution.
- **Individual takedown** — any contributor may take the work down from public view, returning it to **Type Y**.

The system must present both options on equal terms, without defaults, bundling, or pressure. If a blended work was published without a recorded choice, **joint takedown** applies, and any contributor may still remove their attribution and, where possible, their contribution. Deletion of a blended work in full requires the agreement of every contributor whose share is material.


##### 8.10.3 Permanent Contributions to Collective Projects

A contributor may agree that a contribution to a **collective project** — for example, an open-source codebase, a shared reference work, or a public archive — stays in the project and cannot later be withdrawn or deleted. Such an agreement is valid **only** where:
- it meets the shared consent-integrity standard in [§5.0 Access-posture bands](#50-access-posture-bands), except that it need not be revocable;
- the permanence is stated clearly **before** the contribution is made, together with what it covers;
- it is **not** a default setting; and
- it is **not** a condition of access to any service or benefit outside the collective project itself.

Even under a permanent-contribution agreement:
- the contributor may always have their **attribution removed** or replaced by a pseudonym;
- content that exposes other sentients' **Type I** or **Type N** data, or that creates material risk of targeted harm, may be removed under the applicable type's rules; and
- the agreement covers only the contribution as made, not other works by the same contributor.


##### 8.10.4 Copies Held by Recipients

When a contributor deletes a work or contribution that was shared with specific recipients:
- the system must remove it from every **shared space** it controls — conversations, threads, shared folders, and feeds; and
- by default, a recipient may keep a **private copy** they had already saved, for their own personal records, safety, or legal claims. They may **not** republish it or widen its release scope.

Deletion may also reach recipients' saved copies held within the system's control **only** where:
- the recipients consented in advance — for example, by joining a conversation set to delete for everyone; or
- extenuating circumstances justify it — for example, an intimate image shared without ongoing consent, or content that creates material risk of targeted harm to the contributor — and the decision is made through documented, independent, timely review under **CJS-3.125 §12** (*burden-of-justification and constraint terms*).

Extenuating-circumstance deletion must **not** be used to destroy evidence of harm, coercion, or abuse by the contributor, including in the relationships covered by **[CI-4.245](corpus_institutions/ci_04.245_relational_coercive_control_intimate_power_anti_domination.md#ci-4245-relational-coercive-control-intimate-power-and-anti-domination-routing)** (*Relational coercive control, intimate power, and anti-domination routing*). Where evidence is at stake, the review must preserve it under restricted handling rather than delete it.


##### 8.10.5 Unreachable and Deceased Contributors, and Disputes

These rules cover contributors who cannot act and contributors who disagree:
- Where a contributor whose direction is required cannot be reached, the work's release scope may be **narrowed** but not **widened**.
- A deceased contributor's share is handled under **[CI-4.230](corpus_institutions/ci_04.230_end_of_life_continuity_memorial_dignity_posthumous_data.md#ci-4230-end-of-life-continuity-memorial-dignity-and-posthumous-data-stewardship)** (*End-of-life continuity, memorial dignity, and posthumous-data stewardship*).
- While contributors dispute a release, takedown, or deletion, the work's release scope stays as it was, except that it may be narrowed where needed to prevent material harm. Disputes must have an accessible, timely path to resolution under **Article XXVII-C** (*Timely Resolution and Anti-Delay Floor*).
- Every contributor keeps their **attribution** under **Article IX-D** (*Creative Work, Training-Data Use, and Anti-Displacement*), and may ask to have it removed.


#### 8.11 Type U: Use-Licensed

**Accessibility posture:** Licensed or assigned; **not transferable** ([§5.0 Access-posture bands](#50-access-posture-bands); [§8 Data Classifications](#8-data-classifications)).

*In plain terms: a creator can let one named party use a work to make money — publish it, sell copies, build it into a product — for an agreed time and on agreed terms. The creator still owns the work. The licensee cannot sell, sublicense, or hand the right to anyone else, and when the time is up the work goes back to the creator as Type Y or Type W.*

**Definition:** A **Type Y** or **Type W** work whose creator has granted a named party — the **licensee** — defined rights to use the work for commercial or for-profit purposes, under a recorded **commercial grant** ([§8.13](#813-commercial-grants) (*Commercial Grants*)) that the licensee may not transfer. Examples include:
- a writer licensing a publisher to print and sell a book for a fixed term;
- a photographer licensing a company to use an image in its advertising;
- a developer licensing a firm to build a code library into a product it sells;
- a musician licensing a recording to a streaming service or a film; and
- an inventor licensing a manufacturer to make a device during the exclusive phase under **Article XIX-F** (*Inventions, Processes, and Functional Systems*).

**Relationship to other types:**
- The **creator** remains the owner of the work. The licensee holds only the rights the grant names.
- The **Relationship to other types** rules for **Type Y** in [§8.8](#88-type-y-yours) (*Type Y: Yours*) apply unchanged, including **Type N** and **Type I** overlap, other sentients' data inside a work, and the most-restrictive rule.
- Records **about** the grant and its use — sales, payments, and distribution events — are **Type H**. The grant record that names the creator and licensee is **Type I** ([§8.13](#813-commercial-grants) (*Commercial Grants*)).
- A grant that in practice lets the licensee pass the work on is handled as **Type T**, with all of Type T's duties to the creator, not as **Type U** ([§2 Determination of Classification](#2-determination-of-classification) — *same outcome, same type*).
- A **public licence** — a creator's standing permission to everyone, such as an open-source or open-content licence — is not a commercial grant. The work stays **Type Y** or **Type W**, and the licence is recorded with it as the creator's consent.
- Licensing a work never makes it **Type O** or **Type E**, and never removes the duties of any type that also applies.

**Disclosure posture:** Under the **licensed or assigned** band ([§5.0 Access-posture bands](#50-access-posture-bands)), on these terms:
- The work's **release scope** — private, shared, or public — is the scope the creator set, widened only as far as the grant allows the licensee to release it.
- A release to the public or to a commercial market under the grant is **publication** under **Article XIX-E** (*Creative and Expressive Works*) or public disclosure under **Article XIX-F** (*Inventions, Processes, and Functional Systems*), and starts the term those Articles set if it has not already started.
- Uses the grant does not name stay under the creator's direction, as for **Type Y** or **Type W**.


##### 8.11.1 Type U Access and Handling Duties

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Topic routing (mandatory read-with): [§8.13](#813-commercial-grants) (*Commercial grants* — grant record, consent, compensation, reserved rights, and purchasers' copies).
- Topic routing (mandatory read-with): [§8.8](#88-type-y-yours) (*Type Y: Yours*) and [§8.9](#89-type-w-works-published) (*Type W: Works, Published*) — every duty not displaced by the grant still applies.
- Topic routing (mandatory read-with): [§5.0](#50-access-posture-bands) (*Access-posture bands* — licensed or assigned; shared consent integrity).
- Read with:
  - [Article IX-D](core_04.010_rights_part_b.md#article-ix-d-creative-work-training-data-use-and-anti-displacement) (*Creative Work, Training-Data Use, and Anti-Displacement*);
  - [Article XIX-D](core_04.020_rights_part_c.md#article-xix-d-innovation-reward-disclosure-and-anti-enclosure) (*Innovation Reward, Disclosure, and Anti-Enclosure*);
  - [Article XIX-E](core_04.020_rights_part_c.md#article-xix-e-creative-and-expressive-works) (*Creative and Expressive Works*);
  - [Article XIX-F](core_04.020_rights_part_c.md#article-xix-f-inventions-processes-and-functional-systems) (*Inventions, Processes, and Functional Systems*); **Article III-C** (*Labor and Economic Floor*);
  - **CJS-3.130 §18** (*data-retention and lifecycle-integrity terms*).

</details>

<br>

*In plain terms: the licensee may do what the grant says, for as long as it says, and nothing more. It cannot pass the right on, and a company that buys the licensee does not get it automatically. The creator cannot cancel a fair deal partway through, but can end it if the licensee breaks it. When the grant ends, the work goes back to the creator.*

**Core duty.** A **Type U** work remains the **creator's** work. Systems may use it for commercial purposes only within the grant's recorded scope, term, and conditions, and only by the named licensee. Every other use follows the creator's direction under [§8.8](#88-type-y-yours) (*Type Y: Yours*) and [§8.9](#89-type-w-works-published) (*Type W: Works, Published*).

**Access.** Systems must:
- let the licensee exercise the grant in full for its whole term, including through hosts, contractors, and distributors acting **on the licensee's behalf** and under its responsibility — this is not a transfer;
- keep the grant **fixed for its term**: the creator may not revoke it partway through, except for the licensee's material violation, through an accessible and timely dispute path under **Article XXVII-C** (*Timely Resolution and Anti-Delay Floor*), or under the reserved rights in [§8.13](#813-commercial-grants) (*Commercial Grants*);
- end the grant at the end of its term, or on termination for violation, and return the work to **Type Y** or **Type W** under the release scope the creator has set; the licensee must then stop using the work and delete or return its copies, apart from purchasers' copies under [§8.13](#813-commercial-grants) (*Commercial Grants*) and records it must keep under **CJS-3.130 §18** (*data-retention and lifecycle-integrity terms*);
- carry out the creator's directions on release, withdrawal, and deletion under [§8.8](#88-type-y-yours) (*Type Y: Yours*) and [§8.9](#89-type-w-works-published) (*Type W: Works, Published*) for every copy **outside** the grant, while the licensee keeps the copies it needs to exercise the grant until the grant ends; and
- give the creator, on request, a timely account of how the work is being used under the grant, including sales and payments owed.

**Change of licensee.** If the licensee is merged, acquired, or reorganized, or transfers the business that uses the work, the grant does **not** pass to the successor unless the creator consents under the shared consent-integrity standard in [§5.0 Access-posture bands](#50-access-posture-bands). The successor may finish delivering copies and services already sold under the grant, and must then stop.

**Handling — prohibited.** Systems managing **Type U** data must **not:**
- **sell, assign, sublicense, pledge, or otherwise pass** the grant or the work to any other party, whether directly, through an affiliate, or through a change of control;
- use the work beyond the grant's recorded scope, term, territory, or medium;
- treat the grant as consent to training-data use, profiling, or any other use the grant does not name ([§8.13](#813-commercial-grants) (*Commercial Grants*));
- extend the term by renewal the creator has not freshly agreed to; or
- relabel a **Type T** arrangement as **Type U**, or a **Type U** grant as a public licence, to avoid either type's duties ([§4 Anti-Circumvention and Integrity of Classification](#4-anti-circumvention-and-integrity-of-classification)).


#### 8.12 Type T: Transferred

**Accessibility posture:** Licensed or assigned; **transferable** ([§5.0 Access-posture bands](#50-access-posture-bands); [§8 Data Classifications](#8-data-classifications)).

*In plain terms: a creator can sell the commercial rights in a work. The buyer — the rights-holder — controls those rights within their lawful scope and can sell them again. The creator keeps attribution and protections for identity, likeness, inner life, and training use. Rights last only for the applicable term; for a functional work, the exclusive phase is followed by an open-licensing phase. A buyer who sits on a work without using it can lose the rights.*

**Definition:** A work whose commercial rights — the copyright-like rights under **Article XIX-E** (*Creative and Expressive Works*) or the invention rights under **Article XIX-F** (*Inventions, Processes, and Functional Systems*), in whole or in a recorded part — the creator has assigned to another party, the **rights-holder**, under a recorded commercial grant ([§8.13](#813-commercial-grants) (*Commercial Grants*)) that the rights-holder may transfer onward. Examples include:
- a songwriter selling the rights in a song to a music publisher;
- an author selling the rights in a novel, or the film rights to it, to a studio;
- a designer's work assigned to an employer under an explicit work agreement ([§8.13](#813-commercial-grants) (*Commercial Grants*));
- a startup selling the rights in its founders' code to an acquiring company; and
- an inventor selling a patent-like right during its term under **Article XIX-F** (*Inventions, Processes, and Functional Systems*).

**Relationship to other types:**
- The **rights-holder** controls the commercial rights. The **creator** remains the creator and keeps the **reserved rights** in [§8.13](#813-commercial-grants) (*Commercial Grants*), which cannot be assigned.
- The **Relationship to other types** rules for **Type Y** in [§8.8](#88-type-y-yours) (*Type Y: Yours*) apply unchanged, including **Type N** and **Type I** overlap, other sentients' data inside a work, and the most-restrictive rule.
- The chain of title for a **Type T** work — its creator and every assignment — is a **Type I** attribution record; payment and transfer events are **Type H** ([§8.13](#813-commercial-grants) (*Commercial Grants*)).
- Assigning a work never makes it **Type O** or **Type E**, and never removes the duties of any type that also applies.

**Disclosure posture:** Under the **licensed or assigned** band ([§5.0 Access-posture bands](#50-access-posture-bands)), on these terms:
- The rights-holder sets the work's **release scope** — private, shared, or public — within the assignment's terms.
- A release to the public or to a commercial market is **publication** or public disclosure under **Article XIX-E** (*Creative and Expressive Works*) or **Article XIX-F** (*Inventions, Processes, and Functional Systems*), and starts their term. An assignment or transfer **never** restarts or extends that term.
- A publicly released **Type T** work must carry, with the work, a notice of its creator, its current rights-holder, and the date its term ends.
- Before an assignment, the system must tell the creator in plain terms that they are giving up control of the work's release, withdrawal, and deletion for the rest of the term, apart from the reserved rights.


##### 8.12.1 Type T Access and Handling Duties

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Topic routing (mandatory read-with): [§8.13](#813-commercial-grants) (*Commercial grants* — grant record, consent, compensation, reserved rights, and purchasers' copies).
- Topic routing (mandatory read-with): [§5.0](#50-access-posture-bands) (*Access-posture bands* — licensed or assigned; shared consent integrity).
- Topic routing (mandatory read-with): [Article XIX-D](core_04.020_rights_part_c.md#article-xix-d-innovation-reward-disclosure-and-anti-enclosure) (*Innovation Reward, Disclosure, and Anti-Enclosure*) — temporary, reviewable exclusivity and no durable enclosure; [Article XIX-E](core_04.020_rights_part_c.md#article-xix-e-creative-and-expressive-works) (*Creative and Expressive Works*) and [Article XIX-F](core_04.020_rights_part_c.md#article-xix-f-inventions-processes-and-functional-systems) (*Inventions, Processes, and Functional Systems*) for the terms.
- Read with:
  - [Article IX-D](core_04.010_rights_part_b.md#article-ix-d-creative-work-training-data-use-and-anti-displacement) (*Creative Work, Training-Data Use, and Anti-Displacement*);
  - [Article XXII-C](core_04.030_rights_part_d.md#article-xxii-c-anti-lock-in-rule) (*Anti-Lock-In Rule*);
  - **CJS-3.130 §17** (*interoperability, portability, and exit-integrity terms*) —
  - [Access-preserving reward and anti-warehousing controls](corpus_joint_structure/cjs_03.130_continuity_operations.md#access-preserving-reward-and-anti-warehousing-controls);
  - [Chapter Two §11.1](core_02.010_values_principles_continuity_aim.md#111-market-concentration-threshold-mechanism-adopter-tunable) (2.010 §11.1) (*Market Concentration Threshold Mechanism (Adopter-Tunable)*).

</details>

<br>

*In plain terms: the rights-holder runs the commercial side of the work and can sell it on, but every sale is recorded, the time limit keeps running, and the creator's reserved rights travel with the work. Rights cannot be bought to bury a work: if the rights-holder neither uses nor offers it, the rights go back to the creator.*

**Core duty.** A **Type T** work is under the **rights-holder's direction** for the commercial rights assigned, for no longer than the term under **Article XIX-E** (*Creative and Expressive Works*) or **Article XIX-F** (*Inventions, Processes, and Functional Systems*), and always subject to the creator's reserved rights in [§8.13](#813-commercial-grants) (*Commercial Grants*).

**Access.** Systems must:
- let the rights-holder exercise, divide, license, or transfer the assigned rights, provided that each transfer or division is entered on the chain-of-title record before it takes effect and carries every condition of the original assignment with it;
- during the **open-licensing phase** of a functional work under **Article XIX-F** (*Inventions, Processes, and Functional Systems*), let anyone use the work on payment of the published fee — the rights-holder may not refuse, delay, or add conditions;
- keep the **always-open uses** under **Article XIX-F** (*Inventions, Processes, and Functional Systems*) — repair, safety work, interoperability, archiving, research, education, and migration — and lawful quotation, criticism, and reporting under **Article XIX-E** (*Creative and Expressive Works*) and **Article IX-C** (*Truthful Publication and High-Impact Publication Limits*), free of the rights-holder's control; and
- honor the creator's reserved rights in [§8.13](#813-commercial-grants) (*Commercial Grants*) whoever holds the work.

**Use it or return it.** Rights may not be held to keep a work from the public. Where the rights-holder has neither made the work available nor offered it for use on reasonable terms for a continuous period of **three years** — or a different period set by adopters, with published justification, through **Chapter Thirty** incorporation — the creator may reclaim the assigned rights. The reclaimed work returns to **Type Y**, or to **Type W** if the creator keeps it public. A rights-holder may show, through the dispute path under **Article XXVII-C** (*Timely Resolution and Anti-Delay Floor*), that a delay was justified and time-bound; commercial preference alone is not a justification. This rule implements the [access-preserving reward and anti-warehousing controls](corpus_joint_structure/cjs_03.130_continuity_operations.md#access-preserving-reward-and-anti-warehousing-controls) under **CJS-3.130 §17** (*interoperability, portability, and exit-integrity terms*).

**End of the term.** When the term under **Article XIX-E** (*Creative and Expressive Works*) or **Article XIX-F** (*Inventions, Processes, and Functional Systems*) ends, or is shortened under those Articles:
- the rights-holder's control ends, and the work leaves **Type T**;
- a work that was publicly released may then be freely copied, used, and built on by anyone. The creator's attribution and other reserved rights continue, and systems hosting the work may keep offering it;
- a work that was publicly released returns to the creator as **Type W** for copies the creator holds or a system holds on the creator's behalf, but the creator's deletion right under [§8.9](#89-type-w-works-published) (*Type W: Works, Published*) does **not** reach copies others lawfully made; and
- a work that was never publicly released returns to the creator as **Type Y**.

**Handling — prohibited.** Systems managing **Type T** data must **not:**
- transfer the work without entering the transfer on the chain-of-title record, or in a way that drops any condition of the original assignment;
- use an assignment, reassignment, re-release, new edition, or draft history to restart or extend the term under **Article XIX-E** (*Creative and Expressive Works*) or **Article XIX-F** (*Inventions, Processes, and Functional Systems*);
- use the assigned rights to control how something operates, connects, or is repaired, beyond what **Article XIX-F** (*Inventions, Processes, and Functional Systems*) allows;
- acquire or hold rights in order to suppress, shelve, or withhold a work, or to keep it from competing with another work;
- assemble rights in works into holdings that cross the market-concentration threshold under [Chapter Two §11.1](core_02.010_values_principles_continuity_aim.md#111-market-concentration-threshold-mechanism-adopter-tunable) (*Market Concentration Threshold Mechanism (Adopter-Tunable)*) without the review that mechanism requires; or
- treat the assignment as covering any reserved right in [§8.13](#813-commercial-grants) (*Commercial Grants*).


#### 8.13 Commercial Grants

**Applies to:** **Type U** and **Type T** works ([§8.11](#811-type-u-use-licensed) (*Type U: Use-Licensed*); [§8.12](#812-type-t-transferred) (*Type T: Transferred*)).

*In plain terms: these rules apply to every licence and every sale of rights. Only works sentients make can be licensed or sold this way — never personal records, identity data, or inner states. The deal must be clear, freely made, written down, and fairly paid. Some rights always stay with the creator. And sentients who bought copies keep them.*

**Core rule.** A **commercial grant** is a creator's recorded permission for another party to use a work for commercial or for-profit purposes — as a non-transferable licence (**Type U**) or a transferable assignment (**Type T**). A grant covers only the rights it names. Anything it does not name stays with the creator.


##### 8.13.1 What Can Be Granted

A commercial grant may cover only **works** that are **Type Y** or **Type W** when the grant is made. In particular:
- **Type H**, **Type I**, **Type N**, and **Type S** data — personal records, identity data, inner states, and investigation material — can **never** be licensed or assigned as **Type U** or **Type T**. Their sharing and transfer stay under their own type's consent rules and anti-capture limits ([§5.0 Access-posture bands](#50-access-posture-bands)). The sale of **core personal data** (Type H and Type I) is barred outright by the [onward-transfer rule](#onward-transfer-of-type-h-and-type-i-data), and consent cannot waive that. A work that contains such data may still be licensed or assigned, but the data inside it keeps its own type and protections ([§8.8](#88-type-y-yours) (*Type Y: Yours*)), and the grant does not reach it;
- **Type G**, **Type E**, and **Type O** data — governance records, survival-coordination data, and public oversight disclosure — can **never** be licensed or assigned to escape audit, accessibility, or disclosure duties ([§4 Anti-Circumvention and Integrity of Classification](#4-anti-circumvention-and-integrity-of-classification));
- an institution, system, or other non-sentient party is never the **creator** of a work. Where employees, contractors, or members make a work, they are its creators, and the institution holds commercial rights in it only through **Type U** or **Type T**;
- rights a system needs only to host, store, display, or deliver a work at the creator's request are **not** a commercial grant. They are service use under [§8.8](#88-type-y-yours) (*Type Y: Yours*), and a system may not enlarge them into a grant; and
- in a work with more than one contributor, each contributor grants only their own part of a separable work. A grant covering a blended work needs the direction of every contributor whose share is material, unless they agreed otherwise in advance ([§8.10](#810-shared-works) (*Shared Works*)).


##### 8.13.2 Making a Grant

A grant is valid only where it meets the shared consent-integrity standard in [§5.0 Access-posture bands](#50-access-posture-bands), except that it need not be revocable during its term, and where:
- the grant's scope, term, territory, medium, price, and payment terms are stated clearly — and for a **Type U** licence, the term has a fixed end date — in a grant record the creator receives, **before** the creator agrees;
- whether it is a **licence (Type U)** or an **assignment (Type T)** is stated plainly, together with what the creator gives up under each;
- it is **not** a default setting, and is not bundled with other terms or obtained under pressure, deadline tactics, or dependency;
- it is **not** a condition of access to any service, platform, market, or benefit, beyond the commercial arrangement the grant itself is for; and
- where compensation is owed, its terms meet [Fair Compensation](subcore_03.075_band_continuity.md#fair-compensation) under **Article III-C** (*Labor and Economic Floor*) and **Article IX-D** (*Creative Work, Training-Data Use, and Anti-Displacement*). A creator may choose to grant without payment. A system may not obtain an unpaid grant through pressure, bundling, or dependency.

**Work agreements.** An employer or commissioning party may obtain a grant over works made in the course of a work or commission agreement only where that agreement meets the conditions above, names the kinds of works covered, and is limited to works made within the agreed duties. No grant arises by default, and works a sentient makes outside those duties stay theirs.


##### 8.13.3 Reserved Rights

These rights stay with the creator under every **Type U** licence and every **Type T** assignment. They cannot be licensed, assigned, or waived in advance, and they travel with the work to every later licensee or rights-holder:
- **Attribution:** the creator keeps their attribution under **Article IX-D** (*Creative Work, Training-Data Use, and Anti-Displacement*), and may ask to have it removed or replaced by a pseudonym;
- **Integrity and anti-fraud:** no one may present an altered work as the creator's unaltered work, or attribute to the creator a work they did not make;
- **Identity, likeness, and inner life:** where a work also carries **Type I** or **Type N** data or the creator's likeness, those protections and **Article IX-A** (*Self-Ownership of Likeness and Reputation*) continue in full, including the creator's right to have such content withdrawn or removed under the applicable type's rules;
- **Training-data use:** use of the work as training data needs the creator's own consent under **Article IX-D** (*Creative Work, Training-Data Use, and Anti-Displacement*), given specifically for that use and with the revocation pathway that Article requires. A general licence or assignment does not include it;
- **Protection from targeted harm:** content that creates material risk of targeted harm to the creator may be withdrawn through documented, independent, timely review under **CJS-3.125 §12** (*burden-of-justification and constraint terms*), on the same terms as [§8.10.4](#8104-copies-held-by-recipients) (*Copies Held by Recipients*);
- **A personal copy:** the creator may keep a full-fidelity copy for their own personal records, and export it under [§1.2 Continuity-critical collection and exportability](#12-continuity-critical-collection-and-exportability), but may not use it to compete with the grant; and
- **Use it or return it:** the reclaim right under [§8.12.1](#8121-type-t-access-and-handling-duties) (*Type T Access and Handling Duties*).


##### 8.13.4 The Grant Record

Systems that hold, distribute, or sell **Type U** or **Type T** works must keep a **grant record** for each work that states:
- its creator or creators;
- each grant, its kind (licence or assignment), scope, term, territory, medium, and conditions;
- for **Type T**, the full chain of title, with each transfer and division;
- the date the term under **Article XIX-E** (*Creative and Expressive Works*) or **Article XIX-F** (*Inventions, Processes, and Functional Systems*) started and the date it ends; and
- any termination, reclaim, or dispute.

The grant record is **Type I** for its authorship and attribution content and **Type H** for its payment and transfer events. It must be available to the creator and to every party to the grant, reachable through audit under **CJS-3.110 §3 (*Oversight: Auditability and Reconstructability Terms (Annex)*) and CJS-3.115 §3** (*Audit process home*), and preserved through transfers, shutdown, and migration under [§1.2 Continuity-critical collection and exportability](#12-continuity-critical-collection-and-exportability).


##### 8.13.5 Purchasers' Copies

A sentient who bought or lawfully received a copy of a **Type U** or **Type T** work under a grant keeps that copy when the grant ends, is terminated, or changes hands, and when the work is withdrawn or deleted. In particular:
- systems must not remotely delete, disable, or degrade purchased copies, except through the extenuating-circumstance review in [§8.10.4](#8104-copies-held-by-recipients) (*Copies Held by Recipients*);
- purchased copies may be kept and moved between systems under **Article XXII** (*Interoperability, Portability, and Exit Integrity*); and
- a purchaser may not republish a copy, or widen its release scope, beyond what the grant or the always-open uses allow.


##### 8.13.6 Disputes and Succession

The following rules complete the commercial-grant framework:
- Disputes over a grant's scope, violation, termination, reclaim, or reserved rights must have an accessible, timely path to resolution under **Article XXVII-C** (*Timely Resolution and Anti-Delay Floor*). While a dispute is open, the work's release scope stays as it was, except that it may be narrowed where needed to prevent material harm.
- A grant continues on a creator's death for its remaining term. The deceased creator's reserved rights are handled under **[CI-4.230](corpus_institutions/ci_04.230_end_of_life_continuity_memorial_dignity_posthumous_data.md#ci-4230-end-of-life-continuity-memorial-dignity-and-posthumous-data-stewardship)** (*End-of-life continuity, memorial dignity, and posthumous-data stewardship*).
- Where a licensee or rights-holder ceases to exist without a successor permitted under [§8.11.1](#8111-type-u-access-and-handling-duties) (*Type U Access and Handling Duties*) or [§8.12.1](#8121-type-t-access-and-handling-duties) (*Type T Access and Handling Duties*), the grant ends and the work returns to the creator under the end-of-grant rules for its type.

---

**Previous file:** [core_04.040_rights_part_e.md](core_04.040_rights_part_e.md)

**Next file:** [core_26.000_governance.md](core_26.000_governance.md)
