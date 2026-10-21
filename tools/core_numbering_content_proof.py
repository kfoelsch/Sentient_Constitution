#!/usr/bin/env python3
"""Compare core and corpus prose with the pre-migration tree.

The pre-migration ref must be present locally. The proof normalizes chapter IDs
and Markdown links, removes Core home declarations, and omits Trace widgets
(they have an independent D13/D14 check). Plain-language companion lines may
move during file-top repair, so their content is compared separately.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TRACE_RE = re.compile(
    r'<details>\s*<summary><strong><span style="color: #2563eb;">Trace</span>'
    r'</strong></summary>.*?</details>', re.S
)
LINK_RE = re.compile(r"(!?)\[([^\]]*)\]\(([^)]*)\)")
CORPUS_ID_RE = re.compile(r"\b(?:CJS|CI|CS|CF)-\d{1,5}(?:\.\d+)*(?:\s*§\s*\d+(?:\.\d+)*)?\b", re.I)


def plain_terms(text: str) -> list[str]:
    return re.findall(r"(?m)^\*In plain terms:.*$", text)


def normalized(
    text: str,
    names: dict[str, str],
    shared_lists: dict[str, str],
    section_map: dict[str, str] | None = None,
) -> str:
    text = TRACE_RE.sub("<TRACE>", text)
    text = re.sub(r"(?m)^Core home:.*$", "", text)
    text = re.sub(r"<a\s+(?:id|name)=[\"'][^\"']+[\"'][^>]*>\s*</a>", "", text, flags=re.I)
    text = re.sub(r"(?m)^\*In plain terms:.*$", "", text)
    expanded_names = dict(names)
    expanded_names.update({Path(current).name: Path(original).name for current, original in names.items()})
    for current, original in sorted(expanded_names.items(), key=lambda item: -len(item[0])):
        text = text.replace(current, original)
    if section_map:
        alternatives = "|".join(
            re.escape(current)
            for current in sorted(section_map, key=len, reverse=True)
        )
        pattern = re.compile(r"(?<![A-Za-z0-9-])(?:" + alternatives + r")(?![A-Za-z0-9.])")
        text = pattern.sub(lambda match: section_map[match.group(0)], text)
    for current, original in sorted(shared_lists.items(), key=lambda item: -len(item[0])):
        text = text.replace(current, original)
    # The formatter may bold a migrated identifier where the legacy citation
    # was plain. Citation emphasis is not surrounding prose, so normalize it.
    text = re.sub(r"(?:\*\*|__)(?=(?:CJS|CI|CS|CF)-\d)", "", text, flags=re.I)
    text = re.sub(r"((?:CJS|CI|CS|CF)-\d[\d.]*)\*\*|((?:CJS|CI|CS|CF)-\d[\d.]*)__", lambda match: match.group(1) or match.group(2), text, flags=re.I)
    # Targets are expected to change during a numbering migration, but link
    # labels are reader-facing content and must remain visible to this proof.
    text = LINK_RE.sub(lambda match: match.group(1) + match.group(2), text)
    text = CORPUS_ID_RE.sub("<CORPUS-ID>", text)
    # A shared legacy ID can expand to several chapter-specific IDs during the
    # migration. Treat a contiguous Markdown list of those IDs as one citation
    # group here; identifier correctness is checked by the migration audits.
    text = text.replace("**<CORPUS-ID>**", "<CORPUS-ID>")
    text = re.sub(
        r"<CORPUS-ID>(?:(?:,\s*|\s+and\s+|,\s+and\s+|\s*[–—-]\s*)<CORPUS-ID>)+",
        "<CORPUS-ID>",
        text,
    )
    text = "\n".join(
        re.sub(r"\*\*|__", "", line) if "<CORPUS-ID>" in line else line
        for line in text.splitlines()
    )
    # CS-9.305's SAC bridge was moved from the legacy §7 grouping to §6.4.
    text = text.replace("§7 SAC bridge", "§6.4 SAC bridge")
    # The migration's widget placement repair removed redundant standalone
    # <br> spacers and varied blank-line counts without changing paragraph text.
    text = re.sub(r"^\s*<br>\s*$", "", text, flags=re.M)
    return "\n".join(line.rstrip() for line in text.splitlines() if line.strip())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--baseline", default="pre-chapter-numbering-2026-10-21")
    args = parser.parse_args()
    root = args.root.resolve()
    registry = json.loads((root / "tools/architecture/chapter_numbers.json").read_text())
    crosswalk = json.loads((root / "tools/architecture/chapter_crosswalk.json").read_text())
    rows = registry["chapters"]
    names = {row["destination_file"]: row["original_file"] for row in rows}
    sys.path.insert(0, str(root / "tools"))
    import renumber_corpus_chapters as migration

    _unique, shared = migration.id_map(registry)
    shared_lists = {}
    for old, destinations in shared.items():
        rendered = (", ".join(destinations[:-1]) + ", and " + destinations[-1]
                    if len(destinations) > 2 else " and ".join(destinations))
        shared_lists[rendered] = old
    section_map = {}
    for item in crosswalk.get("sections", []):
        legacy = item.get("legacy_section_id", "")
        if "." not in legacy:
            continue
        for current in (item.get("display_id", ""), item.get("machine_id", "")):
            if current:
                section_map[current] = legacy

    checked = 0
    mismatches = []
    core_checked = 0
    corpus_checked = 0
    for row in rows:
        try:
            before = subprocess.check_output(
                ["git", "show", f"{args.baseline}:{row['original_file']}"],
                cwd=root, text=True, stderr=subprocess.PIPE,
            )
        except subprocess.CalledProcessError as exc:
            print(f"cannot read baseline {args.baseline}:{row['original_file']}: {exc.stderr.strip()}", file=sys.stderr)
            return 2
        current_path = root / row["destination_file"]
        if not current_path.is_file():
            mismatches.append(f"missing: {row['destination_file']}")
            continue
        checked += 1
        current_text = current_path.read_text()
        if row["layer"] == "CORE":
            core_checked += 1
        else:
            corpus_checked += 1
        before_plain = sorted(normalized(line, names, shared_lists, section_map) for line in plain_terms(before))
        current_plain = sorted(normalized(line, names, shared_lists, section_map) for line in plain_terms(current_text))
        if (normalized(before, names, shared_lists, section_map) != normalized(current_text, names, shared_lists, section_map)
                or before_plain != current_plain):
            mismatches.append(row["destination_file"])

    if mismatches:
        print(f"numbering prose proof: FAIL ({checked} files checked; {len(mismatches)} mismatch(es))")
        for path in mismatches:
            print(f"  {path}")
        return 1
    print(f"numbering prose proof: PASS ({core_checked} core and {corpus_checked} corpus files match after reference and Trace normalization)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
