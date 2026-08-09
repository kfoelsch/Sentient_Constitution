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
> - This is **not** a core constitutional file. It is still part of the constitutional **Corpus** where [Chapter Five](../core_05_band_integrative.md#corpus) and [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) say implementation text is binding when adopted.
> - The CJS folder is written in plain language with low jargon to improve accessibility, audit readability, and practical adoption testing.
>
> **Where this lives**
> - **Navigation wrapper / reader landing:** [corpus_joint_structure.md](../corpus_joint_structure.md) indexes the joint-structure subfiles.
> - **Reader landing:** [corpus_joint_structure.md](../corpus_joint_structure.md) is the human start for this layer. This file is the registry and routing annex, not a second front door.
> - **Shared contract:** **CJS-1.2** (*Shared implementation-corpus preamble contract*) in [cjs_01_scope_purpose_boundary_interface.md](cjs_01_scope_purpose_boundary_interface.md) states authority, readability, shorthand, and canonical-meaning rules for all CJS and implementation files.
> - **Layer homes:** [Preamble — constitutional owner register](../core_00_preamble.md#constitutional-owner-register) for constitutional chapters and companion corpora; this layer's owns / does-not-own list in [cjs_01_scope_purpose_boundary_interface.md](cjs_01_scope_purpose_boundary_interface.md) (**CJS-1**). The CJS folder holds binding joint-structural text within **Corpus** as designated in **Chapter Five** and incorporated through **Chapter Sixteen**.
>
> **How to read CJS**
>
> The joint-structure layer (**CJS**) coordinates how **CJS**, **CS**, **CI**, and **CF** fit together when more than one implementation layer applies to the same facts. **Families CJS-0 through CJS-3 are mostly structural** — registry, boundaries, routing, and cross-layer obligations. They bind when routing or adoption says so, but **most readers need not read CJS front to back**.
>
> **Where to start**
>
> | If you are… | Start here |
> |---|---|
> | **Topic-driven** — you know the subject (forum ops, institutional governance, cross-layer integrity) | [CJS-0.1](cjs_00_registry_and_reading_rules.md#cjs-01-cross-file-routing) → [topic router reader index](../doc_architecture/generated/topic_router_reader_index.md) → primary owner section |
> | **Domain-driven** — you care about forums, institutions, or systems | [corpus_forum.md](../corpus_forum.md), [corpus_institutions.md](../corpus_institutions.md), or [corpus_systems.md](../corpus_systems.md) |
> | **Cross-cutting operational terms** — evidence, procedure, dependency, participation, failure handling, and similar joint terms | [cjs_05_cross_implementation_operational_terms.md](cjs_05_cross_implementation_operational_terms.md) (**CJS-5**) |
>
> **Come back to CJS-0 through CJS-3 when**
> - a citation sends you to **CJS-1.2**, **CJS-3**, or another *reader-facing* section in these families — read that section, not the whole family;
> - you need to know **which file owns a topic** — [CJS-0.1](#cjs-01-cross-file-routing) (*Cross-file routing*) or the [topic router reader index](../doc_architecture/generated/topic_router_reader_index.md);
> - you are **editing or auditing** cross-file routing — **CJS-2** (integrator map) and **CJS-0.3**.
>
> Substantive joint rules and operational terms live in **CJS-4** and **CJS-5**; day-to-day domain doctrine lives in **CS**, **CI**, and **CF**. **CJS-2** is integrator/maintainer only — not a reader door.
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

- Upstream: [CJS-1.2](cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline and [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions.
- Downstream: [CJS-0.1: Cross-file routing](#cjs-01-cross-file-routing); [CJS-0.2: Joint structure registry](#cjs-02-joint-structure-registry); [CJS-0.3: Stable identifiers, edition alignment, and drafting notes](#cjs-03-stable-identifiers-edition-alignment-and-drafting-notes); [CJS-0.4: Cross-domain implementation layer](#cjs-04-cross-domain-implementation-layer).
- Read with: **CJS-0**; **CJS-0.1**; [CJS-2.1](cjs_00_registry_and_reading_rules.md#cjs-21-topic-router-stable-ids); **CJS-1**; **CJS-1.1**.

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

- **CJS-0.1** — cross-file routing for humans: how **primary owner** and **mandatory read-with** work, and the topic finder. **CJS-2** is integrator/maintainer only.
- **CJS-0.2** — joint-structure section-family registry (**CJS-1** through **CJS-5**).
- **CJS-0.3** — stable identifiers, edition alignment, and maintainer drafting notes.
- **CJS-0.4** — cross-domain implementation layer entry pointer.

### CJS-0.1: Cross-file routing

<a id="cjs-01-cross-file-routing"></a>
<a id="cross-file-routing"></a>
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.2](cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-1.1](cjs_01_scope_purpose_boundary_interface.md#cjs-11-joint-structural-boundary-and-owner-discipline) joint structural boundary; [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline and [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions.
- Downstream: this section's local operational requirements for **CJS-0.1: Cross-file routing**.
- Read with: **CJS-0.1**; [CJS-2.1](cjs_00_registry_and_reading_rules.md#cjs-21-topic-router-stable-ids); **CJS-2**; **CJS-1.1**.

</details>

<br>

*In plain terms: when one topic spans more than one implementation file, this section explains how routing works. Average readers use the topic finder and primary owner — not **CJS-2**.*

**Editors and auditors only — CJS-2**

Do not open the [integrator annex (**CJS-2.1**–**CJS-2.3**)](#joint-structure-domain-routing-integrator-annex) for ordinary reading. Stay in the primary owner file for a topic — for example **CF-10** for technical specialist forums or **CI-12** for cross-institution coordination. Each owner file's Trace block states its routing role. Open **CJS-2** sections in this annex only when editing implementation files, auditing bidirectional routing completeness, or applying the deliberate-split (**CJS-2.2**) or two-tier definition (**CJS-2.3**) contracts.

**How cross-file topics work**

Apply topics within the default reading stack named in **CJS-1.1** (*Joint structural boundary and owner discipline*).

- **Start here (primary owner)** — the section that owns the topic's operative rules. A primary owner may be **CJS**, **CS**, **CI**, or **CF**.
- **Also read (mandatory read-with)** — companion sections (and core hooks where listed) that must also be satisfied when the topic materially applies. They complete the topic; they do not replace the primary owner's operative scope.

If a matter triggers more than one cross-layer topic, apply **every** triggered topic whose scope is materially true.

**Topic finder**

Use the [topic router reader index](../doc_architecture/generated/topic_router_reader_index.md) for a plain-language grouped map, then open the primary owner. This section states how **primary owner** and **mandatory read-with** work; it does not send average readers into **CJS-2**.

- **Forum operations** — panel formation, routing, appeals, integrity safeguards, continuity, records, staffing, and related topics (primary owners in **CF**).
- **Institutional governance** — delegated bodies, functional lanes, contest-integrity monitoring, coordination, and class-scaled staffing (primary owners in **CI**).
- **Cross-implementation integrity** — trust across layers and assurance/resilience operations (primary owners in **CJS**).

<details>
<summary><strong><span style="color: #2563eb;">Reader guidance (non-operative): routing anchors, two-tier plain view, operator-map inventory, and cluster index</span></strong></summary>

> The following content is **reader guidance only**. It does not add, remove, or narrow binding obligations elsewhere in this file or in other corpus files.
>
> **Principle-layer routing:** Read with [Chapter One](../core_01_c_stewardship_capacity_principles.md#chapter-01-principles-and-constraints) — [Constitutional Tetrad](../core_00_preamble.md#constitutional-tetrad), [Two Constitutional Aims](../core_00_preamble.md#two-constitutional-aims), and [material stake](../core_00_preamble.md#material-stake). **CJS-5** (*Implementation and cross-implementation operational cluster library*) scales burden and constraint under material stake where materially relevant.
>
> **Implementation anchors**
> - **Routing (human path):** **CJS-0.1** (*Cross-file routing*) and the [topic router reader index](../doc_architecture/generated/topic_router_reader_index.md). **CJS-3.6** (*Implementation-label traceability and stricter-wins discipline*) gives stricter-wins discipline.
> - **Routing (integrator/maintainer only):** authoritative row IDs and mandatory read-with lists live in **CJS-2.1** — not a reader door.
> - **Joint obligations:** **CJS-3** (*Joint structural obligations (cross-domain requirements)*) gives requirements that must be satisfied together when more than one implementation file applies to the same facts.
> - **Domain limits:** CJS coordinates shared interfaces. It does not replace day-to-day domain rules owned only by `corpus_systems.md`, `corpus_institutions.md`, or `corpus_forum.md`.
>
> **What CJS-2 holds (integrator inventory — do not open for ordinary reading)**
>
> | Section | What it is for |
> |---|---|
> | **CJS-2.1** | Authoritative topic router (stable row IDs and mandatory read-with lists) |
> | **CJS-2.2** | Deliberate-split non-duplication — each file keeps only its slice; primary owner is named in **CJS-2.1** |
> | **CJS-2.3** | Two-tier definition contract — binding skeleton in **CJS**; tests, thresholds, and procedures in the primary owner |
>
> Binding operator text: [Joint structure domain routing (integrator annex)](#joint-structure-domain-routing-integrator-annex) (**CJS-2.1**–**CJS-2.3**).
>
> **Two-tier definitions (plain view):** Some ideas cut across **CJS**, **CS**, **CI**, and **CF**. **CJS** may hold a binding skeleton; operative detail stays in the primary owner. Constitutional vs joint operational definition boundaries: **CJS-1.1**. Editors apply the full contract in **CJS-2.3** when drafting.
>
> **Illustrative split** — lawful panel formation when a forum cannot seat a full bench: **CJS** states shared scope, cross-layer triggers, and minimum joint consequences; the forum owner (**CF-4**) states disclosure, recusal, substitution, and inability-to-form mechanics.
>
> **Deliberate splits:** When one topic is intentionally split across files, each file keeps only its slice; the authoritative owner is named by the router. Editors apply **CJS-2.2** when drafting.
>
> **Implementation cross-reference index (routing only):** Joint-structure obligations may connect with **CJS-5** (*Implementation and cross-implementation operational cluster library*) operational clusters. Start at [CJS-5.1 constitutional compass](cjs_05_cross_implementation_operational_terms.md#cjs-51-constitutional-compass-and-cluster-map). For the readable audit process home (what / why / how / when), open **[CJS-5.3](cjs_05_audit_process.md#cjs-53-audit-process-home)** before the Oversight OP annexes. Then the relevant band: **CJS-5.2–CJS-5.6** (Oversight leg OP clusters), **CJS-5.7–CJS-5.10** (Participation leg), **CJS-5.11–CJS-5.15** (Accountability leg), **CJS-5.16–CJS-5.21** (Continuity aim), **CJS-5.22–CJS-5.23** (Integrative cross-leg). This index only helps readers find related material. It does not redefine Chapter Five constitutional terms.

</details>

---

### CJS-0.2: Joint structure registry

<a id="cjs-02-joint-structure-registry"></a>
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.2](cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-2.1](cjs_00_registry_and_reading_rules.md#cjs-21-topic-router-stable-ids) topic router; [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline and [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions.
- Downstream: this section's local operational requirements for **CJS-0.2: Joint structure registry**.
- Read with: **CJS-0**; **CJS-0.2**; **CJS-1**; **CJS-2**; **CJS-3**; **CJS-4**; **CJS-5**.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Definitions · Assessment · Compliance</span></strong></summary>

- [Corpus](../core_05_band_integrative.md#corpus) · [O](../core_05_band_integrative.md#corpus) · [M](../core_05_band_integrative.md#corpus-a) · [A](../core_05_band_integrative.md#corpus-a) · [C](../core_05_band_integrative.md#corpus-c)
- [Authority Stack and Internal Hierarchy](../core_05_band_integrative.md#authority-stack) · [O](../core_05_band_integrative.md#authority-stack) · [M](../core_05_band_integrative.md#authority-stack-a) · [A](../core_05_band_integrative.md#authority-stack-a) · [C](../core_05_band_integrative.md#authority-stack-c)
- [Authority Stack and Internal Hierarchy](../core_05_band_integrative.md#authority-stack) · [O](../core_05_band_integrative.md#authority-stack) · [M](../core_05_band_integrative.md#authority-stack-a) · [A](../core_05_band_integrative.md#authority-stack-a) · [C](../core_05_band_integrative.md#authority-stack-c)

</details>

<br>

*In plain terms: this is the table of contents for the joint-structure folder — stable families **CJS-0** through **CJS-5**. Default sequential reading is wrapper → **CJS-1** → **CJS-3**; there is no dedicated **CJS-2** family file.*

*Filename note:* There is no dedicated **CJS-2** family file; **CJS-2.1**–**CJS-2.3** live in this annex under [Joint structure domain routing (integrator annex)](#joint-structure-domain-routing-integrator-annex).

These are the stable section families for the CJS folder:

| Family | What it covers | Typical reader | Start here |
|---|---|---|---|
| **CJS-0** | Registry, cross-file routing guide, and reading rules | Editors, auditors, readers who are lost | this file (`cjs_00_registry_and_reading_rules.md`) |
| **CJS-1** | Scope, purpose, and boundary interface | Editors, auditors; general readers when cited | [cjs_01_scope_purpose_boundary_interface.md](cjs_01_scope_purpose_boundary_interface.md) |
| **CJS-2** | Integrator/maintainer integration map only — not reader-facing; no dedicated family file (human guide in **CJS-0.1** + reader index) | Editors, auditors | [CJS-2.1](#cjs-21-topic-router-stable-ids) in this file |
| **CJS-3** | General joint structural obligations: requirements that cross domains | Readers handling cross-layer facts; editors, auditors | [cjs_03_joint_structural_obligations.md](cjs_03_joint_structural_obligations.md) |
| **CJS-4** | Specific joint interlocks and shared abstractions | Topic-driven readers when routed; implementers | [cjs_04_specific_joint_interlocks.md](cjs_04_specific_joint_interlocks.md) |
| **CJS-5** | Cross-implementation operational cluster library; audit process home at **CJS-5.3** | Readers needing shared operational terms or the auditing guide | [cjs_05_cross_implementation_operational_terms.md](cjs_05_cross_implementation_operational_terms.md); audit process: [cjs_05_audit_process.md](cjs_05_audit_process.md) |

### CJS-0.3: Stable identifiers, edition alignment, and drafting notes

<a id="cjs-03-stable-identifiers-edition-alignment-and-drafting-notes"></a>
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.2](cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-2.1](cjs_00_registry_and_reading_rules.md#cjs-21-topic-router-stable-ids) topic router; [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline and [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions.
- Downstream: this section's local operational requirements for **CJS-0.3: Stable identifiers, edition alignment, and drafting notes**.
- Read with: **CJS-0.3**; [CJS-2.1](cjs_00_registry_and_reading_rules.md#cjs-21-topic-router-stable-ids); **CJS-4.1**; **CJS-4.2**; **CJS-4**; **CJS-5**.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Definitions · Assessment · Compliance</span></strong></summary>

- [Corpus](../core_05_band_integrative.md#corpus) · [O](../core_05_band_integrative.md#corpus) · [M](../core_05_band_integrative.md#corpus-a) · [A](../core_05_band_integrative.md#corpus-a) · [C](../core_05_band_integrative.md#corpus-c)
- [Incentive Alignment](../core_05_band_integrative.md#incentive-alignment) · [O](../core_05_band_integrative.md#incentive-alignment) · [M](../core_05_band_integrative.md#incentive-alignment-a) · [A](../core_05_band_integrative.md#incentive-alignment-a) · [C](../core_05_band_integrative.md#incentive-alignment-c)
- [Auditability](../core_05_band_oversight.md#auditability) · [O](../core_05_band_oversight.md#auditability) · [M](../core_05_band_oversight.md#auditability-a) · [A](../core_05_band_oversight.md#auditability-a) · [C](../core_05_band_oversight.md#auditability-c)
- [Risk](../core_05_band_continuity.md#risk) · [O](../core_05_band_continuity.md#risk) · [M](../core_05_band_continuity.md#risk-a) · [A](../core_05_band_continuity.md#risk-a) · [C](../core_05_band_continuity.md#risk-c)

</details>

<br>

*In plain terms: section labels like **CJS-2.1** stay stable across corpus editions so cross-references do not break when text moves between files.*

**Edition alignment:** The visible **Corpus edition** and **Effective date** labels must track **Corpus** labels in adopting instruments and [README.md](../README.md) edition metadata.


<details>
<summary><strong><span style="color: #2563eb;">Reader guidance (non-operative): maintainer and drafting notes</span></strong></summary>

> The following content is **reader guidance only**. It does not add, remove, or narrow binding obligations elsewhere in this file or in other corpus files.
>
> **Drafting priority (suggested):**
>
> 1. Extend **CJS-2.1** (*Cross-implementation read-with contract*) with new rows only when the [Preamble — constitutional owner register](../core_00_preamble.md#constitutional-owner-register) or cross-file overlap changes; keep row IDs **stable** — append new IDs, do not renumber. When a row changes, update the **primary owner** and each **mandatory read-with** section so routing stays **bidirectional** (row ↔ owner ↔ read-with).
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

- Upstream: [CJS-1.2](cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-2.1](cjs_00_registry_and_reading_rules.md#cjs-21-topic-router-stable-ids) topic router; [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline and [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions.
- Downstream: this section's local operational requirements for **CJS-0.4: Cross-domain implementation layer**.
- Read with: **CJS-0**; **CJS-0.4**; **CJS-1**; **CJS-1.1**; [CJS-1.2](cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-2.1](cjs_00_registry_and_reading_rules.md#cjs-21-topic-router-stable-ids); **CJS-3**; **CJS-3.6**.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Definitions · Assessment · Compliance</span></strong></summary>

- [Corpus](../core_05_band_integrative.md#corpus) · [O](../core_05_band_integrative.md#corpus) · [M](../core_05_band_integrative.md#corpus-a) · [A](../core_05_band_integrative.md#corpus-a) · [C](../core_05_band_integrative.md#corpus-c)
- [Authority Stack and Internal Hierarchy](../core_05_band_integrative.md#authority-stack) · [O](../core_05_band_integrative.md#authority-stack) · [M](../core_05_band_integrative.md#authority-stack-a) · [A](../core_05_band_integrative.md#authority-stack-a) · [C](../core_05_band_integrative.md#authority-stack-c)
- [Emergency and Contingency](../core_05_band_continuity.md#emergency-and-contingency-constitutional) · [O](../core_05_band_continuity.md#emergency-and-contingency-constitutional) · [M](../core_05_band_continuity.md#emergency-and-contingency-constitutional-a) · [A](../core_05_band_continuity.md#emergency-and-contingency-constitutional-a) · [C](../core_05_band_continuity.md#emergency-and-contingency-constitutional-c)
- [Adjudication and Dispute Resolution](../core_05_band_accountability.md#adjudication-and-dispute-resolution-constitutional) · [O](../core_05_band_accountability.md#adjudication-and-dispute-resolution-constitutional) · [M](../core_05_band_accountability.md#adjudication-and-dispute-resolution-constitutional-a) · [A](../core_05_band_accountability.md#adjudication-and-dispute-resolution-constitutional-a) · [C](../core_05_band_accountability.md#adjudication-and-dispute-resolution-constitutional-c)
- [Epistemic Integrity](../core_05_band_oversight.md#epistemic-integrity) · [O](../core_05_band_oversight.md#epistemic-integrity) · [M](../core_05_band_oversight.md#epistemic-integrity-a) · [A](../core_05_band_oversight.md#epistemic-integrity-a) · [C](../core_05_band_oversight.md#epistemic-integrity-c)

</details>

<br>


*In plain terms: when systems, institutions, and forum rules all land on the same facts, read **CJS-1** in the next sequential file — not this registry section.*

Apply [cjs_01_scope_purpose_boundary_interface.md](cjs_01_scope_purpose_boundary_interface.md) **CJS-1.1** (*Joint structural boundary and owner discipline*) and **CJS-1.2** (*Shared implementation-corpus preamble contract*). For read-with routing, stricter-wins, joint obligations, integrity routing, and emergency layering, follow the **CJS-1.2** authority-stack and routing bullets and the **CJS-2.1**, **CJS-3**, **CJS-3.6**, **CJS-4.3**, and **CJS-5** sections they name.

---

## Joint structure domain routing (integrator annex)

<a id="joint-structure-domain-routing-integrator-annex"></a>
<a id="cjs-2-implementation-integration-map"></a>
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.2](cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-2.1](#cjs-21-topic-router-stable-ids) topic router; [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline and [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions.
- Downstream: [CJS-2.1: Cross-implementation read-with contract](#cjs-21-topic-router-stable-ids); [CJS-2.2: Intentional overlap (non-duplication discipline)](#cjs-22-intentional-overlap-non-duplication-discipline); [CJS-2.3: Two-tier definition contract (binding abstraction + owner detail)](#cjs-23-two-tier-definition-contract-binding-abstraction--owner-detail).
- Read with: **CJS-2**; [CJS-2.1](#cjs-21-topic-router-stable-ids); **CJS-2.2**; **CJS-2.3**; **CJS-3**; **CJS-3.6**; **CJS-1.2**.
- Integrator index (non-operative): authoritative **CJS-R** router table in **CJS-2.1** (*Cross-implementation read-with contract*).

</details>

<br>

*Filename note:* There is no dedicated **CJS-2** family file; **CJS-2.1**–**CJS-2.3** live in this annex. Default sequential reading is wrapper → **CJS-1** → **CJS-3**.

### CJS-2.1: Cross-implementation read-with contract

<a id="cjs-21-topic-router-stable-ids"></a>
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.2](cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-2.1](#cjs-21-topic-router-stable-ids) topic router; [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline and [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions.
- Downstream: this section's local operational requirements for **CJS-2.1: Cross-implementation read-with contract**.
- Read with: [CJS-2.1](#cjs-21-topic-router-stable-ids); **CJS-4.1**; **CJS-4.5**; **CJS-4.3**; **CJS-4.4**; [CJS-2.3](#cjs-23-two-tier-definition-contract-binding-abstraction--owner-detail); [CJS-1.1](cjs_01_scope_purpose_boundary_interface.md#cjs-11-joint-structural-boundary-and-owner-discipline).

</details>

<br>

When implementation text intersects other implementation layers, apply the default reading stack in [CJS-1.1](cjs_01_scope_purpose_boundary_interface.md#cjs-11-joint-structural-boundary-and-owner-discipline) (*Joint structural boundary and owner discipline*). Within that stack, read only what **CJS-2.1** routes for the topic.

Router rows are **indicative**, not exhaustive: if a matter triggers multiple rows, apply **all** triggered rows whose scope is materially true.

Joint abstractions and constitutional non-redefinition discipline: [CJS-1.1](cjs_01_scope_purpose_boundary_interface.md#cjs-11-joint-structural-boundary-and-owner-discipline) (*Joint structural boundary and owner discipline*) and the two-tier contract in [CJS-2.3](#cjs-23-two-tier-definition-contract-binding-abstraction--owner-detail) (*Two-tier definition contract (binding abstraction + owner detail)*).

<details>
<summary><strong><span style="color: #2563eb;">Integrator reference: full router table (stable row IDs)</span></strong></summary>

> Maintainer and audit surface. Stable row IDs (**CJS-R01** (*Delegated binding bodies and hybrid composition (non-forum institutions)*)–**CJS-R19** (*integrity assurance and resilience operations*)) are **corpus-local** labels; they are **not** Sentient Constitution article numbers.

**Bidirectional routing:** The **primary owner** must cite its **CJS-R** row here and the same mandatory read-with list — or a one-line pointer to that row for the full list. Each **mandatory read-with** section must cite the row and **primary owner** where the topic materially applies. Do not maintain a second competing read-with list in the owner file.

| Row ID | Topic | Primary owner | Mandatory read-with |
|--------|--------|---------------|---------------------|
| **CJS-R01** | Delegated binding bodies and hybrid composition (non-forum institutions) | `corpus_institutions.md` **CI-9.3** | **CJS-4.1**, **CJS-4.5**, **CJS-5.13** (*Accountability: procedural integrity and adjudication terms*); `corpus_systems.md` **CS-3 — System classification and handling**, **CS-4 — Critical system stewardship**; `corpus_institutions.md` **CI-3**; the CJS implementation layer **CJS-5.11 and CJS-5.7 — Distributed and Proportional Authority**, **CJS-5.12 — Burden of Justification and Constraint** (as cited in owner text) |
| **CJS-R02** | Forum chambers, divisions, and designated panels (Chapter Eleven families) | `corpus_forum.md` **CF-3.5**–**CF-3.8** | **CJS-4.1**, **CJS-4.5**, **CJS-5.13** (*Accountability: procedural integrity and adjudication terms*); `corpus_institutions.md` **CI-9.3**; `corpus_systems.md` **CS-3 — System classification and handling**, **CS-4 — Critical system stewardship**; `core_11-11_forum.md` **Chapter Eleven** |
| **CJS-R03** | Lawful panel formation, disclosure, recusal, substitution, inability-to-form | `corpus_forum.md` **CF-4** | **CJS-4.5**, **CJS-5.13** (*Accountability: procedural integrity and adjudication terms*); `corpus_institutions.md` **CI-4**, **CI-5**; `core_09-09_standing_integration.md` **Chapter Nine §5.5** (*Special locks*), **§6.2** (*Competency bars and clearances*), and **§8** (*Restoration and reassessment*); `core_11-11_forum.md` **Chapter Eleven**; the CJS implementation layer **CJS-5.13 — Procedural Integrity and Adjudication** |
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
| **CJS-R14** | Institutional functional lanes and non-delegable splits | `corpus_institutions.md` **CI-3** | the CJS implementation layer **CJS-5.11 and CJS-5.7 — Distributed and Proportional Authority**; `corpus_systems.md` **CS-4 — Critical system stewardship** where CSS stewardship intersects |
| **CJS-R15** | Contest-integrity monitoring (pathway integrity, not merits) | `corpus_institutions.md` **CI-7.3** | `corpus_systems.md` **CS-3 — System classification and handling**, **CS-3** (including steward contest-integrity paragraphs where applicable); the CJS implementation layer **CJS-5.13 — Procedural Integrity and Adjudication**; the lawful-panel and forum-performance router topics (**CJS-R03** and **CJS-R10**) where forum performance data feeds monitors |
| **CJS-R16** | Cross-institution coordination, deadlock, and escalation | `corpus_institutions.md` **CI-12** | `corpus_forum.md` **CF-5**, **CF-7**; `core_11-11_forum.md` **Chapter Eleven** (including backup and cross-forum integrity routing) |
| **CJS-R17** | Cross-implementation trust integrity (joint operation model) | **CJS-4.3 — Cross-implementation trust integrity** | [Chapter Five section **3.11**](../core_05_band_oversight.md#trust-and-trustworthiness-cluster) (*Trust*, *Trustworthiness*, *Trust Degradation and Misleading Reliance*); `corpus_systems.md` **CS-3 — System classification and handling**, **CS-4 — Critical system stewardship** where classification or dependency scales assurance burden; **CJS-5.9** (*Participation: salience integrity and attention-allocation terms*), **CJS-5.10** (*Participation: disclosure sufficiency and observability terms*), **CJS-5.16** (*Continuity: dependency integrity and disclosure terms*), **CJS-5.19** (*Continuity: graceful degradation and failure-mode integrity terms*), **CJS-5.17** (*Continuity: interoperability, portability, and exit-integrity terms*), **CJS-5.3** (*Oversight: auditability and reconstructability terms*), **CJS-5.5** (*Oversight: independent verification and claim-integrity terms*), **CJS-5.20** (*Continuity: reversibility and containment terms*), and **CJS-5.18** (*Continuity: data-retention and lifecycle-integrity terms*) where the trust claim depends on the corresponding operational fact; `corpus_institutions.md` **CI-7.3**, **CI-8** and `corpus_forum.md` **CF-11** where pathway integrity, publication cadence, or accessibility materially conditions justified trust |
| **CJS-R18** | Class-scaled lane staffing and competency redundancy for materially binding stewardship | `corpus_institutions.md` **CI-3**, **CI-4**, **CI-11**, **CI-12** | **CJS-4.4**; **CJS-5.11** (*Accountability: distributed and proportional authority terms*); `corpus_systems.md` **CS-3 — System classification and handling**, **CS-4 — Critical system stewardship**; `core_12-12_governance.md` **Chapter Twelve**, section **5** |
| **CJS-R19** | integrity assurance and resilience operations | **CJS-5.6** (*Oversight: integrity assurance and resilience operations*) | the CJS implementation layer **CJS-5.3 — Auditability** through **CJS-5.15 and CJS-5.6 — Evolution, Revalidation, and Non-Entrenchment**; **Chapter Five** (*Auditability*, *Verifiability*, *Reversibility*, *Dependency*, *Cascading Failure*, *Adversarial, Scaled, and Exploited Conditions*, *Trustworthiness*); `corpus_systems.md` **CS-2 — Information types and handling**, **CS-3 — System classification and handling**, **CS-4 — Critical system stewardship** where classification, data handling, or stewardship scales burden; `corpus_institutions.md` **CI-7.3**, **CI-8** and `corpus_forum.md` **CF-11** where monitoring, escalation, publication, or review pathways are materially required |

</details>

### CJS-2.2: Intentional overlap (non-duplication discipline)

<a id="cjs-22-intentional-overlap-non-duplication-discipline"></a>
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.2](cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-2.1](#cjs-21-topic-router-stable-ids) topic router; [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline and [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions.
- Downstream: this section's local operational requirements for **CJS-2.2: Intentional overlap (non-duplication discipline)**.
- Read with: **CJS-2.2**; [CJS-2.1](#cjs-21-topic-router-stable-ids).

</details>

<br>

Some topics are **deliberately** split across implementation files — for example contest-integrity design, delegated subunits, or forensic and technical-forum interfaces. For those rows:

- the **primary owner** states the **full operative** rules for the scope that row assigns to it;
- **CJS** text for the same topic adds **joint satisfaction conditions**, **read-with pointers**, and **interface requirements** only when **CJS** is not the **primary owner** for that row;
- do **not** restate **CJS-5** (*Implementation and cross-implementation operational cluster library*) OP clusters, **CS-2/CS-3** tables, or **CF-** / **CI-** checklists except in brief **quote** or **summary pointer** form when needed for coherence.

Domain-layer overlap discipline: apply [Institutions overlap discipline](../corpus_institutions/ci_00_registry_and_reading_rules.md#institutions-overlap-discipline), [Forums overlap discipline](../corpus_forum/cf_00_registry_and_reading_rules.md#forums-overlap-discipline), and [Systems overlap discipline](../corpus_systems/cs_00_registry_and_reading_rules.md#systems-overlap-discipline) in the respective registry annexes.

### CJS-2.3: Two-tier definition contract (binding abstraction + owner detail)

<a id="cjs-23-two-tier-definition-contract-binding-abstraction--owner-detail"></a>
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.2](cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-2.1](#cjs-21-topic-router-stable-ids) topic router; [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline and [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions.
- Downstream: this section's local operational requirements for **CJS-2.3: Two-tier definition contract (binding abstraction + owner detail)**.
- Read with: **CJS-2.3**; [CJS-2.1](#cjs-21-topic-router-stable-ids); **CJS-2.2**; **CJS-4.2**; **CJS-3.6**.

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
2. The canonical owner meaning in **CJS**, **CS**, **CI**, or **CF**, as routed by **CJS-2.1** (*Topic router (stable IDs)*) and the [Preamble — constitutional owner register](../core_00_preamble.md#constitutional-owner-register).
3. The **Tier 1** CJS abstraction stated in this section.
4. Local shorthand, examples, summaries, or other drafting convenience text, as described in **CJS-1.2** (*Shared implementation-corpus preamble contract*).

Do not use a broad reading of CJS to change, shrink, expand, or move a rule that belongs to a canonical owner. If the conflict is still unclear after applying this order, do not treat the broader CJS reading as controlling. Send the question to the canonical owner named in **CJS-2.1**, including the forum owner in **CF** where forum routing, forum authority, or Chapter Eleven procedure is affected, and update the CJS pointer once the owner clarifies it. For stricter-wins between two adopted implementation standards on the same risk, read **CJS-3.6** (*Implementation-label traceability and stricter-wins discipline*).

Domain-layer read-with contracts: apply [Institutions read-with pointers](../corpus_institutions/ci_00_registry_and_reading_rules.md#institutions-read-with-pointers), [Forums read-with pointers](../corpus_forum/cf_00_registry_and_reading_rules.md#forums-read-with-pointers), and [Systems read-with pointers](../corpus_systems/cs_00_registry_and_reading_rules.md#systems-read-with-pointers) in the respective registry annexes.

---

**Previous file:** [corpus_joint_structure.md](../corpus_joint_structure.md)

**Next file:** [cjs_01_scope_purpose_boundary_interface.md](cjs_01_scope_purpose_boundary_interface.md)
