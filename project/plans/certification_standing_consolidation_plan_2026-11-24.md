# Certification and standing chapter consolidation plan

**Status:** Complete (custodian requested implementation on 2026-11-24; completed 2026-11-25). Existing rules were relocated without changing constitutional meaning. The clause inventory and crosswalk were reconciled against the resulting files; see the numbered move log for the repeatable workflow and verification record. The edition remains pre-release and this is not adoption.

## Goal and proposed chapter map

Give readers one accessible core chapter for each process, with detailed, equally binding rules in attached subcore files. Preserve all duties and protections. The current 31 numbered chapters become 25: Chapters 8–16 consolidate into three, reducing the count by six. Chapter Thirty-One was added after the plan's initial map and therefore also moves, to Chapter Twenty-Five.

| Current chapters | Proposed chapter | Process |
| --- | --- | --- |
| 8–10 | 8 | System alignment certification |
| 11–13 | 9 | Institutional alignment certification |
| 14–16 | 10 | Standing assessment: records, measurement, and integration |
| 17–30 | 11–24, respectively | Existing subjects, in the same order |
| 31 | 25 | Incorporation (current Chapter Thirty-One) |

The existing subcores of the consolidated chapters become subcores of their new chapter; choose final file boundaries and letter labels after the clause inventory. The chapter-number registry is the numbering source. The resulting summaries and subcores have equal constitutional force; navigational or illustrative material does not create duties.

The final detail structure uses six linked subcores per chapter so classification, evaluation, forum roles, outcomes, records, and continuing review stay easy to locate. Chapter Eight covers system classification, evaluation, forum seats and sequence, forum outcomes, record contents, and continuing review. Chapter Nine covers institutional classification, evaluation, forum seats and readiness, forum outcomes, new material authority and system reopening, and continuing records. Chapter Ten covers event types and fields, verification, route descriptors and input tables, measurement, integration order, and integration effects. The [714-clause crosswalk](certification_standing_clause_crosswalk_2026-11-24.md) points to the resulting detail files; the [source snapshot](certification_standing_obligation_snapshot_2026-11-24.json) preserves the before inventory.

## Reader-facing design

Each core chapter should explain the whole process in its natural order, identify its major guarantees and practical consequences, and link to the exact subcore rules at each step. Use concise language, a small process diagram, and links to worked examples. Do not set a word limit before the inventory: preserve the qualifications a reader needs to understand the result.

### Proposed Chapter 8: system certification

Explain scope and class; applicable evaluations; independent forum review and stakeholder participation; outcomes, certification conditions and the go-live gate; the published record, challenge, monitoring, recertification, and reopening. Explain the limited bridge to standing. Group detailed classification and scaling, evaluation and domain tests, seats and procedures, outcome and go-live mechanics, record contents, ongoing review and challenge in navigable subcores. Existing Subcores 8-A, 9-A, and 10-A are starting points; split large topics rather than creating an unmanageable file.

### Proposed Chapter 9: institutional certification

Follow the same sequence as system certification. State prominently that an institution may form and continue operating without certification, while its systems have their own go-live rules. Preserve the defined wait and qualifications for new material authority. Explain the one-system, several-system, and no-system cases; the limits of institutional outcomes; and how institutional and system findings interact. Move detailed class tests, evaluation items, forum seats and sequence, outcomes, conditions, record requirements, reopening, new authority and system-reopening mechanics to subcore. Existing Subcores 11-A, 12-A, and 13-A are starting points.

### Proposed Chapter 10: standing assessment

Organize around the existing three questions: **What happened? How good or bad was it? What follows?** Explain verified records and challenge; separate contribution and violation measurement; and integration and handoff to the consequence chapters. Keep visible the verified-input gate, separate axes and no offset, the distinction between allegations and verified findings, the prohibition on changing facts or measurement to reach a preferred result, and that standing is not a rating of inherent worth. Measurement alone does not authorize a liberty restriction. Explain that applicable locks control blocked pathways. The downstream consequence chapters retain their own rules: integration begins Question 3, not the entirety of its answer.

Group the detail in subcores for (1) event types, verification, record fields, opening authority, custody, versioning and handling; (2) measurement dimensions, descriptors, scaling, LEQU and axis assignment, with tables split if useful; and (3) integration records, processing order, automation and review, descriptors, attachments and continuity. Existing Subcores 14-A, 15-A, and 16-A are starting points.

## Implementation sequence

1. **Baseline and inventory.** Fetch the shared branch and establish the current state. Capture an obligation inventory and chapter, section and anchor map. Inventory each binding clause in current Chapters 8–16 and their subcores, including actors, duties, conditions, exceptions, thresholds, clocks, rights, evidence, and remedies.
2. **Destination crosswalk.** Map every clause and source section to its proposed core or subcore destination, including one-to-many moves and essential summaries. Identify current chapter-number references and registered corpus homes. Record where a detail is fully stated and where its guarantee is summarized. Resolve ambiguous meaning with the custodian rather than choosing it during relocation.
3. **Move the detail.** Relocate rules with wording and context preserved wherever possible. Check every surrounding qualification and cross-reference. Assign clear authoritative homes and avoid competing formulations. Update registry and historical compatibility metadata for changed identifiers, including ambiguous legacy identifiers; do not add prohibited redirect anchors.
4. **Write and review the core chapters.** Draft the three binding summaries against the mapped source text. Preserve the important limits and exceptions above, add direct links to detail, and check each summary for changed meaning. A change to duty, authority, threshold, clock, or scope requires a separate decision.
5. **Renumber and reconnect.** Apply the full map through the chapter-number registry, filenames, headings, links, citations, owner registers, section references, Mermaid charts, front doors, run sheets, illustrations, and affected implementation-corpus homes and identifiers. Check every local link to a subcore against the registry: its chapter label must match the subcore's current Core home, and it must not retain a superseded dotted chapter ID. Run `make chapter-number-audit` for this full-corpus link check. Then sweep every current Mermaid chart source across the repository, compare chapter labels and named owners with the current chapter registry and headings, correct stale labels, and regenerate derived chart outputs. Compare the chapter numbers and linked title labels in Chapter One’s owner-register sections with the chapter registry and canonical headings. Regenerate other affected indexes and generated files. Preserve translations and translation work; translation is paused. Maintain historical mapping for later reconciliation.
6. **Check meaning and usability.** The before and after inventories each contain 714 clauses; the source-backed inventory comparison passes, and all 714 crosswalk rows point to existing detail files. Walkthroughs confirmed the system path from classification through independently verified go-live conditions and record publication; the institution path through classification, the defined wait and limited blockers for new material authority, and reopening of affected systems; and the standing path from verified event and challenge record, through separate contribution and violation measurements, to ordered integration, locks, and consequence handoff. The system and institution walkthroughs also use their existing worked illustrations. Confirm that each core chapter communicates the basic process without requiring a detour into subcore.
7. **Complete repository verification and delivery.** Follow the current move-log and shared-branch rules. Run `make preflight` after each edit and `make chapter-number-audit`, `make chapter-number-audit-test`, relevant link, anchor, chart and front-door checks, and `make audit-report` before completion. Fix source-backed findings without weakening audits, refresh and commit affected generated files, push the coherent move to `work`, and sync and verify the central checkout. Keep the published branch consistent: develop in stages if needed, but deliver the structural renumbering as one coordinated change.

## Completion criteria

- All 714 inventoried clauses have a reviewed destination; the before and after inventory comparison passes.
- Three accessible chapters describe the processes and link to equal-force detail; downstream consequence rules remain discoverable.
- Chapter numbering, cross-references, charts, front doors, registry, historical mappings and generated artifacts agree; paused translation files are preserved.
- Every current Mermaid chart source was reviewed after renumbering; chapter labels and referenced owners agree with the current registry and headings, and generated chart outputs were rebuilt.
- Chapter One’s owner-register headings and linked chapter titles were checked against the current registry and canonical headings.
- Required audits pass, the move is logged and committed, and the shared branch and central checkout are synchronized.
