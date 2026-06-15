## CJS-2: Implementation integration map
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.2](cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-2.1](cjs_02_implementation_integration_map.md#cjs-21-topic-router-stable-ids) topic router; [Chapter Fifteen](../core_15-15_incorporation.md#chapter-fifteen-incorporation-bridge) incorporation discipline and [Chapter Five](../core_05-05_definitions_a_independent.md#chapter-five-foundational-definitions) canonical definitions.
- Downstream: [CJS-2.1: Topic router (stable IDs)](#cjs-21-topic-router-stable-ids); [CJS-2.2: Intentional overlap (non-duplication discipline)](#cjs-22-intentional-overlap-non-duplication-discipline); [CJS-2.3: Two-tier definition contract (binding abstraction + owner detail)](#cjs-23-two-tier-definition-contract-binding-abstraction--owner-detail).
- Read with: **CJS-2**; [CJS-2.1](cjs_02_implementation_integration_map.md#cjs-21-topic-router-stable-ids); **CJS-2.2**; **CJS-2.3**; **CJS-3**; **CJS-3.6**; **CJS-1.2**.

</details>

<br>

*In plain terms: **CJS-2** tells you which implementation file owns which cross-cutting topic and what else to read with it. Start at **CJS-2.1** (*Topic router (stable IDs)*) for the owner map. **CJS-2.2** states how to avoid duplicating deliberately split topics. **CJS-2.3** states the two-tier definition contract for binding joint abstractions.*

### CJS-2.1: Topic router (stable IDs)
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.2](cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-2.1](cjs_02_implementation_integration_map.md#cjs-21-topic-router-stable-ids) topic router; [Chapter Fifteen](../core_15-15_incorporation.md#chapter-fifteen-incorporation-bridge) incorporation discipline and [Chapter Five](../core_05-05_definitions_a_independent.md#chapter-five-foundational-definitions) canonical definitions.
- Downstream: this section's local operational requirements for **CJS-2.1: Topic router (stable IDs)**.
- Read with: [CJS-2.1](cjs_02_implementation_integration_map.md#cjs-21-topic-router-stable-ids); **CJS-4.1**; **CJS-4.7**; **CJS-4.4**; **CJS-4.6**.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Definitions · Evaluation · Compliance</span></strong></summary>

- [Adversarial, Scaled, and Exploited Conditions](../core_05-05_definitions_a_independent.md#adversarial-scaled-and-exploited-conditions) · [O](../core_05-05_definitions_a_independent.md#adversarial-scaled-and-exploited-conditions) · [E](../core_05-05_definitions_a_independent.md#adversarial-scaled-and-exploited-conditions-e) · [C](../core_05-05_definitions_a_independent.md#adversarial-scaled-and-exploited-conditions-c)
- [Trust Degradation and Misleading Reliance](../core_05-05_definitions_c_dependent_clusters.md#trust-degradation-and-misleading-reliance) · [O](../core_05-05_definitions_c_dependent_clusters.md#trust-degradation-and-misleading-reliance) · [E](../core_05-05_definitions_c_dependent_clusters.md#trust-degradation-and-misleading-reliance-e) · [C](../core_05-05_definitions_c_dependent_clusters.md#trust-degradation-and-misleading-reliance-c)
- [Verification Accessibility](../core_05-05_definitions_c_dependent_clusters.md#verification-accessibility) · [O](../core_05-05_definitions_c_dependent_clusters.md#verification-accessibility) · [E](../core_05-05_definitions_c_dependent_clusters.md#verification-accessibility-e) · [C](../core_05-05_definitions_c_dependent_clusters.md#verification-accessibility-c)
- [Cascading Failure](../core_05-05_definitions_a_independent.md#cascading-failure) · [O](../core_05-05_definitions_a_independent.md#cascading-failure) · [E](../core_05-05_definitions_a_independent.md#cascading-failure-e) · [C](../core_05-05_definitions_a_independent.md#cascading-failure-c)
- [Trustworthiness](../core_05-05_definitions_c_dependent_clusters.md#trustworthiness) · [O](../core_05-05_definitions_c_dependent_clusters.md#trustworthiness) · [E](../core_05-05_definitions_c_dependent_clusters.md#trustworthiness-e) · [C](../core_05-05_definitions_c_dependent_clusters.md#trustworthiness-c)
- [Accessibility](../core_05-05_definitions_a_independent.md#accessibility-constitutional) · [O](../core_05-05_definitions_a_independent.md#accessibility-constitutional) · [E](../core_05-05_definitions_a_independent.md#accessibility-constitutional-e) · [C](../core_05-05_definitions_a_independent.md#accessibility-constitutional-c)
- [Reversibility](../core_05-05_definitions_a_independent.md#reversibility-constitutional) · [O](../core_05-05_definitions_a_independent.md#reversibility-constitutional) · [E](../core_05-05_definitions_a_independent.md#reversibility-constitutional-e) · [C](../core_05-05_definitions_a_independent.md#reversibility-constitutional-c)

</details>

<br>

When a topic touches more than one implementation file, use the router table below. Apply each row within the default reading stack named in **CJS-1.1** (*Joint structural boundary and owner discipline*).

- **Primary owner** — the section named in the **Primary owner** column. That is where the topic's operative rules start. A primary owner may be **CJS**, **CS**, **CI**, or **CF**.
- **Mandatory read-with** — companion sections (and core hooks where listed) that must also be satisfied when the topic materially applies. They complete the topic; they do not replace the primary owner's operative scope.

**Bidirectional routing:** This table is the authoritative integration view for each row, but routing must work both ways. The **primary owner** must cite its **CJS-R** row here and the same mandatory read-with list — or a one-line pointer to that row for the full list. Each **mandatory read-with** section must cite the row and **primary owner** where the topic materially applies. Do not maintain a second competing read-with list in the owner file.

Stable row IDs (**CJS-R01** (*Delegated binding bodies and hybrid composition (non-forum institutions)*)–**CJS-R19** (*Implementation and cross-implementation integrity assurance and resilience operations*)) are **corpus-local** labels; they are **not** Sentient Constitution article numbers.

| Row ID | Topic | Primary owner | Mandatory read-with |
|--------|--------|---------------|---------------------|
| **CJS-R01** | Delegated binding bodies and hybrid composition (non-forum institutions) | `corpus_institutions.md` **CI-9.3** | **CJS-4.1**, **CJS-4.7**, **CJS-5.7**; `corpus_systems.md` **CS-4 — System classification and handling**, **CS-5 — Critical system stewardship**; `corpus_institutions.md` **CI-3**; the CJS implementation layer **CJS-5.2 and CJS-5.12 — Distributed and Proportional Authority**, **CJS-5.5 — Burden of Justification and Constraint** (as cited in owner text) |
| **CJS-R02** | Forum chambers, divisions, and designated panels (Chapter Nine families) | `corpus_forum.md` **CF-3.5**–**CF-3.8** | **CJS-4.1**, **CJS-4.7**, **CJS-5.7**; `corpus_institutions.md` **CI-9.3**; `corpus_systems.md` **CS-4 — System classification and handling**, **CS-5 — Critical system stewardship**; `core_09-09_forum.md` **Chapter Nine** |
| **CJS-R03** | Lawful panel formation, disclosure, recusal, substitution, inability-to-form | `corpus_forum.md` **CF-4** | **CJS-4.7**, **CJS-5.7**; `corpus_institutions.md` **CI-4**, **CI-5**; `core_09-09_forum.md` **Chapter Nine**; the CJS implementation layer **CJS-5.7 — Procedural Integrity and Adjudication** |
| **CJS-R04** | Routing, intake, transfer, certification, representative treatment | `corpus_forum.md` **CF-5** | **CJS-4.7**, **CJS-5.7**; `core_09-09_forum.md` **Chapter Nine**; `corpus_institutions.md` **CI-8** |
| **CJS-R05** | Appeal, secondary review, exhaustion | `corpus_forum.md` **CF-6** | `corpus_institutions.md` **CI-6**; **CJS-5.7** procedural integrity and adjudication terms |
| **CJS-R06** | Forum integrity operations, anti-capture, anti-self-judging support | `corpus_forum.md` **CF-7** | `corpus_institutions.md` **CI-5**, **CI-7.3**; `core_09-09_forum.md` **Chapter Nine** |
| **CJS-R07** | Forum forensic and analytical support | `corpus_forum.md` **CF-8** | `corpus_institutions.md` **CI-7**, **CI-7.3** |
| **CJS-R08** | Independent investigative service and prosecution interface | `corpus_forum.md` **CF-9** | `corpus_institutions.md` **CI-8** |
| **CJS-R09** | Technical forums and specialist chambers | `corpus_forum.md` **CF-10** | `corpus_institutions.md` **CI-17**; `core_09-09_forum.md` **Chapter Nine** |
| **CJS-R10** | Forum performance, backlog requirements, publication timeliness, accessibility | `corpus_forum.md` **CF-11** | `corpus_institutions.md` **CI-7.3**; Sentient Constitution **Article XV** themes in `core_10-10_rights_part_*.md` **Chapter Ten** |
| **CJS-R11** | Forum continuity | `corpus_forum.md` **CF-12** | `corpus_systems.md` **Protocol A — System Design, Testing, Verification, and Deployment**; `corpus_institutions.md` **CI-14** (where transition or continuity interfaces apply); `core_09-09_forum.md` **Chapter Nine** |
| **CJS-R11A** | Fallback operation | `corpus_forum.md` **CF-13** | `corpus_systems.md` **Protocol A — System Design, Testing, Verification, and Deployment**; **CJS-R03** and **CJS-R06** where lawful panel constitution, backup routing, or anti-capture constraints apply |
| **CJS-R11B** | Emergency adjudication | `corpus_forum.md` **CF-14** | `corpus_systems.md` **Protocol A — System Design, Testing, Verification, and Deployment**; `core_09-09_forum.md` **Chapter Nine**; **CJS-R10** where emergency performance or restoration tracking applies |
| **CJS-R12** | Standard forum records, forms, and evidence artifacts | `corpus_forum.md` **CF-15** | `corpus_institutions.md` **CI-6**; `core_02-04_definition_mechanics.md` **Chapters Two through Four** (traceability and verification discipline) |
| **CJS-R13** | Forum staffing, shared administration, structural review, structural records | `corpus_forum.md` **CF-16** | `corpus_institutions.md` **CI-4**, **CI-5**; **CI-9.3** where delegated forum subunits apply |
| **CJS-R14** | Institutional functional lanes and non-delegable splits | `corpus_institutions.md` **CI-3** | the CJS implementation layer **CJS-5.2 and CJS-5.12 — Distributed and Proportional Authority**; `corpus_systems.md` **CS-5 — Critical system stewardship** where CSS stewardship intersects |
| **CJS-R15** | Contest-integrity monitoring (pathway integrity, not merits) | `corpus_institutions.md` **CI-7.3** | `corpus_systems.md` **CS-4 — System classification and handling**, **CS-5** (including steward contest-integrity paragraphs where applicable); the CJS implementation layer **CJS-5.7 — Procedural Integrity and Adjudication**; the lawful-panel and forum-performance router topics (**CJS-R03** and **CJS-R10**) where forum performance data feeds monitors |
| **CJS-R16** | Cross-institution coordination, deadlock, and escalation | `corpus_institutions.md` **CI-8** | `corpus_forum.md` **CF-5**, **CF-7**; `core_09-09_forum.md` **Chapter Nine** (including backup and cross-forum integrity routing) |
| **CJS-R17** | Cross-implementation trust integrity (joint operation model) | **CJS-4.4 — Cross-implementation trust integrity** | [Chapter Five section **3.11**](../core_05-05_definitions_c_dependent_clusters.md#trust-and-trustworthiness-cluster) (*Trust*, *Trustworthiness*, *Trust Degradation and Misleading Reliance*); `corpus_systems.md` **CS-4 — System classification and handling**, **CS-5 — Critical system stewardship** where classification or dependency scales assurance burden; **CJS-5.14**, **CJS-5.15**, **CJS-5.16**, **CJS-5.19**, **CJS-5.17**, **CJS-5.9**, **CJS-5.11**, **CJS-5.21**, and **CJS-5.18** where the trust claim depends on the corresponding operational fact; `corpus_institutions.md` **CI-7.3**, **CI-8** and `corpus_forum.md` **CF-11** where pathway integrity, publication cadence, or accessibility materially conditions justified trust |
| **CJS-R18** | Class-scaled lane staffing and competency redundancy for materially binding stewardship | `corpus_institutions.md` **CI-3**, **CI-4**, **CI-11**, **CI-12** | **CJS-4.6**; **CJS-5.2**; `corpus_systems.md` **CS-4 — System classification and handling**, **CS-5 — Critical system stewardship**; `core_11-11_governance.md` **Chapter Eleven**, section **5** |
| **CJS-R19** | Implementation and cross-implementation integrity assurance and resilience operations | **CJS-5.8** | the CJS implementation layer **CJS-5.9 — Auditability** through **CJS-5.23 and CJS-5.8 — Evolution, Revalidation, and Non-Entrenchment**; **Chapter Five** (*Auditability*, *Verifiability*, *Verification Accessibility*, *Reversibility*, *Dependency*, *Cascading Failure*, *Adversarial, Scaled, and Exploited Conditions*, *Trustworthiness*); `corpus_systems.md` **CS-3 — Information types and handling**, **CS-4 — System classification and handling**, **CS-5 — Critical system stewardship** where classification, data handling, or stewardship scales burden; `corpus_institutions.md` **CI-7.3**, **CI-8** and `corpus_forum.md` **CF-11** where monitoring, escalation, publication, or review pathways are materially required |

Rows are **indicative**, not exhaustive: if a matter triggers multiple rows, apply **all** triggered rows whose scope is materially true.

### CJS-2.2: Intentional overlap (non-duplication discipline)
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.2](cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-2.1](cjs_02_implementation_integration_map.md#cjs-21-topic-router-stable-ids) topic router; [Chapter Fifteen](../core_15-15_incorporation.md#chapter-fifteen-incorporation-bridge) incorporation discipline and [Chapter Five](../core_05-05_definitions_a_independent.md#chapter-five-foundational-definitions) canonical definitions.
- Downstream: this section's local operational requirements for **CJS-2.2: Intentional overlap (non-duplication discipline)**.
- Read with: **CJS-2.2**; [CJS-2.1](cjs_02_implementation_integration_map.md#cjs-21-topic-router-stable-ids).

</details>

<details>
<summary><strong><span style="color: #2563eb;">Definitions · Evaluation · Compliance</span></strong></summary>

- [Contestability](../core_05-05_definitions_b_semi_independent.md#contestability) · [O](../core_05-05_definitions_b_semi_independent.md#contestability) · [E](../core_05-05_definitions_b_semi_independent.md#contestability-e) · [C](../core_05-05_definitions_b_semi_independent.md#contestability-c)
- [Adjudication and Dispute Resolution](../core_05-05_definitions_b_semi_independent.md#adjudication-and-dispute-resolution-constitutional) · [O](../core_05-05_definitions_b_semi_independent.md#adjudication-and-dispute-resolution-constitutional) · [E](../core_05-05_definitions_b_semi_independent.md#adjudication-and-dispute-resolution-constitutional-e) · [C](../core_05-05_definitions_b_semi_independent.md#adjudication-and-dispute-resolution-constitutional-c)
- [Epistemic Integrity](../core_05-05_definitions_c_dependent_clusters.md#epistemic-integrity) · [O](../core_05-05_definitions_c_dependent_clusters.md#epistemic-integrity) · [E](../core_05-05_definitions_c_dependent_clusters.md#epistemic-integrity-e) · [C](../core_05-05_definitions_c_dependent_clusters.md#epistemic-integrity-c)

</details>

<br>

Some topics are **deliberately** split across implementation files — for example contest-integrity design, delegated subunits, or forensic and technical-forum interfaces. For those rows:

- the **primary owner** states the **full operative** rules for the scope that row assigns to it;
- **CJS** text for the same topic adds **joint satisfaction conditions**, **read-with pointers**, and **interface requirements** only when **CJS** is not the **primary owner** for that row;
- do **not** restate **CJS-5** (*Implementation and cross-implementation operational cluster library*) OP clusters, **CS-4/CS-5** tables, or **CF-** / **CI-** checklists except in brief **quote** or **summary pointer** form when needed for coherence.

### CJS-2.3: Two-tier definition contract (binding abstraction + owner detail)
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.2](cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-2.1](cjs_02_implementation_integration_map.md#cjs-21-topic-router-stable-ids) topic router; [Chapter Fifteen](../core_15-15_incorporation.md#chapter-fifteen-incorporation-bridge) incorporation discipline and [Chapter Five](../core_05-05_definitions_a_independent.md#chapter-five-foundational-definitions) canonical definitions.
- Downstream: this section's local operational requirements for **CJS-2.3: Two-tier definition contract (binding abstraction + owner detail)**.
- Read with: **CJS-2.3**; [CJS-2.1](cjs_02_implementation_integration_map.md#cjs-21-topic-router-stable-ids).

</details>

<details>
<summary><strong><span style="color: #2563eb;">Definitions · Evaluation · Compliance</span></strong></summary>

- [Materiality Determination](../core_05-05_definitions_b_semi_independent.md#materiality-determination) · [O](../core_05-05_definitions_b_semi_independent.md#materiality-determination) · [E](../core_05-05_definitions_b_semi_independent.md#materiality-determination-e) · [C](../core_05-05_definitions_b_semi_independent.md#materiality-determination-c)
- [Procedural Fairness](../core_05-05_definitions_b_semi_independent.md#procedural-fairness-constitutional) · [O](../core_05-05_definitions_b_semi_independent.md#procedural-fairness-constitutional) · [E](../core_05-05_definitions_b_semi_independent.md#procedural-fairness-constitutional-e) · [C](../core_05-05_definitions_b_semi_independent.md#procedural-fairness-constitutional-c)

</details>

<br>

The CJS folder may adopt **binding high-level joint abstractions** only where a term or construct is materially cross-implementation and cannot be safely interpreted through a single owner file alone.

For this contract:

- **Tier 1 (CJS abstraction):** state only shared admission scope, cross-implementation trigger conditions, and minimum joint consequences needed to avoid contradiction or silent gaps.
- **Tier 2 (owner detail):** retain all operational tests, thresholds, procedures, and implementation mechanics in the **primary owner** section(s) named in **CJS-2.1** (*Topic router (stable IDs)*).
- **No parallel canon:** CJS abstractions must not become a second full taxonomy for domains owned by **CJS**, **CS**, **CI**, or **CF**.
- **Specialize, do not redefine:** owner files may specialize a CJS abstraction for their domain scope but must not redefine it incompatibly.

---

**Previous file:** [cjs_01_scope_purpose_boundary_interface.md](cjs_01_scope_purpose_boundary_interface.md)

**Next file:** [cjs_03_joint_structural_obligations.md](cjs_03_joint_structural_obligations.md)
