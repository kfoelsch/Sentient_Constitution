#!/usr/bin/env python3
"""Remove legacy duplicate anchors from core_06; update corpus links."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CH06 = ROOT / "core_06-06_standing_assessment.md"

KEEP = {
    "chapters-six-nine-constitutional-compass",
    "chapter-six-compliance-violation-and-standing-model",
    "chapter-six-part-a-orientation",
    "2-purpose-and-role",
    "2-standing-records",
    "chapter-six-part-b-oversight-foundation",
    "21-standing-records-as-the-unit-of-application",
    "contribution-standing-record",
    "violation-standing-record",
    "22-standing-record-operational-requirements",
    "211-related-record-cross-references",
    "212-minimum-record-contents",
    "verified-inputs-for-standing",
    "216-collective-and-actor-specific-records",
    "213-versioning",
    "214-implementation-visibility",
    "215-implementation-tools",
    "227-forum-boundary",
    "chapter-six-part-c-accountability-gate",
    "23-linked-records-and-no-offset-bridge",
    "3-primary-axis-categories-slot-grammar-and-defaults",
    "chapter-six-part-d-flourishing-measure",
    "31-slot-grammar-and-display-labels",
    "311-what-the-slot-grammar-does",
    "312-table-1-slot-display-labels",
    "313-how-to-read-table-1",
    "32-constitutional-outcome-baseline-for-slots",
    "33-primary-category-defaults-and-lequ-slot-baseline",
    "34-violation-axis-rules-violation-nature-adverse-findings-and-severity",
    "chapter-six-part-e-accountability-measure",
    "41-formal-non-compliance",
    "42-remedial-substantive-non-compliance",
    "43-constitutional-substantive-non-compliance",
    "44-duty-based-or-negligent-harm-violation",
    "45-aggravated-violation",
    "46-coercive-or-safeguard-process-violation",
    "47-critical-non-compliance",
    "48-adjacent-level-application-notes",
}

REDIRECT: dict[str, str] = {
    "1-purpose-and-role": "2-purpose-and-role",
    "chapters-six-eight-standing-pipeline-map": "chapters-six-nine-constitutional-compass",
    "2-primary-contribution-and-violation-levels": "2-standing-records",
    "2-standing-effect-verified-inputs-forums": "2-standing-records",
    "2-standing-records-and-verified-inputs": "2-standing-records",
    "25-standing-record-operational-underpinnings": "22-standing-record-operational-requirements",
    "25-standing-record-operational-requirements": "22-standing-record-operational-requirements",
    "251-scope-and-bounded-subject": "22-standing-record-operational-requirements",
    "221-scope-and-bounded-subject": "22-standing-record-operational-requirements",
    "252-assessment-path": "212-minimum-record-contents",
    "222-assessment-path": "212-minimum-record-contents",
    "224-related-record-cross-references": "211-related-record-cross-references",
    "254-related-record-cross-references": "211-related-record-cross-references",
    "225-minimum-record-contents": "212-minimum-record-contents",
    "255-minimum-record-contents": "212-minimum-record-contents",
    "31-verified-input-gate": "verified-inputs-for-standing",
    "3-verified-inputs-forums-and-no-offset-rules": "verified-inputs-for-standing",
    "253-collective-and-actor-specific-records": "216-collective-and-actor-specific-records",
    "223-collective-and-actor-specific-records": "216-collective-and-actor-specific-records",
    "213-versioning-and-implementation-visibility": "213-versioning",
    "226-versioning-and-implementation-visibility": "213-versioning",
    "256-versioning-and-implementation-visibility": "213-versioning",
    "23-verified-inputs-and-forum-boundary": "227-forum-boundary",
    "23-dispute-phase-material-forums-and-challenge-protections": "227-forum-boundary",
    "221-dispute-phase-material-forums-and-challenge-protections": "227-forum-boundary",
    "32-dispute-phase-material-forums-and-challenge-protections": "227-forum-boundary",
    "214-separate-records-and-no-netting": "23-linked-records-and-no-offset-bridge",
    "216-separate-records-and-no-netting": "23-linked-records-and-no-offset-bridge",
    "215-separate-records-and-no-netting": "23-linked-records-and-no-offset-bridge",
    "24-coexistence-and-no-offset-bridge": "23-linked-records-and-no-offset-bridge",
    "24-linked-records-and-no-offset-bridge": "23-linked-records-and-no-offset-bridge",
    "33-coexistence-and-no-offset-bridge": "23-linked-records-and-no-offset-bridge",
    "3-primary-axis-categories-and-slot-defaults": "4-primary-axis-categories-slot-grammar-and-defaults",
    "3-primary-axis-categories-slot-grammar-and-defaults": "3-primary-axis-categories-slot-grammar-and-defaults",
    "4-primary-axis-categories-slot-grammar-and-defaults": "3-primary-axis-categories-slot-grammar-and-defaults",
    "21-two-axis-map": "31-slot-grammar-and-display-labels",
    "30-slot-grammar-and-display-labels": "31-slot-grammar-and-display-labels",
    "40-slot-grammar-and-display-labels": "31-slot-grammar-and-display-labels",
    "211-what-the-map-does": "311-what-the-slot-grammar-does",
    "401-what-the-slot-grammar-does": "311-what-the-slot-grammar-does",
    "212-table-1-slot-display-labels": "312-table-1-slot-display-labels",
    "402-table-1-slot-display-labels": "312-table-1-slot-display-labels",
    "213-how-to-read-table-1": "313-how-to-read-table-1",
    "403-how-to-read-table-1": "313-how-to-read-table-1",
    "41-lequ-baseline": "32-constitutional-outcome-baseline-for-slots",
    "22-lequ-baseline": "32-constitutional-outcome-baseline-for-slots",
    "2-lequ-baseline": "32-constitutional-outcome-baseline-for-slots",
    "22-constitutional-outcome-baseline-for-slots": "32-constitutional-outcome-baseline-for-slots",
    "41-constitutional-outcome-baseline-for-slots": "32-constitutional-outcome-baseline-for-slots",
    "42-constitutional-outcome-baseline-for-slots": "32-constitutional-outcome-baseline-for-slots",
    "42-axis-i-contribution-state-and-standing-effect": "33-primary-category-defaults-and-lequ-slot-baseline",
    "214-table-2-primary-category-defaults": "33-primary-category-defaults-and-lequ-slot-baseline",
    "3-primary-category-defaults-and-lequ-slot-baseline": "33-primary-category-defaults-and-lequ-slot-baseline",
    "4-primary-category-defaults-and-lequ-slot-baseline": "33-primary-category-defaults-and-lequ-slot-baseline",
    "42-primary-category-defaults-and-lequ-slot-baseline": "33-primary-category-defaults-and-lequ-slot-baseline",
    "32-contribution-axis-rules-contribution-state-positive-only": "33-primary-category-defaults-and-lequ-slot-baseline",
    "2-axis-i-contribution-state-and-standing-effect": "33-primary-category-defaults-and-lequ-slot-baseline",
    "3-axis-i-contribution-state-and-standing-effect": "33-primary-category-defaults-and-lequ-slot-baseline",
    "30-scope-contribution-state-and-standing-effect": "33-primary-category-defaults-and-lequ-slot-baseline",
    "20-scope-contribution-state-and-standing-effect": "33-primary-category-defaults-and-lequ-slot-baseline",
    "301-contribution-state-axis-i-positive-only": "33-primary-category-defaults-and-lequ-slot-baseline",
    "201-contribution-state-axis-i-positive-only": "33-primary-category-defaults-and-lequ-slot-baseline",
    "302-co-occurrence-with-violation-nature": "33-primary-category-defaults-and-lequ-slot-baseline",
    "202-co-occurrence-with-violation-nature": "33-primary-category-defaults-and-lequ-slot-baseline",
    "303-standing-effect": "33-primary-category-defaults-and-lequ-slot-baseline",
    "203-standing-effect": "33-primary-category-defaults-and-lequ-slot-baseline",
    "304-informal-and-non-institutional-contribution": "33-primary-category-defaults-and-lequ-slot-baseline",
    "204-informal-and-non-institutional-contribution": "33-primary-category-defaults-and-lequ-slot-baseline",
    "305-relationship-to-section-7-domain-lenses": "33-primary-category-defaults-and-lequ-slot-baseline",
    "305-relationship-to-section-5-domain-lenses": "33-primary-category-defaults-and-lequ-slot-baseline",
    "205-relationship-to-section-5-domain-lenses": "33-primary-category-defaults-and-lequ-slot-baseline",
    "305-relationship-to-section-12-domain-lenses": "33-primary-category-defaults-and-lequ-slot-baseline",
    "205-relationship-to-section-12-domain-lenses": "33-primary-category-defaults-and-lequ-slot-baseline",
    "31-baseline-contribution": "33-primary-category-defaults-and-lequ-slot-baseline",
    "21-baseline-contribution": "33-primary-category-defaults-and-lequ-slot-baseline",
    "32-positive-contribution": "33-primary-category-defaults-and-lequ-slot-baseline",
    "33-stewardship-positive-contribution": "33-primary-category-defaults-and-lequ-slot-baseline",
    "34-champion-contribution": "33-primary-category-defaults-and-lequ-slot-baseline",
    "33-violation-axis-rules-violation-nature-adverse-findings-and-severity": "34-violation-axis-rules-violation-nature-adverse-findings-and-severity",
    "43-violation-axis-rules-violation-nature-adverse-findings-and-severity": "34-violation-axis-rules-violation-nature-adverse-findings-and-severity",
    "4-axis-ii-violation-nature-legal-constitutional-type": "34-violation-axis-rules-violation-nature-adverse-findings-and-severity",
    "3-axis-ii-violation-nature-legal-constitutional-type": "34-violation-axis-rules-violation-nature-adverse-findings-and-severity",
    "40-scope-violation-nature-and-standing-inputs": "34-violation-axis-rules-violation-nature-adverse-findings-and-severity",
    "401-violation-nature-axis-ii-adverse-findings": "34-violation-axis-rules-violation-nature-adverse-findings-and-severity",
    "402-co-occurrence-with-contribution-state-axis-i": "34-violation-axis-rules-violation-nature-adverse-findings-and-severity",
    "403-standing-effect-inputs-forums-findings": "34-violation-axis-rules-violation-nature-adverse-findings-and-severity",
    "404-forum-phase-material-and-pathways": "34-violation-axis-rules-violation-nature-adverse-findings-and-severity",
    "405-relationship-to-section-7-domain-lenses": "34-violation-axis-rules-violation-nature-adverse-findings-and-severity",
    "405-relationship-to-section-5-domain-lenses": "34-violation-axis-rules-violation-nature-adverse-findings-and-severity",
    "31-formal-non-compliance": "41-formal-non-compliance",
    "42-substantive-non-compliance": "42-remedial-substantive-non-compliance",
    "43-aggravated-violation": "45-aggravated-violation",
    "44-critical-non-compliance": "47-critical-non-compliance",
    "4-extended-axis-ii-legal-hybrid-and-duty-categories": "34-violation-axis-rules-violation-nature-adverse-findings-and-severity",
    "5-extended-axis-i-standing-hooks-and-supplements": "33-primary-category-defaults-and-lequ-slot-baseline",
    "5-axis-i-extended": "33-primary-category-defaults-and-lequ-slot-baseline",
}

ANCHOR_LINE = re.compile(r'^<a id="([^"]+)"></a>\s*$')
INLINE_ANCHOR = re.compile(r'<a id="([^"]+)"></a>')


def prune_ch06(text: str) -> str:
    out: list[str] = []
    for line in text.splitlines():
        m = ANCHOR_LINE.match(line)
        if m:
            aid = m.group(1)
            if aid == "1-purpose-and-role":
                out.append('<a id="2-purpose-and-role"></a>')
                continue
            if aid not in KEEP:
                continue
        # Strip inline legacy anchors in table cells
        if INLINE_ANCHOR.search(line) and not ANCHOR_LINE.match(line):
            def repl(match: re.Match[str]) -> str:
                aid = match.group(1)
                return "" if aid not in KEEP else match.group(0)

            line = INLINE_ANCHOR.sub(repl, line)
        out.append(line)
    return "\n".join(out) + "\n"


def update_links(text: str) -> str:
    for old, new in sorted(REDIRECT.items(), key=lambda x: -len(x[0])):
        text = text.replace(f"core_06-06_standing_assessment.md#{old}", f"core_06-06_standing_assessment.md#{new}")
        text = text.replace(f"core_06-06_standing_assessment.md##{old}", f"core_06-06_standing_assessment.md#{new}")
        # same-file anchors
        text = re.sub(rf"\(#{re.escape(old)}\)", f"(#{new})", text)
        text = re.sub(rf"\(#{re.escape(old)}-", f"(#{new}-", text)
    return text


def main() -> None:
    ch06_text = CH06.read_text()
    pruned = prune_ch06(ch06_text)
    CH06.write_text(update_links(pruned))

    for path in ROOT.rglob("*"):
        if path == CH06 or path.name.startswith("."):
            continue
        if path.suffix not in {".md", ".json"}:
            continue
        if "archive/" in str(path) or "tools/ch06_prune" in str(path):
            continue
        original = path.read_text()
        updated = update_links(original)
        if updated != original:
            path.write_text(updated)

    print("Pruned legacy anchors in core_06 and updated corpus links.")


if __name__ == "__main__":
    main()
