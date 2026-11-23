# CJS-3.140: oDef Parse Mechanics

<details>
<summary><strong><span style="color: #2563eb;">Corpus placement (non-operative): file structure and reading rules</span></strong></summary>

> This file is **binding incorporated implementation text** where [`corpus_joint_structure.md`](../corpus_joint_structure.md) is incorporated under [Chapter Thirty-One](../core_31.000_incorporation.md). It must satisfy the Sentient Constitution and does not override or narrow it. It holds **CJS-3.140 §13** (*Operational Structure and Subsection-Local Terminology*) and **CJS-3.140 §14** (*Operational Clusters*).
>
> Start at the [Joint structure landing page](../corpus_joint_structure.md) or the [joint-structure reader guide](cjs_reader_guide.md). General readers may defer this file until cross-domain **oDef** clusters are in scope.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream:
  - [CJS-0.110 §3](cjs_00.110_scope_purpose_boundary_interface.md#cjs-0110-3-shared-implementation-corpus-preamble-contract) (*Shared Implementation-Corpus Preamble Contract*) shared implementation-corpus contract;
  - [CJS-0.110 §1](cjs_00.110_scope_purpose_boundary_interface.md#cjs-0110-1-section-identifiers-and-article-references) (*Section Identifiers and Article References*) section identifiers and **Def.*** / **oDef** homes;
  - [Chapter Thirty-One](../core_31.000_incorporation.md#chapter-thirty-one-incorporation-bridge) (31.000) incorporation discipline and
  - [Chapter Three](../core_03.000_definitions_home.md#chapter-three-foundational-definitions) (3.000) canonical definitions.
- Downstream: [CJS-3.140 §13](#cjs-3140-13-operational-structure-and-subsection-local-terminology) (*Operational Structure and Subsection-Local Terminology*); [CJS-3.140 §14](#cjs-3140-14-operational-clusters) (*Operational Clusters*).
- Read with: **CJS-3.140 §13** (*Operational Structure and Subsection-Local Terminology*); **CJS-3.140 §14** (*Operational Clusters*); **CJS-3.105 (*Operational cluster library (oDef)*) through CJS-3.135 (*Integrative cross-leg operations (oDef.22–oDef.23)*)** (*operational cluster library (oDef)*).

</details>

<details>
<summary><strong><span style="color: #2563eb;">Definitions (O · M · A · C)</span></strong></summary>

- [Constitutional Constraint](../subcore_03.080_band_integrative.md#constitutional-constraint) · [O](../subcore_03.080_band_integrative.md#constitutional-constraint) · [M](../subcore_03.080_band_integrative.md#constitutional-constraint-a) · [A](../subcore_03.080_band_integrative.md#constitutional-constraint-a) · [C](../subcore_03.080_band_integrative.md#constitutional-constraint-c)

</details>

<br>

Core home: 03

This file is the joint-structure implementation home for **CJS-3.140 §13** (*Operational Structure and Subsection-Local Terminology*) and **CJS-3.140 §14** (*Operational Clusters*), together the oDef parse mechanics.

*In plain terms: these sections say how to read each **oDef** entry and how to treat a cluster of entries as one compound definition.*

## Purpose, Role, and Scope

**Purpose:** Make the structure of joint operational definitions understandable and consistent.

**Role:** Section 13 sets the entry format and subsection-local terminology; section 14 sets how an operational cluster is read and applied. These rules cover **oDef** entries in the **CJS-3.105** (*operational cluster library (oDef)*) through **CJS-3.135** (*Integrative cross-leg operations (oDef.22–oDef.23)*) files. A short reader gloss lives in the [joint-structure reader guide](cjs_reader_guide.md#how-to-read-an-odef-entry).

## CJS-3.140 §13: Operational Structure and Subsection-Local Terminology

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream:
  - [CJS-0.110 §3](cjs_00.110_scope_purpose_boundary_interface.md#cjs-0110-3-shared-implementation-corpus-preamble-contract) (*Shared Implementation-Corpus Preamble Contract*) shared implementation-corpus contract;
  - [CJS-0.105 §1](cjs_00.105_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids) (*Cross-File Routing*) topic router;
  - [Chapter Thirty-One](../core_31.000_incorporation.md#chapter-thirty-one-incorporation-bridge) (31.000) incorporation discipline and
  - [Chapter Three](../core_03.000_definitions_home.md#chapter-three-foundational-definitions) (3.000) canonical definitions.
- Read with: **CJS-3.140 §13** (*Operational Structure and Subsection-Local Terminology*); **CJS-3.140 §14** (*Operational Clusters*).

</details>

<br>

*In plain terms: How to read each **oDef** entry: **What it is** says what the rule covers, **How to measure and assess** says what evidence to check and how reviewers verify it, and **What must hold** states the binding failure modes.*

**oDef** entries use a local joint operational rule format. Reader-facing headers match the Chapter Three guidepost presentation so the same O/M/A/C scan path works across layers; the entries remain joint-operational rules, not constitutional dictionary entries.

That format uses a titled entry (optionally preceded by an HTML anchor whose `id` is the entry slug), an optional italic `*In plain terms: …*` gloss, then:

- `- **What it is**` — Ontological (O) scope, with mandatory `**In scope:**` and `**Out of scope:**` sub-bullets (optional `**Depends on:**` only when constitutive prerequisites must be separated),
- `- **How to measure and assess**` — Measurement (M) interwoven with Assessment (A), introduced by an HTML anchor whose `id` is the entry slug plus `-a`, with layered `**Primary measure:**` / `**Primary assessment:**` pairing (and secondary/tertiary layers only when the entry states them),
- `- **What must hold**` — Compliance (C), introduced by an HTML anchor whose `id` is the entry slug plus `-c`, with `**Primary failure:**` (and secondary/tertiary failure labels when layers apply).

**Primary measure** on an **oDef** names the auditable control, record, evidence object, or operational check the term turns on. It does not invent Preamble or Chapter Three measurement-family leads unless the entry already points there.

These labels are modeled on **Subcore 3-A** (*Ontological (O)*, *Measurement (M)*, *Assessment (A)*, *Compliance (C)*) and the Chapter Three guidepost headers. They remain local to this joint-structure implementation layer.

The consequences of that structure are:

- **oDef** guidepost entries are not Independent Definitions and are not Chapter Three **Def.*** entries,
- they do not add constitutional terms,
- they do not satisfy **Subcore 3-A** or **Subcore 3-B** definition-integrity rules for defined concepts.

Constitutional terms used under **What it is**, **How to measure and assess**, or **What must hold** take their meanings from **Chapter Three** and the applicable Sentient Constitution `core_*.md` files (see [README.md](../README.md)).

**oDef** text does not redefine those terms.

Subsection-local shorthand applies only inside the subsection where it appears, unless another corpus file defines the phrase and cites that subsection.

## CJS-3.140 §14: Operational Clusters

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream:
  - [CJS-0.110 §3](cjs_00.110_scope_purpose_boundary_interface.md#cjs-0110-3-shared-implementation-corpus-preamble-contract) (*Shared Implementation-Corpus Preamble Contract*) shared implementation-corpus contract;
  - [CJS-0.105 §1](cjs_00.105_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids) (*Cross-File Routing*) topic router;
  - [Chapter Thirty-One](../core_31.000_incorporation.md#chapter-thirty-one-incorporation-bridge) (31.000) incorporation discipline and
  - [Chapter Three](../core_03.000_definitions_home.md#chapter-three-foundational-definitions) (3.000) canonical definitions.
- Read with: **CJS-3.140 §14** (*Operational Clusters*); **CJS-3.140 §13** (*Operational Structure and Subsection-Local Terminology*).

</details>

<br>

*In plain terms: Where several entries appear together as an **oDef** cluster, the head entry and the ones beneath it form a single compound definition. Reading one component alone will give the wrong answer.*

<strong><span style="color: #2563eb;">Definition:</span></strong> [Constitutional Constraint](../subcore_03.080_band_integrative.md#constitutional-constraint) · [O](../subcore_03.080_band_integrative.md#constitutional-constraint) · [M](../subcore_03.080_band_integrative.md#constitutional-constraint-a) · [A](../subcore_03.080_band_integrative.md#constitutional-constraint-a) · [C](../subcore_03.080_band_integrative.md#constitutional-constraint-c)

Some subsections are structured as an **oDef** operational cluster. For the identifier and definition-home rules, see [CJS-0.110 §1 Section Identifiers and Article References](cjs_00.110_scope_purpose_boundary_interface.md#cjs-0110-1-section-identifiers-and-article-references).

In an **oDef** cluster, the head entry and the component entries in the same subsection work together as one compound operational definition.

Read the structure as follows:

- the head entry is the guidepost block (**What it is** / **How to measure and assess** / **What must hold**) immediately under the titled head line,
- component entries are introduced by a plain title line without **`###`**,
- each component then has its own guidepost block,
- the cluster continues until a **`---` delimiter** or the next **`###`** subsection heading.

Application rules are strict:

- the head and all components must be applied together,
- partial satisfaction is not compliance,
- no component may be used, satisfied, or evaluated on its own in a way that changes the compliance result.

That **oDef**-cluster rule is local to one **oDef**. Cross-file combined satisfaction when more than one implementation file applies to the same facts lives in [Chapter Two §15.4.4](../core_02.030_constitutional_interpretation.md#1544-combined-satisfaction-of-jointly-applicable-incorporated-obligations) (*Combined Satisfaction of Jointly Applicable Incorporated Obligations*).

By structural analogy, this follows the **joint invocation and satisfaction** rule for **Dependent clusters** in [Chapter Three §4.1 Joint Invocation and Satisfaction](../core_03.000_definitions_home.md#41-joint-invocation-and-satisfaction).

**oDef** clusters remain local to this implementation layer:

- they are not **Chapter Three** **Def.*** Clustered Definitions,
- they do not add Independent Definitions.

Any read-with cross-reference stated in the head **In scope** (or head Trace) applies to the whole cluster.

---

**Previous file:** [cjs_31.105_drafting_contracts.md](cjs_31.105_drafting_contracts.md)

**Next file:** [cjs_31.110_specific_joint_interlocks.md](cjs_31.110_specific_joint_interlocks.md)
