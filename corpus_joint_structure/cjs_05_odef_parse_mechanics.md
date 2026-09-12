# CJS-1.13–CJS-1.14: oDef parse mechanics

<details>
<summary><strong><span style="color: #2563eb;">Corpus placement (non-operative): file structure and reading rules</span></strong></summary>

> The following content is **reader guidance only**. It does not add, remove, or narrow binding obligations in this file or elsewhere.
>
> This file is **binding incorporated implementation text** where [`corpus_joint_structure.md`](../corpus_joint_structure.md) is incorporated under [Chapter Sixteen](../core_16_incorporation.md). It must satisfy the Sentient Constitution and does not override or narrow it. It holds **CJS-1.13** (*oDef parse mechanics*) and **CJS-1.14**.
>
> Start at the [Joint structure landing page](../corpus_joint_structure.md) or the [joint-structure reader guide](cjs_reader_guide.md). General readers may defer this file until cross-domain **oDef** clusters are in scope.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.3](cjs_01_scope_purpose_boundary_interface.md#cjs-13-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-1.1](cjs_01_scope_purpose_boundary_interface.md#cjs-11-section-identifiers-and-article-references) section identifiers and **Def.*** / **oDef** homes; [Chapter Sixteen](../core_16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline and [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions.
- Downstream: [CJS-1.13](#cjs-113-operational-structure-and-subsection-local-terminology); [CJS-1.14](#cjs-114-operational-clusters).
- Read with: **CJS-1.13**; **CJS-1.14**; **CJS-3**.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Definitions · Assessment · Compliance</span></strong></summary>

- [Constitutional Constraint](../core_05_band_integrative.md#constitutional-constraint) · [O](../core_05_band_integrative.md#constitutional-constraint) · [M](../core_05_band_integrative.md#constitutional-constraint-a) · [A](../core_05_band_integrative.md#constitutional-constraint-a) · [C](../core_05_band_integrative.md#constitutional-constraint-c)

</details>

<br>

This file is the joint-structure implementation home for **CJS-1.13** and **CJS-1.14** (*oDef parse mechanics*).

*In plain terms: these sections say how to read each **oDef** entry and how to treat a cluster of entries as one compound definition.*

A short reader gloss lives in the [joint-structure reader guide](cjs_reader_guide.md#how-to-read-an-odef-entry). The subsections below are the binding parse rules for **oDef** entries in **CJS-3** (*Implementation and cross-implementation operational cluster library*) — the reader-facing guidepost format (**What it is** / **How to measure and assess** / **What must hold**).

## CJS-1.13: Operational structure and subsection-local terminology
<a id="cjs-113-operational-structure-and-subsection-local-terminology"></a>
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.3](cjs_01_scope_purpose_boundary_interface.md#cjs-13-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-0.1](cjs_00_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids) topic router; [Chapter Sixteen](../core_16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline and [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions.
- Read with: **CJS-1.13**; **CJS-1.14**.

</details>

<br>

*In plain terms: How to read each **oDef** entry: **What it is** says what the rule covers, **How to measure and assess** says what evidence to check and how reviewers verify it, and **What must hold** states the binding failure modes.*

**oDef** entries use a local joint operational rule format. Reader-facing headers match the Chapter Five guidepost presentation so the same O/M/A/C scan path works across layers; the entries remain joint-operational rules, not constitutional dictionary entries.

That format uses a titled entry (optionally preceded by an HTML anchor whose `id` is the entry slug), an optional italic `*In plain terms: …*` gloss, then:
- `- **What it is**` — Ontological (O) scope, with mandatory `**In scope:**` and `**Out of scope:**` sub-bullets (optional `**Depends on:**` only when constitutive prerequisites must be separated),
- `- **How to measure and assess**` — Measurement (M) interwoven with Assessment (A), introduced by an HTML anchor whose `id` is the entry slug plus `-a`, with tiered `**Primary measure:**` / `**Primary assessment:**` pairing (and secondary/tertiary tiers only when the entry states them),
- `- **What must hold**` — Compliance (C), introduced by an HTML anchor whose `id` is the entry slug plus `-c`, with `**Primary failure:**` (and secondary/tertiary failure labels when tiers apply).

**Primary measure** on an **oDef** names the auditable control, record, evidence object, or operational check the term turns on. It does not invent Preamble or Chapter Five measurement-family leads unless the entry already points there.

These labels are modeled on **Chapter Two** (*Ontological (O)*, *Measurement (M)*, *Assessment (A)*, *Compliance (C)*) and the Chapter Five guidepost headers. They remain local to this joint-structure implementation layer.

The consequences of that structure are:
- **oDef** guidepost entries are not Independent Definitions and are not Chapter Five **Def.*** entries,
- they do not add constitutional terms,
- they do not satisfy **Chapter Two** or **Chapter Three** definition-integrity rules for defined concepts.

Constitutional terms used under **What it is**, **How to measure and assess**, or **What must hold** take their meanings from **Chapter Five** and the applicable Sentient Constitution `core_*.md` files (see [README.md](../README.md)).

**oDef** text does not redefine those terms.

Subsection-local shorthand applies only inside the subsection where it appears, unless another corpus file defines the phrase and cites that subsection.

## CJS-1.14: Operational clusters
<a id="cjs-114-operational-clusters"></a>
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.3](cjs_01_scope_purpose_boundary_interface.md#cjs-13-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-0.1](cjs_00_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids) topic router; [Chapter Sixteen](../core_16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline and [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions.
- Read with: **CJS-1.14**; **CJS-1.13**.

</details>

<br>

*In plain terms: Where several entries appear together as an **oDef** cluster, the head entry and the ones beneath it form a single compound definition. Reading one component alone will give the wrong answer.*

<strong><span style="color: #2563eb;">Definition:</span></strong> [Constitutional Constraint](../core_05_band_integrative.md#constitutional-constraint) · [O](../core_05_band_integrative.md#constitutional-constraint) · [M](../core_05_band_integrative.md#constitutional-constraint-a) · [A](../core_05_band_integrative.md#constitutional-constraint-a) · [C](../core_05_band_integrative.md#constitutional-constraint-c)

Some subsections are structured as an **oDef** operational cluster (see **CJS-1.1** (*Section identifiers and article references*) for the **oDef.*n*** = **CJS-3.*n*** rule).

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

That **oDef**-cluster rule is local to one **oDef**. Cross-file combined satisfaction when more than one implementation file applies to the same facts lives in [Chapter One §8.4.4](../core_01_b_interaction_interpretation.md#844-combined-satisfaction) (*Combined satisfaction of jointly applicable incorporated obligations*).

By structural analogy, this follows the **joint invocation and satisfaction** rule for **Dependent clusters** in [Chapter Five](../core_05__definitions_home.md#joint-invocation-and-satisfaction).

**oDef** clusters remain local to this implementation layer:
- they are not **Chapter Five** **Def.*** Clustered Definitions,
- they do not add Independent Definitions.

Any read-with cross-reference stated in the head **In scope** (or head Trace) applies to the whole cluster.

---

**Previous file:** [cjs_04_drafting_contracts.md](cjs_04_drafting_contracts.md)

**Next file:** [cjs_02_specific_joint_interlocks.md](cjs_02_specific_joint_interlocks.md)
