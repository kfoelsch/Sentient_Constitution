# Chapter Eight go-live gate and challenge-path move (2026-10-08)

Architectural rule: **CH8-PROCESS-ORDER-01** in [doc_architecture.md](../../doc_architecture.md#chapter-eight-process-order-ch8-process-order-01).

## Decision

Before the pre-release announcement, the editor decided:

1. **No go-live before certification.** A system does not go live, as a pilot or in full deployment, before it is certified (provisional or full certification, with or without conditions).
2. **A pilot needs its own certification**, scaled by class and by how substitutable the system is. Class never permits skipping a required evaluation.
3. **Systems already operating** when an adopter's instrument takes effect are excepted for the transition period only, under the "Existing instantiations" clock in Article XXVIII-A.

Consequence: the published record challenge path cannot open in Phase I Frame for a new system, because it has no stakeholders until after the outcome. The record names the path before sign-off. The path opens when the outcome is published (so a challenge can be filed, and reliance stayed, before go-live) and is already open for a system already operating. The section moved from Frame to the start of Phase VI Operate.

## Operative changes (obligations changed, not only order)

| Where | Change |
|-------|--------|
| Part B §5 Certification Outcomes | New paragraphs **No go-live before certification** and **Systems already operating** (exception by reference to Article XXVIII-A). |
| Part A §2.1 How class scales every evaluation | New **Pilot** paragraph: own record, depth scaled by class and substitutability (Dependency), expectation to pilot kept and moved here from the challenge-path section. |
| Part B §7.1.1 Contestability paths | **When the path opens** rewritten: opens at publication of the first outcome for a system not yet operating; already open (or opens with the record) for a system already operating. |
| Part B §4.2 Supervisory sequence | **Challenge path first**: the record must *name* the path before sign-off (was: name an *open* path). A record that does not name it cannot be signed off. |
| Part B §4.3 Contestability chain, step 1 | For a system not yet operating, step 1 opens with the outcome; steps 2 to 4 are available throughout review. |

Clause inventory (`tools/obligation_inventory_diff.py`, Parts A–C): 295 clauses before, 298 after. Five clauses reported as "dropped" in Part A and the same five as "added" in Part B are the challenge section moving between files. The new clauses are: "The more readily the system can be replaced, and the lower its class, the lighter the pilot's evaluation may be" (Part A §2.1); "Full deployment needs its own recognition outcome, which may draw on the pilot's record" and "A new system, or a material expansion of an operating one, is new conduct and must meet the rule above" (Part B §5). The tool's modality list does not catch every new duty here (for example "does not go live until…" and "a pilot is certified on its own record"), so the table above is the complete list.

**Wording needs the steward's sign-off before release.**

## Phases after the move

| Phase | Sections | File |
|-------|----------|------|
| I. Frame | §2 System Class Evaluation | Part A |
| II. Evaluate | §3 Whole-System Certification Evaluation | Part A |
| III. Review | §4 Forum Process | Part B |
| IV. Decide | §5 Certification Outcomes (go-live gate) | Part B |
| V. Record | §6 System Certification Record | Part B |
| VI. Operate | §7 Recertification and Reopening (§7.1 Challenging a Certification, §7.1.1 Contestability paths, §7.2 Provisional and full certification, §7.3 Non-evasion); §8 Relationship to Standing | Part B |

## Old to new numbers

Starting point: the six-phase numbering of 2026-10-07.

| Old | New | Title |
|-----|-----|-------|
| A 1, 1.1, 1.2, 2, 2.1 | unchanged | |
| A 3 | **B 7.1** | Challenging a Certification |
| A 3.1 | **B 7.1.1** | Contestability paths |
| A 4 | A 3 | Whole-System Certification Evaluation |
| A 4.1–4.8 | A 3.1–3.8 | (same titles) |
| A 4.4.1, 4.7.1 | A 3.4.1, 3.7.1 | |
| A 4.8.k | A 3.8.k | the six domain evaluations |
| B 5, 5.1–5.4 | B 4, 4.1–4.4 | Forum Process and subsections |
| B 6 | B 5 | Certification Outcomes |
| B 7, 7.1, 7.2 | B 6, 6.1, 6.2 | System Certification Record and subsections |
| B 8 | B 7 | Recertification and Reopening |
| B 8.1 | B 7.2 | Provisional and full certification |
| B 8.2 | B 7.3 | Non-evasion |
| B 9 | B 8 | Relationship to Standing |
| C 4.4.1 | C 3.4.1 | Illustrative data-handling application |
| C 4.8.k.1 | C 3.8.k.1 | Illustrative domain applications |

Part B shifted down by one so numbering stays continuous after Part A lost a section. Anchors are the slug of "number title" (one current anchor per heading; no fossil anchors).

## Reading aids and text updated

- Part A §1.1: plain-terms sentence, phase paragraph, **chart** (challenge-path box moved to Operate and placed after Record; "No go-live before certification" on the Decide node; the three status nodes (Full Certification, Provisional Certification, Not Certified)), and the phase table (Frame is §2 only).
- Hub (`core_08_system_alignment_certification.md`): ownership table, phase table, run sheet (challenge-path step moved to Operate; steps renumbered 1–11), record checklist ("Challenge paths" now produced in Review and Record), closing reading note. Two link labels the script could not remap (ranges in link text) were fixed by hand.
- Part A and Part B file headers and plain-terms sentences; Part B §4 and §5 trace lines; Part B §7 subsections line.
- Part A header said Part B was the "last three phases"; it is four. Fixed.
- `implementation/STEWARD_ENTRY_DOORS.md` ("System alignment certification" next step) and `implementation/steward_owner_clock_index.json` (`clock_note`): same new sentence, as STEWARD-DOOR-LOCKSTEP-01 requires.
- `corpus_systems/cs_02_b_data_classifications.md` (hand-edited file, skipped by the script): two Chapter Eight links retargeted. `evaluation/external_audit_2026-08/FINDINGS.md`: one anchor and its label retargeted.
- `doc_architecture.md` (rule text and decision record), `project/MEMLOG.md` (entry and standing decision).
- Regenerated: `doc_architecture/generated/plain_terms_edition.{md,json}` and `boundary_chunks.json` (their checks passed before the move).

## Tooling

- `tools/ch8_go_live_gate_reorder.py` (mapping-driven; links, anchors, bare cites; moved the section between files; recomposed Parts A, B, and C). Run on 302 files; 2,358 links rewritten.
- Left as written on purpose: `steward_box_review.md` (historical working draft with "not applied" text), `evaluation/results/`, `archive/`, `evidence/`.
- Translations were re-anchored for links into English files only; they stay paused.

## Verification

- Audits: the 81 targets in `make regression` were run target by target on a clean copy of the tracked files before the change and on the changed copy after.
  - Failing before: `article-cite-gloss-audit`, `corpus-ref-name-audit`, `section-abbreviation-descriptor-audit`, `section-cite-name-audit`. Same four after, with identical output.
  - No new failures after the evidence file and generated files were in place (`local-markdown-fragment-audit` flagged only the missing link to this file, and the stale generated plain-terms edition, until each was fixed).
  - `steward-door-lockstep-audit` and its test failed until the index `clock_note` matched the card; both pass.
  - `section-label-anchor-audit`, `fossil-anchor-audit`, `anchor-heading-drift-audit`, `widget-top-placement-audit`, `reference-audit` pass.
- Link scan: every link into Chapter Eight resolves, and each link's visible section number matches the heading it points to (one false positive: a range label).
- AI indexes regenerated with `make ai-corpus-sync` on a clean copy: `section_manifest.json`, `crossref_matrix.json`, and `section_crossref.json` changed and were copied back (the other two indexes differed only in `generated_at`). `ai-manifest-validate` failed before this change for those three files and now passes. The print pack check was already failing and is untouched.
- Chart: the updated §1.1 process chart was rendered with Mermaid 10.9.1 and checked by eye against VIS-CHART-CROSSING-06 (no crossing links) and VIS-CHART-ORIENT-04 (top to bottom). The challenge-path box sits right of centre under Record, as the recognition branch did before, because of the dotted link to Chapter Nine.
- Branch: the work was moved to a new branch `restructure/ch08-go-live-gate-challenge-path`, cut from the previous branch's head (GIT-BRANCH-NAME-01). The old branch `feat/ch08-record-decision-concerns` and its remote were not touched, because renaming a branch with an open pull request closes it.

## Follow-ups for the steward

1. Sign off the wording in the five places above.
2. Decide whether to add a short standstill between publishing an outcome and go-live. Not added; the rule says only that the path opens at publication, so a challenge can reach it first.
3. Checked and left as is: `evaluation/SCENARIOS.md` and `SCENARIOS_FACTS_ONLY.md` mention a "stakeholder challenge window" only as a release-level window under CI-4.6 (scenario 16) and as a failure fact ("got no challenge window"); neither states when the Chapter Eight path opens, so the new rule does not contradict them.
