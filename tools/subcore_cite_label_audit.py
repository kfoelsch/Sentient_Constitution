#!/usr/bin/env python3
"""Require every cite into a subcore file to say "Subcore N-X".

Readers tell the fixed guarantees of the core from the standardized detail of
the subcore by the cite itself: core text is cited as "Chapter Ten §3.1 …",
subcore text as "Subcore 10-A §3.8 …". The two layers have the same force; the
label shows the role, not the weight.

A Markdown link whose target is a subcore file outside Chapter Three passes
when its link text starts with "Subcore N-X" (or "Subcores"), optionally in
bold, or when the same line names "Subcore N-X" for that file elsewhere, so
that term links such as ``[**Type I**](subcore_04.050_data_types.md#…)`` pass
beside a "(Subcore 4-A)" label. Chapter Three's definition files (Subcores 3-A
to 3-O) are out of scope: they are cited by the defined term. Footer navigation
lines (``**Previous file:**``, ``**Next file:**``), headings, and fenced code
are out of scope, as is a link from a file to itself.

Rule ID: SUBCORE-CITE-01
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from corpus_paths import binding_corpus_scope  # noqa: E402

LINK_RE = re.compile(r"\[((?:[^\[\]]|\[[^\]]*\])*)\]\(([^)\s]+)\)")
TARGET_RE = re.compile(r"(?:^|/)(subcore_(\d\d)\.\d+_[a-z0-9_]+\.md)(?:#|$)")
SKIP_LINE_RE = re.compile(r"^\s*(\*\*(Previous|Next) file:\*\*|#{1,6} )")


def display_labels(root: Path) -> dict[str, str]:
    data = json.loads((root / "tools/architecture/chapter_numbers.json").read_text(encoding="utf-8"))
    rows = data if isinstance(data, list) else next(v for v in data.values() if isinstance(v, list))
    out: dict[str, str] = {}
    for row in rows:
        if not isinstance(row, dict) or row.get("layer") != "SUBCORE":
            continue
        dest = row.get("destination_file", "")
        disp = row.get("display_id", "")
        if dest and disp.startswith("S"):
            out[Path(dest).name] = "Subcore " + disp[1:]
    return out


def _plain(text: str) -> str:
    return re.sub(r"[*_`]", "", text).strip()


def scan_text(rel: str, text: str, labels: dict[str, str]) -> list[str]:
    findings: list[str] = []
    in_fence = False
    own = Path(rel).name
    for lineno, line in enumerate(text.splitlines(), 1):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence or SKIP_LINE_RE.match(line):
            continue
        plain_line = _plain(line)
        for m in LINK_RE.finditer(line):
            tm = TARGET_RE.search(m.group(2))
            if not tm:
                continue
            fname, chap = tm.group(1), tm.group(2)
            if chap == "03" or fname == own:
                continue
            label = labels.get(fname)
            if label is None:
                findings.append(f"{rel}:{lineno}: SUBCORE-CITE-01: link to {fname}, which has no subcore display label in chapter_numbers.json")
                continue
            text_plain = _plain(m.group(1))
            if text_plain.startswith(label) or text_plain.startswith("Subcores "):
                continue
            if re.search(re.escape(label) + r"(?![0-9A-Za-z])", plain_line):
                continue
            findings.append(
                f"{rel}:{lineno}: SUBCORE-CITE-01: link [{m.group(1)[:60]}] into {fname} does not say '{label}': "
                f"start the link text with '{label}', or name '{label}' on the same line"
            )
    return findings


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--root", default=".")
    args = ap.parse_args(argv)
    root = Path(args.root).resolve()
    labels = display_labels(root)
    findings: list[str] = []
    for rel in binding_corpus_scope(root):
        path = root / rel
        if path.suffix != ".md" or not path.exists():
            continue
        findings.extend(scan_text(rel, path.read_text(encoding="utf-8"), labels))
    if findings:
        print(f"FAIL: SUBCORE-CITE-01 — {len(findings)} subcore cite(s) without a 'Subcore N-X' label.")
        for f in findings:
            print("  " + f)
        return 2
    print("PASS: SUBCORE-CITE-01 — every cite into a subcore file outside Chapter Three says 'Subcore N-X'.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
