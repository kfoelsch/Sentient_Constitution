#!/usr/bin/env python3
"""Chapter Four ↔ Chapter Seven pointer discipline audit (advisory by default).

Flags Chapter Seven sections that restate Chapter Four verification-substrate
rules without upstream citations to Chapters Two through Four.

Rule: CH4-CH7-POINTER in tools/architecture/rule_registry.json.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

CH7_PART_A = "core_07_a_system_alignment_certification_evaluation.md"
CH7_PART_B = "core_07_b_system_alignment_certification_record_process.md"
CH7_FILES = (CH7_PART_A, CH7_PART_B)
CH4_FILE = "core_04-04_burden_traceability_verification.md"

# Operative phrases owned by Chapter Four §§1–6; Ch7 should cite upstream, not restate.
CH4_EXCLUSIVE_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("burden-allocation", re.compile(r"burden of (?:demonstrating )?compliance", re.I)),
    ("trace-artifact", re.compile(r"\btrace artifact\b", re.I)),
    (
        "definition-traceability",
        re.compile(r"Definition Traceability Requirement", re.I),
    ),
    (
        "security-constrained-observability",
        re.compile(r"Security-Constrained Observability", re.I),
    ),
    (
        "crypto-non-substitution",
        re.compile(r"Cryptographic controls do(?:\s+not|\s+\*\*not\*\*)", re.I),
    ),
    ("non-substitution", re.compile(r"\bnon-substitution\b", re.I)),
    (
        "science-informed-evidence",
        re.compile(r"science-informed evidence", re.I),
    ),
    (
        "observability-traceability",
        re.compile(r"Observability of Traceability", re.I),
    ),
    (
        "practical-illusory",
        re.compile(r"practically illusory", re.I),
    ),
    (
        "theoretical-verifiability",
        re.compile(r"theoretical verifiability", re.I),
    ),
    (
        "bidirectional-omac",
        re.compile(r"bidirectional,\s+such that", re.I),
    ),
]

UPSTREAM_POINTER_RE = re.compile(
    r"Chapters?\s+(?:Two\s+through\s+Four|Two\s+and\s+Three)|Chapter\s+Four|"
    r"core_02-03|core_04-04|Ch(?:apter)?\s*2[–-]4",
    re.I,
)

NON_RESTATEMENT_RE = re.compile(r"does not restate", re.I)

SECTION_HEADING_RE = re.compile(r"^###\s+(.+)$")
HIGH_COUPLING_SECTIONS = {
    "12. transparency, auditability, and contestability",
    "14. supervisory sequence and contestability chain",
    "15. relationship to standing",
}

HIGH_COUPLING_TERMS_RE = re.compile(
    r"\b(?:independently reviewable|security-justified limits|practicable challenge|"
    r"verification accessibility|security-constrained)\b",
    re.I,
)


def _strip_details_blocks(text: str) -> str:
    """Remove nested <details> blocks; keep operative prose for heuristic scan."""
    out: list[str] = []
    i = 0
    lines = text.splitlines()
    while i < len(lines):
        line = lines[i]
        if line.strip().lower().startswith("<details"):
            depth = 1
            i += 1
            while i < len(lines) and depth:
                if lines[i].strip().lower().startswith("<details"):
                    depth += 1
                elif lines[i].strip().lower().startswith("</details"):
                    depth -= 1
                i += 1
            continue
        out.append(line)
        i += 1
    return "\n".join(out)


def _split_sections(content: str) -> list[tuple[str, int, str]]:
    lines = content.splitlines()
    sections: list[tuple[str, int, str]] = []
    current_title = "preamble"
    current_start = 1
    current_lines: list[str] = []

    for idx, line in enumerate(lines, start=1):
        match = SECTION_HEADING_RE.match(line)
        if match:
            if current_lines or current_title != "preamble":
                sections.append(
                    (current_title, current_start, "\n".join(current_lines))
                )
            current_title = match.group(1).strip()
            current_start = idx
            current_lines = [line]
        else:
            current_lines.append(line)

    if current_lines:
        sections.append((current_title, current_start, "\n".join(current_lines)))
    return sections


def _section_has_upstream_pointer(section_text: str) -> bool:
    if UPSTREAM_POINTER_RE.search(section_text):
        return True
    if NON_RESTATEMENT_RE.search(section_text):
        return True
    return False


def scan_ch7(root: Path) -> list[str]:
    findings: list[str] = []

    for ch7_file in CH7_FILES:
        path = root / ch7_file
        if not path.is_file():
            findings.append(f"{ch7_file}: missing Chapter Seven file")
            continue

        content = path.read_text(encoding="utf-8")

        # Corpus placement should name Chapter Four as verification-substrate owner.
        placement_match = re.search(
            r"<summary>.*?Corpus placement.*?</summary>\s*(.*?)</details>",
            content,
            re.S | re.I,
        )
        if placement_match:
            placement = placement_match.group(1)
            if "Verification substrate owner" not in placement and ch7_file == CH7_PART_A:
                findings.append(
                    f"{ch7_file}: corpus placement missing Verification substrate owner bullet"
                )
            if not UPSTREAM_POINTER_RE.search(placement) and ch7_file == CH7_PART_A:
                findings.append(
                    f"{ch7_file}: corpus placement missing Chapters Two through Four upstream pointer"
                )
        elif ch7_file == CH7_PART_A:
            findings.append(f"{ch7_file}: corpus placement reader-guidance block not found")

        for title, start_line, section_text in _split_sections(content):
            title_key = title.lower()
            operative = _strip_details_blocks(section_text)

            for label, pattern in CH4_EXCLUSIVE_PATTERNS:
                if pattern.search(operative) and not _section_has_upstream_pointer(
                    section_text
                ):
                    findings.append(
                        f"{ch7_file}:{start_line}: §{title} restates Chapter Four "
                        f"substrate ({label}) without upstream pointer to Chapters Two through Four"
                    )

            if title_key in HIGH_COUPLING_SECTIONS:
                if HIGH_COUPLING_TERMS_RE.search(operative) and not _section_has_upstream_pointer(
                    section_text
                ):
                    findings.append(
                        f"{ch7_file}:{start_line}: §{title} high-coupling verification language "
                        "without upstream pointer to Chapters Two through Four"
                    )

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Repository root")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit non-zero when findings exist (default: report only)",
    )
    args = parser.parse_args()
    root = Path(args.root).resolve()

    findings = scan_ch7(root)

    print("Chapter Four ↔ Chapter Seven pointer discipline audit:")
    if findings:
        print("- Result: FAIL" if args.strict else "- Result: ADVISORY")
        for item in findings:
            print(f"  - {item}")
        return 1 if args.strict else 0

    print("- Result: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
