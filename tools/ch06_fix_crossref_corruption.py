#!/usr/bin/env python3
"""Fix cross-ref corruption from ch06_parallel_axis_restructure (section 5. -> 5.1. on 5.2)."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# (path, old, new) — order matters within each file
FIXES: list[tuple[str, str, str]] = [
    # Chapter Eleven — restore internal §5 / §6
    ("core_10-10_misconduct.md", "section 5.1.2** only", "section 6** only"),
    ("core_10-10_misconduct.md", "section 5.1.2** named", "section 6** named"),
    ("core_10-10_misconduct.md", "section 5.1.1.2", "section 6.1"),
    ("core_10-10_misconduct.md", "boundary in **section 5.1**", "boundary in **section 5**"),
    ("core_10-10_misconduct.md", "Chapter Nine Chapter One §8.1.2", "Chapter Nine Chapter One §6.2"),
    # Chapter Twelve — restore internal §6; fix Ch6 refs
    ("core_12_forum.md", "(**section 5.1**)", "(**section 5**)"),
    ("core_12_forum.md", "Chapter Nine **section 5.1.2** severity", "Chapter Nine **section 5.2** severity"),
    ("core_12_forum.md", "unless **section 5.1.2** transfers", "unless **section 6** transfers"),
    ("core_12_forum.md", "(with **section 5.1.2**)", "(with **section 6**)"),
    ("core_12_forum.md", "under **section 5.1.2**", "under **section 6**"),
    ("core_12_forum.md", "[Chapter Nine Chapter One §8.1.2](core_10_standing_integration.md#71-shared-domain-lenses-cross-axis-vocabulary)", "[Chapter Ten Chapter One §8.1](core_10_standing_integration.md#71-shared-domain-lenses-cross-axis-vocabulary)"),
    ("core_12_forum.md", "[Chapter Nine Chapter One §8.1.2.3](core_10_standing_integration.md#73-stackable-harm-and-conduct-descriptors-violation-nature-supplement)", "[Chapter Ten §3.9](core_10_standing_integration.md#73-stackable-harm-and-conduct-descriptors-violation-nature-supplement)"),
    ("core_12_forum.md", "[Chapter Nine Chapter One §8.1.2](core_09_standing_assessment.md#34-violation-axis-rules-violation-nature-adverse-findings-and-severity)", "[Chapter Nine Chapter One §6.2](core_09_standing_assessment.md#34-violation-axis-rules-violation-nature-adverse-findings-and-severity)"),
    ("core_12_forum.md", "[Chapter Nine Chapter One §8.1](core_10_standing_integration.md#6-extended-axis-ii-legal-hybrid-duty-and-harm-descriptors)", "[Chapter Ten §3](core_10_standing_integration.md#6-extended-axis-ii-legal-hybrid-duty-and-harm-descriptors)"),
    ("core_12_forum.md", "**section 5.1** primary category defaults", "**§4** primary category defaults"),
    # Chapter Ten — Ch6 severity refs
    ("core_10_standing_integration.md", "Chapter Nine section 5.1.1.2", "Chapter Nine section 5.2"),
    ("core_10_standing_integration.md", "Chapter Nine section 5.1.2", "Chapter Nine section 5.2"),
    ("core_10_standing_integration.md", "Chapter Nine **section 5.1.1.2**", "Chapter Nine **section 5.2**"),
    ("core_10_standing_integration.md", "Chapter Nine **section 5.1.2**", "Chapter Nine **section 5.2**"),
    # Implementation scale
    ("implementation/CH06_NINE_SLOT_STANDING_SCALE.md", "Chapter Nine section 5.1.1.2", "Chapter Nine section 5.2"),
    ("implementation/CH06_NINE_SLOT_STANDING_SCALE.md", "**section 5.1.2** severity", "**section 5.2** severity"),
    # Chapter One / Ten corruption
    ("core_06_rights_part_a.md", "section 5.1.2 interaction rules", "section 6 interaction rules"),
    ("corpus_systems/cs_00_registry_and_reading_rules.md", "Chapter One** section 5.1.2.4", "Chapter One** section 6.4"),
    # Corpus Ch9 §6
    ("corpus_joint_structure/cjs_03a_accountability_operations.md", "Chapter Twelve**, **section 5.1.2**", "Chapter Twelve**, **section 6**"),
    ("corpus_forum/cf_06_appeal_secondary_review_exhaustion_pathways.md", "Chapter Twelve**, **section 5.1.2**", "Chapter Twelve**, **section 6**"),
    ("core_10-10_misconduct.md", "[Chapter Nine Chapter One §8.1.7](core_10_standing_integration.md#67-duty-to-resist-unlawful-or-unconstitutional-instructions)", "[Chapter Ten §6.7](core_10_standing_integration.md#67-duty-to-resist-unlawful-or-unconstitutional-instructions)"),
    ("core_10-10_misconduct.md", "[Chapter Nine Chapter One §8.1.6](core_10_standing_integration.md#410-collective-accountability-and-acquiescent-participation)", "[Chapter Ten Chapter One §8.10](core_10_standing_integration.md#410-collective-accountability-and-acquiescent-participation)"),
    ("corpus_forum/cf_04_panel_formation_disclosure_recusal_bench_constitution.md", "Chapter Nine Chapter One §8.1.2", "Chapter Nine Chapter One §6.2"),
]
    for rel, old, new in FIXES:
        path = ROOT / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        if old in text:
            path.write_text(text.replace(old, new), encoding="utf-8")
            print(f"fixed {rel}")


if __name__ == "__main__":
    main()
