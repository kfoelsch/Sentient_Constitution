# CJS-25.105: Drafting Contracts and Owner-to-CJS Seam

<details>
<summary><strong><span style="color: #2563eb;">Corpus placement (non-operative): file structure and reading rules</span></strong></summary>

> This file is **binding incorporated implementation text** where [`corpus_joint_structure.md`](../corpus_joint_structure.md) is incorporated under [Chapter Twenty-Five](../core_25.000_incorporation.md). It must satisfy the Sentient Constitution and does not override or narrow it. It holds **CJS-25.105 §7** (*Intentional Overlap (Non-Duplication Discipline)*), **CJS-25.105 §8** (*Two-Layer Definition Contract (Binding Abstraction + Owner Detail)*), and **CJS-25.105 §8.1** (*Implementation boundary (primary owner to CJS seam)*).
>
> Start at the [Joint structure landing page](../corpus_joint_structure.md) or the [joint-structure reader guide](cjs_reader_guide.md). Most readers reach this file from a citation rather than reading the folder front to back.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream:
  - [CJS-0.110 §3](cjs_00.110_scope_purpose_boundary_interface.md#cjs-0110-3-shared-implementation-corpus-preamble-contract) (*Shared Implementation-Corpus Preamble Contract*) shared implementation-corpus contract;
  - [CJS-0.105 §1](cjs_00.105_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids) (*Cross-File Routing*) topic router;
  - [Chapter Twenty-Five](../core_25.000_incorporation.md#chapter-twenty-five-incorporation-bridge) (31.000) incorporation discipline and
  - [Chapter Three](../core_03.000_definitions_home.md#chapter-three-foundational-definitions) (3.000) canonical definitions.
- Downstream: [CJS-25.105 §7](#cjs-25105-7-intentional-overlap-non-duplication-discipline) (*Intentional Overlap (Non-Duplication Discipline)*); [CJS-25.105 §8](#cjs-25105-8-two-layer-definition-contract-binding-abstraction--owner-detail) (*Two-Layer Definition Contract (Binding Abstraction + Owner Detail)*); [CJS-25.105 §8.1](#cjs-25105-81-implementation-boundary-primary-owner-to-cjs-seam) (*Implementation boundary (primary owner to CJS seam)*).
- Read with: [CJS-0.110 §3](cjs_00.110_scope_purpose_boundary_interface.md#cjs-0110-3-shared-implementation-corpus-preamble-contract) (*Shared Implementation-Corpus Preamble Contract*); [CJS-0.105 §1](cjs_00.105_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids) (*Cross-File Routing*); [Chapter Two §15.4.3](../core_02.030_constitutional_interpretation.md#1543-incorporation-layer) (2.030 §15.4.3) (*cross-file Fullest Protective Effect rule*).

</details>

<br>

Core home: 25
This file is the joint-structure implementation home for **CJS-25.105 §7** (*Intentional Overlap (Non-Duplication Discipline)*), **CJS-25.105 §8** (*Two-Layer Definition Contract (Binding Abstraction + Owner Detail)*), and **CJS-25.105 §8.1** (*Implementation boundary (primary owner to CJS seam)*).

*In plain terms: these sections are for editors and auditors. They say how to split a topic across files without writing two competing rulebooks, and how to keep **CJS** as a connector where another file owns the topic, while leaving CJS-owned rules with CJS.*

## Purpose, Role, and Scope

**Purpose:** Keep shared implementation text and primary-owner detail coordinated when a topic spans files.

**Role:** Sections 7 and 8 set the non-duplication and two-layer drafting contracts. Section 8.1 states the boundary between a primary owner and CJS.

Average readers can skip this file unless a citation sends them here. How to enter the layer: [joint-structure reader guide](cjs_reader_guide.md).

## CJS-25.105 §7: Intentional Overlap (Non-Duplication Discipline)

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Read with: **CJS-25.105 §7** (*Intentional Overlap (Non-Duplication Discipline)*); [CJS-0.105 §1](cjs_00.105_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids) (*Cross-File Routing*).

</details>

<br>

*In plain terms: when a topic is deliberately split across files, the named owner keeps its full rule and the other files add only the connections they need.*

Some topics are **deliberately** split across implementation files — for example contest-integrity design, delegated subunits, or forensic and technical-forum interfaces. For those rows:

- the **primary owner** states the **full operative** rules for the scope that row assigns to it;
- **CJS** text for the same topic adds **joint satisfaction conditions**, **read-with pointers**, and **interface requirements** only when **CJS** is not the **primary owner** for that row;
- do **not** restate **oDef** / **CJS-3.105** (*operational cluster library (oDef)*) clusters and their leg files, **Subcore 4-A** (*Data Types*)/**CS-8.305 (*System classification machinery*) and Subcore 8-A** (*System Classification*) tables, or **CF-** / **CI-** checklists except in brief **quote** or **summary pointer** form when needed for coherence.

Domain-layer overlap discipline: apply [Institutions Overlap Discipline](../corpus_institutions/ci_00.205_registry_and_reading_rules.md#institutions-overlap-discipline), [Forums Overlap Discipline](../corpus_forum/cf_00.405_registry_and_reading_rules.md#forums-overlap-discipline), and [Systems Overlap Discipline](../corpus_systems/cs_00.305_registry_and_reading_rules.md#systems-overlap-discipline) in the respective registry annexes.

## CJS-25.105 §8: Two-Layer Definition Contract (Binding Abstraction + Owner Detail)

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Read with:
  - **CJS-25.105 §8** (*Two-Layer Definition Contract (Binding Abstraction + Owner Detail)*);
  - [CJS-0.105 §1](cjs_00.105_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids) (*Cross-File Routing*);
  - **CJS-25.105 §7** (*Intentional Overlap (Non-Duplication Discipline)*);
  - **CJS-25.105 §8.1** (*Implementation boundary (primary owner to CJS seam)*);
  - [Chapter Two §15.4.3](../core_02.030_constitutional_interpretation.md#1543-incorporation-layer) (2.030 §15.4.3) (*cross-file Fullest Protective Effect rule*).
- Downstream: [CJS-25.105 §8.1 Implementation Boundary (Primary Owner to CJS Seam)](#cjs-25105-81-implementation-boundary-primary-owner-to-cjs-seam).

</details>

<br>

*In plain terms: use a shared binding abstraction only when one owner cannot safely cover the cross-layer issue; leave the detailed tests and procedures with the named owner.*

The CJS folder may adopt **binding high-level joint abstractions** only where a term or construct is materially cross-implementation and cannot be safely interpreted through a single owner file alone.

For this contract:

- **Layer 1 (CJS abstraction):** state only shared admission scope, cross-implementation trigger conditions, and minimum joint consequences needed to avoid contradiction or silent gaps.
- **Layer 2 (owner detail):** retain all operational tests, thresholds, procedures, and implementation mechanics in the **primary owner** section(s) named in **CJS-0.105 §1** (*Cross-File Routing*).
- **No parallel canon:** CJS abstractions must not become a second full taxonomy for domains owned by **CJS**, **CS**, **CI**, or **CF**.
- **Specialize, do not redefine:** owner files may specialize a CJS abstraction for their domain scope but must not redefine it incompatibly.

When CJS text seems to conflict with a **primary owner** section, apply **CJS-25.105 §7** (*Intentional Overlap (Non-Duplication Discipline)*) and **CJS-25.105 §8.1** (*Implementation boundary (primary owner to CJS seam)*): if the CJS text only helps readers connect files, trigger a joint rule, or use shorthand inside one subsection, it does not replace the owner's meaning.

When that boundary does not resolve the conflict, use this order:

1. The Sentient Constitution and core definitions, including **Chapter Twenty-Five**.
2. The canonical owner meaning in **CJS**, **CS**, **CI**, or **CF**, as routed by **CJS-0.105 §1** (*Cross-File Routing*) and the [Chapter One — constitutional owner register](../core_01.000_constitutional_map.md#6-principles-definitions-and-rights).
3. The **Layer 1** CJS abstraction stated in this section.
4. Local shorthand, examples, summaries, or other drafting convenience text, as described in **CJS-0.110 §3** (*Shared Implementation-Corpus Preamble Contract*).

Do not use a broad reading of CJS to change, shrink, expand, or move a rule that belongs to a canonical owner. If the conflict is still unclear after applying this order, do not treat the broader CJS reading as controlling. Send the question to the canonical owner named in **CJS-0.105 §1** (*Cross-File Routing*), including the forum owner in **CF** where forum routing, forum authority, or Chapter Twenty-Two procedure is affected, and update the CJS pointer once the owner clarifies it. For the [Subcore 3-L — Fullest Protective Effect](../subcore_03.080_band_integrative.md#fullest-protective-effect) rule between two adopted implementation standards on the same risk, read [Chapter Two §15.4.3 Incorporation Layer](../core_02.030_constitutional_interpretation.md#1543-incorporation-layer) (*Incorporation layer*, including the cross-file Fullest Protective Effect rule).

Domain-layer read-with contracts: apply [Institutions Read-with Pointers](../corpus_institutions/ci_00.205_registry_and_reading_rules.md#institutions-read-with-pointers), [Forums Read-with Pointers](../corpus_forum/cf_00.405_registry_and_reading_rules.md#forums-read-with-pointers), and [Systems Read-with Pointers](../corpus_systems/cs_00.305_registry_and_reading_rules.md#systems-read-with-pointers) in the respective registry annexes.

### CJS-25.105 §8.1 Implementation Boundary (Primary Owner to CJS Seam)

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream:
  - [CJS-25.105 §8](#cjs-25105-8-two-layer-definition-contract-binding-abstraction--owner-detail) (*Two-Layer Definition Contract (Binding Abstraction + Owner Detail)*);
  - [CJS-0.110 §1](cjs_00.110_scope_purpose_boundary_interface.md#cjs-0110-1-section-identifiers-and-article-references) (*Section Identifiers and Article References*);
  - [CJS-25.105 §7](#cjs-25105-7-intentional-overlap-non-duplication-discipline) (*Intentional Overlap (Non-Duplication Discipline)*);
  - [Chapter Two §15.4.4](../core_02.030_constitutional_interpretation.md#1544-combined-satisfaction-of-jointly-applicable-incorporated-obligations) (2.030 §15.4.4).
- Read with:
  - **CJS-25.105 §8.1** (*Implementation boundary (primary owner to CJS seam)*);
  - **CJS-0.110 §1** (*Section Identifiers and Article References*);
  - **CJS-25.105 §7** (*Intentional Overlap (Non-Duplication Discipline)*);
  - **CJS-25.105 §8** (*Two-Layer Definition Contract (Binding Abstraction + Owner Detail)*);
  - **CJS-0.105 §3** (*Stable Identifiers, Edition Alignment, and Drafting Notes*);
  - [Chapter Two §15.4.4](../core_02.030_constitutional_interpretation.md#1544-combined-satisfaction-of-jointly-applicable-incorporated-obligations) (2.030 §15.4.4);
  - [Chapter Two §15.4.3](../core_02.030_constitutional_interpretation.md#1543-incorporation-layer) (2.030 §15.4.3) (*cross-file Fullest Protective Effect rule*).

</details>

<br>

*In plain terms: **CJS** connects files without taking over another owner’s rules. When editors revise joint-structure text, keep the full rule in the **primary owner** file (**CS**, **CI**, or **CF** where one of those owns the topic), keep **CJS** pointers short, and keep **CJS-3.105 (*Operational cluster library (oDef)*) through CJS-3.135 (*Integrative cross-leg operations (oDef.22–oDef.23)*)** (*operational cluster library (oDef)*) cluster citations traceable under **CJS-0.105 §3** (*Stable Identifiers, Edition Alignment, and Drafting Notes*).*

Under the identifier and definition-home rules in **CJS-0.110 §1** (*Section Identifiers and Article References*), the **CJS-3.105** (*operational cluster library (oDef)*) through **CJS-3.135** (*Integrative cross-leg operations (oDef.22–oDef.23)*) files remain the operative home for **oDef** clusters.

When revising **CJS** joint-structure text:

- keep **CS**, **CI**, or **CF** **primary owner** requirements in those files;
- keep read-with restatements short; and
- preserve **oDef** / **CJS-3.105 (*Operational cluster library (oDef)*) through CJS-3.135 (*Integrative cross-leg operations (oDef.22–oDef.23)*)** citations so references remain traceable under [CJS-0.105 §3](cjs_00.105_registry_and_reading_rules.md#cjs-0105-3-stable-identifiers-edition-alignment-and-drafting-notes) (*Stable Identifiers, Edition Alignment, and Drafting Notes*); the [Subcore 3-L — Fullest Protective Effect](../subcore_03.080_band_integrative.md#fullest-protective-effect) rule remains [Chapter Two §15.4.3 Incorporation Layer](../core_02.030_constitutional_interpretation.md#1543-incorporation-layer) (*Incorporation layer*, including the cross-file Fullest Protective Effect rule).

---

**Previous file:** [cjs_00.110_scope_purpose_boundary_interface.md](cjs_00.110_scope_purpose_boundary_interface.md)

**Next file:** [cjs_03.140_odef_parse_mechanics.md](cjs_03.140_odef_parse_mechanics.md)