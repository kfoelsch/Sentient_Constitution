## CJS-2: Implementation integration map
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.2](cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-2.1](cjs_02_implementation_integration_map.md#cjs-21-topic-router-stable-ids) topic router; [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline and [Chapter Five](../core_05-05_definitions_a_independent.md#chapter-five-foundational-definitions) canonical definitions.
- Downstream: [CJS-2.1: Cross-implementation read-with contract](#cjs-21-topic-router-stable-ids); [CJS-2.2: Intentional overlap (non-duplication discipline)](#cjs-22-intentional-overlap-non-duplication-discipline); [CJS-2.3: Two-tier definition contract (binding abstraction + owner detail)](#cjs-23-two-tier-definition-contract-binding-abstraction--owner-detail).
- Read with: **CJS-2**; [CJS-2.1](cjs_02_implementation_integration_map.md#cjs-21-topic-router-stable-ids); **CJS-2.2**; **CJS-2.3**; **CJS-3**; **CJS-3.6**; **CJS-1.2**.
- Integrator index (non-operative): authoritative **CJS-R** router table in **CJS-2.1** (*Cross-implementation read-with contract*); plain-language grouped index: [topic_router_reader_index.md](../doc_architecture/generated/topic_router_reader_index.md) (generated via `make architecture-index`). Reading guide: [CJS-0.1](cjs_00_registry_and_reading_rules.md#cjs-01-cross-file-routing) (*Cross-file routing*).

</details>

<br>

*In plain terms: **CJS-2** names where to read when a topic crosses layers — topic routing, overlap discipline, and definition tiers. Default reading stack: **CJS-1.1**; for which section owns a cross-layer topic, use **[CJS-0.1](cjs_00_registry_and_reading_rules.md#cjs-01-cross-file-routing)** or **CJS-2.1**; **CI-2**, **CF-2**, and **CS-2** mirror this pattern at the domain layer without maintaining a competing router table.*

**Quick orientation**

- **CJS-2.1** — default reading stack and authoritative topic router when more than one implementation layer applies (start here).
- **CJS-2.2** — how deliberately split cross-layer topics avoid duplication.
- **CJS-2.3** — two-tier definition contract for binding joint abstractions and owner detail.

### CJS-2.1: Cross-implementation read-with contract

<a id="cjs-21-topic-router-stable-ids"></a>
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.2](cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-2.1](cjs_02_implementation_integration_map.md#cjs-21-topic-router-stable-ids) topic router; [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline and [Chapter Five](../core_05-05_definitions_a_independent.md#chapter-five-foundational-definitions) canonical definitions.
- Downstream: this section's local operational requirements for **CJS-2.1: Cross-implementation read-with contract**.
- Read with: [CJS-2.1](cjs_02_implementation_integration_map.md#cjs-21-topic-router-stable-ids); **CJS-4.1**; **CJS-4.5**; **CJS-4.3**; **CJS-4.4**; [CJS-2.3](#cjs-23-two-tier-definition-contract-binding-abstraction--owner-detail); [CJS-1.1](cjs_01_scope_purpose_boundary_interface.md#cjs-11-joint-structural-boundary-and-owner-discipline).

</details>

<br>

*In plain terms: apply the default reading stack in **CJS-1.1**; route topics and mandatory read-with through this section.*

When implementation text intersects other implementation layers, apply the default reading stack in [CJS-1.1](cjs_01_scope_purpose_boundary_interface.md#cjs-11-joint-structural-boundary-and-owner-discipline) (*Joint structural boundary and owner discipline*). Within that stack, read only what **CJS-2.1** routes for the topic.

Router rows are **indicative**, not exhaustive: if a matter triggers multiple rows, apply **all** triggered rows whose scope is materially true.

For how **primary owner** and **mandatory read-with** work, read [CJS-0.1](cjs_00_registry_and_reading_rules.md#cjs-01-cross-file-routing) (*Cross-file routing*). For which section owns which topic, use that section, [topic_router_reader_index.md](../doc_architecture/generated/topic_router_reader_index.md), or the integrator router table in this section.

Joint abstractions and constitutional non-redefinition discipline: [CJS-1.1](cjs_01_scope_purpose_boundary_interface.md#cjs-11-joint-structural-boundary-and-owner-discipline) (*Joint structural boundary and owner discipline*) and the two-tier contract in [CJS-2.3](#cjs-23-two-tier-definition-contract-binding-abstraction--owner-detail) (*Two-tier definition contract (binding abstraction + owner detail)*).

<details>
<summary><strong><span style="color: #2563eb;">Integrator reference: full router table (stable row IDs)</span></strong></summary>

> Maintainer and audit surface. Stable row IDs (**CJS-R01** (*Delegated binding bodies and hybrid composition (non-forum institutions)*)–**CJS-R19** (*integrity assurance and resilience operations*)) are **corpus-local** labels; they are **not** Sentient Constitution article numbers.

**Bidirectional routing:** The **primary owner** must cite its **CJS-R** row here and the same mandatory read-with list — or a one-line pointer to that row for the full list. Each **mandatory read-with** section must cite the row and **primary owner** where the topic materially applies. Do not maintain a second competing read-with list in the owner file.

| Row ID | Topic | Primary owner | Mandatory read-with |
|--------|--------|---------------|---------------------|
| **CJS-R01** | Delegated binding bodies and hybrid composition (non-forum institutions) | `corpus_institutions.md` **CI-9.3** | **CJS-4.1**, **CJS-4.5**, **CJS-5.13** (*Accountability: procedural integrity and adjudication terms*); `corpus_systems.md` **CS-4 — System classification and handling**, **CS-5 — Critical system stewardship**; `corpus_institutions.md` **CI-3**; the CJS implementation layer **CJS-5.11 and CJS-5.7 — Distributed and Proportional Authority**, **CJS-5.12 — Burden of Justification and Constraint** (as cited in owner text) |
| **CJS-R02** | Forum chambers, divisions, and designated panels (Chapter Eleven families) | `corpus_forum.md` **CF-3.5**–**CF-3.8** | **CJS-4.1**, **CJS-4.5**, **CJS-5.13** (*Accountability: procedural integrity and adjudication terms*); `corpus_institutions.md` **CI-9.3**; `corpus_systems.md` **CS-4 — System classification and handling**, **CS-5 — Critical system stewardship**; `core_11-11_forum.md` **Chapter Eleven** |
| **CJS-R03** | Lawful panel formation, disclosure, recusal, substitution, inability-to-form | `corpus_forum.md` **CF-4** | **CJS-4.5**, **CJS-5.13** (*Accountability: procedural integrity and adjudication terms*); `corpus_institutions.md` **CI-4**, **CI-5**; `core_11-11_forum.md` **Chapter Eleven**; the CJS implementation layer **CJS-5.13 — Procedural Integrity and Adjudication** |
| **CJS-R04** | Routing, intake, transfer, certification, representative treatment | `corpus_forum.md` **CF-5** | **CJS-4.5**, **CJS-5.13** (*Accountability: procedural integrity and adjudication terms*); `core_11-11_forum.md` **Chapter Eleven**; `corpus_institutions.md` **CI-8** |
| **CJS-R05** | Appeal, secondary review, exhaustion | `corpus_forum.md` **CF-6** | `corpus_institutions.md` **CI-6**; **CJS-5.13** (*Accountability: procedural integrity and adjudication terms*) procedural integrity and adjudication terms |
| **CJS-R06** | Forum integrity operations, anti-capture, anti-self-judging support | `corpus_forum.md` **CF-7** | `corpus_institutions.md` **CI-5**, **CI-7.3**; `core_11-11_forum.md` **Chapter Eleven** |
| **CJS-R07** | Forum forensic and analytical support | `corpus_forum.md` **CF-8** | `corpus_institutions.md` **CI-7**, **CI-7.3** |
| **CJS-R08** | Independent investigative service and prosecution interface | `corpus_forum.md` **CF-9** | `corpus_institutions.md` **CI-8** |
| **CJS-R09** | Technical forums and specialist chambers | `corpus_forum.md` **CF-10** | `corpus_institutions.md` **CI-25**; `core_11-11_forum.md` **Chapter Eleven** |
| **CJS-R10** | Forum performance, backlog requirements, publication timeliness, accessibility | `corpus_forum.md` **CF-11** | `corpus_institutions.md` **CI-7.3**; Sentient Constitution **Article XV** (*Audit, Transparency, and Independent Verification*) themes in `core_06-06_rights_part_*.md` **Chapter Six** |
| **CJS-R11** | Forum continuity | `corpus_forum.md` **CF-12** | `corpus_systems.md` **Protocol A — System Design, Testing, Verification, and Deployment**; `corpus_institutions.md` **CI-14** (where transition or continuity interfaces apply); `core_11-11_forum.md` **Chapter Eleven** |
| **CJS-R11A** | Fallback operation | `corpus_forum.md` **CF-13** | `corpus_systems.md` **Protocol A — System Design, Testing, Verification, and Deployment**; **CJS-R03** and **CJS-R06** where lawful panel constitution, backup routing, or anti-capture constraints apply |
| **CJS-R11B** | Emergency adjudication | `corpus_forum.md` **CF-14** | `corpus_systems.md` **Protocol A — System Design, Testing, Verification, and Deployment**; `core_11-11_forum.md` **Chapter Eleven**; **CJS-R10** where emergency performance or restoration tracking applies |
| **CJS-R12** | Standard forum records, forms, and evidence artifacts | `corpus_forum.md` **CF-15** | `corpus_institutions.md` **CI-6**; `core_02-03_definition_mechanics.md` **Chapters Two through Four** (traceability and verification discipline) |
| **CJS-R13** | Forum staffing, shared administration, structural review, structural records | `corpus_forum.md` **CF-16** | `corpus_institutions.md` **CI-4**, **CI-5**; **CI-9.3** where delegated forum subunits apply |
| **CJS-R14** | Institutional functional lanes and non-delegable splits | `corpus_institutions.md` **CI-3** | the CJS implementation layer **CJS-5.11 and CJS-5.7 — Distributed and Proportional Authority**; `corpus_systems.md` **CS-5 — Critical system stewardship** where CSS stewardship intersects |
| **CJS-R15** | Contest-integrity monitoring (pathway integrity, not merits) | `corpus_institutions.md` **CI-7.3** | `corpus_systems.md` **CS-4 — System classification and handling**, **CS-5** (including steward contest-integrity paragraphs where applicable); the CJS implementation layer **CJS-5.13 — Procedural Integrity and Adjudication**; the lawful-panel and forum-performance router topics (**CJS-R03** and **CJS-R10**) where forum performance data feeds monitors |
| **CJS-R16** | Cross-institution coordination, deadlock, and escalation | `corpus_institutions.md` **CI-12** | `corpus_forum.md` **CF-5**, **CF-7**; `core_11-11_forum.md` **Chapter Eleven** (including backup and cross-forum integrity routing) |
| **CJS-R17** | Cross-implementation trust integrity (joint operation model) | **CJS-4.3 — Cross-implementation trust integrity** | [Chapter Five section **3.11**](../core_05o_oversight_definitions.md#trust-and-trustworthiness-cluster) (*Trust*, *Trustworthiness*, *Trust Degradation and Misleading Reliance*); `corpus_systems.md` **CS-4 — System classification and handling**, **CS-5 — Critical system stewardship** where classification or dependency scales assurance burden; **CJS-5.9** (*Participation: salience integrity and attention-allocation terms*), **CJS-5.10** (*Participation: disclosure sufficiency and observability terms*), **CJS-5.16** (*Continuity: dependency integrity and disclosure terms*), **CJS-5.19** (*Continuity: graceful degradation and failure-mode integrity terms*), **CJS-5.17** (*Continuity: interoperability, portability, and exit-integrity terms*), **CJS-5.3** (*Oversight: auditability and reconstructability terms*), **CJS-5.5** (*Oversight: independent verification and claim-integrity terms*), **CJS-5.20** (*Continuity: reversibility and containment terms*), and **CJS-5.18** (*Continuity: data-retention and lifecycle-integrity terms*) where the trust claim depends on the corresponding operational fact; `corpus_institutions.md` **CI-7.3**, **CI-8** and `corpus_forum.md` **CF-11** where pathway integrity, publication cadence, or accessibility materially conditions justified trust |
| **CJS-R18** | Class-scaled lane staffing and competency redundancy for materially binding stewardship | `corpus_institutions.md` **CI-3**, **CI-4**, **CI-11**, **CI-12** | **CJS-4.4**; **CJS-5.11** (*Accountability: distributed and proportional authority terms*); `corpus_systems.md` **CS-4 — System classification and handling**, **CS-5 — Critical system stewardship**; `core_12-12_governance.md` **Chapter Twelve**, section **5** |
| **CJS-R19** | integrity assurance and resilience operations | **CJS-5.6** (*Oversight: integrity assurance and resilience operations*) | the CJS implementation layer **CJS-5.3 — Auditability** through **CJS-5.15 and CJS-5.6 — Evolution, Revalidation, and Non-Entrenchment**; **Chapter Five** (*Auditability*, *Verifiability*, *Verification Accessibility*, *Reversibility*, *Dependency*, *Cascading Failure*, *Adversarial, Scaled, and Exploited Conditions*, *Trustworthiness*); `corpus_systems.md` **CS-3 — Information types and handling**, **CS-4 — System classification and handling**, **CS-5 — Critical system stewardship** where classification, data handling, or stewardship scales burden; `corpus_institutions.md` **CI-7.3**, **CI-8** and `corpus_forum.md` **CF-11** where monitoring, escalation, publication, or review pathways are materially required |

</details>

### CJS-2.2: Intentional overlap (non-duplication discipline)
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.2](cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-2.1](cjs_02_implementation_integration_map.md#cjs-21-topic-router-stable-ids) topic router; [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline and [Chapter Five](../core_05-05_definitions_a_independent.md#chapter-five-foundational-definitions) canonical definitions.
- Downstream: this section's local operational requirements for **CJS-2.2: Intentional overlap (non-duplication discipline)**.
- Read with: **CJS-2.2**; [CJS-2.1](cjs_02_implementation_integration_map.md#cjs-21-topic-router-stable-ids).

</details>

<br>

*In plain terms: when one cross-layer topic is split across several implementation files on purpose, each file keeps only its slice — and the authoritative owner is named in **CJS-2.1**, not in a local table elsewhere.*

Some topics are **deliberately** split across implementation files — for example contest-integrity design, delegated subunits, or forensic and technical-forum interfaces. For those rows:

- the **primary owner** states the **full operative** rules for the scope that row assigns to it;
- **CJS** text for the same topic adds **joint satisfaction conditions**, **read-with pointers**, and **interface requirements** only when **CJS** is not the **primary owner** for that row;
- do **not** restate **CJS-5** (*Implementation and cross-implementation operational cluster library*) OP clusters, **CS-4/CS-5** tables, or **CF-** / **CI-** checklists except in brief **quote** or **summary pointer** form when needed for coherence.

Domain-layer overlap discipline: apply **CI-2.2**, **CF-2.2**, and **CS-2.2** at the institutional, forum, and systems layers respectively. For cross-file reading guidance, use [CJS-0.1](cjs_00_registry_and_reading_rules.md#cjs-01-cross-file-routing) (*Cross-file routing*).

### CJS-2.3: Two-tier definition contract (binding abstraction + owner detail)
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.2](cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-2.1](cjs_02_implementation_integration_map.md#cjs-21-topic-router-stable-ids) topic router; [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline and [Chapter Five](../core_05-05_definitions_a_independent.md#chapter-five-foundational-definitions) canonical definitions.
- Downstream: this section's local operational requirements for **CJS-2.3: Two-tier definition contract (binding abstraction + owner detail)**.
- Read with: **CJS-2.3**; [CJS-2.1](cjs_02_implementation_integration_map.md#cjs-21-topic-router-stable-ids); **CJS-2.2**; **CJS-4.2**; **CJS-3.6**.

</details>

<br>

*In plain terms: CJS may adopt shared joint abstractions only where no single owner file can safely hold the term alone; tests, thresholds, and procedures stay in the primary owner named in **CJS-2.1**.*

<details>
<summary><strong><span style="color: #2563eb;">Reader guidance (non-operative): two-tier definition contract</span></strong></summary>

> The following content is **reader guidance only**. It does not add, remove, or narrow binding obligations elsewhere in this section or in other corpus files.

Some ideas cut across **CJS**, **CS**, **CI**, and **CF**. **CJS-2.3** is the discipline for writing those shared ideas in two tiers — a binding skeleton in **CJS** and operative detail in the primary owner named in **CJS-2.1**. Constitutional and joint operational definition boundaries are in **CJS-1.1** (*Joint structural boundary and owner discipline*).

**Illustrative split** — lawful panel formation when a forum cannot seat a full bench: **CJS** states shared scope, cross-layer triggers, and minimum joint consequences; the forum owner (**CF-4** and related rows in **CJS-2.1**) states disclosure, recusal, substitution, and inability-to-form mechanics.

</details>

<br>

The CJS folder may adopt **binding high-level joint abstractions** only where a term or construct is materially cross-implementation and cannot be safely interpreted through a single owner file alone.

For this contract:

- **Tier 1 (CJS abstraction):** state only shared admission scope, cross-implementation trigger conditions, and minimum joint consequences needed to avoid contradiction or silent gaps.
- **Tier 2 (owner detail):** retain all operational tests, thresholds, procedures, and implementation mechanics in the **primary owner** section(s) named in **CJS-2.1** (*Cross-implementation read-with contract*).
- **No parallel canon:** CJS abstractions must not become a second full taxonomy for domains owned by **CJS**, **CS**, **CI**, or **CF**.
- **Specialize, do not redefine:** owner files may specialize a CJS abstraction for their domain scope but must not redefine it incompatibly.

When CJS text seems to conflict with a **primary owner** section, apply **CJS-2.2** (*Intentional overlap (non-duplication discipline)*) and **CJS-4.2** (*Implementation boundary (primary owner to CJS seam)*): if the CJS text only helps readers connect files, trigger a joint rule, or use shorthand inside one subsection, it does not replace the owner's meaning.

When that boundary does not resolve the conflict, use this order:

1. The Sentient Constitution and core definitions, including **Chapter Sixteen**.
2. The canonical owner meaning in **CJS**, **CS**, **CI**, or **CF**, as routed by **CJS-2.1** (*Topic router (stable IDs)*) and `doc_architecture.md`.
3. The **Tier 1** CJS abstraction stated in this section.
4. Local shorthand, examples, summaries, or other drafting convenience text, as described in **CJS-1.2** (*Shared implementation-corpus preamble contract*).

Do not use a broad reading of CJS to change, shrink, expand, or move a rule that belongs to a canonical owner. If the conflict is still unclear after applying this order, do not treat the broader CJS reading as controlling. Send the question to the canonical owner named in **CJS-2.1**, including the forum owner in **CF** where forum routing, forum authority, or Chapter Eleven procedure is affected, and update the CJS pointer once the owner clarifies it. For stricter-wins between two adopted implementation standards on the same risk, read **CJS-3.6** (*Implementation-label traceability and stricter-wins discipline*).

Domain-layer read-with contracts: apply **CI-2.1**, **CF-2.3**, and **CS-2.3** where institutional, forum, or systems text intersects this contract.

---

**Previous file:** [cjs_01_scope_purpose_boundary_interface.md](cjs_01_scope_purpose_boundary_interface.md)

**Next file:** [cjs_03_joint_structural_obligations.md](cjs_03_joint_structural_obligations.md)
