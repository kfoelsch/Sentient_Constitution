## CJS-1: Scope, purpose, and boundary interface

**Quick orientation**

This file explains how the joint-structure layer connects the main companion files. Detailed routing rules and legal authorities stay in the relevant subsections and cross-references.

For the canonical owner map, see **CJS-2.2** and `doc_architecture.md` section 4.

The companion layers named here are:
- **CP:** implementation, meaning the **CJS folder** and its *Cross-domain implementation layer*,
- **CS:** `corpus_systems.md`,
- **CI:** `corpus_institutions.md`,
- **CF:** `corpus_forum.md`.

After this orientation, the section sets the ground rules for scope, references, and boundaries before the integration map in **CJS-2** and the joint requirements in **CJS-3**.

### CJS-1.1: Shared companion preamble contract
This subsection gives the shared starting rules for **CP**, **CS**, **CI**, and **CF**.

Companion files should point back here instead of repeating long boilerplate.

The shared contract is:

- Use the canonical meaning of constitutional terms. Do not redefine constitutional terms, Rights Floors, or O/E/C definition mechanics.
- Add only implementation details that belong inside the file's assigned scope.
- When companion files overlap on the same facts, apply **CJS-2** for read order and stricter-wins, and **CJS-3** for joint requirements.
- Keep companion text understandable under **Article XX**.
- Use **CJS-2.2** and `doc_architecture.md` section 4 to find the single home for each topic.
- Treat shorthand inside a subsection as local to that subsection unless a canonical owner later adopts it. If local shorthand conflicts with canonical definitions, the canonical definitions control.

This file does not create a separate authority stack. Use the constitutional **Authority Stack and Internal Hierarchy** in `core_05-05_definitions_c_dependent_clusters.md` **Chapter Five**, section **3.4** (*Corpus, Authority Stack, Supremacy, and Enforceability*), read with `core_15-15_incorporation.md` **Chapter Fifteen** for incorporation, edition custody, and anti-drift rules.

For this CJS file, that means:

- The numbered `core_*` Sentient Constitution files control constitutional meaning.
- Adopted companion implementation text applies only within valid adoption and incorporation scope.
- Companion files may add implementation detail, and may be stricter, but may not weaken Sentient Constitution requirements or Rights Floors.
- Chapters Two through Four control O/E/C definition mechanics. Chapter Five controls constitutional term definitions.
- Chapter Ten controls rights language. Companion files implement Rights Floors and must not restate weaker versions.
- Chapter Six controls canonical compliance, violation, and standing classification policy.
- [corpus_systems.md](../corpus_systems.md) Chapters S1 through S3 control data types, system classes, dependency types, and steward tiers.
- **PRIM8** and **PROT2** stay separate: **PRIM8** belongs to the architecture layer, and **PROT2** belongs to the governance layer.
- **CJS-2** states the default read order, read-with routing, and **stricter-wins** rules among **CP**, **CS**, **CI**, and **CF**.

### CJS-1.2: Section identifiers and article references
Headings use **CJS-1** through **CJS-4**, meaning *Corpus joint structure* section *n*. Subsections use **CJS-*n*.*m***, such as **CJS-2.2**. These are not Sentient Constitution **Article** numbers. The abbreviation **CJS** matches `doc_architecture.md`, where it means the *Corpus joint structure* companion file.

Unless a section says otherwise, **Article** labels with Roman numerals that point to the Sentient Constitution Chapter Ten part files (`core_10-10_rights_part_*.md`) refer to the canonical `### Article ...` headings in those files.

### CJS-1.3: Joint structural boundary and owner discipline
The CJS folder is the **operative home** for **joint** structural expectations. These are rules and integration interfaces that apply when **two or more** of CP, CS, CI, and CF must be satisfied **together**. The goal is for institutions, forums, and classified systems to read as **one coherent implementation stack** when they materially interact.

The CJS folder is **not** the primary owner for:
- system-class and steward taxonomies, which belong to **CS**,
- general institutional lifecycle and fiscal architecture, which belong to **CI**,
- forum-family operational doctrine, which belongs to **CF**.

Stable implementation-label text lives in the CJS implementation-group files under the **Cross-domain implementation layer**.

Under the authority-stack rules named in **CJS-1.1**, the CJS folder sits in the **binding incorporated implementation** band. It must **implement, not narrow**, Sentient Constitution meaning.

### CJS-1.4: Operational structure and subsection-local terminology
Some subsections use a local joint operational rule format. Its list shape mirrors the format used in `corpus_institutions.md`.

That format uses a titled entry followed by:
- **`- OP-O:`** for what is in scope,
- **`- OP-E:`** for how satisfaction is assessed or evidenced,
- **`- OP-C:`** for binding operational requirements and non-compliance hooks.

These labels are modeled on **Chapter Two**, section **2** (*Ontological (O)*, *Evaluative (E)*, *Compliance (C)*). They remain local to this companion joint-structure file.

The consequences of that structure are:
- **OP-** lines are not Independent Definitions,
- they do not add constitutional terms,
- they do not satisfy **Chapter Two** or **Chapter Three** definition-integrity rules for defined concepts.

Constitutional terms used in **OP-O**, **OP-E**, or **OP-C** take their meanings from the Sentient Constitution `core_*.md` files (see [README.md](../README.md)) and from `core_05-05_definitions_a_independent.md`.

**OP-** text does not redefine those terms.

Subsection-local shorthand applies only inside the subsection where it appears, unless another corpus file defines the phrase and cites that subsection.

### CJS-1.5: Operational clusters
Some subsections are structured as an operational cluster.

In an operational cluster, the head entry and the component entries in the same subsection work together as one compound operational definition.

Read the structure as follows:
- the head entry is the **`- OP-O:`** / **`- OP-E:`** / **`- OP-C:`** block immediately under the titled head line,
- component entries are introduced by a plain title line without **`###`**,
- each component then has its own **`- OP-O:`**, **`- OP-E:`**, and **`- OP-C:`** lines,
- the cluster continues until a **`---` delimiter** or the next **`###`** subsection heading.

Application rules are strict:
- the head and all components must be applied together,
- partial satisfaction is not compliance,
- no component may be used, satisfied, or evaluated on its own in a way that changes the compliance result.

By structural analogy, this follows the **joint invocation and satisfaction** rule for **Dependent clusters** in `core_05-05_definitions_c_dependent_clusters.md` **Chapter Five**, **section 3** (*Dependent clusters*).

Operational clusters remain local to this companion layer:
- they are not **Chapter Five** Clustered Definitions,
- they do not add Independent Definitions.

Any read-with cross-reference stated in the head **OP-O** applies to the whole cluster.

---

**Next file:** [cjs_02_companion_integration_map.md](cjs_02_companion_integration_map.md)
