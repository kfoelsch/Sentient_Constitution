# Disclaimer inventory (DISC-INV-01)

Auto-generated. Do not edit by hand.

Generated: 2026-08-03T20:43:03+00:00

Scopes **Chapter Five** band and aim files. Classifies disclaimer / negative-scope clauses on **O**, **E**, and **C** components using [tools/architecture/disclaimer_themes.json](../tools/architecture/disclaimer_themes.json).

Editorial model: **safe redundancy** = one canonical exposition + pointers (see [doc_architecture.md](../doc_architecture.md) §12).

## Summary

- **Total hits (actionable):** 7
- **Thin candidates:** 3
- **Review candidates:** 2
- **Keep (local boundary + canonical homes):** 2
- **Canonical exposition (do not thin):** 0
- **Same-theme duplicates across O/E/C (terms):** 1

### By recommended action

| Action | Count | Meaning |
| --- | ---: | --- |
| thin | 3 | Replace with Trace read-with / single C line |
| review | 2 | Triage per term — may stay local |
| keep | 2 | Term-pair or jurisdictional — do not fold |
| canonical | 0 | Canonical home for theme — retain |

### By O/E/C component

| Component | Hits |
| --- | ---: |
| O | 4 |
| E | 0 |
| C | 3 |

### By source file

| File | Hits |
| --- | ---: |
| core_05_band_participation.md | 5 |
| core_05_apex_participation_leg.md | 2 |

### By theme family

| Theme | Hits | Default action | Canonical home |
| --- | ---: | --- | --- |
| Governance layer separation (authorization vs participation) | 2 | thin | core_00_preamble.md §4–§5; core_05_band_integrative.md Constitutional Contract c… |
| Rights-Floor jurisdiction / does not displace Ch6 | 2 | keep | core_06_rights_part_*.md; Trace routing |
| Anti-formalism / label-gaming evasion block | 2 | review | core_02_definition_structure.md Chapter Three §2.2.1; core_01_c_stewardship_… |
| Symbolic / theater participation negative | 1 | thin | core_01_c_stewardship_capacity_principles.md §11; Participation definition |

## Intra-entry redundancy (same theme, multiple components)

Highest-yield thinning: drop duplicate theme on secondary components when one enforceable **C** line or principle-layer pointer remains.

| Term | Theme | Components |
| --- | --- | --- |
| Sentience Status Adjudication | Rights-Floor jurisdiction / does not displace Ch6 | C, O |

## Thin candidates (sample)

| File | Line | Term | Comp | Theme | Excerpt |
| --- | ---: | --- | --- | --- | --- |
| core_05_apex_participation_leg.md | 29 | (no heading) | O | layer_separation | Give affected sentients and [Stakeholders](core_05_band_participation.md#stakeholder) real voice in… |
| core_05_apex_participation_leg.md | 29 | (no heading) | O | symbolic_participation | Give affected sentients and [Stakeholders](core_05_band_participation.md#stakeholder) real voice in… |
| core_05_band_participation.md | 1712 | Binding Stakeholder Choice — Decision-R… | O | layer_separation | A **Stakeholder System Participation** layer requirement: when material disagreement requires a bin… |

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
- **Canonical home:** core_05_band_oversight.md Proxy Divergence; core_01_c_stewardship_capacity_principles.md §11.1.2
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
- **Canonical home:** core_00_preamble.md §4–§5; core_05_band_integrative.md Constitutional Contract cluster
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
- **Canonical home:** core_02_definition_structure.md Chapter Three §2.2.1; core_01_c_stewardship_capacity_principles.md §11.6 for formal-structure change; term-specific C on gamed entries
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
- **Canonical home:** core_06_rights_part_*.md; Trace routing
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
