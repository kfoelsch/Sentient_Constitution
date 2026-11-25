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
CHAPTER_OR_PART_RE = re.compile(r"\b(?:Chapter\s+(?:One|Two|Three|Four|Five|Six|Seven|Eight|Nine|Ten|Eleven|Twelve|Thirteen|Fourteen|Fifteen|Sixteen|Seventeen|Eighteen|Nineteen|Twenty-One|Twenty-Two|Twenty-Three|Twenty-Four|Twenty-Five|Twenty-Six|Twenty-Seven|Twenty-Nine|Twenty-Eight|Twenty|\d+)|Part\s+[A-E])\b", re.I)
D14_REFERENCE_RE = re.compile(r"\[[^\]]+\]\([^)]+\)|\*\*(?:Chapter\s+[A-Za-z0-9]+|(?:CF|CI|CJS|CS)-\d+(?:\.\d+)?(?:\s+§\s*\d+(?:\.\d+)*)?)\*\*", re.I)
CHAPTER_WORDS = (
    "Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
    "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen",
    "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty-One", "Twenty-Two",
    "Twenty-Three", "Twenty-Four", "Twenty-Five", "Twenty-Six", "Twenty-Seven",
    "Twenty-Eight", "Twenty-Nine", "Thirty", "Thirty-One",
)
CHAPTER_WORD_NUMBERS = {word.casefold(): n for n, word in enumerate(CHAPTER_WORDS)}
CHAPTER_LABEL_RE = re.compile(r"\bChapter\s+(" + "|".join(re.escape(w) for w in sorted(CHAPTER_WORDS, key=len, reverse=True)) + r"|\d+)\b", re.I)
LEGACY_SUBCORE_ID_RE = re.compile(r"^\s*\((\d{1,2}\.\d{3})(?:\s+§[^)]*)?\)")


def display(number: str) -> str:
    return f"{int(number[:2])}.{number[2:]}"


def run(root: Path, fail: bool) -> int:
    root = root.resolve()
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
    subcore_rows = {
        row.get("destination_file", ""): row
        for row in rows
        if row.get("layer") == "SUBCORE"
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
        if layer == "SUBCORE":
            # Subcore files (2026-11-20): numbered inside their chapter's home, displayed as S<chapter>-<letter>.
            if machine_id != f"SUB-{number}":
                problems.append(f"{number}: subcore machine id should be SUB-{number}")
            if not re.fullmatch(rf"S{int(number[:2])}-[A-Z]", row.get("display_id", "")):
                problems.append(f"{machine_id}: subcore display id must be S<chapter>-<letter>")
            if not Path(destination).name.startswith(f"subcore_{number[:2]}.{number[2:]}_"):
                problems.append(f"{destination}: filename must start with subcore_{number[:2]}.{number[2:]}_")
            if destination in seen_files:
                problems.append(f"{destination}: duplicate destination file")
            seen_files.add(destination)
            if not (root / destination).is_file():
                problems.append(f"{machine_id}: destination not present: {destination}")
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
    # Linked subcore citations must use their current Chapter home. A historical
    # chapter number in the link label or its adjacent dotted citation survived
    # the 2026 consolidation in ordinary prose, outside the original Trace-only
    # check, so inspect all local Markdown links in the binding corpus.
    candidates = list(root.glob("core_*.md")) + list(root.glob("subcore_*.md"))
    for folder in PREFIX_DIR.values():
        candidates.extend((root / folder).glob("*.md"))
    for path in candidates:
        source_rel = path.relative_to(root).as_posix()
        text = path.read_text(encoding="utf-8", errors="replace")
        for link in LINK_RE.finditer(text):
            label, target = link.groups()
            target_path = target.split("#", 1)[0]
            if not target_path:
                continue
            resolved = (path.parent / target_path).resolve()
            try:
                rel_target = resolved.relative_to(root).as_posix()
            except ValueError:
                continue
            row = subcore_rows.get(rel_target)
            if not row:
                continue
            current_home = int(row["core_home"])
            for chapter_match in CHAPTER_LABEL_RE.finditer(label):
                token = chapter_match.group(1)
                number = int(token) if token.isdigit() else CHAPTER_WORD_NUMBERS[token.casefold()]
                if number != current_home:
                    line_no = text.count("\n", 0, link.start()) + 1
                    problems.append(
                        f"{source_rel}:{line_no}: subcore link to {rel_target} labels it Chapter {token}; current home is Chapter {CHAPTER_WORDS[current_home]}"
                    )
            # Dotted chapter IDs were temporary navigation labels, not stable
            # subcore identities. Flag one only when it immediately follows the
            # link and exactly matches this row's recorded pre-consolidation ID.
            tail = text[link.end():]
            legacy_match = LEGACY_SUBCORE_ID_RE.match(tail)
            legacy_id = row.get("pre_consolidation_display_id")
            if (legacy_match and legacy_id and legacy_match.group(1) == legacy_id
                    and int(legacy_match.group(1).split(".", 1)[0]) != current_home):
                line_no = text.count("\n", 0, link.end()) + 1
                problems.append(
                    f"{source_rel}:{line_no}: subcore link to {rel_target} retains historical chapter ID ({legacy_id})"
                )

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
    counts = {layer: sum(1 for row in rows if row.get("layer") == layer) for layer in ("CORE", "SUBCORE")}
    corpus = len(rows) - counts["CORE"] - counts["SUBCORE"]
    expected = (data.get("expected_core_count"), data.get("expected_subcore_count"), 75)
    if (counts["CORE"], counts["SUBCORE"], corpus) != expected:
        problems.append(f"registry has {counts['CORE']} core, {counts['SUBCORE']} subcore and {corpus} corpus rows; expected {expected[0]}, {expected[1]} and {expected[2]}")
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
