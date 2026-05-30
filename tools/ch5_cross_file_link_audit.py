#!/usr/bin/env python3
"""Cross-file Markdown link resolution for Chapter Five fragment targets.

Validates every ``](core_05-05_definitions_*.md#…)`` link in the corpus scope
against the same merged anchor model as ``ch5_dec_widget_audit`` (explicit
``<a id>`` tags, heading auto-slugs, and Part A unified A–Z directory slugs).

This closes the gap left by ``reference_audit.py`` (Article Roman numerals only)
and complements ``ch5_dec_widget_audit.py`` (D/E/C widget rows only): inline
prose links, Trace blocks, and cluster cross-links are checked here.

Run: ``make ch5-cross-file-link-audit`` or ``python3 tools/ch5_cross_file_link_audit.py --root .``
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from ch5_dec_widget_audit import (  # noqa: E402
    anchor_resolves_for_widget,
    collect_all_ch5_anchors,
)
from ch5_paths import CH5_ALL  # noqa: E402
from corpus_paths import binding_corpus_scope  # noqa: E402

CH5_FILE_PATTERN = re.compile(
    r"\]\((core_05-05_definitions_(?:a_independent|b_semi_independent|c_dependent_clusters)\.md)#([^)]+)\)"
)

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", default=".", help="Repository root.")
    p.add_argument(
        "--file",
        action="append",
        dest="files",
        metavar="PATH",
        help="Restrict audit to this file (repeatable). Relative to --root.",
    )
    return p.parse_args()


def audit_file(path: Path, anchors: set[str]) -> list[str]:
    violations: list[str] = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        return [f"{path}: error reading file: {exc}"]
    for lineno, line in enumerate(lines, start=1):
        for m in CH5_FILE_PATTERN.finditer(line):
            slug = m.group(2)
            if not anchor_resolves_for_widget(slug, anchors):
                violations.append(
                    f"{path}:{lineno}: Chapter Five link #{slug} does not resolve "
                    f"({m.group(0)})"
                )
    return violations


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    scope = args.files if args.files else binding_corpus_scope(root)

    missing_part = [name for name in CH5_ALL if not (root / name).is_file()]
    if missing_part:
        print(
            f"Missing Chapter Five file(s): {', '.join(missing_part)}",
            file=sys.stderr,
        )
        return 2

    anchors = collect_all_ch5_anchors(root)
    violations: list[str] = []
    for rel in scope:
        fp = root / rel
        if not fp.is_file():
            continue
        violations.extend(audit_file(fp, anchors))

    if violations:
        for v in violations:
            print(v, file=sys.stderr)
        print(
            f"\nFAIL: {len(violations)} unresolved Chapter Five Markdown link(s).",
            file=sys.stderr,
        )
        return 1
    print(
        "PASS: every `](core_05-05_definitions_*.md#…)` link in scope resolves "
        "to a live Chapter Five anchor (merged model)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
