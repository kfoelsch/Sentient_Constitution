# Conceptual overview follow-up resolution

**Completed:** 2026-09-17. **Edition:** `SC-Corpus-2026.08.09`, pre-release. **Status:** working-tree process-support correction; not adoption or publication.

**Subsequent quality check and correction (2026-09-17):** The [quality check](alignment_followup_quality_check.md) found remaining textual gaps and that the broad audit task was not complete. The [textual resolution](remaining_textual_issues_resolution.md) closes those textual gaps; the broader audit task remains open. The account below records the earlier correction.

## Textual alignment

`CONCEPTUAL_OVERVIEW.md` now:

- labels and lists seven opening questions;
- states that later-stage coordination alone does not justify a deadline extension and names the continuing necessity, proportionality, and no-less-restrictive-feasible-alternative showing, while preserving intake, preservation, interim-protection, restore-challenge, and outer-bound clocks;
- explains equal foundational political voice, the narrower domain of stake-weighted participation, pathway-scoped ordinary locks, the qualifying final Chapter Ten withholding rule, good-faith inability protections, restoration routes, and liberty-restriction limits;
- explains silence by default, no-record ordinary access, anti-aggregation, the lived burden of lawful locks, and lower-slot archival after restoration;
- explains provisional inclusion and independent representation during sentience uncertainty, including the rule that protection belongs to the entity rather than the operator; and
- states the Authority Stack ordering as owner/source status, canonical Chapter Five definitions, integrated Chapter One reading, and Internal Hierarchy only as a last-resort residual rule.

The three local companion edition footers in CS-12, CI-26, and CJS-3i now inherit edition and effective date from `README.md`; the corpus edition was not advanced.

## Audit repair

The three unnamed section citations in `core_06_rights_part_a.md` and `core_06_rights_part_b.md` now include section titles. The `doc_architecture.md` audit example no longer contains a link to a nonexistent `#132-pro-competition-and-anti-domination` fragment.

Validation:

- `python3 tools/section_cite_name_audit.py --root . --changed-only` — PASS
- `python3 tools/section_label_anchor_audit.py --root .` — PASS
- `python3 tools/reference_audit.py --root .` — PASS
- `python3 tools/validate_ai_manifests.py --root . --check-freshness` — PASS

The full section-citation scan still reports the repository’s broader pre-existing backlog; only the changed-only gate is used for this repair, consistent with the prior resolution record. The deferred P1 regression/evidence workflow was not reinstated.
