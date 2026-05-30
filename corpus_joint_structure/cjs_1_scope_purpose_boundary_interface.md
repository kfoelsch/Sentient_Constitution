## CJS-1: Scope, purpose, and boundary interface

**Constitutional index (abridged)**
- Topic-level routing and cited authorities remain in subsection text and cross-references.
- Canonical owner map: `corpus_joint_structure.md` **CJS-2.2** and `doc_architecture.md` section 4.

**Companion layers in joint-structure routing:** **CP** — implementation (`corpus_joint_structure.md`, *Cross-domain implementation layer*); **CS** — `corpus_systems.md`; **CI** — `corpus_institutions.md`; **CC** — `corpus_forum.md`.

This section establishes scope and reference conventions for joint structural rules before the integration map and joint requirements in **CJS-2** and **CJS-3**.

### CJS-1.1: Shared companion preamble contract
This subsection is the shared preamble contract for **CP**, **CS**, **CI**, and **CC**.

Companion files should keep this contract concise by pointer and avoid repeating long boilerplate blocks.

The shared contract is:

- Inherit canonical meaning and do not redefine constitutional terms, Rights Floors, or O/E/C definition mechanics.
- Add only domain-specific implementation detail within each file's assigned scope.
- For cross-companion overlap on the same facts, apply **CJS-2** (read order and stricter-wins) and **CJS-3** (joint requirements).
- Keep companion text usable under **Article XX** comprehensibility expectations.
- Use **CJS-2.2** and `doc_architecture.md` section 4 for single-home owner routing.
- Treat subsection-local shorthand as local unless a canonical owner later adopts it expressly; if shorthand conflicts with canonical definitions, canonical definitions govern.
- Use the shared interpretation baseline at `implementation/INTERPRETATION_BASELINE_SHARED_2026-04-09.md`.

### CJS-1.2: Section identifiers and article references
Headings use **CJS-1** through **CJS-4** (*Corpus joint structure* section *n*). Subsections use **CJS-*n*.*m*** (for example **CJS-2.2**). They are not Sentient Constitution **Article** numbers. The abbreviation **CJS** matches `doc_architecture.md` (*Corpus joint structure* companion file).

Unless another reference pattern is stated, **Article** labels with Roman numerals in cross-references to the Sentient Constitution Chapter Ten part files (`core_10-10_rights_part_*.md`) denote those articles per their canonical `### Article …` headings, per companion conventions.

### CJS-1.3: Joint structural boundary and owner discipline
This file is the **operative home** for **joint** structural expectations: rules and integration interfaces that apply when **two or more** of CP, CS, CI, and CC must be satisfied **together**, so institutions, forums, and classified systems read as **one coherent implementation stack** where they materially interact.

It is **not** the primary owner for system-class and steward taxonomies (**CS**), general institutional lifecycle and fiscal architecture (**CI**), or forum-family operational doctrine (**CC**). Stable implementation-label text is hosted in this file under **Cross-domain implementation layer**.

Read **Authority Stack and Internal Hierarchy** in `core_05-05_definitions_a_independent.md` **Chapter Five** with **Sentient Constitution Chapter Fifteen** in `core_15-15_incorporation.md`. This file sits in the **binding incorporated implementation** band; it must **implement, not narrow**, Sentient Constitution meaning.

### CJS-1.4: Operational structure and subsection-local terminology
Some subsections use a corpus-local joint operational rule format that mirrors the list shape used in `corpus_institutions.md`.

That format uses a titled entry followed by:
- **`- OP-O:`** for what is in scope,
- **`- OP-E:`** for how satisfaction is assessed or evidenced,
- **`- OP-C:`** for binding operational requirements and non-compliance hooks.

These labels align by analogy with **Chapter Two**, section **2** (*Ontological (O)*, *Evaluative (E)*, *Compliance (C)*) but remain local to this companion joint-structure file.

The consequences of that structure are:
- **OP-** lines are not Independent Definitions,
- they do not add constitutional terms,
- they do not satisfy **Chapter Two** or **Chapter Three** definition-integrity rules for defined concepts.

Constitutional terms used in **OP-O**, **OP-E**, or **OP-C** take their meanings from the Sentient Constitution `core_*.md` files (see [README.md](../README.md)) and `core_05-05_definitions_a_independent.md`.

**OP-** text does not redefine those terms.

Subsection-local shorthand applies only within the hosting subsection unless another corpus file defines the phrase and cites that subsection.

### CJS-1.5: Operational clusters
Some subsections are structured as an operational cluster.

In an operational cluster, the head entry and the component entries in the same subsection together form one compound operational definition.

Read the structure as follows:
- the head entry is the **`- OP-O:`** / **`- OP-E:`** / **`- OP-C:`** block immediately under the titled head line,
- component entries are introduced by a plain title line without **`###`**,
- each component then has its own **`- OP-O:`**, **`- OP-E:`**, and **`- OP-C:`** lines,
- the cluster continues until a **`---` delimiter** or the next **`###`** subsection heading.

Application rules are strict:
- the head and all components must be applied together,
- partial satisfaction is not compliance,
- a component must not be used, satisfied, or evaluated on its own in a way that changes the compliance result.

This follows the **joint invocation and satisfaction** rule for **Dependent clusters** in `core_05-05_definitions_c_dependent_clusters.md` **Chapter Five**, **section 3** (*Dependent clusters*), by structural analogy.

Operational clusters remain local to this companion file:
- they are not **Chapter Five** Clustered Definitions,
- they do not add Independent Definitions.

Any read-with cross-reference stated in the head **OP-O** remains operative for the whole cluster.

---

