## CS-3: Information types and handling

**Introductory provisions:** Systems must preserve the practical ability to publish truthful information while maintaining safeguards for harm prevention, privacy, trust, and system integrity.

Requirements and limitations scale proportionally with system classification and potential impact. They must impose proportionate safeguards on publication within their boundaries where necessary to preserve trust, safety, and constitutional compliance.

### I. Purpose and scope
**Sentient Constitution Chapter Six** (Articles **I**–**XXV**; presentation **Parts A–D**) states Foundational Rights that depend upon strong, reproducible procedures and governance. That includes info-sphere, audit, and comprehensibility hooks where they apply to data handling (e.g., **Articles XIV**, **XV**, and **XX**).

Therefore, all data must be identified as belonging to one or more of the types defined in CS-3 — Information types and handling. Where multiple classifications apply, the most restrictive applicable protections govern, subject to proportionality (**CJS-5.11** (*distributed and proportional authority terms*) and **CJS-5.7** (*quorum and participatory legitimacy terms*)).

Handling must align with Sentient Constitution Chapter Six and scale with system class under CS-4 — System classification and handling. Where data handling supports material portability, audit, repair, continuity, migration, or cross-implementation operation for **Class A**, **Class B**, or **Class C** systems, format, schema, API, and interchange-protocol choices must also satisfy `corpus_joint_structure.md` **CJS-5.17** (*interoperability, portability, and exit-integrity terms*). **Continuity-critical collection and exportability** for those classes is stated in **section VI.5** below and read with **Article II-E** (*Info-Sphere Dependency, Continuity, and Operator Non-Viability*).

**Class A/B/C public-interest visibility default.** For **Class A**, **Class B**, and **Class C** systems, data necessary to understand system purpose, classification, dependency structure, operational status, material risks, performance, failures, governance, audit outcomes, stakeholder effects, and constitutional compliance is **public by default** and must be classified as **Type P** when released for public-baseline access.

This default applies most strongly to material drawn from **Type C** and **Type G** sources. It does **not** convert **Type H**, **Type I**, **Type N**, or **Type S** data into **Type P** without lawful reclassification, aggregation, de-identification, summary disclosure, or other maximum feasible public substitute. Where privacy, internal-state protection, identity protection, safety, security, or restricted-investigation needs justify limiting raw disclosure, systems must provide the maximum feasible **Type P** public substitute, including aggregation, de-identification, summary disclosure, delayed disclosure, or qualified audit access.

Any restriction must be **narrowly scoped**, **documented**, **proportionate**, **auditable**, and **subject to challenge**. Security or investigation-based restrictions must be **time-bound** and **review-bound** under **Type S**. Restrictions must not conceal systemic behavior, constitutional violations, material risk, dependency, failure, or externalized cost.

### II. Temporal, systemic, and dependency scope of rights
Data-handling protections under CS-3 — Information types and handling apply not only to immediate and direct system effects. They also apply to delayed, cumulative, and indirect impacts arising through system interactions and dependency chains.

Where systems create or contribute to material risk to sentients, including through transitive dependencies, those risks fall within the scope of these protections. Systems must **not** externalize risk or harm across time, populations, or system boundaries. That prohibition includes layered or indirect dependencies. Those dependencies must not bypass, defer, or dilute the protections and constraints established in Sentient Constitution Chapters One through Six.

### III. Determination of classification
**Basis:** Classification and reclassification are determined by the **functional nature of the data** and **the effects it enables**.

Classification and reclassification must not be determined solely by format, origin, stage within a processing pipeline, or processing context.

**Ambiguity and default:** Where ambiguity exists, default to the **most protective applicable category**, subject to proportionality (**CJS-5.11** (*distributed and proportional authority terms*) and **CJS-5.7** (*quorum and participatory legitimacy terms*)).

Protection may be reduced only through **justified, documented override** under **CJS-5.12** (*burden-of-justification and constraint terms*). Where data may be **reconstructed, transformed, or aggregated** into a more sensitive classification, the **more sensitive** classification’s protections apply.

**Transparency and challenge:** Functional equivalence of outcome constitutes equivalence of classification.

All classification decisions and transformations must remain **transparent (`corpus_joint_structure.md` CJS-5.10 (*disclosure sufficiency and observability terms*))**, **auditable (`corpus_joint_structure.md` CJS-5.3 (*auditability and reconstructability terms*))**, and **subject to challenge (`corpus_joint_structure.md` CJS-5.13 (*procedural integrity and adjudication terms*))**.

**Misclassification:** Misclassification, evasive structuring, or functional circumvention violates **informational integrity** (**Article XIV** (*Info-Sphere Integrity*)), auditability where observable evidence is implicated (**Article XV-A** (*Auditability and Observable Evidence*)), and **applicable rights under Chapter Six, Articles V through IX**.

### IV. Anti-circumvention and integrity of classification
Data classification under CS-3 — Information types and handling is binding across all systems, processes, and transformations. **No system may:**
- **shift** data between classifications without maintaining the protections required by the **most restrictive applicable** classification
- **fragment, transform, aggregate, or re-label** data to avoid classification while preserving equivalent functional access or effect
- **structure** data pipelines, processing stages, or system boundaries to bypass applicable classification requirements
- **distribute** processing across multiple systems, stages, agents, or time-separated operations to achieve outcomes that would be prohibited if performed within a single system
- **rely** on intermediate systems, agents, or third parties to perform actions that would be prohibited if performed directly
- **de-anonymize** anonymized data except under **CJS-5.12** (*burden-of-justification and constraint terms*), with such actions **fully documented and auditable**

### V. Cross-domain governance principles
All data, regardless of classification, must be handled in accordance with the following cross-domain principles. These principles govern how classifications are applied, enforced, and interacted with across systems, and ensure alignment with **Chapter Six, Articles V through IX** and **CJS-5** (*Implementation and cross-implementation operational cluster library*) operational clusters in **corpus_joint_structure.md**.

**1. Proportional access and handling.** Access and handling must scale with **impact on sentients, the environment, and the info-sphere**.

They must also scale with stakeholder dependency and potential for harm, including irreversibility.

Higher-impact systems and actions require **greater transparency (`corpus_joint_structure.md` CJS-5.10 (*disclosure sufficiency and observability terms*))**, **deeper auditability (`corpus_joint_structure.md` CJS-5.3 (*auditability and reconstructability terms*))**, and **stronger justification** for restriction or access (**CJS-5.12** (*burden-of-justification and constraint terms*)). **No** system may claim reduced requirements while exerting **material external** effects (**CJS-5.11** (*distributed and proportional authority terms*) and **CJS-5.7** (*quorum and participatory legitimacy terms*)).

**2. Most restrictive applicable classification governs.** Where data falls under multiple classifications, the most restrictive applicable protections govern.

Reductions in protection may occur only through **proportional application** (**CJS-5.11** (*distributed and proportional authority terms*) and **CJS-5.7** (*quorum and participatory legitimacy terms*)) and **justified, documented override** (**CJS-5.12** (*burden-of-justification and constraint terms*)). Systems must **not** selectively apply less restrictive classifications to enable access, processing, or disclosure that would otherwise be prohibited.

**3. Tiered transparency and audit access.** Data access must satisfy `corpus_joint_structure.md` **CJS-5.4** (*tiered transparency and audit-access terms*) for balancing transparency, auditability, and protected-boundary constraints.

It must also balance protection of internal states and sensitive data (**Sentient Constitution Chapter Six, **Article VII-B** (*Internal-State Boundary and Type-N Protection*)**; Types **H**, **I**, **N**, and **S** in this chapter). Where applicable based on system impact (**CJS-5.11** (*distributed and proportional authority terms*) and **CJS-5.7** (*quorum and participatory legitimacy terms*)), systems must support **baseline accessibility** (sufficient visibility into behavior and effects for informed participation and risk evaluation). **Type P** governs public-baseline release posture, including lawful online publication where infrastructure exists. Systems must support qualified audit access (structured pathways for independent auditors to deeper data where verification requires it) and forensic access (full reconstruction in cases of harm, dispute, or credible risk, consistent with **CJS-5.11** (*distributed and proportional authority terms*) and **CJS-5.7** (*quorum and participatory legitimacy terms*) and **CJS-5.12** (*burden-of-justification and constraint terms*)).

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

### VI. Data separation, attribution, and lifecycle integrity
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

**Transition to full attribution:** Where systems **increase in impact**, they must transition toward **full attribution** as **CS-3 — Information types and handling** requires. **The same** applies when they **introduce persistent value, identity, or resource transfer** or **affect external systems**. **No** system may continue under **reduced attribution** once it **exceeds low-impact thresholds**.

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

### VII. Data classifications
The ordering of data classifications (**Type C** through **Type S**, including **Type P**) reflects functional role and typical accessibility, not intrinsic sensitivity or priority. Letter designations are non-sequential and reflect domain identifiers rather than hierarchical ranking or sensitivity.  Protections are defined within each classification and may vary independently of ordering. Where ambiguity exists, the most restrictive applicable protections govern.

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

**Handling constraints:** No system may classify governance-relevant or operationally material information as secret **merely** for convenience, reputational protection, or power preservation. **No** system may provide **performative summaries** while withholding information necessary for meaningful review. **No** system may use **complexity, opacity, or format fragmentation** to defeat auditability (contrary to `corpus_joint_structure.md` **CJS-5.8** (*comprehensibility and cognitive accessibility terms*), **CJS-5.10** (*disclosure sufficiency and observability terms*), and **CJS-5.3** (*auditability and reconstructability terms*)). Material released for public-baseline transparency must be classified and handled as **Type P**.

---

**Type P: Public disclosure data.** **Default classification:** Public by Default (strong presumption for public-baseline release).  
**Normative alignment:** [Transparency](../core_05defs_oversight.md#transparency); `corpus_joint_structure.md` **CJS-5.4** (*tiered transparency and audit-access terms*), **CJS-5.10** (*disclosure sufficiency and observability terms*), **CJS-5.3** (*auditability and reconstructability terms*), and **CJS-5.5** (*independent verification and claim-integrity terms*); **Article XV** (*Audit, Transparency, and Independent Verification*).

**Definition:** Data released or required to be released for **public-baseline** transparency, oversight, audit, and contestability — including lawful substitutes where source records remain in a more restricted type. Examples include:
- **published certification, governance, and audit records** required for public baseline visibility
- **class A/B/C public-interest visibility disclosures** under the default above
- **aggregated, de-identified, summary, or delayed** public releases that substitute for restricted source data
- **public eligibility rules and routing** for qualified audit access where full raw disclosure is inappropriate
- **versioned public change notices, operational status, and material-risk summaries** for baseline understanding

**Relationship to other types:** Source or operational records may remain **Type C**, **Type G**, or another type internally. **Type P** governs the **publication posture** of baseline disclosure artifacts. Data does **not** become **Type P** merely by copying **Type H**, **Type I**, **Type N**, or **Type S** without meeting substitute, reclassification, or release requirements in this chapter.

**Core constraint:** Must remain sufficiently accessible for informed participation, oversight, audit, and challenge at the public-baseline tier.

**Disclosure requirement:** Baseline public accessibility. Deeper structured or qualified audit access may run in parallel but must not replace the public baseline where **Type P** applies.

**Online publication:** Where lawful online publication infrastructure exists to support class-appropriate access, **Type P** data must be **freely available online** — without paywalls or insider-only substitutes for the public baseline.

**Access requirements:** Systems must provide **Type P** data in a manner that is **understandable**, **documented**, **attributable**, **versioned** where material changes occur, and **retained** for a duration proportional to system impact and dependency.

**Restrictions:** Redactions must **not** prevent meaningful accountability at the public-baseline tier. Limited redaction is permitted only to protect **Type N** data, **Type I** data beyond necessary scope, **active Type S** data related to restricted investigations, or **narrowly scoped** security-sensitive implementation detail where disclosure would create **material risk** — and only where a lawful **Type P** substitute still preserves meaningful accountability.

**Handling constraints:** Systems must **not:**
- withhold **Type P** material behind paywalls, account barriers beyond reasonable identity verification for restricted tiers, or insider-only distribution substitutes for the public baseline
- treat **Type P** publication as satisfied by performative summaries while withholding decision-relevant baseline material
- use **complexity, opacity, or format fragmentation** to defeat public-baseline auditability or contestability
- label restricted source data **Type P** without lawful substitute, reclassification, or release discipline

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

Extension requires **re-classification** under **CS-3 — Information types and handling**, which may require **consent** or **justified override** under **CJS-5.12** (*burden-of-justification and constraint terms*).

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

If revalidation does not occur within the defined time bound, restriction expires automatically and data must be reclassified and disclosed per **CS-3 — Information types and handling**.

**Reclassification and release:** On expiration or invalidation of justification, systems must reclassify to the appropriate non-restricted domain (including **Type P**, **Type C**, or **G** where applicable). They must disclose the data, or a sufficiently informative summary classified as **Type P** where public-baseline release applies, for audit and accountability.

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

**Previous file:** [cs_protocol_c_justice_safeguards_restitution_rehabilitation.md](cs_protocol_c_justice_safeguards_restitution_rehabilitation.md)

**Next file:** [cs_s2_system_classification_and_handling.md](cs_s2_system_classification_and_handling.md)
