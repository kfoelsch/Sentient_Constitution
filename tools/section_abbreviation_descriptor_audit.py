#!/usr/bin/env python3
"""Flag naked implementation-section IDs in prose where descriptors are expected."""

from __future__ import annotations

import argparse
import pathlib
import re
import subprocess
import sys
from dataclasses import dataclass

from corpus_paths import binding_corpus_scope


SECTION_ID_RE = re.compile(
    r"\b(?:CF|CI|CJS|CS)-(?:R\d+|\d+(?:\.\d+)*[A-Z]?)(?:\.\d+)?\b"
)
DESCRIPTOR_AFTER_RE = re.compile(
    r"(?:\s*(?:—|-|:)\s*[^.;,\n]+|\s*\([^)]+\)|\s+\*[^*]+\*)"
)
TRACE_WIDGET_START_RE = re.compile(r"<summary>.*Trace", re.IGNORECASE)


@dataclass(frozen=True)
class Finding:
    file: str
    line: int
    section_id: str
    text: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Repository root.")
    parser.add_argument(
        "--changed-only",
        action="store_true",
        help="Scan added Markdown lines changed relative to HEAD instead of the full scope.",
    )
    parser.add_argument(
        "--paths",
        nargs="*",
        help="Specific repository-relative Markdown paths to scan.",
    )
    parser.add_argument(
        "--include-support-docs",
        action="store_true",
        default=False,
        help="Scan README.md and doc_architecture.md in addition to binding corpus files.",
    )
    return parser.parse_args()


def is_exempt_line(line: str, *, in_trace_widget: bool) -> bool:
    stripped = line.strip()
    if not stripped:
        return True
    if in_trace_widget:
        return True
    if stripped.startswith("#"):
        return True
    if stripped.startswith("|"):
        return True
    if stripped.startswith("<"):
        return True
    if "`INST-PROTO-" in stripped:
        return True
    if stripped.startswith("- `"):
        return True
    if stripped.startswith("- Upstream:") or stripped.startswith("- Downstream:"):
        return True
    if stripped.startswith("- Read with:") or stripped.startswith("**Mandatory read-with:**"):
        return True
    return False


def has_descriptor(text_after_id: str) -> bool:
    text_after_id = text_after_id.lstrip()
    if text_after_id.startswith("**"):
        text_after_id = text_after_id[2:].lstrip()
    return bool(DESCRIPTOR_AFTER_RE.match(text_after_id))


def scan_line(rel_path: str, line_number: int, line: str) -> Finding | None:
    if is_exempt_line(line, in_trace_widget=False):
        return None

    match = SECTION_ID_RE.search(line)
    if not match:
        return None

    if has_descriptor(line[match.end() :]):
        return None

    return Finding(rel_path, line_number, match.group(0), line.strip())


def changed_markdown_findings(root: pathlib.Path, allowed_scope: set[str]) -> list[Finding]:
    result = subprocess.run(
        ["git", "diff", "--unified=0", "--diff-filter=ACM", "HEAD", "--", "*.md"],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    )

    findings: list[Finding] = []
    rel_path: str | None = None
    new_line = 0
    for line in result.stdout.splitlines():
        if line.startswith("+++ b/"):
            rel_path = line.removeprefix("+++ b/")
            continue
        if line.startswith("@@"):
            match = re.search(r"\+(\d+)(?:,\d+)?", line)
            new_line = int(match.group(1)) if match else 0
            continue
        if rel_path is None or rel_path not in allowed_scope:
            continue
        if line.startswith("+") and not line.startswith("+++"):
            finding = scan_line(rel_path, new_line, line[1:])
            if finding:
                findings.append(finding)
            new_line += 1
            continue
        if not line.startswith("-"):
            new_line += 1

    return findings


def scan_file(root: pathlib.Path, rel_path: str) -> list[Finding]:
    path = root / rel_path
    if not path.is_file():
        return []

    findings: list[Finding] = []
    in_trace_widget = False
    for idx, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if TRACE_WIDGET_START_RE.search(line):
            in_trace_widget = True
        if in_trace_widget and "</details>" in line:
            in_trace_widget = False
            continue
        if is_exempt_line(line, in_trace_widget=in_trace_widget):
            continue

        match = SECTION_ID_RE.search(line)
        if not match:
            continue

        if not has_descriptor(line[match.end() :]):
            findings.append(Finding(rel_path, idx, match.group(0), line.strip()))

    return findings


def main() -> int:
    args = parse_args()
    root = pathlib.Path(args.root).resolve()
    full_scope = binding_corpus_scope(root, include_support_docs=args.include_support_docs)
    if args.paths:
        scope = [path for path in args.paths if path in set(full_scope)]
    elif args.changed_only:
        findings = changed_markdown_findings(root, set(full_scope))
        if findings:
            print("Naked implementation-section IDs found:", file=sys.stderr)
            for finding in findings:
                print(
                    f"{finding.file}:{finding.line}: {finding.section_id}: {finding.text}",
                    file=sys.stderr,
                )
            return 1

        print("Section abbreviation descriptor audit passed.")
        return 0
    else:
        scope = full_scope

    findings: list[Finding] = []
    for rel_path in scope:
        findings.extend(scan_file(root, rel_path))

    if findings:
        print("Naked implementation-section IDs found:", file=sys.stderr)
        for finding in findings:
            print(
                f"{finding.file}:{finding.line}: {finding.section_id}: {finding.text}",
                file=sys.stderr,
            )
        return 1

    print("Section abbreviation descriptor audit passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
