#!/usr/bin/env python3
"""Audit Chapter Five entry-title and trace-separator formatting.

Also enforces the **reference-side no-redundant-`(Constitutional)`-suffix rule**
(see ``doc_architecture.md`` §"Order and alphabetization (Chapter Five)"
Section 1, *Reference-side rule*) across the binding corpus, architectural
maps, and active implementation / planning notes. The rule: visible prose
must not append `` (Constitutional)`` to a Chapter Five defined-term
reference. URL anchor fragments (``#…-constitutional``) and HTML anchor tags
(``<a id="…-constitutional"></a>``) are link-target identifiers and remain
untouched. ``(Constitutional Constraint)`` is a distinct parenthetical that
is part of the canonical title and is preserved verbatim. Backtick-quoted
meta-text that names the literal suffix (e.g. the rule's own
```` `(Constitutional)` ````) is preserved as meta-reference.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

_TOOLS = pathlib.Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from ch5_paths import CH5_ALL

from corpus_paths import binding_corpus_scope


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Workspace root (default: .).")
    parser.add_argument(
        "--file",
        default="core_05_definitions_home.md",
        help="Chapter Five Markdown file under --root.",
    )
    return parser.parse_args()


# ``" (Constitutional)"`` as a standalone parenthetical suffix. The closing
# ``\)`` rules out ``(Constitutional Constraint)`` automatically.
_REDUNDANT_SUFFIX_RE = re.compile(r" \(Constitutional\)")

# Substrings that mark a line as meta-text about the literal suffix itself.
# Such lines are legitimately allowed to name ``(Constitutional)``.
_REDUNDANT_SUFFIX_META_MARKERS = ("`(Constitutional)`",)


def audit_redundant_suffix(root: pathlib.Path) -> list[str]:
    violations: list[str] = []
    extra_scope = [
        "archive/ARCHITECTURE_PRIMER_ARCHIVED_2026-05-08.md",
        "archive/ARCHITECTURE_ADOPTION_APPENDIX_ARCHIVED_2026-05-08.md",
        "archive/TRUST_UNDER_ATTACK_DELTA_REPORT_ARCHIVED_2026-05-01.md",
        "implementation/TRANSITION_FRAMEWORK_2026.md",
    ]
    for rel in [*binding_corpus_scope(root, include_support_docs=True), *extra_scope]:
        path = root / rel
        if not path.exists():
            continue
        for lineno, raw in enumerate(
            path.read_text(encoding="utf-8").splitlines(), start=1
        ):
            if any(marker in raw for marker in _REDUNDANT_SUFFIX_META_MARKERS):
                continue
            if _REDUNDANT_SUFFIX_RE.search(raw):
                violations.append(
                    f"{path}:{lineno}: redundant ' (Constitutional)' suffix in "
                    f"prose reference (see doc_architecture.md §'Order and "
                    f"alphabetization (Chapter Five)' Section 1 — "
                    f"Reference-side rule): {raw.rstrip()}"
                )
    return violations


def prev_significant(lines: list[str], start: int) -> int | None:
    idx = start
    while idx >= 0:
        line = lines[idx].strip()
        if line and not line.startswith("<a id="):
            return idx
        idx -= 1
    return None


def next_nonempty(lines: list[str], start: int) -> int | None:
    idx = start
    while idx < len(lines):
        if lines[idx].strip():
            return idx
        idx += 1
    return None


def title_for_details(lines: list[str], details_idx: int) -> tuple[int, str] | None:
    """Find the heading that owns a Trace ``<details>`` block.

    Walks back past spacers, horizontal rules, and closed non-entry widgets
    (corpus placement / reader guidance) so aim- and leg-head files that place
    Trace after those widgets still resolve to the ``#`` / ``####`` title.
    """
    nonentry_open, nonentry_close = nonentry_widget_detail_lines(lines)
    idx = details_idx - 1
    while idx >= 0:
        stripped = lines[idx].strip()
        if not stripped or stripped in {"---", "<br>"} or stripped.startswith("<a id="):
            idx -= 1
            continue
        if idx in nonentry_close:
            # Jump to the matching non-entry ``<details>`` open, then keep walking.
            open_idx = next((o for o in sorted(nonentry_open) if o < idx), None)
            if open_idx is None:
                return None
            idx = open_idx - 1
            continue
        if stripped.startswith("#"):
            return idx, lines[idx].rstrip()
        # Plain-text titles are legacy; still accept when immediately above Trace.
        return idx, lines[idx].rstrip()
    return None


# File-top orientation widgets are not Trace / definition entries; the
# separator-above-title and post-block ``<br>`` spacer rules below apply to
# Trace blocks, not these. File-top spacing is governed by
# ``file_top_placement_audit`` and ``nav_widget_spacer_audit`` instead.
_NONENTRY_WIDGET_MARKERS = (
    "Corpus placement (non-operative):",
    "Reader guidance (non-operative):",
)


def nonentry_widget_detail_lines(lines: list[str]) -> tuple[set[int], set[int]]:
    """Line indices of ``<details>``/``</details>`` for non-entry widgets."""
    opens: set[int] = set()
    closes: set[int] = set()
    for idx, raw in enumerate(lines):
        if raw.strip() != "<details>":
            continue
        summary_idx = idx + 1
        if summary_idx >= len(lines):
            continue
        if not any(marker in lines[summary_idx] for marker in _NONENTRY_WIDGET_MARKERS):
            continue
        opens.add(idx)
        depth = 1
        j = idx + 1
        while j < len(lines) and depth:
            stripped = lines[j].strip()
            if stripped == "<details>":
                depth += 1
            elif stripped == "</details>":
                depth -= 1
                if depth == 0:
                    closes.add(j)
            j += 1
    return opens, closes


def iter_titles(lines: list[str]) -> list[tuple[int, str, bool]]:
    titles: list[tuple[int, str, bool]] = []
    for idx, raw in enumerate(lines):
        line = raw.rstrip()
        stripped = line.strip()
        if stripped.startswith("#### ") or stripped.startswith("##### "):
            titles.append((idx, stripped, True))
            continue
        if stripped.startswith("<a id="):
            next_idx = next_nonempty(lines, idx + 1)
            if next_idx is None:
                continue
            candidate = lines[next_idx].strip()
            if candidate and not candidate.startswith(("-", "<", "#")):
                after_idx = next_nonempty(lines, next_idx + 1)
                if after_idx is not None and (
                    lines[after_idx].lstrip().startswith("- O:")
                    or lines[after_idx].strip() == "<details>"
                ):
                    titles.append((next_idx, candidate, False))
        if candidate := stripped:
            if candidate.startswith(("-", "<", "#")) or candidate == "---":
                continue
            after_idx = next_nonempty(lines, idx + 1)
            if after_idx is None:
                continue
            after = lines[after_idx].strip()
            if after.startswith("- O:") or after.startswith("- E:") or after.startswith("- C:"):
                titles.append((idx, candidate, False))
    seen: set[tuple[int, str, bool]] = set()
    deduped: list[tuple[int, str, bool]] = []
    for item in titles:
        if item not in seen:
            seen.add(item)
            deduped.append(item)
    return deduped


def audit_one_ch5_file(path: pathlib.Path, violations: list[str]) -> None:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except FileNotFoundError:
        violations.append(f"Missing required file: {path}")
        return

    for idx, title, is_heading in iter_titles(lines):
        lineno = idx + 1
        if "(Constitutional)" in title:
            violations.append(
                f"{path}:{lineno}: visible Chapter Five entry titles must not use '(Constitutional)': {title}"
            )
        if not is_heading:
            violations.append(
                f"{path}:{lineno}: Chapter Five entry titles that own O/E/C content must use an explicit Markdown heading so following bullets render consistently: {title}"
            )

    for idx in range(len(lines) - 1):
        current = lines[idx].strip()
        following = lines[idx + 1].lstrip()
        if not following.startswith("- O:"):
            continue
        if not current:
            continue
        if current.startswith(("#", "-", "<", ">")) or current == "---":
            continue
        violations.append(
            f"{path}:{idx + 2}: Chapter Five entry titles that use plain-text labels must keep a blank line before '- O:' so bullets render consistently: {current}"
        )

    for idx in range(len(lines) - 1):
        current = lines[idx].strip()
        following = lines[idx + 1].strip()
        if not current.startswith(("#### ", "##### ")):
            continue
        if following != "<details>":
            continue
        violations.append(
            f"{path}:{idx + 2}: trace-bearing Chapter Five headings must keep a blank line between the heading and '<details>' so the Trace block renders with consistent spacing"
        )

    nonentry_open, nonentry_close = nonentry_widget_detail_lines(lines)

    for idx, raw in enumerate(lines):
        if raw.strip() != "<details>":
            continue
        if idx in nonentry_open:
            continue
        title_info = title_for_details(lines, idx)
        if title_info is None:
            violations.append(
                f"{path}:{idx + 1}: unable to find owning title line for Trace/details block"
            )
            continue
        title_idx, title = title_info
        before_title_idx = prev_significant(lines, title_idx - 1)
        if before_title_idx is None:
            continue
        before_title = lines[before_title_idx].strip()
        if before_title == "---":
            continue
        if title.startswith("#### ") and before_title.startswith("### "):
            continue
        violations.append(
            f"{path}:{title_idx + 1}: trace-bearing Chapter Five entry should use a separator line above its title for local consistency: {title}"
        )

    for idx, raw in enumerate(lines):
        if raw.strip() != "</details>":
            continue
        if idx in nonentry_close:
            continue
        if idx + 3 >= len(lines):
            violations.append(
                f"{path}:{idx + 1}: trace/details block must be followed by a single visible spacer before the next content line"
            )
            continue
        if lines[idx + 1].strip():
            violations.append(
                f"{path}:{idx + 2}: trace/details block must be followed by a blank line before the spacer"
            )
            continue
        if lines[idx + 2].strip() != "<br>":
            violations.append(
                f"{path}:{idx + 3}: trace/details block must use exactly one '<br>' as the post-block spacer"
            )
            continue
        if lines[idx + 3].strip():
            violations.append(
                f"{path}:{idx + 4}: trace/details block must keep one blank line after the spacer before the next content line"
            )

    for idx in range(len(lines) - 3):
        if lines[idx].strip() != "---":
            continue
        if lines[idx + 1].strip():
            continue
        if lines[idx + 2].strip() != "---":
            continue
        next_line = lines[idx + 3].strip()
        if next_line.startswith(("<a id=", "#### ", "##### ")):
            violations.append(
                f"{path}:{idx + 3}: Chapter Five entries must not use duplicated separator lines between adjacent entries"
            )

def main() -> int:
    args = parse_args()
    root = pathlib.Path(args.root)
    violations: list[str] = []

    if args.file == "core_05_definitions_home.md" and all(
        (root / n).exists() for n in CH5_ALL
    ):
        for name in CH5_ALL:
            audit_one_ch5_file(root / name, violations)
    else:
        audit_one_ch5_file(root / args.file, violations)

    violations.extend(audit_redundant_suffix(root))

    if violations:
        print("\n".join(violations), file=sys.stderr)
        return 1

    print(
        "PASS: Chapter Five entry titles and trace separators follow the local "
        "format rule; no redundant '(Constitutional)' suffix in corpus "
        "references."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
