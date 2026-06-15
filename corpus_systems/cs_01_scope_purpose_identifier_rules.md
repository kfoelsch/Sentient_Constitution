# Systems implementation

*In plain terms: this file is the systems-and-data rulebook — how classified systems are typed, stewarded, tested, and operated without contradicting the Sentient Constitution.*

**Corpus edition:** `SC-Corpus-2026.04.32` · **Effective date:** 2026-04-24

<details>
<summary><strong><span style="color: #2563eb;">Reader guidance (non-operative): edition, status, and where this file lives</span></strong></summary>

> The following content is **reader guidance only**. It does not add, remove, or narrow binding obligations elsewhere in this file or in other corpus files.
>
> **Edition and alignment**
> - These labels track the same edition metadata as the numbered `core_*.md` files (see [README.md](../README.md)), [corpus_institutions.md](../corpus_institutions.md), [corpus_forum.md](../corpus_forum.md), and [corpus_joint_structure.md](../corpus_joint_structure.md).
> - Canonical mapping: [doc_architecture.md](../doc_architecture.md) **section 17**.
>
> **Status**
> - This is **not** a core constitutional file. It is binding incorporated implementation text where [Chapter Five](../core_05-05_definitions_c_dependent_clusters.md#corpus) and [Chapter Fifteen](../core_15-15_incorporation.md#chapter-fifteen-incorporation-bridge) designate it.
> - Prefer the filename **`corpus_systems.md`** in cross-references; the bare phrase *Constitutional Systems* is not used in corpus body text (see [doc_architecture.md](../doc_architecture.md) — Plain-Language Vocabulary Guardrails, Ambiguous implementation labels).
> - The CS folder is written in plain language with low jargon to improve accessibility, audit readability, and practical adoption testing.
>
> **Where this lives**
> - **Navigation wrapper:** [corpus_systems.md](../corpus_systems.md) indexes the `corpus_systems/` subfiles.
> - **Editorial map:** [doc_architecture.md](../doc_architecture.md) section 4 (definitions protocol) and section 2 (ownership map).
> - **Shared contract:** [corpus_joint_structure.md](../corpus_joint_structure.md) **CJS-1.2** (*Shared implementation-corpus preamble contract*).

</details>

<br>

**Quick orientation**

The systems layer (**CS**) owns typing, classification, stewardship, and protocol-level engineering rules for systems and data:

- **CJS** — [corpus_joint_structure.md](../corpus_joint_structure.md) (joint-structure interfaces)
- **CS** — this folder (`corpus_systems/`)
- **CI** — [corpus_institutions.md](../corpus_institutions.md)
- **CF** — [corpus_forum.md](../corpus_forum.md)

**CS** is the canonical home for **Chapters S1–S3**, **Protocol A** through **Protocol T**, and related systems labels. Constitutional meanings, Rights Floors, and definition-satisfaction rules remain in the Sentient Constitution and Chapter Five.

System and data obligations here align with [corpus_joint_structure.md — Cross-domain implementation layer](../corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cross-domain-implementation-layer), especially **CJS-4.4** (*Cross-implementation trust integrity (joint operation model)*) and the **CJS-5** (*Implementation and cross-implementation operational cluster library*) operational cluster library.

Shared preamble contract: apply [corpus_joint_structure.md](../corpus_joint_structure.md) **CJS-1.2** (*Shared implementation-corpus preamble contract*).

<details>
<summary><strong><span style="color: #2563eb;">Reader guidance (non-operative): routing anchors and cluster index</span></strong></summary>

> The following content is **reader guidance only**. It does not add, remove, or narrow binding obligations elsewhere in this file or in other corpus files.
>
> **CJS cluster mapping (routing only)**
> - Technical requirements map primarily to **CJS-5B** (*Evidence, audit, and claim integrity*), **CJS-5C** (*Participation, comprehension, and disclosure*), **CJS-5D** (*Dependency, exit, and lifecycle integrity*), and **CJS-5E** (*Failure, robustness, intervention, and correction*).
> - Governance, proportionality of authority, justification, challenge, and collective-choice processes map primarily to **CJS-5A** (*Authority, constraint, secrecy, and procedure*), together with Chapter Eleven decision-resolution requirements.
>
> **File-specific implementation anchors**
> - **Taxonomy home:** data types, system classes/dependency types, and steward tiers are canonical in **Chapters S1–S3**; other corpus files reference these labels.
> - **Chapter Ten structure:** This file implements Chapter Ten themes operationally (challenge/redress via **Article XII-B**; auditability via **Article XV-A** with **Chapters Two through Four**; justice and emergencies via **Article XXIII** with **Chapter One** section 6.4; info-sphere and publication via **Articles XIV** and **VIII-C** with Chapter Five clusters). It must not narrow those articles.
> - **Intervention layering:** **CJS-5E.2** (*Implementation and cross-implementation intervention and override integrity terms*) and **CJS-5A.2** (*Implementation and cross-implementation intervention governance and override-authorization terms*) — jointly applicable where relevant.
> - **Voting / crypto / roles:** Chapter Eleven section 4 (*Voting and Binding Collective Choice Protocols*); Chapter Four section 5.1 (*Cryptographic protection, credentials, and verification*); Chapter Eleven section 5 (*Authorized Roles, Competency Development, and Contribution*).
> - **Capital-markets scope:** specialist corporate-securities law remains outside dedicated implementation file coverage.
> - **Joint implementation read:** where **S2/S3** intersect institutional governance, forum operations, or **CJS-5** clusters, read **`corpus_joint_structure.md`** **CJS-2** (especially **CJS-2.2**) and **CJS-3**.
> - **Chapter Six standing composites:** Standing inputs must be **verified** only ([Chapter Six — Assessment](../core_06-06_standing_assessment.md) section 2). **Forum** allegations and claims are not standing-calculus inputs (**Chapter Nine**). Recency weighting applies only to contribution-linked credit under [Chapter Seven §4.1](../core_07-07_standing_integration.md#38-standing-integration-contribution-and-violation-nature). Numeric interoperability defaults: [implementation/CH06_NINE_SLOT_STANDING_SCALE.md](../implementation/CH06_NINE_SLOT_STANDING_SCALE.md).

</details>

<br>

Market infrastructure and intermediaries with material dependency, coordination, or info-sphere effects remain in scope under **S2/S3**. They remain subject to applicable Chapter Five definitions, **CJS-5** (*Implementation and cross-implementation operational cluster library*) operational clusters, and protocol controls.

**Market-mediated personal services (Article X-C implementation interface):** Systems that **match**, **dispatch**, **schedule**, **settle payment for**, or **reputation-score** **in-person** personal services are **presumptively material** for **dependency**, **safety**, **coercion risk**, and **fairness** analysis when impact thresholds are approached. This is especially true where **intimacy**, **bodily contact**, **private-space or in-home access**, or **isolated work** is involved. They must be evaluated under **Chapter S2** classification and **Chapter S3** stewardship together with **Chapter Five** (*Coercion and Manipulation* and *Consent*) and **Chapter Ten**, **Article X-A**. They must **not** be structured to evade **Article X-C**’s **decriminalization** or **nondiscrimination** floors through **technical** exclusion, **de-banking**, or **opaque** ranking. Institutional expectations appear in **`corpus_institutions.md`** **CI-15** (*Vulnerable personal services markets — general regulation and Article X-C interface*).

**Contingent claims and event markets:** Systems that match counterparties, pool stakes, or settle payments contingent on external events (**Chapter Five** — [*Contingent Claim*](../core_05-05_definitions_a_independent.md#contingent-claim), [*Event-Contract Market*](../core_05-05_definitions_a_independent.md#event-contract-market); [*Game of Chance*](../core_05-05_definitions_a_independent.md#game-of-chance) forms) are presumptively material for incentive, capture, manipulation, and stability analysis. They must be evaluated under **Sentient Constitution Chapter One**, section **7.2.5** and scaled under **Chapter S2** classification and **Chapter S3** stewardship where impact thresholds are met. Operators must document resolution authority, dependencies on outcome-resolution sources, privileged-information pathways, conflict separation between market-making and resolution roles where relevant (**Chapter Five** — [*Capture of Resolution Pathways*](../core_05-05_definitions_b_semi_independent.md#capture-of-resolution-pathways)), and plausible misuse scenarios including coordination to affect outcomes. This implementation file does not specify licensing, criminal offenses, or tax rules for gambling; adopting law remains primary for those bases. **Article XIV** and **Article XV-A** where auditability or observable evidence is implicated limit treating settlement prices or odds as authority enough by themselves to decide epistemic questions.

## Systems Identifier and Article-Reference Rules
Apply `corpus_joint_structure.md` **CJS-1.3** (*Section identifiers and article references*) as the shared implementation-corpus identifier rule. In this file specifically, **Protocol A**, **Protocol B**, **Protocol S4**, **Protocol S5**, **Protocol T**, **Protocol R**, **Protocol D**, and **Chapter S1** through **Chapter S3** are systems implementation labels. They must not be read as Sentient Constitution **Article** or chapter numbers. The editor abbreviation **CS** may appear in owner tables, stable IDs, and short routing references, but citations should prefer `corpus_systems.md` plus the named protocol or Chapter S label where practical.

Unless another reference pattern is stated, **Article** labels with Roman numerals in this file point to Sentient Constitution Chapter Ten in the `core_10-10_rights_part_*.md` files.

---

**Next file:** [cs_protocol_a_system_design_testing_verification_deployment.md](cs_protocol_a_system_design_testing_verification_deployment.md)
