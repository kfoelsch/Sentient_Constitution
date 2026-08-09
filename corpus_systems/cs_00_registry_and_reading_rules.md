# Systems registry and identifier rules

*In plain terms: this file is the systems **registry annex** — how CS section labels work, the stable family map, and systems-only domain routing for integrators. Start reading at [corpus_systems.md](../corpus_systems.md); continue in order at [cs_01_scope_purpose_identifier_rules.md](cs_01_scope_purpose_identifier_rules.md).*

<details>
<summary><strong><span style="color: #2563eb;">Corpus placement (non-operative): file structure and reading rules</span></strong></summary>

> The following content is **reader guidance only**. It does not add, remove, or narrow binding obligations elsewhere in this file or in other corpus files.
>
> **Edition and alignment**
> - **Corpus edition:** `SC-Corpus-2026.04.33` · **Effective date:** 2026-04-24
> - These labels track the same edition metadata as the numbered `core_*.md` files (see [README.md](../README.md)), [corpus_institutions.md](../corpus_institutions.md), [corpus_forum.md](../corpus_forum.md), and [corpus_joint_structure.md](../corpus_joint_structure.md).
> - Edition and custody: [README.md](../README.md) and [Chapter Five *Corpus*](../core_05_band_integrative.md#corpus).
>
> **Status**
> - This is **not** a core constitutional file. It is binding incorporated implementation text where [Chapter Five](../core_05_band_integrative.md#corpus) and [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) designate it.
> - Prefer the filename **`corpus_systems.md`** in cross-references; the bare phrase *Constitutional Systems* is not used in corpus body text (see [tools/architecture/lexical_guardrails.json](../tools/architecture/lexical_guardrails.json)).
> - The CS folder is written in plain language with low jargon to improve accessibility, audit readability, and practical adoption testing.
> - **Reader landing:** [corpus_systems.md](../corpus_systems.md) is the human start for this layer. This file is the registry and identifier annex, not a second front door.
>
> **Where this lives**
> - **Navigation wrapper / reader landing:** [corpus_systems.md](../corpus_systems.md) indexes the `corpus_systems/` subfiles.
> - **Layer homes:** [Preamble — constitutional owner register](../core_00_preamble.md#constitutional-owner-register); this layer's owns / does-not-own list in [cs_01_scope_purpose_identifier_rules.md](cs_01_scope_purpose_identifier_rules.md) (**CS-1**). Definition placement: **CJS-1.1**, **CJS-1.2**, and **CJS-2.3**.
> - **Shared contract:** **CJS-1.2** (*Shared implementation-corpus preamble contract*).
>
> **Implementation layer map**
>
> The systems layer (**CS**) owns typing, classification, stewardship, and protocol-level engineering rules for systems and data:
>
> - **CJS** — [corpus_joint_structure.md](../corpus_joint_structure.md) (joint-structure interfaces)
> - **CS** — this folder (`corpus_systems/`)
> - **CI** — [corpus_institutions.md](../corpus_institutions.md)
> - **CF** — [corpus_forum.md](../corpus_forum.md)
>
> **CS** is the canonical home for **CS-2–CS-4**, **Protocol A** through **Protocol T**, and related systems labels. Constitutional meanings, Rights Floors, and definition-satisfaction rules remain in the Sentient Constitution and Chapter Five.
>
> System and data obligations here align with [corpus_joint_structure.md — Cross-domain implementation layer](../corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cross-domain-implementation-layer), especially **CJS-4.3** (*Cross-implementation trust integrity (joint operation model)*) and the **CJS-5** (*Implementation and cross-implementation operational cluster library*) operational cluster library.
>
> Shared preamble contract: apply **CJS-1.2** (*Shared implementation-corpus preamble contract*).
>
> **Principle-layer routing:** Read with [Chapter One](../core_01_c_stewardship_capacity_principles.md#chapter-01-principles-and-constraints) — [Constitutional Tetrad](../core_00_preamble.md#constitutional-tetrad), [Two Constitutional Aims](../core_00_preamble.md#two-constitutional-aims), and [material stake](../core_00_preamble.md#material-stake) scaling. **CS-3** (*System classification and handling*) and **CS-3** (*Critical system stewardship*) map to material stake; **Protocol A** subsection **H** and **Protocol D** implement self-healing and partition resilience under the **Continuity aim** (operational continuity language is not a substitute for that aim).
>
> **CJS cluster mapping (routing only)**
> - Technical requirements map primarily to **CJS-5.2–CJS-5.6** (*Oversight leg*), **CJS-5.7–CJS-5.10** (*Participation leg*), **CJS-5.16–CJS-5.21** (*Continuity aim*), and **CJS-5.22–CJS-5.23** (*Integrative cross-leg*).
> - Governance, proportionality of authority, justification, challenge, and collective-choice processes map primarily to **CJS-5.11–CJS-5.15** (*Accountability leg*), together with Chapter Twelve decision-resolution requirements.
>
> **File-specific implementation anchors**
> - **Taxonomy home:** data types, system classes/dependency types, and steward tiers are canonical in **CS-4–CS-4**; other corpus files reference these labels.
> - **Chapter Six structure:** This folder implements Chapter Six themes operationally (challenge/redress via **Article XII-B** (*Right to Challenge, Review, and Redress*); auditability via **Article XV-A** (*Auditability and Observable Evidence*) with **Chapters Two through Four**; justice and emergencies via **Article XXIII** (*Conflict Resolution, Escalation, and Emergency Proportionality*) with **Chapter One** section 6.4; info-sphere and publication via **Articles XIV** and **VIII-C** with Chapter Five clusters). It must not narrow those articles.
> - **Intervention layering:** **CJS-5.23** (*intervention and override integrity terms*) and **CJS-5.14** (*intervention governance and override-authorization terms*) — jointly applicable where relevant.
> - **Voting / crypto / roles:** Chapter Twelve section 4 (*Voting and Binding Collective Choice Protocols*); Chapter Four section 5.1.1 (*Cryptographic protection, credentials, and verification*); Chapter Twelve section 5.1 (*Authorized Roles, Competency Development, and Contribution*).
> - **Capital-markets scope:** specialist corporate-securities law remains outside dedicated implementation file coverage.
> - **Joint implementation read:** where **CS-2/CS-3** intersect institutional governance, forum operations, or **CJS-5** clusters, read **CJS-2** (especially **CJS-2.1**) and **CJS-3**. Systems-only topic ownership and domain reading order live in this file under [Systems domain routing (integrator annex)](#systems-domain-routing-integrator-annex).
> - **Standing pipeline:** Chapter Eight owns Questions 1 and 2: verified standing records and Contribution Axis / Violation Axis measurement. **Forum** allegations and unadjudicated claims are not standing measurement inputs (**Chapter Eleven**). Chapter Nine owns Question 3 consequences; recency and currentness are gate/readiness inputs under [Chapter Nine §6.1](../core_09-09_standing_integration.md#61-recency-and-currentness) and must not alter the Chapter Eight contribution slot or LEQU measurement. Violation locks are decided before contribution gates under [Chapter Nine §2](../core_09-09_standing_integration.md#2-integration-record-and-decision-order). Numeric interoperability defaults: [implementation/CH06_NINE_SLOT_STANDING_SCALE.md](../implementation/CH06_NINE_SLOT_STANDING_SCALE.md).

</details>

<br>

<a id="systems-identifier-and-article-reference-rules"></a>
## Systems identifier and article-reference rules
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.2](../corpus_joint_structure/cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-1.3](../corpus_joint_structure/cjs_01_scope_purpose_boundary_interface.md#cjs-13-section-identifiers-and-article-references) section identifiers; [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline; and [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions.
- Downstream: [Systems registry (stable section families)](#systems-registry-stable-section-families); [Systems domain routing (integrator annex)](#systems-domain-routing-integrator-annex).
- Read with: **CS-1**; **CJS-1.3**.

</details>

<br>

*In plain terms: labels like **CS-3 — System classification and handling** and **Protocol A** are systems-implementation section numbers — not Sentient Constitution article numbers.*

Apply **CJS-1.3** (*Section identifiers and article references*) as the shared implementation-corpus identifier rule. In this folder specifically, **Protocol A**, **Protocol B**, **Protocol S4**, **Protocol S5**, **Protocol T**, **Protocol R**, **Protocol D**, and **CS-1** / **CS-2 — Information types and handling** through **CS-4 — Critical system stewardship** are systems implementation labels. They must not be read as Sentient Constitution **Article** or chapter numbers. The editor abbreviation **CS** may appear in owner tables, stable IDs, and short routing references, but citations should prefer `corpus_systems.md` plus the named protocol or CS section label where practical.

Unless another reference pattern is stated, **Article** labels with Roman numerals in this folder point to Sentient Constitution Chapter Six in the `core_06-06_rights_part_*.md` files.

<a id="systems-registry-stable-section-families"></a>
## Systems registry (stable section families)
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.2](../corpus_joint_structure/cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-2.1](../corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cjs-21-topic-router-stable-ids) topic router; [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline; and [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions.
- Downstream: [Systems domain routing (integrator annex)](#systems-domain-routing-integrator-annex).
- Read with: **CS-1**; **CS-2 — Information types and handling**; **CS-3 — System classification and handling**; **CS-4 — Critical system stewardship**; **Protocol A**.

</details>

<br>

*In plain terms: this is the table of contents for the systems folder — stable families, each with a home file.*

| Family | What it covers | Start here |
|---|---|---|
| **CS-1** | Scope, purpose, and boundary interface | [cs_01_scope_purpose_identifier_rules.md](cs_01_scope_purpose_identifier_rules.md) |
| **CS-2, Part A** | Handling rules (§1–§7) | [cs_02_a_information_types_and_handling.md](cs_02_a_information_types_and_handling.md) |
| **CS-2, Part B** | Data classifications (§8; Type E–S including Type O) | [cs_02_b_data_classifications.md](cs_02_b_data_classifications.md) |
| **CS-3, Part A** | Classification machinery (§1–§7; Dep-A–P dependency types) | [cs_03_a_system_classification_machinery.md](cs_03_a_system_classification_machinery.md) |
| **CS-3, Part B** | System impact classifications (§8 overview and aspect-comparative matrices; §§9–13 Class A–P cards) | [cs_03_b_system_impact_classifications.md](cs_03_b_system_impact_classifications.md) |
| **CS-4 — Critical system stewardship** | Critical system stewardship | [cs_04_critical_system_stewardship.md](cs_04_critical_system_stewardship.md) |
| **Protocol A** | System design, testing, verification, and deployment | [cs_protocol_a_system_design_testing_verification_deployment.md](cs_protocol_a_system_design_testing_verification_deployment.md) |
| **Protocol B** | System comprehensibility and complexity stewardship | [cs_protocol_b_system_comprehensibility_complexity_stewardship.md](cs_protocol_b_system_comprehensibility_complexity_stewardship.md) |
| **Protocol C** | Justice safeguards, restitution, and rehabilitation implementation | [cs_protocol_c_justice_safeguards_restitution_rehabilitation.md](cs_protocol_c_justice_safeguards_restitution_rehabilitation.md) |
| **Protocol S4** | Adaptive sustainability and ecosystem resilience | [cs_protocol_s4_adaptive_sustainability_ecosystem_resilience.md](cs_protocol_s4_adaptive_sustainability_ecosystem_resilience.md) |
| **Protocol S5** | Resource allocation and funding stewardship | [cs_protocol_s5_resource_allocation_funding_stewardship.md](cs_protocol_s5_resource_allocation_funding_stewardship.md) |
| **Protocol T** | Transition constitution and migration governance | [cs_protocol_t_transition_constitution_migration_governance.md](cs_protocol_t_transition_constitution_migration_governance.md) |
| **Protocol R** | Subversion response, replacement, and reconstitution | [cs_protocol_r_subversion_response_replacement_reconstitution.md](cs_protocol_r_subversion_response_replacement_reconstitution.md) |
| **Protocol D** | Decentralized constitutional continuity and partition resilience | [cs_protocol_d_decentralized_constitutional_continuity_partition_resilience.md](cs_protocol_d_decentralized_constitutional_continuity_partition_resilience.md) |

<a id="systems-domain-routing-integrator-annex"></a>
## Systems domain routing (integrator annex)
<a id="systems-domain-routing-integrator-annex"></a>
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.2](../corpus_joint_structure/cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-2.1](../corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cjs-21-topic-router-stable-ids) topic router; [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline; and [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions.
- Downstream: [Domain topic owner map (CS-D)](#domain-topic-owner-map-cs-d); [Systems overlap discipline](#systems-overlap-discipline); [Systems read-with pointers](#systems-read-with-pointers).
- Read with: [CJS-2.1](../corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cjs-21-topic-router-stable-ids); **CJS-2.2**; **CJS-2.3**; [CJS-1.1](../corpus_joint_structure/cjs_01_scope_purpose_boundary_interface.md#cjs-11-joint-structural-boundary-and-owner-discipline); **CS-1**; **CS-2 — Information types and handling**; **CS-3 — System classification and handling**; **CS-4 — Critical system stewardship**; **Protocol A**.

</details>

<br>

*In plain terms: this annex tells integrators which systems file owns which systems-only topic. Cross-layer mandatory read-with stays in **CJS-2.1** — this file does not maintain a competing list.*

**Domain-internal reading order (systems-only topics):** for classification, dependency typing, and stewardship scale, read **CS-2 — Information types and handling** → **CS-3 — System classification and handling** → **CS-4 — Critical system stewardship** before specialized protocols unless a protocol row below is the stated primary owner for the topic.

When a systems topic materially intersects **CI**, **CF**, or **CJS**, use [CJS-2.1](../corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cjs-21-topic-router-stable-ids) (*Topic router (stable IDs)*) for the authoritative mandatory read-with list.

<a id="domain-topic-owner-map-cs-d"></a>
### Domain topic owner map (CS-D)
<a id="domain-topic-owner-map-cs-d"></a>
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [Systems domain routing (integrator annex)](#systems-domain-routing-integrator-annex); [CJS-2.1](../corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cjs-21-topic-router-stable-ids) topic router.
- Read with: **CS-2 — Information types and handling**; **CS-3 — System classification and handling**; **CS-4 — Critical system stewardship**; **Protocol A**.

</details>

<br>

| CS-D row | Topic (short) | CS primary owner | Companion read-with (systems-local) |
|----------|---------------|------------------|-------------------------------------|
| **CS-D01** | Information types and handling taxonomy | **CS-2 — Information types and handling** | **CS-3 — System classification and handling**; **CS-4 — Critical system stewardship** where classification scales handling |
| **CS-D02** | System classification and dependency typing | **CS-3 — System classification and handling** | **CS-2 — Information types and handling**; **CS-4 — Critical system stewardship** where class scales stewardship |
| **CS-D03** | Critical system stewardship tiers | **CS-4 — Critical system stewardship** | **CS-3 — System classification and handling**; **Protocol A** where design and verification apply |
| **CS-D04** | Design, testing, verification, deployment lifecycle | **Protocol A** | **CS-3 — System classification and handling**, **CS-4 — Critical system stewardship** where class scales burden |

**CS-D** row IDs are **corpus-local** domain-internal labels; they are **not** Sentient Constitution article numbers and do not replace **CJS-R** rows.

<a id="systems-overlap-discipline"></a>
### Systems overlap discipline
<a id="systems-overlap-discipline"></a>
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [Systems domain routing (integrator annex)](#systems-domain-routing-integrator-annex); [CJS-2.2](../corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cjs-22-intentional-overlap-non-duplication-discipline) intentional overlap.
- Read with: [CJS-2.2](../corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cjs-22-intentional-overlap-non-duplication-discipline); **CS-3 — System classification and handling**; **Protocol A**; **Protocol B**.

</details>

<br>

Some systems topics are **deliberately** split — for example taxonomy (**CS-2 — Information types and handling**), classification (**CS-3 — System classification and handling**), stewardship (**CS-4 — Critical system stewardship**), and lifecycle engineering (**Protocol A**). For those splits:

- the **primary owner** named in the [Domain topic owner map (CS-D)](#domain-topic-owner-map-cs-d) states the **full operative** rules for its assigned scope;
- companion **CS** protocols specialize without redefining **CS-2–CS-4** taxonomy labels;
- do **not** restate **CJS-5** operational clusters or **CI**/**CF** checklists except in brief pointer form when needed for coherence.

For cross-layer overlap discipline, apply [CJS-2.2](../corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cjs-22-intentional-overlap-non-duplication-discipline) (*Intentional overlap (non-duplication discipline)*).

<a id="systems-read-with-pointers"></a>
### Systems read-with pointers
<a id="systems-read-with-pointers"></a>
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [Systems domain routing (integrator annex)](#systems-domain-routing-integrator-annex); [CJS-1.1](../corpus_joint_structure/cjs_01_scope_purpose_boundary_interface.md#cjs-11-joint-structural-boundary-and-owner-discipline) joint structural boundary.
- Read with: [CJS-1.1](../corpus_joint_structure/cjs_01_scope_purpose_boundary_interface.md#cjs-11-joint-structural-boundary-and-owner-discipline); [CJS-2.3](../corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cjs-23-two-tier-definition-contract-binding-abstraction--owner-detail); **CS-1**.

</details>

<br>

When systems implementation text intersects other implementation layers, apply the default reading stack in [CJS-1.1](../corpus_joint_structure/cjs_01_scope_purpose_boundary_interface.md#cjs-11-joint-structural-boundary-and-owner-discipline) (*Joint structural boundary and owner discipline*). Within that stack, read only what [CJS-2.1](../corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cjs-21-topic-router-stable-ids) routes for the topic.

Systems-local abstractions may specialize **CJS** joint operational definitions cited in owner text but must not redefine constitutional terms or create parallel constitutional definitions. For the two-tier definition contract, apply [CJS-2.3](../corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cjs-23-two-tier-definition-contract-binding-abstraction--owner-detail) (*Two-tier definition contract (binding abstraction + owner detail)*).

---

**Previous file:** [corpus_systems.md](../corpus_systems.md)

**Next file:** [cs_01_scope_purpose_identifier_rules.md](cs_01_scope_purpose_identifier_rules.md)
