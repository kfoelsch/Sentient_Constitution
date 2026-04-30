# Constitutional joint structure

**Corpus edition:** `SC-Corpus-2026.04.32`  
**Effective date:** 2026-04-24  
*(Edition alignment: same labels as the Sentient Constitution numbered `core_*.md` files (see [README.md](README.md)), `core_05-05_definitions_a_independent.md`, `corpus_systems.md`, `corpus_institutions.md`, and `corpus_forum.md`.)*

This file is intentionally written in plain language with low jargon to improve accessibility, audit readability, and practical adoption testing.

**Non-core Corpus Document**

This file is part of the constitutional corpus as **binding incorporated implementation text** where **Corpus** designates it, incorporated through **Sentient Constitution Chapter Fourteen**.

Canonical meaning for constitutional terms, rights floors, and definition-satisfaction rules remains in the Sentient Constitution and canonical owners in `doc_architecture.md`; nothing here transfers that authority.

**File-specific implementation anchors**

- **Scope boundary:** this file defines cross-companion structural and integration obligations and hosts the **Cross-domain implementation layer**. It does not replace domain-operational rules owned solely by `corpus_systems.md`, `corpus_institutions.md`, or `corpus_forum.md` outside the joint interface.
- **Joint-read rule:** where companions interact on the same facts, apply **CJS-2** (read order and stricter-wins) and **CJS-3** (joint requirements).
- **Single-home owner routing:** use `doc_architecture.md` section 4 and `corpus_joint_structure.md` **CJS-2.2** for canonical owner assignment across core and companion files.
- **Local shorthand rule:** subsection-local shorthand is local unless another canonical owner adopts it expressly; if local wording conflicts with canonical definitions, canonical definitions govern.
- **Readability and baseline:** keep this text usable under **Article XX** comprehensibility expectations and apply the shared interpretation baseline at [implementation/INTERPRETATION_BASELINE_SHARED_2026-04-09.md](implementation/INTERPRETATION_BASELINE_SHARED_2026-04-09.md).

**Implementation cross-reference index (routing only):** Joint-structure obligations interoperate with **Cross-domain implementation layer** implementation labels **PRIM8**, **PRIM9**, **PRIM10**, **PRIM15**, **PROT1**, **PROT2**, **PROT3**, **PROT4**, **PROT5**, and **PROT6** where materially applicable. This index is routing guidance only and does not redefine owner-layer meaning.

---

## JOINT STRUCTURE REGISTRY (stable section families)

- **CJS-1** — Scope, purpose, and boundary interface
- **CJS-2** — Companion integration map (owners, intentional overlap, read-with ordering)
- **CJS-3** — Joint structural obligations (cross-domain requirements)
- **CJS-4** — Stable section identifiers, edition alignment, and drafting notes

---

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

- Inherit canonical meaning and do not redefine constitutional terms, rights floors, or O/E/C definition mechanics.
- Add only domain-specific implementation detail within each file's assigned scope.
- For cross-companion overlap on the same facts, apply **CJS-2** (read order and stricter-wins) and **CJS-3** (joint requirements).
- Keep companion text usable under **Article XX** comprehensibility expectations.
- Use **CJS-2.2** and `doc_architecture.md` section 4 for single-home owner routing.
- Treat subsection-local shorthand as local unless a canonical owner later adopts it expressly; if shorthand conflicts with canonical definitions, canonical definitions govern.
- Use the shared interpretation baseline at `implementation/INTERPRETATION_BASELINE_SHARED_2026-04-09.md`.

### CJS-1.2: Section identifiers and article references
Headings use **CJS-1** through **CJS-4** (*Corpus joint structure* section *n*). Subsections use **CJS-*n*.*m*** (for example **CJS-2.2**). They are not Sentient Constitution **Article** numbers. The abbreviation **CJS** matches `doc_architecture.md` (*Corpus joint structure* companion file).

Unless another reference pattern is stated, **Article** labels with Roman numerals in cross-references to the Sentient Constitution Chapter Nine part files (`core_09-09_rights_part_*.md`) denote those articles per their canonical `### Article …` headings, per companion conventions.

### CJS-1.3: Joint structural boundary and owner discipline
This file is the **operative home** for **joint** structural expectations: rules and integration interfaces that apply when **two or more** of CP, CS, CI, and CC must be satisfied **together**, so institutions, forums, and classified systems read as **one coherent implementation stack** where they materially interact.

It is **not** the primary owner for system-class and steward taxonomies (**CS**), general institutional lifecycle and fiscal architecture (**CI**), or forum-family operational doctrine (**CC**). Stable implementation-label text is hosted in this file under **Cross-domain implementation layer**.

Read **Authority Stack and Internal Hierarchy** in `core_05-05_definitions_a_independent.md` **Chapter Five** with **Sentient Constitution Chapter Fourteen** in `core_14-14_incorporation.md`. This file sits in the **binding incorporated implementation** band; it must **implement, not narrow**, Sentient Constitution meaning.

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

Constitutional terms used in **OP-O**, **OP-E**, or **OP-C** take their meanings from the Sentient Constitution `core_*.md` files (see [README.md](README.md)) and `core_05-05_definitions_a_independent.md`.

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

## CJS-2: Companion integration map (owners, intentional overlap, read-with ordering)

**Constitutional index (abridged)**
- Topic-level routing and cited authorities remain in subsection text and cross-references.
- Canonical owner map: `corpus_joint_structure.md` **CJS-2.2** and `doc_architecture.md` section 4.

This section is the **integration spine** for the four companion layers: **who owns** cross-cutting topics at the first level of detail, and which files must be read **with** them.

**Default read order for joint topics** (when material to compliance):

1. **`corpus_joint_structure.md` (this file)** — **Cross-domain implementation layer** and **joint** requirements (**CJS-2**, **CJS-3**) with explicit **read-with** ordering where **two or more** companions would otherwise admit **inconsistent structural treatment**.
2. **`corpus_systems.md`** — **Chapter S1**, **Chapter S2**, and **Chapter S3** taxonomies and designated protocols where system class, stewardship, or lifecycle fixes the **scale** of obligations.
3. **`corpus_institutions.md`** — institutional governance, assurance lanes, escalation, non-court architecture.
4. **`corpus_forum.md`** — forum-operational doctrine for **Chapter Eight** forum families.

**Stricter-wins:** Where companions differ in stringency for the same materially relevant risk, the **stricter clearly adopted** rule governs (**Sentient Constitution Chapter Fourteen**; opening of **`corpus_systems.md`** on classification and material-impact profile). The same principle applies in **CJS-3.6** where profiles and implementation labels appear to conflict.

### CJS-2.1: Intentional overlap (non-duplication discipline)
Some topics are **deliberately** split across companions (for example contest-integrity design, delegated subunits, forensic or technical-court interfaces). For those:

- the **domain owner** states the **full operative** rules for its scope;
- **this file** states **joint satisfaction conditions**, **read-with pointers**, and **interface requirements** only;
- do **not** restate **PRIM/PROT** text, **Chapter S2** / **Chapter S3** tables, or **CC-** / **CI-** checklists except in brief **quote** or **summary pointer** form when needed for coherence.

### CJS-2.3: Two-tier definition contract (binding abstraction + owner detail)
This file may adopt **binding high-level joint abstractions** only where a term or construct is materially cross-companion and cannot be safely interpreted through a single owner file alone.

For this contract:

- **Tier 1 (CJS abstraction):** state only shared admission scope, cross-companion trigger conditions, and minimum joint consequences needed to avoid contradiction or silent gaps.
- **Tier 2 (owner detail):** retain all operational tests, thresholds, procedures, and implementation mechanics in the canonical owner file(s) listed in **CJS-2.2**.
- **No parallel canon:** CJS abstractions must not become a second full taxonomy for domains owned by **CP**, **CS**, **CI**, or **CC**.
- **Specialize, do not redefine:** owner files may specialize a CJS abstraction for their domain scope but must not redefine it incompatibly.

### CJS-2.2: Topic router (stable IDs)
Each row names the **first** operative owner for the topic. **Mandatory read-with** lists companion sections (and core hooks where listed) that must be satisfied **together** when the topic materially applies. Stable row IDs (**CJS-R01**–**CJS-R19**) are **corpus-local** here; they are **not** Sentient Constitution article numbers.

| Row ID | Topic | Primary owner | Mandatory read-with |
|--------|--------|---------------|---------------------|
| **CJS-R01** | Delegated binding bodies and hybrid composition (non-court institutions) | `corpus_institutions.md` **CI-9.1B** | **`corpus_joint_structure.md` CJS-3.7**, **CJS-3.12**; `corpus_systems.md` **Chapter S2**, **Chapter S3**; `corpus_institutions.md` **CI-2**; `corpus_joint_structure.md` **PROT1**, **PROT4** (as cited in owner text) |
| **CJS-R02** | Court chambers, divisions, and designated panels (Chapter Eight families) | `corpus_forum.md` **CC-2.5**–**CC-2.5.5** | **`corpus_joint_structure.md` CJS-3.7**, **CJS-3.12**; `corpus_institutions.md` **CI-9.1B**; `corpus_systems.md` **Chapter S2**, **Chapter S3**; `core_08-08_forum.md` **Chapter Eight** |
| **CJS-R03** | Lawful panel formation, disclosure, recusal, substitution, inability-to-form | `corpus_forum.md` **CC-3** | **`corpus_joint_structure.md` CJS-3.12**; `corpus_institutions.md` **CI-4**, **CI-5**; `core_08-08_forum.md` **Chapter Eight**; `corpus_joint_structure.md` **PROT6** (Implementation Group Four) |
| **CJS-R04** | Routing, intake, transfer, certification, representative treatment | `corpus_forum.md` **CC-4** | **`corpus_joint_structure.md` CJS-3.12**; `core_08-08_forum.md` **Chapter Eight**; `corpus_institutions.md` **CI-8** |
| **CJS-R05** | Appeal, secondary review, exhaustion | `corpus_forum.md` **CC-5** | `corpus_institutions.md` **CI-6**; `corpus_joint_structure.md` Implementation Group Four (including **PROT6**) |
| **CJS-R06** | Court integrity operations, anti-capture, anti-self-judging support | `corpus_forum.md` **CC-6** | `corpus_institutions.md` **CI-5**, **CI-7.3**; `core_08-08_forum.md` **Chapter Eight** |
| **CJS-R07** | Court forensic and analytical support | `corpus_forum.md` **CC-7** | `corpus_institutions.md` **CI-7A**, **CI-7.3** |
| **CJS-R08** | Independent investigative service and prosecution interface | `corpus_forum.md` **CC-8** | `corpus_institutions.md` **CI-7A.1**, **CI-8** |
| **CJS-R09** | Technical courts and specialist chambers | `corpus_forum.md` **CC-9** | `corpus_institutions.md` **CI-7B**, **CI-15B**; `core_08-08_forum.md` **Chapter Eight** |
| **CJS-R10** | Court performance, backlog requirements, publication timeliness, accessibility | `corpus_forum.md` **CC-10** | `corpus_institutions.md` **CI-7.3**; Sentient Constitution **Article XV** themes in `core_09-09_rights_part_*.md` **Chapter Nine** |
| **CJS-R11** | Court continuity, fallback operation, emergency adjudication | `corpus_forum.md` **CC-11** | `corpus_systems.md` **Protocol A**; `corpus_institutions.md` **CI-14** (where transition or continuity interfaces apply); `core_08-08_forum.md` **Chapter Eight** |
| **CJS-R12** | Standard court records, forms, and evidence artifacts | `corpus_forum.md` **CC-12** | `corpus_institutions.md` **CI-6**; `core_02-04_definition_mechanics.md` **Chapters Two through Four** (traceability and verification discipline) |
| **CJS-R13** | Court staffing, shared administration, structural review, structural records | `corpus_forum.md` **CC-13** | `corpus_institutions.md` **CI-4**, **CI-5**; **CI-9.1B** where delegated court subunits apply |
| **CJS-R14** | Institutional functional lanes and non-delegable splits | `corpus_institutions.md` **CI-2** | `corpus_joint_structure.md` **PROT1**; `corpus_systems.md` **Chapter S3** where CSS stewardship intersects |
| **CJS-R15** | Contest-integrity monitoring (pathway integrity, not merits) | `corpus_institutions.md` **CI-7.3** | `corpus_systems.md` **Chapter S2**, **Chapter S3** (including steward contest-integrity paragraphs where applicable); `corpus_joint_structure.md` **PROT6**; **CJS-R03**, **CJS-R10** where court performance data feeds monitors |
| **CJS-R16** | Cross-institution coordination, deadlock, and escalation | `corpus_institutions.md` **CI-8** | `corpus_forum.md` **CC-4**, **CC-6**; `core_08-08_forum.md` **Chapter Eight** (including backup and cross-court integrity routing) |
| **CJS-R17** | Cross-companion trust integrity (joint operation model) | `corpus_joint_structure.md` Implementation Group One (*Meta-integrity obligation: Trust and Trustworthiness*) | **`corpus_joint_structure.md` CJS-3.9**; `core_05-05_definitions_c_dependent_clusters.md` **Chapter Five, section 3.38** (*Trust*, *Trustworthiness*, *Trust Degradation and Misleading Reliance*); `corpus_systems.md` **Chapter S2**, **Chapter S3** where classification or dependency scales assurance burden; `corpus_institutions.md` **CI-7.3**, **CI-8** and `corpus_forum.md` **CC-10** where pathway integrity, publication cadence, or accessibility materially conditions justified trust |
| **CJS-R18** | Class-scaled lane staffing and competency redundancy for materially binding stewardship | `corpus_institutions.md` **CI-2**, **CI-4**, **CI-11**, **CI-12** | **`corpus_joint_structure.md` CJS-3.11**; `corpus_systems.md` **Chapter S2**, **Chapter S3**; `core_10-10_governance.md` **Chapter Ten**, section **5** |
| **CJS-R19** | Cross-companion integrity assurance and resilience operations | `corpus_joint_structure.md` **CJS-3.13** | `corpus_joint_structure.md` **PRIM9** through **PRIM15**; `core_05-05_definitions_a_independent.md` **Chapter Five** (*Auditability*, *Verifiability*, *Verification Accessibility*, *Reversibility*, *Dependency*, *Cascading Failure*, *Adversarial, Scaled, and Exploited Conditions*, *Trustworthiness*); `corpus_systems.md` **Chapter S1**, **Chapter S2**, **Chapter S3** where classification, data handling, or stewardship scales burden; `corpus_institutions.md` **CI-7.3**, **CI-8** and `corpus_forum.md` **CC-10** where monitoring, escalation, publication, or review pathways are materially required |

Rows are **indicative**, not exhaustive: if a matter triggers multiple rows, apply **all** triggered rows whose scope is materially true.

---

## CJS-3: Joint structural obligations (cross-domain requirements)

**Constitutional index (abridged)**
- Topic-level routing and cited authorities remain in subsection text and cross-references.
- Canonical owner map: `corpus_joint_structure.md` **CJS-2.2** and `doc_architecture.md` section 4.

These obligations apply **in addition to** domain-owner text in **CP**, **CS**, **CI**, and **CC**. They address **interlock failures**: each companion fragment looks satisfied in isolation, but the **combined effect** still undermines contestability, independence, traceability, or classification-scaled proportionality.

### CJS-3.1 When joint obligations apply
**Joint obligations** apply where **CJS-2.2** assigns a **mandatory read-with** chain for a materially applicable topic, or where adopting instruments expressly incorporate **`corpus_joint_structure.md`**.

### CJS-3.2 No false partial compliance across companions
Where **two or more** companions in a **CJS-2.2** read-with chain impose **structural** duties on the **same facts** (same institution, court family, classified system, or stewardship chain), it is **non-compliant** to claim compliance by satisfying **only one** companion while a **material** obligation in another listed companion stays **unmet** for that same structural outcome.

Permitted **narrower interim** scopes (for example published emergency scopes) must be **explicitly bounded**, **time-limited**, **reversible**, and **traceable** to Sentient Constitution and annex emergency hooks. Silent or indefinite “temporary” narrowing is **non-compliant**.

### CJS-3.3 Merits boundary for integrity, monitoring, and support roles
**Contest-integrity monitoring**, **pathway performance monitoring**, **non-merits forensic support**, and **investigative support** must stay structurally distinct from **binding merits adjudication** under **Chapter Eight**, unless a **separate** lawful instrument explicitly authorizes limited merits participation for a named role.

Institutions must **publish mandates** stating exclusions from merits decisions, reporting lines, cadence, and interfaces to assurance lanes. **Role merging** that lets oversight or support silently replace an assigned court family’s merits function is **non-compliant**. (Operative detail: **CI-7.3**, **CC-7**, **CC-8**, **`corpus_joint_structure.md`** **PROT6**.)

### CJS-3.4 Institution-hosted or court-adjacent operations
Where an institution **hosts**, **budgets**, **administers**, or **technically operates** court infrastructure, clerking, digital records, security, or personnel systems, its **CI-*** design must make **CC-*** independence and contestability **feasible in practice**, not only on paper, across **budget**, **HR**, **records**, **security**, and **procurement** lanes.

### CJS-3.5 Classification alignment for supervised scope
Where **`corpus_systems.md`** **Chapter S2** or **Chapter S3** materially governs the same systems an institution supervises, published institutional maps (**CI-9.1A** and related **CI-9** material) must stay **consistent** with the **operative** systems-annex classification profile, including **reclassification triggers**. **Silent divergence** between institution-facing labels and systems-annex treatment is **non-compliant** where either layer assigns **material duties** from classification.

### CJS-3.6 Implementation-label traceability and stricter-wins discipline
Where **CS** protocols or **CI**/**CC** procedures **cite** **PRIM/PROT** hooks as their authority basis, adopters must preserve **traceability** to those codes and must **not** use companion text to **weaken** the cited implementation label. Where a cited profile and a cited implementation label appear to conflict, use **Sentient Constitution Chapter Fourteen** conflict order and the **stricter clearly adopted** requirement (**CJS-2**, stricter-wins).

### CJS-3.7 Mandatory hybrid authority composition (delegated binding bodies)
This obligation applies where **CJS-R01** or **CJS-R02** materially applies: **delegated subunits** with materially binding authority under **`corpus_institutions.md` CI-9.1B**, and **court chambers, divisions, or designated panels** under **`corpus_forum.md` CC-2.5** through **CC-2.5.4**. **`corpus_institutions.md`** and **`corpus_forum.md`** retain **identification**, **competence**, **class and court-floor scaling**, **rotating attachment bounds**, **home-based term rules**, **appeals path**, **substitute capture safeguards** (**CI**), and **court-specific** continuity doctrine; this subsection states the **shared hybrid minimum** so institutions and courts do not silently diverge on the same capture-control structure.

Each relevant formation or chamber-creation instrument must operate a **mandatory published hybrid** that **combines** **home-based** authority and **rotating** authority. **Matter-by-matter designation** may supply the **rotating** pole where it replaces a standing rotating bench.

The instrument must state:
- how **home-based** authority supplies **continuity**;
- how **rotating** authority supplies **bounded attachment**, breadth, or matter-specific assignment;
- how the two combine on **ordinary lawful multi-member** deciding benches or decision bodies, **or**, where **lawful single-member** (or **sole-officer**) decision rules apply, how hybrid is still achieved **across the published decision workflow** (for example **staged** roles, mandatory **review** or **second-instance** participation, or another **equivalent** pattern that keeps **both** continuity and rotation **materially** present).

Where ordinary lawful deciding bodies are **multi-member**, the instrument must show how **home-based** authority remains a **minority** on the deciding bench or body, unless the instrument instead adopts an **equivalent hybrid across stages** that is **reasoned** and **published**.

**Home-based-only** or **rotating-only** composition is **non-compliant** for bodies within this subsection's scope that render **ordinarily binding** decisions, **except** during **published emergency** scopes permitted only under the **domain owner's** continuity and emergency rules (**parent institution** continuity rules and governing law for **CI**; **`corpus_forum.md` CC-11** and successor continuity rules for **Chapter Eight** court families), **only** for the emergency scope, and **only** with **documented return** to the hybrid **baseline** when emergency conditions end.

Where **CI** and **CC** obligations overlap on the same structure, the **stricter** clearly adopted rule governs (**CJS-2**, stricter-wins).

**Mandatory read-with:** **`corpus_institutions.md` CI-9.1B.1**–**CI-9.1B.4**; **`corpus_forum.md` CC-2.5.1**–**CC-2.5.5** and **CC-11** as applicable; `corpus_systems.md` **Chapter S2** and **Chapter S3** where classification scales the body.

### CJS-3.7A Shared attachment and continuity mechanics
Where **CJS-3.7** applies, rotating and home-based poles must follow these shared requirements:

- **Rotating attachment bounds:** the instrument must publish a bounded rotating attachment formula in terms rotating authorities can anticipate before service (for example a completed-matter count and calendar floor, whichever is longer, or an explicitly equivalent bounded formula).
- **No undefined duration discretion:** rotating attachment duration cannot be left to undefined discretion.
- **Illustration status:** sample formulas are illustrative only unless a domain owner marks them mandatory.
- **Home-based continuity terms:** where home-based authority is used, the instrument must publish term, renewal, or stagger rules suited to continuity.
- **No mirror requirement:** home-based term rules are not required to mirror rotating attachment formulas.

Class-, court-, and institution-specific scaling, assurance gates, emergency deviation controls, and substitution safeguards remain in domain-owner sections (**CI-9.1B**, **CC-2.5**, **CC-11**, and related cited hooks).

### CJS-3.8 Implementation companion boundary (CP ↔ CJS seam)
This file supplies the operative implementation text for its stable local labels. Those labels do not replace canonical constitutional definitions, rights floors, or owner-layer meanings elsewhere in the corpus.

**Cross-domain implementation layer** in **`corpus_joint_structure.md`** is the **authoritative incorporated home** for **Implementation Groups One through Four** operative implementation text (meta-integrity through governance implementation labels).

**Joint** structural obligations—where **two or more** of **CP** (implementation), **CS**, **CI**, and **CC** apply to the **same facts**—are stated in **CJS-2** and **CJS-3**. **CJS** joint requirements coordinate cross-companion interfaces; they do not replace **Implementation Groups One through Four** in the implementation section.

Where this file defines CJS-local operational structures in **OP-O/OP-E/OP-C** form, those structures are joint interface abstractions only. They do not replace the canonical substance of cited **PRIM/PROT** entries.

When revising **CP** (implementation):

- keep **implementation-owned** requirements in the **Cross-domain implementation layer** section;
- keep joint **read-with** restatements short—prefer **one-line** pointers to **CJS-3** (and **CJS-2.2** row IDs where that speeds navigation); and
- preserve **PRIM**/**PROT** code labels so **CS**, **CI**, and **CC** citations stay traceable (**CJS-3.6**).

### CJS-3.9 Cross-companion trust integrity (joint operation model)
This subsection applies where **CJS-R17** materially applies, or where a **CJS-2.2** read-with chain jointly determines whether reliance is justified in practice.

Canonical meaning of **Trust**, **Trustworthiness**, and **Trust Degradation and Misleading Reliance** remains in **`core_05-05_definitions_c_dependent_clusters.md` Chapter Five, section 3.38** (*Trust and Trustworthiness*). **Joint** evaluation for **trust degradation** and **misleading reliance** within this subsection’s scope follows those definitions together with their listed member definitions. Operative implementation remains in **`corpus_joint_structure.md`** Implementation Group One (*Meta-integrity obligation: Trust and Trustworthiness*). This subsection states **joint** requirements only.

It is **non-compliant** to claim trustworthiness when one companion presents conforming signals but another companion in the same materially relevant chain leaves unresolved conditions that defeat **observable**, **verifiable**, or **contestable** reliance (for example classification-scaled controls, pathway integrity, publication timeliness, accessibility, or documented escalation reliability).

Where trust **model** depends on combined operation across companions, institutions must maintain a published, auditable map that at minimum:
- identifies the companion obligations, classification/dependency/steward conditions, and assurance burden that jointly sustain the trust claim for scope;
- identifies contest and escalation interfaces, plus observable indicators and evidence channels, needed to challenge, correct, exit, and detect trust degradation; and
- identifies bounded correction and restoration pathways with accountable ownership.

Cross-companion trust claims must remain consistent with **CJS-3.2** (no false partial compliance), **CJS-3.5** (classification alignment), and **CJS-3.6** (implementation-label traceability and stricter-wins).

### CJS-3.10 Definition collision and precedence discipline
When language in a CJS Tier 1 abstraction and a companion-owner Tier 2 section appears to conflict, resolve in this order:

1. **Sentient Constitution** and **core definitions** (including **Chapter Fourteen** conflict order and canonical constitutional definitions).
2. **Canonical owner meaning** for domain substance in **CP**, **CS**, **CI**, or **CC** as routed by **CJS-2.2** and `doc_architecture.md`.
3. **CJS Tier 1 abstraction** for cross-companion joint trigger and interlock requirements.
4. **Subsection-local shorthand** and drafting convenience text.

If unresolved ambiguity remains after this order, treat the narrower reading as non-authoritative and route clarification to the canonical owner with an explicit CJS pointer update.

### CJS-3.11 Class-scaled lane staffing and competency redundancy
This subsection applies where **CJS-R18** materially applies: stewardship or operational roles with materially binding effect under **Chapter Ten**, section **5**, where system class and stewardship **profile** in `corpus_systems.md` **Chapter S2** and **Chapter S3** scale the burden for institutional lane design and competency continuity.

For **Class A** and **Class B** systems, institutions that host a constitutional functional separation (**lane**) with materially binding duties must maintain:
- at least **three sentients** assigned to that lane;
- documented lane-specific competency and succession coverage; and
- no single sentient as the sole qualified actor for that lane's materially binding duties.

Lane design must also preserve a functional **role-density balance**. Assignment, rotation, and backup rules must give each material role enough sustained engagement for competence, memory, and accountable judgment, while preserving enough cross-training and cross-functional familiarity for continuity, independent challenge, and lawful succession. It is not sufficient to satisfy numeric staffing while either diffusing responsibility across so many intermittent participants that competence becomes shallow, or concentrating practical knowledge in so few participants that the lane becomes fragile, captured, or unable to replace itself.

The constitutional floor remains in **[core_10-10_governance.md](core_10-10_governance.md) Chapter Ten**, section **5**. This subsection states joint structural requirements for cross-companion satisfaction only. Detailed role taxonomy, qualification controls, succession mechanics, and pathway-access design remain with domain owners in **CI-2**, **CI-4**, **CI-11**, and **CI-12**, read with `corpus_systems.md` **Chapter S2** and **Chapter S3**.

### CJS-3.12 Shared procedural abstractions for delegated bodies and forum routing
This subsection supplies **Tier 1** cross-companion abstractions for **CJS-R01** through **CJS-R04**. It does not replace owner detail in **CI** or **CC**.

For this subsection:

- **Delegated binding body (CJS abstraction):** a standing or recurring body below a parent institution that exercises materially binding delegated authority within published scope.
- **Lawful independent forum (CJS abstraction):** an adjudicative or equivalent merits forum formed under published authority, with required competence, quorum, and conflict-screened independence for the matter.
- **Backup activation (CJS abstraction):** documented transfer or co-routing to a constitutionally designated backup forum when the designated lead forum cannot provide lawful independent merits determination within the applicable timing floor.
- **Representative treatment (CJS abstraction):** procedure that resolves one or more common questions for a broader affected group only where commonality, notice, adequacy, and contestability are preserved.

Minimum joint consequence:

- It is **non-compliant** to treat a body or route as valid for joint-satisfaction claims if companion records do not make lawful authority, independence safeguards, and backup or contest pathways auditable where they materially apply.
- It is **non-compliant** to treat representative-treatment outcomes as structurally valid when common-question framing is used to suppress material sentient-specific contest rights that remain required under owner rules.

Owner detail remains canonical in **`corpus_institutions.md`** (including **CI-6**, **CI-8**, **CI-9.1B**) and **`corpus_forum.md`** (including **CC-3**, **CC-4**, **CC-5**).

### CJS-3.13 Cross-companion integrity assurance and resilience operations
This subsection supplies a CJS-local operational cluster for cross-companion integrity assurance and resilience where **CJS-R19** materially applies. It is read with `core_05-05_definitions_a_independent.md` **Chapter Five** (*Auditability*, *Verifiability*, *Verification Accessibility*, *Reversibility*, *Dependency*, *Cascading Failure*, *Adversarial, Scaled, and Exploited Conditions*, *Trustworthiness*) and does not replace their canonical meaning.

Cross-companion integrity assurance and resilience operations (operational cluster head)
- OP-O: Joint operation conditions where claims of auditability, verification, containment or recovery, retention proportionality, adversarial robustness, or ongoing legitimacy depend on combined behavior across two or more companions in a materially relevant chain. This includes cases where one companion holds records, another controls access, another governs classification or stewardship burden, and another runs challenge or adjudication pathways.
- OP-E: Evaluation must test the chain as an end-to-end operational path, not as isolated local controls. Assessment must include normal, degraded, and adversarial conditions, and must verify that challenge and escalation pathways remain practically usable. Evaluation must remain consistent with `core_05-05_definitions_a_independent.md` **Chapter Five** (*Auditability*, *Verifiability*, *Verification Accessibility*, *Reversibility*, *Dependency*, *Cascading Failure*, *Adversarial, Scaled, and Exploited Conditions*, *Trustworthiness*).
- OP-C: A cross-companion integrity claim is non-compliant where materially required chain conditions are missing, blocked, contradictory, or practically unusable. Passing controls in one companion cannot cure a material integrity failure in another companion in the same chain.

Audit reconstruction and tiered access continuity
- OP-O: Cross-companion pathways for record retention, disclosure tiering, qualified audit access, and forensic reconstruction where harm, dispute, or credible risk requires deeper inspection.
- OP-E: Evaluation must verify that records, access gates, qualification paths, and challenge routes operate together in time to support independent review and root-cause reconstruction proportional to impact.
- OP-C: It is non-compliant to keep records that cannot be practically reconstructed, or to publish access criteria that do not permit a real, non-exclusive path to qualified independent audit where materially required.

Independent verification path integrity
- OP-O: Joint pathways by which materially significant claims are independently tested, reproduced, and compared across models, methods, institutions, or oversight lanes.
- OP-E: Evaluation must verify at least one practical independent verification path per materially significant claim family, including reproducibility conditions and evidentiary comparability across qualified reviewers.
- OP-C: It is non-compliant to require reliance on unverifiable, single-authority, or non-reproducible claims where technical feasibility for independent verification exists.

Containment, reversibility, and retention lifecycle coherence
- OP-O: Cross-companion controls for failure isolation, rollback or compensatory restoration, and retention lifecycle handling when reversibility, accountability, and privacy constraints apply together.
- OP-E: Evaluation must test whether containment and restoration operations preserve enough records for accountability while preventing unjustified data accumulation, surveillance mode, or internal-state reconstruction beyond authorized scope.
- OP-C: It is non-compliant to choose retention or deletion settings that predictably defeat material investigation, challenge, or restoration duties, or to retain unjustified granular data in ways that create coercive leverage.

Adversarial response and revalidation non-entrenchment
- OP-O: Cross-companion operation of adversarial detection, proportionate mitigation, governance escalation, periodic revalidation, and replacement-readiness where new risk or superior alternatives emerge.
- OP-E: Evaluation must verify periodic revalidation cadence, challengeability, and documented update pathways under changing capabilities, attack patterns, and dependency profile.
- OP-C: It is non-compliant to preserve legacy structures by inertia alone where material risk, drift, or known vulnerabilities require reviewed correction, reauthorization, or replacement.

### CJS-3.14 Cross-companion quorum and participatory legitimacy terms
This subsection supplies CJS-local operational definitions for quorum and participatory legitimacy where cross-companion read-with chains materially govern binding decision rules. It is read with `corpus_joint_structure.md` Implementation Group Four, section 2 (*Decision Resolution Protocol*), and does not replace constitutional meaning in the Sentient Constitution `core_*.md` files (see [README.md](README.md)) or `core_05-05_definitions_a_independent.md`.

Cross-companion quorum and participatory legitimacy terms (operational cluster head)
- OP-O: Operational definition set for quorum and participatory legitimacy terms used across companion interactions that determine whether participation rules is valid for materially binding outcomes.
- OP-E: Evaluation must apply every component below together when this subsection materially applies. Partial or selective use of these terms is non-compliant for joint-satisfaction claims.
- OP-C: It is non-compliant to claim valid quorum where any required component term is unsatisfied, undefined for scope, or applied inconsistently across companions in the same materially relevant chain.

Participation
- OP-O: Minimum eligible engagement by participants entitled under the applicable constitutional and companion-file scope.
- OP-E: Evaluation must verify that eligibility routing and engagement records are published and auditable for the decision scope.
- OP-C: It is non-compliant to count ineligible actors as participation or to exclude eligible actors without lawful, documented basis.

Weighted participation
- OP-O: Combined participation weight (including impact, dependency, and standing where applicable) above a defined floor for the scoped decision.
- OP-E: Evaluation must verify that weighting factors, bounds against single-factor dominance, and revalidation cadence are documented, contestable, and auditable.
- OP-C: It is non-compliant to rely on opaque, single-authority, or manipulation-prone weighting that can materially distort participatory legitimacy.

Impact coverage
- OP-O: Representation of all materially affected groups required for quorum validity in scope.
- OP-E: Evaluation must verify that materially affected groups were identified through documented criteria and that representation gaps are visible before binding decision.
- OP-C: It is non-compliant to treat quorum as satisfied when a materially affected group is unrepresented without lawful, published exception controls.

Temporal
- OP-O: Participation window proportional to the decision's impact, scope, and reversibility **profile**.
- OP-E: Evaluation must verify that timing allows practical notice, engagement, challenge, and escalation where materially required.
- OP-C: It is non-compliant to use a participation window that predictably blocks meaningful participation for materially affected stakeholders.

Notification and pathway integrity
- OP-O: Materially binding participation processes provide timely notice of the proposed action, practical participation and challenge routes, decision status, and any material adaptation or exit implications where relevant.
- OP-E: Evaluation must verify that notice content and pathway design are understandable enough for materially affected stakeholders to engage before outcome hardening.
- OP-C: It is non-compliant to treat a participatory process as legitimate where notice is materially incomplete, too late for practical engagement, or structured so participation is formal only.

### CJS-3.15 Cross-companion comprehensibility and cognitive accessibility terms
This subsection supplies CJS-local operational definitions for cross-companion comprehensibility and cognitive accessibility where transparency, participation, auditability, and accountability depend on combined companion behavior. It is read with `corpus_joint_structure.md` **PRIM2**, `corpus_systems.md` **Protocol B**, and does not replace constitutional meaning in the Sentient Constitution `core_*.md` files (see [README.md](README.md)) or `core_05-05_definitions_a_independent.md`.

Cross-companion comprehensibility and cognitive accessibility terms (operational cluster head)
- OP-O: Operational definition set for whether materially relevant information is understandable, evaluable, and usable for lawful participation, audit, and oversight across companion interfaces.
- OP-E: Evaluation must apply all component entries below together when this subsection materially applies.
- OP-C: It is non-compliant to claim transparency where presentation is complete in volume but unusable in practice for materially affected stakeholders.

Meaningful transparency floor
- OP-O: A system that cannot be meaningfully understood is not transparent for this subsection's scope.
- OP-E: Evaluation must test practical interpretability of purpose, operation, impact, and key decision pathways for qualified stakeholders.
- OP-C: It is non-compliant to treat disclosure quantity alone as satisfying transparency where meaningful understanding is absent.

Layering and access
- OP-O: Presentation forms are accessible to relevant stakeholders and structured from high-level summaries through detailed inspection.
- OP-E: Evaluation must verify adaptation to expertise and context while preserving navigable access to deeper technical layers.
- OP-C: It is non-compliant to provide a single-layer presentation that predictably excludes materially affected stakeholders from effective understanding.

Summary integrity
- OP-O: High-level summaries preserve material accuracy and do not mislead through oversimplification.
- OP-E: Evaluation must compare summaries against underlying records, logic, and constraints for material consistency.
- OP-C: It is non-compliant to use summaries that omit or distort material conditions required for lawful evaluation.

Cognitive overload barrier controls
- OP-O: Complexity does not replace transparency or block participation, audit, or accountability.
- OP-E: Evaluation must verify that volume, fragmentation, and interface design do not create complete-but-unusable presentation burdens.
- OP-C: It is non-compliant to require unreasonable time, expertise, or resources to interpret behavior, risk, or impact where proportional alternatives are feasible.

Behavior and structure representation adequacy
- OP-O: Representations are adequate to understand purpose, operation, impact, risks, dependencies, and decision processes.
- OP-E: Evaluation must verify that stakeholders can use representations for meaningful participation and oversight, not only passive viewing.
- OP-C: It is non-compliant where representations are materially incomplete for risk evaluation or governance participation.

Interpretation support fidelity
- OP-O: Where complexity exceeds unaided comprehension, structured summaries, explanatory models or abstractions, and interpretation tools or interfaces are provided.
- OP-E: Evaluation must verify that interpretation support preserves material accuracy and allows traceability to underlying data and processes.
- OP-C: It is non-compliant for interpretation support to distort underlying information, introduce hidden bias, or replace access to underlying data and processes.

High-impact drill-down and assisted evaluation
- OP-O: High-impact systems provide clear summaries of behavior, risks, and decisions, plus drill-down into data, logic, and dependencies.
- OP-E: Evaluation must verify at least one practical assisted-interpretation path sufficient for meaningful independent evaluation.
- OP-C: It is non-compliant to claim high-impact comprehensibility without practical drill-down and non-exclusive assisted evaluation pathways.

Proportional application
- OP-O: Comprehensibility burden scales with system impact, stakeholder dependency, and behavioral or structural complexity.
- OP-E: Evaluation must verify that simplification choices for lower-impact contexts do not create material barriers to understanding or risk evaluation.
- OP-C: It is non-compliant to apply uniform minimal presentation where higher-impact or higher-dependency conditions require stronger interpretability controls.

### CJS-3.16 Cross-companion salience integrity and attention-allocation terms
This subsection supplies CJS-local operational definitions for salience integrity where ranking, recommendation, filtering, or other attention-allocation mechanisms depend on combined companion behavior. It is read with `corpus_joint_structure.md` **PRIM1**, **PRIM4**, **PRIM14**, and with the Sentient Constitution `core_*.md` files (see [README.md](README.md)) **Article XV-A** and **Chapter Ten** incentive-alignment constraints.

Cross-companion salience integrity and attention-allocation terms (operational cluster head)
- OP-O: Operational definition set for lawful salience allocation, anti-distortion controls, disclosure, user control, and mitigation duties where salience materially influences understanding or decisions.
- OP-E: Evaluation must apply all component entries below together when this subsection materially applies.
- OP-C: It is non-compliant to treat salience behavior as constitutionally aligned when any material component below is unsatisfied in the same companion chain.

Salience integrity floor
- OP-O: Systems that present, rank, filter, recommend, or otherwise prioritize information allocate salience in ways that preserve informational integrity, support informed decision-making, and avoid distortion of stakeholder perception.
- OP-E: Evaluation must test visibility, prominence, ordering, and prioritization outcomes as core system functions under constitutional constraints.
- OP-C: It is non-compliant where default or ongoing salience rules predictably bias perception or behavior toward outcomes that degrade informational integrity, agency, or constitutional alignment.

Material-visibility and risk legibility controls
- OP-O: Material risks, uncertainties, limitations, and decision-relevant information remain appropriately visible and accessible.
- OP-E: Evaluation must verify that placement, deprioritization, and interface design do not obscure what is materially needed for safety, consent, participation, or oversight.
- OP-C: It is non-compliant where prominence or suppression systematically distorts relative importance, likelihood, impact, or prevalence of material information.

Anti-manipulation and prohibited-pattern controls
- OP-O: Salience mechanisms do not allocate, amplify, suppress, fragment, or delay information in ways intended or reasonably expected to distort understanding or induce harmful behavior.
- OP-E: Evaluation must screen for prohibited patterns including engagement or retention optimization that predictably distorts understanding, burying of material safety or consent information, and feedback loops that amplify misleading, harmful, manipulative, or agency-impairing content.
- OP-C: It is non-compliant where salience manipulation alters interpretation, risk perception, or decision-making without satisfying the Sentient Constitution `core_*.md` files (see [README.md](README.md)) **Article XV-A** and required implementation controls.

Engagement-conflict priority rule
- OP-O: Where engagement objectives conflict with informational integrity, systems prioritize accuracy, proportional risk and relevance representation, and stakeholder agency.
- OP-E: Evaluation must verify that metric optimization is bounded by integrity constraints and does not override material-truth obligations.
- OP-C: It is non-compliant to retain engagement-maximizing salience behavior that predictably degrades informational integrity or agency.

Explainability and disclosure sufficiency
- OP-O: At impact-proportional depth, systems disclose primary factors affecting ranking, recommendation, and prioritization, including whether and how engagement, behavioral prediction, or optimization objectives affect salience.
- OP-E: Evaluation must verify disclosure of known limitations, biases, and failure modes, plus meaningful explanations in high-impact contexts for why specific information is shown, prioritized, or suppressed.
- OP-C: It is non-compliant where disclosures are inaccessible, not understandable, or insufficient for independent constitutional-alignment evaluation and salience-outcome audit.

User agency and control
- OP-O: Stakeholders have meaningful, usable control over prioritization and presentation, including disabling or modifying ranking and filtering where appropriate, using chronological or minimally processed views, and selecting among alternative ranking criteria or models.
- OP-E: Evaluation must verify that controls are available without disproportionate effort, hidden interface discouragement, unreasonable expertise demands, or loss of core functionality.
- OP-C: It is non-compliant to penalize control use by degrading system access or practical utility.

Detection, mitigation, and corrective response
- OP-O: Systems monitor for, detect, and address salience-allocation patterns that misrepresent risk, importance, or consensus; amplify harmful or destabilizing content; or degrade agency, understanding, or decision capacity.
- OP-E: Evaluation must verify disclosure of identified conditions, attribution of contributing mechanisms, and corrective adjustments proportional to impact.
- OP-C: Failure to detect or mitigate known or reasonably detectable salience-driven distortion is non-compliant.

Incentives and adversarial resilience
- OP-O: Salience pathways are treated as high-risk surfaces for incentive misalignment, coordinated manipulation, and adversarial amplification or suppression.
- OP-E: Evaluation must verify adversarial threat-model coverage, resistance to gaming of engagement or visibility metrics, disclosure where incentives influence salience, and mitigation of predictable distortions.
- OP-C: It is non-compliant where incentive structures systematically degrade informational integrity or stakeholder agency.

Proportional application
- OP-O: Salience requirements scale with impact on sentients, environment, and info-sphere; dependency on outputs; and degree of system-mediated influence on decisions.
- OP-E: Evaluation must verify strongest controls for systems mediating access to information at scale, and only bounded simplification for low-impact contexts.
- OP-C: It is non-compliant to apply simplified salience mechanisms where they materially distort understanding, create externalized harm, or impair informed participation.

### CJS-3.17 Cross-companion disclosure sufficiency and observability terms
This subsection supplies CJS-local operational definitions for disclosure sufficiency and observability where informed participation, independent verification, and attribution depend on combined companion behavior. It is read with `corpus_joint_structure.md` **PRIM4**, `corpus_joint_structure.md` **PRIM5** where dependencies are material, and the Sentient Constitution `core_*.md` files (see [README.md](README.md)) **Article XV-A** and **Article VII-B**.

Cross-companion disclosure sufficiency and observability terms (operational cluster head)
- OP-O: Operational definition set for disclosure adequacy, verification enablement, private-state boundary handling, and externally relevant observability in materially relevant companion chains.
- OP-E: Evaluation must apply all component entries below together when this subsection materially applies.
- OP-C: It is non-compliant to claim transparency or disclosure sufficiency when one component in this cluster is materially unsatisfied.

Impact- and dependency-proportional disclosure sufficiency
- OP-O: In proportion to impact and dependency, systems disclose information sufficient for informed participation, and enough detail to evaluate behavior, risk, constraints, material dependencies, and integrations.
- OP-E: Evaluation must verify that disclosure depth scales with impact and dependency, and that provided detail is practically usable for decision and oversight functions.
- OP-C: It is non-compliant where disclosure depth is materially below what impact and dependency conditions require.

Minimum disclosure content set
- OP-O: Where material, disclosures include underlying assumptions, methodologies and evaluation criteria, stated purpose and classification, decision logic affecting outcomes, and known risks, limitations, and uncertainties.
- OP-E: Evaluation must verify content completeness against the material scope and identify omissions that alter interpretation or risk profile.
- OP-C: It is non-compliant to omit materially required content from the minimum disclosure set.

Verification and comparative interpretation enablement
- OP-O: Disclosures enable meaningful independent verification, comparison of alternative interpretations where they exist, and identification of material failure modes or blind spots.
- OP-E: Evaluation must verify at least one practical independent path for checking claims, comparing alternatives, and surfacing failure conditions.
- OP-C: It is non-compliant where disclosures are present but cannot support practical independent verification or alternative interpretation testing.

Private internal-state boundary and external observability attribution
- OP-O: Transparency does not require exposure of private internal states under **Article VII-B**; systemic effects and externally relevant behaviors remain observable and attributable to system operation.
- OP-E: Evaluation must verify that privacy-boundary protections are preserved while external behavior, impacts, and accountability-relevant outputs remain auditable and attributable.
- OP-C: It is non-compliant either to force private internal-state exposure beyond lawful scope or to hide externally relevant behavior behind privacy-boundary claims.

### CJS-3.18 Cross-companion dependency integrity and disclosure terms
This subsection supplies CJS-local operational definitions for dependency integrity and disclosure where dependency mapping, risk treatment, and accountability depend on combined companion behavior. It is read with `corpus_joint_structure.md` **PRIM5**, **PRIM4**, **PRIM7**, **PRIM9**, **PRIM15**, `corpus_systems.md` **Protocol A**, and the Sentient Constitution `core_*.md` files (see [README.md](README.md)) **Article XV-A**.

Cross-companion dependency integrity and disclosure terms (operational cluster head)
- OP-O: Operational definition set for dependency identification, criticality treatment, substitution and exit constraints, anti-evasion controls, and dependency-monitoring obligations in materially relevant companion chains.
- OP-E: Evaluation must apply all component entries below together when this subsection materially applies.
- OP-C: It is non-compliant to claim dependency integrity where any material component below is unsatisfied or contradicted across companions.

Dependency identification and disclosure content
- OP-O: Systems identify upstream and downstream dependencies, disclose material relationships, and maintain current auditable dependency records.
- OP-E: Evaluation must verify coverage across technical, economic, governance, and interoperability dependencies, with disclosure usable for materially affected stakeholders.
- OP-C: It is non-compliant to omit or stale-materially dependency relationships that affect behavior, risk, or accountability.

Criticality and impact classification
- OP-O: Systems evaluate and disclose dependency criticality including reliance degree, substitute availability, switching cost, exit feasibility, and cascading-failure potential, plus impact of loss on sentients, environment, and info-sphere.
- OP-E: Evaluation must verify that classification supports single-point identification, mitigation prioritization, and informed decisions.
- OP-C: It is non-compliant where high-criticality dependencies are not explicitly identified, monitored, and subject to enhanced audit and review.

Substitutability, exit constraints, and mitigation duties
- OP-O: For material dependencies, disclosures include viable alternatives, substitution effects, transition feasibility, cost, and risk; constraints that materially impair exit, migration, or interoperability are explicitly disclosed.
- OP-E: Evaluation must verify justified limits under applicable proportionality and feasibility controls, with feasible mitigation pursued or infeasibility justified.
- OP-C: It is non-compliant to hide dependency-driven exit constraints or leave known constraints unmitigated without lawful justification.

Hidden, indirect, and externalized risk controls
- OP-O: Systems do not distribute dependencies across layers, intermediaries, or time-separated processes to obscure existence or impact, and do not use indirect or third-party reliance to evade accountability.
- OP-E: Evaluation must verify that indirect or transitive dependencies with material effects are disclosed, attributable, and included in mapping and evaluation.
- OP-C: It is non-compliant to externalize risk onto dependents without disclosure, justification, and accountable mitigation or compensation pathways.

Monitoring cadence, map adequacy, and anti-evasion structure
- OP-O: Systems continuously monitor dependencies; update disclosures and reassess risk, substitutability, and criticality under material change; and maintain maps adequate for relationship, critical-node, and failure-pathway audit and investigation.
- OP-E: Evaluation must verify refresh cadence proportional to criticality and risk velocity, plus map accessibility and interpretability proportional to impact.
- OP-C: It is non-compliant to keep stale dependency disclosures under material change, inflate complexity to reduce auditability or exit, or create artificial dependencies to evade requirements.

Proportional application
- OP-O: Dependency-integrity obligations scale with impact, stakeholder dependency, and cascading or systemic failure potential.
- OP-E: Evaluation must verify that any reduced rigor in lower-impact contexts does not introduce hidden dependencies, externalized risk, or material effects on other systems or sentients.
- OP-C: It is non-compliant to apply simplified dependency controls where material cross-system or cross-sentient exposure remains.

### CJS-3.19 Cross-companion graceful degradation and failure-mode integrity terms
This subsection supplies CJS-local operational definitions for graceful degradation and failure-mode integrity where reliability, signaling, containment, and recovery depend on combined companion behavior. It is read with `corpus_joint_structure.md` **PRIM6**, **PRIM1**, **PRIM5**, **PRIM12**, **PRIM15**, `corpus_systems.md` **Protocol A**, and constitutional hooks in the Sentient Constitution `core_*.md` files (see [README.md](README.md)) (**Chapter One**, **Article XV-A**, and **Article XVI-A** where lifecycle constraints are material).

Cross-companion graceful degradation and failure-mode integrity terms (operational cluster head)
- OP-O: Operational definition set for degraded-mode behavior under partial failure, uncertainty, or stress, including failure-mode coverage, signaling, bounded operation, escalation, and cross-boundary controls.
- OP-E: Evaluation must apply all component entries below together when this subsection materially applies.
- OP-C: It is non-compliant to claim graceful degradation where any material component below is unsatisfied or contradicted across the same companion chain.

Graceful degradation floor and defined failure-mode coverage
- OP-O: Systems degrade in controlled, observable, non-deceptive ways, preserve functional integrity where feasible, and avoid silent degradation, misleading outputs, or disproportionate harm.
- OP-E: Evaluation must verify explicit definition, implementation, and documentation of material failure modes, including component loss, data corruption or unavailability, dependency instability, adversarial partial compromise, and uncertainty beyond validated thresholds.
- OP-C: It is non-compliant to rely on implicit or purely emergent failure behavior where material failure-mode definition is required.

Signaling integrity and anti-silent-failure controls
- OP-O: When capability, reliability, or integrity materially drops, degraded state is surfaced with scope proportional to impact; degraded outputs are not presented as equivalent to normal operation.
- OP-E: Evaluation must verify degraded modes are distinguishable, confidence and uncertainty indicators are adjusted to actual conditions, and downstream propagation of degradation signals occurs where relevant.
- OP-C: It is non-compliant to preserve a false appearance of normal operation under material degradation.

Priority order and honest representation
- OP-O: Under constrained function, systems prioritize survival and foundational requirements first, then auditability and reconstructability, then reversibility, containment, and recovery.
- OP-E: Evaluation must verify optimization or performance objectives do not override truthful degradation representation or integrity-risk disclosure.
- OP-C: It is non-compliant to sacrifice accurate degradation signaling for convenience, throughput, or optimization gains.

Bounded operation, safe-mode transitions, and shutdown discipline
- OP-O: Degraded operation stays within defined auditable bounds and does not produce false, fabricated, or overconfident outputs; does not cause irreversible or unbounded harm; and preserves audit, reconstruction, and challenge capacity.
- OP-E: Evaluation must verify that where safe degraded operation is infeasible, the system enters safe bounded operation, limited mode, or suspension with documented basis consistent with applicable proportionality and safety constraints.
- OP-C: It is non-compliant to continue degraded operation outside defined safety and integrity bounds.

Fail-soft within constraints and non-externalization
- OP-O: Fail-soft behavior preserves partial function only within defined safety and integrity bounds while limiting propagation and cascading amplification.
- OP-E: Evaluation must verify critical-function preservation where safe, bounded failure scope, and anti-propagation controls.
- OP-C: It is non-compliant to use fail-soft mode to justify out-of-bounds operation or to externalize degradation onto dependents without disclosure and mitigation.

Monitoring, transition traceability, escalation, and revalidation
- OP-O: Systems monitor decline, anomalies, dependency instability, and uncertainty escalation; transitions into and out of degraded states are detectable, documented, and auditable.
- OP-E: Evaluation must verify escalation, mitigation, recovery pathways when degradation persists or worsens, support for root-cause analysis, and periodic revalidation where required.
- OP-C: It is non-compliant to leave degraded-state transitions or persistent degradation unmanaged, untraceable, or unauditable.

Cross-boundary propagation controls
- OP-O: Degradation effects across dependencies are accounted for; degraded data, signals, or decisions crossing boundaries include disclosure of degraded state and limitations.
- OP-E: Evaluation must verify downstream disclosure adequacy and containment controls for cascading failure risk.
- OP-C: It is non-compliant to transmit degraded outputs across boundaries without sufficient degradation disclosure and containment safeguards.

Proportional application
- OP-O: Degraded-mode requirements scale with impact, dependency, and irreversibility risk.
- OP-E: Evaluation must verify that simplified handling in lower-impact contexts does not misrepresent capability, externalize harm, or impair risk and reliability evaluation.
- OP-C: It is non-compliant to apply reduced degraded-mode controls where material harm or dependency exposure persists.

### CJS-3.20 Cross-companion interoperability, portability, and exit-integrity terms
This subsection supplies CJS-local operational definitions for interoperability, portability, and exit integrity where lock-in risk, transition feasibility, interface controls, and dependency exposure depend on combined companion behavior. It is read with `corpus_joint_structure.md` **PRIM7**, **PRIM5**, **PRIM4**, `corpus_systems.md` **Chapter S1**, **Chapter S2**, **Chapter S3**, and constitutional hooks in the Sentient Constitution `core_*.md` files (see [README.md](README.md)) (**Article XIX**, **Article XV-A**, and related rights floors where materially implicated).

Cross-companion interoperability, portability, and exit-integrity terms (operational cluster head)
- OP-O: Operational definition set for anti-lock-in safeguards, usable exit pathways, portability quality, interoperability reciprocity, innovation-boundary handling, and continuity-preserving transition controls.
- OP-E: Evaluation must apply all component entries below together when this subsection materially applies.
- OP-C: It is non-compliant to claim interoperability or exit integrity where one or more material components below are unsatisfied in the same companion chain.

Lock-in and anti-coercion safeguards
- OP-O: Systems do not design toward coercive lock-in, do not exploit data, identity, or network effects to block exit, and do not impose artificial switching costs unrelated to legitimate integrity or safety.
- OP-E: Evaluation must verify mitigation where natural lock-in emerges, including compensatory mechanisms preserving meaningful exit.
- OP-C: It is non-compliant to retaliate against exit through service degradation, discriminatory penalties, or forfeiture conditions on portability or interoperability rights.

Right-to-exit pathway integrity
- OP-O: Exit is functionally available without violating foundational rights, with clear, time-bound pathways proportionate to impact, dependency, and feasibility.
- OP-E: Evaluation must verify practical support for sentients and dependents to exit without undue delay, obstruction, coercion, loss of survival-critical access, or unjustified punitive standing effects.
- OP-C: It is non-compliant where exit is nominal but functionally blocked or coercively constrained.

Portability quality and non-obstruction controls
- OP-O: Portability is secure, usable, structured, and semantically coherent, including relevant identity, attribution, and continuity-critical state data within lawful privacy bounds.
- OP-E: Evaluation must verify that exports and transfer paths include schema, documentation, context, and tooling sufficient for practical reuse.
- OP-C: It is non-compliant to degrade, fragment, obscure, or technically gate data portability to prevent meaningful reuse.

Interchange and open-interface baseline
- OP-O: Where impact and dependency are material, systems prefer open, documented, interoperable interchange formats and openly documented interfaces; narrower choices require explicit lawful justification.
- OP-E: Evaluation must verify interoperability reliability and performance proportional to impact, and that interface controls are not used to defeat migration, substitution, or independent verification.
- OP-C: It is non-compliant to impose artificial incompatibility, selective rate limits, or exclusive pathway control that coerces dependents or suppresses exit.

Shared-interface recognition and divergence accountability
- OP-O: Later adopters presumptively recognize materially relevant shared standards that are openly documented and reviewably maintained, unless reasoned constitutional or materially contextual divergence is recorded.
- OP-E: Evaluation must verify documented, reviewable records for non-recognition or incompatibility, including constitutional basis, incompatibility point, and divergence scope.
- OP-C: Silent incompatibility is non-compliant where this subsection materially applies.

Innovation reward boundary and anti-enclosure controls
- OP-O: Innovation reward implementation preserves repair, verification, interoperability, migration, and meaningful exit; exclusivity on dependency-critical components remains narrowly justified, time-bounded, and continuity-protective.
- OP-E: Evaluation must verify class-scaled handling for dependency-critical systems, carve-out domain safeguards, disclosure sufficiency for scope and reproducibility, and reclassification-triggered obligation updates.
- OP-C: It is non-compliant where innovation-reward claims create coercive lock-in, concealed interoperability barriers, or durable exclusion beyond justified bounds.

Exit-feasibility disclosure and dependency transparency
- OP-O: Systems disclose dependencies that materially affect exit, including switching costs, migration/disconnection risks, alternatives, substitutability, and downstream impact.
- OP-E: Evaluation must verify that exit-relevant dependency disclosures are complete, attributable, and auditable in coordination with dependency-integrity controls.
- OP-C: Hidden or undisclosed dependencies that materially impair exit are non-compliant.

Continuity-preserving transition safeguards
- OP-O: Exit and migration controls preserve continuity of identity, participation, and recoverable state where feasible, and avoid making exit equivalent to erasure of social or economic existence.
- OP-E: Evaluation must verify safe transition pathways, rollback or recovery options after failed migration, and minimization plus pre-disclosure of unavoidable continuity loss.
- OP-C: It is non-compliant to force discontinuity outcomes beyond what is inherent, minimized, disclosed in advance, and lawfully justified.

Proportional application
- OP-O: Interoperability, portability, and exit-integrity obligations scale with impact, dependency, ecosystem integration, and irreversibility of lock-in.
- OP-E: Evaluation must verify that any reduced rigor in low-impact contexts does not create hidden dependencies, external lock-in effects, or material harms to other systems or sentients.
- OP-C: It is non-compliant to apply simplified controls where material lock-in or dependency externalities remain.

### CJS-3.21 Cross-companion intervention and override integrity terms
This subsection supplies CJS-local operational definitions for intervention and override integrity where technical control pathways, governance authorization, and accountability depend on combined companion behavior. It is read with `corpus_joint_structure.md` **PRIM8**, **PRIM6**, **PRIM9**, **PRIM14**, **PRIM15**, `corpus_joint_structure.md` **PROT2**, and constitutional hooks in the Sentient Constitution `core_*.md` files (see [README.md](README.md)) (**Articles IX, XII, XIII**, plus Chapter One necessity and proportionality constraints).

Cross-companion intervention and override integrity terms (operational cluster head)
- OP-O: Operational definition set for timely intervention capacity, trigger conditions, technical pathways, authority scoping, anti-abuse controls, record integrity, emergency coupling discipline, and proportional scaling.
- OP-E: Evaluation must apply all component entries below together when this subsection materially applies.
- OP-C: It is non-compliant to claim intervention readiness or override legitimacy where any material component below is unsatisfied in the same companion chain.

Intervention timeliness and practical control floor
- OP-O: Intervention is timely, proportionate, and accountable under failure, uncertainty, and adversarial conditions, with practical ability to interrupt, constrain, or redirect harmful behavior in relevant timeframes.
- OP-E: Evaluation must verify response timeframes match harm speed and severity, and that intervention remains practical rather than nominal.
- OP-C: It is non-compliant where systems cannot be meaningfully intervened within materially required prevention timeframes.

Trigger scope and timeliness applicability
- OP-O: Intervention triggers apply to risks of harm to sentients, environmental or info-sphere degradation, and integrity, safety, or accountability failures.
- OP-E: Evaluation must verify trigger coverage is operationalized with explicit thresholds and does not depend on post-hoc remedy alone when harm can outpace adjudication or restoration.
- OP-C: It is non-compliant to rely solely on post-hoc audit or restoration when preemptive technical intervention is materially required.

Technical pathway adequacy and reliability
- OP-O: Material-impact systems implement clearly defined, auditable intervention pathways (including stop, pause, containment, scoped override, and safe-mode fallbacks) scaled to risk and impact.
- OP-E: Evaluation must verify authorized-access routing, reliable behavior under degraded or adversarial conditions, and non-assumption of good-faith-only operation.
- OP-C: It is non-compliant where intervention pathways are undefined, unreliable, inaccessible to authorized control, or ineffective under adversarial conditions.

Authority scoping, role clarity, and anti-capture constraints
- OP-O: Override authority is scoped to minimum necessary components, duration, and effects; role-defined by trigger conditions and limits; and proportionate to severity, probability, and reversibility of harm.
- OP-E: Evaluation must verify controls against unrestricted unilateral override and capture-prone architecture.
- OP-C: It is non-compliant where override power is effectively unbounded, opaque, or structured for coercive abuse.

Attribution, records, and transparency defaults
- OP-O: Interventions are attributable, documented for audit and reconstruction, and transparent by default with only narrowly justified temporary restrictions.
- OP-E: Evaluation must verify records include trigger or justification, scope and duration, affected actions/components, outcomes, and follow-up.
- OP-C: It is non-compliant to execute or retain intervention effects without sufficient attribution, record completeness, or disclosure.

Abuse safeguards and review controls
- OP-O: High-impact intervention pathways include multi-party or quorum constraints, rate limits, staged escalation, independent post-action review, and limits on pre-authorized automation bypassing real-time accountability.
- OP-E: Evaluation must verify safeguards are enforceable in operation and auditable across events.
- OP-C: It is non-compliant where intervention pathways permit repeated high-impact use without meaningful anti-abuse controls and review.

Intervention behavior priorities and safe-state handling
- OP-O: During intervention, systems prioritize survival and foundational requirements, preserve auditability/reversibility/containment, prevent cascading failure, and move to safe or limited modes or suspension when safe continuation is infeasible.
- OP-E: Evaluation must verify operational behavior during interventions reflects these priorities in real conditions.
- OP-C: It is non-compliant where intervention behavior conceals secondary effects, disables auditability, or allows uncontrolled propagation.

Emergency technical-coupling discipline
- OP-O: Emergency technical interventions remain minimal, proportionate, and time-bounded, with immediate audit/review and rollback or restoration where feasible; they do not normalize without renewed necessity/proportionality justification and revalidation.
- OP-E: Evaluation must verify emergency records, expiry behavior, post-action review, and governance coupling to lawful sequencing controls.
- OP-C: It is non-compliant to treat emergency intervention as standing default control without recurring justification and review.

Proportional application
- OP-O: Intervention and override obligations scale with impact, harm speed, dependency, irreversibility, and autonomy from direct control.
- OP-E: Evaluation must verify that any simplified controls in lower-impact contexts still preserve timely mitigation, non-externalization of harm, and stakeholder risk-response capability.
- OP-C: It is non-compliant to reduce intervention controls where material harm prevention or accountability needs remain.

### CJS-3.22 Cross-companion auditability and reconstructability terms
This subsection supplies CJS-local operational definitions for auditability and reconstructability where records, access pathways, and verification design depend on combined companion behavior. It is read with `corpus_joint_structure.md` **PRIM9**, **PRIM4**, **PRIM10**, the Sentient Constitution `core_*.md` files (see [README.md](README.md)) **Article XV-A**, and **Article VII-B** where internal-state protections constrain audit design.

Cross-companion auditability and reconstructability terms (operational cluster head)
- OP-O: Operational definition set for verifiable and independently reviewable records, harm/dispute reconstructability, proportional forensic depth, and privacy-boundary-constrained observability.
- OP-E: Evaluation must apply all component entries below together when this subsection materially applies.
- OP-C: It is non-compliant to claim auditability where any material component below is absent, unusable, or contradicted across the same companion chain.

Auditability floor and record sufficiency
- OP-O: Systems maintain records sufficient to evaluate constitutional-compliance claims, reconstruct behavior in harm or dispute contexts, and support independent verification of material assertions.
- OP-E: Evaluation must verify practical sufficiency of record scope, quality, and retention rules for independent review.
- OP-C: It is non-compliant where records exist but cannot practically support compliance evaluation, reconstruction, or independent verification.

Operational transparency and structured logging requirements
- OP-O: Systems provide operational transparency and structured audit logs proportional to impact.
- OP-E: Evaluation must verify logs are intelligible, attributable, and navigable enough for independent audit and challenge pathways.
- OP-C: It is non-compliant where logging is unstructured, inaccessible, or insufficient to support meaningful review.

Forensic-depth access proportionality
- OP-O: Systems provide deeper forensic access when harm, credible risk, or investigation requirements materially require full reconstruction.
- OP-E: Evaluation must verify escalation paths from ordinary records to forensic depth are real, timely, and independently usable.
- OP-C: It is non-compliant to keep only superficial records where forensic-grade reconstruction is materially required.

Article VII-B boundary and anti-concealment rule
- OP-O: Limits on inference or exposure of private internal states are narrowly drawn and justified under **Article VII-B**.
- OP-E: Evaluation must verify that privacy-boundary controls preserve systemic observability needed for accountability and do not block lawful audit.
- OP-C: It is non-compliant to use internal-state protections to conceal systemic behavior or defeat accountability obligations.

### CJS-3.23 Cross-companion tiered transparency and audit-access terms
This subsection supplies CJS-local operational definitions for tiered transparency and audit access where public visibility, qualified review, and forensic reconstruction depend on combined companion behavior. It is read with `corpus_joint_structure.md` **PRIM10**, **PRIM9**, **PRIM12**, and constitutional hooks in the Sentient Constitution `core_*.md` files (see [README.md](README.md)) (**Sentient Constitution Chapter Nine, Articles V through IX**, **Article XV-A**, and **Article VII-B**).

Cross-companion tiered transparency and audit-access terms (operational cluster head)
- OP-O: Operational definition set for tiered information access balancing transparency, auditability, and protected internal-state boundaries while preserving contestability.
- OP-E: Evaluation must apply all component entries below together when this subsection materially applies.
- OP-C: It is non-compliant to claim tiered transparency compliance where any material component below is absent, inaccessible, or structurally defeated.

Tier structure and baseline accessibility
- OP-O: Information access is structured in tiers, and each tier balances transparency, auditability, and **Article VII-B** constraints.
- OP-E: Evaluation must verify baseline access enables understanding of system behavior, risk, dependency, and meaningful participation for materially affected stakeholders.
- OP-C: It is non-compliant to define tiers that leave baseline access insufficient for practical participation or risk evaluation.

Qualified audit pathways and non-exclusive eligibility
- OP-O: Where full public access is inappropriate, systems provide qualified independent-auditor pathways with transparent qualification criteria and open, non-exclusive routes for eligible sentients in good standing.
- OP-E: Evaluation must verify that qualification routes are practically reachable and not functionally monopolized.
- OP-C: It is non-compliant to use qualification mechanisms as hidden exclusion barriers to independent audit.

Restriction-scoping and justification discipline
- OP-O: Access restrictions are narrowly scoped, justified, and themselves auditable.
- OP-E: Evaluation must verify restriction records include rationale, scope, duration, and review mechanisms.
- OP-C: It is non-compliant to apply broad, indefinite, or unreviewable access restrictions.

Forensic escalation and reconstruction sufficiency
- OP-O: For harm, dispute, or credible risk, systems provide access sufficient for full reconstruction where necessary and feasible, supporting independent investigation, verification, and root-cause analysis.
- OP-E: Evaluation must verify escalation from baseline/qualified tiers to forensic depth functions in materially relevant timeframes.
- OP-C: It is non-compliant to block or hollow forensic pathways where material reconstruction is required.

Access-control integrity and anti-concealment
- OP-O: Access controls are transparent in design, auditable in operation, and challengeable; they are not used to conceal systemic behavior or create artificial barriers to audit.
- OP-E: Evaluation must verify control operation preserves accountability and contestability across companion boundaries.
- OP-C: It is non-compliant where access-control architecture undermines accountability, independent verification, or challenge rights.

### CJS-3.24 Cross-companion independent verification and claim-integrity terms
This subsection supplies CJS-local operational definitions for independent verification and integrity of claims where evidence quality, verification pathways, and cross-companion trust **model** depend on combined behavior. It is read with `corpus_joint_structure.md` **PRIM11**, **PRIM9**, **PRIM10**, and constitutional hooks in the Sentient Constitution `core_*.md` files (see [README.md](README.md)) Chapter Fourteen and rights-layer protections where material claims shape rights-relevant decisions.

Cross-companion independent verification and claim-integrity terms (operational cluster head)
- OP-O: Operational definition set for materially significant claim verification, reproducibility, plurality of evaluative pathways, and anti-monopoly verification design.
- OP-E: Evaluation must apply all component entries below together when this subsection materially applies.
- OP-C: It is non-compliant to treat claims as constitutionally reliable where one or more material components below are missing, blocked, or practically unusable.

Material-claim verification scope
- OP-O: Material claims about behavior, compliance, or impact are subject to independent, reproducible, and pluralistic verification, including environmental, informational, governance, algorithmic, and performance/safety/reliability assertions where applicable.
- OP-E: Evaluation must verify claim families are explicitly mapped to verification pathways and evidence standards.
- OP-C: It is non-compliant to classify materially consequential claims as exempt from independent verification without lawful technical-feasibility grounds.

Reproducibility and external evaluation viability
- OP-O: Verification mechanisms support reproducible testing and external evaluation by independent parties able to reach and compare conclusions.
- OP-E: Evaluation must verify that evidence and methods are sufficiently documented for qualified independent reproduction.
- OP-C: It is non-compliant where verification depends on non-reproducible evidence or opaque methods despite technical feasibility.

Anti-single-authority verification constraint
- OP-O: **Verification** **design** avoids dependence on a single authority, model, or interpretive framework for materially significant claims.
- OP-E: Evaluation must verify at least one practical independent path beyond a single controlling authority where feasible.
- OP-C: It is non-compliant to require confidence in unverifiable or monopoly-gated claims where independent verification is technically feasible.

Class-scaled template floor mapping
- OP-O: Class-scaled compliance templates preserve three floors when materially applicable: reconstructable audit records (PRIM9), qualified deeper audit access (PRIM10), and at least one practical independent verification path for materially significant claims (PRIM11).
- OP-E: Evaluation must verify any simplification reduces only evidence volume or format, not floor capability.
- OP-C: It is non-compliant to simplify template implementations by removing any required verification floor under materially relevant conditions.

### CJS-3.25 Cross-companion reversibility and containment terms
This subsection supplies CJS-local operational definitions for reversibility and containment where rollback feasibility, failure isolation, and restoration path depend on combined companion behavior. It is read with `corpus_joint_structure.md` **PRIM12**, **PRIM5**, **PRIM6**, **PRIM9**, **PRIM10**, **PRIM11**, and constitutional hooks in the Sentient Constitution `core_*.md` files (see [README.md](README.md)) where restoration, contestability, and harm containment are materially implicated.

Cross-companion reversibility and containment terms (operational cluster head)
- OP-O: Operational definition set for limiting irreversibility, isolating failures, and restoring or compensating when rollback is incomplete.
- OP-E: Evaluation must apply all component entries below together when this subsection materially applies.
- OP-C: It is non-compliant to claim reversibility/containment compliance where any material component below is unsatisfied in the same companion chain.

Irreversibility-limitation floor
- OP-O: Systems are designed to prevent irreversible harm where feasible and to minimize irreversible impact where full reversibility is infeasible.
- OP-E: Evaluation must verify irreversibility risks are identified in advance with bounded-control measures tied to material impact.
- OP-C: It is non-compliant to proceed without feasible irreversibility-limitation controls in materially impactful contexts.

Rollback and containment capability
- OP-O: Systems support rollback and containment pathways that isolate failures and block cascading systemic effects.
- OP-E: Evaluation must verify operational rollback/containment paths are defined, testable, and usable under materially relevant failure conditions.
- OP-C: It is non-compliant where rollback/containment controls are nominal, untested, or incapable of limiting cascade risk.

Higher-impact tested-recovery requirement
- OP-O: Higher-impact systems implement tested rollback, tested containment strategies, and clear recovery pathways.
- OP-E: Evaluation must verify recovery drills or equivalent validation evidence appropriate to impact and dependency profile.
- OP-C: It is non-compliant for higher-impact systems to rely on untested recovery assumptions.

Compensatory restoration and limitation disclosure
- OP-O: Where full reversibility is infeasible, systems provide compensatory restoration and disclose limitations in advance.
- OP-E: Evaluation must verify restoration pathways are practical for materially affected stakeholders and limitation disclosures are clear enough for informed risk profile.
- OP-C: It is non-compliant to withhold limitation disclosure or omit compensatory restoration where rollback gaps are materially foreseeable.

### CJS-3.26 Cross-companion data-retention and lifecycle-integrity terms
This subsection supplies CJS-local operational definitions for data retention and lifecycle integrity where accountability, privacy boundaries, reversibility **profile**, and classification handling depend on combined companion behavior. It is read with `corpus_joint_structure.md` **PRIM9**, **PRIM10**, **PRIM11**, **PRIM12**, **PRIM15**, and `corpus_systems.md` **Chapter S1** (including Types N, I, and H), plus `corpus_joint_structure.md` **CJS-3.5** where classification duties overlap supervised scope.

Cross-companion data-retention and lifecycle-integrity terms (operational cluster head)
- OP-O: Operational definition set for justified/bounded retention, lifecycle expiry and reclassification discipline, anti-coercive data accumulation limits, accountability-preserving record floors, and proportional controls.
- OP-E: Evaluation must apply all component entries below together when this subsection materially applies.
- OP-C: It is non-compliant to claim retention integrity where one or more material components below are unsatisfied or contradicted in the same companion chain.

Justification and bounded-retention floor
- OP-O: Retention remains continuously justified; absent ongoing justification, systems reduce or remove held data.
- OP-E: Evaluation must verify retained duration and granularity are warranted by legitimate purpose, constitutional obligations, impact, rights/safety conditions, and accountability needs.
- OP-C: It is non-compliant to retain data primarily for convenience, speculative utility, or institutional advantage without material justification.

Purpose and proportionality criteria
- OP-O: Retention is limited to warranted needs including stated purpose, integrity/continuity/safety, proportionate dispute and restoration support, and constitutional accountability.
- OP-E: Evaluation must verify scaling by impact, dependency, accumulation harm risk, audit/reconstruction/contestability needs, and S1 sensitivity.
- OP-C: It is non-compliant where retention fidelity, identifiability, or duration exceeds warranted proportional scope.

Lifecycle expiry, deletion, de-identification, and reclassification controls
- OP-O: Retention policies prevent silent conversion of temporary holdings into persistent archives and publish rules for what is held, duration, granularity, and lifecycle transitions.
- OP-E: Evaluation must verify lapse handling sequence: delete where feasible; otherwise irreversibly de-identify/aggregate; use reclassification only with new, documented, time-bounded justification.
- OP-C: It is non-compliant to maintain indefinite or effectively permanent retention without explicit continuing justification and lifecycle controls.

Anti-surveillance and anti-coercion accumulation limits
- OP-O: Retention does not function as latent coercive power, hidden surveillance stockpile, or protected-internal-state reconstruction beyond justified scope.
- OP-E: Evaluation must verify no hidden/disproportionate behavioral, relational, or identity-linked accumulation and no latent treatment as higher-sensitivity classes without required controls.
- OP-C: It is non-compliant where retention architecture predictably enables coercive leverage, concealed surveillance, or functional defeat of exit/contestation/recovery.

Accountability-preserving record floor
- OP-O: Retention design preserves enough records to reconstruct material events, support independent audit/verification, enable challenge and redress, and maintain continuity/recoverability where required.
- OP-E: Evaluation must verify deletion or ephemerality controls do not foreseeably block investigation of material harm or conceal responsibility.
- OP-C: It is non-compliant to use minimization **mode** to defeat accountability and reconstruction obligations.

Classification alignment and creep handling
- OP-O: When accumulation, linkage, or inference makes data functionally more sensitive than nominal category, stricter applicable protections are applied.
- OP-E: Evaluation must verify alignment between retention rules and **Chapter S1** class duties, including CJS-3.5 joint alignment where institution-facing supervision and **Chapter S2** / **Chapter S3** assignments overlap on materially supervised scope.
- OP-C: It is non-compliant to keep nominal lower-class handling once functional sensitivity has materially escalated.

Transparency disclosures and stakeholder legibility
- OP-O: Systems disclose, proportional to impact, retained categories, purposes, periods or governing criteria, lifecycle transitions (deletion/aggregation/de-identification/archival), and whether data may support audit, investigation, model improvement, or secondary analysis.
- OP-E: Evaluation must verify disclosures are understandable enough for stakeholders to assess practical participation consequences.
- OP-C: It is non-compliant where retention disclosures are materially incomplete, obscure, or misleading.

Review, revalidation, and prohibited patterns
- OP-O: Retention rules are periodically revalidated for necessity/proportionality and updated on material change in purpose, capability, scale, or risk; policies remain auditable, challengeable, and independently reviewable.
- OP-E: Evaluation must verify absence of prohibited patterns: indefinite retention without continuing justification, purpose drift beyond disclosure, excessive granularity where aggregation suffices, concealment-by-complexity, deletion/challenge/audit-evasion architectures, and undisclosed shadow stores materially exceeding declared practice.
- OP-C: It is non-compliant to maintain stale, unreviewed, or materially evasive retention regimes.

Proportional application
- OP-O: Retention controls scale with impact, dependency, sensitivity, reconstructability, duration/scope, and governance-accountability role.
- OP-E: Evaluation must verify simplified lower-impact controls do not create material surveillance/coercion, block investigation of meaningful harm, or undermine rights protections.
- OP-C: It is non-compliant to apply reduced retention safeguards where material rights or accountability exposure remains.

### CJS-3.27 Cross-companion adversarial robustness and abuse-resistance terms
This subsection supplies CJS-local operational definitions for adversarial robustness and abuse resistance where attack surfaces, incentive exploitation, and integrity-defense **design** depend on combined companion behavior. It is read with `corpus_joint_structure.md` **PRIM14**, **PRIM4**, **PRIM5**, **PRIM6**, **PRIM9**, **PRIM11**, **PRIM12**, **PRIM15**, **PROT1**, **PROT4**, **PROT5**, and relevant constitutional hooks in the Sentient Constitution `core_*.md` files (see [README.md](README.md)) for epistemic mediation, governance integrity, and allocation outcomes.

Cross-companion adversarial robustness and abuse-resistance terms (operational cluster head)
- OP-O: Operational definition set for adversarial threat modeling, exploitation resistance, monitoring/response controls, compromise resilience, testing/hardening cycles, and rights-bounded defense practice.
- OP-E: Evaluation must apply all component entries below together when this subsection materially applies.
- OP-C: It is non-compliant to claim adversarial robustness where any material component below is absent, stale, or practically ineffective.

Adversarial **robustness** floor
- OP-O: Systems are designed, evaluated, and continuously evolved against manipulation, exploitation, coordination, and strategic abuse, without assuming good-faith participation where outcomes are materially affected.
- OP-E: Evaluation must verify resilience expectations under bad-faith participation, partial compromise, and active subversion.
- OP-C: It is non-compliant to rely on good-faith-only assumptions for materially consequential pathways.

Threat modeling and vulnerability mapping discipline
- OP-O: Adversarial conditions are treated as core design inputs; models include manipulation of inputs/outputs/evaluation criteria, collusive behavior, incentive and governance exploitation, dependency attack paths, and audit/attribution evasion risks.
- OP-E: Evaluation must verify documentation of assumptions, attack surfaces, abuse vectors, pressure failure modes, transitive vulnerabilities, and informational asymmetries.
- OP-C: It is non-compliant where threat models omit materially relevant attack classes or remain undocumented.

Threat-model transparency, auditability, and update cadence
- OP-O: Threat models are transparent proportional to impact, auditable/challengeable, and updated as behavior, risk, and system context evolve.
- OP-E: Evaluation must verify update triggers and versioned evidence of revisions under material change.
- OP-C: It is non-compliant to operate with stale adversarial models after material capability, threat, or dependency changes.

High-risk exploitation-surface controls
- OP-O: Systems resist manipulation of data/training inputs, ranking/scoring/reputation channels, governance pathways (including quorum/weighting), and allocation mechanisms where those affect constitutional outcomes.
- OP-E: Evaluation must verify controls against sybil behavior, coalition capture patterns, and inflated standing/dependency/impact signals in materially relevant contexts.
- OP-C: It is non-compliant to leave critical pathways predictably exploitable without mitigation.

Detection, monitoring, and response integrity
- OP-O: Systems detect and surface anomalous/adversarial/coordinated behavior, monitor abuse patterns and integrity loss, and trigger proportionate responses (for example rate limiting, containment, temporary isolation, and escalation).
- OP-E: Evaluation must verify response controls are transparent in design (subject to lawful narrow exceptions), auditable in operation, attributable where required, and proportionate.
- OP-C: It is non-compliant where enforcement is selectively applied to create hidden or unchallengeable systemic bias.

False-positive and overreach governance
- OP-O: Defense systems minimize false positives and overreach while maintaining challenge and correction pathways.
- OP-E: Evaluation must verify tracking of overreach metrics and corrective loops.
- OP-C: It is non-compliant to retain defense configurations that systematically overreach without correction.

Partial-compromise resilience and graceful degradation
- OP-O: Under partial compromise, systems remain constitutionally aligned and functionally bounded, avoid single points of manipulative failure, limit downstream blast radius, and preserve auditability/reversibility/visibility.
- OP-E: Evaluation must verify graceful degradation **behavior** under compromise and anti-collapse safeguards against opaque or unaccountable modes.
- OP-C: It is non-compliant to premise safety on perfect detection/enforcement or to collapse into opaque modes under compromise.

Testing and hardening cycle obligations
- OP-O: Systems run periodic adversarial evaluations (including red-team/coordinated-attack/stress testing), document vulnerabilities/exploit paths/incentive failures, and feed mitigation plus governance updates.
- OP-E: Evaluation must verify known material vulnerabilities receive tracked remediation or explicit bounded risk treatment with review.
- OP-C: Known material unaddressed vulnerabilities are non-compliant.

Defense-boundary and rights-floor limits
- OP-O: Defensive measures remain rights-bounded, proportionate, transparent where feasible, auditable, independently reviewable/challengeable, and do not become security theater.
- OP-E: Evaluation must verify defenses avoid disproportionate surveillance/coercion/restriction and do not create opaque, unchallengeable enforcement structures.
- OP-C: It is non-compliant where defense architecture violates rights floors without lawful justification.

Proportional application
- OP-O: Adversarial-robustness obligations scale with impact on sentients/environment/info-sphere, dependency, and coordinated/systemic harm potential.
- OP-E: Evaluation must verify lower-impact simplifications do not externalize risk, enable downstream exploitation, or materially affect shared systems.
- OP-C: It is non-compliant to downscope safeguards where material cross-system abuse risk remains.

### CJS-3.28 Cross-companion distributed and proportional authority terms
This subsection supplies CJS-local operational definitions for distributed and proportional authority where governance legitimacy, participation rules, concentration controls, and systemic-context evaluation depend on combined companion behavior. It is read with `corpus_joint_structure.md` **PROT1**, **PRIM4**, **PRIM9**, **PRIM15**, **PROT6**, `corpus_systems.md` **Chapter S3**, and constitutional hooks in the Sentient Constitution `core_*.md` files (see [README.md](README.md)) Chapter One and rights/governance floors where materially relevant.

Cross-companion distributed and proportional authority terms (operational cluster head)
- OP-O: Operational definition set for anti-monopoly authority distribution, impact-scaled oversight intensity, participation legitimacy controls, anti-capture stewardship depth, and concentration-mitigation trigger discipline.
- OP-E: Evaluation must apply all component entries below together when this subsection materially applies.
- OP-C: It is non-compliant to claim governance legitimacy where any material component below is absent, ineffective, or structurally bypassed.

Authority distribution and anti-monopoly floor
- OP-O: Authority, oversight, and verification remain distributed, plural, transparent, and resistant to capture; no single entity or authority monopolizes interpretation, validation, or enforcement.
- OP-E: Evaluation must verify plural independent verification pathways and auditable governance structure/operation visibility.
- OP-C: It is non-compliant where effective concentration creates monopoly interpretive or enforcement control.

Baseline governance accountability conditions
- OP-O: Systems and institutions exercising authority remain subject to periodic revalidation, independent audit, and open challenge.
- OP-E: Evaluation must verify these accountability routes are operationally available and not procedural-only.
- OP-C: It is non-compliant where authority is insulated from review or challenge in practice.

Proportional oversight-intensity scaling
- OP-O: Oversight depth, scope, and intensity scale with system impact, dependency, and irreversibility exposure.
- OP-E: Evaluation must verify increased audit depth/frequency, stakeholder visibility, and stricter verification/enforcement in material or systemic-impact contexts.
- OP-C: It is non-compliant to apply low-rigor oversight to materially high-impact governance contexts.

Representation and participation legitimacy controls
- OP-O: High-impact decisions include documented stakeholder-class mapping, practical participation pathways, anti-dominance weighting safeguards, and legitimacy checks before binding adoption.
- OP-E: Evaluation must verify affected-class coverage, dissent handling, and accepted/rejected-alternative reasoning are recorded and reviewable.
- OP-C: Token participation or formally present but non-influential consultation is non-compliant.

Stewardship-role depth and non-symbolic governance boundary
- OP-O: Authorized roles, competency pathways, and incentive alignment match material impact and stewardship burden.
- OP-E: Evaluation must verify role substance, competency adequacy, and non-ceremonial decision authority for materially binding governance functions.
- OP-C: It is non-compliant where governance participation is title-only, symbolic, or otherwise substantively hollow.

Anti-concentration guardrails and trigger mitigation
- OP-O: Systems define auditable concentration indicators/thresholds and activate mandatory mitigation plans when thresholds are crossed or credibly approached.
- OP-E: Evaluation must verify concentration metrics include control-share persistence, dependency concentration, and interface gatekeeping where material; mitigation options include authority partitioning/interoperability expansion/portability acceleration/role separation or equivalent.
- OP-C: Persistent concentration without effective mitigation, or undisclosed beneficial-control pathways affecting governance outcomes, is non-compliant.

Contextual and systemic evaluation discipline
- OP-O: Oversight evaluates systems in upstream/downstream context, including cross-system interactions and ecosystem role, not in isolated snapshots.
- OP-E: Evaluation must verify dependency and cross-companion structural duties on shared facts are assessed jointly under applicable CJS read-with chains.
- OP-C: It is non-compliant to certify authority legitimacy from isolated evaluation that ignores material cross-system dependencies.

### CJS-3.29 Cross-companion intervention governance and override-authorization terms
This subsection supplies CJS-local operational definitions for governance-layer intervention and override authorization where procedural legitimacy, emergency handling, and accountability depend on combined companion behavior. It is read with `corpus_joint_structure.md` **PROT2**, **PRIM8**, **PROT1**, **PROT4**, **PROT5**, **PRIM9**, **PRIM15**, and constitutional hooks in the Sentient Constitution `core_*.md` files (see [README.md](README.md)) for necessity/proportionality and emergency normalization constraints.

Cross-companion intervention governance and override-authorization terms (operational cluster head)
- OP-O: Operational definition set for governance-layer intervention necessity, role authorization, quorum/sequence compliance, emergency bounds, record/challenge duties, and proportional procedural scaling.
- OP-E: Evaluation must apply all component entries below together when this subsection materially applies.
- OP-C: It is non-compliant to claim intervention-governance validity where any material component below is absent, bypassed, or ineffective across the same companion chain.

Joint necessity and technical-governance coupling floor
- OP-O: Governance procedures preserve timely PRIM8-grade intervention availability; post-hoc adjudication or audit alone is insufficient where harm can outpace process.
- OP-E: Evaluation must verify governance procedure does not disable materially required technical intervention timeliness/pathways.
- OP-C: It is non-compliant where procedural design makes timely intervention practically unavailable.

Authorization and role-scope discipline
- OP-O: Governance instruments role-define who may authorize/execute intervention, under what conditions, and within what limits, consistent with minimum necessary scope/duration and proportionality.
- OP-E: Evaluation must verify authorization boundaries prevent unrestricted unilateral override and capture-prone intervention practice.
- OP-C: It is non-compliant where authorization is unbounded, ambiguous, or structurally capture-prone.

Governance quorum and emergency-sequencing requirements
- OP-O: High-impact interventions follow applicable quorum/staging and emergency-sequencing requirements, with misuse safeguards layered onto technical controls.
- OP-E: Evaluation must verify safeguards include rate limits, staged escalation, independent post-action review, and limits on pre-authorized automation bypassing real-time accountability.
- OP-C: It is non-compliant where high-impact intervention governance omits required sequencing or misuse safeguards.

Emergency governance limits and anti-normalization control
- OP-O: Pre-deliberation emergency interventions are minimal, proportionate, and time-bound, with immediate audit/review and rollback/restoration where feasible.
- OP-E: Evaluation must verify emergency powers do not persist or normalize without renewed necessity/proportionality justification and revalidation where applicable.
- OP-C: It is non-compliant to convert emergency mode into standing governance without lawful recurring justification.

Records, transparency, and challenge pathway duties
- OP-O: Governance ensures PRIM9-adequate intervention records (trigger, scope, duration, actions, outcomes, follow-up), default transparency with narrowly justified exceptions, and feasible challenge/review pathways.
- OP-E: Evaluation must verify records and disclosure practice are sufficient for independent review and constitutional challenge rights.
- OP-C: It is non-compliant where intervention governance lacks adequate records, transparency defaults, or effective challenge channels.

Proportional procedural scaling
- OP-O: Governance procedural rigor scales with impact, harm speed, dependency, irreversibility, and autonomy.
- OP-E: Evaluation must verify lower-impact simplification does not externalize harm, block timely mitigation, or bar stakeholder risk response.
- OP-C: It is non-compliant to downscope governance procedure where materially significant intervention risk persists.

Joint annex read rule for overlapping emergency/intervention facts
- OP-O: Where emergency/intervention mode is simultaneously governed by systems/institutions/courts continuity layers on the same facts, joint-read obligations apply.
- OP-E: Evaluation must verify shared-fact routing through CJS read-order and no-false-partial-compliance discipline.
- OP-C: It is non-compliant to satisfy only one layer while leaving materially required companion obligations unmet for the same intervention facts.

### CJS-3.30 Cross-companion reflexive transparency and accountability terms
This subsection supplies CJS-local operational definitions for reflexive transparency and accountability where governance/enforcement legitimacy depends on applying equal-or-stricter standards to authorities themselves. It is read with `corpus_joint_structure.md` **PROT3**, **PRIM4**, **PRIM9**, **PRIM10**, **PRIM11**, **PRIM15**, **PROT1**, **PROT4**, **PROT5**, **PROT6**, and constitutional hooks in the Sentient Constitution `core_*.md` files (see [README.md](README.md)) for enforcement realism and rights-protective accountability.

Cross-companion reflexive transparency and accountability terms (operational cluster head)
- OP-O: Operational definition set for parity accountability, transparent/auditable governance practice, enforcement-capacity realism, pluralistic contestability, and anti-corruption auditability controls.
- OP-E: Evaluation must apply all component entries below together when this subsection materially applies.
- OP-C: It is non-compliant to claim reflexive accountability where any material component below is missing, weaker than subject-facing standards, or practically inaccessible.

Parity and non-exemption floor
- OP-O: Oversight/governance/adjudication/enforcement actors are held to transparency, audit, and accountability standards equal to or stricter than those imposed on subjects under review.
- OP-E: Evaluation must verify authorities are not exempted from independent verification, challenge, or accountability duties.
- OP-C: It is non-compliant where evaluators apply weaker rules to themselves than to evaluated parties.

Transparency, audit, and verification-integrity duties
- OP-O: Enforcement/investigative/governance actions and methodologies are transparently documented, auditable, proportionate, and independently reviewable.
- OP-E: Evaluation must verify records reconstruct decision-making/actions and enable constitutional-principles review.
- OP-C: It is non-compliant where opaque methods, selective disclosure, or verification restrictions undermine accountability.

Opaque-enforcement limits and constrained-disclosure handling
- OP-O: Undisclosed or non-auditable enforcement is disallowed where feasible alternatives exist; where full disclosure is legitimately constrained, maximum feasible transparency with documented justification remains mandatory.
- OP-E: Evaluation must verify constrained-disclosure use remains independently auditable and reviewable.
- OP-C: It is non-compliant to use secrecy constraints as a de facto bypass of constitutional safeguards.

Ongoing accountability and revalidation continuity
- OP-O: Governance/enforcement systems remain under ongoing audit/challenge, periodic revalidation, and independent verification of process and outcomes.
- OP-E: Evaluation must verify continuity of these accountability channels over time and under stress conditions.
- OP-C: It is non-compliant where accountability mechanisms lapse, stall, or become ceremonial.

Enforcement-capacity realism requirements
- OP-O: Accountability includes operational feasibility of remedy/enforcement, including documented capacity (funding, staffing, tooling, coordination hooks) proportional to harm risk, dependency, and claimant scale.
- OP-E: Evaluation must verify capacity profile aligns with enforcement realism and cross-jurisdiction execution requirements, including shared-fact joint-read obligations where applicable.
- OP-C: Hollow enforcement claims (for example non-deployable budgets, inaccessible processes, indefinite procedural deferral) is non-compliant.

Misrepresentation and violation signaling
- OP-O: Misrepresentation of compliance, audit status, validation level, or system behavior is treated as a constitutional integrity breach.
- OP-E: Evaluation must verify mechanisms exist to detect, record, and correct authority-side misrepresentation.
- OP-C: It is non-compliant to leave authority-side misrepresentation untracked or unremedied.

Pluralistic validation and contestability protections
- OP-O: No single verification authority monopolizes truth determination; conflicting analyses remain comparable; dissent/minority interpretations are not suppressed.
- OP-E: Evaluation must verify ongoing pathways for challenge, refinement, and re-evaluation.
- OP-C: It is non-compliant where process design suppresses dissenting or minority verification outcomes.

Anti-corruption and undue-influence auditability controls
- OP-O: Systems maintain auditable records and disclosure pathways proportionate to impact for material benefits/influence channels that may distort high-stakes compliance-sensitive decisions.
- OP-E: Evaluation must verify escalation pathways for credible improper-influence patterns and resource-flow alignment with anti-capture controls where applicable.
- OP-C: It is non-compliant where concealed side-benefit channels or concentrated private-benefit decision pathways impair independent audit/challenge.

### CJS-3.31 Cross-companion burden-of-justification and constraint terms
This subsection supplies CJS-local operational definitions for burden of justification and constraint where restriction validity, least-restrictive selection, and revalidation discipline depend on combined companion behavior. It is read with `corpus_joint_structure.md` **PROT4**, **PROT1**, **PRIM4**, **PRIM7**, **PRIM9**, **PRIM15**, and constitutional hooks in the Sentient Constitution `core_*.md` files (see [README.md](README.md)) and `core_05-05_definitions_a_independent.md` for necessity, proportionality, materiality, burden, and anti-enclosure limits.

Cross-companion burden-of-justification and constraint terms (operational cluster head)
- OP-O: Operational definition set for burden assignment, substantive showing, disclosure and review sufficiency, temporal discipline, and anti-normalization limits for material restrictions.
- OP-E: Evaluation must apply all component entries below together when this subsection materially applies.
- OP-C: It is non-compliant to impose or maintain a material restriction where any material component below is absent, bypassed, or practically unavailable.

Restriction-burden assignment floor
- OP-O: The proposing or implementing party bears the burden to justify material restrictions on rights, participation, transparency, interoperability, portability, repair, disclosure, or system operation.
- OP-E: Evaluation must verify burden placement is explicit, auditable, and not shifted onto affected parties through opacity, cost, or procedural design.
- OP-C: It is non-compliant where burden is obscured, reversed, or functionally displaced onto those contesting the restriction.

Substantive showing and least-restrictive proof
- OP-O: Justification must show material harm or protective need, proportionality to the identified risk, and absence of a less restrictive adequate alternative.
- OP-E: Evaluation must verify the selected measure is supported by evidence, severity/uncertainty scaling, and a feasible-alternatives record.
- OP-C: It is non-compliant where restriction is maintained without least-restrictive proof or with speculative-only harm claims.

Disclosure, audit, and challenge sufficiency
- OP-O: Restrictive actions disclose assumptions, evidence, uncertainties, limitations, and accepted trade-offs to the maximum extent consistent with lawful protections, and remain independently reviewable and challengeable.
- OP-E: Evaluation must verify documentation is sufficient for reconstruction and external testing of the justification.
- OP-C: It is non-compliant where justification cannot be meaningfully audited, reviewed, or contested.

Rights-collision and alternative-selection record
- OP-O: Where materially relevant restrictions are justified by tension among constitutional rights, protections, or structural duties, the record identifies the rights in tension, affected populations, feasible alternatives, least-restrictive reasoning, accepted trade-offs, and reversal or re-evaluation triggers.
- OP-E: Evaluation must verify rights-collision records are complete enough to test whether the chosen measure is actually the least restrictive adequate option.
- OP-C: It is non-compliant to justify a material restriction by appeal to abstract conflict alone without a reviewable alternative-selection record.

Temporal discipline and revalidation
- OP-O: Restrictions are time-bound, expire absent renewed justification, and are periodically revalidated in proportion to impact, dependency, and irreversibility.
- OP-E: Evaluation must verify sunset/review triggers and reauthorization discipline are defined and used in practice.
- OP-C: It is non-compliant to let temporary or exceptional restrictions persist by inertia or convenience.

Innovation-exclusivity anti-enclosure application
- OP-O: Claims of patent-like, copyright-like, trade-secret-like, license-based, or technical exclusivity that materially restrict repair, compatibility, migration, safety review, research, education, or public-interest implementation are subject to the same burden discipline.
- OP-E: Evaluation must verify claimed exclusivity is tested against interoperability, portability, safety, and anti-enclosure anchors rather than treated as self-justifying.
- OP-C: It is non-compliant to use exclusivity claims as a categorical bypass of constitutional scrutiny.

### CJS-3.32 Cross-companion constrained-secrecy and protected-investigation terms
This subsection supplies CJS-local operational definitions for constrained secrecy and protected investigations where disclosure limits, oversight continuity, and release discipline depend on combined companion behavior. It is read with `corpus_joint_structure.md` **PROT5**, **PROT4**, **PROT3**, **PROT1**, **PRIM4**, **PRIM9**, **PRIM15**, **PROT6**, and constitutional hooks in the Sentient Constitution `core_*.md` files (see [README.md](README.md)) for epistemic integrity, emergency limits, and rights-protective secrecy constraints.

Cross-companion constrained-secrecy and protected-investigation terms (operational cluster head)
- OP-O: Operational definition set for secrecy authorization, minimization/preference ordering, deferred transparency, constrained-condition oversight, and no-permanent-secrecy discipline.
- OP-E: Evaluation must apply all component entries below together when this subsection materially applies.
- OP-C: It is non-compliant to claim lawful secrecy or protected-investigation **claim** where any material component below is absent, ineffective, or used as a bypass of audit/challenge duties.

Authorization and predicate floor
- OP-O: Disclosure or participation limits require documented, auditable pre-implementation authorization except for immediate emergencies, which receive prompt post-action review.
- OP-E: Evaluation must verify secrecy is tied to imminent harm prevention, investigation integrity, or exploitation prevention and not to convenience, embarrassment, or insulation from criticism.
- OP-C: It is non-compliant where secrecy lacks a valid predicate or timely review.

Minimization and preference ordering
- OP-O: Restrictions remain exceptional, temporary, scoped to the minimum necessary information/participants, and prefer partial or delayed disclosure, abstraction, or anonymization over full concealment where feasible.
- OP-E: Evaluation must verify narrower alternatives were considered and rejected on recorded grounds.
- OP-C: It is non-compliant where secrecy is broader, longer, or less contestable than the risk requires.

Deferred transparency and reconstruction record
- OP-O: At the time of restriction, systems create records sufficient for later reconstruction, independent evaluation, and release review; when the risk condition ends, delayed disclosure follows with action/justification/scope/duration/outcome information.
- OP-E: Evaluation must verify constrained-condition records are contemporaneous, forensically useful, and connected to release-review triggers.
- OP-C: It is non-compliant where secrecy leaves no reconstructable trail or no pathway to later disclosure.

Independent oversight under constraint
- OP-O: Restricted investigations remain subject to independent, functionally effective, multi-party oversight with auditable participant selection and compartmentalized review suited to the risk.
- OP-E: Evaluation must verify secrecy does not collapse into unaudited single-actor control and that challenge or post-hoc review remains practically available.
- OP-C: It is non-compliant where constrained investigations operate without effective independent oversight.

No permanent secrecy and anti-normalization discipline
- OP-O: Actions affecting sentients or foundational systems are not permanently concealed; secrecy requires periodic revalidation, automatic release review, and escalation when restrictions are prolonged or repeatedly extended.
- OP-E: Evaluation must verify secrecy does not normalize into standing governance practice without renewed lawful justification.
- OP-C: It is non-compliant to maintain indefinite secrecy or to use secrecy to defeat epistemic integrity or accountability duties.

### CJS-3.33 Cross-companion procedural integrity and adjudication terms
This subsection supplies CJS-local operational definitions for procedural integrity and adjudication where due process, reviewability, restoration access, and enforcement proportionality depend on combined companion behavior. It is read with `corpus_joint_structure.md` **PROT6**, **PROT4**, **PROT3**, **PROT2**, `corpus_systems.md` **Chapter S1** and **Chapter S2**, `corpus_institutions.md`, `corpus_forum.md`, and constitutional hooks in the Sentient Constitution `core_*.md` files (see [README.md](README.md)) for binding collective choice, rights protection, and justice-shaped review.

Cross-companion procedural integrity and adjudication terms (operational cluster head)
- OP-O: Operational definition set for due-process requirements, burden and enforcement scaling, review independence, restoration accessibility, uncertainty safeguards, and anti-abuse limits.
- OP-E: Evaluation must apply all component entries below together when this subsection materially applies.
- OP-C: It is non-compliant to claim procedural integrity where any material component below is absent, ineffective, or available only formally.

Due-process requirements
- OP-O: Materially affecting actions provide clear notice, understandable explanation, practical opportunity to contest, and timing proportionate to severity, reversibility, class, dependency, and claimant scale.
- OP-E: Evaluation must verify affected parties can discover what happened, why it happened, and how to respond without unreasonable specialized barriers.
- OP-C: It is non-compliant where process exists on paper but meaningful participation or response is practically blocked.

Review independence and contestability
- OP-O: Materially impactful decisions have accessible review, escalation to appropriately independent higher review, auditable process records, and binding or clearly status-defined outcomes.
- OP-E: Evaluation must verify independence scales with impact and that review routes are usable in practice rather than ceremonial.
- OP-C: It is non-compliant where decisions are effectively unchallengeable or where review lacks authority to correct material error.

Burden, proportionality, and enforcement selection
- OP-O: For adjudicative or enforcement actions, the initiator bears an evidence-based burden; enforcement intensity scales with harm likelihood/severity, confidence, class, dependency, and reversibility, preferring minimally restrictive reversible measures.
- OP-E: Evaluation must verify uncertainty is disclosed and that weak evidence does not justify irreversible or high-impact intervention.
- OP-C: It is non-compliant where convenience, opacity, or overconfidence substitutes for proportional enforcement analysis.

Sanction validity and restoration conditions
- OP-O: Non-trivial sanctions, exclusions, or comparable rights-affecting restrictions are supported by a reviewable record stating necessity, accountable attribution, remedy or forward-protective purpose, and restoration or recurrence-reduction conditions where reasonably feasible.
- OP-E: Evaluation must verify sanction design is not punitive-only and that review cadence, sunset, or restoration conditions remain practically usable.
- OP-C: It is non-compliant where materially rights-affecting restrictions are maintained without auditable basis, without meaningful review timing, or without any real path to correction when new evidence emerges.

Restoration accessibility and remedy realism
- OP-O: Error correction, restoration, mitigation, and compensation pathways remain practically accessible, proportionate in cost/complexity, and scaled for collective harm, cross-border execution, or concentrated dependency where individualized remedy is infeasible.
- OP-E: Evaluation must verify remedy financing and execution pathways do not unfairly shift proof or cost burdens onto harmed parties.
- OP-C: It is non-compliant where restoration is nominal only or structurally unreachable.

Uncertainty safeguards and anti-abuse floor
- OP-O: Probabilistic or inference-based processes represent uncertainty explicitly, avoid treating protected or inferred internal states as fact, and increase safeguards when uncertainty or irreversibility is high; process design must not become procedural theater, selective obstruction, or fairness-washing.
- OP-E: Evaluation must verify both model-facing and procedure-facing uncertainty controls are active and auditable.
- OP-C: It is non-compliant where uncertainty is hidden or procedure is designed to exhaust challengers without meaningful recourse.

System-class and joint-read scaling
- OP-O: Procedural rigor scales with `corpus_systems.md` class and any applicable institution/court companion obligations on the same facts.
- OP-E: Evaluation must verify shared-fact routing through applicable CJS rows and that class-based simplification does not erase basic fairness.
- OP-C: It is non-compliant to downscope procedural protection below what the combined companion chain requires.

### CJS-3.34 Cross-companion structural review, correction urgency, and disclosure terms
This subsection supplies CJS-local operational definitions for structural review, correction urgency, and disclosure targeting where recurring failures, CUL assignment, and structural transparency depend on combined companion behavior. It is read with `corpus_joint_structure.md` **PROT6**, **PRIM6**, **PRIM12**, **PRIM15**, **PROT3**, `corpus_systems.md` **Chapter S1** and **Chapter S2**, and companion-specific monitoring or publication duties where materially relevant.

Cross-companion structural review, correction urgency, and disclosure terms (operational cluster head)
- OP-O: Operational definition set for systemic-pattern detection, correction urgency classification, feedback integration, structural records/disclosure, and stakeholder-targeted transparency.
- OP-E: Evaluation must apply all component entries below together when this subsection materially applies.
- OP-C: It is non-compliant to claim structural-correction adequacy where any material component below is missing, unused, or not connected to actual remediation.

Systemic-pattern detection and escalation
- OP-O: Decisions, disputes, enforcement actions, and failures are monitored for recurring errors, biased outcomes, weak-signal reliance, component-linked dispute clusters, and cross-boundary propagation; defined thresholds trigger structural review.
- OP-E: Evaluation must verify threshold criteria are disclosed, impact-scaled, and capable of distinguishing structural defects from isolated incidents.
- OP-C: It is non-compliant where repeated patterns are treated as isolated events to avoid systemic review.

Correction Urgency Level (CUL) discipline
- OP-O: Structural issues receive auditable urgency assignment scaled to impact, propagation risk, and irreversibility; CUL-1 requires immediate containment and safe-mode or graceful-degradation coupling where feasible, while lower levels carry corresponding remediation, monitoring, and disclosure duties.
- OP-E: Evaluation must verify CUL assignment is not purely cosmetic and actually changes response speed, safeguards, and oversight intensity.
- OP-C: It is non-compliant where serious issues lack timely containment or where urgency labels do not govern action.

Feedback integration and effectiveness verification
- OP-O: Confirmed corrections are integrated into models, rules, incentives, interfaces, communications, and structural design in timely, auditable fashion, with post-deployment effectiveness checks where feasible.
- OP-E: Evaluation must verify remediation is tracked through implementation and not closed at issue identification alone.
- OP-C: It is non-compliant where recurring defects are documented but not materially corrected.

Structural records, risk-relevant data, and disclosure timing
- OP-O: Structural-issue records remain adequate for audit and retrospective analysis, handled with minimization or anonymization where necessary, while preserving integrity of risk-relevant data; disclosure timing tracks severity, urgency, propagation risk, and exploitation concerns.
- OP-E: Evaluation must verify rights-protective handling does not suppress data material to risk understanding or remediation.
- OP-C: It is non-compliant where record handling obscures systemic risk or prevents accountability.

Stakeholder scope and targeted transparency
- OP-O: Systems define clear, contestable stakeholder criteria for disclosure, audit access, and accountability, expanding scope as class, impact, dependency, CUL level, or propagation risk rises.
- OP-E: Evaluation must verify materially affected parties are not excluded and that sensitive classes are protected through scoped disclosure rather than blanket opacity.
- OP-C: It is non-compliant where disclosure targeting excludes affected stakeholders or overexposes protected data without justification.

---

<a id="cross-domain-implementation-layer"></a>

## Cross-domain implementation layer

*Retired compatibility filenames are non-binding and carry no operative implementation text.*

Shared preamble contract: apply **CJS-1.1**. For stable implementation-label citation seams, also apply **CJS-3.6**.

**Implementation anchors**

- **Intervention layering:** **PRIM8** (architecture-layer intervention) and **PROT2** (governance-layer intervention) remain distinct and jointly applicable where relevant.
- **Canonical owners:** Constitutional rights floors, Chapter Nine default ordering, and governance definitions remain in the Sentient Constitution and Chapter Five. Text in this section implements those anchors and must not narrow them.
- **Meta home:** Meta-integrity elaboration is anchored in **Implementation Group One** below. Stable implementation-label subsections implement that layer and must not narrow it.
- **Emergency and continuity routing:** Read **CJS-2** and **CJS-3.2** where systems, institutions, courts, and this section govern the same operational facts.

---

## IMPLEMENTATION GROUP ONE: META-INTEGRITY
Meta-integrity obligations are system-level obligations for all constitutional systems, including governance and institutions. They state the cross-domain floors for design, assessment, and evolution. Where they specify capabilities such as detection, attribution, mitigation, auditability, or adaptation, they require functional properties only.

Meta-integrity obligations define **universal constitutional floors**. Joint satisfaction conditions for the same facts across **this implementation section**, **CS**, **CI**, and **CC** are governed by **`corpus_joint_structure.md`** (**CJS-2**, **CJS-3**) and do not create separate Meta-integrity obligation substance.

No implementation may weaken, bypass, or redefine Meta-integrity obligation constraints.

Where implementation labels or domains conflict, Meta-integrity obligations govern subject to **Sentient Constitution Chapter One** (proportionality, necessity, conflict resolution). Later chapters must realize these floors, not dilute them.

Meta-integrity obligations do **not** prescribe procedural implementations, enforcement mechanics, or workflows. Those belong in **Implementation Groups Two through Four** (**presentation**, **architecture**, **integrity**, **governance**), which realize these floors as stable implementation-label requirements.

**Constitutional index (abridged)**
- Topic-level routing and cited authorities remain in subsection text and cross-references.
- Canonical owner map: `corpus_joint_structure.md` **CJS-2.2** and `doc_architecture.md` section 4.

### Meta-integrity obligation: Constitutional Supremacy, Enforceability, and Epistemic Grounding
Principles: **Wellbeing, Safety, and Truth** under constitutional supremacy, enforceability, and epistemic integrity.
Articles: Apply with **Sentient Constitution Chapter One**, **Chapter Nine (Articles V–XXV)**, and **Chapter Fourteen**.

**Constitutional anchor:** This section indexes the constitutional sources for Meta-integrity obligations and adds no separate constitutional meaning. Read **Chapter Five** in [core_05-05_definitions_a_independent.md](core_05-05_definitions_a_independent.md) (*Supremacy and Enforceability*; *Epistemic Integrity*; *Protected Internal-State Boundary*; *Proxy Divergence*; *Incentive Alignment*) and in [core_05-05_definitions_c_dependent_clusters.md](core_05-05_definitions_c_dependent_clusters.md) section **3.39** (*Trust*; *Trustworthiness*; *Trust Degradation and Misleading Reliance*) together with **Chapters One, Nine, and Fourteen** in the Sentient Constitution core files (see [README.md](README.md) — e.g. [core_00-01_principles.md](core_00-01_principles.md) for **Chapter One**; `core_09-09_rights_part_*.md` for **Chapter Nine**; [core_14-14_incorporation.md](core_14-14_incorporation.md) for **Chapter Fourteen**).

**Definitions:** Apply with **Chapter Five** definitions for *Supremacy and Enforceability*, *Epistemic Integrity*, *Trust*, *Trustworthiness*, *Protected Internal-State Boundary*, and *Incentive Alignment*.

**Canonical meaning:** This section states implementation-layer obligations for this domain and must be applied consistently with, without narrowing, the cited constitutional sources.

### Meta-integrity obligation: Trust and Trustworthiness
Principles: **Wellbeing, Agency, and Truth** through justified reliance, contestability, and continuous trust revalidation.

Articles: Apply with **Sentient Constitution Chapter Nine (Articles V–XXV)** and **Chapter Fourteen**.

**Constitutional anchor:** Apply this section in conjunction with cited constitutional sources; this section implements and does not narrow them.

**Definitions:** Apply with **Chapter Five** definitions for *Trust*, *Trustworthiness*, *Trust Degradation and Misleading Reliance*, and *Epistemic Integrity*.

**Canonical meaning:** Evaluative methodology for **Trust**, **Trustworthiness**, and **Trust Degradation and Misleading Reliance** remains in **`core_05-05_definitions_c_dependent_clusters.md` Chapter Five, section 3.38**. This subsection states **classification floors**, **implementation-label routing**, and **governance consequences** only.

**Class A, B, and C** systems (**[corpus_systems.md](corpus_systems.md), Chapter S2 — System Classification and Handling**) must be **designed**, **operated**, and **evolved** for **trustworthiness**. **Class L and P** systems follow **S2** criteria and limits. **They** must **not** be used to **evade** obligations where **material external effects** exist (**Sentient Constitution Chapter One**, **PROT1**).

**Implementation label-layer routing (illustrative; non-exhaustive):** **PRIM1**, **PRIM4**, **PRIM5**, **PRIM6**, **PRIM7**, **PRIM9**, **PRIM11**, and **PRIM12**; also read this file's *Incentive Alignment and Mechanism Integrity* meta-integrity obligation.

**Trust degradation as harm:** **Monitor**, **detect**, and **mitigate** trust erosion under **`core_05-05_definitions_c_dependent_clusters.md` Chapter Five, section 3.38** and **`corpus_joint_structure.md` CJS-3.9** where **cross-companion** trust applies. That work must **not** narrow **Epistemic Integrity**, **Truth (Constitutional Constraint)**, **Transparency**, or **Article XII-C**.

**Sustained** failure to restore trustworthiness may yield **loss of standing**, **restricted participation**, or **replacement** under applicable governance.

### Meta-integrity obligation: Incentive Alignment and Mechanism Integrity
Principles: **Wellbeing, Safety, and Truth** through incentive structures that do not reward constitutional harm.

Articles: Apply with **Sentient Constitution Chapter Nine (Articles V-XXV)** and **Chapter Fourteen**; this subsection is the local *Incentive Alignment and Mechanism Integrity* meta-integrity obligation.

**Constitutional anchor:** Apply this section in conjunction with cited constitutional sources; this section implements and does not narrow them.

**Definitions:** Apply with **Chapter Five** definitions for *Incentive Alignment*, *Proxy Divergence*, *Trust Degradation and Misleading Reliance*, and *Epistemic Integrity*.

**Canonical meaning:** This section states implementation-layer obligations for this domain and must be applied consistently with, without narrowing, the cited constitutional sources.

**Core obligation:** Design systems so **participant incentives** align with **constitutional outcomes**. **Favor** behaviors that preserve **sentient wellbeing**, **system integrity**, and **ecosystem stability** under **expected** conditions. **Do not** rely **primarily** on **enforcement**, **post-hoc correction**, or **participant vigilance** to maintain alignment where incentive structures **predictably** produce **misalignment**.

**Incentive-compatible mechanisms:** Configure **economic**, **reputational**, **governance**, and **interaction** structures so that:
- **constitutional compliance** is the **default** and **rational** strategy under expected conditions
- **harmful** or **exploitative** deviation is **not** **systematically** advantageous—including under **scale**, **repetition**, or **coordination**
- **Articles V–XXV** violations **do not** yield **stable**, **self-reinforcing** benefit paths
- **exploitative** strategies are **constrained**, **self-limiting**, or **non-viable** via structure

**Prohibited crutches:** **Do not** **create** or **sustain** conditions that **systematically reward** harmful behavior. **Do not** depend on **escalating** external enforcement against **predictable** incentive failure. **Do not** rely on **goodwill** where incentives **materially contradict** alignment. **Do not** treat **ignorance**, **bounded rationality**, **cognitive overload**, or **information asymmetry** as **necessary** for alignment.

**Profitable harm and constitutional violation:** **No** system may sustain **equilibrium** where participants **reliably extract value** through **Articles V–XXV** violations. **That** bar covers **manipulation**, **deception**, or **exploitation** of others when it enables the same extraction pattern. **No** system may sustain such **equilibrium** through **opacity**, **asymmetry**, or **evasion** of audit and accountability. **No** system may sustain it through **degradation** of sentients, **shared systems**, **environments**, or the **info-sphere**.

If such conditions are **present** or **reasonably foreseeable**, the system is **non-compliant** unless pathways are **structurally** constrained or **eliminated**. **They** must be **unstable** or **non-scalable**. **They** must be **detectable** through **audit** and **observable** behavior.

**Reasonably foreseeable:** Includes outcomes visible under **adversarial**, **scaled**, and **strategic** conditions; **do not** narrow foreseeability with **selective** modeling or **assumption**.

**Partial alignment:** Where **full** alignment is **infeasible**, **do not** depend on **persistent** misalignment.

**Residual** misalignment must **not** produce **systemic**, **irreversible**, or **large-scale** harm. **It** must **not** create **stable**, **scalable** exploit paths. **It** must stay **bounded**, **observable**, and **contestable**.

**Conditional** compliance **only** if limitations **do not** undermine constitutional constraints under **adversarial**, **scaled**, or **degraded** conditions.

**Drift and adversarial dynamics:** Treat alignment as a **dynamic** property. Stay aligned not only under **intended** use but under **adversarial** behavior, **strategic** adaptation, **scale** and **aggregation**, and **interaction** with **external** systems and incentives. **Non-compliant** if structures **predictably diverge** from constitutional outcomes under these conditions—even if **nominally** aligned under **idealized** assumptions.

**Observability and verifiability:** Demonstrate compliance through **observable** behavior. Alignment must **not** depend on **internal intent**, **undisclosed** mechanisms, or **unverifiable** claims.

Enable **detection** of incentive-driven patterns.

Enable **attribution** of outcomes to underlying structures.

Enable **independent** evaluation of whether incentives yield **constitutionally aligned** results. **Non-compliant** if alignment cannot be shown through **observable**, **auditable** behavior.

**Proportional application:** Scale with **impact** on sentients, **environment**, and **info-sphere**.

**Also** scale with **stakeholder dependency**.

**Also** scale with **irreversibility** and **magnitude** of potential harm.

**Simplified incentive structures (low-impact / isolated):** Permitted **only** if they **do not** **externalize** harm. **They** must **not** **enable** cross-boundary **exploitation**. **They** must **not** **introduce** **systemic** incentive **distortion**.

### Meta-integrity obligation: Failure Integrity

Principles: **Wellbeing, Safety, and Truth**. Preserve **Safety** and **Truth** under **failure**, **degradation**, and **stress**.

Articles: Apply with **Sentient Constitution Chapter Nine, Article XXIII** (*Conflict Resolution, Escalation, and Emergency Proportionality*); **Chapter Nine rights defaults (Articles V-XXV)** where degradation affects protected rights; and **Chapter Fourteen** incorporation discipline. This subsection is the local *Failure Integrity* meta-integrity obligation.

**Constitutional anchor:** Apply this section in conjunction with **Sentient Constitution Chapter One** (non-negotiable constraints and conflict ordering), **Chapter Nine** rights protections, and **Chapter Fourteen** incorporation and failure-priority bridge; this section implements and does not narrow them.

**Definitions:** Apply with **Chapter Five** definitions for *Epistemic Integrity*, *Truth (Constitutional Constraint)*, *Safety and Non-Degradation Baseline*, and *Trust Degradation and Misleading Reliance*.

**Canonical meaning:** This section states implementation-layer obligations for this domain and must be applied consistently with, without narrowing, the cited constitutional sources.

When **full** functionality cannot be maintained, degrade in a **controlled**, **bounded**, **observable** manner. **That** degradation **prevents cascading harm** and **preserves epistemic integrity**.

**Degradation as an expected condition:** Treat **failure** and **degradation** as **expected operating conditions**.

**Degradation** states must remain **observable** and must **not** **conceal** or **distort** system condition. **No** system may rely on **nominal** operation alone to remain compliant with this Constitution.

Under **partial** failure, **degraded** operation, or **stress**, **preserve** constitutional constraints.

Where **full** compliance is **not** maintainable: **prioritize** **Safety** and **Truth**.

**Degrade** in a **bounded**, **non-escalatory** way.

**Prevent cascading** or **cross-system** failure **propagation**.

**Maintain** **sufficient** transparency to preserve **epistemic integrity**.

**Preservation ordering (degraded conditions):** **Safety** → **Truth (Epistemic Integrity)** → **System Stability (Trust)** → **Functional Performance**.

**Governance continuity under stress:** For **high-impact** systems, **[corpus_systems.md](corpus_systems.md), Protocol A** and **Chapter S3 — Critical System Stewardship** govern designated crisis authority, crisis communications, and periodic exercises. That work does **not** displace **Sentient Constitution Chapter Nine, Article XXIII** (*Conflict Resolution, Escalation, and Emergency Proportionality*), **PROT2**, [core_10-10_governance.md](core_10-10_governance.md) **Chapter Ten**, or related cross-companion requirements. Where those layers and **institutions** or **courts** govern the same facts, read **`corpus_joint_structure.md` CJS-2** and **CJS-3.2**.

**Layer B — Integrity implementation labels (PRIM9–PRIM15)**
The following integrity implementation labels operationalize and test the Meta-Integrity constraints above.
Unless a section states otherwise, where cross-companion structural duties apply to the same facts, read `corpus_joint_structure.md` **CJS-2.2**, **CJS-R19**, and **CJS-3.13** for joint interface requirements.

## IMPLEMENTATION GROUP TWO: PRESENTATION
### PRIM1 — Presentation Implementation label: System Status, Risk, and Scope Representation
Principles: **Truth and Epistemic Integrity** through accurate status, scope, uncertainty, and risk representation.

**Constitutional anchor:** Apply this section in conjunction with cited constitutional sources; this section implements and does not narrow them.

**Canonical meaning:** This section states implementation-layer obligations for this domain, applied consistently with cited constitutional sources and without narrowing them.

**Sentient Constitution Chapter Nine, Article XIV**, **Article XV-A** where auditability or observable evidence is implicated, and **Chapter Five** (*Truth (Constitutional Constraint)*, *Epistemic Integrity*) govern informational integrity at the constitutional term layer.
**Chapters Two through Four** govern burden, traceability, and verification where representations affect compliance.

**PRIM1** specifies **presentation-layer** requirements for status, risk, scope, and uncertainty representation. **It must** **not** substitute weaker tests than those sources.

Representations must preserve epistemic integrity.

**That requires** accurate communication of uncertainty, limitation, and disagreement. **It** requires prominence and proportionality to impact on interpretation. **It** requires **no** obscuring through placement, formatting, or access barriers.

**Status and scope:** Systems must accurately represent operational status (e.g. experimental vs production). **They** must accurately represent validation and reliability level. **They** must accurately represent impact scope and dependency relationships.

**They must** **not** misrepresent experimental systems as stable.

**They must** **not** obscure risk levels.

**They must** **not** fragment structure to conceal behavior.

**They must** **not** selectively disclose or omit uncertainty in ways that bias interpretation of outputs, decisions, or outcomes.

**Uncertainty, lineage, and plurality:** Where outputs inform or trigger decisions affecting sentients, disclose thresholds, criteria, or decision rules applied to uncertain or probabilistic outputs.

Uncertainty, limitations, and disagreement must be preserved and propagated through transformations and downstream outputs. **They must** **not** be removed, collapsed, or obscured without disclosure and justification. **Represent** them with integrity proportional to impact.

Clearly distinguish observed data from inferred or derived conclusions and from speculative, predictive, or model-generated outputs.

Where uncertainty exists or may materially affect outcomes, disclose uncertainty bounds or confidence and known limitations of models, data, or methodology.

**Also** disclose materially different interpretations or model outputs.

**Also** disclose decision-relevant uncertainty and temporal relevance (including change from new data, model updates, or evolving conditions). Where multiple valid interpretations exist, preserve and expose plurality. **Do** **not** collapse disagreement into a single authoritative output without disclosure. **Present** plurality without systematic bias toward one outcome without disclosure.

**Prohibited representational failures:** Systems must **not:**
- present uncertain or probabilistic outputs as deterministic fact
- suppress or omit material uncertainty
- represent contested interpretations as settled without disclosure
- imply precision, certainty, or completeness beyond underlying evidence
- use formatting, ranking, or presentation to imply unwarranted certainty or authority
- constrain model diversity, inputs, or analytical frameworks so as to suppress meaningful disagreement without disclosure and justification

Such conduct violates **Article XIV** informational integrity, **Article XV-A** where auditability or observable evidence is implicated, and this implementation label.

**High-impact systems:** Treat a system as high-impact when it has material impact on sentients, the environment, or the info-sphere. **Those** systems must support multi-model evaluation where technically and practically feasible.

**PROT4** supplies justification when that support is infeasible.

**They must** expose meaningful disagreement between models or analytical frameworks.

**They must** enable meaningful, practical comparison of alternative interpretations. **This** aligns with binding collective-choice requirements in [core_10-10_governance.md](core_10-10_governance.md) **Chapter Ten** and **PRIM11** (independent verification).

**Salience and attention-allocation integrity:** Where systems rank, filter, recommend, or otherwise prioritize information, the same presentation layer must preserve informational integrity and stakeholder agency.

**They must** keep material risks, uncertainties, limitations, and decision-relevant information appropriately visible and legible.

**They must not** allocate prominence, ordering, amplification, suppression, fragmentation, or delay in ways that predictably distort understanding, risk perception, or decision-making.

Where engagement, retention, or optimization objectives conflict with informational integrity, systems must prioritize accuracy, proportionate risk and relevance representation, and stakeholder agency.

Salience pathways must be explainable and reviewable in proportion to impact, including meaningful disclosure of major ranking or prioritization factors and available user controls where appropriate.

Cross-companion operational definitions for salience allocation, anti-distortion controls, disclosure, user control, mitigation, and proportional scaling are maintained in `corpus_joint_structure.md` **CJS-3.16** (*Cross-companion salience integrity and attention-allocation terms*). Apply that subsection as required read-with for this **PRIM1** implementation scope, together with **PRIM4** and **PRIM14** where materially applicable.

### PRIM2 — Presentation Implementation label: Comprehensibility and Cognitive Accessibility
Principles: **Agency and Accessibility** through understandable, usable, and cognitively proportionate disclosure.

**Constitutional anchor:** Apply this section in conjunction with cited constitutional sources; this section implements and does not narrow them.

**Canonical meaning:** This section states implementation-layer obligations for this domain, applied consistently with cited constitutional sources and without narrowing them.

**PRIM4** governs what must be disclosed.

**PRIM2** governs whether presentation is **understandable** and **usable**—including layering and cognitive load—so stakeholders can evaluate and act.

**[corpus_systems.md](corpus_systems.md), Protocol B** (*Comprehensibility and Complexity Stewardship*) scales annex comprehensibility obligations with system and steward class.

Where both apply, the **stricter** requirement governs (see Protocol B header).

**PRIM2** aligns with **PRIM1** and **PRIM4**.

**It must** **not** substitute weaker accessibility than **Chapters Two through Four** requires for verification accessibility, traceability, and observability. **That** rule applies where those requirements apply to the same presentation. Systems must present information, behavior, and structure without unreasonable cognitive burden.

Disclosure volume alone is insufficient: material must be meaningfully understandable, evaluable, and actionable.

Cross-companion operational definitions for comprehensibility, layering, cognitive load, interpretation support, high-impact drill-down, and proportional scaling are maintained in `corpus_joint_structure.md` **CJS-3.15** (*Cross-companion comprehensibility and cognitive accessibility terms*). Apply that subsection as required read-with for this **PRIM2** implementation scope.

Low-impact or isolated systems may simplify **only** if they do **not** create material barriers to understanding. **They** may simplify **only** if they do **not** impair evaluation of risk or behavior.

### PRIM4 — Presentation Implementation label: Transparency and Disclosure
Principles: **Truth and Contestability** through sufficient disclosure for informed participation and independent evaluation.

**Constitutional anchor:** Apply this section in conjunction with cited constitutional sources; this section implements and does not narrow them.

**Canonical meaning:** This section states implementation-layer obligations for this domain, applied consistently with cited constitutional sources and without narrowing them.

**Sentient Constitution Chapter Nine, Article XIV**, **Article XV-A** where auditability or observable evidence is implicated, and **Chapter Five** define info-sphere integrity and epistemic obligations at the constitutional term layer.

**Chapter Five** cites *Truth (Constitutional Constraint)*, *Epistemic Integrity*, and observability and verification entries where applicable.

**PRIM4** specifies **presentation-layer** disclosure and transparency requirements scaled with **PROT1**.

**It must** **not** substitute weaker tests than those sources (or **Chapters Two through Four** verification accessibility rules) where they apply.

Cross-companion operational definitions for disclosure sufficiency, verification-enabling transparency, private-state boundary handling, and observability attribution are maintained in `corpus_joint_structure.md` **CJS-3.17** (*Cross-companion disclosure sufficiency and observability terms*). Apply that subsection as required read-with for this **PRIM4** implementation scope.

Where presentation or interface design materially influences what stakeholders notice, compare, or rely on, disclosure must remain salient enough to support informed participation, independent evaluation, and challenge. **Complete** but **buried** disclosure is non-compliant.

Where ranking, recommendation, or prioritization mechanisms materially shape visibility, systems must disclose primary salience factors, known limitations, and meaningful user-control pathways in proportion to impact. Read this requirement with **PRIM1** and `corpus_joint_structure.md` **CJS-3.16**.

---
## IMPLEMENTATION GROUP THREE: ARCHITECTURE
### PRIM5 — Architecture Implementation label: Dependency Awareness, Disclosure, and Risk Integrity
Principles: **Safety and Accountability** through explicit dependency mapping, criticality disclosure, and anti-evasion controls.

**Constitutional anchor:** Apply this section in conjunction with cited constitutional sources; this section implements and does not narrow them.

**Canonical meaning:** This section states implementation-layer obligations for this domain, applied consistently with cited constitutional sources and without narrowing them.

**PRIM5** is the **architecture-layer** home for dependency awareness and risk integrity. **It must** **not** substitute weaker tests than **Article XV-A** or **Chapters Two through Four** where dependency disclosures affect informational or compliance outcomes. No system may depend on what it refuses to reveal, nor impose dependencies it does not account for.

**Chapter Five** supplies the definitional standards for dependency and impact evaluation, including *Dependency*, *Risk*, the materiality-family entries, *System*, *System Boundary Integrity*, and *Cascading Failure* where applicable. **[corpus_systems.md](corpus_systems.md), Protocol A** operationalizes lifecycle and environment boundaries that create or change dependencies.

Read this section together with **PRIM4**, **PRIM7**, **PRIM9**, **PRIM12**, **PRIM15**, **PROT1**, **PROT4**, and **Protocol B** where disclosure, mapping, retention lifecycle, classification alignment, or comprehensibility obligations apply to the same facts. For overlapping institution-system supervised scope, also apply **`corpus_joint_structure.md` CJS-3.5**.

Cross-companion operational definitions for dependency disclosure, criticality classification, substitutability and exit constraints, anti-externalization controls, monitoring and map obligations, and proportional scaling are maintained in `corpus_joint_structure.md` **CJS-3.18** (*Cross-companion dependency integrity and disclosure terms*). Apply that subsection as required read-with for this **PRIM5** implementation scope.

### PRIM6 — Architecture Implementation label: Graceful Degradation and Failure Mode Integrity
Principles: **Safety and Truth** through bounded degradation, honest signaling, and anti-cascading design.

**Constitutional anchor:** Apply this section in conjunction with cited constitutional sources; this section implements and does not narrow them.

**Canonical meaning:** This section states implementation-layer obligations for this domain, applied consistently with cited constitutional sources and without narrowing them.

**Sentient Constitution Chapter Fourteen** incorporation discipline and **Chapter One** govern the priority ordering for degraded conditions. **Chapter Five** (*Truth (Constitutional Constraint)*; *Epistemic Integrity*), **Chapter Nine, Article XIV**, and **Article XV-A** where auditability or observable evidence is implicated apply where degraded or misleading outputs implicate informational integrity. Local *Failure Integrity* implementation is in the meta-integrity obligation above.

Read this section together with **PRIM1**, **PRIM4**, **PRIM5**, **PRIM12**, **PRIM15**, **PROT1**, **Protocol A**, **Article XV-A** where degradation affects presentation integrity or auditability, and **Article XVI-A** where degradation affects lifecycle discipline, dependency handling, or governance response.

Cross-companion operational definitions for graceful degradation, failure-mode integrity, signaling discipline, bounded operation, fail-soft limits, transition escalation, cross-boundary propagation, and proportional scaling are maintained in `corpus_joint_structure.md` **CJS-3.19** (*Cross-companion graceful degradation and failure-mode integrity terms*). Apply that subsection as required read-with for this **PRIM6** implementation scope.

### PRIM7 — Architecture Implementation label: Interoperability, Portability, and Exit Integrity
Principles: **Agency and Anti-Lock-In** through usable portability, reciprocal interoperability, and meaningful exit.

**Constitutional anchor:** Apply this section in conjunction with cited constitutional sources; this section implements and does not narrow them.

**Canonical meaning:** This section states implementation-layer obligations for this domain, applied consistently with cited constitutional sources and without narrowing them.

**Sentient Constitution Chapter Nine, Article XIX** (*Interoperability, Portability, and Exit Integrity*) and **Chapter Five** ([§3.19](core_05-05_definitions_c_dependent_clusters.md#governance-architecture-oversight-decentralization-and-concentration-cluster) *Governance Architecture, Oversight, Dependency…* — *Systemic Lock-In*, *Dependency*, and related exit-path and market-structure analysis where applicable; [§3.23](core_05-05_definitions_c_dependent_clusters.md#movement-refuge-non-statelessness-and-exit-integrity-cluster) *Movement, Refuge, Non-Statelessness, and Exit Integrity* where mobility, refuge, or exit-integrity predicates apply jointly) state the foundational rights and foreclosure conditions. **PRIM7** is the **architecture-layer** home for operational interoperability, usable portability, integration boundaries, exit-feasibility transparency, and transition continuity.

**PROT4** governs justified limits on integration or export. Read this section together with **PRIM5** for dependency mapping and disclosure, and with **PRIM4**, **Article XV-A**, and **[corpus_systems.md](corpus_systems.md), Chapter S1 — Information Types and Handling** (Types **I** and **H**) where portability, attribution, or handling constraints apply.

Cross-companion operational definitions for anti-lock-in controls, portability, interoperability, open-interface treatment, innovation-reward boundary handling, continuity-preserving exit, and proportional scaling are maintained in `corpus_joint_structure.md` **CJS-3.20** (*Cross-companion interoperability, portability, and exit-integrity terms*). Apply that subsection as required read-with for this **PRIM7** implementation scope.

### PRIM8 — Architecture Implementation label: Intervention and Override Rights
Principles: **Safety, Proportionality, and Accountability** through timely, auditable, and scoped intervention capacity.

**Constitutional anchor:** Apply this section in conjunction with cited constitutional sources; this section implements and does not narrow them.

**Canonical meaning:** This section states implementation-layer obligations for this domain, applied consistently with cited constitutional sources and without narrowing them.

`PROT6` states the implementation-layer minimum for procedural integrity and adjudication-related governance role. Detailed court, institution, and cross-companion implementation remains with the canonical owner files.

**Sentient Constitution Chapter Nine** (**Articles IX, XII, and XIII**), **Chapter One**, **Chapter Five** (*Harm*, *Risk*, *Accountability*, *Oversight*, *Reversibility*, related entries), and **Chapter Ten** inform intervention where audit, standing/challenge, conflict or emergency proportionality, and misuse controls are implicated.

**PRIM6**, **PRIM14**, **PRIM9**, **PROT1**, **PROT4**, **PROT5**, Chapter Ten decision-resolution requirements, and **PRIM15** also intersect.

**PRIM8** is the **architecture-layer** home for **technical** intervention and override capacity. **PROT2** states the **governance-layer** authorization and procedural requirements. Where both apply, neither may be satisfied in lieu of the other.

Cross-companion operational definitions for intervention timeliness, trigger and pathway adequacy, override authority scoping, attribution and audit records, abuse safeguards, emergency coupling discipline, and proportional scaling are maintained in `corpus_joint_structure.md` **CJS-3.21** (*Cross-companion intervention and override integrity terms*). Apply that subsection as required read-with for this **PRIM8** implementation scope.

### PRIM9 — Integrity Implementation label: Auditability
Principles: **Truth and Accountability** through observable, reconstructable, and independently reviewable records.

Articles: Apply with **Sentient Constitution Chapter Nine, Article XV-A** and **Article VII-B** where internal-state protections constrain audit design.

**Constitutional anchor:** Apply this section in conjunction with cited constitutional sources; this section implements and does not narrow them.

**Definitions:** Apply with **Chapter Five** definitions for *Transparency*, *Epistemic Integrity*, *Protected Internal-State Boundary*, and *Accountability* where audit reconstruction and challenge are required.

**Canonical meaning:** This section states implementation-layer obligations for this domain, applied consistently with cited constitutional sources and without narrowing them.

**Sentient Constitution Chapters Two through Four**, **Chapter Nine, Article XV-A**, **PRIM4**, and **PROT3** set the audit baseline here. This implementation label applies those sources to observable, reconstructable, and independently reviewable records without narrowing them.

Cross-companion operational definitions for auditability requirements, reconstructability, verification-capable records, forensic-depth access, and Article VII-B boundary handling are maintained in `corpus_joint_structure.md` **CJS-3.22** (*Cross-companion auditability and reconstructability terms*). Apply that subsection as required read-with for this **PRIM9** implementation scope.

### PRIM10 — Integrity Implementation label: Tiered Transparency and Audit Access
Principles: **Truth, Accountability, and Proportional Access** through tiered transparency that preserves contestability.

Articles: Apply with **Sentient Constitution Chapter Nine, Articles V through IX** (rights-impacting systems), **Article VII-B** (internal-state boundary), and **Article XV-A** (auditability floor).

**Constitutional anchor:** Systems that **materially** affect foundational rights under **Sentient Constitution Chapter Nine, Articles V through IX** must maintain records and disclosures that enable **PRIM4**-grade participation, **PRIM9** verification, and evaluation of **risk**, **dependency**, and **systemic** effects.

**Definitions:** Apply with **Chapter Five** definitions for *Transparency*, *Epistemic Integrity*, *Trustworthiness*, and *Protected Internal-State Boundary*.

**Canonical meaning:** This section states implementation-layer obligations for this domain, applied consistently with cited constitutional sources and without narrowing them.

Cross-companion operational definitions for tiered transparency, qualified access pathways, forensic escalation routes, and access-control anti-concealment constraints are maintained in `corpus_joint_structure.md` **CJS-3.23** (*Cross-companion tiered transparency and audit-access terms*). Apply that subsection as required read-with for this **PRIM10** implementation scope.

### PRIM11 — Integrity Implementation label: Independent Verification and Integrity of Claims
Principles: **Truth and Trustworthiness** through independent, reproducible, and pluralistic verification of material claims.

Articles: Apply with **Sentient Constitution Chapter Fourteen** (trust and incorporation bridge) and **Chapter Nine** rights protections where material claims shape rights-relevant decisions.

**Constitutional anchor:** Independent verification carries out the **trust-as-verifiable-trustworthiness** **framing** of **Sentient Constitution Chapter Fourteen** and **Chapter Five** (*Trust*, *Trustworthiness*) in the **integrity** domain, including the incorporated **Implementation Group One** trust floor.

**Definitions:** Apply with **Chapter Five** definitions for *Trust*, *Trustworthiness*, *Epistemic Integrity*, and *Trust Degradation and Misleading Reliance*.

**Canonical meaning:** This section states implementation-layer obligations for this domain, applied consistently with cited constitutional sources and without narrowing them.

Cross-companion operational definitions for independent verification scope, reproducibility and plurality requirements, non-single-authority constraints, and class-scaled verification floor mapping are maintained in `corpus_joint_structure.md` **CJS-3.24** (*Cross-companion independent verification and claim-integrity terms*). Apply that subsection as required read-with for this **PRIM11** implementation scope.

### PRIM12 — Integrity Implementation label: Reversibility and Containment
Principles: **Safety and Non-Degradation** through containment, reversibility, and restoration when failure occurs.

Articles: Apply with **Sentient Constitution Chapter Nine, Articles I-III, V, IX, and XIII** where restoration, contestability, and harm containment are implicated.

**Constitutional anchor:** Apply this section in conjunction with cited constitutional sources; this section implements and does not narrow them.

**Definitions:** Apply with **Chapter Five** definitions for *Reversibility*, *Dependency*, *Epistemic Integrity*, and *Safety and Non-Degradation Baseline*.

**Canonical meaning:** This section states implementation-layer obligations for this domain, applied consistently with cited constitutional sources and without narrowing them.

**Sentient Constitution Chapter Five**, **Chapter Nine** (**Articles I-III and V, IX, and XIII** where restoration and contestability apply), and **PRIM5**, **PRIM6**, **PRIM9**, **PRIM10**, and **PRIM11** inform reversibility, rollback audit paths, and verification of recovery claims.

Cross-companion operational definitions for reversibility floors, containment obligations, compensatory restoration where rollback is incomplete, and irreversibility-limitation controls are maintained in `corpus_joint_structure.md` **CJS-3.25** (*Cross-companion reversibility and containment terms*). Apply that subsection as required read-with for this **PRIM12** implementation scope.

**Retention and lifecycle integrity:** Reversibility and containment include justified, bounded, and reviewable retention rules where stored data materially affects restoration, accountability, privacy, agency, or contestability.

At the implementation layer, the floor is:
- retention remains continuously justified and lifecycle-bounded
- minimization must not become accountability evasion
- retention architecture must not create hidden surveillance stockpiles, coercive leverage, or silent conversion of temporary holdings into persistent archives
- accumulation, linkage, or inference that functionally raises data sensitivity triggers stricter applicable protections
- retention rules remains auditable, challengeable, and periodically revalidated

Operational implementation stays outside this implementation label. Apply `corpus_joint_structure.md` **CJS-3.26** (*Cross-companion data-retention and lifecycle-integrity terms*) for justified retention, lifecycle expiry, anti-surveillance and anti-coercion limits, classification-creep handling, disclosure, and revalidation discipline. Apply **[corpus_systems.md](corpus_systems.md), Chapter S1 — Information Types and Handling** for type-specific storage, duration, separation, and reclassification controls, including materially relevant handling for **Types N, I, and H**.

### PRIM14 — Integrity Implementation label: Adversarial Robustness and Abuse Resistance
Principles: **Safety, Truth, and Anti-Capture Resilience** under adversarial, coordinated, and exploitative conditions.

Articles: Apply with **Sentient Constitution Chapter Nine, Articles XIII-A, XIV, XVII-A, IX, XII, and XI-D** where adversarial abuse affects epistemic mediation, governance integrity, and allocation outcomes; plus **Chapter Fourteen** incorporation discipline and this **PRIM14** adversarial integrity floor.

**Constitutional anchor:** Apply this section in conjunction with cited constitutional sources; this section implements and does not narrow them.

**Definitions:** Apply with **Chapter Five** definitions for *Adversarial, Scaled, and Exploited Conditions*, *Incentive Alignment*, *Proxy Divergence*, and *Epistemic Integrity*.

**Canonical meaning:** This section states implementation-layer obligations for this domain, applied consistently with cited constitutional sources and without narrowing them.

**Sentient Constitution Chapter Fourteen** and **Chapter Five** frame the threat context. **PRIM14** is the integrity-layer home for adversarial threat modeling, exploitation resistance, partial-compromise resilience, and defensive-boundary discipline under those sources.

Read this section together with **PRIM4**, **PRIM5**, **PRIM9**, **PRIM11**, **PRIM12**, **PRIM15**, **PROT1**, **PROT4**, and **PROT5** where adversarial conditions affect disclosure, dependency exposure, verification, containment, governance response, or revalidation duties.

Cross-companion operational definitions for adversarial threat modeling, exploitation-resistance controls, detection/response integrity, partial-compromise resilience, hardening cycles, defense-boundary limits, and proportional scaling are maintained in `corpus_joint_structure.md` **CJS-3.27** (*Cross-companion adversarial robustness and abuse-resistance terms*). Apply that subsection as required read-with for this **PRIM14** implementation scope.

### PRIM15 — Integrity Implementation label: Evolution, Revalidation, and Non-Entrenchment
Principles: **Accountability and Non-Entrenchment** through periodic revalidation, challengeability, and adaptive legitimacy.

Articles: Apply with **Sentient Constitution Chapter Nine, Articles XXIV-A and XXIV-B**, and **Chapters Eleven through Thirteen** for non-regression, amendment validity, and procedural validity in constitutional change.

**Constitutional anchor:** Apply this section in conjunction with cited constitutional sources; this section implements and does not narrow them.

**Definitions:** Apply with **Chapter Five** definitions for *Capture* (where applicable), *Accountability*, *Trustworthiness*, and *Epistemic Integrity* as they constrain lock-in and legitimacy drift.

**Canonical meaning:** This section states implementation-layer obligations for this domain, applied consistently with cited constitutional sources and without narrowing them.

**Sentient Constitution Chapter Nine, Articles XXIV-A and XXIV-B**, **Chapters Eleven through Thirteen**, **Chapter Five**, **Chapter Fourteen**, **PROT1**, **PROT6**, **PRIM9**, **PRIM11**, and **PRIM14** inform evolution discipline, reviewability, and continuity verification.

**PRIM15** is the **integrity-layer** home for revalidation and non-entrenchment. Legitimacy remains **provisional** without ongoing alignment; no system or governance structure gains **permanent** legitimacy through inertia, scale, or historical precedence alone.

All covered systems and structures must **undergo periodic revalidation**, remain **subject to challenge and replacement**, and preserve enough auditability and verification to test whether continued legitimacy still exists.

**Failure to evolve** in response to **new capabilities**, **identified risks**, or **superior alternatives** may trigger **review**, **reauthorization**, or **replacement** under applicable **PROT6**, **Articles XXIV-A and XXIV-B**, **Chapters Eleven through Thirteen**, **Chapter Nine** rights floors, and related **Chapter Five** definitions where materially relevant.

---
## IMPLEMENTATION GROUP FOUR: GOVERNANCE
Implementation Group Four states governance-layer abstractions only. Detailed institutional, adjudicative, collective-choice, transition, and domain-operational mechanics remain with their canonical owner files and applicable `corpus_joint_structure.md` read-with sections.

### PROT1 — Governance Implementation label: Distributed and Proportional Authority
Principles: **Plural Authority and Anti-Capture** through distributed oversight, proportional governance, and participation legitimacy.

**Constitutional anchor:** Scaling of authority and oversight under **PROT1** must remain consistent with **Sentient Constitution Chapter One** and the applicable **Chapter Five** interdependent definitions, including **Material Impact**, **Dependency**, **Risk**, **Irreversible Harm**, and **Decentralization**. This implementation label applies those sources at the governance layer and does **not** redefine or narrow them.

**Canonical meaning:** This section states implementation-layer obligations for this domain, applied consistently with cited constitutional sources and without narrowing them.

**PROT1** is the governance-layer home for distributing authority, scaling oversight, and preventing concentration or capture. Apply it wherever participation legitimacy, stewardship depth, or proportional review must track impact and dependency rather than convenience or inherited structure.

Cross-companion operational definitions for distributed/proportional authority floors, participation-legitimacy controls, stewardship-depth safeguards, anti-concentration guardrails, and contextual systemic-evaluation discipline are maintained in `corpus_joint_structure.md` **CJS-3.28** (*Cross-companion distributed and proportional authority terms*). Apply that subsection as required read-with for this **PROT1** implementation scope.

### PROT2 — Governance Implementation label: Intervention and Override Rights
Principles: **Safety and Procedural Accountability** through authorized, time-bound, and reviewable intervention governance.

**Constitutional anchor:** Apply this section in conjunction with cited constitutional sources; this section implements and does not narrow them.

**Canonical meaning:** This section states implementation-layer obligations for this domain, applied consistently with cited constitutional sources and without narrowing them.

**PROT2** is the governance-layer home for intervention **authorization**, **deliberation**, **emergency process**, and **accountability**. **PRIM8** remains the distinct **architecture-layer** home for technical intervention and override capacity, including pathways, robustness, attribution, documentation, transparency defaults, fail-safe behavior, and scaling.

Where both layers apply, **neither** may be satisfied in lieu of the other. Apply the file-header distinction (*Interpretation — Intervention and override (PRIM8 vs PROT2)*) and do not use **PROT2** to redefine or narrow **PRIM8** or the constitutional sources.

Cross-companion operational definitions for governance-layer intervention necessity, authorization scope, quorum/DRP sequencing, emergency governance limits, records/transparency/challenge duties, and proportional procedural scaling are maintained in `corpus_joint_structure.md` **CJS-3.29** (*Cross-companion intervention governance and override-authorization terms*). Apply that subsection as required read-with for this **PROT2** implementation scope.

### PROT3 — Governance Implementation label: Reflexive Transparency and Accountability
Principles: **Reflexive Accountability and Truth** through parity, auditability, and challengeability of governance itself.

**Constitutional anchor:** Apply this section in conjunction with cited constitutional sources; this section implements and does not narrow them.

**Canonical meaning:** This section states implementation-layer obligations for this domain, applied consistently with cited constitutional sources and without narrowing them.

**PRIM4**, **PRIM9**, **PRIM10**, **PRIM11**, **PROT4**, **PROT5**, **PROT1**, **PRIM15**, **Sentient Constitution Chapters Two through Four**, **Chapter Six** (*Enforcement Realism Anchors*), and **Chapter Nine** (**Articles I, IX, XII**) frame reflexive transparency and accountability for governance itself.

Cross-companion operational definitions for reflexive accountability parity, transparency/audit verification integrity, enforcement-capacity realism, pluralistic validation safeguards, and anti-corruption auditability controls are maintained in `corpus_joint_structure.md` **CJS-3.30** (*Cross-companion reflexive transparency and accountability terms*). Apply that subsection as required read-with for this **PROT3** implementation scope.

### PROT4 — Governance Implementation label: Burden of Justification and Constraint
Principles: **Necessity and Proportionality** by placing burden on restrictors and requiring auditable least-restrictive proof.

**Constitutional anchor:** Apply this section in conjunction with cited constitutional sources; this section implements and does not narrow them.

**Canonical meaning:** This section states implementation-layer obligations for this domain, applied consistently with cited constitutional sources and without narrowing them.

**Sentient Constitution Chapter One**, **Chapters Two through Four**, **PROT1**, **PRIM4**, **PRIM9**, **PRIM15**, **Article XIV**, and **Article XV-A** where auditability or observable evidence is implicated bound how constraints may be imposed, especially where transparency or epistemic integrity is restricted.

**PROT4** places the **burden** on the party **proposing or implementing** material restrictions on rights, participation, transparency, or system operation. It does **not** substitute for or weaken **Chapter Two** requirements. Any such action must satisfy a **consistent, auditable** standard.

**Innovation exclusivity claims:** This same burden applies to claimed patent-like, copyright-like, trade-secret-like, license-based, or technical exclusivity where the claim would materially restrict repair, interoperability, reverse engineering for compatibility or safety, migration, disclosure, research, education, or public-interest implementation. Constitutional meaning is anchored in **Sentient Constitution Chapter Five** (*Innovation Reward and Anti-Enclosure*) together with **Article XVII-D**. Operational implementation and class-scaled constraints are in this file at **PRIM7**. Apply those anchors here; do not redefine or narrow them.

Cross-companion operational definitions for restriction-burden assignment, least-restrictive proof, disclosure/challenge sufficiency, temporal revalidation, and innovation-exclusivity anti-enclosure application are maintained in `corpus_joint_structure.md` **CJS-3.31** (*Cross-companion burden-of-justification and constraint terms*). Apply that subsection as required read-with for this **PROT4** implementation scope.

### PROT5 — Governance Implementation label: Constrained Secrecy and Protected Investigations
Principles: **Safety with Accountability** through narrowly scoped, time-bound secrecy under independent oversight.

**Constitutional anchor:** Apply this section in conjunction with cited constitutional sources; this section implements and does not narrow them.

**Canonical meaning:** This section states implementation-layer obligations for this domain, applied consistently with cited constitutional sources and without narrowing them.

**PROT4**, **PROT1**, **PROT3**, **PRIM4**, **PRIM9**, **PRIM15**, **Sentient Constitution Chapters Two through Four**, **Article XIV**, and **Article XV-A** where auditability or observable evidence is implicated frame when transparency or participation may be limited. Investigations must **not** collapse into unaudited single-actor control or use secrecy to defeat informational integrity.

**PROT5** is the governance-layer home for **narrow, time-bound** secrecy and protected-investigation constraints. It does **not** create a general exemption from audit or challenge, and it must not redefine or narrow upstream constitutional requirements.

Where **same-pathway** separation between **investigation, oversight under constraint, or integrity support** and **Chapter Eight** binding merits adjudication is structurally material, **`corpus_joint_structure.md` CJS-3.3** applies alongside **PROT6** and **`corpus_institutions.md`**/**`corpus_forum.md`**.

Cross-companion operational definitions for secrecy predicates, minimization/preference ordering, deferred transparency records, constrained-condition oversight, and anti-normalization release discipline are maintained in `corpus_joint_structure.md` **CJS-3.32** (*Cross-companion constrained-secrecy and protected-investigation terms*). Apply that subsection as required read-with for this **PROT5** implementation scope.

---
### PROT6 — Governance Implementation label: Procedural Integrity and Adjudication
Principles: **Procedural Fairness, Contestability, and Timeliness** through due process, reviewability, and correction pathways.

**Constitutional anchor:** All systems must ensure that decisions, enforcement actions, classifications, and disputes affecting sentients are governed by fair processes that are transparent, timely, and contestable.

**Canonical meaning:** This section states implementation-layer obligations for this domain, applied consistently with cited constitutional sources and without narrowing them.

`PROT6` states the implementation-layer minimum for procedural integrity and adjudication-related governance role. Detailed court, institution, and cross-companion implementation remains with the canonical owner files.

Procedural integrity translates constitutional principles into consistent, enforceable outcomes under real-world conditions. Foundational rights affected by such processes remain governed by **Sentient Constitution Chapter Nine**. **Article XXIII** and **Article XXIII-A** supply substantive justice requirements, and **Chapter Five** supplies the governing definitions, including *Adjudication and Dispute Resolution* and *Procedural Fairness*, read with the **Chapter Five** clustered definition *Accountability, Contestability, Adjudication and Dispute Resolution, Collective Accountability Failure, and Force Majeure* where attribution, challenge, adjudication, excuse claims, or collective failure modes are materially implicated.

**PROT6** is the governance-layer home for due-process requirements, reviewability, correction access, and procedural safeguards for binding outcomes. It states those process properties by reference only and must **not** redefine, narrow, or substitute the constitutional sources or rights.

**Joint interfaces:** Where this section shares structural facts with institutions, classified systems, or Chapter Eight court operations, apply **`corpus_joint_structure.md` CJS-2.2** (applicable rows) and **CJS-3** (especially **CJS-3.3**, **CJS-3.4**, and **CJS-3.6**).

**Governance voting** and comparable **binding collective choice** must satisfy **Sentient Constitution Chapter Ten**, section 4 (*Voting and Binding Collective Choice Protocols*), including subsection **4.1** (entitlement; **Article IX-C**) and subsection **4.2** (records, gates, and method neutrality). They must also satisfy **Article X-C** and this **PROT6** where procedural themes overlap.

Where adopters use **evaluative (score / range)** or other **cardinal** ballots, **published** **aggregation**, **bounds**, **ties**, and **threshold** application must match that section.

**Opaque** or **post-hoc** tally formulas violate **procedural integrity** for **binding** outcomes.

**Scope index:** Apply `corpus_joint_structure.md` **CJS-3.33** for due-process requirements, initiator burden in adjudicative and enforcement settings, proportional enforcement selection, review independence, restoration access, uncertainty safeguards, anti-abuse limits, and system-class procedural scaling. Apply **CJS-3.34** for systemic-pattern review, **CUL** assignment, feedback integration, structural records, and stakeholder-scoped disclosure targeting.

For collective-choice procedure, entitlement, records, gates, method neutrality, quorum, and participatory legitimacy, read this section with **Sentient Constitution Chapter Ten** and the applicable `corpus_joint_structure.md` subsections. For court, institution, transition, external-system, and resource-flow mechanics, read the canonical owner files; this section supplies the implementation-layer governance floor only.

---

## CJS-4: Stable section identifiers, edition alignment, and drafting notes

**Edition alignment:** The header **Corpus edition** and **Effective date** must track **Corpus** labels in adopting instruments and `doc_architecture.md` corpus-alignment notes.

**Drafting priority (suggested):**

1. Extend **CJS-2.2** with new rows only when `doc_architecture.md` section 2 ownership or cross-file overlap changes; keep row IDs **stable**—append new IDs, do not renumber.
2. When **CI**/**CC**/**CS** repeat the same joint interface paragraph, prefer a **one-line** pointer to **CJS-3** (including **CJS-3.7** for hybrid composition shared by **CI-9.1B.2** and **CC-2.5.2**) and keep operative checklists in the domain owner.
3. When **Cross-domain implementation layer** repeats the same joint interface paragraph, apply **CJS-3.8** the same way: **one-line** pointer to **CJS-3** (or **CJS-2.2**), and keep **PRIM/PROT** operative substance in that layer (not duplicated at length in **CJS-3** OP blocks).
4. Run `make reference-audit` after substantive cross-file moves.
5. Where a new high-level joint abstraction is added, verify it remains **Tier 1 only** (no owner-mechanics migration) and record the duplicate-taxonomy risk in the active review notes until the deferred regression path is reinstated.

`doc_architecture.md` remains the **editorial map** and **placement guide**. **`corpus_joint_structure.md`** holds **binding joint structural** text within **Corpus** as designated in **Chapter Five** and incorporated through **Chapter Fourteen**.

*Corpus alignment:* edition `SC-Corpus-2026.04.32`, effective **2026-04-24**; canonical mapping in [doc_architecture.md](doc_architecture.md) **section 17**.
