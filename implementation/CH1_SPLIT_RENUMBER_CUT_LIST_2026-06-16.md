# Chapter One split and renumber — cut list and migration spec

**Status:** Applied (2026-06-16) — Chapter One split, Part B renumber, Chapter Five definitions (P3), corpus-wide link migration, edition `SC-Corpus-2026.04.33`. **2026-06-16 follow-up:** Part filenames reordered to `core_01_a_values_principles.md` / `core_01_b_stewardship_capacity_principles.md` (Chapter Five `_a_`/`_b_` convention; fixes reverse alphabetical sort).  
**Date:** 2026-06-16  
**Scope:** Split `core_00-01_principles.md` into three files; renumber Chapter One Part B §§6–13 per stewardship → governance → capacity hierarchy.

---

## 1. Target file family

| File | Chapter | Title | Source lines (current `core_00-01_principles.md`) |
|---|---|---|---|
| `core_00_preamble.md` | **00** | Preamble / Foundational Requirements | L6–L45 (after file header) |
| `core_01_a_values_principles.md` | **01, Part A** | Values Principles | L48–L631 (through end of §5.1; **exclude** L632–L665 legacy redirect block) |
| `core_01_b_stewardship_capacity_principles.md` | **01, Part B** | Stewardship, Capacity, and Constitutional Safeguards | L666–L1833 (reordered + renumbered) |
| `core_00-01_principles.md` | — | **Removed (pre-release)** | Former redirect stub; legacy anchors live in `core_00_preamble.md` and `core_01_a_values_principles.md`. |

**Reading order:** `core_00_preamble.md` → `core_01_a_values_principles.md` → `core_01_b_stewardship_capacity_principles.md` → `core_02-04_definition_mechanics.md`

**`tools/corpus_paths.py` CORE_FILES** — replace `core_00-01_principles.md` with the three files above (stub omitted if fully migrated).

---

## 2. Physical cut boundaries

### 2.1 `core_00_preamble.md`

```
CUT START: L6  ## CHAPTER 00: PREAMBLE
CUT END:   L45 (blank line before ---)
```

**New file header (replace L1–L4):**

```markdown
# Sentient Constitution — Preamble

This file is **part of the Sentient Constitution** and is **binding only together** with the other numbered `core_*` files read as one instrument. It contains **Chapter 00** (preamble / foundational requirements). Reading order and edition metadata: [README.md](README.md).

**Next:** [core_01_a_values_principles.md](core_01_a_values_principles.md) (Chapter One, Part A — Values Principles).
```

**Preamble link fixes (in cut content):**

| Old | New |
|---|---|
| `[Chapter One, §2 Purpose and Role](#2-purpose-and-role)` | `core_01_a_values_principles.md#2-purpose-and-role` |
| `[§3.2 Recognition…](#32-recognition-reinforcement-and-aspiration)` | `core_01_a_values_principles.md#32-recognition-reinforcement-and-aspiration` |
| `Chapter One` (generic, L27) | `Chapter One` (still valid; add Part A/B note in L34 bullet) |

**Anchors retained in preamble file:** `#constitutional-triad`, `#material-stake`, `#material-family-orientation`

---

### 2.2 `core_01_a_values_principles.md`

```
CUT START: L48  ## CHAPTER 01: PRINCIPLES AND CONSTRAINTS
CUT END:   L631 (end of §5.1 Resilience and Self-Healing Design)
EXCLUDE:   L632–L665 (legacy redirect anchor HTML comment block — migrate to Part B stub)
```

**New file header:**

```markdown
# Sentient Constitution — Values Principles (Chapter One, Part A)

Binding only together with other `core_*` files. **Chapter One, Part A** — §§1–5 (interpretation, aims, wellbeing, Safety/Truth, Trust).

**Upstream:** [core_00_preamble.md](core_00_preamble.md)  
**Next:** [core_01_b_stewardship_capacity_principles.md](core_01_b_stewardship_capacity_principles.md) (Chapter One, Part B).
```

**Chapter heading:** change to `## CHAPTER 01, PART A: VALUES PRINCIPLES`

**Intra-file trace updates (Part A only):** replace downstream refs to old Part B sections:

| Old ref pattern | New ref |
|---|---|
| `#7-stewardship-and-distributed-understanding` | `core_01_b_stewardship_capacity_principles.md#6-stewardship-and-distributed-understanding` |
| `#6-shared-system-capacity` | `core_01_b_stewardship_capacity_principles.md#8-shared-system-capacity` |
| `#814-minimization-of-avoidable-burden` | `core_01_b_stewardship_capacity_principles.md#914-minimization-of-avoidable-burden` |
| `#91-required-evaluation-factors` | `core_01_b_stewardship_capacity_principles.md#101-required-evaluation-factors` |
| `#92-incentive-alignment-and-system-capture` | `core_01_b_stewardship_capacity_principles.md#7-governance-under-stewardship-discipline` |
| `#922-stewardship-and-operator-incentive-alignment` | `core_01_b_stewardship_capacity_principles.md#74-stewardship-and-operator-incentive-alignment` |
| `#11-prohibition-on-absolute-override` | `core_01_b_stewardship_capacity_principles.md#12-prohibition-on-absolute-override` |
| `#821-preservation-of-epistemic-integrity` | `core_01_b_stewardship_capacity_principles.md#921-preservation-of-epistemic-integrity` |
| `#822-trust-truth-alignment` | `core_01_b_stewardship_capacity_principles.md#922-trust-truth-alignment` |

**Anchors retained in Part A:** `#two-constitutional-aims`, `#flourishing`, `#continuity`, all §1–§5 anchors unchanged.

---

### 2.3 `core_01_b_stewardship_capacity_principles.md`

**Assembly order (not current file order):**

1. New file header + principle hierarchy intro (new prose)
2. Legacy redirect anchor block (from L632–L665, **extended** — see §4)
3. New Part B arc paragraph (replaces L659–L665)
4. **§6** — body from old L874–L1068 (old §7)
5. **§7** — new framing §7.1–7.2 + body from old L1520–L1688 (old §9.2)
6. **§8** — body from old L669–L871 (old §6)
7. **§9** — body from old L1070–L1202 + L1305–L1411 (old §8; subsections renumbered)
8. **§10** — body from old L1413–L1518 (old §9.1 only) + new §10.2 pointer to §7
9. **§11** — old L1690–L1734 (old §10)
10. **§12** — old L1736–L1767 (old §11)
11. **§13** — old L1769–L1808 (old §12)
12. Vocabulary index from L1810–L1830 (update section refs)
13. Footer: **Next file** → `core_02-04_definition_mechanics.md`

---

## 3. Section renumber map (old → new)

| Old § | New § | New title |
|---|---|---|
| §7 | **§6** | Stewardship and Distributed Understanding |
| §9.2 | **§7** | Governance Under Stewardship Discipline |
| §6 | **§8** | Shared-System Capacity |
| §8 | **§9** | Interaction and Conflict Resolution |
| §9.1 | **§10** | Systemic Evaluation Requirement |
| §10 | **§11** | Freedom (Bounded Agency) |
| §11 | **§12** | Prohibition on Absolute Override |
| §12 | **§13** | Integrated Application |

### 3.1 Subsection renumber (complete)

#### §6 Stewardship (was §7)

| Old | New |
|---|---|
| §7 | §6 |
| §7.1 Stewardship | §6.1 |
| §7.2 Distributed Understanding | §6.2 |
| §7.3 Institutional Development | §6.3 |
| §7.4 Openness Aspiration | §6.4 |
| §7.5 Bounds and Rights-Floor Disclaimer | §6.5 |

#### §7 Governance (was §9.2 + new framing)

| Old | New | Notes |
|---|---|---|
| *(new)* | §7.1 Governance as Authorized Structure | New prose; link Ch 11, Ch 5 `Governance` |
| *(new)* | §7.2 Short-Horizon Governance Defect | New prose; link Ch 5 definition (new) |
| §9.2 intro | §7 opening | Retain incentive-alignment lead-in |
| §9.2.1 | §7.3 Alignment Requirement |
| §9.2.2 | §7.4 Stewardship and Operator Incentive Alignment |
| §9.2.3 | §7.5 Role Depth and Material Responsibility Pathways |
| §9.2.4 | §7.6 Misalignment Correction and Capture Response |
| §9.2.5 | §7.7 Contingent Claims, Games of Chance, and Event-Contract Markets |

#### §8 Capacity (was §6)

| Old | New |
|---|---|
| §6 | §8 |
| §6.1 | §8.1 |
| §6.2 | §8.2 |
| §6.3 | §8.3 |
| §6.4 | §8.4 |
| §6.5 | §8.5 |

#### §9 Interaction (was §8)

| Old | New |
|---|---|
| §8 | §9 |
| §8.1 | §9.1 |
| §8.1.1–§8.1.4 | §9.1.1–§9.1.4 |
| §8.2 | §9.2 |
| §8.2.1–§8.2.2 | §9.2.1–§9.2.2 |
| §8.3 | §9.3 |
| §8.3.1–§8.3.2 | §9.3.1–§9.3.2 |
| §8.4 | §9.4 |
| §8.4.1–§8.4.2 | §9.4.1–§9.4.2 |

#### §10 Evaluation (was §9.1)

| Old | New |
|---|---|
| §9 (parent intro) | §10 (rewrite; drop §9.2 body) |
| §9.1 | §10.1 |
| §9.1.1–§9.1.5 | §10.1.1–§10.1.5 |
| *(new)* | §10.2 Read-with: Governance and Incentive Discipline → §7 |

#### §11–§13

| Old | New |
|---|---|
| §10 Freedom | §11 |
| §11 Prohibition | §12 |
| §12 Integrated Application | §13 |

---

## 4. Anchor ID migration

**Rule:** Every **primary** anchor gets a new canonical id matching the new section number. **All old ids** remain as empty redirect anchors in `core_01_b_stewardship_capacity_principles.md` (or retired stub) for one edition cycle.

### 4.1 Primary anchors (old → new)

| Old anchor | New canonical anchor | Section |
|---|---|---|
| `7-stewardship-and-distributed-understanding` | `6-stewardship-and-distributed-understanding` | §6 |
| `522-stewardship` / `71-stewardship` | `61-stewardship` | §6.1 |
| `521-distributed-understanding` | `62-distributed-understanding` | §6.2 |
| `92-incentive-alignment-and-system-capture` | `7-governance-under-stewardship-discipline` | §7 |
| `921-alignment-requirement` | `73-alignment-requirement` | §7.3 |
| `922-stewardship-and-operator-incentive-alignment` | `74-stewardship-and-operator-incentive-alignment` | §7.4 |
| `923-role-depth-and-material-responsibility-pathways` | `75-role-depth-and-material-responsibility-pathways` | §7.5 |
| `924-misalignment-correction-and-capture-response` | `76-misalignment-correction-and-capture-response` | §7.6 |
| `925-contingent-claims-games-of-chance-and-event-contract-markets` | `77-contingent-claims-games-of-chance-and-event-contract-markets` | §7.7 |
| `6-shared-system-capacity` | `8-shared-system-capacity` | §8 |
| `61-productive-capacity-instrumental-good` | `81-productive-capacity-instrumental-good` | §8.1 |
| `62-constitutional-efficiency` | `82-constitutional-efficiency` | §8.2 |
| `63-concentration-threshold-mechanism-adopter-tunable` | `83-concentration-threshold-mechanism-adopter-tunable` | §8.3 |
| `64-pro-competition-and-anti-domination` | `84-pro-competition-and-anti-domination` | §8.4 |
| `65-consolidation-ceiling` | `85-consolidation-ceiling` | §8.5 |
| `8-interaction-and-conflict-resolution` | `9-interaction-and-conflict-resolution` | §9 |
| `81-core-tradeoff-principles` | `91-core-tradeoff-principles` | §9.1 |
| `811-proportionality` | `911-proportionality` | §9.1.1 |
| `812-necessity` | `912-necessity` | §9.1.2 |
| `813-minimization-of-harm` | `913-minimization-of-harm` | §9.1.3 |
| `814-minimization-of-avoidable-burden` | `914-minimization-of-avoidable-burden` | §9.1.4 |
| `82-epistemic-disclosure-constraints` | `92-epistemic-disclosure-constraints` | §9.2 |
| `821-preservation-of-epistemic-integrity` | `921-preservation-of-epistemic-integrity` | §9.2.1 |
| `822-trust-truth-alignment` | `922-trust-truth-alignment` | §9.2.2 |
| `83-freedom-limitation-constraints` | `93-freedom-limitation-constraints` | §9.3 |
| `831-constraint-on-freedom` | `931-constraint-on-freedom` | §9.3.1 |
| `832-time-consistency-constraint` | `932-time-consistency-constraint` | §9.3.2 |
| `84-rights-collision-procedure` | `94-rights-collision-procedure` | §9.4 |
| `841-rights-collision-decision-test` | `941-rights-collision-decision-test` | §9.4.1 |
| `842-proxy-divergence-invalidation` | `942-proxy-divergence-invalidation` | §9.4.2 |
| `9-systemic-evaluation-requirement` | `10-systemic-evaluation-requirement` | §10 |
| `91-required-evaluation-factors` | `101-required-evaluation-factors` | §10.1 |
| `911-systemic-scope-and-risk-factors` | `1011-systemic-scope-and-risk-factors` | §10.1.1 |
| `912-accessibility-under-sentience-non-exclusion` | `1012-accessibility-under-sentience-non-exclusion` | §10.1.2 |
| `913-privacy-informational-joint-invocation` | `1013-privacy-informational-joint-invocation` | §10.1.3 |
| `914-voluntary-discontinuation-and-exit-rights` | `1014-voluntary-discontinuation-and-exit-rights` | §10.1.4 |
| `915-assembly-collective-organization-and-institutional-formation` | `1015-assembly-collective-organization-and-institutional-formation` | §10.1.5 |
| `10-freedom-bounded-agency` | `11-freedom-bounded-agency` | §11 |
| `11-prohibition-on-absolute-override` | `12-prohibition-on-absolute-override` | §12 |
| `12-integrated-application` | `13-integrated-application` | §13 |

### 4.2 New anchors to add

| Anchor | Section |
|---|---|
| `7-governance-as-authorized-structure` | §7.1 |
| `72-short-horizon-governance-defect` | §7.2 |
| `102-read-with-governance-and-incentive-discipline` | §10.2 |
| `chapter-01-part-b-stewardship-capacity-and-constitutional-safeguards` | Part B H2 |

### 4.3 Legacy redirect block (retain in Part B)

Keep existing pre-elevation ids from L632–L657 **plus** all superseded primary ids from §4.1 as:

```html
<!-- Legacy Chapter One anchor redirects (2026-06 split/renumber); do not remove without link migration. -->
<a id="6-shared-system-capacity"></a>
<a id="7-stewardship-and-distributed-understanding"></a>
…
```

---

## 5. New prose blocks (draft)

### 5.1 Part B — principle hierarchy (insert after H2)

```markdown
**Principle hierarchy (Part B).** At principle layer:

1. **Stewardship** ([Stewardship](core_05c_continuity_definitions.md#stewardship-constitutional)) orients systems toward durable constitutional alignment over time, including the **Continuity** aim under the [Two Constitutional Aims](core_01_a_values_principles.md#two-constitutional-aims).
2. **Governance** ([Governance](core_05a_accountability_definitions.md#governance)) structures authorized decision-making, participation, and accountability. Where governance and stewardship conflict, stewardship discipline controls at principle layer unless **Necessity** and **Proportionality** expressly justify a bounded, time-limited exception with correction paths. Operative authorization and contract-layer requirements remain owned by **Chapter Eleven**.
3. **Shared-System Capacity** ([Shared-System Capacity](core_05c_continuity_definitions.md#shared-system-capacity-constitutional)) is the durable, contestable ability those jointly produce — an **instrumental outcome**, not a freestanding trump value.

**Reading arc:** §6 stewardship → §7 governance discipline → §8 capacity → §9 tradeoffs → §10 whole-system evaluation → §§11–13 agency, integration, and override limits.
```

### 5.2 §7.1 Governance as Authorized Structure (new)

```markdown
#### 7.1 Governance as Authorized Structure

*In plain terms: governance tells you who may decide and how — but only counts when it stays under stewardship discipline and does not eat the future for today's metrics.*

**Governance** at principle layer means the structures, rules, allocation of authority, and processes by which already-authorized systems and institutions are directed and held accountable — as defined in Chapter Five and operationalized under **Chapter Eleven** for the **Constitutional Contract Layer** and stakeholder participation layers stated in [Chapter 00](core_00_preamble.md#chapter-00-preamble--foundational-requirements).

Governance is **necessary** but **not sufficient**. It must remain subordinate to **Stewardship** where procedural regularity, short-horizon optimization, or institutional self-protection would otherwise defeat durable alignment, **Continuity**, or Rights-Floor integrity.
```

### 5.3 §7.2 Short-Horizon Governance Defect (new)

```markdown
#### 7.2 Short-Horizon Governance Defect

*In plain terms: governance that keeps hitting quarterly targets while hollowing safety, truth, participation, or the future is not "working governance" — it is a defect this Constitution names and corrects.*

A **short-horizon governance defect** ([Short-Horizon Governance Defect](core_05c_continuity_definitions.md#short-horizon-governance-defect-constitutional)) is a material pattern that optimizes immediate output, convenience, institutional self-protection, or transient stability at the foreseeable expense of medium- or long-horizon constitutional alignment.

Systems must detect, disclose, and correct such defects through **Review and Correction Duty**, contestable oversight, and the incentive and capture discipline in **§§7.3–7.7**.
```

### 5.4 §8 opening (adapt from old §6 lead)

Replace old §6–§9 sequence paragraph with:

```markdown
*In plain terms: shared systems must keep building real productive capacity — but capacity is something stewardship and lawful governance produce and preserve, not a license to concentrate power.*

**§8** states **Shared-System Capacity** as an instrumental outcome downstream of **§6 Stewardship** and **§7 Governance Under Stewardship Discipline**. Capacity claims fail where they rest on domination, proxy divergence, irreversible lock-in, or governance that defeats the [Constitutional Triad](core_00_preamble.md#constitutional-triad).
```

### 5.5 §10.2 Read-with pointer (new)

```markdown
#### 10.2 Read-with: Governance and Incentive Discipline

Whole-system evaluation under **§10.1** is incomplete if it omits whether incentives and governance structures will preserve constitutional outcomes. Apply **§7 Governance Under Stewardship Discipline** for that discipline; **§10.1** does not duplicate **§7**.
```

### 5.6 §13 Integrated Application — arc rewrite

Replace "§§6–9" language with:

> Read together, **§§6–10** move from stewardship and governance discipline, to shared-system capacity, to tradeoff procedure, to whole-system validation.

---

## 6. Chapter Five definitions (draft O/E/C)

**Placement:** new semi-independent topic group in `core_05-05_definitions_b_semi_independent.md`, before or after existing `Stewardship, review, and correction` group.

**Topic group title:** `Stewardship, governance discipline, and shared-system capacity`

**Members:** Stewardship · Shared-System Capacity · Distributed Understanding · Short-Horizon Governance Defect · (amended) Governance · Strategic Stewardship Obligation · Stewardship Defect

### 6.1 Stewardship (new)

- **O:** The principle-layer orientation of systems, institutions, and authorized actors toward preserving constitutional alignment, repair capacity, distributed understanding, and long-horizon consequences — including ecological, intergenerational, and **Continuity**-aim effects — over time.
- **E:** Distinguish from governance form, documentation, consultation theater, or single-metric optimization. Assess foresight, correction, participation pathways, and incentive design across delayed, cumulative, systemic, and intergenerational effects. Read with **Strategic Stewardship Obligation** for operative duty on stewards and operators with material influence.
- **C:** Non-compliant where long-horizon duties are treated as optional, subordinated to short-horizon convenience or metric gaming without **Necessity** and **Proportionality**, or masked by non-functional stewardship posture after drift is reasonably foreseeable.

### 6.2 Shared-System Capacity (new)

- **O:** The durable, contestable ability of sentients and shared systems to achieve constitutionally aligned outcomes over time — including **Productive Capacity**, **Constitutional Efficiency**, anti-concentration discipline, and the participation, exit, and ecological preconditions that keep capacity real rather than hollow.
- **E:** Treat as an instrumental outcome produced and preserved through **Stewardship** and **Governance** operating under Values Principles (Chapter One, Part A). Apply **Productive Capacity**, **Constitutional Efficiency**, **Concentration Threshold**, and related definitions for component tests.
- **C:** Non-compliant where claimed capacity improvements materially degrade wellbeing, meaningful agency, dignity, ecological integrity, contestability, or constitutional review; or where capacity is asserted without traceable constitutional outcomes under Chapters Two through Four.

### 6.3 Distributed Understanding (new)

- **O:** Workable opportunities for materially affected sentients to learn how shared systems that affect them operate, with understanding scaled by **Materiality** and **Dependency**, supporting informed participation, stewardship, and contestability.
- **E:** Distinguish from nominal disclosure, jargon barriers, or summaries that misstate operative effect. Read with **Educational Agency**, **Transparency**, **Accessibility**, and **Article XX**.
- **C:** Non-compliant where understanding is withheld, obscured, or made practically unusable without **Necessity**, **Proportionality**, and applicable security limits.

### 6.4 Short-Horizon Governance Defect (new)

- **O:** A material governance pattern that optimizes immediate metrics, convenience, institutional self-protection, or transient stability at the foreseeable expense of medium- or long-horizon constitutional alignment, **Continuity**, or Rights-Floor integrity.
- **E:** Include uncorrected proxy divergence, permanent-emergency normalization, deferred safeguard maintenance, and incentive structures rewarding throughput over outcomes. Read with **Stewardship Defect** and **System Capture**.
- **C:** Non-compliant where such a pattern persists after risks or drift are reasonably foreseeable and correction was practicable.

### 6.5 Governance (amend existing O/E/C)

**Add to O (end):**

> At principle layer, **Governance** is subordinate to **Stewardship** where authorized structures, incentives, or procedures would otherwise permit foreseeable constitutional drift, Rights-Floor degradation, or short-horizon optimization that defeats durable alignment. Operative authorization requirements remain owned by **Chapter Eleven** and the **Constitutional Contract Layer**.

**Add to E:**

> Detect **short-horizon governance defect** where governance optimizes immediate outputs without revalidation against medium- and long-horizon constitutional outcomes.

**Add to C:**

> Non-compliant where governance arrangements normalize permanent emergency, suppress correction, or entrench capture while preserving nominal procedure.

### 6.6 Part C cluster (new)

**Cluster id:** `stewardship-governance-capacity-cluster`  
**Admission scope:** matters materially implicating principle-layer ordering, capacity claims, governance incentive structure, or long- vs. short-horizon tradeoffs.

---

## 7. Corpus-wide link migration

### 7.1 File path replacements

| Old | New |
|---|---|
| `core_00-01_principles.md` (preamble anchors) | `core_00_preamble.md` |
| `core_00-01_principles.md` (§§1–5) | `core_01_a_values_principles.md` |
| `core_00-01_principles.md` (§§6–13) | `core_01_b_stewardship_capacity_principles.md` |

**Triad / material stake / aims:** split by anchor — triad + material-stake → preamble or values file as listed in §4.

### 7.2 Bulk anchor replacements (regex-oriented)

Run in order after file split. Example patterns:

```
core_00-01_principles.md#7-stewardship-and-distributed-understanding
  → core_01_b_stewardship_capacity_principles.md#6-stewardship-and-distributed-understanding

core_00-01_principles.md#6-shared-system-capacity
  → core_01_b_stewardship_capacity_principles.md#8-shared-system-capacity

core_00-01_principles.md#92-incentive-alignment-and-system-capture
  → core_01_b_stewardship_capacity_principles.md#7-governance-under-stewardship-discipline

core_00-01_principles.md#922-stewardship-and-operator-incentive-alignment
  → core_01_b_stewardship_capacity_principles.md#74-stewardship-and-operator-incentive-alignment

core_00-01_principles.md#814-minimization-of-avoidable-burden
  → core_01_b_stewardship_capacity_principles.md#914-minimization-of-avoidable-burden

core_00-01_principles.md#constitutional-triad
  → core_00_preamble.md#constitutional-triad

core_00-01_principles.md#two-constitutional-aims
  → core_01_a_values_principles.md#two-constitutional-aims
```

Full mapping: generate from §4.1 via script `tools/ch1_split_link_migrate.py` (to be written).

### 7.3 High-touch files (manual review after bulk pass)

- `core_05-05_definitions_*.md` (~280 refs)
- `core_10-10_rights_part_*.md` (~315 refs)
- `core_11-11_governance.md`
- `README.md`, `doc_architecture.md`
- `ai_corpus/indexes/*.json`
- `tools/corpus_paths.py`, `tools/generate_definition_registry.py`

---

## 8. Execution phases

| Phase | Work | Verify |
|---|---|---|
| **P0** | Approve this cut list | Operator sign-off |
| **P1** | Create three files; retire or stub `core_00-01_principles.md` | Visual read; line counts |
| **P2** | Renumber Part B body + new §7 framing | Section walkthrough |
| **P3** | Insert Ch 5 definitions + amend Governance | `ch5_dec_widget_audit` |
| **P4** | Bulk link migration + README/doc_architecture | `rg 'core_00-01_principles'` → 0 binding refs |
| **P5** | Update `corpus_paths.py`, manifests, stable_id_index | `make regression` |
| **P6** | Edition bump `SC-Corpus-2026.04.33` (or next) | README edition table |

---

## 9. Verification checklist

- [x] Chapter One reads §1–§13 continuously across three files
- [x] No orphaned `core_00-01_principles.md#` links in binding `core_*` files
- [x] Legacy anchors resolve (stub or redirect block)
- [x] §13 arc references §§6–10 correctly
- [x] Chapter Ten default stack cites new § numbers
- [x] `make regression` clean
- [x] `tools/footer_audit.py` / `corpus_markdown_audit.py` pass (footer chain updated for split)
- [x] Chapter Five P3 definitions + dependent clusters §3.10–§3.15

---

**Next step:** Phase P1 — mechanical file split script or manual cut with `sed`/Python, then P2 renumber pass on Part B only.
