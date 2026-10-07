# Privacy ↔ CS-2 data types linkage

**Date:** 2026-10-06
**Branch:** `lane-d/privacy-data-types-linkage` (cut from `docs/ch08-reorg-and-chart-standards` at `8c0f3f0`, because Chapter Eight §3.8 edits build on that branch)
**Lane:** D (core text) with Lane A/E housekeeping
**Status:** Process / evidence support. This file does **not** bind. Indexes point; source binds.
**Drafting:** drafted by an AI (Claude) at the custodian's request; not yet reviewed by a person.

## Problem

Privacy pointed down to CS-2 only generically ("see CS-2"), and CS-2 never pointed back. CS-2 Part B never used the word *privacy*. CS-2 Parts A and B had no links to [Privacy (Informational)](../../core_05_band_continuity.md#privacy-informational), **Def.C3**, [Protected Internal-State Boundary](../../core_05_band_continuity.md#protected-internal-state-boundary), or [Surveillance Boundary](../../core_05_band_continuity.md#surveillance-boundary). None of the privacy rows in the [2026-08-31 coverage audit](../2026-08-31/cs2_data_types_coverage_audit.md#privacy-and-rights-floor-kinds--type-the-category-list) had reached source.

## Changes by finding

| # | Finding | Change | Where |
|---|---|---|---|
| 1 | Type S expiry said lapsed restrictions are "reclassified and disclosed", which reached protected-party, witness, and at-risk location data | On expiry, each component is retyped under Part A §2. Type S-only components are disclosed (or summarized as Type O) as before. Components that are also H, I, or N stay restricted. Expiry removes the security basis but does not make them disclosable. Added: a lapsed review must not expose a protected party | CS-2 Part B §9.7.1 |
| 2 | One-way link | Part B: **Privacy link** paragraph (`#privacy-link`) and a **Privacy homes** list on Types H, I, N, S. Part A: **Privacy** paragraph in CS-2.1 (`#privacy-owner-link`) naming CS-2 as the Def.C3 rulebook; privacy-discipline paragraph in §5.0 bands. Def.C3 operational-alignment line names the type map and links back | CS-2 Parts A and B; Def.C3 |
| 3 | Privacy categories untyped | **Data types** sub-bullet on Privacy (Informational) (category → type map from the 08-31 audit), Surveillance Boundary, Training-Data Use, Likeness and Documentary Depiction Interface, Protected Characteristics, Protected Intimate-Signal Gating | Chapter Five continuity and participation bands |
| 4 | Chapter One §13.2.3 listed six loose categories (no O, no S; "system-operational" matched nothing) | Replaced with the seven type letters and names; points to the Privacy (Informational) map | `core_01_b` §13.2.3 |
| 5 | Chapter Eight §3.2 and §3.8 never referred to each other | §3.2: *Data-types evidence* bullet (System Data Types Record is evidence; a locus cannot close on handling the record does not show). §3.8: **Privacy discipline** paragraph, new defect ("matches its type label but fails the privacy homes"), Read-with to §3.2 | `core_08_a` |
| 6 | System Data Types Record had no purpose, recipients, basis, or derived-data fields, though the §1.3 collection notice must be "consistent with" it | Added those three content items, matching primary-assessment item, and a secondary failure. Also repaired a garbled clause in assessment item 1 | System Data Types Record (Chapter Five) |
| 7 | De-identification standard pointed at CJS-3.11 / CJS-3.7 | Type H public release and CS-2.7 substitutes now use [Derived Information](../../core_05_band_integrative.md#derived-information) / Chapter One §15.1.2 (not reasonably re-identifiable; relying party carries the showing). CJS-3.11/3.7 kept for release scope | Part B §9.4; Part A §7 |
| 8 | Privacy-vs-transparency collisions not routed | CS-2.7 substitutes: a material privacy ↔ baseline-disclosure trade is a Constitutional Collision on a [Constitutional Collision Record](../../core_05_band_integrative.md#constitutional-collision-record) | Part A §7 |
| 9 | Article IX-B cited privacy protections "under Articles I, II, XIII, and XIV" (stale numbering) | Now VII-A, VII-B, IX-A, X-A, XIV-A, XV, each with its title gloss | `core_06_rights_part_b` IX-B |
| 10 | Identity Data Protection labelled Type H as identity data and was not a Def.C3 member | Reworded (Type I; Type H once linked to identity). Added to Def.C3 scope and member list, Chapter One §13.2.3 downstream trace and D·A·C widget | Chapter Five; `core_01_b` |
| 11 | Def.C3 routed to the Continuity family; all members measure under Participation | Routing line now *Participation measurement family (Privacy and data stewardship)*. Measurement seed for Identity Data Protection aligned (`3.3 Continuity` → `3.4 Participation`, matching its own primary measure and the other three members) | Def.C3; `tools/architecture/measurement_tier_seeds.json` |
| 12 | Part A and Part B were both numbered CS-2.8 | Part B renumbered to **CS-2.9** (9.1–9.7), following the CS-3 / CS-5 convention that Part B continues Part A's numbering. Part A guidance already said §§1–8. All inbound links and labels retargeted (`corpus_systems.md`, `family_map.json`, CS-2 Part A, CS-4, oversight band, 15 translation links). `CS-2 §8` citations to System Data Types Record governance are unchanged | CS-2 Part B and referrers |

## Non-regression self-check (Test 1)

- **No Rights Floor narrowed.** Every privacy link is stated as *point, do not narrow*. Type letters on Chapter Five homes add protection; under Part A §2 the most protective type still governs.
- **Finding 1 is the one deliberate narrowing of a disclosure duty.** The obligation diff flags it as `DROPPED or WEAKENED DUTY`. It narrows only post-expiry disclosure of components that are also H, I, or N. The Type O summary duty (nature, justification, duration, scope, oversight path, outcomes) is unchanged for all components. The old text already conflicted with Part A §2's most-restrictive rule and with Articles VII-A, IX-A, and XIV-A. Transparency about the restriction is preserved; exposure of protected parties is not compelled.
- **Added duties** (System Data Types Record fields, Chapter Eight checks) raise operator burden at material-impact scale only, where the record is already required.

## Gate results

| Gate | Result |
|---|---|
| `make regression` | Three failures, all **identical to HEAD** (baseline run on a clean export of `8c0f3f0`): `ch5-measurement-coverage-audit` (four seedless leaves unrelated to privacy), `prose-continuity-audit`, `lexical-vocabulary-audit`. No new findings in any of the three. All other targets pass, including `reference-audit`, `local-markdown-fragment-audit`, `corpus-ref-name-audit`, `article-cite-gloss-audit`, `steward-door-lockstep-audit`, `fossil-anchor-audit`, `anchor-heading-drift-audit`, `ch1-dac-order-audit`, and `ch1-cjs3-alignment-audit` |
| Readability (touched files) | Every touched file was above grade 14 on HEAD. CS-2 Part B improved 15.07 → 14.95; Part A 14.68 → 14.74; core files moved by ≤ 0.03 |
| Obligation diff | [obligation_inventory_diff_obligation_before.json](obligation_inventory_diff_obligation_before.json): 1008 → 1014 obligations; 8 added (intended); 1 narrowed (finding 1, justified above). Converted to the slim format after the fact (1.6 MB → 10 KB): it keeps per-file counts, the 20 changed obligations in old and new wording, and the findings and notes; unchanged records and derived `terms` lists were dropped |
| Derived artifacts | Regenerated `ai-corpus-sync`, `architecture-index`, `plain-terms-edition`, `reader-accessibility`, `boundary-chunks`. `plain_terms_edition.json`, `human_definition_lookup.*`, and `boundary_chunks.json` were already stale on HEAD, so part of their diff is pre-existing drift |
| Alignment audit | `ch1_cjs3_*_2026-10-06` in this folder were written by the regression run |

## Not done (needs the custodian)

- **Proposal issue** before the pull request (Lane D entry), and the spec change-log line on merge.
- **Remaining 08-31 audit rows outside privacy:** named-record type letters (Charter, certification/classification records, Forum Case Record, Standing Record, and others), Evidence Preservation, Protected Reporting, High-Impact publication constraint, Consent, Sexual.
- **Translations** carry the old Chapter One §13.2.3 wording and lack the new type lines until the translation restart. Only their link fragments were updated.
- **Optional tooling:** a bidirectional check (privacy homes ↔ type lines), modeled on `router_bidirectional_audit.py`.
