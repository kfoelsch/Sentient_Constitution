## CS-2: Implementation integration map
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.2](../corpus_joint_structure/cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-2.1](../corpus_joint_structure/cjs_02_implementation_integration_map.md#cjs-21-topic-router-stable-ids) topic router; [Chapter Fifteen](../core_15-15_incorporation.md#chapter-fifteen-incorporation-bridge) incorporation discipline; and [Chapter Five](../core_05-05_definitions_a_independent.md#chapter-five-foundational-definitions) canonical definitions.
- Downstream: [CS-2.1: Systems topic router (domain and CJS-R index)](#cs-21-systems-topic-router-domain-and-cjs-r-index); [CS-2.2: Systems overlap discipline](#cs-22-systems-overlap-discipline); [CS-2.3: Systems read-with contract](#cs-23-systems-read-with-contract).
- Read with: **CS-2**; **CS-2.1**; **CS-2.2**; **CS-2.3**; [CJS-2.1](../corpus_joint_structure/cjs_02_implementation_integration_map.md#cjs-21-topic-router-stable-ids); **CJS-2.2**; **CJS-2.3**; **CS-1**.

</details>

<br>

*In plain terms: **CS-2** tells you which systems file owns which systems topic and where to find the authoritative cross-implementation read-with list. Start at **CS-2.1** for the systems-layer index. **CJS-2.1** remains authoritative for mandatory read-with across implementation layers — this file does not maintain a competing list.*

### CS-2.1: Systems topic router (domain and CJS-R index)
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.2](../corpus_joint_structure/cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-2.1](../corpus_joint_structure/cjs_02_implementation_integration_map.md#cjs-21-topic-router-stable-ids) topic router; [Chapter Fifteen](../core_15-15_incorporation.md#chapter-fifteen-incorporation-bridge) incorporation discipline; and [Chapter Five](../core_05-05_definitions_a_independent.md#chapter-five-foundational-definitions) canonical definitions.
- Downstream: this section's local operational requirements for **CS-2.1: Systems topic router (domain and CJS-R index)**.
- Read with: **CS-2.1**; [CJS-2.1](../corpus_joint_structure/cjs_02_implementation_integration_map.md#cjs-21-topic-router-stable-ids); **CS-3 — Information types and handling**; **CS-4 — System classification and handling**; **CS-5 — Critical system stewardship**; **Protocol A**.

</details>

<br>

**Domain-internal reading order (systems-only topics):** for classification, dependency typing, and stewardship scale, read **CS-3 — Information types and handling** → **CS-4 — System classification and handling** → **CS-5 — Critical system stewardship** before specialized protocols unless a protocol row below is the stated primary owner for the topic.

When a systems topic materially intersects **CI**, **CF**, or **CJS**, use the **CJS-R** index rows below and read the authoritative mandatory read-with list in [CJS-2.1](../corpus_joint_structure/cjs_02_implementation_integration_map.md#cjs-21-topic-router-stable-ids).

| CJS-R row / domain row | Topic (short) | CS primary owner | Authoritative read-with |
|------------------------|---------------|------------------|-------------------------|
| **CS-D01** | Information types and handling taxonomy | **CS-3 — Information types and handling** | **CS-4 — System classification and handling**; **CS-5 — Critical system stewardship** where classification scales handling |
| **CS-D02** | System classification and dependency typing | **CS-4 — System classification and handling** | **CS-3 — Information types and handling**; **CS-5 — Critical system stewardship** where class scales stewardship |
| **CS-D03** | Critical system stewardship tiers | **CS-5 — Critical system stewardship** | **CS-4 — System classification and handling**; **Protocol A** where design and verification apply |
| **CS-D04** | Design, testing, verification, deployment lifecycle | **Protocol A** | **CS-4 — System classification and handling**, **CS-5 — Critical system stewardship** where class scales burden |
| **CJS-R01** (read-with) | Delegated binding bodies — classification interface | **CS-4 — System classification and handling**, **CS-5 — Critical system stewardship** | [CJS-R01](../corpus_joint_structure/cjs_02_implementation_integration_map.md#cjs-r01) in **CJS-2.1** |
| **CJS-R02** (read-with) | Forum chambers — classification interface | **CS-4 — System classification and handling**, **CS-5 — Critical system stewardship** | [CJS-R02](../corpus_joint_structure/cjs_02_implementation_integration_map.md#cjs-r02) in **CJS-2.1** |
| **CJS-R11** (read-with) | Forum continuity — technical continuity | **Protocol A** | [CJS-R11](../corpus_joint_structure/cjs_02_implementation_integration_map.md#cjs-r11) in **CJS-2.1** |
| **CJS-R15** (read-with) | Contest-integrity monitoring — classification burden | **CS-4 — System classification and handling**, **CS-5 — Critical system stewardship** | [CJS-R15](../corpus_joint_structure/cjs_02_implementation_integration_map.md#cjs-r15) in **CJS-2.1** |
| **CJS-R17** (read-with) | Cross-implementation trust integrity | **CS-4 — System classification and handling**, **CS-5 — Critical system stewardship** | [CJS-R17](../corpus_joint_structure/cjs_02_implementation_integration_map.md#cjs-r17) in **CJS-2.1** |
| **CJS-R19** (read-with) | Integrity assurance and resilience operations | **CS-3 — Information types and handling**, **CS-4 — System classification and handling**, **CS-5 — Critical system stewardship** | [CJS-R19](../corpus_joint_structure/cjs_02_implementation_integration_map.md#cjs-r19) in **CJS-2.1** |

**CS-D** row IDs are **corpus-local** domain-internal labels; they are **not** Sentient Constitution article numbers and do not replace **CJS-R** rows.

### CS-2.2: Systems overlap discipline
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.2](../corpus_joint_structure/cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-2.1](../corpus_joint_structure/cjs_02_implementation_integration_map.md#cjs-21-topic-router-stable-ids) topic router; [Chapter Fifteen](../core_15-15_incorporation.md#chapter-fifteen-incorporation-bridge) incorporation discipline; and [Chapter Five](../core_05-05_definitions_a_independent.md#chapter-five-foundational-definitions) canonical definitions.
- Downstream: this section's local operational requirements for **CS-2.2: Systems overlap discipline**.
- Read with: **CS-2.2**; [CJS-2.2](../corpus_joint_structure/cjs_02_implementation_integration_map.md#cjs-22-intentional-overlap-non-duplication-discipline); **CS-4 — System classification and handling**; **Protocol A**; **Protocol B**.

</details>

<br>

Some systems topics are **deliberately** split — for example taxonomy (**CS-3 — Information types and handling**), classification (**CS-4 — System classification and handling**), stewardship (**CS-5 — Critical system stewardship**), and lifecycle engineering (**Protocol A**). For those splits:

- the **primary owner** named in **CS-2.1** states the **full operative** rules for its assigned scope;
- companion **CS** protocols specialize without redefining **CS-3–CS-5** taxonomy labels;
- do **not** restate **CJS-5** operational clusters or **CI**/**CF** checklists except in brief pointer form when needed for coherence.

For cross-layer overlap discipline, apply [CJS-2.2](../corpus_joint_structure/cjs_02_implementation_integration_map.md#cjs-22-intentional-overlap-non-duplication-discipline) (*Intentional overlap (non-duplication discipline)*).

### CS-2.3: Systems read-with contract
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.2](../corpus_joint_structure/cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-2.1](../corpus_joint_structure/cjs_02_implementation_integration_map.md#cjs-21-topic-router-stable-ids) topic router; [Chapter Fifteen](../core_15-15_incorporation.md#chapter-fifteen-incorporation-bridge) incorporation discipline; and [Chapter Five](../core_05-05_definitions_a_independent.md#chapter-five-foundational-definitions) canonical definitions.
- Downstream: this section's local operational requirements for **CS-2.3: Systems read-with contract**.
- Read with: **CS-2.3**; [CJS-2.3](../corpus_joint_structure/cjs_02_implementation_integration_map.md#cjs-23-two-tier-definition-contract-binding-abstraction--owner-detail); **CS-1**; [CJS-1.1](../corpus_joint_structure/cjs_01_scope_purpose_boundary_interface.md#cjs-11-joint-structural-boundary-and-owner-discipline).

</details>

<br>

When systems implementation text intersects other implementation layers, apply the default reading stack in **CJS-1.1** (*Joint structural boundary and owner discipline*): **CJS** joint rules first (**CJS-2.1** and **CJS-3**), then **CS** for system classification and stewardship scale, **CI** for institutional governance and assurance, and **CF** for **Chapter Nine** forum-family doctrine.

Systems-local abstractions may specialize **CJS** joint operational definitions cited in owner text but must not redefine constitutional terms or create parallel constitutional definitions. For the two-tier definition contract, apply [CJS-2.3](../corpus_joint_structure/cjs_02_implementation_integration_map.md#cjs-23-two-tier-definition-contract-binding-abstraction--owner-detail) (*Two-tier definition contract (binding abstraction + owner detail)*).

---

**Previous file:** [cs_01_scope_purpose_identifier_rules.md](cs_01_scope_purpose_identifier_rules.md)

**Next file:** [cs_protocol_a_system_design_testing_verification_deployment.md](cs_protocol_a_system_design_testing_verification_deployment.md)
