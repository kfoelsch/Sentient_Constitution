## CJS-2: Implementation integration map

**Constitutional index (abridged)**
This section shows who owns major shared topics, where to look first, and which implementation files must be read together. The stable owner map is **CJS-2.2**, read with `doc_architecture.md` section 4.

When a topic involves more than one implementation file and matters for compliance, use this reading order:

1. **CJS folder**
   - Start here for cross-domain implementation rules and shared requirements, especially **CJS-2** and **CJS-3**.

2. **`corpus_systems.md`**
   - Use this for system classifications, stewardship rules, lifecycle duties, and protocols that determine the scale of obligations.

3. **`corpus_institutions.md`**
   - Use this for institutional governance, assurance processes, escalation paths, and non-forum structures.

4. **`corpus_forum.md`**
   - Use this for operational rules related to **Chapter Nine** forum families.

If two implementation files set different standards for the same meaningful risk, the stricter clearly adopted rule controls, following **Chapter Fifteen** and the classification/material-impact rules at the start of `corpus_systems.md`. The same rule applies in **CJS-3.6** when profiles and implementation labels seem to conflict.

### CJS-2.1: Intentional overlap (non-duplication discipline)
Some topics are **deliberately** split across implementation files (for example contest-integrity design, delegated subunits, forensic or technical-forum interfaces). For those:

- the **domain owner** states the **full operative** rules for its scope;
- the **CJS folder** states **joint satisfaction conditions**, **read-with pointers**, and **interface requirements** only;
- do **not** restate **PRIM/PROT** text, **S2/S3** tables, or **CF-** / **CI-** checklists except in brief **quote** or **summary pointer** form when needed for coherence.

### CJS-2.2: Topic router (stable IDs)
Each row names the **first** operative owner for the topic. **Mandatory read-with** lists implementation sections (and core hooks where listed) that must be satisfied **together** when the topic materially applies. Stable row IDs (**CJS-R01**–**CJS-R19**) are **corpus-local** here; they are **not** Sentient Constitution article numbers.

| Row ID | Topic | Primary owner | Mandatory read-with |
|--------|--------|---------------|---------------------|
| **CJS-R01** | Delegated binding bodies and hybrid composition (non-forum institutions) | `corpus_institutions.md` **CI-9.1B** | **CJS-4.1**, **CJS-4.7**, **CJS-5A.6**; `corpus_systems.md` **Chapter S2**, **Chapter S3**; `corpus_institutions.md` **CI-2**; the CJS implementation layer **PROT1 — Distributed and Proportional Authority**, **PROT4 — Burden of Justification and Constraint** (as cited in owner text) |
| **CJS-R02** | Forum chambers, divisions, and designated panels (Chapter Nine families) | `corpus_forum.md` **CF-2.5**–**CF-2.5.5** | **CJS-4.1**, **CJS-4.7**, **CJS-5A.6**; `corpus_institutions.md` **CI-9.1B**; `corpus_systems.md` **Chapter S2**, **Chapter S3**; `core_09-09_forum.md` **Chapter Nine** |
| **CJS-R03** | Lawful panel formation, disclosure, recusal, substitution, inability-to-form | `corpus_forum.md` **CF-3** | **CJS-4.7**, **CJS-5A.6**; `corpus_institutions.md` **CI-4**, **CI-5**; `core_09-09_forum.md` **Chapter Nine**; the CJS implementation layer **PROT6 — Procedural Integrity and Adjudication** (Implementation Group Four) |
| **CJS-R04** | Routing, intake, transfer, certification, representative treatment | `corpus_forum.md` **CF-4** | **CJS-4.7**, **CJS-5A.6**; `core_09-09_forum.md` **Chapter Nine**; `corpus_institutions.md` **CI-8** |
| **CJS-R05** | Appeal, secondary review, exhaustion | `corpus_forum.md` **CF-5** | `corpus_institutions.md` **CI-6**; CJS Implementation Group Four (including **PROT6 — Procedural Integrity and Adjudication**) |
| **CJS-R06** | Forum integrity operations, anti-capture, anti-self-judging support | `corpus_forum.md` **CF-6** | `corpus_institutions.md` **CI-5**, **CI-7.3**; `core_09-09_forum.md` **Chapter Nine** |
| **CJS-R07** | Forum forensic and analytical support | `corpus_forum.md` **CF-7** | `corpus_institutions.md` **CI-7A**, **CI-7.3** |
| **CJS-R08** | Independent investigative service and prosecution interface | `corpus_forum.md` **CF-8** | `corpus_institutions.md` **CI-7A.1**, **CI-8** |
| **CJS-R09** | Technical forums and specialist chambers | `corpus_forum.md` **CF-9** | `corpus_institutions.md` **CI-7B**, **CI-15B**; `core_09-09_forum.md` **Chapter Nine** |
| **CJS-R10** | Forum performance, backlog requirements, publication timeliness, accessibility | `corpus_forum.md` **CF-10** | `corpus_institutions.md` **CI-7.3**; Sentient Constitution **Article XV** themes in `core_10-10_rights_part_*.md` **Chapter Ten** |
| **CJS-R11** | Forum continuity, fallback operation, emergency adjudication | `corpus_forum.md` **CF-11** | `corpus_systems.md` **Protocol A — System Design, Testing, Verification, and Deployment**; `corpus_institutions.md` **CI-14** (where transition or continuity interfaces apply); `core_09-09_forum.md` **Chapter Nine** |
| **CJS-R12** | Standard forum records, forms, and evidence artifacts | `corpus_forum.md` **CF-12** | `corpus_institutions.md` **CI-6**; `core_02-04_definition_mechanics.md` **Chapters Two through Four** (traceability and verification discipline) |
| **CJS-R13** | Forum staffing, shared administration, structural review, structural records | `corpus_forum.md` **CF-13** | `corpus_institutions.md` **CI-4**, **CI-5**; **CI-9.1B** where delegated forum subunits apply |
| **CJS-R14** | Institutional functional lanes and non-delegable splits | `corpus_institutions.md` **CI-2** | the CJS implementation layer **PROT1 — Distributed and Proportional Authority**; `corpus_systems.md` **Chapter S3** where CSS stewardship intersects |
| **CJS-R15** | Contest-integrity monitoring (pathway integrity, not merits) | `corpus_institutions.md` **CI-7.3** | `corpus_systems.md` **Chapter S2**, **Chapter S3** (including steward contest-integrity paragraphs where applicable); the CJS implementation layer **PROT6 — Procedural Integrity and Adjudication**; the lawful-panel and forum-performance router topics (**CJS-R03** and **CJS-R10**) where forum performance data feeds monitors |
| **CJS-R16** | Cross-institution coordination, deadlock, and escalation | `corpus_institutions.md` **CI-8** | `corpus_forum.md` **CF-4**, **CF-6**; `core_09-09_forum.md` **Chapter Nine** (including backup and cross-forum integrity routing) |
| **CJS-R17** | Cross-implementation trust integrity (joint operation model) | CJS Implementation Group One (*Meta-integrity obligation: Trust and Trustworthiness*) | **CJS-4.4**; [Chapter Five section **3.11**](../core_05-05_definitions_c_dependent_clusters.md#trust-and-trustworthiness-cluster) (*Trust*, *Trustworthiness*, *Trust Degradation and Misleading Reliance*); `corpus_systems.md` **Chapter S2**, **Chapter S3** where classification or dependency scales assurance burden; `corpus_institutions.md` **CI-7.3**, **CI-8** and `corpus_forum.md` **CF-10** where pathway integrity, publication cadence, or accessibility materially conditions justified trust |
| **CJS-R18** | Class-scaled lane staffing and competency redundancy for materially binding stewardship | `corpus_institutions.md` **CI-2**, **CI-4**, **CI-11**, **CI-12** | **CJS-4.6**; **CJS-5A.1**; `corpus_systems.md` **Chapter S2**, **Chapter S3**; `core_11-11_governance.md` **Chapter Eleven**, section **5** |
| **CJS-R19** | Implementation and cross-implementation integrity assurance and resilience operations | **CJS-5B.1** | the CJS implementation layer **PRIM9 — Auditability** through **PRIM15 — Evolution, Revalidation, and Non-Entrenchment**; **Chapter Five** (*Auditability*, *Verifiability*, *Verification Accessibility*, *Reversibility*, *Dependency*, *Cascading Failure*, *Adversarial, Scaled, and Exploited Conditions*, *Trustworthiness*); `corpus_systems.md` **Chapter S1**, **Chapter S2**, **Chapter S3** where classification, data handling, or stewardship scales burden; `corpus_institutions.md` **CI-7.3**, **CI-8** and `corpus_forum.md` **CF-10** where monitoring, escalation, publication, or review pathways are materially required |

Rows are **indicative**, not exhaustive: if a matter triggers multiple rows, apply **all** triggered rows whose scope is materially true.

### CJS-2.3: Two-tier definition contract (binding abstraction + owner detail)
The CJS folder may adopt **binding high-level joint abstractions** only where a term or construct is materially cross-implementation and cannot be safely interpreted through a single owner file alone.

For this contract:

- **Tier 1 (CJS abstraction):** state only shared admission scope, cross-implementation trigger conditions, and minimum joint consequences needed to avoid contradiction or silent gaps.
- **Tier 2 (owner detail):** retain all operational tests, thresholds, procedures, and implementation mechanics in the canonical owner file(s) listed in **CJS-2.2**.
- **No parallel canon:** CJS abstractions must not become a second full taxonomy for domains owned by **CP**, **CS**, **CI**, or **CF**.
- **Specialize, do not redefine:** owner files may specialize a CJS abstraction for their domain scope but must not redefine it incompatibly.

---

**Next file:** [cjs_03_joint_structural_obligations.md](cjs_03_joint_structural_obligations.md)
