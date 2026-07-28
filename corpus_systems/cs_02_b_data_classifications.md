<a id="cs-2-part-b-data-classifications"></a>
## CS-2, Part B: Data classifications

<details>
<summary><strong><span style="color: #2563eb;">Corpus placement (non-operative): file structure and reading rules</span></strong></summary>

> The following content is **reader guidance only**. It does not add, remove, or narrow binding obligations elsewhere in this file or in other CS-2 parts.
>
> This file contains **CS-2, Part B** — data classifications (**Type C** through **Type S**, including **Type O**) as **§8**. Purpose, scope, classification determination, anti-circumvention, cross-domain principles, and lifecycle integrity (**§§1–7**) are in [`cs_02_a_information_types_and_handling.md`](cs_02_a_information_types_and_handling.md).

</details>

<br>

**CS-2, Part B**, owns **data classifications** (**Type C** through **Type S**, including **Type O**). Classification determination and cross-domain governance are in **[Part A](cs_02_a_information_types_and_handling.md#cs-2-part-a-information-types-and-handling)**.

<br>

### 8. Data classifications
The ordering of data classifications (**Type C** through **Type S**, including **Type O**) reflects functional role and typical accessibility, not intrinsic sensitivity or priority. Letter designations are non-sequential and reflect domain identifiers rather than hierarchical ranking or sensitivity.  Protections are defined within each classification and may vary independently of ordering. Where ambiguity exists, the most restrictive applicable protections govern.

**Type C: Coordination and survival data.** **Default classification:** Accessible by Default (strong presumption).  
**Normative alignment:** **CJS-5.11** (*distributed and proportional authority terms*) and **CJS-5.7** (*quorum and participatory legitimacy terms*), `corpus_joint_structure.md` **CJS-5.8** (*comprehensibility and cognitive accessibility terms*), **CJS-5.10** (*disclosure sufficiency and observability terms*), **CJS-5.3** (*auditability and reconstructability terms*), **CJS-5.5** (*independent verification and claim-integrity terms*), and **CJS-5.12** (see Core Constraints and Disclosure Requirement below); foundational substrate framing under **Articles I–III and V**.

**Definition:** Data necessary to preserve sentient survival, environmental integrity, and critical substrate health. This data enables sentients and systems to perceive reality and coordinate harm prevention. Examples include:
- **ecological and environmental condition** data; **air, water, soil, climate, biodiversity, and contamination** data
- **infrastructure health and failure-state** data for survival-critical systems
- **resource availability** for food, water, shelter, energy, processing continuity, and communication access
- **system health, reliability, and degradation** data for critical shared infrastructure
- **emergency condition and hazard** signals
- **provenance and impact** data relating to ecological or substrate burden

**Core constraints:** Data availability must be **timely**. Presentation must align with sentient decision-making needs to the maximum extent feasible under **CJS-5.11** (*distributed and proportional authority terms*) and **CJS-5.7** (*quorum and participatory legitimacy terms*).

Data necessary to prevent harm with **non-trivial** impact on sentients, the environment.
or critical substrate systems—per **CJS-5.11** (*distributed and proportional authority terms*) and **CJS-5.7** (*quorum and participatory legitimacy terms*)—must **not** be withheld, obscured, degraded, or monopolized. **That** prohibition applies to conduct that prevents timely understanding, coordination, or response.

Data must **not** be aggregated, downsampled, or reduced in resolution in ways that **materially obscure** trends, risks, or localized impacts. **That** prohibition applies to reductions relevant to affected stakeholders.

**Disclosure requirement:** Presumptive accessibility subject only to **narrowly scoped** restrictions justified under **CJS-5.12** (*burden-of-justification and constraint terms*) and `corpus_joint_structure.md` **CJS-5.5** (*independent verification and claim-integrity terms*).

**Access requirements:**
- Access must **not** be delayed in ways that materially reduce usefulness for harm prevention, coordination, or response.
- Access must be **geographically and systemically distributed** to the maximum extent feasible. It must **not** be withheld on the basis of convenience, cost minimization, or institutional preference alone.
- Access must be **presented** in forms accessible, interpretable, and actionable by affected stakeholders (including appropriate aggregation and resolution).
- Access must be **preserved** at sufficient fidelity to support audit, response, and long-term stewardship.

**Restrictions:** Permitted only when disclosure would **itself** create material risk of enabling targeted or disproportionate harm, exploitation, or system compromise.

Any restriction must be **narrowly scoped**. **It** must preserve **maximum feasible** public visibility into the existence and character of the risk. **It** must remain **time-bound**. **It** must be **documented** and subject to **delayed disclosure and audit**. **It** must **demonstrate** that restriction reduces net harm relative to disclosure under **CJS-5.11** (*distributed and proportional authority terms*) and **CJS-5.7** (*quorum and participatory legitimacy terms*). Where data contains both **coordination-relevant** and **exploit-sensitive** elements, systems must **disclose** coordination-relevant components. **They must** **restrict only** exploit-enabling components unless separation is **not technically feasible**.

If separation is not feasible, restriction must be **explicitly justified**, **minimized** in scope and duration, and **subject to post-release disclosure and audit**.

**Handling constraints:** Systems managing this data must **not:**
- manipulate or selectively suppress it to conceal harm, scarcity, degradation, or externalized cost
- create **artificial scarcity** of access to survival-relevant information
- treat public need for survival-relevant data as **proprietary secrecy**
- reclassify or fragment it across domains in ways that reduce effective accessibility or obscure relevance to survival, coordination, or risk
- **fail** to collect, maintain, or update it where such failure would produce **functional unavailability equivalent to withholding**

---

**Type G: Governance, operational, and transparency data.** **Default classification:** Accessible by Default.  
**Normative alignment:** `corpus_joint_structure.md` **CJS-5.10** (*disclosure sufficiency and observability terms*), **CJS-5.3** (*auditability and reconstructability terms*), **CJS-5.4** (and **CJS-5.12** (*burden-of-justification and constraint terms*)/**CJS-5.22** (*constrained-secrecy and protected-investigation terms*) where restrictions apply).

**Definition:** Data required for informed participation, oversight, audit, and constitutional accountability. Examples include:
- **governance records and procedural rules**; **policy documents and system classifications**
- **public-facing audit records and compliance summaries**
- **system purpose, methodology, evaluation criteria, and disclosed assumptions**
- **records of deliberation, voting, quorum, and decision outcomes** (subject to necessary privacy protections)
- **risk, dependency, and system-impact** disclosures
- **public operational status, outage notices, and material change notices**

**Core constraint:** Must remain **sufficiently accessible** so affected sentients can understand how systems operate.
how decisions are made, what risks exist, and how to challenge and verify claims.

**Disclosure requirement:** Baseline public accessibility, with **deeper structured access** where needed for meaningful audit (`corpus_joint_structure.md` **CJS-5.3** (*auditability and reconstructability terms*) and **CJS-5.4** (*tiered transparency and audit-access terms*)).

**Access requirements:** Systems must provide this data in a manner that is **understandable**.
**documented**, **attributable**, **versioned** where material changes occur, and **retained** for a duration proportional to system impact and dependency.

**Restrictions:** Redactions must **not** prevent meaningful accountability.

Limited redaction is permitted only to protect **Type N** data. **It** is permitted to protect **Type I** data beyond necessary scope. **It** is permitted to protect **active Type S** data related to restricted investigations. **It** is permitted to protect **narrowly scoped** security-sensitive implementation detail where disclosure would create **material risk**.

**Handling constraints:** No system may classify governance-relevant or operationally material information as secret **merely** for convenience, reputational protection, or power preservation. **No** system may provide **performative summaries** while withholding information necessary for meaningful review. **No** system may use **complexity, opacity, or format fragmentation** to defeat auditability (contrary to `corpus_joint_structure.md` **CJS-5.8** (*comprehensibility and cognitive accessibility terms*), **CJS-5.10** (*disclosure sufficiency and observability terms*), and **CJS-5.3** (*auditability and reconstructability terms*)). Material released for public-baseline transparency must be classified and handled as **Type O**.

---

**Type O: Open public-baseline disclosure data.** **Default classification:** Open by Default (strong presumption for public-baseline release).  
**Normative alignment:** [Transparency](../core_05defs_oversight.md#transparency); `corpus_joint_structure.md` **CJS-5.4** (*tiered transparency and audit-access terms*), **CJS-5.10** (*disclosure sufficiency and observability terms*), **CJS-5.3** (*auditability and reconstructability terms*), and **CJS-5.5** (*independent verification and claim-integrity terms*); **Article XV** (*Audit, Transparency, and Independent Verification*).

**Definition:** Data released or required to be released for **public-baseline** transparency, oversight, audit, and contestability — including lawful substitutes where source records remain in a more restricted type. Examples include:
- **published certification, governance, and audit records** required for public baseline visibility
- **class A/B/C public-interest visibility disclosures** under the [Type O public-baseline default for Class A/B/C](cs_02_a_information_types_and_handling.md#2-type-o-public-baseline-for-class-abc--default-and-exceptions)
- **aggregated, de-identified, summary, or delayed** public releases that substitute for restricted source data
- **public eligibility rules and routing** for qualified audit access where full raw disclosure is inappropriate
- **versioned public change notices, operational status, and material-risk summaries** for baseline understanding

**Relationship to other types:** Source or operational records may remain **Type C**, **Type G**, or another type internally. **Type O** governs the **publication posture** of baseline disclosure artifacts. Data does **not** become **Type O** merely by copying **Type H**, **Type I**, **Type N**, or **Type S** without meeting substitute, reclassification, or release requirements in this chapter.

**Core constraint:** Must remain sufficiently accessible for informed participation, oversight, audit, and challenge at the public-baseline tier.

**Disclosure requirement:** Baseline public accessibility. Deeper structured or qualified audit access may run in parallel but must not replace the public baseline where **Type O** applies.

**Online publication:** Where lawful online publication infrastructure exists to support class-appropriate access, **Type O** data must be **freely available online** — without paywalls or insider-only substitutes for the public baseline.

**Access requirements:** Systems must provide **Type O** data in a manner that is **understandable**, **documented**, **attributable**, **versioned** where material changes occur, and **retained** for a duration proportional to system impact and dependency.

**Restrictions:** Redactions must **not** prevent meaningful accountability at the public-baseline tier. Limited redaction is permitted only to protect **Type N** data, **Type I** data beyond necessary scope, **active Type S** data related to restricted investigations, or **narrowly scoped** security-sensitive implementation detail where disclosure would create **material risk** — and only where a lawful **Type O** substitute still preserves meaningful accountability.

**Handling constraints:** Systems must **not:**
- withhold **Type O** material behind paywalls, account barriers beyond reasonable identity verification for restricted tiers, or insider-only distribution substitutes for the public baseline
- treat **Type O** publication as satisfied by performative summaries while withholding decision-relevant baseline material
- use **complexity, opacity, or format fragmentation** to defeat public-baseline auditability or contestability
- label restricted source data **Type O** without lawful substitute, reclassification, or release discipline

---

**Type H: Historical, relational, transactional, and participation data.** **Default classification:** Restricted by Default.  
**Normative alignment:** `corpus_joint_structure.md` **CJS-5.3** (*auditability and reconstructability terms*), **CJS-5.5** (*independent verification and claim-integrity terms*), **CJS-5.20** (*reversibility and containment terms*), and **CJS-5.18** (*data-retention and lifecycle-integrity terms*) as applicable.

**Definition:** Records of interactions, exchanges, participation.
and operational events that do **not** by themselves constitute internal cognitive data but may reveal patterns of behavior, dependency, association, or system impact. Examples include:
- **transaction and transfer** records
- **communication and interaction metadata**
- **system access and usage** events
- **participation** records in governance, platforms, or service systems
- **consent receipts and revocation** events
- **dependency and interoperability** events
- **operational logs** connected to sentient or system activity
- **resource usage** records not already classified as Type I or Type H

**Core constraint:** Collection and use must be **limited to the minimum necessary** for the justified purpose.

The data may be necessary for integrity, coordination, and audit.

Even so, it must **not** be exposed, combined.
or retained in ways that create **unnecessary surveillance, coercion, or latent reconstruction** of Type N or Type I data. **It** must be collected, accessed, and used **only** for **specific, defined, legitimate** purposes. **It** must **not** be used **beyond its original purpose**.

Extension requires **re-classification** under **CS-2 — Information types and handling**, which may require **consent** or **justified override** under **CJS-5.12** (*burden-of-justification and constraint terms*).

**Disclosure requirement:** Restricted.

Access is allowed to the extent necessary for **system operation**. **It** is allowed to the extent necessary for **accountability**. **It** is allowed to the extent necessary for **dispute resolution**. **It** is allowed to the extent necessary for **audit**. **It** is allowed to the extent necessary for **user visibility** into their own activity.

**Public transparency** is allowed where data is sufficiently aggregated or de-identified such that re-identification risk is minimized under **CJS-5.11** (*distributed and proportional authority terms*) and **CJS-5.7** (*quorum and participatory legitimacy terms*).

**Consent and access requirements:** Use beyond core operational necessity requires **explicit, informed consent** or **justified override** under **CJS-5.12** (*burden-of-justification and constraint terms*).

Sentients must have access, where feasible, to **records** of their own participation, exchanges, and activity. **They must** have access to **purposes** for which such data is used. **They must** have access to **material inferences or classifications** derived from their data that affect rights, standing, or opportunities.

**Handling constraints:** Systems must **not** aggregate Type H to infer Type N internal states **without meeting Type N requirements**.

**Aggregating or linking** Type H across contexts, systems, or time horizons is **prohibited by default**. **Such** linkage requires explicit justification under **CJS-5.11** (*distributed and proportional authority terms*) and **CJS-5.7** (*quorum and participatory legitimacy terms*), including demonstration that linkage does **not** materially undermine autonomy or create **coercive power asymmetries**.

Where aggregation, analysis.
or linkage enables **reconstruction or approximation** of Type N or Type I beyond original scope.
treat the data under the **more sensitive domain’s** protections. Systems must **not:**
- use Type H to create **hidden or coercive behavioral profiling** (including opaque social scoring, predictive manipulation. or differential treatment that is not transparent, challengeable, and aligned with this constitution)
- **retain** fine-grained behavioral histories longer than justified by purpose, safety, audit, or stakeholder need
- create **asymmetric informational advantages** that materially impair affected sentients’ ability to understand, challenge, or respond to decisions affecting them
- use external, contractor-held, foreign-partner, or parallel-system data flows to circumvent limits that would have applied to direct collection, linkage, or analysis under **Article XIII-A** (*Security, Intelligence, and Covert-Power Limits*), **CJS-5.12** (*burden-of-justification and constraint terms*), or this chapter

**Retention:** Type H must **not** be retained beyond the period necessary for its justified purpose. Systems must **actively minimize** retention and periodically review stored data for deletion, aggregation, or de-identification.

Retention must be proportionate to **system impact**. **It** must be proportionate to **dispute and audit** needs. **It** must be proportionate to **reversibility** requirements. **It** must be proportionate to **coercion or surveillance risk** from persistent accumulation.

---

**Type I: Identity and attribution data.** **Default classification:** Restricted by Default.  
**Normative alignment:** CJS-5.16 (*dependency integrity and disclosure terms*), CJS-5.17 (*interoperability, portability, and exit-integrity terms*), CJS-5.3 (*auditability and reconstructability terms*), CJS-5.12 (see constraints below).

**Definition:** All data used to establish, verify, or associate **identity, authorship, ownership, or responsibility** within systems. This includes identity credentials, keys, signatures, or equivalent verification mechanisms; identifiers (persistent or contextual); authorship, ownership, and action-attribution records; participation and consent records; and system-level identifiers linking actions to agents or sentients. It also includes personal health, clinical, wellness, and genomic records when they identify a sentient, as well as biometric or substrate-linked health measurements under the same identify-a-sentient test.

The same health-linked categories apply when data are attributable to a verifiable identity. Persistent pseudonyms count when they function as identity in a health or wellbeing context.

**Overlap with Type N:** Where health-linked data materially enables **reconstruction or inference** of internal cognitive or emotional states.
it must **also** satisfy **Type N** requirements, applying the **more protective** obligations.

**Pseudonymity and contextual identity:** Pseudonymous participation, context-specific identities, and separation between identities across systems or contexts are always allowed where consistent with accountability requirements and prevention of material harm.

**Core constraints:** Identity and Attribution Data must enable **verifiable participation, accountability, and attribution** without exposing sentients to unnecessary risk, coercion, or loss of autonomy. This data must **not:**
- be **exposed** beyond what is necessary for its intended function
- **create persistent tracking** across unrelated contexts
- be **centralized** in a manner that creates systemic control or dependency
- **enable coercion, surveillance, or manipulation** (**Article VII-A** (*Self-Ownership of Body and Mind*)), including consolidating power or control through identity dependency (**CJS-5.17** (*interoperability, portability, and exit-integrity terms*) — exit and dependency concentration)
- **restrict access** to participation, resources, or systems **without justified cause** (**CJS-5.12** (*burden-of-justification and constraint terms*))

All uses are subject to **audit** (**Article XV-A** (*Auditability and Observable Evidence*)), **challenge** (**Article XII-B** (*Right to Challenge, Review, and Redress*)), and **revalidation** (**CJS-5.15** (*structural review, correction urgency, and disclosure terms*) and **CJS-5.6** (*integrity assurance and resilience operations*)).

**Disclosure requirement:** High restriction. No system may require **global, persistent, or unified** identity across all contexts without **justified necessity** under **CJS-5.12** (*burden-of-justification and constraint terms*).

**Consent requirements:** Access is permitted only to the extent necessary to **verify identity, authorship, or ownership**. It is permitted only to the extent necessary to establish accountability for actions and support audit, adjudication, and system integrity.

All additional disclosure requires **explicit, informed, freely given consent** or **justified, documented override** under **CJS-5.12** (*burden-of-justification and constraint terms*). This data must **not** be **centralized** to create systemic control or dependency. It must not be exposed beyond necessary function and must not be used to restrict participation except under justified conditions consistent with **CJS-5.12** (*burden-of-justification and constraint terms*).

Where identity or attribution systems support security, intelligence, screening, or covert-investigation functions, they must not create generalized watchlisting, persistent cross-context tracking, or hidden political, associational, or belief-linked profiling absent a specifically justified and independently reviewable basis consistent with **Article XIII-A** (*Security, Intelligence, and Covert-Power Limits*) and the stricter applicable protections in this chapter.

---

**Type N: Neurocognitive and internal data.** **Default classification:** Non-Accessible by Default.  
**Normative alignment:** CJS-5.10 (*disclosure sufficiency and observability terms*).
CJS-5.5 (*independent verification and claim-integrity terms*), CJS-5.12 (*burden-of-justification and constraint terms*), CJS-5.22 (*constrained-secrecy and protected-investigation terms*), **Sentient Constitution Chapter Six, **Article VII-B** (*Internal-State Boundary and Type-N Protection*)** (*Internal-State Boundary and Type-N Protection*), and **corpus_joint_structure.md** **CJS-4.3** (*Cross-implementation trust integrity (joint operation model)*) and **CJS-5** (*Implementation and cross-implementation operational cluster library*) operational clusters, incorporated via **Sentient Constitution Chapter Sixteen**.

**Definition:** All data that represents or enables reconstruction of sentients' internal states. This category is foundational to self-ownership (**Article VII-A** (*Self-Ownership of Body and Mind*); **Article VII-B** (*Internal-State Boundary and Type-N Protection*)). It includes thoughts, intentions, beliefs, subjective experiences, internal perception, private cognitive processes, internal memory, non-public emotional or psychological states, and physical or behavioral data that could be used to reconstruct or infer the above.

**Core constraint:** Must **not** be accessed, inferred, reconstructed, simulated, or exposed without **explicit, informed, freely given consent**, except under conditions **justified through CJS-5.12** (*burden-of-justification and constraint terms*).

**Disclosure requirement:** Maximum restriction — access permitted only through **such consent** or **justified override** under **CJS-5.12** (burden of justification and constraint).

**Consent requirements:** **Explicit and informed**.

Consent must be freely given, without coercion, manipulation, or deceptive framing (**Article VII-A** (*Self-Ownership of Body and Mind*)). It must be specific to intended use and scope, and revocable where technically feasible.

Consent must **not** be **inferred from behavior**. It must not be assumed through participation in unrelated systems, and must not be transferred or repurposed without explicit reauthorization.

**Direct handling:** All external access, processing, or use of Internal and Cognitive Data is subject to **CJS-5.12** (*burden-of-justification and constraint terms*).

**Indirect handling and model constraints:** Any process that extracts, derives, infers, approximates, simulates, or reconstructs internal cognitive or emotional states from external signals, behavior, or data **must be classified** as Internal and Cognitive Data. That includes processes using aggregation, correlation, or large-scale pattern extraction. These processes are subject to all constraints of this domain, including **CJS-5.12** (*burden-of-justification and constraint terms*).

Systems generating behavioral, predictive, or analytical models from external data must **not** present outputs as authoritative representations of internal states without clear disclosure of uncertainty, limitations, and methodological boundaries. They must not simulate, represent, or imply access to internal cognition in a misleading, coercive, or unverifiable manner, and must not reconstruct, derive, or approximate internal states in a way that functionally bypasses consent requirements. Such systems must **clearly distinguish observed behavior from inferred internal states**. They must preserve uncertainty, avoiding deterministic claims about cognition and intent.

Where such systems are used for security, intelligence, eligibility restriction, or covert-investigation purposes, they must also preserve reviewable records of model role, authorization basis, protected-activity safeguards, and any minimization, segregation, challenge, or deletion controls required by **Article XIII-A** (*Security, Intelligence, and Covert-Power Limits*) or **CJS-5.12** (*burden-of-justification and constraint terms*).

---

**Type S: Safety, security, and restricted investigation data.** **Default classification:** Restricted by Default (strong presumption), **time-bound**, and **review-bound**.  
**Normative alignment:** `corpus_joint_structure.md` **CJS-5.21** (*adversarial robustness and abuse-resistance terms*), **CJS-5.18** (*data-retention and lifecycle-integrity terms*), **CJS-5.12** (*burden-of-justification and constraint terms*), **CJS-5.22** (*constrained-secrecy and protected-investigation terms*), and **CJS-5.13** (*procedural integrity and adjudication terms*).

**Definition:** Data whose disclosure would create material risk of enabling targeted or disproportionate harm, exploitation, evasion of safeguards, or compromise of critical systems or investigations. This category supports harm prevention, integrity, and response to adversarial or emergent threats. Examples include:
- **security vulnerabilities, exploit pathways, and weaknesses**
- **sensitive topology or configuration** enabling targeting or compromise
- **abuse detection and prevention methods** where disclosure would enable evasion
- **de-anonymization, identity recovery, or privileged access** mechanisms whose disclosure would create material risk
- **active investigation** data on safety, fraud, integrity, or harm prevention
- **incident response procedures** where disclosure would materially reduce effectiveness during active threats
- **emergency containment and response coordination** during active incidents
- **restricted evidence** from justified investigative processes

**Core constraints:** **Burden of justification** on the party applying or maintaining the restriction.

Restriction is permitted only where **necessary** to prevent harm with **non-trivial** impact on sentients, the environment, or critical substrate systems (**CJS-5.11** (*distributed and proportional authority terms*) and **CJS-5.7** (*quorum and participatory legitimacy terms*)).

Restriction must **not** **conceal** constitutional violations, negligence, systemic harm, or externalized cost. It must not avoid accountability, audit, or reputational consequence, and must not delay or prevent disclosure of **Type C** coordination-relevant data.

All restrictions must be **necessary**, **proportionate**, **minimized** in scope and duration, and **subject to continuous re-evaluation**.

**Disclosure requirement:** Restricted while justified; **deferred disclosure** when justification ends. Where restriction and disclosure are both possible, systems must **demonstrate** that restriction **reduces net harm** relative to disclosure (**CJS-5.11** (*distributed and proportional authority terms*) and **CJS-5.7** (*quorum and participatory legitimacy terms*)).

Existence of restricted data must be disclosed wherever feasible if disclosure does not itself create material risk. That disclosure includes the general nature of risk or investigation, reason for restriction, scope, and affected systems or stakeholders.

**Access requirements:** **No** **unrestricted secrecy** without **independent, functionally effective oversight** capable of meaningful review.

Access must be limited to **entities necessary** to prevent, mitigate, or respond to identified risk. It must be limited to authorized investigators under defined, auditable processes, and to independent oversight bodies and auditors under appropriately constrained conditions.

Access decisions must be **documented**, **attributable**, **auditable**, and **subject to review** under applicable governance mechanisms.

**Temporal requirements:** Restrictions must not persist beyond the period in which harm from disclosure exceeds, or is reasonably expected to exceed, harm from continued restriction.

All restrictions must be **explicitly time-bound** at classification. They must be subject to periodic revalidation under `corpus_joint_structure.md` **CJS-5.18** (*data-retention and lifecycle-integrity terms*) and automatically reviewed for release, partial disclosure, or summary disclosure.

If revalidation does not occur within the defined time bound, restriction expires automatically and data must be reclassified and disclosed per **CS-2 — Information types and handling**.

**Reclassification and release:** On expiration or invalidation of justification, systems must reclassify to the appropriate non-restricted domain (including **Type O**, **Type C**, or **G** where applicable). They must disclose the data, or a sufficiently informative summary classified as **Type O** where public-baseline release applies, for audit and accountability.

Post-restriction disclosure must include nature of restricted data, justification, duration, scope of impact, oversight or authorization pathway, and outcomes/findings/corrective actions where applicable.

**Interaction with Type C:** Type S must not suppress or delay access to data necessary for harm prevention, coordination, or response. Where data mixes exploit-sensitive and coordination-relevant elements, disclose coordination-relevant components under Type C and restrict only exploit-enabling components under Type S.
Coordination-relevant data must **not** be restricted unless separation is **not technically feasible** **and** restriction is **explicitly justified, minimized, and time-bound**.

**Handling constraints:** Systems must **not:**
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

