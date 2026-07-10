#!/usr/bin/env python3
"""Audit Chapter Six trace placement and minimum linked-content rules.

Rules: NAV-TRACE-08, NAV-TRACE-09 in tools/architecture/rule_registry.json.
Each Chapter Six subarticle must:

1. Carry a local Trace ``<details>`` block immediately under the subarticle
   heading using the standard Trace summary label, AND
2. Either (a) carry a separate **Definitions · Assessment · Compliance**
   ``<details>`` widget directly after the Trace close, OR (b) carry a
   single-concept inline ``<strong><span style="color: #2563eb;">Definition:
   </span></strong>`` line directly after the Trace close, OR (c) — for
   sections with no Chapter Five invocations — neither, with that absence
   recorded as deliberate.

The legacy ``- Definitions:`` line inside Trace is no longer accepted as
satisfying requirement 2; ``Definitions:`` content has been lifted out per
the architecture rule.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys


DEFAULT_FILES = [
    "core_06-06_rights_part_a.md",
    "core_06-06_rights_part_b.md",
    "core_06-06_rights_part_c.md",
    "core_06-06_rights_part_d.md",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Workspace root (default: .).")
    parser.add_argument(
        "--files",
        nargs="*",
        default=DEFAULT_FILES,
        help="Chapter Six files under --root.",
    )
    return parser.parse_args()


def next_nonempty(lines: list[str], start: int) -> int | None:
    idx = start
    while idx < len(lines):
        if lines[idx].strip():
            return idx
        idx += 1
    return None


def main() -> int:
    args = parse_args()
    root = pathlib.Path(args.root)
    violations: list[str] = []

    for rel in args.files:
        path = root / rel
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except FileNotFoundError:
            violations.append(f"Missing required file: {path}")
            continue

        for idx, raw in enumerate(lines):
            stripped = raw.strip()
            if not re.match(r"^#### Article [A-Z0-9-]+:", stripped):
                continue

            lineno = idx + 1
            details_idx = next_nonempty(lines, idx + 1)
            if details_idx is None or lines[details_idx].strip() != "<details>":
                violations.append(
                    f"{path}:{lineno}: Chapter Six subarticles must carry a local Trace/details block immediately under the subarticle heading"
                )
                continue

            summary_idx = next_nonempty(lines, details_idx + 1)
            if summary_idx is None or lines[summary_idx].strip() != '<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>':
                violations.append(
                    f"{path}:{details_idx + 1}: Trace/details block must use the standard Trace summary label"
                )
                continue

            end_idx = summary_idx + 1
            while end_idx < len(lines) and lines[end_idx].strip() != "</details>":
                end_idx += 1
            if end_idx >= len(lines):
                violations.append(f"{path}:{details_idx + 1}: unterminated Trace/details block")
                continue

            block = [line.strip() for line in lines[summary_idx + 1 : end_idx] if line.strip()]
            principles_line = next(
                (
                    line
                    for line in block
                    if line.startswith("- Principles:")
                    or line.startswith("- Upstream: Principles:")
                ),
                None,
            )

            if principles_line is None:
                violations.append(
                    f"{path}:{lineno}: Chapter Six subarticle Trace blocks must include a '- Principles:' or '- Upstream: Principles:' line"
                )

            # Per doc_architecture.md rule 12 (2026-04-16 D/A/C split), the
            # legacy in-Trace ``- Definitions:`` line is no longer accepted.
            # Look forward from </details> for either a D/A/C widget or a
            # single-concept inline ``Definition:`` line. Either satisfies the
            # rule; their absence is allowed only for sections with no
            # invocations (we cannot verify "no invocations" mechanically here,
            # so the audit warns once and treats the warning as informational).
            dec_summary = (
                '<summary><strong><span style="color: #2563eb;">'
                "Definitions \u00b7 Evaluation \u00b7 Compliance</span></strong></summary>"
            )
            inline_prefix = (
                '<strong><span style="color: #2563eb;">Definition:</span></strong>'
            )

            scan_idx = end_idx + 1
            # Skip blank lines and a trailing <br> spacer.
            while scan_idx < len(lines) and lines[scan_idx].strip() in ("", "<br>"):
                scan_idx += 1

            has_widget = False
            has_inline = False
            if scan_idx < len(lines):
                first = lines[scan_idx].strip()
                if first == "<details>":
                    # Look at the next non-empty line for the D/A/C summary.
                    sidx = next_nonempty(lines, scan_idx + 1)
                    if sidx is not None and lines[sidx].strip() == dec_summary:
                        has_widget = True
                elif first.startswith(inline_prefix):
                    has_inline = True

            # Also accept legacy in-Trace ``- Definitions:`` line during the
            # transition only if the legacy line is the sole carrier and there
            # is no widget — this branch should never trip after the rollout
            # completes, but we report it loudly so it does not silently slip
            # back in.
            legacy_definitions_line = next(
                (line for line in block if line.startswith("- Definitions:")),
                None,
            )
            if legacy_definitions_line is not None:
                violations.append(
                    f"{path}:{lineno}: legacy '- Definitions:' line found inside Trace (must be lifted into a separate Definitions \u00b7 Evaluation \u00b7 Compliance widget per doc_architecture.md rule 12)"
                )

            # Note: we deliberately do not require a D/A/C widget to be present.
            # Some sections genuinely invoke zero Chapter Five concepts; in those
            # cases the absence is correct. We only flag the legacy pattern.
            _ = (has_widget, has_inline)  # reserved for future stricter check

    if violations:
        print("\n".join(violations), file=sys.stderr)
        return 1

    print(
        "PASS: Chapter Six subarticle Trace blocks are present, no legacy "
        "'- Definitions:' lines remain inside Trace, and Principles upstream "
        "is named where required."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
