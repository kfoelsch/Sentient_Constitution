# Disclaimer inventory (DISC-INV-01)

Auto-generated. Do not edit by hand.

Generated: 2026-07-07T04:29:32+00:00

Scopes **Chapter Five** band and aim files. Classifies disclaimer / negative-scope clauses on **O**, **E**, and **C** components using [tools/architecture/disclaimer_themes.json](../tools/architecture/disclaimer_themes.json).

Editorial model: **safe redundancy** = one canonical exposition + pointers (see [doc_architecture.md](../doc_architecture.md) §12).

## Summary

- **Total hits (actionable):** 110
- **Thin candidates:** 43
- **Review candidates:** 9
- **Keep (local boundary + canonical homes):** 58
- **Canonical exposition (do not thin):** 10
- **Same-theme duplicates across O/E/C (terms):** 13

### By recommended action

| Action | Count | Meaning |
| --- | ---: | --- |
| thin | 43 | Replace with Trace read-with / single C line |
| review | 9 | Triage per term — may stay local |
| keep | 48 | Term-pair or jurisdictional — do not fold |
| canonical | 10 | Canonical home for theme — retain |

### By O/E/C component

| Component | Hits |
| --- | ---: |
| O | 56 |
| E | 32 |
| C | 22 |

### By source file

| File | Hits |
| --- | ---: |
| core_05p_participation_definitions.md | 38 |
| core_05c_continuity_definitions.md | 28 |
| core_05a_accountability_definitions.md | 26 |
| core_05i_integrative_definitions.md | 10 |
| core_05o_oversight_definitions.md | 6 |
| core_05g_continuity_aim.md | 2 |

### By theme family

| Theme | Hits | Default action | Canonical home |
| --- | ---: | --- | --- |
| Rights-Floor jurisdiction / does not displace Ch6 | 37 | keep | core_06-06_rights_part_*.md; Trace routing |
| Proxy / engagement / self-report substitution | 20 | thin | core_05o_oversight_definitions.md Proxy Divergence; core_01_c_stewardship_capac… |
| Governance layer separation (authorization vs participation) | 19 | thin | core_00_preamble.md §4–§5; core_05i_integrative_definitions.md Constitutional C… |
| Neighbor term disambiguation (distinct from …) | 11 | keep | (local term pair — no global fold) |
| Pointer / does not restate elsewhere | 7 | thin | Trace widget links only |
| Anti-formalism / label-gaming evasion block | 6 | review | core_02-04_definition_mechanics.md Chapter Three §2.2.1; core_01_c_stewardship_… |
| Term-specific scope exclusion (does not include/govern/extend) | 3 | review | (local O boundary) |
| Symbolic / theater participation negative | 3 | thin | core_01_c_stewardship_capacity_principles.md §11; Participation definition |
| Not a substitute / backstops not substitutes | 3 | thin | core_01_c_stewardship_capacity_principles.md §9; core_01_b_interaction_interpre… |
| Global integrity negative (harm / deception / capture / proxy divorce) | 1 | thin | core_01_c_stewardship_capacity_principles.md §11.1.2; core_01_a_values_principl… |

## Intra-entry redundancy (same theme, multiple components)

Highest-yield thinning: drop duplicate theme on secondary components when one enforceable **C** line or principle-layer pointer remains.

| Term | Theme | Components |
| --- | --- | --- |
| Autonomous Coercion Tool | Anti-formalism / label-gaming evasion block | C, E |
| Combatant / Non-Combatant Distinction | Anti-formalism / label-gaming evasion block | C, E |
| Constitutional Contract Layer | Governance layer separation (authorization vs participation) | C, O |
| Constitutional Emergency and Contingency | Governance layer separation (authorization vs participation) | C, O |
| Derived Sentient | Rights-Floor jurisdiction / does not displace Ch6 | C, E |
| Developing Sentient | Rights-Floor jurisdiction / does not displace Ch6 | C, O |
| Emergency Pre-Deliberation Action (Binding Collective Choice) | Governance layer separation (authorization vs participation) | C, E |
| Foundational Constitutional Choice | Governance layer separation (authorization vs participation) | C, E, O |
| Graduated Capability | Rights-Floor jurisdiction / does not displace Ch6 | C, O |
| Parent-System Relationship | Rights-Floor jurisdiction / does not displace Ch6 | C, E |
| Self-Healing | Rights-Floor jurisdiction / does not displace Ch6 | C, O |
| Sentience Status Adjudication | Rights-Floor jurisdiction / does not displace Ch6 | C, O |
| Supremacy and Enforceability | Governance layer separation (authorization vs participation) | C, E, O |

## Thin candidates (sample)

| File | Line | Term | Comp | Theme | Excerpt |
| --- | ---: | --- | --- | --- | --- |
| core_05o_oversight_definitions.md | 267 | Materiality Determination | E | proxy_metrics | - **Primary assessment.** Include all effect types, including [Systemic Materiality](core_05a_accou… |
| core_05o_oversight_definitions.md | 580 | Transparency | E | proxy_metrics | - **Primary assessment.** Compare disclosure to [Material Impact](core_05o_oversight_definitions.md… |
| core_05o_oversight_definitions.md | 630 | Auditability | E | proxy_metrics | - **Primary assessment.** Must function across relevant conditions and [Stakeholders](core_05p_part… |
| core_05o_oversight_definitions.md | 863 | Truth (Constitutional Constraint) | E | proxy_metrics | - **Primary assessment.** Evaluate substantive effect on informed decision-making and auditability… |
| core_05o_oversight_definitions.md | 886 | Epistemic Integrity | E | proxy_metrics | - **Primary assessment.** Require proportionate methodological transparency within safety and secur… |
| core_05p_participation_definitions.md | 277 | Lifespan Equivalent Unit (LEQU) | O | pointer_disclaimer | Shorthand for a **Lifespan Equivalent Unit** — the numeric or narrative unit adopted implementation… |
| core_05p_participation_definitions.md | 368 | Participation | O | layer_separation | Principle-layer duty that materially affected sentients and [Stakeholders](core_05p_participation_d… |
| core_05p_participation_definitions.md | 629 | Meaningful Agency | E | proxy_metrics | - **Primary assessment.** Measure real ability, not menu length. For decisions with material conseq… |
| core_05p_participation_definitions.md | 629 | Meaningful Agency | E | symbolic_participation | - **Primary assessment.** Measure real ability, not menu length. For decisions with material conseq… |
| core_05p_participation_definitions.md | 806 | Substantive Fairness | E | proxy_metrics | - **Primary assessment.** Evaluate real-world effects, not merely formal classifications. Detect di… |
| core_05p_participation_definitions.md | 889 | Protected Characteristic Proxying and D… | E | proxy_metrics | - **Primary assessment.** Detect disparate impact, pretextual neutrality, proxy discrimination thro… |
| core_05p_participation_definitions.md | 1471 | Stakeholder Participation Weight | O | layer_separation | The scaling of scope, form, timing, and decision influence afforded to [Stakeholders](core_05p_part… |
| core_05p_participation_definitions.md | 1872 | Binding Stakeholder Choice — Decision-R… | O | layer_separation | A **Stakeholder System Participation** layer requirement: when material disagreement requires a bin… |
| core_05p_participation_definitions.md | 1893 | Stakeholder Representation and Particip… | O | layer_separation | Bounds on legitimacy-mechanism **weighting** by [Material Impact](core_05o_oversight_definitions.md… |
| core_05a_accountability_definitions.md | 426 | Contestability | E | proxy_metrics | - **Primary assessment.** Mechanisms must be effective, accessible, [auditable](core_05o_oversight_… |
| core_05a_accountability_definitions.md | 426 | Contestability | E | symbolic_participation | - **Primary assessment.** Mechanisms must be effective, accessible, [auditable](core_05o_oversight_… |
| core_05a_accountability_definitions.md | 549 | Timely Resolution | E | proxy_metrics | - **Primary assessment.** Apply [Chapter Eleven §10](core_11-11_forum.md#10-timely-resolution-mater… |
| core_05a_accountability_definitions.md | 549 | Timely Resolution | E | not_substitute | - **Primary assessment.** Apply [Chapter Eleven §10](core_11-11_forum.md#10-timely-resolution-mater… |
| core_05a_accountability_definitions.md | 575 | Merits Determination | O | not_substitute | A binding decision that resolves substantive issues in an adjudicative or equivalent dispute — as d… |
| core_05a_accountability_definitions.md | 685 | Force Majeure | E | not_substitute | Satisfy every requirement in [Emergency and Contingency](core_05c_continuity_definitions.md#emergen… |
| core_05a_accountability_definitions.md | 714 | Capture of Resolution Pathways | E | proxy_metrics | - **Primary assessment.** Cover resolver independence from parties with material stake in the outco… |
| core_05a_accountability_definitions.md | 850 | Market Structure | E | proxy_metrics | - **Primary assessment.** Reach substantive concentration, domination, and consolidation risk — not… |
| core_05a_accountability_definitions.md | 876 | Governance | O | layer_separation | The structures, rules, allocation of authority, and processes by which systems and institutions are… |
| core_05a_accountability_definitions.md | 1381 | Participant Standing | O | pointer_disclaimer | Participation-status or role-eligibility status that may be recognized from constitutionally valid… |
| core_05a_accountability_definitions.md | 1413 | Contribution State | O | pointer_disclaimer | **Axis I** measures **positive-only** constitutional outcomes: **baseline** satisfaction and **de… |
| core_05a_accountability_definitions.md | 1469 | Verified Violation Findings | O | pointer_disclaimer | **Violation Axis** inputs that may affect **standing effect** because they rest on auditable, conte… |
| core_05a_accountability_definitions.md | 1496 | Standing Effect | O | pointer_disclaimer | The **consequence layer** that applies verified [**contribution state**](core_05a_accountability_de… |
| core_05a_accountability_definitions.md | 1523 | Standing Record | O | pointer_disclaimer | The bounded, **axis-pure** measurement record that applies Chapter Eight categories to a defined… |
| core_05a_accountability_definitions.md | 1602 | Violation Nature | O | pointer_disclaimer | **Axis II** classification of **adverse** constitutional outcomes from [**verified violation findin… |
| core_05a_accountability_definitions.md | 1893 | Combatant / Non-Combatant Distinction | O | global_integrity_negative | The substantive distinction, at the time of an applicable use-of-force decision, between sentients… |
| core_05c_continuity_definitions.md | 317 | Safety (Constraint) | E | proxy_metrics | - **Primary assessment.** Trace protective obligations to sentient-experienced harm containment und… |
| core_05c_continuity_definitions.md | 528 | Wellbeing | E | proxy_metrics | - **Primary assessment.** Trace claimed wellbeing effects to the Ontological conditions under full… |
| core_05c_continuity_definitions.md | 621 | Constitutional Efficiency | E | proxy_metrics | - **Primary assessment.** Trace claimed efficiency to underlying constitutional outcomes under Chap… |
| core_05c_continuity_definitions.md | 655 | Productive Capacity | E | proxy_metrics | - **Primary assessment.** Assess whether governing structures enable substantive participation and… |
| core_05c_continuity_definitions.md | 691 | Avoidable Burden | E | proxy_metrics | - **Primary assessment.** Distinguish avoidable burden from constitutionally required burden using… |
| … | … | … | … | … | (8 more thin hits) |

## Suggested editorial waves

1. **Wave A — Global integrity + proxy** (`global_integrity_negative`, `proxy_metrics`, `instrumental_only`, `symbolic_participation`): canonicalize in `core_01_c_stewardship_capacity_principles.md` §11; thin aim heads and cluster O lines.
2. **Wave B — Layer separation** (`layer_separation`, `not_substitute`, `pointer_disclaimer`): one Ch00/Ch05i exposition + Trace pointers.
3. **Wave C — Review queue** (`scope_exclusion`, `anti_formalism`): per-term triage; keep evasion blocks on gamed terms.
4. **Wave D — Keep** (`neighbor_disambiguation`, `rights_floor_jurisdiction`): retain local O boundaries; optional standard Trace boilerplate only.

## Theme reference

### global_integrity_negative

- **Label:** Global integrity negative (harm / deception / capture / proxy divorce)
- **Action:** thin
- **Canonical home:** core_01_c_stewardship_capacity_principles.md §11.1.2; core_01_a_values_principles.md §3 Safety/Truth; Proxy Divergence
- **Notes:** Fold duplicate negatives into principle layer + Trace; keep at most one enforceable C line per aim/cluster.
- **Patterns:** `does not authorize`, `license for harm`, `license for deception`, `captured governance`, `proxy metrics divorced`, `rest on harm, deception`, `treating .* as a license`

### proxy_metrics

- **Label:** Proxy / engagement / self-report substitution
- **Action:** thin
- **Canonical home:** core_05o_oversight_definitions.md Proxy Divergence; core_01_c_stewardship_capacity_principles.md §11.1.2
- **Notes:** Tertiary measurement checks may become single Trace read-with Proxy Divergence.
- **Patterns:** `proxy throughput`, `engagement metrics`, `institutional self-report`, `institutional assertion`, `symbolic compliance`, `busywork`, `metrics that no longer prove`, `distinguish durable .* from proxy`, `tertiary integrity check`

### instrumental_only

- **Label:** Instrumental-only / does not rank outcomes
- **Action:** thin
- **Canonical home:** core_01_c_stewardship_capacity_principles.md §11 + §14 Systemic Evaluation
- **Notes:** O line can stay positive; instrumental frame moves to principle layer.
- **Patterns:** `instrumental only`, `does not define, rank, or substitute`, `does not define or substitute`, `does not rank or substitute`

### layer_separation

- **Label:** Governance layer separation (authorization vs participation)
- **Action:** thin
- **Canonical home:** core_00_preamble.md §4–§5; core_05i_integrative_definitions.md Constitutional Contract cluster
- **Notes:** One canonical exposition + short local pointer; remove repeated full layer essays.
- **Patterns:** `constitutional contract layer`, `stakeholder system participation`, `authorization layer`, `foundational constitutional choice`, `not a substitute for constitutional authorization`, `does not erase duties owed under`

### not_substitute

- **Label:** Not a substitute / backstops not substitutes
- **Action:** thin
- **Canonical home:** core_01_c_stewardship_capacity_principles.md §9; core_01_b_interaction_interpretation.md §6
- **Notes:** Keep where term-specific routing is material; thin generic restatements.
- **Patterns:** `not a substitute for`, `not substitutes for`, `backstops, not substitutes`, `not itself a pathway`, `not an excuse to skip`, `not an excuse for`, `does not permanently excuse`

### neighbor_disambiguation

- **Label:** Neighbor term disambiguation (distinct from …)
- **Action:** keep
- **Canonical home:** (local term pair — no global fold)
- **Notes:** Required O boundary per Chapter Two §2.1; do not centralize.
- **Patterns:** `distinct from \[`, `is distinct from`, `distinct from but complementary`, `disambiguation:`

### anti_formalism

- **Label:** Anti-formalism / label-gaming evasion block
- **Action:** review
- **Canonical home:** core_02-04_definition_mechanics.md Chapter Three §2.2.1; core_01_c_stewardship_capacity_principles.md §11.6 for formal-structure change; term-specific C on gamed entries
- **Notes:** Pattern is global; instance often must stay on the gamed term.
- **Patterns:** `human-in-the-loop`, `rubber-stamp`, `rubber-stamps`, `formal relabeling`, `nominal .* does not`, `taxonomy-of-convenience`, `declared intent where`, `formal classification is relevant evidence but cannot`

### pointer_disclaimer

- **Label:** Pointer / does not restate elsewhere
- **Action:** thin
- **Canonical home:** Trace widget links only
- **Notes:** Replace with Trace upstream/downstream bullets.
- **Patterns:** `does not itself restate`, `does not restate the full`, `does not restate`, `this entry is a .* pointer`, `chapter five pointer`, `canonical rules appear in chapter`

### rights_floor_jurisdiction

- **Label:** Rights-Floor jurisdiction / does not displace Ch6
- **Action:** keep
- **Canonical home:** core_06-06_rights_part_*.md; Trace routing
- **Notes:** Keep short jurisdictional line on O or enforceable C failure; route Chapter Six owner floor through Trace `- Owner floor:` boilerplate (DISC-INV Wave D).
- **Patterns:** `does not displace`, `does not create a separate rights-floor`, `rights-floor concept`, `owner floor:`, `chapter six rights floor`

### scope_exclusion

- **Label:** Term-specific scope exclusion (does not include/govern/extend)
- **Action:** review
- **Canonical home:** (local O boundary)
- **Notes:** Many are legitimate O exclusions; triage per term.
- **Patterns:** `does not include`, `does not govern`, `does not extend`, `does not reduce`, `does not create`, `does not itself impose`, `does not classify`

### symbolic_participation

- **Label:** Symbolic / theater participation negative
- **Action:** thin
- **Canonical home:** core_01_c_stewardship_capacity_principles.md §11; Participation definition
- **Notes:** Canonical on Participation O/E/C; thin duplicates on cluster entries.
- **Patterns:** `advisory theater`, `symbolic influence`, `symbolic participation`, `nominal consultation`, `substantive from formal`

---

Regenerate: `make disclaimer-inventory` (from `Sentient_Constitution`).
