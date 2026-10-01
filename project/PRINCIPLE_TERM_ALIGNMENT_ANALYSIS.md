# Principle term alignment with Chapter Five definitions

**Date:** 2026-10-01 · **Status:** analysis only; no corpus text changed · **Scope:** the 65 Chapter One Definitions · Assessment · Compliance widgets (14 at section level, 43 at subsection level, 8 at third level), their section text, and the 255 Chapter Five definition entries.

Scripts that produce the figures are in `project/analysis/` (`ch1_widget_parse.py`, then `ch1_widget_vs_body.py`; they read the Chapter One files directly and write to `/tmp/an/`).

## Bottom line

The vocabulary is mostly aligned. Only 2 of the 100 distinct widget labels differ from a definition name, and the Chapter One/Chapter Five audit reports every widget row resolving. The simplification opportunity is in **how much each widget lists**, not in the definitions themselves. Most of the redundancy is repetition between parent and child widgets and a few always-appended generic tests.

## Findings

| # | Finding | Evidence |
|---|---|---|
| 1 | **Child widgets repeat the parent's rows.** | 128 of 252 child-widget rows (51%) already appear in the immediate parent's widget. Eleven child widgets are entirely contained in the parent's: §5.3, §5.4, §6.2.1, §6.2.2, §8.4, §9.3, §11.1, §12.2, §13.1, §13.2, §14.1. |
| 2 | **Necessity and Proportionality are appended almost everywhere.** | 47 of 413 rows (11%): Proportionality in 24 widgets, Necessity in 23. Only 14 of the 47 are also linked in the section text. They are the tests owned by §6.1.1 and §6.1.3. |
| 3 | **Many rows are not visible in the section text.** | 236 rows name a definition the section never links. About 79 of those (rough text match) never mention the concept at all. Concentrated in §12.1 (12 rows), §5, §13.1, §16 (5 each). |
| 4 | **The reverse gap is small but real.** | 32 definitions are linked in section text but missing from that section's widget, e.g. §9.2 (Avoidable Burden, Dependency, Epistemic Integrity, Necessity, Proportionality, Truth), §14 (Constitutional Efficiency, Dignity, Ecological Integrity, Productive Capacity, Wellbeing), §13 (Governance, Stewardship), §10.4 (Assembly, Governance, Procedural Fairness). |
| 5 | **Constraint labels use two patterns.** | "Safety (Constraint)" (about 125 references) vs "Truth (Constitutional Constraint)" (115), while "Constitutional Constraint" is also its own definition. Headings §3.1 and §3.2 use a third form ("Safety (Harm Constraint)", "Truth (Epistemic Integrity Constraint)"). |
| 6 | **Two widget labels are aliases.** | "Materiality" links to Materiality Determination; "Foreseeability" links to Foreseeability Diligence. Both are the names principles actually use in prose. |
| 7 | **Some principle titles have no matching definition label.** | §2.1 Fairness (defined as Procedural and Substantive Fairness), §3.4 Plain-Language Accessibility (Accessibility), §4 Trust (Coordination Integrity) (Trust), §4.2 Correction and Remedy (three definitions), §14.1 title vs Market Concentration Threshold, §8.1 title vs No-Bypass. Titles may legitimately differ; the issue is only where a reader cannot tell which definition is meant. |
| 8 | **Single-section vocabulary.** | 35 definitions are cited by exactly one widget. The §12.5 set (Contingent Claim, Event-Contract Market, Game of Chance, Insider Advantage, Capture of Resolution Pathways) is five one-cited entries for one section. Capture of Resolution Pathways calls itself "a form of System Capture". |
| 9 | **Always-together pairs.** | System Capture + Anti-Capture (5 of 5 widgets), Constitutional Efficiency + Productive Capacity (6 of 6). Smaller pairs (2 of 2): Surveillance Boundary + Protected Internal-State Boundary; Educational Agency + Distributed Understanding; Intergenerational Responsibility + Environmental Preconditions; Collective Organization + Business Creation. |

## What I would not simplify

- **Merging definitions.** Capture state vs duty, Trust / Trustworthiness / Trust Degradation, and the Remedy set each carry a different test. Co-citation shows they travel together, not that they are the same concept.
- **Truth vs Epistemic Integrity.** Truth governs decision-relevant claims; Epistemic Integrity governs methods and evidence. §3.2 lists both and should say which does what, but they are not duplicates.
- **Anchors.** 93 of 285 directory anchors end in `-constitutional`, a leftover of the old title suffix. Renaming would break links for no reader benefit.

## Recommendations, lowest risk first

1. **Row-keeping rule (Findings 3 and 4).** A widget row stays only if the section text names or applies the term; a text link to a definition without a row gets one. This is mechanical to check and clears most of the 79 and 32.
2. **Inheritance line for child widgets (Finding 1).** A child widget lists only terms it adds, with an annotation row such as `*Also applies: terms listed under §12.*`. The D/A/C order audit already tolerates annotation rows. Needs a decision on whether a reader landing on a subsection must see the full list.
3. **Move Necessity and Proportionality to the owners (Finding 2).** Keep them in §6.1.1, §6.1.3, §8.2 and sections that impose a limit; elsewhere rely on rule 1.
4. **One constraint-label pattern (Finding 5).** Smallest change: rename "Safety (Constraint)" to "Safety (Constitutional Constraint)" (about 125 references, mechanical) and align the §3.1 and §3.2 headings. Alternative: shorten both to "Safety" and "Truth".
5. **Resolve the two aliases (Finding 6).** Either retitle the definitions to Materiality and Foreseeability (keep anchors) or use the full names in widgets. I lean toward retitling Materiality, since principles use it as a threshold concept and the Chapter Five gravity gate prefers concept names.
6. **Nest the §12.5 vocabulary (Finding 8).** Place the five entries inside the existing contingent-settlement cluster, and fold Capture of Resolution Pathways into System Capture as a named form. This is a Chapter Five structure change, so it needs the gravity and single-definition audits and a definition-count update.
7. **Bundle co-cited pairs (Finding 9).** Optional; only worthwhile if recommendation 2 is adopted, since bundles would be named once at the parent.

## Decisions needed

- Rule for widgets: full list at every level, or inherit from the parent (recommendation 2).
- Constraint label pattern (recommendation 4) and the Materiality/Foreseeability naming (recommendation 5).
- Whether recommendation 6 is wanted before the pre-release announcement, since it changes definition counts.

## Method and limits

- Widget rows come from the Definitions · Assessment · Compliance block under each numbered heading, including third-level headings. My first pass missed third-level widgets and inflated §6.1 and §6.2; the figures above use the corrected parse.
- "Linked in text" counts only links to Chapter Five anchors, with `-a`/`-c` and band suffixes resolved to the directory label. "Mentioned" is an approximate stem match and overstates how many rows are truly unmentioned (for example label differences such as Foreseeability Diligence).
- Principle-text figures cover Chapter One only; Chapter Seven and later articles were not analysed.

## Update 2026-10-01 (later)

Recommendations 4 and 5 were carried out. "Safety (Constraint)" is now "Safety (Constitutional Constraint)", "Materiality Determination" is now "Materiality", and "Foreseeability Diligence" is now "Foreseeability" in all source files, with anchors unchanged. The §3.1 and §3.2 heading parentheticals, the inheritance rule, the Necessity/Proportionality rule and the §12.5 nesting remain undecided. Figures above describe the state before the renames.

## Update 2026-10-01 (later)

Recommendations 4 and 5 were carried out. "Safety (Constraint)" is now "Safety (Constitutional Constraint)", "Materiality Determination" is now "Materiality", and "Foreseeability Diligence" is now "Foreseeability" in all source files, with anchors unchanged. The §3.1 and §3.2 heading parentheticals, the inheritance rule, the Necessity/Proportionality rule and the §12.5 nesting remain undecided. Figures above describe the state before the renames.
