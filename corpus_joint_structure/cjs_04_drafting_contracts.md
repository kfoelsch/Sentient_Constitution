# CJS-1.7–CJS-1.8.1: Drafting contracts and owner-to-CJS seam

<details>
<summary><strong><span style="color: #2563eb;">Corpus placement (non-operative): file structure and reading rules</span></strong></summary>

> The following content is **reader guidance only**. It does not add, remove, or narrow binding obligations in this file or elsewhere.
>
> This file is **binding incorporated implementation text** where [`corpus_joint_structure.md`](../corpus_joint_structure.md) is incorporated under [Chapter Sixteen](../core_16-16_incorporation.md). It must satisfy the Sentient Constitution and does not override or narrow it. It holds **CJS-1.7**, **CJS-1.8**, and **CJS-1.8.1** (*drafting contracts and the primary-owner-to-CJS seam*).
>
> Start at the [Joint structure landing page](../corpus_joint_structure.md) or the [joint-structure reader guide](cjs_reader_guide.md). Most readers reach this file from a citation rather than reading the folder front to back.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.3](cjs_01_scope_purpose_boundary_interface.md#cjs-13-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-0.1](cjs_00_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids) topic router; [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline and [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions.
- Downstream: [CJS-1.7](#cjs-17-intentional-overlap-non-duplication-discipline); [CJS-1.8](#cjs-18-two-tier-definition-contract-binding-abstraction--owner-detail); [CJS-1.8.1](#cjs-181-implementation-boundary-primary-owner-to-cjs-seam).
- Read with: [CJS-1.3](cjs_01_scope_purpose_boundary_interface.md#cjs-13-shared-implementation-corpus-preamble-contract); [CJS-0.1](cjs_00_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids); [Chapter One §8.4.3](../core_01_b_interaction_interpretation.md#843-incorporation-layer) (*stricter-wins*).

</details>

<br>

This file is the joint-structure implementation home for **CJS-1.7**, **CJS-1.8**, and **CJS-1.8.1** (*drafting contracts and the primary-owner-to-CJS seam*).

*In plain terms: these sections are for editors and auditors. They say how to split a topic across files without writing two competing rulebooks, and how to keep **CJS** as a connector rather than a second owner.*

Average readers can skip this file unless a citation sends them here. How to enter the layer: [joint-structure reader guide](cjs_reader_guide.md).

## CJS-1.7: Intentional overlap (non-duplication discipline)

<a id="cjs-17-intentional-overlap-non-duplication-discipline"></a>
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Read with: **CJS-1.7**; [CJS-0.1](cjs_00_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids).

</details>

<br>

Some topics are **deliberately** split across implementation files — for example contest-integrity design, delegated subunits, or forensic and technical-forum interfaces. For those rows:

- the **primary owner** states the **full operative** rules for the scope that row assigns to it;
- **CJS** text for the same topic adds **joint satisfaction conditions**, **read-with pointers**, and **interface requirements** only when **CJS** is not the **primary owner** for that row;
- do **not** restate **oDef** / **CJS-3** (*Implementation and cross-implementation operational cluster library*) clusters, **CS-2/CS-3** tables, or **CF-** / **CI-** checklists except in brief **quote** or **summary pointer** form when needed for coherence.

Domain-layer overlap discipline: apply [Institutions overlap discipline](../corpus_institutions/ci_00_registry_and_reading_rules.md#institutions-overlap-discipline), [Forums overlap discipline](../corpus_forum/cf_00_registry_and_reading_rules.md#forums-overlap-discipline), and [Systems overlap discipline](../corpus_systems/cs_00_registry_and_reading_rules.md#systems-overlap-discipline) in the respective registry annexes.

## CJS-1.8: Two-tier definition contract (binding abstraction + owner detail)

<a id="cjs-18-two-tier-definition-contract-binding-abstraction--owner-detail"></a>
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Read with: **CJS-1.8**; [CJS-0.1](cjs_00_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids); **CJS-1.7**; **CJS-1.8.1**; [Chapter One §8.4.3](../core_01_b_interaction_interpretation.md#843-incorporation-layer) (*stricter-wins*).
- Downstream: [CJS-1.8.1 Implementation boundary (primary owner to CJS seam)](#cjs-181-implementation-boundary-primary-owner-to-cjs-seam).

</details>

<br>

The CJS folder may adopt **binding high-level joint abstractions** only where a term or construct is materially cross-implementation and cannot be safely interpreted through a single owner file alone.

For this contract:

- **Tier 1 (CJS abstraction):** state only shared admission scope, cross-implementation trigger conditions, and minimum joint consequences needed to avoid contradiction or silent gaps.
- **Tier 2 (owner detail):** retain all operational tests, thresholds, procedures, and implementation mechanics in the **primary owner** section(s) named in **CJS-0.1** (*Cross-implementation read-with contract*).
- **No parallel canon:** CJS abstractions must not become a second full taxonomy for domains owned by **CJS**, **CS**, **CI**, or **CF**.
- **Specialize, do not redefine:** owner files may specialize a CJS abstraction for their domain scope but must not redefine it incompatibly.

When CJS text seems to conflict with a **primary owner** section, apply **CJS-1.7** (*Intentional overlap (non-duplication discipline)*) and **CJS-1.8.1** (*Implementation boundary (primary owner to CJS seam)*): if the CJS text only helps readers connect files, trigger a joint rule, or use shorthand inside one subsection, it does not replace the owner's meaning.

When that boundary does not resolve the conflict, use this order:

1. The Sentient Constitution and core definitions, including **Chapter Sixteen**.
2. The canonical owner meaning in **CJS**, **CS**, **CI**, or **CF**, as routed by **CJS-0.1** (*Topic router (stable IDs)*) and the [Preamble — constitutional owner register](../core_00_preamble.md#4-principles-definitions-and-rights).
3. The **Tier 1** CJS abstraction stated in this section.
4. Local shorthand, examples, summaries, or other drafting convenience text, as described in **CJS-1.3** (*Shared implementation-corpus preamble contract*).

Do not use a broad reading of CJS to change, shrink, expand, or move a rule that belongs to a canonical owner. If the conflict is still unclear after applying this order, do not treat the broader CJS reading as controlling. Send the question to the canonical owner named in **CJS-0.1**, including the forum owner in **CF** where forum routing, forum authority, or Chapter Eleven procedure is affected, and update the CJS pointer once the owner clarifies it. For stricter-wins between two adopted implementation standards on the same risk, read [Chapter One §8.4.3](../core_01_b_interaction_interpretation.md#843-incorporation-layer) (*Incorporation layer*, including cross-file stricter-wins).

Domain-layer read-with contracts: apply [Institutions read-with pointers](../corpus_institutions/ci_00_registry_and_reading_rules.md#institutions-read-with-pointers), [Forums read-with pointers](../corpus_forum/cf_00_registry_and_reading_rules.md#forums-read-with-pointers), and [Systems read-with pointers](../corpus_systems/cs_00_registry_and_reading_rules.md#systems-read-with-pointers) in the respective registry annexes.

### CJS-1.8.1 Implementation boundary (primary owner to CJS seam)
<a id="cjs-181-implementation-boundary-primary-owner-to-cjs-seam"></a>
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.8](#cjs-18-two-tier-definition-contract-binding-abstraction--owner-detail); [CJS-1.1](cjs_01_scope_purpose_boundary_interface.md#cjs-11-section-identifiers-and-article-references); [CJS-1.7](#cjs-17-intentional-overlap-non-duplication-discipline); [Chapter One §8.4.4](../core_01_b_interaction_interpretation.md#844-combined-satisfaction).
- Read with: **CJS-1.8.1**; **CJS-1.1**; **CJS-1.7**; **CJS-1.8**; **CJS-0.3**; [Chapter One §8.4.4](../core_01_b_interaction_interpretation.md#844-combined-satisfaction); [Chapter One §8.4.3](../core_01_b_interaction_interpretation.md#843-incorporation-layer) (*stricter-wins*).

</details>

<br>

*In plain terms: **CJS** connects files — it does not swallow them. When editors revise joint-structure text, keep the full rule in the **primary owner** file (**CS**, **CI**, or **CF**), keep **CJS** pointers short, and keep **CJS-3** cluster citations traceable under **CJS-0.3**.*

Under the identifier and definition-home rules in **CJS-1.1** (*Section identifiers and article references*), the **CJS-3** (*Implementation and cross-implementation operational cluster library*) files remain the operative home for **oDef** clusters (**oDef.*n*** = **CJS-3.*n***).

When revising **CJS** joint-structure text:
- keep **CS**, **CI**, or **CF** **primary owner** requirements in those files;
- keep read-with restatements short; and
- preserve **oDef** / **CJS-3** (*operational cluster library*) citations so references remain traceable under [CJS-0.3](cjs_00_registry_and_reading_rules.md#cjs-03-stable-identifiers-edition-alignment-and-drafting-notes) (*Stable identifiers, edition alignment, and drafting notes*); stricter-wins remains [Chapter One §8.4.3](../core_01_b_interaction_interpretation.md#843-incorporation-layer) (*Incorporation layer*, including cross-file stricter-wins).

---

**Previous file:** [cjs_01_scope_purpose_boundary_interface.md](cjs_01_scope_purpose_boundary_interface.md)

**Next file:** [cjs_05_odef_parse_mechanics.md](cjs_05_odef_parse_mechanics.md)
