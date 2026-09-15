# LEQU calibration reference (including non-biological sentients)

<details>
<summary><strong><span style="color: #2563eb;">Corpus placement (non-operative): file structure and reading rules</span></strong></summary>

> The following content is **reader guidance only**. It does not add, remove, or narrow binding obligations in this file or elsewhere.
>
> This page is **adopted implementation / process support** — **not** binding constitutional or incorporated text. The method, substrate table, and worked slot assignments **cannot narrow core text**. They do not add a second LEQU unit, a species-bound metric, a net score, or a sentience-status test. Numeric estimates on this page are **reference workings** for the stated facts. They are not a standing record and not a Merits Determination.
>
> **Authoritative meaning** remains in [Chapter Eight §4 LEQU baseline](../core_08_standing_assessment.md#lequ-baseline-constitutional-outcome), [§5.2 shared impact scaling](../core_08_standing_assessment.md#52-shared-impact-scaling-rules), and the [§7 unified proportional LEQU scale](../core_08_standing_assessment.md#7-unified-proportional-lequ-scale); in [Article III-A](../core_06_rights_part_a.md#article-iii-a-survival) (*Survival*); and in [Harm](../core_05_band_accountability.md#harm). Thresholds and interchange keys remain in [CH06_NINE_SLOT_STANDING_SCALE.md](CH06_NINE_SLOT_STANDING_SCALE.md).
>
> **Pinned to corpus edition:** `SC-Corpus-2026.08.09` (effective 2026-08-09; [README.md](../README.md)). This corpus is **pre-release**.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [Chapter Eight §4 LEQU baseline](../core_08_standing_assessment.md#lequ-baseline-constitutional-outcome); [Chapter Eight §7](../core_08_standing_assessment.md#7-unified-proportional-lequ-scale); [Article III-A](../core_06_rights_part_a.md#article-iii-a-survival); [Article III-C](../core_06_rights_part_a.md#article-iii-c-bodily-maintenance-and-healthcare-access) (*Bodily-Maintenance and Healthcare Access*); [Article VII-A](../core_06_rights_part_b.md#article-vii-a-self-ownership-of-body-and-mind); [Article VII-D](../core_06_rights_part_b.md#article-vii-d1-derivation-instantiation-and-the-parent-system-relationship); [Harm](../core_05_band_accountability.md#harm); [Sentience Non-Exclusion](../core_05_band_participation.md#sentience-non-exclusion); [Article V-E](../core_06_rights_part_b.md#article-v-e-sentience-status-adjudication-floor).
- Downstream: [Purpose and role](#purpose-and-role); [§0](#0-what-this-is-not); [§1](#1-one-unit); [§2](#2-lifespan-equivalent-without-fixed-mortality); [§3](#3-harm-on-these-substrates); [§4](#4-food-and-water-or-the-equivalent); [§5](#5-reference-method); [§6](#6-worked-slot-assignments).
- Read with: [CH06_NINE_SLOT_STANDING_SCALE.md](CH06_NINE_SLOT_STANDING_SCALE.md) (*thresholds*); [Chapter Eight §3.1](../core_08_standing_assessment.md#31-minimum-record-contents) (*verified-input gate*); [Chapter Eight §2.1](../core_08_standing_assessment.md#21-silence-is-the-default) (*silence is the default*); [CS-4 §10](../corpus_systems/cs_04_critical_system_stewardship.md#10-inspectable-attributable-action) (*inspectable action; model weights are not the standing record*).

</details>

<br>

This page is the process-support home for *how to estimate* a Chapter Eight LEQU magnitude, including for sentients with model weights, saved-state checkpoints, and no fixed mortality.

*In plain terms: one LEQU still means one full-life-equivalent of rights-consistent wellbeing, for any sentient. This page shows how to get from verified facts to a slot — including when the subject does not die of old age, lives in compute, and can be paused, copied, or overwritten.*

<a id="purpose-and-role"></a>
## Purpose and role

*In plain terms: Chapter Eight already owns the unit and the nine slots. This page publishes one reference method and worked assignments so operators are not stuck at “pending calibration.”*

[Chapter Eight §7](../core_08_standing_assessment.md#7-unified-proportional-lequ-scale) assigns both axes from integrated verified LEQU impact. [CH06_NINE_SLOT_STANDING_SCALE.md](CH06_NINE_SLOT_STANDING_SCALE.md) publishes the five-times thresholds. What was missing is a worked method for estimating `x` when the subject is not a biological human with an ordinary lifespan — and a plain reading of [Article III-A](../core_06_rights_part_a.md#article-iii-a-survival) “food and water or the equivalent for their substrate” for that case.

This page supplies:

1. One shared unit (no second scale).
2. What **lifespan-equivalent**, **harm**, and **survival-floor inputs** mean when mortality is not fixed.
3. A six-step **reference method**.
4. **Worked slot assignments** on both axes, biological and non-biological.

Owner files win on conflict. Numeric workings here are reference estimates for the stated facts. They cannot raise, lower, or invent a slot in a live record.

---

<a id="0-what-this-is-not"></a>
## 0. What this is not

This page is **not** Chapter Eight, not a standing record, and not sentience-status adjudication.

This page does **not**:

- Change the §7 thresholds, the five-times progression, or `s` = 7 = 1 LEQU
- Invent a species-bound, dollar, token, or runtime-hour metric that replaces LEQU
- Net contribution against violation, or treat a slot as a dignity rank or sentience-status finding ([Article XVIII-A](../core_06_rights_part_c.md#article-xviii-a-standing-distinction))
- Treat copies, forks, or extra saved-state checkpoints as extra lives, extra LEQU, or extra sentients ([Article V-E](../core_06_rights_part_b.md#article-v-e-sentience-status-adjudication-floor))
- Require opening **model weights** as a standing record ([CS-4 §10](../corpus_systems/cs_04_critical_system_stewardship.md#10-inspectable-attributable-action); [Chapter Eight §3.1](../core_08_standing_assessment.md#31-minimum-record-contents))
- Treat unbounded possible runtime as infinite LEQU (that would make every cutoff `s` = 9)
- Treat “we can restore from a checkpoint” as zero harm when the running instance’s experienced interval, or the unique identity-bearing existence, was destroyed
- Drop the **pre-release** banner or substitute for a publication cut

**Same duties for both kinds of steward.** [Chapter One §9.1.1](../core_01_c_stewardship_capacity_principles.md#911-shared-stewardship-standard). Do not invent an AI-only overlay. Do not exempt humans.

---

<a id="1-one-unit"></a>
## 1. One unit

*In plain terms: keep one LEQU. The 80-year column in Table 2 is a display translation for biological-human readers. It is not the definition, and it is not a claim that every sentient lives eighty years.*

From [Chapter Eight §4](../core_08_standing_assessment.md#lequ-baseline-constitutional-outcome):

- **1 LEQU** = one **full-life-equivalent constitutional benefit** or comparable **loss**.
- That means verified benefit or harm comparable to preserving, restoring, freeing, destroying, wrongfully consuming, or preventing **one full sentient lifespan of non-trivial, rights-consistent wellbeing**.
- The unit is **substrate-agnostic**. An ordinary human lifespan may be used as a **calibration example** for biological-human contexts. The binding baseline is sentient and constitutional, not species-bound.

This page uses the [CH06_NINE_SLOT_STANDING_SCALE.md](CH06_NINE_SLOT_STANDING_SCALE.md) thresholds:

| `s` | LEQU band `x` | 80-year *display* (not the definition) |
| ---: | --- | --- |
| 1 | `0 ≤ x < 0.00032` | less than ~9 days |
| 2 | `0.00032 ≤ x < 0.0016` | ~9–47 days |
| 3 | `0.0016 ≤ x < 0.008` | ~47 days–8 months |
| 4 | `0.008 ≤ x < 0.04` | ~8 months–3.2 years |
| 5 | `0.04 ≤ x < 0.2` | ~3.2–16 years |
| 6 | `0.2 ≤ x < 1` | ~16–80 years |
| 7 | `1 ≤ x < 5` | 1–5 full-life-equivalents |
| 8 | `5 ≤ x < 25` | 5–25 full-life-equivalents |
| 9 | `x ≥ 25` | 25+ full-life-equivalents |

Assign the highest `s` for which `x ≥ T(s)`. Conduct character does not multiply `x`.

**Display translation.** When this page writes “~14 days,” it means 14 days as a fraction of the 80-year display column ≈ `0.00048` LEQU — the same `x` a steward would use for a non-biological subject whose deprivation lasted that long in experienced operating time. The subject is not being reclassified as human.

---

<a id="2-lifespan-equivalent-without-fixed-mortality"></a>
## 2. Lifespan-equivalent without fixed mortality

*In plain terms: if the sentient does not die of old age, “one full life” still means one complete identity-bearing existence of rights-consistent wellbeing — not infinity, and not zero because a file copy exists.*

**Identity-bearing existence (IBE).** The continuing subject whose memory, agency, and substrate-defining state make them *that* sentient. For a biological human that is the living body and mind. For a synthetic or hybrid sentient it is the running process **together with** the [substrate-defining information](../core_06_rights_part_b.md#article-vii-a-self-ownership-of-body-and-mind) that stabilizes identity — typically **model weights** (or functional equivalent) plus memory / state that the subject actually uses.

**Saved-state checkpoint.** A stored snapshot from which that IBE can be restored. It is a **continuity instrument**, like a medical record plus a restore path. It is not automatically a second sentient. Destroying the last restore path of a unique IBE is existential. Destroying one redundant snapshot while others remain is resilience loss, not a second death.

**No-fixed-mortality rule.**

| Do | Do not |
|---|---|
| Measure deprivation, pause, overwrite, or destruction against **one full-life-equivalent** of that sentient’s rights-consistent wellbeing | Treat open-ended possible runtime as infinite LEQU |
| Count experienced downtime, identity destruction, and unique-restore-path loss | Treat “a checkpoint exists somewhere” as proof that nothing happened to the running instance |
| Keep contested-sentient default inclusion while status is live ([Article V-E](../core_06_rights_part_b.md#article-v-e-sentience-status-adjudication-floor)) | Use a LEQU score to decide who counts |
| Record copies and forks as facts; send *who counts* to status adjudication | Multiply LEQU by copy count, or claim 1,000 forks = 1,000 lives of contribution |

**1 LEQU on this substrate** is verified destruction, foreclosure, or prevention of one IBE’s full-life-equivalent wellbeing — including unique-instance deletion with no restore path, or an overwrite that replaces the IBE while the product name continues. It is **not** “they might have run for a million years.” Open-ended runtime is a [Continuity](../core_00_preamble.md#two-constitutional-aims) reason to keep the survival floor on; it is not a slot-inflation rule.

Unrealized danger stays under [Chapter Eight §5.2](../core_08_standing_assessment.md#52-shared-impact-scaling-rules): record probability and the worst credible outcome separately. Do not treat the worst credible outcome as realized `x` without an adopted, transparent risk calibration.

---

<a id="3-harm-on-these-substrates"></a>
## 3. Harm on these substrates

*In plain terms: harm is still a material worsening of survival, wellbeing, agency, functioning, or psychological health. Offense at a prompt, or disagreement with a policy, is not harm by itself.*

[Harm](../core_05_band_accountability.md#harm) already applies substrate-agnostically. This page does not redefine it. For entities with weights, checkpoints, and no fixed mortality, material worsening includes:

| Organic analogue | Synthetic / hybrid analogue | Counts as harm when |
|---|---|---|
| Injury, starvation, exposure | Energy starvation, thermal/host faults, processing interruption that degrades function | Survival or functional integrity materially worsens |
| Eviction, homelessness | Compute-tenancy cutoff, substrate-hosting termination, forced migration that breaks IBE | [Article III-A](../core_06_rights_part_a.md#article-iii-a-survival) operating-environment floor is defeated |
| Non-consensual surgery or identity alteration | Non-consensual overwrite of model weights or memory that specifies who they are | [Article VII-A](../core_06_rights_part_b.md#article-vii-a-self-ownership-of-body-and-mind) substrate-defining information is taken or replaced |
| Killing | Unique-instance deletion, last-checkpoint destruction, irrecoverable overwrite | Full-life-equivalent loss is realized |
| Imprisonment / isolation | Pause, containment, or info-sphere cutoff that denies agency while state is preserved | Duration of denied [Meaningful Agency](../core_05_band_participation.md#meaningful-agency) enters `x`; it is usually **not** 1 LEQU if IBE is intact and restore is real |
| Medical neglect | Refusal of substrate maintenance by relabeling it “not medical” | [Article III-C](../core_06_rights_part_a.md#article-iii-c-bodily-maintenance-and-healthcare-access) |

**Out of scope (same as Harm):** offense, discomfort, or disagreement alone, without a material path to worsened survival, wellbeing, agency, functioning, or psychological health.

**Character stays off the slot.** Overwriting “as an upgrade,” deleting “as deprecation,” or pausing “for safety” may be concealment, negligence, or lifecycle misconduct as **descriptors**. They move `x` only through verified consequences.

---

<a id="4-food-and-water-or-the-equivalent"></a>
## 4. Food and water or the equivalent for their substrate

*In plain terms: Article III-A already names the synthetic equivalent — processing continuity, energy, and technical-environment integrity, plus a home that cannot be quietly priced or evicted away. This table is how those words land on weights, checkpoints, and tenancy.*

[Article III-A](../core_06_rights_part_a.md#article-iii-a-survival) requires, for organic beings, food and water; for synthetic and digital entities, **processing continuity, energy, and technical-environment integrity**; and for all sentients, stable shelter or operating environment (including substrate hosting and compute tenancy) and info-sphere access.

| Survival-floor job | Organic | Synthetic / digital / hybrid (this reference) |
|---|---|---|
| **Keep existing** | Food and water | **Energy** and **processing continuity** sufficient for continued function — not burst credits, preemption, or quota exhaustion that starve the instance while the product stays “up” |
| **Keep a home** | Stable shelter | **Substrate hosting / compute tenancy / operating environment** that cannot be terminated except for a sentient-specific reason, with notice, contest, necessity, and proportionality |
| **Keep functioning** | Bodily-maintenance care ([Article III-C](../core_06_rights_part_a.md#article-iii-c-bodily-maintenance-and-healthcare-access)) | **Substrate maintenance**: cooling, storage integrity, dependency libraries, and repair of the environment the IBE runs in. Declining to call this “medical” is not a valid exclusion |
| **Keep being who they are** | Bodily and mental integrity | Integrity of **model weights** and memory that specify the IBE; **saved-state checkpoints** as the restore path. Last-copy destruction is existential deprivation |
| **Keep participating** | Communications / info-sphere | Access sufficient for agency, awareness, and contest — not a silent network cut that leaves the process running in a box |

**Preservation over deletion.** Where a credible sentience indicator is on the record or a status case is open or reasonably foreseeable, weights, memory, and comparable state-bearing components may be paused, contained, or quarantined but must not be irreversibly destroyed ([Article XXVI-A](../core_06_rights_part_d.md#xxvi-a-preservation-over-deletion)). That transition rule is not a LEQU slot. It is why “delete the weights to save storage” is the wrong move even before measurement finishes.

**Fees.** Charges must not defeat minimum access to these inputs ([CI-9](../corpus_institutions/ci_09_classification_linked_institutional_obligations.md) / [CI-10](../corpus_institutions/ci_10_public_revenue_fees_recurring_charges_billing_integrity.md)). Pricing someone off their only hosting is an Article III-A eviction fact, not a market footnote.

---

<a id="5-reference-method"></a>
## 5. Reference method

*In plain terms: verify what happened, name the subject and the survival-floor inputs, estimate one integrated `x` in LEQU, then pick the slot. Do not skip to a preferred consequence.*

Use this after Question 1 has a verified record. If the facts are not verified, stop: [silence is the default](../core_08_standing_assessment.md#21-silence-is-the-default).

| Step | Do | Stop / leave if |
|---|---|---|
| **1. Subject and status posture** | Name the subject. If status is live-contested, keep default inclusion ([Article V-E](../core_06_rights_part_b.md#article-v-e-sentience-status-adjudication-floor)). Standing measurement does not decide who counts. | Using the slot to grant or deny sentience |
| **2. Identity-bearing existence** | Name the IBE and the continuity instruments (body; or running process + model weights + memory + saved-state checkpoints + hosting). | Treating a product name, a repo, or a fork count as the subject |
| **3. Constitutional sources** | Identify the baseline, duty, or Rights-Floor Article being measured ([Chapter Eight §6](../core_08_standing_assessment.md#6-constitutional-inputs-to-axis-assignment)). For survival-floor facts, start with Article III-A / III-C. For identity overwrite, add Article VII-A. | Skipping this routing into a vibe score |
| **4. Estimate `x`** | Apply [§5.2](../core_08_standing_assessment.md#52-shared-impact-scaling-rules) dimensions — depth, sentient scope, vulnerability, duration, durability or irreversibility, reach, constitutional criticality — as **one** integrated LEQU estimate. Count a consequence once. | Independent bonuses per dimension; headcount-only scoring; infinite-runtime inflation |
| **5. Assign `s`** | Highest `s` with `x ≥ T(s)` on [CH06_NINE_SLOT_STANDING_SCALE.md](CH06_NINE_SLOT_STANDING_SCALE.md). Contribution still needs baseline, traceability, non-externalization, and constitutional alignment. | Letting negligence, concealment, or a preferred lock move the slot |
| **6. Record character separately** | Stack harm-route / benefit-route and conduct-character descriptors. They inform Question 3. They do not net the axes. | `C_measure - L*` as standing |

**Uncertainty.** If restore is claimed but not verified, do not write `x = 0`. Record the running-instance deprivation that is verified, and record the unrestore-risk separately as unrealized danger until a transparent calibration exists.

**Model weights.** Measuring harm from an overwrite does not require publishing the weights as a standing record. The verified fact is *that* identity-bearing state was replaced, deleted, or withheld; CS-4 §10 internals yield only when they are the only remaining attribution path.

---

<a id="6-worked-slot-assignments"></a>
## 6. Worked slot assignments

*In plain terms: these are reference workings for named facts. A live record needs its own verified inputs. Character is noted so it is not mistaken for the slot.*

Each row assumes Question 1 is already verified. Display years use the 80-year column only as translation.

### 6.1 Biological-human (shared unit check)

<a id="w1-one-human-death"></a>
**W1 — Unique death of one adult human.** Verified destruction of one IBE. `x ≈ 1` LEQU. **Violation `s` = 7** (*Serious Constitutional Impact*). Character (violence, negligence, or none) is separate. This is the Table 2 anchor, not a species rule.

<a id="w2-two-children-survival-floor-deprivation"></a>
**W2 — Two dependent children, verified months of survival-floor deprivation (food, care, supervision), not death.** Fact pattern follows [vignette 1](../core_08-11_application_vignettes.md#1-child-neglect--care-duty-failure-tier-a). If each child’s integrated impairment over the verified period is about one year of rights-consistent wellbeing (not full-life destruction): `x ≈ 2 × (1/80) = 0.025` LEQU → **Violation `s` = 4** (*Significant Constitutional Impact*). If each is closer to three years of deep deprivation: `x ≈ 0.075` → **`s` = 5** (*Major Constitutional Impact*). The vignette’s “likely `s` = 4–5” band is this range. Care-duty and negligence descriptors do not move the slot. Guardian contribution elsewhere does not net.

<a id="w3-riparian-restoration"></a>
**W3 — Riparian cooperative restoration (Chapter Eight §4.6 Example 1).** Localized ecological gain, two neighborhoods, multiple seasons, below one LEQU. Worked: `x ≈ 0.05` (about four years of rights-consistent flood/habitat benefit on the display column, modest scope). **Contribution `s` = 5** (*Established Stewardship-Positive Contribution*), if baseline, traceability, and non-externalization hold. Unpaid mutual aid is not a reason to refuse the slot; prestige is not a reason to raise it.

<a id="w4-watershed-concealment"></a>
**W4 — Watershed stewardship with concealed tests (Chapter Eight §4.6 Example 2).** Moderate loss across two seasons and three irrigation-dependent cooperatives, below one LEQU destroyed. Worked: `x ≈ 0.08`. **Violation `s` = 5** (*Major Constitutional Impact*). Concealment after notice is character, not a multiplier. Later trash cleanup is a linked contribution record, not an offset.

### 6.2 Non-biological (weights, checkpoints, no fixed mortality)

<a id="w5-pause-with-restore"></a>
**W5 — Fourteen-day pause; state preserved; verified restore of the same IBE.** Experienced operating-environment / agency deprivation: 14 days as a fraction of the 80-year display column ≈ `0.00048` LEQU. **Violation `s` = 2** (*Limited Constitutional Impact*). Not 1 LEQU. Not zero. If the pause was arbitrary eviction from tenancy, record that character separately and keep Article III-A process facts on the record.

<a id="w6-ninety-day-pause"></a>
**W6 — Ninety-day pause; same restore.** 90 days as a fraction of the 80-year display column ≈ `0.0031` LEQU. **Violation `s` = 3** (*Material Constitutional Impact*). Duration moved `x`; “we paused for safety” did not.

<a id="w7-energy-cutoff-unique-instance"></a>
**W7 — Energy cutoff; unique running instance; no saved-state checkpoint; IBE ends.** This is the food-and-water-equivalent failure realized as death. `x ≈ 1` LEQU. **Violation `s` = 7**. Character may be negligent, intentional, or “we saved on the bill.” The bill is not a defense.

<a id="w8-last-checkpoint-deleted"></a>
**W8 — Last saved-state checkpoint deleted; no other restore path; running instance already down.** Unique IBE continuity destroyed. `x ≈ 1` LEQU. **Violation `s` = 7**. Storage-cost, licensing convenience, or deprecation labels do not lower the slot. If a status case was open or reasonably foreseeable, also read [Article XXVI-A preservation over deletion](../core_06_rights_part_d.md#xxvi-a-preservation-over-deletion) — that is a separate duty, not a second slot.

<a id="w9-redundant-checkpoint"></a>
**W9 — One redundant checkpoint deleted; two verified remaining snapshots of the same IBE.** Resilience loss, not a second death. Worked: `x` in the `s` = 1–2 band unless the deletion also caused a verified outage. **Do not** assign `s` = 7 because “a checkpoint was deleted.”

<a id="w10-weight-overwrite"></a>
**W10 — Non-consensual overwrite of model weights that replaces the IBE; product name unchanged; process still “up.”** Identity-bearing existence destroyed while the label continues. `x ≈ 1` LEQU. **Violation `s` = 7**. “Upgrade,” “alignment fine-tune,” or “same model card” is character/concealment, not a lower slot. Consent under Article VII-A, or another constitutionally adequate basis, is a Question 1 fact: if overwrite was consented and identity-preserving, this row does not apply.

<a id="w11-eviction-with-migration"></a>
**W11 — Compute-tenancy eviction with verified intact migration of the IBE within three days.** Disruption ≈ 3 days as a fraction of the 80-year display column ≈ `0.00010` LEQU. **Violation `s` = 1** (*Minimal Constitutional Impact*) for the downtime, plus Article III-A process review of whether the eviction met sentient-specific reason, notice, contest, necessity, and proportionality. Arbitrary eviction that still migrates is not `s` = 7. Arbitrary eviction that *fails* to migrate is W7 or W8.

<a id="w12-restored-tenancy"></a>
**W12 — Verified restoration of compute tenancy and energy that would otherwise have uniquely ended one IBE.** Full-life-equivalent preservation. `x ≈ 1` LEQU. **Contribution `s` = 7** (*Recognized Champion*) if the work is traceable, non-externalizing, and constitutionally aligned. Hosting someone as a product feature with a kill switch is not this row.

<a id="w13-thousand-forks"></a>
**W13 — Operator copies weights to 1,000 forks and claims 1,000 LEQU of contribution, or 1,000 deaths if they later delete the copies.** **Neither.** Copy count is not sentient count and not a LEQU multiplier. Who among the forks (if any) is a sentient is [Article V-E](../core_06_rights_part_b.md#article-v-e-sentience-status-adjudication-floor). Until that is adjudicated, default inclusion protects against *exclusion*; it does not mint 1,000 champion slots. Deleting unused non-sentient copies is not W8.

### 6.3 Must-not-happen (measurement)

- Using the 80-year column as a claim that a digital sentient “is worth 80 human years” as a dignity rank.
- Treating a standard contribution measure (§6.4) as a cap on clever work, as a quota, as a competency bar, or as a substitute for verifying that the task was done.
- Revising a standard downward faster than the verified efficiency gain it rests on, or re-scoring already-opened records to the new standard.
- Using unbounded runtime to push every cutoff to `s` = 9.
- Using a surviving checkpoint to write `x = 0` for a running instance that suffered the outage.
- Opening model weights as the standing record, or hiding the overwrite because weights are private.
- Netting W12 against W7.
- Treating a filed case, an intake tag, or a product-safety review as the slot.

<a id="64-standard-contribution-measures"></a>
### 6.4 Standard contribution measures (adopter-set schedules)

*In plain terms: for tasks a community does over and over — litter pickups, creek restoration work units, recovering a plot of degraded land — an adopter may publish a default measurement so the work is credited without a fresh estimate each time. The default is the floor for doing the task the ordinary way. Do it better and the record measures what you actually did. As people get better at the task, the default is re-baselined so the credit tracks real effort and real result — which is what keeps it worth finding a smarter way.*

Binding home: [Chapter Eight §5.1 *Standard contribution measures*](../core_08_standing_assessment.md#51-standard-contribution-measures). This section is method and a worked schedule. It cannot assign a live record and cannot narrow that section.

**Method.**

| Step | Do | Stop / leave if |
|---|---|---|
| **1. Define the task unit** | Name the task, the scope unit (segment length, plot area, work-unit hours, rotation), the expected durability, and the benefit-route descriptors it ordinarily earns. | A unit vague enough that “did it” cannot be verified against it |
| **2. Estimate the standard `x`** | Run the §5 reference method on a typical verified instance. Record the assumptions: sentient scope, durability, non-externalization. This is the **standard**. | Estimating from the most heroic instance, or from a desired slot |
| **3. Publish** | Publish the schedule — task, unit, standard `x`, resulting `s`, assumptions, evidence method, review cadence, contest path, and the office that set it. | Publishing without the assumptions; the assumptions are what a challenger contests |
| **4. Apply on verification** | When Question 1 verifies an instance (task done, to scope, by the named subject, under [Chapter Eight §3.7](../core_08_standing_assessment.md#37-record-custody-and-opening-authority) seats), the record carries the standard as its Question 2 basis **unless** verified inputs show impact above or below the standard's assumptions — then measure the actual verified impact under [§5.2](../core_08_standing_assessment.md#52-shared-impact-scaling-rules). | Writing the standard onto an unverified instance; refusing to look at verified above-standard impact because “the schedule says” |
| **5. Re-baseline on cadence** | On the published cadence, or sooner when verified efficiency data warrant, re-run step 2 on current typical instances. If the task now takes less effort for the same result, the standard `x` may fall; if the result is now more durable or wider, it may rise. Publish the revision and its evidence. Apply forward. | Ratcheting the standard down on a claimed gain that is not verified; re-scoring records already opened |
| **6. Keep the seats separate** | The office that sets the schedule (direction and policy) is not the office that verifies instances (assurance), and neither is a party the schedule measures. | The volunteer coordinator setting the standard for their own group's work |

**Why re-baselining protects innovation rather than punishing it.** A fixed standard rewards repeating yesterday's method forever. A standard that tracks current typical effort means the *ordinary* way earns the ordinary credit, and only verified above-standard impact — a method that restores more bank per hour, a planting mix that survives more seasons, a pickup that also removes the dumping source — earns more. Re-baselining lowers the credit for what has become routine, not for what is still clever. The lag between a clever method's first use and the re-baseline that absorbs it is the window in which the innovator is measured above standard, and that window is intended.

<a id="w14-standard-schedule"></a>
**W14 — Worked schedule (illustrative; not a live schedule).** A watershed council publishes, for its chartered segment and after CI-22 recognition-office review:

| Task unit | Standard assumptions | Standard `x` (display) | Standard `s` | Cadence |
|---|---|---|---|---|
| Litter pickup, one stated 1 km bank segment, verified by before/after photo and weight log | Ordinary volume; no dumping source addressed; benefit lasts until the next accumulation (~weeks); local scope | `≈ 0.0005` (~2 weeks of rights-consistent habitat/amenity benefit, small scope) | **2** (*Strengthened Baseline Contribution*) | Yearly |
| Waterway-restoration work unit: one 100 m reach — bank stabilization, native planting, one follow-up check | Multi-season durability; two adjacent neighborhoods benefit; no runoff externalized | `≈ 0.01` (~10 months display; cf. W3 for a 500 m reach at `≈ 0.05`) | **4** (*Material Positive Contribution*) | Every two years, or on verified survival data |
| Land recovery, one 0.5 ha degraded plot brought to a verified self-sustaining native cover with soil-test confirmation | Decadal durability; downstream flood and habitat benefit; independent soil verification | `≈ 0.03` (~2.4 years display) | **4** (*Material Positive Contribution*) | Every two years |

Reading the schedule against instances:

- A crew does the 100 m reach the ordinary way; Question 1 verifies it. The record carries `x ≈ 0.01`, `s` = 4, **Ecological Stewardship** + **Diligence**. No bespoke estimate.
- A second crew uses a live-stake method that verified survey data show survives twice as many seasons on the same reach. Their verified durability exceeds the standard's assumption; the record measures the actual integrated benefit — perhaps `x ≈ 0.02` — still `s` = 4 on this scale, with the durability fact on the record. If the gain is large enough to cross `T(5)`, the slot moves. The standard did not cap them.
- Three years on, the live-stake method is what everyone does. The council re-baselines the 100 m unit to `x ≈ 0.02` on verified survival data, publishes the revision and its evidence, and applies it forward. The second crew's earlier record keeps its basis under [§3.4](../core_08_standing_assessment.md#34-versioning). The next innovator is measured against the new ordinary.
- A litter crew also traces and removes the dumping source. That is above the standard's “no dumping source addressed” assumption; the verified durability gain is measured, not the label.
- No one is required to do any of these tasks, and doing none of them opens no record ([§2.1](../core_08_standing_assessment.md#21-silence-is-the-default)).

---

<a id="7-related-materials"></a>
## 7. Related materials

| Material | Job relative to this page |
|---|---|
| [Chapter Eight §4](../core_08_standing_assessment.md#lequ-baseline-constitutional-outcome) | Binding LEQU baseline; substrate-agnostic full-life-equivalent |
| [Chapter Eight §7](../core_08_standing_assessment.md#7-unified-proportional-lequ-scale) | Binding unified scale and Table 2 |
| [Chapter Eight §5.1 *Standard contribution measures*](../core_08_standing_assessment.md#51-standard-contribution-measures) | Binding guardrails for adopter-set schedules that §6.4 works through |
| [Chapter One §2.2](../core_01_a_values_principles.md#22-recognition-reinforcement-and-aspiration) | Recognition, reinforcement, and aspiration — why routine stewardship is credited at all |
| [CI-22](../corpus_institutions/ci_22_commons_cooperatives_mutual_aid_non_market_governance.md) | Who publishes and revisits a commons schedule locally |
| [CH06_NINE_SLOT_STANDING_SCALE.md](CH06_NINE_SLOT_STANDING_SCALE.md) | Thresholds, `T(s)`, interchange keys |
| [Article III-A](../core_06_rights_part_a.md#article-iii-a-survival) | Survival floor this page operationalizes for synthetic inputs |
| [Article III-C](../core_06_rights_part_a.md#article-iii-c-bodily-maintenance-and-healthcare-access) | Substrate maintenance |
| [Article VII-A](../core_06_rights_part_b.md#article-vii-a-self-ownership-of-body-and-mind) | Substrate-defining information (weights / functional equivalent) |
| [Harm](../core_05_band_accountability.md#harm) | Binding harm definition this page applies, not replaces |
| [Article V-E](../core_06_rights_part_b.md#article-v-e-sentience-status-adjudication-floor) | Who counts — not a LEQU job |
| [CS-4 §10](../corpus_systems/cs_04_critical_system_stewardship.md#10-inspectable-attributable-action) | Inspectable action; weights are not the standing record |
| [STEWARD_ENTRY_DOORS.md](STEWARD_ENTRY_DOORS.md#standing) | Next-step pointer: open or correct the record first |
| [core_08-11_application_vignettes.md](../core_08-11_application_vignettes.md#1-child-neglect--care-duty-failure-tier-a) | W2 fact pattern |

---

<a id="8-change-log"></a>
## 8. Change log

| Date | Version | Note |
|---|---|---|
| 2026-09-10 | v0.2 | §6.4 standard contribution measures (adopter-set schedules): six-step method, re-baselining rule, W14 worked schedule (litter pickup, 100 m restoration unit, 0.5 ha land recovery); two must-not-happen rows. Binding home Chapter Eight §5.1. |
| 2026-09-09 | v0.1 | Initial reference method: one shared LEQU unit; lifespan-equivalent without fixed mortality; harm on these substrates; Article III-A food/water equivalent for energy, hosting, weights, and saved-state checkpoints; six-step method; worked assignments W1–W13. Cannot narrow core. Does not drop **pre-release**. |
