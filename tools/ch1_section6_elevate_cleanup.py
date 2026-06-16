#!/usr/bin/env python3
"""Post-migration label fixes for Chapter One §6 elevation."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REPLACEMENTS: list[tuple[str, str]] = [
    # core_00-01_principles.md sequence + plain terms
    (
        "*In plain terms: shared systems must keep building real productive capacity — without letting wealth, power, or control pile up in a few hands. **§6–§6.5** carry productive-capacity discipline",
        "*In plain terms: shared systems must keep building real productive capacity — without letting wealth, power, or control pile up in a few hands. **§6.1–§6.5** carry productive-capacity discipline",
    ),
    (
        "Read together with the sections that follow, **§§6–9** form a sequence:\n"
        "- **§6** — shared-system capacity, contestability, and anti-concentration discipline\n"
        "- **§8** — stewardship, distributed understanding, and institutional learning\n"
        "- **§9** — conflict-resolution and tradeoff procedure among values, rights, and constraints\n"
        "- **§10** — whole-system validation before classification, governance, limitation, or compliance claims can stand",
        "Read together with the sections that follow, **§§6–9** form a sequence:\n"
        "- **§6** — shared-system capacity, contestability, and anti-concentration discipline\n"
        "- **§7** — stewardship, distributed understanding, and institutional learning\n"
        "- **§8** — conflict-resolution and tradeoff procedure among values, rights, and constraints\n"
        "- **§9** — whole-system validation before classification, governance, limitation, or compliance claims can stand",
    ),
    ("section **7.2.2**", "section **9.2.2**"),
    ("[7.2.2 Stewardship and Operator Incentive Alignment]", "[9.2.2 Stewardship and Operator Incentive Alignment]"),
    ("[7.2.1 Alignment Requirement]", "[9.2.1 Alignment Requirement]"),
    ("(#6-shared-system-capacity-and-stewardship)", "(#6-shared-system-capacity)"),
    ("[§11 Freedom (Bounded Agency)]", "[§10 Freedom (Bounded Agency)]"),
    ("[§11 Freedom]", "[§10 Freedom]"),
    ("§11 Freedom", "§10 Freedom"),
    ("[§8 Stewardship and Distributed Understanding]", "[§7 Stewardship and Distributed Understanding]"),
    ("Chapter One §9.2 — Epistemic Disclosure Constraints", "Chapter One §8.2 — Epistemic Disclosure Constraints"),
    (
        "[6.1.1 Reversibility-under-uncertainty](core_01_stewardship_capacity_principles.md#811-proportionality-necessity-and-reversibility-under-uncertainty)",
        "[8.1.1 Proportionality](core_01_stewardship_capacity_principles.md#911-proportionality)",
    ),
    (
        "[6.1.1 Proportionality, Necessity, and Reversibility under Uncertainty](core_01_stewardship_capacity_principles.md#811-proportionality-necessity-and-reversibility-under-uncertainty)",
        "[8.1.1 Proportionality](core_01_stewardship_capacity_principles.md#911-proportionality)",
    ),
    (
        "[7.1.4 Voluntary Discontinuation and Exit Rights](core_01_stewardship_capacity_principles.md#1014-voluntary-discontinuation-and-exit-rights)",
        "[9.1.4 Voluntary Discontinuation and Exit Rights](core_01_stewardship_capacity_principles.md#1014-voluntary-discontinuation-and-exit-rights)",
    ),
    (
        "[§8 Stewardship and Distributed Understanding — §7.2 Distributed Understanding]",
        "[§7 Stewardship and Distributed Understanding — §7.2 Distributed Understanding]",
    ),
    (
        "*In plain terms: shared systems should help sentients live better over time — more real capacity, less waste. **Productive Capacity** is the durable ability to turn time, effort, and resources into constitutionally aligned outcomes. **Constitutional Efficiency** asks whether that happens without burning more sentient time, attention, and shared resources than necessary. Neither label counts if the \"gain\" comes from hoarding wealth or power, cheating metrics, stripping rights, or loading harm onto others or the planet. **§6.3–§6.5** carry the anti-concentration discipline",
        "*In plain terms: shared systems should help sentients live better over time — more real capacity, less waste. **Productive Capacity** is the durable ability to turn time, effort, and resources into constitutionally aligned outcomes. **Constitutional Efficiency** asks whether that happens without burning more sentient time, attention, and shared resources than necessary. Neither label counts if the \"gain\" comes from hoarding wealth or power, cheating metrics, stripping rights, or loading harm onto others or the planet. **§6.3–§6.5** carry the anti-concentration discipline",
    ),
]


def main() -> int:
    for path in sorted(ROOT.glob("core_*.md")):
        text = path.read_text(encoding="utf-8")
        original = text
        for old, new in REPLACEMENTS:
            text = text.replace(old, new)
        if text != original:
            path.write_text(text, encoding="utf-8")
            print(f"updated {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
