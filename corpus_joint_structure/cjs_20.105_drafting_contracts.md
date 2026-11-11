# CJS-20.105: Drafting Contracts and Owner-to-CJS Seam

<details>
<summary><strong><span style="color: #2563eb;">Corpus placement (non-operative): file structure and reading rules</span></strong></summary>

> This file is **binding incorporated implementation text** where [`corpus_joint_structure.md`](../corpus_joint_structure.md) is incorporated under [Chapter Twenty](../core_20.000_incorporation.md). It must satisfy the Sentient Constitution and does not override or narrow it. It holds **CJS-20.105 §7** (*drafting contracts and the primary-owner-to-CJS seam*), **CJS-20.105 §8**, and **CJS-20.105 §8.1**.
>
> Start at the [Joint structure landing page](../corpus_joint_structure.md) or the [joint-structure reader guide](cjs_reader_guide.md). Most readers reach this file from a citation rather than reading the folder front to back.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream:
  - [CJS-0.110 §3](cjs_00.110_scope_purpose_boundary_interface.md#cjs-0110-3-shared-implementation-corpus-preamble-contract) (*Shared Implementation-Corpus Preamble Contract*) shared implementation-corpus contract;
  - [CJS-0.105 §1](cjs_00.105_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids) (*Cross-File Routing*) topic router;
  - [Chapter Twenty](../core_20.000_incorporation.md#chapter-twenty-incorporation-bridge) (20.000) incorporation discipline and
  - [Chapter Five](../core_05.000_definitions_home.md#chapter-five-foundational-definitions) (5.000) canonical definitions.
- Downstream: [CJS-20.105 §7](#cjs-20105-7-intentional-overlap-non-duplication-discipline) (*Intentional Overlap (Non-Duplication Discipline)*); [CJS-20.105 §8](#cjs-20105-8-two-layer-definition-contract-binding-abstraction--owner-detail) (*Two-Layer Definition Contract (Binding Abstraction + Owner Detail)*); [CJS-20.105 §8.1](#cjs-20105-81-implementation-boundary-primary-owner-to-cjs-seam) (*Implementation boundary (primary owner to CJS seam)*).
- Read with: [CJS-0.110 §3](cjs_00.110_scope_purpose_boundary_interface.md#cjs-0110-3-shared-implementation-corpus-preamble-contract) (*Shared Implementation-Corpus Preamble Contract*); [CJS-0.105 §1](cjs_00.105_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids) (*Cross-File Routing*); [Chapter One §15.4.3](../core_01.005_interaction_interpretation.md#1543-incorporation-layer) (1.005 §15.4.3) (*cross-file Fullest Protective Effect rule*).

</details>

<br>

Core home: 20

This file is the joint-structure implementation home for **CJS-20.105 §7** (*Intentional Overlap (Non-Duplication Discipline)*), **CJS-20.105 §8** (*Two-Layer Definition Contract (Binding Abstraction + Owner Detail)*), and **CJS-20.105 §8.1** (*Implementation boundary (primary owner to CJS seam)*).

*In plain terms: these sections are for editors and auditors. They say how to split a topic across files without writing two competing rulebooks, and how to keep **CJS** as a connector rather than a second owner.*

Average readers can skip this file unless a citation sends them here. How to enter the layer: [joint-structure reader guide](cjs_reader_guide.md).

## CJS-20.105 §7: Intentional Overlap (Non-Duplication Discipline)


<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Read with: **CJS-20.105 §7** (*Intentional Overlap (Non-Duplication Discipline)*); [CJS-0.105 §1](cjs_00.105_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids) (*Cross-File Routing*).

</details>

<br>

Some topics are **deliberately** split across implementation files — for example contest-integrity design, delegated subunits, or forensic and technical-forum interfaces. For those rows:

- the **primary owner** states the **full operative** rules for the scope that row assigns to it;
- **CJS** text for the same topic adds **joint satisfaction conditions**, **read-with pointers**, and **interface requirements** only when **CJS** is not the **primary owner** for that row;
- do **not** restate **oDef** / **CJS-5.105** (*operational cluster library (oDef)*) clusters and their leg files, **CS-6.305 (*Information types and handling*) and CS-6.310** (*Data Classifications*)/**CS-9.305 (*System classification machinery*) and CS-9.310** (*System Impact Classifications*) tables, or **CF-** / **CI-** checklists except in brief **quote** or **summary pointer** form when needed for coherence.

Domain-layer overlap discipline: apply [Institutions Overlap Discipline](../corpus_institutions/ci_00.205_registry_and_reading_rules.md#institutions-overlap-discipline), [Forums Overlap Discipline](../corpus_forum/cf_00.405_registry_and_reading_rules.md#forums-overlap-discipline), and [Systems Overlap Discipline](../corpus_systems/cs_00.305_registry_and_reading_rules.md#systems-overlap-discipline) in the respective registry annexes.

## CJS-20.105 §8: Two-Layer Definition Contract (Binding Abstraction + Owner Detail)


<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Read with:
  - **CJS-20.105 §8** (*Two-Layer Definition Contract (Binding Abstraction + Owner Detail)*);
  - [CJS-0.105 §1](cjs_00.105_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids) (*Cross-File Routing*);
  - **CJS-20.105 §7** (*Intentional Overlap (Non-Duplication Discipline)*);
  - **CJS-20.105 §8.1** (*Implementation boundary (primary owner to CJS seam)*);
  - [Chapter One §15.4.3](../core_01.005_interaction_interpretation.md#1543-incorporation-layer) (1.005 §15.4.3) (*cross-file Fullest Protective Effect rule*).
- Downstream: [CJS-20.105 §8.1 Implementation Boundary (Primary Owner to CJS Seam)](#cjs-20105-81-implementation-boundary-primary-owner-to-cjs-seam).

</details>

<br>

The CJS folder may adopt **binding high-level joint abstractions** only where a term or construct is materially cross-implementation and cannot be safely interpreted through a single owner file alone.

For this contract:

- **Layer 1 (CJS abstraction):** state only shared admission scope, cross-implementation trigger conditions, and minimum joint consequences needed to avoid contradiction or silent gaps.
- **Layer 2 (owner detail):** retain all operational tests, thresholds, procedures, and implementation mechanics in the **primary owner** section(s) named in **CJS-0.105 §1** (*Cross-File Routing*).
- **No parallel canon:** CJS abstractions must not become a second full taxonomy for domains owned by **CJS**, **CS**, **CI**, or **CF**.
- **Specialize, do not redefine:** owner files may specialize a CJS abstraction for their domain scope but must not redefine it incompatibly.

When CJS text seems to conflict with a **primary owner** section, apply **CJS-20.105 §7** (*Intentional Overlap (Non-Duplication Discipline)*) and **CJS-20.105 §8.1** (*Implementation boundary (primary owner to CJS seam)*): if the CJS text only helps readers connect files, trigger a joint rule, or use shorthand inside one subsection, it does not replace the owner's meaning.

When that boundary does not resolve the conflict, use this order:

1. The Sentient Constitution and core definitions, including **Chapter Twenty**.
2. The canonical owner meaning in **CJS**, **CS**, **CI**, or **CF**, as routed by **CJS-0.105 §1** (*Topic router (stable IDs)*) and the [Preamble — constitutional owner register](../core_00.000_preamble.md#4-principles-definitions-and-rights).
3. The **Layer 1** CJS abstraction stated in this section.
4. Local shorthand, examples, summaries, or other drafting convenience text, as described in **CJS-0.110 §3** (*Shared Implementation-Corpus Preamble Contract*).

Do not use a broad reading of CJS to change, shrink, expand, or move a rule that belongs to a canonical owner. If the conflict is still unclear after applying this order, do not treat the broader CJS reading as controlling. Send the question to the canonical owner named in **CJS-0.105 §1** (*Cross-File Routing*), including the forum owner in **CF** where forum routing, forum authority, or Chapter Fifteen procedure is affected, and update the CJS pointer once the owner clarifies it. For the [Fullest Protective Effect](../core_05.045_band_integrative.md#fullest-protective-effect) rule between two adopted implementation standards on the same risk, read [Chapter One §15.4.3 Incorporation Layer](../core_01.005_interaction_interpretation.md#1543-incorporation-layer) (*Incorporation layer*, including the cross-file Fullest Protective Effect rule).

Domain-layer read-with contracts: apply [Institutions Read-with Pointers](../corpus_institutions/ci_00.205_registry_and_reading_rules.md#institutions-read-with-pointers), [Forums Read-with Pointers](../corpus_forum/cf_00.405_registry_and_reading_rules.md#forums-read-with-pointers), and [Systems Read-with Pointers](../corpus_systems/cs_00.305_registry_and_reading_rules.md#systems-read-with-pointers) in the respective registry annexes.

### CJS-20.105 §8.1 Implementation Boundary (Primary Owner to CJS Seam)

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream:
  - [CJS-20.105 §8](#cjs-20105-8-two-layer-definition-contract-binding-abstraction--owner-detail) (*Two-Layer Definition Contract (Binding Abstraction + Owner Detail)*);
  - [CJS-0.110 §1](cjs_00.110_scope_purpose_boundary_interface.md#cjs-0110-1-section-identifiers-and-article-references) (*Section Identifiers and Article References*);
  - [CJS-20.105 §7](#cjs-20105-7-intentional-overlap-non-duplication-discipline) (*Intentional Overlap (Non-Duplication Discipline)*);
  - [Chapter One §15.4.4](../core_01.005_interaction_interpretation.md#1544-combined-satisfaction-of-jointly-applicable-incorporated-obligations) (1.005 §15.4.4).
- Read with:
  - **CJS-20.105 §8.1** (*Implementation boundary (primary owner to CJS seam)*);
  - **CJS-0.110 §1** (*Section Identifiers and Article References*);
  - **CJS-20.105 §7** (*Intentional Overlap (Non-Duplication Discipline)*);
  - **CJS-20.105 §8** (*Two-Layer Definition Contract (Binding Abstraction + Owner Detail)*);
  - **CJS-0.105 §3** (*Stable Identifiers, Edition Alignment, and Drafting Notes*);
  - [Chapter One §15.4.4](../core_01.005_interaction_interpretation.md#1544-combined-satisfaction-of-jointly-applicable-incorporated-obligations) (1.005 §15.4.4);
  - [Chapter One §15.4.3](../core_01.005_interaction_interpretation.md#1543-incorporation-layer) (1.005 §15.4.3) (*cross-file Fullest Protective Effect rule*).

</details>

<br>

*In plain terms: **CJS** connects files — it does not swallow them. When editors revise joint-structure text, keep the full rule in the **primary owner** file (**CS**, **CI**, or **CF**), keep **CJS** pointers short, and keep **CJS-5.105 (*Operational cluster library (oDef)*) through CJS-5.135 (*Integrative cross-leg operations (oDef.22–oDef.23)*)** (*operational cluster library (oDef)*) cluster citations traceable under **CJS-0.105 §3** (*Stable Identifiers, Edition Alignment, and Drafting Notes*).*

Under the identifier and definition-home rules in **CJS-0.110 §1** (*Section Identifiers and Article References*), the **CJS-5.105 (*Operational cluster library (oDef)*) through CJS-5.135 (*Integrative cross-leg operations (oDef.22–oDef.23)*)** (*operational cluster library (oDef)*) files remain the operative home for **oDef** clusters (**oDef.*n*** = **CJS-5.105 (*Operational cluster library (oDef)*) through CJS-5.135 (*Integrative cross-leg operations (oDef.22–oDef.23)*).*n***).

When revising **CJS** joint-structure text:
- keep **CS**, **CI**, or **CF** **primary owner** requirements in those files;
- keep read-with restatements short; and
- preserve **oDef** / **CJS-5.105 (*Operational cluster library (oDef)*) through CJS-5.135 (*Integrative cross-leg operations (oDef.22–oDef.23)*)** citations so references remain traceable under [CJS-0.105 §3](cjs_00.105_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids) (*Stable Identifiers, Edition Alignment, and Drafting Notes*); the [Fullest Protective Effect](../core_05.045_band_integrative.md#fullest-protective-effect) rule remains [Chapter One §15.4.3 Incorporation Layer](../core_01.005_interaction_interpretation.md#1543-incorporation-layer) (*Incorporation layer*, including the cross-file Fullest Protective Effect rule).

---

**Previous file:** [cjs_00.110_scope_purpose_boundary_interface.md](cjs_00.110_scope_purpose_boundary_interface.md)

**Next file:** [cjs_05.140_odef_parse_mechanics.md](cjs_05.140_odef_parse_mechanics.md)