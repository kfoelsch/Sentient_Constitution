# CI-10: Public revenue, fees, recurring charges, and billing integrity

<details>
<summary><strong><span style="color: #2563eb;">Corpus placement (non-operative): file structure and reading rules</span></strong></summary>

> The following content is **reader guidance only**. It does not add, remove, or narrow binding obligations in this file or elsewhere.
>
> This file is **binding incorporated implementation text** where [`corpus_institutions.md`](../corpus_institutions.md) is incorporated under [Chapter Sixteen](../core_16-16_incorporation.md). It must satisfy the Sentient Constitution and does not override or narrow it. It holds **CI-10** (*Public revenue, fees, recurring charges, and billing integrity*).
>
> Start at the [Institutions landing page](../corpus_institutions.md) for reading order, or the [institutions registry](ci_00_registry_and_reading_rules.md) for identifier rules and the family map. Most readers reach this file from a citation rather than reading the folder front to back.

</details>

<br>

This file is the institutional implementation home for **CI-10** (*Public revenue, fees, recurring charges, and billing integrity*).

<br>

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.2](../corpus_joint_structure/cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-0.1](../corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids) topic router; [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline; [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions; and [Chapter Six](../core_06-06_rights_part_a.md#chapter-six-foundational-rights) rights architecture where rights interfaces are invoked.
- Downstream: [CI-10.1: Public revenue, user fees, and class-aligned burden](#ci-101-public-revenue-user-fees-and-class-aligned-burden); [CI-10.2: Recurring charges, renewals, and commercial billing integrity](#ci-102-recurring-charges-renewals-and-commercial-billing-integrity).
- Read with: **CI-10**; **CI-9**; **CI-9.3**; **CI-10.1**; **CI-10.2**; **CI-12.3**; [CJS-1.2](../corpus_joint_structure/cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Definitions · Assessment · Compliance</span></strong></summary>

- [Avoidable Burden](../core_05_band_continuity.md#avoidable-burden) · [O](../core_05_band_continuity.md#avoidable-burden) · [M](../core_05_band_continuity.md#avoidable-burden-a) · [A](../core_05_band_continuity.md#avoidable-burden-a) · [C](../core_05_band_continuity.md#avoidable-burden-c)
- [Contestability](../core_05_band_accountability.md#contestability) · [O](../core_05_band_accountability.md#contestability) · [M](../core_05_band_accountability.md#contestability-a) · [A](../core_05_band_accountability.md#contestability-a) · [C](../core_05_band_accountability.md#contestability-c)
- [Auditability](../core_05_band_oversight.md#auditability) · [O](../core_05_band_oversight.md#auditability) · [M](../core_05_band_oversight.md#auditability-a) · [A](../core_05_band_oversight.md#auditability-a) · [C](../core_05_band_oversight.md#auditability-c)
- [Transparency](../core_05_band_oversight.md#transparency) · [O](../core_05_band_oversight.md#transparency) · [M](../core_05_band_oversight.md#transparency-a) · [A](../core_05_band_oversight.md#transparency-a) · [C](../core_05_band_oversight.md#transparency-c)
- [Material](../core_05_band_oversight.md#material) · [O](../core_05_band_oversight.md#material) · [M](../core_05_band_oversight.md#material-a) · [A](../core_05_band_oversight.md#material-a) · [C](../core_05_band_oversight.md#material-c)
- [Corpus](../core_05_band_integrative.md#corpus) · [O](../core_05_band_integrative.md#corpus) · [M](../core_05_band_integrative.md#corpus-a) · [A](../core_05_band_integrative.md#corpus-a) · [C](../core_05_band_integrative.md#corpus-c)
- [System](../core_05_band_continuity.md#system-definition) · [O](../core_05_band_continuity.md#system-definition) · [M](../core_05_band_continuity.md#system-definition-a) · [A](../core_05_band_continuity.md#system-definition-a) · [C](../core_05_band_continuity.md#system-definition-c)
- [Trust Degradation and Misleading Reliance](../core_05_band_continuity.md#trust-degradation-and-misleading-reliance) · [O](../core_05_band_continuity.md#trust-degradation-and-misleading-reliance) · [M](../core_05_band_continuity.md#trust-degradation-and-misleading-reliance-a) · [A](../core_05_band_continuity.md#trust-degradation-and-misleading-reliance-a) · [C](../core_05_band_continuity.md#trust-degradation-and-misleading-reliance-c)
- [Coercion and Manipulation](../core_05_band_participation.md#coercion-and-manipulation-constitutional) · [O](../core_05_band_participation.md#coercion-and-manipulation-constitutional) · [M](../core_05_band_participation.md#coercion-and-manipulation-constitutional-a) · [A](../core_05_band_participation.md#coercion-and-manipulation-constitutional-a) · [C](../core_05_band_participation.md#coercion-and-manipulation-constitutional-c)
- [Meaningful Agency](../core_05_band_participation.md#meaningful-agency) · [O](../core_05_band_participation.md#meaningful-agency) · [M](../core_05_band_participation.md#meaningful-agency-a) · [A](../core_05_band_participation.md#meaningful-agency-a) · [C](../core_05_band_participation.md#meaningful-agency-c)
- [Material Impact](../core_05_band_oversight.md#material-impact) · [O](../core_05_band_oversight.md#material-impact) · [M](../core_05_band_oversight.md#material-impact-a) · [A](../core_05_band_oversight.md#material-impact-a) · [C](../core_05_band_oversight.md#material-impact-c)
- [Proportionality](../core_05_band_accountability.md#proportionality) · [O](../core_05_band_accountability.md#proportionality) · [M](../core_05_band_accountability.md#proportionality-a) · [A](../core_05_band_accountability.md#proportionality-a) · [C](../core_05_band_accountability.md#proportionality-c)
- [Accessibility](../core_05_band_participation.md#accessibility-constitutional) · [O](../core_05_band_participation.md#accessibility-constitutional) · [M](../core_05_band_participation.md#accessibility-constitutional-a) · [A](../core_05_band_participation.md#accessibility-constitutional-a) · [C](../core_05_band_participation.md#accessibility-constitutional-c)

</details>

<br>

*In plain terms: **CI-10** is the institutions layer's money-and-access rulebook — how public revenue, user fees, subscriptions, and recurring charges must stay fair, transparent, and aligned with how essential the underlying system is. Institutions must not price sentients out of survival-critical access, trick them into paid renewals, or trap them in billing cycles they cannot exit.  out of survival-critical access, tricked into paid renewals, or trapped in billing cycles you cannot exit. Shared fiscal and charge-exit floors live in **CJS-3.12** (*burden-of-justification and constraint terms*) and **CJS-3.17** (*interoperability, portability, and exit-integrity terms*); digital pathway detail lives in **CI-12.3**. What this file adds is local: what each institution must publish and maintain locally.*

**Quick orientation**

- **What this file covers** — class-aligned fiscal orientation and supervised recurring-charge duties for institutions that set, supervise, or authorize fee and billing rules.
- **What this file does not cover** — tax bases, rates, credits, enforcement mechanics, and cross-border tax law. Those remain governing law outside **CI-10**.
- **CI-10.1** — public revenue and user fees: charges must align with system class and must not make essential access unaffordable or administratively unreachable.
- **CI-10.2** — subscriptions, renewals, trials, and commercial billing: honest disclosure before commitment, usable cancel/downgrade paths, and supervision maps for recurring charges.
- **Read with** — **CI-9** and **CI-9.4** for classification and essential-access interfaces; **CI-12.3** where digital self-service billing pathways apply.

*In plain terms: if money touches access, the charge design must match the system's real importance — and sentients must be able to see what they owe, challenge unfair fees, and leave recurring charges through a published path that actually works.*

*Shared rules live elsewhere.* Class-aligned revenue and access-burden terms are in **CJS-3.12** (*burden of justification and constraint terms*). Commitment, renewal, and charge-exit terms are in **CJS-3.17** (*interoperability, portability, and exit-integrity terms*). **CI-10** does not repeat those floors; it keeps only institutional fiscal-map, supervision, and reporting duties.

## CI-10.1: Public revenue, user fees, and class-aligned burden
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Read with: **CI-10.1**; **CI-10.2**; **CI-12.3**.

</details>

<br>

*In plain terms: fees and public charges must fit the system's risk class — survival-critical and normal-operation-critical access cannot be treated as the main place to extract money. Commercial or premium use may bear more cost; baseline participation must not.*

Apply **CJS-3.12** **Class-aligned revenue and access-burden floor** for the shared floor. **CI-10.1** keeps only what each institution must name and maintain locally:

- who owns the **fiscal map** linking revenue and charge choices to published class and tier assignments;
- who owns **constrained-capacity priority** rules when limited public capacity must be allocated fairly;
- the **Protocol S5** reporting channel for resource-allocation and funding-stewardship alignment; and
- named owners for **CI-10.2** and **CI-12.3** where the institution supervises recurring charges or digital billing pathways.

## CI-10.2: Recurring charges, renewals, and commercial billing integrity
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Read with: **CI-10.2**; **CI-10.1**; **CI-9**; **CI-12.3**.

</details>

<br>

*In plain terms: subscriptions, memberships, trials, and auto-renewals must be honest before you sign up — clear price, clear timing, clear renewal rules — and cancellation or downgrade must work through a published path without dark patterns or surprise charges after exit.*

Apply **CJS-3.17** **Commitment, renewal, and charge-exit integrity** for the shared floor. **CI-10.2** keeps only what each institution must name and maintain locally:

- who owns the **charge-supervision map** for recurring and transaction-linked charges the institution supervises, authorizes, or sets compliance expectations for;
- a **stricter-law check** duty where governing law imposes stronger billing or consumer-protection requirements;
- **reclassification triggers** when essentiality or dependency changes and charge treatment must be reviewed with **CI-9** classification; and
- linkage to the **CI-10.1** fiscal interface where public revenue and supervised charges intersect.

Each supervised charge type must appear on the local map with:

- charge type and supervised scope;
- class and tier assignment under **CI-9**;
- the accountable office;
- the evidence artifact showing compliance; and
- the billing and exit complaint route — including coordination with **CI-12.3** where digital self-service pathways apply.

---

**Previous file:** [ci_09_classification_linked_institutional_obligations.md](ci_09_classification_linked_institutional_obligations.md)

**Next file:** [ci_11_resource_stewardship_incentive_integrity.md](ci_11_resource_stewardship_incentive_integrity.md)