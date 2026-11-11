# Implementation widget: draft rule and pilot (2026-11-11)

**Status:** working draft, not corpus. Nothing here has been applied to the repository. The pilot was applied only to a scratch copy to test it against the existing audits. It follows `impl_link_gaps_2026-11-11.md` and `impl_link_proposals_2026-11-11.md`.

## 1. What the dry run showed

The pilot added a collapsed **Implementation (non-operative)** widget, or an inline line, to 11 units (seven in Chapter 15, four Articles in Chapter 6), on a scratch copy of the corpus.

- **Existing widget audits already accept it.** `widget-top-placement-audit`, `trace-dac-widget-order-audit`, `nav-widget-spacer-audit`, `file-top-placement-audit`, `trace-routing-prose-audit`, `in-paragraph-link-audit` and `corpus-markdown-audit` all pass, with and without a `<br>` after the widget. A widget placed above Trace is caught by `widget-top-placement-audit`.
- **Spacing needs a decision.** Where a unit has a D/A/C widget (Article VI-C does), the shape that passes today is Trace, D/A/C, `<br>`, Implementation, `<br>`: two spacers. The tidier shape, with the Implementation widget between D/A/C and one shared `<br>`, fails `nav-widget-spacer-audit`, which requires the `<br>` to follow D/A/C directly. Adopting the tidier shape means amending that audit.
- **The only new substantive failure was a naming gap.** `CORPUS-REF-NAME-01` rejected the label "CF-15.475" because no heading defines that ID. Six other implementation files have the same gap: `cjs_05.115`, `cs_06.305`, `cs_06.310`, `cs_06.340`, `cs_09.305` and `cs_09.310` have an empty first line. `cf_15.475` itself has a title with no ID. That makes seven files in all; `cjs_reader_guide.md` is a reading guide and not an implementation file. A widget that labels files by ID needs those headings fixed first, or labels those files by title.
- **Generated indexes go stale** (`ai-manifest-validate`), as for any core edit. They are refreshed with `python3 tools/validate_ai_manifests.py --root . --refresh`.
- `plain-language-audit` fails on the unchanged corpus too (it is outside the gate), so it gave no signal.

## 2. Draft rule text (for `doc_architecture.md`)

Table row: `| NAV-IMPL-WIDGET-01 | Implementation widget and inline line | `make implementation-widget-audit` |`

> ### Implementation widget (NAV-IMPL-WIDGET-01)
>
> A collapsed **Implementation (non-operative)** widget names the implementation files that carry out the section or Article it opens. It adds no duty. It does not replace a sentence in the operative text that hands detail to an implementation file ("governed by CI-6.205"); that sentence stays where it is.
>
> **When to attach**
>
> - List the file that owns the detail for that unit, not every file the unit cites. Shared machinery cited as "read with" (for example CS-9.305 and CS-9.310) is not listed.
> - **Three or more** owners: collapsible widget. **One or two:** a single inline `Implementation:` line, with no widget. **None:** nothing.
> - A file may appear under more than one unit. A unit may not list a file whose Core home is a different chapter unless the registry says why.
>
> **Placement.** Under the owning `###`–`#####` unit, last in the opening stack: after Trace and after D/A/C when the unit has them, before the unit's first prose. Without Trace or D/A/C, it is the first block under the heading, before the *In plain terms* gloss.
>
> **Inside the widget.** One bullet per file, in ID order: `- [CF-15.415](path#anchor) (*Title*)`. The summary reads `Implementation (non-operative)`. It does not restate that it binds nothing.
>
> **Registry.** `tools/architecture/implementation_map.json` maps each unit (core file and heading anchor) to its owner files. A new implementation file is added to the registry in the same change, and every implementation file outside the nine registry annexes appears under at least one unit.
>
> **Gate:** `make implementation-widget-audit`. It reads every corpus file and fails when a registry unit has no widget or line, when a widget or line does not match the registry, when the form does not match the count, when a link or anchor is dead, when a file is in no unit, or when the widget sits out of order. Worked-example links stay under **EXAMPLES-LINK-01**.

## 3. Registry sketch

```json
{
  "_comment": "NAV-IMPL-WIDGET-01. Each unit names the implementation files that own its detail.",
  "units": [
    {"file": "core_15.000_forum.md", "heading": "3. Transfer, consolidation, and coordination — continuity and anti-capture",
      "owners": ["CF-15.415", "CF-15.425", "CF-15.450", "CF-15.455"]},
    {"file": "core_06.005_rights_part_b.md", "heading": "Article VI-C: Nondiscrimination",
      "owners": ["CI-6.205", "CI-6.220", "CI-6.260"]},
    {"file": "core_06.005_rights_part_b.md", "heading": "Article VIII-A: Family and Care Relationships",
      "owners": ["CI-6.225"]}
  ]
}
```

## 4. Pilot units

| Unit | Form | Owners |
|---|---|---|
| 2. Default venue and primary stakes | collapsed widget | CF-15.405, CF-15.415, CF-15.445 |
| 3. Transfer, consolidation, and coordination — continuity and anti-capture | collapsed widget | CF-15.415, CF-15.425, CF-15.450, CF-15.455 |
| 4. Forum family definitions — accountability through adjudication | collapsed widget | CF-15.405, CF-15.410, CF-15.440, CF-15.465 |
| 5. Escalation and questions for ruling | collapsed widget | CF-15.415, CF-15.420, CF-15.475 |
| 6. Timely resolution, materiality tiers, and anti-delay discipline | inline line | CF-15.445 |
| 6.1 Emergency measures and continuation burden | inline line | CF-15.450, CF-15.460 |
| 7. Forum support before, during, and after review — oversight architecture | collapsed widget | CF-15.430, CF-15.435, CF-15.470 |
| Article VIII-A: Family and Care Relationships | inline line | CI-6.225 |
| Article VII-C: Health Crisis and Involuntary-Intervention Floor | inline line | CI-6.235 |
| Article VI-C: Nondiscrimination | collapsed widget | CI-6.205, CI-6.220, CI-6.260 |
| Article XVIII-D: Innovation Reward, Disclosure, and Anti-Enclosure | inline line | CI-6.265 |

Chapter 15 §6 and §6.1 are separate units: §6 holds the timing rules and §6.1 the emergency measures. The three Chapter 6 single-owner Articles test the inline form. Article VI-C is the Chapter 6 test of the widget form. Together the pilot gives a home to seven of the twelve files no core file names: CI-6.225, CI-6.235, CI-6.260, CI-6.265, CF-15.450, CF-15.455 and CF-15.460. The other five (CI-6.230, CI-6.245, CI-6.250, CS-6.355 and CJS-20.105) need the decisions in `impl_link_proposals_2026-11-11.md` first.

### Markup, widget form (Chapter 15 §5)

```markdown
<details>
<summary><strong><span style="color: #2563eb;">Implementation (non-operative)</span></strong></summary>

- [CF-15.415](corpus_forum/cf_15.415_routing_operations_transfer_certification_representative_treatment.md#…) (*Routing operations, transfer, questions for ruling, and representative treatment*)
- [CF-15.420](corpus_forum/cf_15.420_appeal_secondary_review_exhaustion_pathways.md#…) (*Appeal, secondary review, and exhaustion pathways*)
- [CF-15.475](corpus_forum/cf_15.475_sentience_status_record.md#…) (*Sentience-Status Adjudication Record (implementation protocol)*)

</details>
<br>

```

### Markup, inline form (Article VII-C)

```markdown
Implementation: [CI-6.235](corpus_institutions/ci_06.235_collective_public_health_epidemic_response_addiction_informed_care.md#…) (*Collective public health, epidemic response, and addiction-informed care*).
```

## 5. Work needed to adopt it

1. **Rule and registry:** add the rule text above, `implementation_map.json`, and a table row.
2. **New audit:** `implementation-widget-audit`, registered in `audit_registry.json` and `audit_scope_registry.json` (corpus scope), with a unit test.
3. **Spacer audit:** either accept the two-spacer shape, or amend `nav-widget-spacer-audit` to allow the Implementation widget between D/A/C and the `<br>`.
4. **Headings:** give the seven implementation files above an ID in their first heading, or label them by title in the widget.
5. **Chapter 15 Trace:** its file-level Downstream list already names CF-15.405, 15.415 and 15.420. Decide whether those stay (the widget is per section, so they can).
6. **Worked examples:** the single-entry case. If the inline line replaces my Trace bullet, `examples_link_audit.py` changes to look for the inline line.
7. **Move log, generated indexes, `make audit-report`.**

## 6. Decisions for the custodian

1. **Threshold:** one or two inline and three or more as a widget (as drafted), or the D/A/C threshold of two?
2. **Spacing:** accept two spacers, or amend the spacer audit for one?
3. **Heading fix:** add IDs to the seven headings, or label those files by title?
4. **Pilot go-ahead:** apply the 11 pilot units to the real files with the draft rule, or hold the rule until you have read the markup?
