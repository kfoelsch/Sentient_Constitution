# CJS-3: Joint structural obligations (cross-domain requirements)

<details>
<summary><strong><span style="color: #2563eb;">Corpus placement (non-operative): file structure and reading rules</span></strong></summary>

> The following content is **reader guidance only**. It does not add, remove, or narrow binding obligations in this file or elsewhere.
>
> This file is **binding incorporated implementation text** where [`corpus_joint_structure.md`](../corpus_joint_structure.md) is incorporated under [Chapter Sixteen](../core_16-16_incorporation.md). It must satisfy the Sentient Constitution and does not override or narrow it. It holds **CJS-3** (*Joint structural obligations (cross-domain requirements)*).
>
> Start at the [Joint structure landing page](../corpus_joint_structure.md) for reading order, or the [joint-structure registry](cjs_00_registry_and_reading_rules.md) for identifier rules and the family map. Most readers reach this file from a citation rather than reading the folder front to back.

</details>

<br>

This file is the joint-structure implementation home for **CJS-3** (*Joint structural obligations (cross-domain requirements)*).

<br>

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.2](cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline and [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions.
- Downstream: [CJS-3.1 When joint obligations apply](#cjs-31-when-joint-obligations-apply); [CJS-3.2 No false partial compliance across implementation files](#cjs-32-no-false-partial-compliance-across-implementation-files); [CJS-3.3 Boundary Between Support Roles and Merits Decisions](#cjs-33-boundary-between-support-roles-and-merits-decisions); [CJS-3.4 Institution-hosted or forum-adjacent operations](#cjs-34-institution-hosted-or-forum-adjacent-operations); [CJS-3.5 Classification alignment for supervised scope](#cjs-35-classification-alignment-for-supervised-scope); [CJS-3.6 Implementation-label traceability and stricter-wins discipline](#cjs-36-implementation-label-traceability-and-stricter-wins-discipline).
- Read with: **CJS-3**; [CJS-1.1](cjs_01_scope_purpose_boundary_interface.md#cjs-11-joint-structural-boundary-and-owner-discipline); [CJS-1.2](cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract); **CJS-4**.
- Topic routing (human path): [CJS-0.1](cjs_00_registry_and_reading_rules.md#cjs-01-cross-file-routing) and the [topic router reader index](../doc_architecture/generated/topic_router_reader_index.md). (**CJS-2** is integrator/maintainer only.)

</details>

<details>
<summary><strong><span style="color: #2563eb;">Definitions · Assessment · Compliance</span></strong></summary>

- [Authority Stack and Internal Hierarchy](../core_05_band_integrative.md#authority-stack) · [O](../core_05_band_integrative.md#authority-stack) · [M](../core_05_band_integrative.md#authority-stack-a) · [A](../core_05_band_integrative.md#authority-stack-a) · [C](../core_05_band_integrative.md#authority-stack-c)
- [Adjudication and Dispute Resolution](../core_05_band_accountability.md#adjudication-and-dispute-resolution-constitutional) · [O](../core_05_band_accountability.md#adjudication-and-dispute-resolution-constitutional) · [M](../core_05_band_accountability.md#adjudication-and-dispute-resolution-constitutional-a) · [A](../core_05_band_accountability.md#adjudication-and-dispute-resolution-constitutional-a) · [C](../core_05_band_accountability.md#adjudication-and-dispute-resolution-constitutional-c)
- [Classification-Scaled Governance](../core_05_band_oversight.md#classification-scaled-governance) · [O](../core_05_band_oversight.md#classification-scaled-governance) · [M](../core_05_band_oversight.md#classification-scaled-governance-a) · [A](../core_05_band_oversight.md#classification-scaled-governance-a) · [C](../core_05_band_oversight.md#classification-scaled-governance-c)
- [Contestability](../core_05_band_accountability.md#contestability) · [O](../core_05_band_accountability.md#contestability) · [M](../core_05_band_accountability.md#contestability-a) · [A](../core_05_band_accountability.md#contestability-a) · [C](../core_05_band_accountability.md#contestability-c)
- [Merits Determination](../core_05_band_accountability.md#merits-determination) · [O](../core_05_band_accountability.md#merits-determination) · [M](../core_05_band_accountability.md#merits-determination-a) · [A](../core_05_band_accountability.md#merits-determination-a) · [C](../core_05_band_accountability.md#merits-determination-c)
- [Oversight](../core_05_apex_oversight_leg.md#oversight-constitutional) · [O](../core_05_apex_oversight_leg.md#oversight-constitutional) · [M](../core_05_apex_oversight_leg.md#oversight-constitutional-m) · [A](../core_05_apex_oversight_leg.md#oversight-constitutional-a) · [C](../core_05_apex_oversight_leg.md#oversight-constitutional-c)
- [Procedural Fairness](../core_05_band_participation.md#procedural-fairness-constitutional) · [O](../core_05_band_participation.md#procedural-fairness-constitutional) · [M](../core_05_band_participation.md#procedural-fairness-constitutional-a) · [A](../core_05_band_participation.md#procedural-fairness-constitutional-a) · [C](../core_05_band_participation.md#procedural-fairness-constitutional-c)
- [Material](../core_05_band_oversight.md#material) · [O](../core_05_band_oversight.md#material) · [M](../core_05_band_oversight.md#material-a) · [A](../core_05_band_oversight.md#material-a) · [C](../core_05_band_oversight.md#material-c)
- [Corpus](../core_05_band_integrative.md#corpus) · [O](../core_05_band_integrative.md#corpus) · [M](../core_05_band_integrative.md#corpus-a) · [A](../core_05_band_integrative.md#corpus-a) · [C](../core_05_band_integrative.md#corpus-c)
- [Incentive Alignment](../core_05_band_integrative.md#incentive-alignment) · [O](../core_05_band_integrative.md#incentive-alignment) · [M](../core_05_band_integrative.md#incentive-alignment-a) · [A](../core_05_band_integrative.md#incentive-alignment-a) · [C](../core_05_band_integrative.md#incentive-alignment-c)
- [Materiality Determination](../core_05_band_oversight.md#materiality-determination) · [O](../core_05_band_oversight.md#materiality-determination) · [M](../core_05_band_oversight.md#materiality-determination-a) · [A](../core_05_band_oversight.md#materiality-determination-a) · [C](../core_05_band_oversight.md#materiality-determination-c)

</details>

<br>

*In plain terms: this file holds domain-specific joint rules that cut across systems, institutions, and forums — support roles vs merits, hosted-forum independence, and classification alignment. Shared-contract rules (when joint duties apply, combined satisfaction, and stricter-wins) live in **CJS-1.2** and **CJS-0.1**.*

**Where else to look**

- Shared contract (combined satisfaction, stricter-wins, authority stack): **CJS-1.2**
- Reading stack and layer boundary: **CJS-1.1**
- When joint rules apply: [CJS-0.1](cjs_00_registry_and_reading_rules.md#cjs-01-cross-file-routing) (*Cross-file routing*)
- Specific interlocks next: **CJS-4** (*Specific joint interlocks and shared abstractions*)

<details>
<summary><strong><span style="color: #2563eb;">Reader guidance (non-operative): joint structural obligations</span></strong></summary>

> The following content is **reader guidance only**. It does not add, remove, or narrow binding obligations elsewhere in this file or in other corpus files.
>
> **CJS-3** body is the domain-specific cannot-cherry-pick rules below (**CJS-3.3**–**CJS-3.5**). Combined satisfaction and stricter-wins are part of the shared contract in **CJS-1.2**; applicability is in **CJS-0.1** (stubs **CJS-3.1**, **CJS-3.2**, and **CJS-3.6** keep stable citations).
>
> **What each operative section does** — **CJS-3.3** support roles vs merits decisions; **CJS-3.4** institution-hosted forum independence; **CJS-3.5** classification alignment across supervision and systems text.

</details>

<br>

## CJS-3.1 When joint obligations apply

<a id="cjs-31-when-joint-obligations-apply"></a>

*In plain terms: these joint rules apply when topic routing requires reading more than one implementation file for the same facts, or when an adopting instrument applies the CJS folder.*

Operative trigger: [CJS-0.1](cjs_00_registry_and_reading_rules.md#cjs-01-cross-file-routing) (*Cross-file routing*) — **When joint obligations apply**.

## CJS-3.2 No false partial compliance across implementation files

<a id="cjs-32-no-false-partial-compliance-across-implementation-files"></a>

*In plain terms: doing well on one rulebook does not count as compliance if another material duty for the same facts is still unmet.*

Operative home: [CJS-1.2](cjs_01_scope_purpose_boundary_interface.md#cjs-12-combined-satisfaction) (*Shared implementation-corpus preamble contract*) — **Combined satisfaction across implementation files**.

## CJS-3.3 Boundary Between Support Roles and Merits Decisions
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Read with: **CJS-3.3**; **CJS-5.13** (*Accountability: procedural integrity and adjudication terms*); [Merits Determination](../core_05_band_accountability.md#merits-determination).

</details>

<br>

*In plain terms: people who monitor performance, give forensic help, or support investigations help the process — they do not decide who wins, unless a separate lawful instrument clearly says they may.*

Roles that monitor, review how challenge or review routes perform, provide forensic help, or support investigations must not make binding [Merits Determination](../core_05_band_accountability.md#merits-determination) decisions under [Chapter Eleven](../core_11-11_forum.md#chapter-eleven-forums-and-jurisdiction) and **Adjudication and Dispute Resolution**. The only exception is when a separate lawful instrument clearly gives a named role limited authority to decide merits issues.

Institutions must publish what each role may do and what it may **not** decide — including who the role reports to, how often it reports, and how it connects to assurance work. Oversight and support roles must not quietly take over merits decisions assigned to a lawfully constituted forum family under **Chapter Eleven**.

See **CI-7.3** (*Contest-integrity monitoring (Class A and Class B)*), **CF-8** (*Forum forensic and analytical support*), **CF-9** (*Independent investigative service and prosecution interface*), and **CJS-5.13** (*Accountability: procedural integrity and adjudication terms*).

## CJS-3.4 Institution-hosted or forum-adjacent operations

*In plain terms: hosting the building, budget, or software for a forum does not let the host control the forum's decisions.*

When an institution hosts, funds, administers, or technically runs forum infrastructure, it must make forum independence and contestability work in practice — including budget, staffing, records, security, procurement, clerking, digital systems, and personnel systems. Independence on paper is not enough.

## CJS-3.5 Classification alignment for supervised scope

*In plain terms: do not call a system one risk class in supervision papers and a different class in how it is actually run, if that label change would change what duties apply.*

Apply **CJS-5.11** (*Accountability: distributed and proportional authority terms*) **Classification-scaled governance burden** for the shared class- and tier-scaling rule.

When an institution supervises systems under `corpus_systems.md` **CS-3 — System classification and handling** or **CS-4 — Critical system stewardship**, its published maps under **CI-9.2** (*Published industry and domain mapping*) and related **CI-9** (*Classification-linked institutional obligations*) material must match the operative systems classification profile, including when reclassification is required.

## CJS-3.6 Implementation-label traceability and stricter-wins discipline

<a id="cjs-36-implementation-label-traceability-and-stricter-wins-discipline"></a>

*In plain terms: if two adopted rules disagree about the same real risk, follow the stricter one.*

Operative home: [CJS-1.2](cjs_01_scope_purpose_boundary_interface.md#cjs-12-stricter-wins) (*Shared implementation-corpus preamble contract*) — **Stricter-wins among adopted implementation standards**. Citation hygiene for **CJS-5** labels remains in [CJS-0.3](cjs_00_registry_and_reading_rules.md#cjs-03-stable-identifiers-edition-alignment-and-drafting-notes).

---

**Previous file:** [CJS-1](cjs_01_scope_purpose_boundary_interface.md) (*Scope, purpose, and boundary interface*)

**Next file:** [CJS-4](cjs_04_specific_joint_interlocks.md) (*Specific joint interlocks and shared abstractions*)