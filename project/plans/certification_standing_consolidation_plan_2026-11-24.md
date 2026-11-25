# Certification and standing chapter consolidation plan

**Status:** In implementation (custodian requested implementation on 2026-11-24). The work relocates existing rules without changing constitutional meaning; any unresolved choice about a duty, authority, threshold, clock, or scope must be presented to the custodian. Chapter numbers below describe the corpus at plan creation unless marked proposed; the current corpus map was reconciled on 2026-11-24 before structural edits.

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

The initial destination boundary is one detailed subcore for each existing process phase: classification/evaluation, forum/outcomes, and records/continuing review for system and institutional certification; records/verification, measurement, and integration for standing. The clause-level crosswalk and preserved 714-clause source inventory are in [the certification and standing crosswalk](certification_standing_clause_crosswalk_2026-11-24.md) and [its source snapshot](certification_standing_obligation_snapshot_2026-11-24.json). These destinations are provisional until each surrounding provision is checked during relocation.

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
5. **Renumber and reconnect.** Apply the full map through the chapter-number registry, filenames, headings, links, citations, owner registers, section references, Mermaid charts, front doors, run sheets, illustrations, and affected implementation-corpus homes and identifiers. Regenerate derived indexes and other affected generated files. Preserve translations and translation work; translation is paused. Maintain historical mapping for later reconciliation.
6. **Check meaning and usability.** Compare the before and after obligation inventories and account for every difference with a clause-level review; mechanical comparison alone does not prove equivalence. Walk through a system go-live, an institution seeking new material authority, and a standing case through all three questions. Confirm that each core chapter communicates the basic process without requiring a detour into subcore.
7. **Complete repository verification and delivery.** Follow the current move-log and shared-branch rules. Run `make preflight` after each edit and `make chapter-number-audit`, `make chapter-number-audit-test`, relevant link, anchor, chart and front-door checks, and `make audit-report` before completion. Fix source-backed findings without weakening audits, refresh and commit affected generated files, push the coherent move to `work`, and sync and verify the central checkout. Keep the published branch consistent: develop in stages if needed, but deliver the structural renumbering as one coordinated change.

## Completion criteria

- All current binding clauses and qualifications have a reviewed destination, with discrepancies resolved or explicitly presented for decision.
- Three accessible chapters describe the processes and link to equal-force detail; downstream consequence rules remain discoverable.
- Chapter numbering, cross-references, charts, front doors, registry, historical mappings and generated artifacts agree; paused translation files are preserved.
- Required audits pass, the move is logged and committed, and the shared branch and central checkout are synchronized.
