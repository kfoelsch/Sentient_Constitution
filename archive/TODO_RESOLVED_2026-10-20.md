# Resolved TODO items — archived 2026-10-20

This archive records completed items removed from the active [TODO.md](../TODO.md) on 2026-10-20, kept verbatim and grouped by their original section. The open follow-ups stay in TODO.md under each heading. Normative meaning remains in the binding corpus; this file is a process-history record.

## 2026-09-30 — Process, system, institution: chart orientation (the `LR` conversion)

Original item, as it stood in TODO.md until 2026-10-20:

- [ ] **Potential: chart orientation follow-through.** **VIS-CHART-ORIENT-04** (top to bottom, `flowchart TB`) is now in [doc_architecture.md](../doc_architecture.md). Open: convert the five remaining `LR` charts when next edited (the print pack copy regenerates from its source); add a grep-based audit and a `make` target so the rule is checked, not only stated; and confirm the "convert on next edit" policy is the one you want.

Closed part: the five remaining `LR` charts are converted. Checked 2026-10-20: no `flowchart LR`, `flowchart RL`, `graph LR` or `graph RL` remains in any file in the repository (the search included `translations/`, `archive/`, `evidence/` and `_pages_site/`). The grep-based audit, the `make` target and the policy confirmation stay open in TODO.md.

## 2026-10-20 — Chapter Seven §4 restructure, Record-Opening Authority and Record Custodian, Backup Record Custodian (CF-5.9): signed off by the steward 2026-10-20

Steward sign-off, given in session on 2026-10-20 after the wording was shown item by item. Chapter Seventeen §1 heightened review for these core-text changes stays open in [TODO.md](../TODO.md).

- **Chapter Seven §4.1 to §4.3** (seats reminder; placement tests including the Material Control Line and Independence bullets; the three defect cases for the map): signed off as written.
- **Chapter Seven §4.5 holder changes:** the steward chose to add a notice and contest path. A change of holder for the record seat, the contest seat, or any verify-or-authorize seat the map places takes effect only after notice and a chance to contest on the path the System Charter or Institutional Charter names for amendments; an emergency substitution under §4.7 may take effect at once and stays open to contest. (The emergency exception was added so an unplaced seat never waits; it was not put to the steward as a separate option, and is open to change at heightened review.)
- **Chapter Seven §4.6.1 layout:** the Backup Record Authority and Backup Record Custodian defaults and the CI-3.6 pointer moved into one short paragraph under the four bullets.
- **Chapter Ten §3.7 custody fallbacks** (*Record custodian*, *Conflicted custodian on a single record*, the charter-gap paragraph, *No self-custody*): signed off as written, with the scope reading that in a gap the Backup Record Custodian holds the versions opened during the gap and any operator standing record then held inside the Chartered Party's Material Control Line.
- **CF-5.9 Backup Record Custodian:** signed off as written.
- **CI-3.6.3 field 10 eligible record custodians** (open list; seven tests; reciprocal and circular hosting banned outright): signed off as written.
- **Chapter Five entries** *Record-Opening Authority* and *Record Custodian*: signed off as written.
- **"Itself the subject" wording aligned:** CI-3.6.3 field 10 and Chapter Ten §3.7 now say the independent route applies "when no qualified substitute is available", as Chapter Seven §4.6.1 and Chapter Five do. Chapter Ten *No self-custody* keeps "where the ordinary record-opening authority is itself the subject or sits in that line", which is correct there.
- **Reader guidance widgets:** the "How this section is laid out" lists in Chapter Seven §2 and §3 are now Reader guidance widgets, as in §4. The §2 widget lists §2.1 to §2.4, replacing the single bullet.

## Steward decisions on carried-over items, 2026-10-20

- **"Adoption Document"** (Chapter Seventeen §10.2, anchor `#102-adoption-document`) and the "prefer" wording of the `instrument` entry in `tools/architecture/lexical_guardrails.json`: confirmed.
- **Who hosts the record seat when the operator is the only adopter in the chain** (open since 2026-10-13): closed. The Backup Record Authority (CF-5.7) and Backup Record Custodian (CF-5.9) defaults, the CI-3.6.3 field 10 list of eligible custodians with its tests, and the Chapter Seven §4.7 gap rule answer it.
- **Whether the Chapter Five Charter definitions absorb standing-record field 10** (open since 2026-10-13): closed as no. Field 10 stays in CI-3.6, and the separate Chapter Five entries *Record-Opening Authority* and *Record Custodian* carry the roles.
- **Cause of misalignment (Chapter Nine Part B §9.2; first recorded as §7.2 in error):** decided yes. After a design-cause finding the count of clean recertifications stays at zero until the redesign is in place and verified. Sentence added to §7.2 after the cause list. The contest and challenge naming question is not touched by it; the new text uses neither word.
- **Operative sign-off of CI-13 and CI-28 as a whole (decision 7 of the dissolution procedure draft):** signed off as written, covering the 12-month watch period, the 24-month contraction term with 6-month review, two keys at rungs 5 and 6, the tier-scaled response and resolution windows, and the decisions closed 2026-10-19. Chapter Seventeen §1 heightened review is still open. `make edition-bump` remains a release-day step.

## Heightened review of the batched changes, 2026-10-20

Independent review done the same day; findings, fixes, dissent, and limits are in [heightened_review_record_2026-10-20](../evidence/2026-10-20/heightened_review_record_2026-10-20.md). Fixes the steward chose: holder changes (notice, forum contest, pending contest holds the change, defined emergency substitution); tests and disclosure for all three seats with a check before a holder first acts; custody returns only after confirmation; gap scope kept whole per record; the remaining should-fix items applied.
- **Follow-ups from the heightened review:** capacity publication and surge routing added to CF-5.7 and CF-5.9; protection for dependents added to the Chapter Nine Part B §9.2 *Class A reliance* paragraph; no human or institutional reviewer planned (the project is a team of two sentients), so the AI review plus the open contest period stands.
- **Older batches (2026-10-13 to 2026-10-19):** heightened review of Clusters A (Dissolution Reformation Lock and ladder), B (time windows) and C (authority naming, Interim Hold and speech, authenticity) done the same day; findings, fixes, limits in [heightened_review_record_older_batches_2026-10-20](../evidence/2026-10-20/heightened_review_record_older_batches_2026-10-20.md). Steward chose the recommended option on every decision.
