#!/usr/bin/env python3
"""Audit the Implementation widget and inline line (NAV-IMPL-WIDGET-01).

``tools/architecture/implementation_map.json`` lists units (a core section or Article) and the
implementation files that own their detail. For each unit the audit requires:

* exactly one owner: a single inline ``Implementation:`` line, no widget;
* two or more owners: a collapsed ``Implementation (non-operative)`` widget, one bullet per
  owner in registry order, followed by ``<br>``; no ``<br>`` sits between it and the widgets above
  it (NAV-DAC-12-SPACER: one ``<br>`` after the last widget of a stack);
* the widget or line sits last in the unit's opening stack (after Trace and D/A/C), before
  the first prose;
* every row is ``[Title](path#anchor)`` with the owner file's own title and a live anchor;
* an owner's ``Core home`` is the unit's chapter, unless the registry gives a ``why``;
* no Implementation widget or line appears anywhere that the registry does not list.

Coverage (implementation files in no unit) is reported, not gated, while the rollout is partial.
``--write`` inserts the block for a unit that has none. The audit reads every corpus file.
"""

from __future__ import annotations

import argparse
import glob
import json
import posixpath
import re
import sys
from pathlib import Path

REGISTRY = "tools/architecture/implementation_map.json"
SUMMARY = "Implementation (non-operative)"
SUMMARY_LINE = f'<summary><strong><span style="color: #2563eb;">{SUMMARY}</span></strong></summary>'
ID_RE = re.compile(r"^(CJS|CS|CI|CF)-(\d+)\.(\d+)$")
HEADING_RE = re.compile(r"^#{1,6}\s+(.*?)\s*$")
ROW_RE = re.compile(r"^\[(?P<title>.+)\]\((?P<path>[^)#\s]+)#(?P<anchor>[^)\s]+)\)$")
ENTRY_RE = re.compile(r"\[[^\]]+\]\([^)\s]+\)")
ANCHOR_ID_RE = re.compile(r'<a id="([^"]+)"')


def slug(heading: str) -> str:
    text = re.sub(r"<[^>]+>", "", heading).strip().lower()
    text = re.sub(r"[^\w\s\-]", "", text)
    return re.sub(r"\s", "-", text)


def owner_info(root: Path, ident: str) -> dict | None:
    match = ID_RE.match(ident)
    if not match:
        return None
    prefix, chapter, section = match.group(1).lower(), int(match.group(2)), match.group(3)
    found = sorted(glob.glob(str(root / f"corpus_*/{prefix}_{chapter:02d}.{section}_*.md")))
    if len(found) != 1:
        return None
    path = Path(found[0])
    text = path.read_text(encoding="utf-8")
    heading = next((line for line in text.split("\n") if HEADING_RE.match(line)), "")
    h1 = HEADING_RE.match(heading).group(1) if heading else ""
    title = h1.split(":", 1)[1].strip() if re.match(r"^(CJS|CS|CI|CF)-\d+\.\d+:", h1) else h1
    anchors = {slug(m.group(1)) for line in text.split("\n") for m in [HEADING_RE.match(line)] if m}
    anchors |= set(ANCHOR_ID_RE.findall(text))
    home = re.search(r"^Core home: (\d+)", text, re.MULTILINE)
    return {
        "path": path.relative_to(root).as_posix(),
        "title": title,
        "anchor": slug(h1),
        "anchors": anchors,
        "home": home.group(1) if home else None,
    }


def render(infos: list[dict]) -> list[str]:
    entries = [f"[{info['title']}]({info['path']}#{info['anchor']})" for info in infos]
    if len(entries) == 1:
        return [f"Implementation: {entries[0]}.", ""]
    return ["<details>", SUMMARY_LINE, ""] + [f"- {entry}" for entry in entries] + ["", "</details>", "<br>", ""]


def opening_stack(lines: list[str], heading_index: int) -> tuple[list[tuple[int, int]], int]:
    """Return the widgets of the opening stack as (start, end) and the index after the stack."""
    widgets: list[tuple[int, int]] = []
    i = heading_index + 1
    after = i
    while i < len(lines):
        stripped = lines[i].strip()
        if stripped == "" or stripped == "<br>" or re.match(r'<a id="[^"]*"></a>$', stripped):
            i += 1
            after = i
            continue
        if stripped == "<details>":
            end = next((k for k in range(i, len(lines)) if lines[k].strip() == "</details>"), None)
            if end is None:
                break
            widgets.append((i, end))
            i = end + 1
            after = i
            continue
        break
    return widgets, after


def corpus_files(root: Path) -> list[Path]:
    return sorted(list(root.glob("core_*.md")) + list(root.glob("corpus_*.md")) + list(root.glob("corpus_*/*.md")))


def find_heading(lines: list[str], heading: str) -> list[int]:
    return [i for i, line in enumerate(lines) if (m := HEADING_RE.match(line)) and m.group(1) == heading]


def audit(root: Path, registry: dict, write: bool = False) -> tuple[list[str], dict]:
    findings: list[str] = []
    chapters = json.loads((root / "tools/architecture/chapter_numbers.json").read_text(encoding="utf-8"))["chapters"]
    home_of = {c["destination_file"]: c["core_home"] for c in chapters if c.get("layer") == "CORE"}
    claimed: dict[str, set[int]] = {}
    covered: set[str] = set()
    for unit in registry.get("units", []):
        name, heading, owners = unit["file"], unit["heading"], unit["owners"]
        path = root / name
        if not path.is_file():
            findings.append(f"{REGISTRY}: {name} does not exist")
            continue
        infos = []
        for ident in owners:
            info = owner_info(root, ident)
            if info is None:
                findings.append(f"{REGISTRY}: {name} / {heading}: owner {ident} is not one implementation file")
                continue
            if info["home"] != home_of.get(name) and not unit.get("why"):
                findings.append(f"{name}: {heading}: owner {ident} has Core home {info['home']}, the unit is in chapter {home_of.get(name)}; give a 'why' or remove it")
            covered.add(info["path"])
            infos.append(info)
        if len(infos) != len(owners):
            continue
        lines = path.read_text(encoding="utf-8").split("\n")
        hits = find_heading(lines, heading)
        if len(hits) != 1:
            findings.append(f"{name}: heading '{heading}' found {len(hits)} times, expected once")
            continue
        widgets, after = opening_stack(lines, hits[0])
        impl_widgets = [w for w in widgets if lines[w[0] + 1].strip() == SUMMARY_LINE]
        inline = lines[after].startswith("Implementation: ") if after < len(lines) else False
        label = f"{name}: {heading}"
        if write and not impl_widgets and not inline:
            if len(infos) > 1 and widgets:
                # One <br> only after the last widget: the new widget takes the stack's <br>.
                last_end = widgets[-1][1]
                tail = [x for x in lines[last_end + 1 : after] if x.strip() != "<br>"]
                while tail and not tail[0].strip():
                    tail.pop(0)
                lines[last_end + 1 : after] = [""] + render(infos) + tail
            else:
                lines[after:after] = render(infos)
            path.write_text("\n".join(lines), encoding="utf-8")
            widgets, after = opening_stack(lines, hits[0])
            impl_widgets = [w for w in widgets if lines[w[0] + 1].strip() == SUMMARY_LINE]
            inline = lines[after].startswith("Implementation: ")
        one = len(infos) == 1
        if one:
            if impl_widgets:
                findings.append(f"{label}: NAV-IMPL-WIDGET-01: one owner takes an inline 'Implementation:' line, not a widget")
            if not inline:
                findings.append(f"{label}: NAV-IMPL-WIDGET-01: missing the inline 'Implementation:' line after the opening widgets")
            else:
                claimed.setdefault(name, set()).add(after)
                entries = ENTRY_RE.findall(lines[after])
                findings.extend(check_rows(label, entries, infos))
        else:
            if inline:
                findings.append(f"{label}: NAV-IMPL-WIDGET-01: two or more owners take a widget, not an inline line")
            if len(impl_widgets) != 1:
                findings.append(f"{label}: NAV-IMPL-WIDGET-01: needs one 'Implementation (non-operative)' widget, found {len(impl_widgets)}")
            else:
                start, end = impl_widgets[0]
                claimed.setdefault(name, set()).add(start)
                if widgets[-1] != impl_widgets[0]:
                    findings.append(f"{label}: NAV-IMPL-WIDGET-01: the Implementation widget must be last in the opening stack, after Trace and D/A/C")
                rows = [line[2:] for line in lines[start + 2 : end] if line.startswith("- ")]
                findings.extend(check_rows(label, rows, infos))
                follow = next((lines[k].strip() for k in range(end + 1, len(lines)) if lines[k].strip()), "")
                if follow != "<br>":
                    findings.append(f"{label}: NAV-IMPL-WIDGET-01: a <br> must follow the Implementation widget, as it follows D/A/C")
    for path in corpus_files(root):
        rel = path.relative_to(root).as_posix()
        text = path.read_text(encoding="utf-8").split("\n")
        for number, line in enumerate(text):
            is_widget = line.strip() == SUMMARY_LINE
            is_inline = line.startswith("Implementation: ")
            if not (is_widget or is_inline):
                continue
            key = number - 1 if is_widget else number
            if key not in claimed.get(rel, set()):
                findings.append(f"{rel}:{number + 1}: NAV-IMPL-WIDGET-01: Implementation widget or line is not in {REGISTRY}")
    return findings, {"covered": sorted(covered)}


def check_rows(label: str, rows: list[str], infos: list[dict]) -> list[str]:
    findings: list[str] = []
    if len(rows) != len(infos):
        return [f"{label}: NAV-IMPL-WIDGET-01: expected {len(infos)} implementation entries, found {len(rows)}"]
    for row, info in zip(rows, infos):
        match = ROW_RE.match(row.strip())
        if not match:
            findings.append(f"{label}: NAV-IMPL-WIDGET-01: entry is not '[Title](path#anchor)': {row[:80]}")
            continue
        if match.group("path") != info["path"]:
            findings.append(f"{label}: NAV-IMPL-WIDGET-01: entry order or target differs from the registry at {info['path']}")
        elif match.group("title") != info["title"]:
            findings.append(f"{label}: NAV-IMPL-WIDGET-01: title '{match.group('title')}' is not the file's title '{info['title']}'")
        elif match.group("anchor") not in info["anchors"]:
            findings.append(f"{label}: NAV-IMPL-WIDGET-01: #{match.group('anchor')} is not a heading or anchor in {info['path']}")
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Repository root (default: .).")
    parser.add_argument("--write", action="store_true", help="Insert the block for a unit that has none.")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    registry = json.loads((root / REGISTRY).read_text(encoding="utf-8"))
    findings, info = audit(root, registry, write=args.write)
    if findings:
        print("FAIL: implementation widgets")
        for finding in findings:
            print(f"  {finding}")
        return 1
    print(f"PASS: implementation widgets: {len(registry['units'])} units match the registry; {len(info['covered'])} implementation files listed (coverage is reported, not gated).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
