<a id="cs-5-part-a-user-facing-capability-surfaces"></a>
# CS-5, Part A: User-facing capability surfaces

<details>
<summary><strong><span style="color: #2563eb;">Corpus placement (non-operative): file structure and reading rules</span></strong></summary>

> The following content is **reader guidance only**. It does not add, remove, or narrow binding obligations elsewhere in this file or in other CS-5 parts.
>
> This file is **binding incorporated implementation text** where [`corpus_systems.md`](../corpus_systems.md) is incorporated under [Chapter Sixteen](../core_16_incorporation.md). It must satisfy the Sentient Constitution and does not override or narrow it. It holds **CS-5, Part A** (*User-facing capability surfaces*). Lifecycle engineering (**CS-5** §§1–10) remains in [`cs_05_design_testing_verification_deployment.md`](cs_05_design_testing_verification_deployment.md).
>
> Start at the [Systems and data landing page](../corpus_systems.md) for reading order, or the [systems registry](cs_00_registry_and_reading_rules.md) for identifier rules and the family map. Most readers reach this file from a citation rather than reading the folder front to back.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [Article XII-B](../core_06_rights_part_c.md#article-xii-b-right-to-challenge-review-and-redress) (*Right to Challenge, Review, and Redress*); [Article XVI](../core_06_rights_part_c.md#article-xvi-system-lifecycle-environments-and-reversibility) (*System Lifecycle, Environments, and Reversibility*); [Public Oversight Baseline Disclosure](../core_05_band_oversight.md#public-oversight-baseline-disclosure); [Chapter Sixteen](../core_16_incorporation.md#chapter-sixteen-incorporation-bridge); and [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions.
- Downstream: [§11](#cs-5-11-purpose-and-role); [§12](#cs-5-12-in-scope-catalog); [§13](#cs-5-13-analog-digital-and-channel-class); [§14](#cs-5-14-what-this-file-does-not-own).
- Read with: **CS-5**; **CS-2 — Information types and handling**; **CS-3 — System classification and handling**; **CS-4 — Critical system stewardship**; **CS-6**; **CJS-3.8**; **CJS-3.17**; **CI-8.3**.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Definitions · Assessment · Compliance</span></strong></summary>

- [Contestability](../core_05_band_accountability.md#contestability) · [O](../core_05_band_accountability.md#contestability) · [M](../core_05_band_accountability.md#contestability-a) · [A](../core_05_band_accountability.md#contestability-a) · [C](../core_05_band_accountability.md#contestability-c)
- [Auditability](../core_05_band_oversight.md#auditability) · [O](../core_05_band_oversight.md#auditability) · [M](../core_05_band_oversight.md#auditability-a) · [A](../core_05_band_oversight.md#auditability-a) · [C](../core_05_band_oversight.md#auditability-c)
- [Public Oversight Baseline Disclosure](../core_05_band_oversight.md#public-oversight-baseline-disclosure) · [O](../core_05_band_oversight.md#public-oversight-baseline-disclosure) · [M](../core_05_band_oversight.md#public-oversight-baseline-disclosure-a) · [A](../core_05_band_oversight.md#public-oversight-baseline-disclosure-a) · [C](../core_05_band_oversight.md#public-oversight-baseline-disclosure-c)
- [Accessibility](../core_05_band_participation.md#accessibility-constitutional) · [O](../core_05_band_participation.md#accessibility-constitutional) · [M](../core_05_band_participation.md#accessibility-constitutional-a) · [A](../core_05_band_participation.md#accessibility-constitutional-a) · [C](../core_05_band_participation.md#accessibility-constitutional-c)

</details>

<br>

This file is the systems implementation home for **CS-5, Part A** (*User-facing capability surfaces*).

*In plain terms: **CS-5, Part A** is a pointer catalog of what an in-scope system must let sentients do or inspect — identity control, export, Type O inspect, challenge entry, comprehensibility, digital self-service when entry was already digital — without turning those duties into a product list, and without taking standing, forum, voting, or remedy away from their owners.*

<a id="cs-5-11-purpose-and-role"></a>
## CS-5.11 Purpose and role

*In plain terms: this file names the reachable surfaces an in-scope system must expose, then points at the homes that already own the rules; it does not invent apps.*

**What this file owns**

- the systems-layer catalog of **user-reachable capability surfaces** for in-scope systems — who can do or inspect a named act, and which owner already states the duty;
- the channel-class rule in [§13](#cs-5-13-analog-digital-and-channel-class): analog remains lawful unless the cited owner already requires a digital or machine-usable channel;
- the negative duties in [§14](#cs-5-14-what-this-file-does-not-own): do not invent a standing portal, a federated Type O directory, or a unified subject-access product that defeats Chapter Eight silence.

**What this file does not own**

- lifecycle engineering in **[CS-5](cs_05_design_testing_verification_deployment.md)** §§1–10;
- information typing and identity / export mechanics in **CS-2 — Information types and handling**;
- classification disclosure and challenge in **CS-3 — System classification and handling**;
- inspectable attributable action and chokepoint continuity in **CS-4 — Critical system stewardship**;
- comprehensibility and complexity stewardship in **CS-6**;
- shared digital self-service and exit-integrity terms in **CJS-3.17** and institutional supervision in **CI-8.3**;
- the challenge, review, and redress floor in **Article XII-B**;
- standing records, forum dockets, collective choice, and remedy offices — those remain in Chapters Seven through Twelve, **CF**, and **CI**.

This file implements the **CS-5.1** rule that the constitution defines required capabilities and outcomes, and that specific technical implementations may evolve, provided they remain auditable. It is a catalog of surfaces, not a software list and not a second home for **CF-15** or **CJS-3.17**.

Where this file is silent, Sentient Constitution Chapters Two through Five govern. Where this file and `corpus_joint_structure.md` conflict, the stricter applicable requirement governs.

<a id="cs-5-12-in-scope-catalog"></a>
## CS-5.12 In-scope catalog

*In plain terms: for each reachable act, open the owner named here — this table does not restate those rules.*

The rows below are **pointers**. Operative detail stays on the cited home. Class scaling stays in **CS-3 — System classification and handling** and **CS-4 — Critical system stewardship**. Do not treat this table as a product catalog or as a reason to lock a technical implementation.

| Capability | Owner (do not restate) | Channel note |
|---|---|---|
| Revoke, rotate, and correct identity and attribution credentials | [CS-2 §1.1](cs_02_a_information_types_and_handling.md#11-identity-self-ownership-and-recoverability) | Analog may satisfy |
| Export or migrate continuity-critical data on disclosed paths | [CS-2 §1.2](cs_02_a_information_types_and_handling.md#12-continuity-critical-collection-and-exportability); **CJS-3.17** (*collection-time exportability*) | Analog may satisfy unless the owner already requires a usable export format |
| Inspect Type O baseline; challenge class, data-types, and certification records | [CS-2 §7](cs_02_a_information_types_and_handling.md#cs-2-7-type-o-baseline-for-class-a-b-c-systems); [CS-2 §8](cs_02_a_information_types_and_handling.md#cs-2-8-system-data-types-record-governance); [CS-3.7](cs_03_a_system_classification_machinery.md#cs-3-7-classification-governance-disclosure-and-challenge) | Mixed: where lawful online publication exists, the Type O floor is not a paywalled insider-only page |
| Challenge, review, and redress entry | [Article XII-B](../core_06_rights_part_c.md#article-xii-b-right-to-challenge-review-and-redress) | Analog may satisfy |
| Reconstruct what the system did; qualified audit access | [CS-2 §5.3](cs_02_a_information_types_and_handling.md#53-tiered-transparency-and-audit-access); **CJS-3.3** (*How we audit*) | Mixed: class-scaled logs |
| Proportional comprehensibility; summaries plus drill-down | **CS-6**; **CJS-3.8** (*comprehensibility and cognitive accessibility terms*) | Mixed |
| Digital self-service enroll, manage, exit, and charge-exit | **CJS-3.17** (*digital self-service pathway integrity*; *commitment, renewal, and charge-exit integrity*); **CI-8.3** | Digital **when entry was already digital**; this row does not force a digital channel where none was used |
| Inspectable attributable-action log (five-element set) | [CS-4 §10](cs_04_critical_system_stewardship.md#10-inspectable-attributable-action) | Mixed; role-scoped — not a public surveillance dashboard |
| Chokepoint appeal, human review, and export | [CS-4.14](cs_04_critical_system_stewardship.md#cs-4-14-private-chokepoints-sentients-depend-on-access-continuity-and-non-capture) | Mixed |
| Crisis communications for high-impact systems | [CS-5 §8](cs_05_design_testing_verification_deployment.md#cs-5-8-governance-continuity-crisis-communications-and-exercises-high-impact-systems) | Analog may satisfy |
| Tamper-evident offline audit chains | [CS-12.5](cs_12_decentralized_continuity_partition_resilience.md#cs-12-5-offline-audit-integrity-and-reconciliation) | Machine-usable chain required |
| Contest post-sale access or subscription cutoffs | [Article II-D](../core_06_rights_part_a.md#article-ii-d-post-sale-access-and-subscription-integrity); when the cutoff is digital self-service, **Article XII-B** plus **CJS-3.17** / **CI-8.3** | Do not invent a second challenge home |
| Accessibility accommodations in participation domains | [Article V-G](../core_06_rights_part_b.md#article-v-g-accessibility); **CJS-3.8**; **CI-15**; **CF-11** | Parity on whatever channel the domain already uses — not a separate product |

Each Class A, Class B, and Class C system must publish its own Type O floor. This file does **not** require a federated directory of all in-scope systems.

<a id="cs-5-13-analog-digital-and-channel-class"></a>
## CS-5.13 Analog, digital, and channel class

*In plain terms: paper, hearing, notice, or manual continuity can satisfy unless the owner already requires a digital or machine-usable channel — and digital self-service must not make exit harder than the channel that was actually used.*

This constitution defines required capabilities and outcomes. Analog forms — paper, hearing, published notice, and manual continuity — satisfy a catalog row unless the cited owner already requires a digital or machine-usable channel for that act.

**CJS-3.17** (*digital self-service pathway integrity*) and **CI-8.3** apply when entry was already digital. They require same-channel-class self-service and charge-exit on that channel. They do **not** force a digital channel onto a system that never used one.

**CS-12.5** requires tamper-evident offline chains where that section applies. Schema validators and other machine-checkable forms in `implementation/` instantiate owners already in this catalog; they are process support and cannot narrow the owner.

Do not treat “user-facing” as “must be an app.”

<a id="cs-5-14-what-this-file-does-not-own"></a>
## CS-5.14 What this file does not own

*In plain terms: standing, forum dockets, voting, and remedy stay where they already live; do not build a portal that quietly opens a standing record or pretends to be a second forms book.*

**Constitutional-operating surfaces** — standing records, forum intake and standard records, collective choice, seat catalogs, and remedy offices — are **not** owned here. They remain with Chapters Seven through Twelve, **CF**, and **CI**. Integrator inventory of those surfaces (process support; cannot narrow; not a second **CF-15**): [`evidence/2026-09-10/cs_user_facing_software_audit.md`](../evidence/2026-09-10/cs_user_facing_software_audit.md).

**Silence default.** Do not invent a standing portal for everyone. [Chapter Eight §2.1](../core_08_standing_assessment.md#21-silence-is-the-default) — silence is the default; most sentients never have a standing record. A filed case is not standing by itself. Tools under [Chapter Eight §3.5](../core_08_standing_assessment.md#35-implementation-tools) are optional and must not bury required fields in a score.

**No unified subject-access product.** Integrators may compose existing surfaces (identity control, inspect-if-open standing records, **Article VIII-B** experiential and derived data). Composition must **not** defeat the Chapter Eight silence default.

**No CS-13.** User-reachable in-scope surfaces stay in this Part A catalog. Constitutional-operating surfaces stay with their existing owners. Do not mint a “required software” family.

---

**Previous file:** [cs_05_design_testing_verification_deployment.md](cs_05_design_testing_verification_deployment.md)

**Next file:** [cs_06_comprehensibility_complexity_stewardship.md](cs_06_comprehensibility_complexity_stewardship.md)
