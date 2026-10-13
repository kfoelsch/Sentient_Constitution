# Institutional alignment certification: implementation note (2026-10-13)

Branch `docs/ch09-institutional-alignment-certification`, uncommitted. Follows the evaluation of the same date (project doc `claude/institutional-alignment-certification-evaluation.md`). Everything here is draft text awaiting steward sign-off.

## What was added or changed

- **New file** `core_09_d_institutional_alignment_certification.md`, Chapter Nine Part D, §11 to §15, continuing Part B's numbering:
  - §11 purpose, relation to System Alignment Certification (composition by link), who is certified, no licence and no gate;
  - §12 institution class (portfolio floor; own impact; own impact above the portfolio), the six institutional evaluation items, evaluations where implicated, scaling by class;
  - §13 four seats, forum roles and sequence, outcomes and their limited effect, the Institutional Certification Record;
  - §14 recertification, reopening triggers, the cascade from System certifications, challenge path, forums and certifiers as institutions;
  - §15 standing bridge and non-evasion.
- **Chapter Five:** two entries, Institutional Alignment Certification and Institutional Certification Record, placed among the independent Continuity terms (beside, not in, the System Alignment Certification group). Directory rows and measurement seeds added.
- **Chapter Nine index:** now four parts; placement table, phase note, run sheet, and links updated. Footers: Part C to Part D to Chapter Ten.
- **Chapter Seven:** opening chart and reading bullets, §2 (Timing and Class of an Institution), §6, §7, and the §2 trace.
- **Chapter Eight:** §2 fourth prohibited pairing now reads "the operator of a system, or the governing authority of an institution, must not verify or authorize an act about that system or institution"; §9 and the placement note.
- **Chapter Thirteen:** §2 list and table, the Integrity row, §3, §4.5 and the certification paragraph now say "systems and institutions".
- **Part A §3.3:** institutional facts may be taken by link. **Part B §8.1 and §9:** institutional record link and one added reopening trigger.
- **CI-3.2 and CI-3.6:** pointers only. Field numbers were not used.
- **Repo wiring:** `tools/corpus_paths.py`, `footer_audit.py`, `core_filename_normalize.py`, `ch5_nested_list_candidate_audit.py`, `README.md`, `docs/corpus_index.md`, `TODO.md`, `doc_architecture.md` (Twelfth move), `project/MEMLOG.md`; derived files regenerated.

## Checks run

`make plain-terms-edition boundary-chunks print-pack reader-accessibility ai-corpus-sync hierarchy-map architecture-index`, then the full 94-target regression list through `run_chunk.py`. Result: all pass except `lexical-vocabulary-audit`, whose only findings are the 12 pre-existing "people" lines in Part A (same as the baseline before any edit). Audit findings on the new text were fixed along the way (bare "Charter", bold list lead-ins, a run-in label, one CI-8 title, and a title containing the banned bare word "drift", which Part D therefore cites as "Chapter Seven §4 Amendment and Review"). I did not re-read Part D against every Part A evaluation item; the audits check form and links, not whether the rules are right.

## Sign-off items (steward)

1. Composition by link, many to many (not containment).
2. Part D inside Chapter Nine; no rename, no new chapter.
3. One system means one pass and one record, with an institutional findings block.
4. No gate on forming or operating an institution. First certification is provisional, inside a class-scaled window set by the adopting instrument, modeled on the Article XXVIII-A clock. Needs a read against Article XI-E.
5. The Integrity forum leads. Institutional forums hold mandate and duty-compliance components.
6. Cascade: a failed, withdrawn, or expired cited System certification is an indicator (step down or no advance), and current misalignment only where the System's cause finding traces to the institution's own governance, incentives, resourcing, Institutional Charter, or portfolio.
7. Forums, certifiers, and record offices are institutions; no two bodies certify each other in a circle within one recertification cycle (new rule, §14.5).
8. Terms: "Institutional Alignment Certification" and "Institutional Certification Record".

## Differences from the evaluation

- Class L takes all six items in simplified form and omits none (Chapter Seven §2 says a Class L Charter may not omit a required item). The evaluation had suggested a shorter pass.
- Institution class: Chapter Seven's portfolio floor is kept. The own-impact class governs only the institution-only items (§12.1 rule 3). This is new.
- The standing bridge is extended to institutions as the attributed actor, since Chapter Ten already treats institutions as possible standing subjects.

## Not done

- Preamble owner-register and process-map entries for Part D; a CS-3 pointer to the institution class test.
- Translations (19 locales; already lagging).
- Chapter Seventeen §1 heightened review for the Chapter Thirteen edits.
- Check against `adoption/ANNOUNCEMENT.md` (not read).
- The untracked `* 2.md` copies were ignored and not touched.

## Git

Nothing committed or pushed. After you commit: `git push -u origin docs/ch09-institutional-alignment-certification` (GIT-PUSH-CL-01: report, do not run).
