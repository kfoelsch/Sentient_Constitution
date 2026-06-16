#!/usr/bin/env python3
"""Structural Markdown checks on Sentient Constitution corpus files.

Catches recurring editorial failures (e.g. flattened nested list items) that do
not affect reference_audit but break reader scanability and intended hierarchy.

Also enforces a blank line before ``---`` horizontal rules (CommonMark / Cursor
preview): a ``---`` line immediately under non-empty text is parsed as a Setext
heading underline, not a thematic break.
"""

from __future__ import annotations

import argparse
import pathlib
import sys

from corpus_paths import binding_corpus_scope


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        default=".",
        help="Workspace root path. Defaults to current directory.",
    )
    parser.add_argument(
        "--file",
        default="core_02-04_definition_mechanics.md",
        help="Corpus Markdown file for Ch 3 / Ch 4 definition-structure slices (under --root).",
    )
    parser.add_argument(
        "--thematic-break-files",
        default=None,
        help=(
            "Comma-separated Markdown paths (under --root) for horizontal-rule "
            "blank-line audit. Default: core + corpus annexes + key support docs."
        ),
    )
    return parser.parse_args()


def load_text(path: pathlib.Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise SystemExit(f"Missing required file: {path}")


def slice_between(text: str, start_line: str, end_line: str) -> str | None:
    """Inclusive start, exclusive end; both must be line prefixes at line start."""
    lines = text.splitlines()
    start_i = end_i = None
    for i, line in enumerate(lines):
        if line.startswith(start_line):
            start_i = i
            break
    if start_i is None:
        return None
    for j in range(start_i + 1, len(lines)):
        if lines[j].startswith(end_line):
            end_i = j
            break
    if end_i is None:
        return None
    return "\n".join(lines[start_i:end_i])


def next_non_empty(lines: list[str], start: int) -> int:
    j = start
    while j < len(lines) and not lines[j].strip():
        j += 1
    return j


def is_nested_bullet(line: str) -> bool:
    stripped = line.lstrip(" \t")
    if line.startswith("\t"):
        return stripped.startswith(("- ", "* "))
    if line.startswith("  "):
        return stripped.startswith(("- ", "* "))
    return False


def collect_immediate_nested_bullets(section_lines: list[str], parent_i: int) -> list[str]:
    children: list[str] = []
    j = next_non_empty(section_lines, parent_i + 1)
    while j < len(section_lines):
        line = section_lines[j]
        stripped = line.strip()
        if not stripped:
            j += 1
            continue
        if line.startswith("#"):
            break
        if is_nested_bullet(line):
            children.append(line)
            j += 1
            continue
        if line.startswith(("- ", "* ")):
            break
        if children:
            j += 1
            continue
        break
    return children


def check_oec_intro_sublist_nesting(lines: list[str], path_label: str) -> list[str]:
    """O/E/C lines that introduce sublists must use nested child bullets."""
    errors: list[str] = []

    for i, raw in enumerate(lines):
        stripped = raw.strip()
        if not (
            stripped.startswith("- O:")
            or stripped.startswith("- E:")
            or stripped.startswith("- C:")
        ):
            continue
        if not stripped.endswith(":"):
            continue

        saw_child = False
        j = i + 1
        while j < len(lines):
            nxt = lines[j]
            nxt_stripped = nxt.strip()
            if not nxt_stripped:
                j += 1
                continue
            if nxt_stripped.startswith(("#", "<a id=", "<details>", "</details>", "---")):
                break
            if nxt_stripped.startswith(("- O:", "- E:", "- C:")):
                break
            if nxt.startswith(("  - ", "  * ", "\t- ", "\t* ")):
                saw_child = True
                j += 1
                continue
            if nxt.startswith(("- ", "* ")) or nxt.startswith((" - ", " * ")):
                preview = stripped if len(stripped) <= 120 else stripped[:117] + "..."
                errors.append(
                    f"{path_label}:{j + 1}: child bullets under {preview!r} must be nested "
                    "with indentation (e.g. '  - '), not written as peer or single-space bullets"
                )
                break
            if saw_child:
                j += 1
                continue
            break

    return errors


def check_ch4_32_mandatory_traceability_bidirectional(section_lines: list[str]) -> list[str]:
    errors: list[str] = []
    parent_i = None
    for i, line in enumerate(section_lines):
        if line.rstrip() == "- bidirectional, such that:":
            parent_i = i
            break
    if parent_i is None:
        errors.append(
            "Chapter Four §3.2: missing parent bullet '- bidirectional, such that:'"
        )
        return errors

    children = collect_immediate_nested_bullets(section_lines, parent_i)
    if len(children) < 2:
        errors.append(
            "Chapter Four §3.2: '- bidirectional, such that:' must be followed by at least two nested child bullets"
        )

    return errors


DEFAULT_THEMATIC_BREAK_TARGETS: tuple[str, ...] = (
    "core_00_preamble.md",
    "core_01_a_values_principles.md",
    "core_01_b_stewardship_capacity_principles.md",
    "core_02-04_definition_mechanics.md",
    "core_05-05_definitions_a_independent.md",
    "core_05-05_definitions_b_semi_independent.md",
    "core_05-05_definitions_c_dependent_clusters.md",
    "core_06-06_standing_assessment.md",
    "core_07-07_standing_integration.md",
    "core_08-08_misconduct.md",
    "core_09-09_forum.md",
    "core_10-10_rights_part_a.md",
    "core_10-10_rights_part_b.md",
    "core_10-10_rights_part_c.md",
    "core_10-10_rights_part_d.md",
    "core_11-11_governance.md",
    "core_12-14_amendment.md",
    "core_15-15_incorporation.md",
    "corpus_systems.md",
    "corpus_institutions.md",
    "corpus_forum.md",
    "corpus_joint_structure.md",
    "CONSTITUTIONAL_REGRESSION_SCENARIOS.md",
    "README.md",
    "doc_architecture.md",
    "architecture_primer.md",
)


def check_horizontal_rule_preceding_blank(lines: list[str], path_label: str) -> list[str]:
    """``---`` must be preceded by a blank line (avoid Setext H2 misparsing)."""
    errors: list[str] = []
    in_fence = False
    in_yaml_fm = False

    for i, line in enumerate(lines):
        s = line.strip()
        if s.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if i == 0 and s == "---":
            in_yaml_fm = True
            continue
        if in_yaml_fm:
            if s == "---":
                in_yaml_fm = False
            continue
        if s != "---":
            continue
        if i == 0:
            continue
        if lines[i - 1].strip() != "":
            prev = lines[i - 1].strip()
            preview = prev if len(prev) <= 120 else prev[:117] + "..."
            errors.append(
                f"{path_label}:{i + 1}: horizontal rule '---' must be preceded by a "
                f"blank line (CommonMark Setext ambiguity); previous text: {preview!r}"
            )
    return errors


def resolve_thematic_paths(root: pathlib.Path, arg: str | None) -> list[pathlib.Path]:
    if arg is None:
        names = [
            *binding_corpus_scope(root, include_support_docs=True),
            "CONSTITUTIONAL_REGRESSION_SCENARIOS.md",
            "architecture_primer.md",
        ]
    else:
        names = tuple(n.strip() for n in arg.split(",") if n.strip())
    paths: list[pathlib.Path] = []
    for name in names:
        p = root / name
        if p.is_file():
            paths.append(p)
    return paths


def check_ch2_42_evansion_nesting(section_lines: list[str]) -> list[str]:
    """First category under Non-Reductive Evasion Types must retain nested examples."""
    errors: list[str] = []
    cat_i = None
    for i, line in enumerate(section_lines):
        if line.rstrip() == "- Representation and Proxy-Based Evasion":
            cat_i = i
            break
    if cat_i is None:
        errors.append(
            "Chapter Three §3.2: missing category line '- Representation and Proxy-Based Evasion'"
        )
        return errors

    children = collect_immediate_nested_bullets(section_lines, cat_i)
    if not children:
        errors.append("Chapter Three §3.2: missing nested lines under Representation and Proxy-Based Evasion")
        return errors
    return errors


def main() -> int:
    args = parse_args()
    root = pathlib.Path(args.root).resolve()
    path = root / args.file
    text = load_text(path)

    findings: list[str] = []
    thematic_paths = resolve_thematic_paths(root, args.thematic_break_files)

    for tb_path in thematic_paths:
        tb_lines = tb_path.read_text(encoding="utf-8").splitlines()
        rel = tb_path.relative_to(root).as_posix()
        findings.extend(check_horizontal_rule_preceding_blank(tb_lines, rel))
        findings.extend(check_oec_intro_sublist_nesting(tb_lines, rel))

    s65 = slice_between(
        text,
        "#### 3.2 Mandatory traceability properties",
        "### 4. Observability of Traceability Requirement",
    )
    if s65 is None:
        findings.append(
            "Could not slice Chapter Four §3.2 (missing heading or section 4 boundary)"
        )
    else:
        findings.extend(
            check_ch4_32_mandatory_traceability_bidirectional(s65.splitlines())
        )

    s42 = slice_between(
        text,
        "#### 2.2 Non-Reductive Evasion Types",
        "#### 2.3 Reductive Evasion",
    )
    if s42 is None:
        findings.append(
            "Could not slice Chapter Three §3.2 (missing heading or §2.3 boundary)"
        )
    else:
        findings.extend(check_ch2_42_evansion_nesting(s42.splitlines()))

    print("Corpus Markdown structure audit:")
    print(f"- Definition-structure slice file: {args.file} (Ch 3 §3.2 + Ch 4 §3.2)")
    print(
        "- Horizontal-rule (---) blank-line targets: "
        + ", ".join(p.relative_to(root).as_posix() for p in thematic_paths)
    )
    if findings:
        print("- Result: FAIL")
        for f in findings:
            print(f"  - {f}")
        return 1

    print("- Result: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
