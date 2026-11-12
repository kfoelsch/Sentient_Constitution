#!/usr/bin/env python3
"""Audit links from core chapters to their worked-example files (EXAMPLES-LINK-01).

The registry ``tools/architecture/example_files.json`` names each example file and
the core files it illustrates. For every ``core_*`` file the audit requires:

* a core file the registry lists links to the example file in its Trace widget
  and in a closing ``*Worked examples`` line placed directly under the footer rule,
  above Previous/Next (a file with no footer keeps the line at the end of the file);
* the two places agree for every core file, listed or not (a Trace link with no
  closing line, or a closing line with no Trace link, fails);
* each example file links back to every core file it is registered to illustrate;
* every link from any corpus file into an example file lands on a real heading or
  anchor of that file.

The audit reads every corpus file: the ``core_*`` files, the four layer wrappers,
and the ``corpus_*`` subfiles.
"""

from __future__ import annotations

import argparse
import json
import posixpath
import re
import sys
from pathlib import Path

REGISTRY = "tools/architecture/example_files.json"
LINK_RE = re.compile(r"\]\(([^)\s]+?\.md)(?:#[^)\s]*)?\)")
FRAGMENT_RE = re.compile(r"\]\(([^)\s#]+?\.md)#([^)\s]+)\)")
HEADING_RE = re.compile(r"^#{1,6}\s+(.*?)\s*#*\s*$")
ID_RE = re.compile(r'<a id="([^"]+)"')
CLOSING_RE = re.compile(r"^\*Worked examples\b")
CLOSING_WINDOW = 12


def split_widgets(lines: list[str]) -> tuple[list[tuple[int, str]], list[tuple[int, str]]]:
    """Return (trace_lines, outside_lines) as (line number, text) pairs."""
    trace: list[tuple[int, str]] = []
    outside: list[tuple[int, str]] = []
    depth = 0
    is_trace = False
    fence = False
    for number, raw in enumerate(lines, start=1):
        stripped = raw.strip()
        if stripped.startswith("```"):
            fence = not fence
        if fence:
            continue
        if stripped == "<details>":
            depth += 1
            is_trace = False
            continue
        if depth and "<summary" in stripped and ">Trace<" in stripped:
            is_trace = True
        if stripped == "</details>":
            depth = max(0, depth - 1)
            if depth == 0:
                is_trace = False
            continue
        if depth:
            if is_trace:
                trace.append((number, raw))
        else:
            outside.append((number, raw))
    return trace, outside


def targets(text: str, base_dir: str) -> set[str]:
    found = set()
    for match in LINK_RE.finditer(text):
        target = posixpath.normpath(posixpath.join(base_dir, match.group(1)))
        found.add(target)
    return found


def footer_index(lines: list[str]) -> int | None:
    for index, raw in enumerate(lines):
        if raw.startswith("**Previous file:**") or raw.startswith("**Next file:**"):
            return index
    return None


def closing_links(lines: list[str], outside: list[tuple[int, str]]) -> tuple[bool, set[str], bool]:
    """Find the closing '*Worked examples' line.

    Returns (found, link targets, above_rule). With a footer, the line must sit
    directly under the footer rule, above Previous/Next; a line found in the
    paragraphs above the rule is reported through ``above_rule`` and does not
    count. With no footer, the line is read from the end of the file.
    """
    outside_numbers = {number for number, _ in outside}
    footer = footer_index(lines)
    if footer is None:
        end = len(lines)
        for index in range(end - 1, max(0, end - CLOSING_WINDOW - 4) - 1, -1):
            if (index + 1) in outside_numbers and CLOSING_RE.match(lines[index]):
                return True, targets(lines[index], ""), False
        return False, set(), False
    rule = footer - 1
    while rule >= 0 and lines[rule].strip() != "---":
        rule -= 1
    if rule < 0 or footer - rule > 6:
        rule = footer
    for index in range(footer - 1, rule, -1):
        if (index + 1) in outside_numbers and CLOSING_RE.match(lines[index]):
            return True, targets(lines[index], ""), False
    for index in range(rule - 1, max(0, rule - CLOSING_WINDOW - 4) - 1, -1):
        if (index + 1) in outside_numbers and CLOSING_RE.match(lines[index]):
            return False, set(), True
    return False, set(), False


def slug(heading: str) -> str:
    text = re.sub(r"<[^>]+>", "", heading).strip().lower()
    text = re.sub(r"[^\w\s\-]", "", text)
    return re.sub(r"\s", "-", text)


def anchors_of(path: Path) -> set[str]:
    found: set[str] = set()
    for raw in path.read_text(encoding="utf-8").split("\n"):
        match = HEADING_RE.match(raw)
        if match:
            found.add(slug(match.group(1)))
        found.update(ID_RE.findall(raw))
    return found


def corpus_files(root: Path) -> list[Path]:
    paths = list(root.glob("core_*.md")) + list(root.glob("corpus_*.md")) + list(root.glob("corpus_*/*.md"))
    return sorted(paths)


def check_anchors(root: Path, example_paths: list[str]) -> list[str]:
    findings: list[str] = []
    known = {example: anchors_of(root / example) for example in example_paths if (root / example).is_file()}
    for path in corpus_files(root):
        rel = path.relative_to(root).as_posix()
        base = posixpath.dirname(rel)
        for number, raw in enumerate(path.read_text(encoding="utf-8").split("\n"), start=1):
            for match in FRAGMENT_RE.finditer(raw):
                target = posixpath.normpath(posixpath.join(base, match.group(1)))
                if target in known and match.group(2) not in known[target]:
                    findings.append(f"{rel}:{number}: EXAMPLES-LINK-01: #{match.group(2)} is not a heading or anchor in {target}")
    return findings


def audit(root: Path, registry: dict) -> list[str]:
    findings: list[str] = []
    files = registry.get("files", {})
    required: dict[str, set[str]] = {}
    for example, info in files.items():
        if not (root / example).is_file():
            findings.append(f"{REGISTRY}: example file {example} does not exist")
            continue
        text = (root / example).read_text(encoding="utf-8")
        linked = targets(text, posixpath.dirname(example))
        for core_name in info.get("illustrates", []):
            if not (root / core_name).is_file():
                findings.append(f"{REGISTRY}: {example} lists {core_name}, which does not exist")
                continue
            required.setdefault(core_name, set()).add(example)
            if core_name not in linked:
                findings.append(f"{example}: no link back to {core_name}, which it is registered to illustrate")
    for path in sorted(root.glob("core_*.md")):
        name = path.name
        lines = path.read_text(encoding="utf-8").split("\n")
        trace, outside = split_widgets(lines)
        trace_hits = targets("\n".join(text for _, text in trace), "")
        has_closing, closing_hits, above_rule = closing_links(lines, outside)
        if above_rule:
            findings.append(
                f"{name}: EXAMPLES-LINK-01: the '*Worked examples' line sits above the footer rule; "
                "move it directly under the rule, above Previous/Next"
            )
        for example in files:
            in_trace = example in trace_hits
            in_closing = example in closing_hits
            want = example in required.get(name, set())
            short = posixpath.basename(example)
            if want and not in_trace:
                findings.append(f"{name}: EXAMPLES-LINK-01: Trace widget needs a link to {short}")
            if want and not in_closing:
                findings.append(
                    f"{name}: EXAMPLES-LINK-01: needs a closing '*Worked examples' line linking {short}, directly under the footer rule"
                )
            if in_trace and not in_closing and not want:
                findings.append(f"{name}: EXAMPLES-LINK-01: Trace links {short} but there is no closing '*Worked examples' line")
            if in_closing and not in_trace and not want:
                findings.append(f"{name}: EXAMPLES-LINK-01: closing line links {short} but the Trace widget does not")
        if has_closing and not closing_hits & set(files):
            findings.append(f"{name}: EXAMPLES-LINK-01: the '*Worked examples' line links no registered example file")
    findings.extend(check_anchors(root, list(files)))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Repository root (default: .).")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    registry = json.loads((root / REGISTRY).read_text(encoding="utf-8"))
    findings = audit(root, registry)
    if findings:
        print("FAIL: worked-example links")
        for finding in findings:
            print(f"  {finding}")
        return 1
    count = sum(len(info.get("illustrates", [])) for info in registry.get("files", {}).values())
    print(f"PASS: worked-example links: {count} core chapters link their example files in Trace and at the close.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
