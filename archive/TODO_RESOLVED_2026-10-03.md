# Resolved TODO items — archived 2026-10-03

This archive records completed items and closed narratives removed from the active [TODO.md](../TODO.md) on 2026-10-03, grouped by their original section and kept verbatim. Normative meaning remains in the binding corpus; this file is a process-history record. Items below marked superseded were written against the pre-relocation Chapter One numbering. Links are relative to the repo root as written in TODO.md; rebased below for this folder where needed.

## 2026-10-01 — Chapter One structure pass: done record

**Done (text only; no renumbering, no anchor changes).** Part A now opens with a reader-guidance map ([core_01_a](../core_01_a_values_principles.md)): how aims, Tetrad, principles, Articles, and definitions connect; a table of which principle develops each Flourishing condition and each Continuity part, with its definition home and Trace Articles; and a table of where the Tetrad legs live. §1 states the chapter's organization in visible prose. §2 now says it develops the Flourishing aim and names the four conditions that sustain it. §4 names Trustworthiness as the Flourishing constituent (matching Preamble §1). Part A gained a reading arc. Part B's "Next" pointer said §§9–14; Part C is §§9–16. `doc_architecture.md` had the same stale range plus a wrong capstone (§15; it is §16).

## 2026-09-30 — Process, system, institution: resolved item

- [x] **Decide the pre-release stance.** Decided 2026-10-01: adopt relocations now, before the announcement.

## 2026-09-17 — Review coverage and technical follow-through (closed)

#### Review coverage and technical follow-through


  **Closure (2026-09-17):** Read and checked the 116-file tracked source ledger (38 core-directory files, including the non-operative vignette file; 4 adopted implementation wrappers; and 74 adopted implementation subfiles) against current source. Repaired the Chapter Eight Part B §11 upstream pointer to Chapters Two through Four; the pointer audit and full `make regression` pass. Translation, implementation, evaluation, lived-experience, and P1 stress-pack work remain separately scoped and open.

## 2026-09-14 — Nested-list readability pass (closed)

### 2026-09-14 — Nested-list readability pass (remaining chapters)

Same nest-or-leave method as Chapter Five and Chapter Six: extend `tools/ch5_nested_list_candidate_audit.py` to the chapter, rank packed bullets, nest real parallel lists, leave one-clause “including …” glosses and continuous legal arguments. After the first nest, **re-scan children for subbullets**: the finder skips any parent that already has a child, so packed lists under those parents never rank until you look by hand (or nest, then re-run). Nest real parallel grandchildren; leave one-clause glosses at that layer too. Advisory finder only (`make ch5-nested-list-candidates`, `make ch6-nested-list-candidates`, `make ch7-nested-list-candidates`, `make ch8-nested-list-candidates`, `make ch9-nested-list-candidates`, `make ch10-nested-list-candidates`, `make ch11-nested-list-candidates`, `make ch12-nested-list-candidates`, `make ch13-nested-list-candidates`); not a regression gate.


  **Closure (2026-09-17):** Added chapter-specific advisory targets/rules for Chapters 0–4 and 14–16; nested the clear parallel checklists in the Preamble and Chapter Seventeen; re-scanned after nesting; left compact legal prose and single-clause “including” glosses unchanged.

## P1 — Regression And Evidence: closure note

  **Closure (2026-09-17):** Run `p1-regression-review-2026-09-17-01` recorded in [P1 regression and evidence review](../evidence/2026-09-17/P1_REGRESSION_AND_EVIDENCE_REVIEW_2026-09-17.md). `make scenario-audit` and the full `make regression` pass; the 189-row matrix has 131 pass, 58 draft, and no fail/partial/unknown results, with all 192 seed blocks present. Section 10.5 remains internally consistent at 8.4 under `SCORING-v1`. The expected `.cursor/rules/testing.mdc` file is absent, and the active Sentient Constitution rule requires `make regression`; no suspended-regression instruction remains in the reviewed policy surfaces. No separate queued observations were found requiring new `RS-*` rows. The 35 stress-pack rows remain draft and are not treated as empirical evidence.

## 2026-10-01 to 2026-10-03 — Chapter One relocation, numbering, and wording log (done items)

## 2026-10-01 — Chapter One continuity relocation: done, open follow-ups
- Done: Part A is now §1 purpose, §2–5 Flourishing, §6–9 Continuity; later sections renumbered (§10–17). §2 and §4 retitled. Report: evidence/2026-10-01/ch1_continuity_relocation_report_2026-10-01.json.
- [ ] Translations (20 languages) still carry the old Chapter One numbering; not updated.
- [ ] Add the relocated Continuity principles (new §6/§7 and §8/§9) to the Trace downstream in core_05_apex_continuity_aim.md.
- [x] Shared-System Capacity aim question resolved 2026-10-01: it straddles both aims (means toward Flourishing, substance of Continuity); swapped to §6 as the bridge, Resilience is now §7.
- [x] "Standardization" measurement seed approved 2026-10-02 (Accountability, primary_secondary); hierarchy map regenerated. Also added to the Governance architecture topic group members and to ch5_cluster_order_audit.
- [ ] Run `make ai-manifest-regenerate` now that source changes are committed.
- Baseline failures corpus-markdown-audit and ch5-cluster-order-audit cleared 2026-10-02 (list-intro colons; Standardization added to the topic group). lexical-vocabulary-audit not re-checked.

- 2026-10-01 (later): Chapter One §9 and §7 swapped (tools/ch1_swap_6_7.py): §9 Shared-System Capacity (straddles both aims), §10 Resilience and Self-Healing Design. Translations still use the old numbering.
- 2026-10-01 (later): Added unnumbered Part A openers "Flourishing Aim: Introduction" (after §1) and "Continuity Aim: Introduction" (before §6), each with a Mermaid chart. Chart sync (VIS-CHART-SYNC-03): update both when §2–§9 headings change. Translations not updated.

## 2026-10-01 — Chapter One Part A numbering smoothed
- Done (tools/ch1_numbering_smoothing.py): §2 Flourishing Aim: Introduction (numbered), §2.1 Non-Negotiable Principle Constraints: Safety and Truth (old §3 shared framing), §3 Wellbeing, §4 Safety, §5 Truth (§5.1 Science-Informed Inquiry, §5.2 Plain-Language Accessibility), §6 Trust, §7 Freedom, §8 Continuity Aim: Introduction, §9 Shared-System Capacity, §10 Resilience, §11 Market Structure, §12 Systemic Evaluation; Part B is §§13–15, Part C §§16–20.
- Also repaired: stale "Chapter One basis: §…" lists in CJS, Chapter Five and related files (only the first cite had been remapped in earlier passes; all tokens now mapped from the pre-relocation numbering), plus stale link labels pointing into Chapter One.
- [x] Mermaid charts (Part A intros, Part C stewardship chart) verified against headings 2026-10-01; hand-maintained, so update when §2–§12 or §16–§20 headings change (VIS-CHART-SYNC-03).
- [ ] Translations (20 languages) still use the old Chapter One numbering.
- [x] Cite sweep 2026-10-01: fixed 27 broken Chapter One links in evaluation/ and project/ (they sat outside the fragment audit's scope) and 5 mislabeled links. Remaining risk: bare untitled "§N" cites in prose; local-markdown-fragment-audit now also scans evaluation/ (excluding dated results) and project/plans/ (implementation/ was already covered).

- 2026-10-02: Added "distinct from each other and meaningful options" to Chapter Five Meaningful Agency and Consent (gloss, assessment, failure lists, topic-group line). Translations and Chapter Six consent articles not checked for the same wording.

- 2026-10-03: Replaced "reasonably effective/well" in the Necessity test and the safer-alternative tests (Ch5 Necessity, Ch1 §7/§7.1/§13.1, core_05_band_oversight, core_06_rights_part_a) with purpose-based wording. Added `avoid-reasonably-well` to lexical-vocabulary-audit (now passes with no findings). Also banned "reasonably effective" (rule `avoid-reasonably-well-or-effective`).

- 2026-10-02: Chapter One §7 reordered (7.1 Limitation Discipline; 7.2 Assembly; 7.3 Dissent; 7.4 Voluntary Discontinuation and Exit Rights). Institutional Secularism moved from §7.5 to §18.2; old 18.2–18.5 are now 18.3–18.6. Optional: Dissent before Assembly was not done. Translations still use old numbering. Bare untitled "§N" Chapter One cites are unchecked by any audit.

## 2026-10-01 — Chapter One structure pass: superseded items (retitle §2/§4)

- [ ] **Decide: retitle §2 and §4 headings?** Only visible text changed so far. A retitle changes the anchor, so every link must move with it. Live-corpus links: §2 64 (14 files), §4 43 (9 files), §5 111 (15 files); translations carry their own copies (174, 116, 155 files). §5's heading matches its Chapter Five defined term (Freedom (Bounded Agency)), so renaming it would add a mismatch. Same decision as the §3.1/§3.2 parenthetical item above. Now tied to the relocation pass, since moved sections change anchors anyway.

## 2026-10-01 — Chapter One structure pass: superseded items (Continuity aim downstream)

- [ ] **Add §14 and §15 to the Continuity aim file's downstream list** ([core_05_apex_continuity_aim.md](../core_05_apex_continuity_aim.md) Trace names §4.1, §13, and §12.1.5). Left alone because Chapter Five files were mid-edit.

## 2026-10-01 — Chapter One principles and Chapter Five definitions: empty headings

**Two worth a second look.** These are the only ones where a distinct concept may lack a home.


**Related finding: one-way link.**

## 2026-10-03 — Regression failures (found and fixed same day)

- [x] **Fix the two failing regression targets (found 2026-10-03).** `make regression` fails: `corpus-markdown-audit` (MD-LIST-INTRO-01: bold list-intro headers ending in a period, `core_01_a_values_principles.md` lines 980 to 984 and 1043); `ch5-measurement-coverage-audit` ("Subversion: hierarchy leaf missing approved seed"). Fixed 2026-10-03: the five lead-ins now end in colons; Subversion seeded in `tools/architecture/measurement_tier_seeds.json` (3.6 Accountability, primary_secondary, approved, matching its primary and secondary measures). Full `make regression` passes.
