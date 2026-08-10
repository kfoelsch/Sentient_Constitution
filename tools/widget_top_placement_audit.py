#!/usr/bin/env python3
"""Audit that opening widgets sit at the top of their owning unit.

Rules:
  NAV-READER-06  — chapter/part Reader guidance belongs in the opening stack
                   before operative prose (local guidance under a later section
                   remains allowed).
  NAV-TRACE-09   — when a section's *direct* content carries Trace / D/A/C,
                   those widgets open the unit (after optional anchors and
                   opening Reader guidance). Child-section widgets do not
                   count against the parent.
  OWNER-OPENING-01 / NAV-PLACEMENT-01 stack order when widgets are present:
                   Corpus placement → Reader guidance → Trace → D/A/C, then
                   the binding owner / home line and other operative prose.
  NAV-WIDGET-TOP-01 spacing — consecutive opening-stack widgets are adjacent
                   (blank lines only; no ``<br>``, owner lines, or other prose
                   between them). ``<br>`` belongs after the last stack widget
                   before operative content.

Does not require every section to carry Trace or D/A/C; it only constrains
placement when those widgets exist in the unit's direct content.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from corpus_paths import COMPANION_WRAPPERS, binding_corpus_scope

ROOT = Path(__file__).resolve().parents[1]

TRACE_SUMMARY = (
    '<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>'
)
DEC_SUMMARY = (
    '<summary><strong><span style="color: #2563eb;">'
    "Definitions · Assessment · Compliance</span></strong></summary>"
)
PLACEMENT_SUMMARY = (
    '<summary><strong><span style="color: #2563eb;">Corpus placement '
    "(non-operative): file structure and reading rules</span></strong></summary>"
)
READER_GUIDANCE_RE = re.compile(
    r'<summary><strong><span style="color: #2563eb;">'
    r"Reader guidance \(non-operative\):"
)
INLINE_DEFINITION_RE = re.compile(
    r'<strong><span style="color: #2563eb;">Definition:</span></strong>'
)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
ANCHOR_RE = re.compile(r'^<a id="[^"]+"></a>\s*$')
PLAIN_TERMS_RE = re.compile(r"^\*In plain terms[:,]")
OWNER_LINE_RE = re.compile(
    r"^(?:"
    r"This file is the "
    r"|This file is \*\*"
    r"|Chapter [A-Za-z0-9, \-*]+ is the constitutional owner\b"
    r"|Chapters? \d+"
    r"|\*\*?CS-\d+"
    r"|\*\*?CI-\d+"
    r"|\*\*?CF-\d+"
    r"|\*\*?CJS-\d+"
    r"|CS-\d+, Part "
    r"|CI-\d+"
    r"|CF-\d+"
    r"|CJS-\d+"
    r")"
)
NON_OPERATIVE_SUBTITLE_RE = re.compile(r"^\*Non-operative subtitle:")
# Bold run-in subsection titles (e.g. **8.3. Audit…**) that host a local Trace.
BOLD_RUNIN_SUBSECTION_RE = re.compile(r"^\*\*\d+(?:\.\d+)+\.?\s")
WIDGET_RANK = {
    "placement": 0,
    "reader": 1,
    "trace": 2,
    "dac": 3,
}

# Landing wrappers use a different front-door anatomy (visible gloss + index).
WRAPPER_NAMES = set(COMPANION_WRAPPERS)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    return parser.parse_args()


def heading_level(line: str) -> int | None:
    match = HEADING_RE.match(line.strip())
    return len(match.group(1)) if match else None


def section_end(lines: list[str], start: int, level: int) -> int:
    for idx in range(start + 1, len(lines)):
        next_level = heading_level(lines[idx])
        if next_level is not None and next_level <= level:
            return idx
    return len(lines)


def direct_content_end(lines: list[str], start: int, level: int, end: int) -> int:
    """End of content owned by this heading before any deeper child heading."""
    for idx in range(start + 1, end):
        child_level = heading_level(lines[idx])
        if child_level is not None and child_level > level:
            return idx
    return end


def next_nonempty(lines: list[str], start: int, end: int | None = None) -> int | None:
    limit = len(lines) if end is None else end
    for idx in range(start, limit):
        if lines[idx].strip():
            return idx
    return None


def classify_details(lines: list[str], open_idx: int, end: int) -> str | None:
    summary_idx = next_nonempty(lines, open_idx + 1, end)
    if summary_idx is None:
        return None
    summary = lines[summary_idx].strip()
    if summary == TRACE_SUMMARY:
        return "trace"
    if summary == DEC_SUMMARY:
        return "dac"
    if summary == PLACEMENT_SUMMARY:
        return "placement"
    if READER_GUIDANCE_RE.search(summary):
        return "reader"
    return "other"


def details_close_idx(lines: list[str], open_idx: int, end: int) -> int | None:
    depth = 0
    for idx in range(open_idx, end):
        stripped = lines[idx].strip()
        if stripped == "<details>":
            depth += 1
        elif stripped == "</details>":
            depth -= 1
            if depth == 0:
                return idx
    return None


def is_registry_annex(rel: str) -> bool:
    return rel.endswith("_00_registry_and_reading_rules.md")


def is_ch5_definition_file(rel: str) -> bool:
    name = Path(rel).name
    return name.startswith("core_05_") or name == "core_05__definitions_home.md"


def intervening_between_widgets(
    lines: list[str], after_close: int, before_open: int, rel: str
) -> list[str]:
    """Only blank lines may appear between consecutive opening-stack widgets."""
    findings: list[str] = []
    for idx in range(after_close + 1, before_open):
        stripped = lines[idx].strip()
        if not stripped:
            continue
        if stripped == "<br>":
            findings.append(
                f"{rel}:{idx + 1}: remove <br> between opening-stack widgets "
                f"(spacer belongs after the last widget before operative prose)"
            )
        else:
            preview = stripped[:72]
            findings.append(
                f"{rel}:{idx + 1}: remove intervening content between "
                f"opening-stack widgets ({preview!r})"
            )
    return findings


def audit_contiguous_widget_run(
    lines: list[str],
    rel: str,
    widgets: list[tuple[int, int, str]],
) -> list[str]:
    """``widgets`` entries are (open_idx, close_idx, kind)."""
    findings: list[str] = []
    last_rank = -1
    last_kind = None
    for i, (open_idx, close_idx, kind) in enumerate(widgets):
        rank = WIDGET_RANK[kind]
        if rank < last_rank:
            findings.append(
                f"{rel}:{open_idx + 1}: file-top widget order must be "
                f"placement → reader guidance → Trace → D/A/C "
                f"(found {kind} after {last_kind})"
            )
        last_rank = max(last_rank, rank)
        last_kind = kind
        if i == 0:
            continue
        prev_close = widgets[i - 1][1]
        findings.extend(
            intervening_between_widgets(lines, prev_close, open_idx, rel)
        )
    return findings


def audit_file_top_stack(lines: list[str], rel: str) -> list[str]:
    """Corpus placement / Reader / Trace / D/A/C before first body heading."""
    if Path(rel).name in WRAPPER_NAMES:
        return []

    first_heading = None
    for idx, line in enumerate(lines):
        if heading_level(line) == 1:
            first_heading = idx
            break
    if first_heading is None:
        return []

    body_start = len(lines)
    for idx in range(first_heading + 1, len(lines)):
        if heading_level(lines[idx]) is not None:
            body_start = idx
            break

    findings: list[str] = []
    seen_widgets: list[tuple[int, int, str]] = []
    stack_closed = False
    registry = is_registry_annex(rel)
    idx = first_heading + 1
    while idx < body_start:
        stripped = lines[idx].strip()
        if not stripped:
            idx += 1
            continue
        if stripped == "<details>":
            kind = classify_details(lines, idx, body_start)
            close = details_close_idx(lines, idx, body_start)
            if close is None:
                findings.append(
                    f"{rel}:{idx + 1}: unterminated <details> in file-top stack"
                )
                break
            if kind in WIDGET_RANK:
                if stack_closed:
                    findings.append(
                        f"{rel}:{idx + 1}: {kind} widget must stay in the file-top "
                        f"opening stack before operative prose "
                        f"(found after stack already closed)"
                    )
                else:
                    seen_widgets.append((idx, close, kind))
            elif kind == "other":
                stack_closed = True
            idx = close + 1
            continue

        # Registry annex gloss may precede the first widget only.
        if (
            registry
            and PLAIN_TERMS_RE.match(stripped)
            and not seen_widgets
            and not stack_closed
        ):
            idx += 1
            continue

        if NON_OPERATIVE_SUBTITLE_RE.match(stripped) and not seen_widgets:
            idx += 1
            continue

        if ANCHOR_RE.match(stripped) and not seen_widgets:
            idx += 1
            continue

        # Any visible prose — including owner/home lines and <br> after the
        # stack — closes the widget window. <br> between widgets is caught by
        # audit_contiguous_widget_run when the next widget still appears.
        if stripped == "<br>":
            nxt = next_nonempty(lines, idx + 1, body_start)
            if (
                nxt is not None
                and lines[nxt].strip() == "<details>"
                and classify_details(lines, nxt, body_start) in WIDGET_RANK
            ):
                # Between-widget <br>; keep stack open so the next widget is
                # recorded and intervening_between_widgets can flag the <br>.
                idx += 1
                continue
            stack_closed = True
            idx += 1
            continue

        # Owner / home line and all other operative prose end the stack.
        stack_closed = True
        idx += 1

    findings.extend(audit_contiguous_widget_run(lines, rel, seen_widgets))
    return findings


def previous_nonempty(lines: list[str], before: int, start: int) -> int | None:
    for idx in range(before - 1, start - 1, -1):
        if lines[idx].strip():
            return idx
    return None


def is_local_runin_widget(lines: list[str], widget_idx: int, start: int) -> bool:
    """True when Trace/D/A/C sits under a bold ``**8.3.``-style run-in title."""
    prev = previous_nonempty(lines, widget_idx, start)
    return prev is not None and bool(
        BOLD_RUNIN_SUBSECTION_RE.match(lines[prev].strip())
    )


def direct_opening_trace_or_dac(
    lines: list[str], start: int, direct_end: int
) -> int | None:
    """First Trace/D/A/C that opens the unit (not a mid-section run-in Trace)."""
    idx = start
    while idx < direct_end:
        if lines[idx].strip() == "<details>":
            kind = classify_details(lines, idx, direct_end)
            close = details_close_idx(lines, idx, direct_end)
            if kind in {"trace", "dac"} and not is_local_runin_widget(
                lines, idx, start
            ):
                return idx
            if close is None:
                return None
            idx = close + 1
            continue
        idx += 1
    return None


def first_kind_line(
    lines: list[str], start: int, end: int, want: str
) -> int | None:
    idx = start
    while idx < end:
        if lines[idx].strip() == "<details>":
            kind = classify_details(lines, idx, end)
            close = details_close_idx(lines, idx, end)
            if kind == want:
                return idx + 1
            if close is None:
                return None
            idx = close + 1
            continue
        idx += 1
    return None


def collect_section_opening_widgets(
    lines: list[str], start: int, direct_end: int
) -> list[tuple[int, int, str]]:
    """Leading reader / Trace / D/A/C widgets under a section heading."""
    widgets: list[tuple[int, int, str]] = []
    idx = start
    while idx < direct_end:
        stripped = lines[idx].strip()
        if not stripped:
            idx += 1
            continue
        if ANCHOR_RE.match(stripped):
            if widgets:
                break
            idx += 1
            continue
        if stripped == "<details>":
            kind = classify_details(lines, idx, direct_end)
            close = details_close_idx(lines, idx, direct_end)
            if close is None:
                break
            if kind in {"reader", "trace", "dac"} and not is_local_runin_widget(
                lines, idx, start
            ):
                widgets.append((idx, close, kind))
                idx = close + 1
                continue
            break
        break
    return widgets


def audit_section_widgets(
    lines: list[str],
    rel: str,
    start: int,
    level: int,
    end: int,
    heading_text: str,
) -> list[str]:
    """Trace / D/A/C in a unit's direct content must open that unit."""
    if is_ch5_definition_file(rel):
        # Chapter Five entry anatomy is owned by ch5-entry-format / related audits.
        return []

    direct_end = direct_content_end(lines, start, level, end)
    opening_widget = direct_opening_trace_or_dac(lines, start + 1, direct_end)
    if opening_widget is None:
        return []

    findings: list[str] = []
    section_widgets = collect_section_opening_widgets(
        lines, start + 1, direct_end
    )
    findings.extend(audit_contiguous_widget_run(lines, rel, section_widgets))

    idx = start + 1
    while idx < direct_end:
        stripped = lines[idx].strip()
        if not stripped:
            idx += 1
            continue
        if stripped == "<details>":
            kind = classify_details(lines, idx, direct_end)
            close = details_close_idx(lines, idx, direct_end)
            if close is None:
                return [
                    f"{rel}:{idx + 1}: unterminated <details> under {heading_text!r}"
                ]
            if idx == opening_widget:
                if kind == "dac":
                    trace_line = first_kind_line(lines, start + 1, direct_end, "trace")
                    if (
                        trace_line is not None
                        and trace_line > idx + 1
                        and not is_local_runin_widget(
                            lines, trace_line - 1, start + 1
                        )
                    ):
                        findings.append(
                            f"{rel}:{idx + 1}: Trace must precede D/A/C on "
                            f"{heading_text!r}"
                        )
                return findings
            if kind in {"trace", "reader", "dac"} and not is_local_runin_widget(
                lines, idx, start + 1
            ):
                return findings
            if kind == "other" and idx < opening_widget:
                findings.append(
                    f"{rel}:{idx + 1}: Trace / D/A/C on {heading_text!r} must open "
                    f"the section (found a non-routing widget first)"
                )
                return findings
            idx = close + 1
            continue

        if ANCHOR_RE.match(stripped) or stripped in {"<br>", "---"}:
            # Leading spacers before the opening widget are stale file-top habits;
            # contiguous-stack checks own between-widget <br> discipline.
            idx += 1
            continue

        if INLINE_DEFINITION_RE.search(stripped):
            if classify_details(lines, opening_widget, direct_end) == "trace":
                findings.append(
                    f"{rel}:{idx + 1}: Trace must precede inline Definition on "
                    f"{heading_text!r}"
                )
            return findings

        if idx < opening_widget:
            preview = stripped[:72]
            findings.append(
                f"{rel}:{idx + 1}: Trace / D/A/C on {heading_text!r} must open "
                f"the section (found prose first: {preview!r})"
            )
            return findings
        return findings

    return findings


def audit_file(path: Path, root: Path) -> list[str]:
    rel = path.relative_to(root).as_posix()
    if rel.startswith("archive/") or rel.startswith("core_05-05_definitions_"):
        return []

    lines = path.read_text(encoding="utf-8").splitlines()
    findings = audit_file_top_stack(lines, rel)

    for idx, line in enumerate(lines):
        level = heading_level(line)
        if level is None or level < 2:
            continue
        end = section_end(lines, idx, level)
        findings.extend(
            audit_section_widgets(lines, rel, idx, level, end, line.strip())
        )
    return findings


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    findings: list[str] = []
    for rel in binding_corpus_scope(root):
        path = root / rel
        if path.is_file() and path.suffix == ".md":
            findings.extend(audit_file(path, root))

    if findings:
        print("Widget top-placement audit failures:", file=sys.stderr)
        for item in findings:
            print(f"  - {item}", file=sys.stderr)
        print(f"Total: {len(findings)}", file=sys.stderr)
        return 1

    print("Widget top-placement audit OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
