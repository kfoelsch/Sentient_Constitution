# Joint-structure registry and reading rules

*In plain terms: this file is the joint-structure **registry annex** — cross-file routing detail, stable family map, and drafting notes. Start reading at [corpus_joint_structure.md](../corpus_joint_structure.md); continue in order at [cjs_01_scope_purpose_boundary_interface.md](cjs_01_scope_purpose_boundary_interface.md).*

<details>
<summary><strong><span style="color: #2563eb;">Corpus placement (non-operative): file structure and reading rules</span></strong></summary>

> The following content is **reader guidance only**. It does not add, remove, or narrow binding obligations elsewhere in this file or in other corpus files.
>
> **Edition and alignment**
> - **Corpus edition:** `SC-Corpus-2026.04.33` · **Effective date:** 2026-04-24
> - These labels track the same edition metadata as the numbered `core_*.md` files (see [README.md](../README.md)), `corpus_systems.md`, `corpus_institutions.md`, and `corpus_forum.md`.
>
> **Status**
> - This is **not** a core constitutional file. It is still part of the constitutional **Corpus** where [Chapter Five](../core_05defs_integrative.md#corpus) and [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) say implementation text is binding when adopted.
> - The CJS folder is written in plain language with low jargon to improve accessibility, audit readability, and practical adoption testing.
>
> **Where this lives**
> - **Navigation wrapper / reader landing:** [corpus_joint_structure.md](../corpus_joint_structure.md) indexes the joint-structure subfiles.
> - **Reader landing:** [corpus_joint_structure.md](../corpus_joint_structure.md) is the human start for this layer. This file is the registry and routing annex, not a second front door.
> - **Shared contract:** **CJS-1.2** (*Shared implementation-corpus preamble contract*) in [cjs_01_scope_purpose_boundary_interface.md](cjs_01_scope_purpose_boundary_interface.md) states authority, readability, shorthand, and canonical-meaning rules for all CJS and implementation files.
> - **Editorial map:** [doc_architecture.md](../doc_architecture.md) is the placement guide; the CJS folder holds binding joint-structural text within **Corpus** as designated in **Chapter Five** and incorporated through **Chapter Sixteen**.
>
> **How to read CJS**
>
> The joint-structure layer (**CJS**) coordinates how **CJS**, **CS**, **CI**, and **CF** fit together when more than one implementation layer applies to the same facts. **Families CJS-0 through CJS-3 are mostly structural** — registry, boundaries, routing, and cross-layer obligations. They bind when routing or adoption says so, but **most readers need not read CJS front to back**.
>
> **Where to start**
>
> | If you are… | Start here |
> |---|---|
> | **Topic-driven** — you know the subject (forum ops, institutional governance, cross-layer integrity) | [topic_router_reader_index.md](../doc_architecture/generated/topic_router_reader_index.md) → primary owner section |
> | **Domain-driven** — you care about forums, institutions, or systems | [corpus_forum.md](../corpus_forum.md), [corpus_institutions.md](../corpus_institutions.md), or [corpus_systems.md](../corpus_systems.md) |
> | **Cross-cutting operational terms** — evidence, procedure, dependency, participation, failure handling, and similar joint terms | [cjs_05_cross_implementation_operational_terms.md](cjs_05_cross_implementation_operational_terms.md) (**CJS-5**) |
>
> **Come back to CJS-0 through CJS-3 when**
> - a citation sends you to **CJS-1.2**, **CJS-2.1**, **CJS-3**, or another section in these families — read that section, not the whole family;
> - you need to know **which file owns a topic** — [CJS-0.1](#cjs-01-cross-file-routing) (*Cross-file routing*) or the topic index;
> - you are **editing or auditing** cross-file routing — **CJS-2.1** and **CJS-0.3**.
>
> Substantive joint rules and operational terms live in **CJS-4** and **CJS-5**; day-to-day domain doctrine lives in **CS**, **CI**, and **CF** as **CJS-2.1** routes.
>
> **Implementation layer map**
>
> - **CJS** — [corpus_joint_structure.md](../corpus_joint_structure.md)
> - **CS** — [corpus_systems.md](../corpus_systems.md)
> - **CI** — [corpus_institutions.md](../corpus_institutions.md)
> - **CF** — [corpus_forum.md](../corpus_forum.md)

</details>

<br>

## CJS-0: Registry and reading rules
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.2](cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline and [Chapter Five](../core_05_definitions_home.md#chapter-five-foundational-definitions) canonical definitions.
- Downstream: [CJS-0.1: Cross-file routing](#cjs-01-cross-file-routing); [CJS-0.2: Joint structure registry](#cjs-02-joint-structure-registry); [CJS-0.3: Stable identifiers, edition alignment, and drafting notes](#cjs-03-stable-identifiers-edition-alignment-and-drafting-notes); [CJS-0.4: Cross-domain implementation layer](#cjs-04-cross-domain-implementation-layer).
- Read with: **CJS-0**; **CJS-0.1**; [CJS-2.1](cjs_02_implementation_integration_map.md#cjs-21-topic-router-stable-ids); **CJS-1**; **CJS-1.1**.

</details>

<br>

*In plain terms: this file is the joint-structure **registry annex** — cross-file routing detail, the section-family map, and maintainer notes. Start at [corpus_joint_structure.md](../corpus_joint_structure.md); continue in order at **CJS-1**.*

**Quick orientation**

The joint-structure layer (**CJS**) coordinates shared interfaces among four implementation layers:

- **CJS** — [corpus_joint_structure.md](../corpus_joint_structure.md)
- **CS** — [corpus_systems.md](../corpus_systems.md)
- **CI** — [corpus_institutions.md](../corpus_institutions.md)
- **CF** — [corpus_forum.md](../corpus_forum.md)

Scope, boundary, and the shared implementation-corpus contract live in the next file: **CJS-1.1** through **CJS-1.3** in [cjs_01_scope_purpose_boundary_interface.md](cjs_01_scope_purpose_boundary_interface.md).

- **CJS-0.1** — cross-file routing: when you need **CJS-2**, how **primary owner** and **mandatory read-with** work, and the topic finder (start here for routing questions).
- **CJS-0.2** — joint-structure section-family registry (**CJS-1** through **CJS-5**).
- **CJS-0.3** — stable identifiers, edition alignment, and maintainer drafting notes.
- **CJS-0.4** — cross-domain implementation layer entry pointer.

### CJS-0.1: Cross-file routing

<a id="cjs-01-cross-file-routing"></a>
<a id="cross-file-routing"></a>
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.2](cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-1.1](cjs_01_scope_purpose_boundary_interface.md#cjs-11-joint-structural-boundary-and-owner-discipline) joint structural boundary; [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline and [Chapter Five](../core_05_definitions_home.md#chapter-five-foundational-definitions) canonical definitions.
- Downstream: this section's local operational requirements for **CJS-0.1: Cross-file routing**.
- Read with: **CJS-0.1**; [CJS-2.1](cjs_02_implementation_integration_map.md#cjs-21-topic-router-stable-ids); **CJS-2**; **CJS-1.1**.

</details>

<br>

*In plain terms: when one topic spans more than one implementation file, the **CJS-2** integration map names where to start and what else to read. Most readers never need to open it.*

**When you need CJS-2**

Stay in the primary owner file for a topic — for example **CF-10** for technical specialist forums or **CI-12** for cross-institution coordination. Each owner file's Trace block states its routing role. Open [CJS-2.1](cjs_02_implementation_integration_map.md#cjs-21-topic-router-stable-ids) when you need the full cross-layer map, you are editing implementation files, or you are auditing whether routing stays complete.

**How cross-file topics work**

Apply topics within the default reading stack named in **CJS-1.1** (*Joint structural boundary and owner discipline*).

- **Start here (primary owner)** — the section that owns the topic's operative rules. A primary owner may be **CJS**, **CS**, **CI**, or **CF**.
- **Also read (mandatory read-with)** — companion sections (and core hooks where listed) that must also be satisfied when the topic materially applies. They complete the topic; they do not replace the primary owner's operative scope.

If a matter triggers more than one cross-layer topic, apply **every** triggered topic whose scope is materially true.

**Topic finder**

Grouped reader index with plain-language links to owner sections: [topic_router_reader_index.md](../doc_architecture/generated/topic_router_reader_index.md) (generated from **CJS-2.1** via `make architecture-index`).

- **Forum operations** — panel formation, routing, appeals, integrity safeguards, continuity, records, staffing, and related topics (primary owners in **CF**).
- **Institutional governance** — delegated bodies, functional lanes, contest-integrity monitoring, coordination, and class-scaled staffing (primary owners in **CI**).
- **Cross-implementation integrity** — trust across layers and assurance/resilience operations (primary owners in **CJS**).

Binding router table, overlap discipline, and definition-tier rules: [cjs_02_implementation_integration_map.md](cjs_02_implementation_integration_map.md) **CJS-2**.

<details>
<summary><strong><span style="color: #2563eb;">Reader guidance (non-operative): routing anchors and cluster index</span></strong></summary>

> The following content is **reader guidance only**. It does not add, remove, or narrow binding obligations elsewhere in this file or in other corpus files.
>
> **Principle-layer routing:** Read with [Chapter One](../core_01_c_stewardship_capacity_principles.md#chapter-01-principles-and-constraints) — [Constitutional Tetrad](../core_00_preamble.md#constitutional-tetrad), [Two Constitutional Aims](../core_00_preamble.md#two-constitutional-aims), and [material stake](../core_00_preamble.md#material-stake). **CJS-5** (*Implementation and cross-implementation operational cluster library*) scales burden and constraint under material stake where materially relevant.
>
> **Implementation anchors**
> - **Routing:** **CJS-0.1** (*Cross-file routing*); operative router in **CJS-2.1** (*Cross-implementation read-with contract*). **CJS-3.6** (*Implementation-label traceability and stricter-wins discipline*) gives stricter-wins discipline.
> - **Joint obligations:** **CJS-3** (*Joint structural obligations (cross-domain requirements)*) gives requirements that must be satisfied together when more than one implementation file applies to the same facts.
> - **Domain limits:** CJS coordinates shared interfaces. It does not replace day-to-day domain rules owned only by `corpus_systems.md`, `corpus_institutions.md`, or `corpus_forum.md`.
>
> **Implementation cross-reference index (routing only):** Joint-structure obligations may connect with **CJS-5** (*Implementation and cross-implementation operational cluster library*) operational clusters. Start at [CJS-5.1 constitutional compass](cjs_05_cross_implementation_operational_terms.md#cjs-51-constitutional-compass-and-cluster-map). For the readable audit process home (what / why / how / when), open **[CJS-5.3](cjs_05_audit_process.md#cjs-53-audit-process-home)** before the Oversight OP annexes. Then the relevant band: **CJS-5.2–CJS-5.6** (Oversight leg OP clusters), **CJS-5.7–CJS-5.10** (Participation leg), **CJS-5.11–CJS-5.15** (Accountability leg), **CJS-5.16–CJS-5.21** (Continuity aim), **CJS-5.22–CJS-5.23** (Integrative cross-leg). This index only helps readers find related material. It does not redefine Chapter Five constitutional terms.

</details>

---

### CJS-0.2: Joint structure registry

<a id="cjs-02-joint-structure-registry"></a>
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.2](cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-2.1](cjs_02_implementation_integration_map.md#cjs-21-topic-router-stable-ids) topic router; [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline and [Chapter Five](../core_05_definitions_home.md#chapter-five-foundational-definitions) canonical definitions.
- Downstream: this section's local operational requirements for **CJS-0.2: Joint structure registry**.
- Read with: **CJS-0**; **CJS-0.2**; **CJS-1**; **CJS-2**; **CJS-3**; **CJS-4**; **CJS-5**.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Definitions · Assessment · Compliance</span></strong></summary>

- [Corpus](../core_05defs_integrative.md#corpus) · [O](../core_05defs_integrative.md#corpus) · [M](../core_05defs_integrative.md#corpus-a) · [A](../core_05defs_integrative.md#corpus-a) · [C](../core_05defs_integrative.md#corpus-c)
- [Authority Stack and Internal Hierarchy](../core_05defs_integrative.md#authority-stack) · [O](../core_05defs_integrative.md#authority-stack) · [M](../core_05defs_integrative.md#authority-stack-a) · [A](../core_05defs_integrative.md#authority-stack-a) · [C](../core_05defs_integrative.md#authority-stack-c)
- [Authority Stack and Internal Hierarchy](../core_05defs_integrative.md#authority-stack) · [O](../core_05defs_integrative.md#authority-stack) · [M](../core_05defs_integrative.md#authority-stack-a) · [A](../core_05defs_integrative.md#authority-stack-a) · [C](../core_05defs_integrative.md#authority-stack-c)

</details>

<br>

*In plain terms: this is the table of contents for the joint-structure folder — stable families **CJS-0** through **CJS-5**, each with a home file.*

These are the stable section families for the CJS folder:

| Family | What it covers | Typical reader | Start here |
|---|---|---|---|
| **CJS-0** | Registry, cross-file routing guide, and reading rules | Editors, auditors, readers who are lost | this file (`cjs_00_registry_and_reading_rules.md`) |
| **CJS-1** | Scope, purpose, and boundary interface | Editors, auditors; general readers when cited | [cjs_01_scope_purpose_boundary_interface.md](cjs_01_scope_purpose_boundary_interface.md) |
| **CJS-2** | Cross-file integration map: read-with contract, overlap discipline, and definition tiers (reading guide in **CJS-0.1**) | Topic lookup, editors, auditors | [cjs_02_implementation_integration_map.md](cjs_02_implementation_integration_map.md) |
| **CJS-3** | General joint structural obligations: requirements that cross domains | Readers handling cross-layer facts; editors, auditors | [cjs_03_joint_structural_obligations.md](cjs_03_joint_structural_obligations.md) |
| **CJS-4** | Specific joint interlocks and shared abstractions | Topic-driven readers when routed; implementers | [cjs_04_specific_joint_interlocks.md](cjs_04_specific_joint_interlocks.md) |
| **CJS-5** | Cross-implementation operational cluster library; audit process home at **CJS-5.3** | Readers needing shared operational terms or the auditing guide | [cjs_05_cross_implementation_operational_terms.md](cjs_05_cross_implementation_operational_terms.md); audit process: [cjs_05_audit_process.md](cjs_05_audit_process.md) |

### CJS-0.3: Stable identifiers, edition alignment, and drafting notes

<a id="cjs-03-stable-identifiers-edition-alignment-and-drafting-notes"></a>
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.2](cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-2.1](cjs_02_implementation_integration_map.md#cjs-21-topic-router-stable-ids) topic router; [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline and [Chapter Five](../core_05_definitions_home.md#chapter-five-foundational-definitions) canonical definitions.
- Downstream: this section's local operational requirements for **CJS-0.3: Stable identifiers, edition alignment, and drafting notes**.
- Read with: **CJS-0.3**; [CJS-2.1](cjs_02_implementation_integration_map.md#cjs-21-topic-router-stable-ids); **CJS-4.1**; **CJS-4.2**; **CJS-4**; **CJS-5**.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Definitions · Assessment · Compliance</span></strong></summary>

- [Corpus](../core_05defs_integrative.md#corpus) · [O](../core_05defs_integrative.md#corpus) · [M](../core_05defs_integrative.md#corpus-a) · [A](../core_05defs_integrative.md#corpus-a) · [C](../core_05defs_integrative.md#corpus-c)
- [Incentive Alignment](../core_05defs_integrative.md#incentive-alignment) · [O](../core_05defs_integrative.md#incentive-alignment) · [M](../core_05defs_integrative.md#incentive-alignment-a) · [A](../core_05defs_integrative.md#incentive-alignment-a) · [C](../core_05defs_integrative.md#incentive-alignment-c)
- [Auditability](../core_05defs_oversight.md#auditability) · [O](../core_05defs_oversight.md#auditability) · [M](../core_05defs_oversight.md#auditability-a) · [A](../core_05defs_oversight.md#auditability-a) · [C](../core_05defs_oversight.md#auditability-c)
- [Risk](../core_05defs_continuity.md#risk) · [O](../core_05defs_continuity.md#risk) · [M](../core_05defs_continuity.md#risk-a) · [A](../core_05defs_continuity.md#risk-a) · [C](../core_05defs_continuity.md#risk-c)

</details>

<br>

*In plain terms: section labels like **CJS-2.1** stay stable across corpus editions so cross-references do not break when text moves between files.*

**Edition alignment:** The visible **Corpus edition** and **Effective date** labels must track **Corpus** labels in adopting instruments and `doc_architecture.md` corpus-alignment notes.


<details>
<summary><strong><span style="color: #2563eb;">Reader guidance (non-operative): maintainer and drafting notes</span></strong></summary>

> The following content is **reader guidance only**. It does not add, remove, or narrow binding obligations elsewhere in this file or in other corpus files.
>
> **Drafting priority (suggested):**
>
> 1. Extend **CJS-2.1** (*Cross-implementation read-with contract*) with new rows only when `doc_architecture.md` section 2 ownership or cross-file overlap changes; keep row IDs **stable** — append new IDs, do not renumber. When a row changes, update the **primary owner** and each **mandatory read-with** section so routing stays **bidirectional** (row ↔ owner ↔ read-with).
> 2. When **CI**/**CF**/**CS** repeat the same joint interface paragraph, prefer a **one-line** pointer to the relevant CJS joint section, including **CJS-4.1** (*Hybrid delegated authority (delegated binding bodies)*) for hybrid composition shared by **CI-9.3.2** (*Authority composition*) and **CF-3.6** (*Chamber authority composition and service mechanics*), and keep operative checklists in the **primary owner**.
> 3. When implementation files repeat the same joint interface paragraph, apply **CJS-4.2** (*Implementation boundary (primary owner to CJS seam)*) the same way: use a **one-line** pointer to **CJS-4** (*Specific joint interlocks and shared abstractions*), **CJS-2.1** (*Cross-implementation read-with contract*), or the applicable **CJS-5** (*Implementation and cross-implementation operational cluster library*) cluster rather than duplicating OP clusters at length.
> 4. Run `make reference-audit` after substantive cross-file moves.
> 5. Where a new high-level joint abstraction is added, verify it remains **Tier 1 only** with no owner-mechanics migration, and record the duplicate-taxonomy risk in the active review notes until the deferred regression path is reinstated.

</details>

<br>

### CJS-0.4: Cross-domain implementation layer

<a id="cjs-04-cross-domain-implementation-layer"></a>
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.2](cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-2.1](cjs_02_implementation_integration_map.md#cjs-21-topic-router-stable-ids) topic router; [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline and [Chapter Five](../core_05_definitions_home.md#chapter-five-foundational-definitions) canonical definitions.
- Downstream: this section's local operational requirements for **CJS-0.4: Cross-domain implementation layer**.
- Read with: **CJS-0**; **CJS-0.4**; **CJS-1**; **CJS-1.1**; [CJS-1.2](cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-2.1](cjs_02_implementation_integration_map.md#cjs-21-topic-router-stable-ids); **CJS-3**; **CJS-3.6**.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Definitions · Assessment · Compliance</span></strong></summary>

- [Corpus](../core_05defs_integrative.md#corpus) · [O](../core_05defs_integrative.md#corpus) · [M](../core_05defs_integrative.md#corpus-a) · [A](../core_05defs_integrative.md#corpus-a) · [C](../core_05defs_integrative.md#corpus-c)
- [Authority Stack and Internal Hierarchy](../core_05defs_integrative.md#authority-stack) · [O](../core_05defs_integrative.md#authority-stack) · [M](../core_05defs_integrative.md#authority-stack-a) · [A](../core_05defs_integrative.md#authority-stack-a) · [C](../core_05defs_integrative.md#authority-stack-c)
- [Emergency and Contingency](../core_05defs_continuity.md#emergency-and-contingency-constitutional) · [O](../core_05defs_continuity.md#emergency-and-contingency-constitutional) · [M](../core_05defs_continuity.md#emergency-and-contingency-constitutional-a) · [A](../core_05defs_continuity.md#emergency-and-contingency-constitutional-a) · [C](../core_05defs_continuity.md#emergency-and-contingency-constitutional-c)
- [Adjudication and Dispute Resolution](../core_05defs_accountability.md#adjudication-and-dispute-resolution-constitutional) · [O](../core_05defs_accountability.md#adjudication-and-dispute-resolution-constitutional) · [M](../core_05defs_accountability.md#adjudication-and-dispute-resolution-constitutional-a) · [A](../core_05defs_accountability.md#adjudication-and-dispute-resolution-constitutional-a) · [C](../core_05defs_accountability.md#adjudication-and-dispute-resolution-constitutional-c)
- [Epistemic Integrity](../core_05defs_oversight.md#epistemic-integrity) · [O](../core_05defs_oversight.md#epistemic-integrity) · [M](../core_05defs_oversight.md#epistemic-integrity-a) · [A](../core_05defs_oversight.md#epistemic-integrity-a) · [C](../core_05defs_oversight.md#epistemic-integrity-c)

</details>

<br>


*In plain terms: when systems, institutions, and forum rules all land on the same facts, read **CJS-1** in the next file — not this registry section.*

Apply [cjs_01_scope_purpose_boundary_interface.md](cjs_01_scope_purpose_boundary_interface.md) **CJS-1.1** (*Joint structural boundary and owner discipline*) and **CJS-1.2** (*Shared implementation-corpus preamble contract*). For read-with routing, stricter-wins, joint obligations, integrity routing, and emergency layering, follow the **CJS-1.2** authority-stack and routing bullets and the **CJS-2.1**, **CJS-3**, **CJS-3.6**, **CJS-4.3**, and **CJS-5** sections they name.

---

**Previous file:** [corpus_joint_structure.md](../corpus_joint_structure.md)

**Next file:** [cjs_01_scope_purpose_boundary_interface.md](cjs_01_scope_purpose_boundary_interface.md)
