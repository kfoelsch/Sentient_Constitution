#!/usr/bin/env python3
"""Validate the chapter-number registry and current chapter homes.

The migration introduces this audit in report-only mode. Pass --fail after the
content migration is complete to enforce all registry/file/home invariants.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REGISTRY = Path("tools/architecture/chapter_numbers.json")
PREFIX_DIR = {"CJS": "corpus_joint_structure", "CI": "corpus_institutions", "CS": "corpus_systems", "CF": "corpus_forum"}
TRACE_RE = re.compile(r'<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>\s*\n(.*?)\n</details>', re.S)
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
CORE_FILE_RE = re.compile(r"core_\d{2}\.\d{3}_[^/]+\.md$")
CHAPTER_OR_PART_RE = re.compile(r"\b(?:Chapter\s+(?:One|Two|Three|Four|Five|Six|Seven|Eight|Nine|Ten|Eleven|Twelve|Thirteen|Fourteen|Fifteen|Sixteen|Seventeen|Eighteen|Nineteen|\d+)|Part\s+[A-E])\b", re.I)
D14_REFERENCE_RE = re.compile(r"\[[^\]]+\]\([^)]+\)|\*\*(?:Chapter\s+[A-Za-z0-9]+|(?:CF|CI|CJS|CS)-\d+(?:\.\d+)?(?:\s+§\s*\d+(?:\.\d+)*)?)\*\*", re.I)


def display(number: str) -> str:
    return f"{int(number[:2])}.{number[2:]}"


def run(root: Path, fail: bool) -> int:
    data = json.loads((root / REGISTRY).read_text())
    rows = data.get("chapters", [])
    problems: list[str] = []
    if data.get("filename_number_format") != "CC.LSS":
        problems.append("registry filename_number_format must be CC.LSS")
    seen_numbers: set[str] = set()
    seen_files: set[str] = set()
    core_display = {
        row.get("destination_file", ""): row.get("display_id", "")
        for row in rows
        if row.get("layer") == "CORE"
    }
    for row in rows:
        layer = row.get("layer")
        number = row.get("machine_number", "")
        machine_id = row.get("machine_id", "")
        destination = row.get("destination_file", "")
        original = row.get("original_file", "")
        if not re.fullmatch(r"\d{5}", number):
            problems.append(f"{machine_id}: machine number must be five digits")
            continue
        expected_id = number if layer == "CORE" else f"{layer}-{number}"
        if machine_id != expected_id:
            problems.append(f"{number}: machine id should be {expected_id}")
        expected_display=display(number) if layer == 'CORE' else f"{layer}-{display(number)}"
        if row.get("display_id") != expected_display:
            problems.append(f"{machine_id}: dotted display id disagrees with formatter")
        layer_prefix = {"CORE": "core", "CJS": "cjs", "CI": "ci", "CS": "cs", "CF": "cf"}.get(layer)
        expected_filename_prefix = f"{layer_prefix}_{number[:2]}.{number[2:]}_" if layer_prefix else ""
        if not expected_filename_prefix or not Path(destination).name.startswith(expected_filename_prefix):
            problems.append(f"{destination}: filename must start with {expected_filename_prefix} (layer_CC.LSS_)")
        if number in seen_numbers:
            problems.append(f"{number}: duplicate number across layers")
        seen_numbers.add(number)
        if destination in seen_files:
            problems.append(f"{destination}: duplicate destination file")
        seen_files.add(destination)
        if layer != "CORE":
            if data.get("layer_digits", {}).get(layer) != number[2]:
                problems.append(f"{machine_id}: layer digit does not match registry")
            if number[:2] != row.get("core_home"):
                problems.append(f"{machine_id}: first two digits disagree with Core home")
            if Path(destination).parent.as_posix() != PREFIX_DIR.get(layer):
                problems.append(f"{destination}: layer folder mismatch")
        source_exists = (root / original).is_file()
        destination_exists = (root / destination).is_file()
        if not source_exists and not destination_exists:
            problems.append(f"{machine_id}: neither source nor destination exists ({original})")
        if source_exists and not destination_exists:
            problems.append(f"PENDING {machine_id}: destination not present: {destination}")
        elif layer != "CORE":
            text = (root / destination).read_text(errors="replace")
            if f"Core home: {row['core_home']}" not in text:
                problems.append(f"{machine_id}: missing Core home declaration")
            manifest_path = root / "ai_corpus/indexes/section_manifest.json"
            if manifest_path.is_file():
                manifest = json.loads(manifest_path.read_text()).get("files", {})
                headings = [section.get("header", "") for section in manifest.get(destination, {}).get("sections", [])]
                if row.get("legacy_section_ids") and not any(header.startswith(row["display_id"]) for header in headings):
                    problems.append(f"{destination}: no manifest heading carries {row['display_id']}")
    # D13: named core chapter/part links in Trace widgets carry the source
    # file's registry number and, where present, the linked section suffix.
    candidates = list(root.glob("core_*.md"))
    for folder in PREFIX_DIR.values():
        candidates.extend((root / folder).glob("*.md"))
    for path in candidates:
        try:
            source_rel = path.relative_to(root)
        except ValueError:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for widget in TRACE_RE.finditer(text):
            body = widget.group(1)
            for line_no, line in enumerate(body.splitlines(), 1):
                if line.startswith("- ") and len(D14_REFERENCE_RE.findall(line)) >= 4:
                    problems.append(f"{source_rel}: Trace line {line_no} has four or more inline references; D14 requires sub-bullets")
            for link in LINK_RE.finditer(body):
                label, target = link.groups()
                target_path = target.split("#", 1)[0]
                if not target_path or not CORE_FILE_RE.fullmatch(Path(target_path).name) or not CHAPTER_OR_PART_RE.search(label):
                    continue
                resolved = (path.parent / target_path).resolve()
                try:
                    rel_target = resolved.relative_to(root).as_posix()
                except ValueError:
                    continue
                number = core_display.get(rel_target)
                if not number:
                    problems.append(f"{source_rel}: Trace link targets unregistered core file {rel_target}")
                    continue
                section = re.search(r"§+\s*(\d+(?:\.\d+)*)", label)
                expected = f"({number}{f' §{section.group(1)}' if section else ''})"
                tail = body[link.end():]
                if not tail.lstrip().startswith(expected):
                    problems.append(f"{source_rel}: Trace link to {rel_target} must carry {expected}")
    if len(rows) != 118:
        problems.append(f"registry has {len(rows)} rows; expected 118 (42 core + 76 corpus)")
    print(f"CHAPTER-NUMBER-01: {len(rows)} registry rows; {len(problems)} findings")
    for problem in problems:
        print(f"  {problem}")
    if fail and problems:
        return 1
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--fail", action="store_true", help="return nonzero when findings remain")
    args = parser.parse_args()
    return run(args.root, args.fail)


if __name__ == "__main__":
    raise SystemExit(main())
