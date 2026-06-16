#!/usr/bin/env python3
"""Migrate core_01_stewardship_capacity_principles.md#anchor links after Chapter One split."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PREAMBLE = "core_00_preamble.md"
VALUES = "core_01_values_principles.md"
PART_B = "core_01_stewardship_capacity_principles.md"
CH1_UPSTREAM = (
    "[core_00_preamble.md](core_00_preamble.md), "
    "[core_01_values_principles.md](core_01_values_principles.md), and "
    "[core_01_stewardship_capacity_principles.md](core_01_stewardship_capacity_principles.md)"
)

PREAMBLE_ANCHORS = {
    "constitutional-triad",
    "material-stake",
    "material-family-orientation",
    "chapter-00-preamble--foundational-requirements",
}

# old_anchor -> new_anchor (Part B only; file is PART_B)
PART_B_ANCHOR_REMAP = {
    "7-stewardship-and-distributed-understanding": "6-stewardship-and-distributed-understanding",
    "522-stewardship": "61-stewardship",
    "521-distributed-understanding": "62-distributed-understanding",
    "52-distributed-understanding-and-stewardship": "6-stewardship-and-distributed-understanding",
    "62-stewardship-and-distributed-understanding": "6-stewardship-and-distributed-understanding",
    "621-stewardship": "61-stewardship",
    "92-incentive-alignment-and-system-capture": "7-governance-under-stewardship-discipline",
    "921-alignment-requirement": "73-alignment-requirement",
    "922-stewardship-and-operator-incentive-alignment": "74-stewardship-and-operator-incentive-alignment",
    "923-role-depth-and-material-responsibility-pathways": "75-role-depth-and-material-responsibility-pathways",
    "924-misalignment-correction-and-capture-response": "76-misalignment-correction-and-capture-response",
    "925-contingent-claims-games-of-chance-and-event-contract-markets": "77-contingent-claims-games-of-chance-and-event-contract-markets",
    "822-stewardship-and-operator-incentive-alignment": "74-stewardship-and-operator-incentive-alignment",
    "6-shared-system-capacity": "8-shared-system-capacity",
    "6-shared-system-capacity-and-stewardship": "8-shared-system-capacity",
    "61-shared-system-capacity": "8-shared-system-capacity",
    "61-productive-capacity-instrumental-good": "81-productive-capacity-instrumental-good",
    "51-productive-capacity-instrumental-good": "81-productive-capacity-instrumental-good",
    "511-productive-capacity-instrumental-good": "81-productive-capacity-instrumental-good",
    "611-productive-capacity-instrumental-good": "81-productive-capacity-instrumental-good",
    "62-constitutional-efficiency": "82-constitutional-efficiency",
    "612-constitutional-efficiency": "82-constitutional-efficiency",
    "63-concentration-threshold-mechanism-adopter-tunable": "83-concentration-threshold-mechanism-adopter-tunable",
    "511-concentration-threshold-mechanism-adopter-tunable": "83-concentration-threshold-mechanism-adopter-tunable",
    "613-concentration-threshold-mechanism-adopter-tunable": "83-concentration-threshold-mechanism-adopter-tunable",
    "64-pro-competition-and-anti-domination": "84-pro-competition-and-anti-domination",
    "614-pro-competition-and-anti-domination": "84-pro-competition-and-anti-domination",
    "65-consolidation-ceiling": "85-consolidation-ceiling",
    "615-consolidation-ceiling": "85-consolidation-ceiling",
    "8-interaction-and-conflict-resolution": "9-interaction-and-conflict-resolution",
    "7-interaction-and-conflict-resolution": "9-interaction-and-conflict-resolution",
    "81-core-tradeoff-principles": "91-core-tradeoff-principles",
    "71-core-tradeoff-principles": "91-core-tradeoff-principles",
    "811-proportionality": "911-proportionality",
    "711-proportionality": "911-proportionality",
    "812-necessity": "912-necessity",
    "813-minimization-of-harm": "913-minimization-of-harm",
    "814-minimization-of-avoidable-burden": "914-minimization-of-avoidable-burden",
    "714-minimization-of-avoidable-burden": "914-minimization-of-avoidable-burden",
    "614-minimization-of-avoidable-burden": "914-minimization-of-avoidable-burden",
    "82-epistemic-disclosure-constraints": "92-epistemic-disclosure-constraints",
    "821-preservation-of-epistemic-integrity": "921-preservation-of-epistemic-integrity",
    "621-preservation-of-epistemic-integrity": "921-preservation-of-epistemic-integrity",
    "822-trust-truth-alignment": "922-trust-truth-alignment",
    "722-trust-truth-alignment": "922-trust-truth-alignment",
    "83-freedom-limitation-constraints": "93-freedom-limitation-constraints",
    "831-constraint-on-freedom": "931-constraint-on-freedom",
    "63-freedom-preservation": "931-constraint-on-freedom",
    "832-time-consistency-constraint": "932-time-consistency-constraint",
    "84-rights-collision-procedure": "94-rights-collision-procedure",
    "841-rights-collision-decision-test": "941-rights-collision-decision-test",
    "741-rights-collision-decision-test": "941-rights-collision-decision-test",
    "842-proxy-divergence-invalidation": "942-proxy-divergence-invalidation",
    "742-proxy-divergence-invalidation": "942-proxy-divergence-invalidation",
    "9-systemic-evaluation-requirement": "10-systemic-evaluation-requirement",
    "8-systemic-evaluation-requirement": "10-systemic-evaluation-requirement",
    "91-required-evaluation-factors": "101-required-evaluation-factors",
    "81-required-evaluation-factors": "101-required-evaluation-factors",
    "911-systemic-scope-and-risk-factors": "1011-systemic-scope-and-risk-factors",
    "912-accessibility-under-sentience-non-exclusion": "1012-accessibility-under-sentience-non-exclusion",
    "913-privacy-informational-joint-invocation": "1013-privacy-informational-joint-invocation",
    "914-voluntary-discontinuation-and-exit-rights": "1014-voluntary-discontinuation-and-exit-rights",
    "915-assembly-collective-organization-and-institutional-formation": "1015-assembly-collective-organization-and-institutional-formation",
    "10-freedom-bounded-agency": "11-freedom-bounded-agency",
    "9-freedom-bounded-agency": "11-freedom-bounded-agency",
    "11-prohibition-on-absolute-override": "12-prohibition-on-absolute-override",
    "10-prohibition-on-absolute-override": "12-prohibition-on-absolute-override",
    "12-integrated-application": "13-integrated-application",
    "11-integrated-application": "13-integrated-application",
    # legacy / orphan anchors from older elevations
    "71-anti-concentration-substantive-fairness-and-materiality-factors": "101-required-evaluation-factors",
    "72-distributed-understanding": "62-distributed-understanding",
    "51-shared-system-capacity": "8-shared-system-capacity",
    "52-stewardship-and-distributed-understanding": "6-stewardship-and-distributed-understanding",
    "5-shared-system-capacity": "8-shared-system-capacity",
}

VALUES_ANCHOR_PREFIXES = (
    "1-",
    "2-",
    "3-",
    "32-",
    "321-",
    "322-",
    "323-",
    "324-",
    "325-",
    "326-",
    "327-",
    "4-",
    "41-",
    "42-",
    "43-",
    "44-",
    "441-",
    "442-",
    "443-",
    "444-",
    "445-",
    "5-",
    "51-",
    "two-constitutional-aims",
    "flourishing",
    "continuity",
)

SKIP_DIRS = {".git", "node_modules", "archive", "evidence", "implementation"}

LINK_RE = re.compile(r"core_00-01_principles\.md#([a-z0-9.-]+)")


def target_for_anchor(anchor: str) -> str:
    if anchor in PREAMBLE_ANCHORS:
        return f"{PREAMBLE}#{anchor}"
    if anchor in PART_B_ANCHOR_REMAP:
        return f"{PART_B}#{PART_B_ANCHOR_REMAP[anchor]}"
    if anchor in ("two-constitutional-aims", "flourishing", "continuity"):
        return f"{VALUES}#{anchor}"
    if any(anchor.startswith(p) for p in VALUES_ANCHOR_PREFIXES if p.endswith("-")):
        return f"{VALUES}#{anchor}"
    if anchor in VALUES_ANCHOR_PREFIXES:
        return f"{VALUES}#{anchor}"
    # default: Part B with same anchor (may be legacy redirect)
    return f"{PART_B}#{anchor}"


def migrate_file_refs(text: str) -> tuple[str, int]:
    count = 0
    old = "[core_00_preamble.md](core_00_preamble.md), [core_01_values_principles.md](core_01_values_principles.md), and [core_01_stewardship_capacity_principles.md](core_01_stewardship_capacity_principles.md)"
    if old in text:
        n = text.count(old)
        text = text.replace(old, CH1_UPSTREAM)
        count += n
    old2 = "`core_00_preamble.md`, `core_01_values_principles.md`, and `core_01_stewardship_capacity_principles.md`"
    new2 = "`core_00_preamble.md`, `core_01_values_principles.md`, and `core_01_stewardship_capacity_principles.md`"
    if old2 in text:
        n = text.count(old2)
        text = text.replace(old2, new2)
        count += n
    return text, count


def migrate_text(text: str) -> tuple[str, int]:
    count = 0

    def repl(match: re.Match[str]) -> str:
        nonlocal count
        anchor = match.group(1)
        count += 1
        return target_for_anchor(anchor)

    text, n_file = migrate_file_refs(text)
    count += n_file
    return LINK_RE.sub(repl, text), count


def iter_files() -> list[Path]:
    paths: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix not in {".md", ".py", ".json", ".mmd"}:
            continue
        if path.name == "core_00-01_principles.md":
            continue
        paths.append(path)
    return paths


def main() -> int:
    total = 0
    changed_files = 0
    for path in iter_files():
        original = path.read_text(encoding="utf-8")
        updated, n = migrate_text(original)
        if n:
            path.write_text(updated, encoding="utf-8")
            total += n
            changed_files += 1
            print(f"{path.relative_to(ROOT)}: {n}")
    print(f"\nMigrated {total} links in {changed_files} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
