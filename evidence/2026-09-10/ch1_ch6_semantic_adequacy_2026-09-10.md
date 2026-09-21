# Semantic adequacy of the principle-to-article maps

**Date:** 2026-09-10
**Scope:** Chapter One → Chapter Six article traces (Lane A citation fidelity; three parent Traces filled where the honest extractor found no live Chapter One cite)
**Not this pass:** keyword-inferred basis as doctrine; remaining Chapter Five fossil labels (`[4.1 Safety]` still appears in some `core_05_*` files)

The 2026-09-10 structural alignment pass reported 124/124 articles with a “direct Chapter One basis.” That count treated fossil labels and keyword inference as if they were live principle cites. This note records the semantic review of those maps, what was retargeted, and what still is not a principle-owner map.

Indexes point. Source binds. Direct traces below were checked against live Chapter One headings in `core_01_a_values_principles.md`, `core_01_b_interaction_interpretation.md`, and `core_01_c_stewardship_capacity_principles.md`.

## How to read the map

Three different things were being called “Chapter One basis”:

| Layer | What it is | Adequacy |
|---|---|---|
| **Href** | Markdown target on a `core_01_*.md#…` link | The intended live principle, in almost every article Trace |
| **Label** (before this pass) | Link text such as `4.1 Safety`, `10.1 Core Tradeoff`, `Chapter One §8.21` | Pre-renumber nicknames. Live §4.1 is Resilience, live §10.1 is Governance as Authorized Structure, and §8.16/§8.20/§8.21/§8.24 are not Chapter One headings |
| **Inferred basis** | `PRINCIPLE_RULES` keyword hits on title+body | Advisory haystack. Not an owner map |

`tools/ch1_ch6_alignment_audit.py` previously extracted the **label** number, not the fragment. After this pass it resolves `core_01_*#fragment` to the live heading, ignores the fossil nickname `Chapter Twelve Chapter One §N`, and drops unlinked `Chapter One §N` cites that are not live headings.

**Inferred basis remains keyword soup.** Typical dumps still include §2, §3.1, §6.1–§6.3, §7, §8, §9, §9.2, §10, §10.1, §11–§13 whenever an article mentions harm, governance, capacity, or audit. Do not treat that column as the semantic map. Use Trace `Upstream: Principles:` and boxed operative text.

## Defects found

### 1. Fossil Chapter One numbers on correct hrefs (high; fixed)

House form after the 2026-06-16 Chapter One split is `[§3.1 Safety](core_01_a_values_principles.md#31-safety-harm-constraint)`. Many Chapter Six traces still said `4.1 Safety` (href already pointed at §3.1). Live §4.1 is **Resilience and Self-Healing Design**, so the published matrix was reporting the wrong live principle.

Confirmed old → live pairs used in Chapter Six traces:

| Fossil label | Live home |
|---|---|
| 4.1 Safety | §3.1 Safety |
| 4.2 Truth | §3.2 Truth |
| 3. Foundational Objective: Wellbeing | §2 Wellbeing |
| 5. Trust | §4 Trust |
| 8.1.1 Proportionality | §6.1.3 Proportionality |
| 8.1.2 Necessity | §6.1.1 Necessity |
| 9.2 Epistemic Disclosure Constraints | §6.2 Epistemic Disclosure Constraints |
| 7.2.1 Preservation of Epistemic Integrity | §6.2.1 Preservation of Epistemic Integrity |
| 7.3.1 Alignment Requirement | §11.1 Alignment Requirement |
| 10.1 Core Tradeoff Principles | §6.1 Core Tradeoff Principles |
| 9. Systemic Evaluation Requirement | §14 Systemic Evaluation Requirement |
| 8. Prohibition on Absolute Override (`#7-prohibition-on-absolute-override` in a Chapter Six file) | §7 in `core_01_b_interaction_interpretation.md` |

Href targets were already the right principles. Labels were retargeted; duties were not rewritten. Obligation inventory 678/678 1:1 (`evidence/2026-09-10/obligation_inventory_diff_ch1_ch6_semantic.json`).

### 2. Chapter Five clusters labeled as Chapter One §8.xx (high; fixed)

These are leftover cluster nicknames from when Def.* clusters sat in Chapter One §8.2–§8.16. Links already went to Chapter Five homes:

| Fossil cite | Live home |
|---|---|
| Chapter One §8.21 | Chapter Five *Indigenous Continuity, Language, Culture, and Heritage* (`core_05_band_continuity.md#indigenous-continuity-language-culture-heritage-semi-independent`) |
| Chapter One §8.16 | Chapter Five *Assembly, Collective Organization, and Institutional Formation* |
| Chapter One §8.20 | Chapter Five *Governance Architecture… Exit-Path Integrity* |
| Chapter One §8.24 | Chapter Five *Movement, Refuge, Non-Statelessness, and Exit Integrity* |

They inflated `direct_ch1_refs` as 8.16 / 8.20 / 8.21 / 8.24. Those are not live Chapter One sections (`doc_architecture.md` NAV-PRE-RELEASE-FRAGMENT-01: one current fragment id; no fossil labels).

### 3. Unlinked body fossils (high; fixed)

| Fossil | Live home | Why high-confidence |
|---|---|---|
| **Chapter One §6.3.1** (*Rights-Collision Decision Test*) | §6.1.5 (decision-record / rights-collision home under the least-restrictive form) | Same nickname already linked to `#615-rights-collision-decision-test` in traces; no live §6.3.1 heading |
| **Chapter Twelve Chapter One §8.1** | [Chapter Twelve §4.1](../../core_12_governance.md#41-entitlement-and-eligibility) (*Political-equality floor* / *Durable political-voice floor*) | Extractor treated this as Chapter One §8.1 (Constitutional No-Bypass). The parenthetical already named the Chapter Twelve floors |
| **Chapter One §9** non-concentration | §13 Market Structure | Adjacent articles already cite live §13 / §13.1 for the same duty |
| **§11.3** concentration-threshold (Article VIII-D Trace) | §13.1 | Live §11.3 is Misalignment Detection; the next bullet already linked §13.1 |

### 4. Missing parent Traces (high; filled)

After fossil Chapter Twelve §8.1 and Chapter Five §8.20/§8.24 were removed from the extractor, three top-level articles had **no live Chapter One cite** (keyword inference only):

| Article | Owner principles now in Trace |
|---|---|
| **V** *Equal Basic Rights* | §2.1 Fairness, §5 Freedom, §2 Wellbeing |
| **XI** *Stakeholder System Participation, Representation, and Due Process* | §5 Freedom, §8.1 No-Bypass, §10 Governance Under Stewardship Discipline |
| **XVIII** *Standing and Participation Status* | §5 Freedom, §8.1 No-Bypass, §8 Constitutional Interpretation |
| **XIX** *Interoperability, Portability, Movement, Refuge, and Exit Integrity* | §5 Freedom, §5.1 Limitation Discipline, §13 Market Structure |

Those Traces name the principle owners already used by child articles or by the article’s operative stack. They do not add duties. Article V’s body already applies the Rights-Floor Minimums Principle; the new Trace supplies the missing numbered Chapter One owners.

## Family review (href / now-live labels)

Privilege **Trace `Upstream: Principles:`** over inferred dumps. Chapter Six §1 already reads every article with the default constraint stack (Safety, Truth, Necessity, Proportionality, §6 process, Tetrad scaling, §11 where capture is material). Child traces that repeat §6.1 / §6.1.5 on restriction articles are the collision stack, not a missing owner.

| Family | Representative | Owner fit |
|---|---|---|
| Survival / resources (I–IV) | I cites §2, §3.1, §3.2, §6, §10. I-A Wellbeing + Safety; I-B Truth + §6.2; I-C Wellbeing + Safety + §14 | Adequate. Environmental Survival is Wellbeing/Safety owned; footprint articles correctly pull Truth/disclosure |
| Equality / access (V–VIII) | V now Fairness + Freedom + Wellbeing. V-B Fairness + Freedom + §6.1 + §6.1.5. V-G now includes §3.4 Plain-Language Accessibility (was an unlinked fossil “§4.1 Accessibility row,” which would have mapped to live Resilience) | Adequate. V-H still reads the Chapter Five assembly cluster rather than also citing Chapter One §5.3; that is a remaining thin owner, not a wrong href |
| Agency / participation (IX–XI) | IX Freedom + Safety + §6 + §11 + §13. XI now Freedom + No-Bypass + §10 | Adequate. XI had been a false §8.1 from the Chapter Twelve nickname |
| Systems / trust / audit (XII–XVII) | XII Wellbeing + Safety + Trust + §6 + §11. XIV still Truth-led | Adequate for trust/reliability. XIV is thin if read as only Truth; §6.2 and §4 Trust are in children and in the chapter-wide stack |
| Standing / interpretation (XVIII–XXII) | XVIII now Freedom + No-Bypass + §8. XIX Freedom + Limitation + Market Structure; body still reads the Chapter Five movement/lock-in clusters | Adequate. Standing is not Chapter Eight measurement; the new Trace does not relocate owner layers |
| Justice / emergency / transition (XXIII–XXVI) | Safety + §6.1 + §6.1.5 + §7 / §15 as traces already had | Adequate. Collision-stack density is expected |

## What this pass did not change

- **Inferred-basis column** — still not a semantic map. `10.2` was removed from `PRINCIPLE_RULES` (no live §10.2). Collision keywords now also infer §6.1.5. That is extractor hygiene, not doctrine.
- **Chapter Five files** still contain fossil labels such as `[4.1 Safety]` and `[8.1.1 Proportionality]` on correct hrefs. They are outside the Chapter Six principle-to-article map.
- **Edition label** — untouched.
- **Chapter Eleven §4.2** (Technical Forum Domains) remains a live *Chapter Eleven* cite in Chapter One §3.3; it is not a Chapter One §4.2.

## Checks

- `make`-equivalent: `python3 tools/ch1_ch6_alignment_audit.py --repo-root . --output-dir evidence/2026-09-10` → **PASS**, 124/124 direct live Chapter One basis
- `python3 tools/obligation_inventory_diff.py --compare evidence/2026-09-10/obligation_snapshot_ch1_ch6_semantic.json` → 678/678 1:1
- `python3 tools/local_markdown_fragment_audit.py` → PASS
- `python3 tools/section_label_anchor_audit.py` → PASS

## Follow-on (not blocking this map)

1. Retarget remaining `[4.1 Safety]` / `[4.2 Truth]` / `[10.1 Core Tradeoff]` labels in Chapter Five traces (same Lane A pattern).
2. Optionally cite Chapter One §5.3 on Article V-H alongside the Chapter Five assembly cluster.
3. Treat inferred-basis as a maintainer haystack only; do not tighten articles to match it.
