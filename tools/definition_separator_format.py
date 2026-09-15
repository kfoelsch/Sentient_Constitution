#!/usr/bin/env python3
"""Canonical ``---`` placement for Chapter Five and CJS-3 definition files.

Architecture (CH5-FORMAT / CJS-1.14): one horizontal rule between reader
units. Anchors for the next heading sit *after* that rule, not a second
rule under the title. Double/triple stacks from retired Part B/C files
are not used on the current band / oDef files.

Canonical shape::

    [end of previous unit]

    ---

    <a id="entry-slug"></a>

    #### Title
"""

from __future__ import annotations

import re

HEADING_RE = re.compile(r"^(#{1,6})\s+\S")
ANCHOR_RE = re.compile(r'^<a id="[^"]+"></a>\s*$')


def heading_level(line: str) -> int | None:
    match = HEADING_RE.match(line)
    return len(match.group(1)) if match else None


def is_anchor(line: str) -> bool:
    return bool(ANCHOR_RE.match(line.strip()))


def is_hr(line: str) -> bool:
    return line.strip() == "---"


def is_trace_bearing(lines: list[str], heading_idx: int) -> bool:
    idx = heading_idx + 1
    while idx < len(lines) and not lines[idx].strip():
        idx += 1
    return idx < len(lines) and lines[idx].strip() == "<details>"


def collect_preamble(lines: list[str], heading_idx: int) -> tuple[int, list[str], bool]:
    """Return (preamble_start, anchors in the separator zone, whether a ``---`` was present).

    The separator zone is the run of blanks, ``---``, and ``<a id>`` lines
    immediately above the heading. Leftover section-end anchors that sat
    between stacked rules are kept with the next heading so one ``---``
    can replace the sandwich.
    """
    idx = heading_idx - 1
    anchors: list[str] = []
    had_hr = False
    while idx >= 0:
        stripped = lines[idx].strip()
        if not stripped:
            idx -= 1
            continue
        if is_anchor(lines[idx]):
            anchors.append(stripped)
            idx -= 1
            continue
        if is_hr(lines[idx]):
            had_hr = True
            idx -= 1
            continue
        break
    anchors.reverse()
    return idx + 1, anchors, had_hr


def normalize_heading_separators(text: str) -> str:
    """Rewrite heading preambles to the canonical single-``---`` shape.

    Does not invent a ``---`` unless the heading already had one or is a
    trace-bearing sibling (CH5-FORMAT). CJS-1.14 treats ``---`` as a cluster
    delimiter, so new rules are not inserted in front of ordinary subsections.
    """
    newline = "\n" if "\r\n" not in text else "\r\n"
    lines = text.splitlines()
    heading_idxs = [i for i, raw in enumerate(lines) if heading_level(raw)]
    if not heading_idxs:
        return text

    units: list[dict] = []
    for heading_idx in heading_idxs:
        preamble_start, anchors, had_hr = collect_preamble(lines, heading_idx)
        units.append(
            {
                "heading_idx": heading_idx,
                "preamble_start": preamble_start,
                "anchors": anchors,
                "had_hr": had_hr,
                "level": heading_level(lines[heading_idx]),
                "heading": lines[heading_idx],
                "trace": is_trace_bearing(lines, heading_idx),
            }
        )

    out: list[str] = []
    cursor = 0
    prev_level: int | None = None
    for index, unit in enumerate(units):
        if index == 0:
            out.extend(lines[: unit["heading_idx"] + 1])
            cursor = unit["heading_idx"] + 1
            prev_level = unit["level"]
            continue

        body = list(lines[cursor : unit["preamble_start"]])
        while body and not body[-1].strip():
            body.pop()
        while body and is_hr(body[-1]):
            unit["had_hr"] = True
            body.pop()
            while body and not body[-1].strip():
                body.pop()

        body_has_content = any(
            raw.strip() and not is_hr(raw) and not is_anchor(raw) for raw in body
        )
        first_child = (
            prev_level is not None
            and unit["level"] is not None
            and unit["level"] > prev_level
            and not body_has_content
        )
        # Invent a missing rule only for Chapter Five leaf titles (#### / #####).
        # CJS-1.14 treats --- as a cluster delimiter, so ## / ### must not gain
        # a new rule just because they carry Trace.
        invent = unit["trace"] and unit["level"] is not None and unit["level"] >= 4
        need_hr = not first_child and (unit["had_hr"] or invent)

        out.extend(body)
        if need_hr:
            if out and out[-1].strip():
                out.append("")
            out.append("---")
            out.append("")
        elif out and out[-1].strip():
            out.append("")

        out.extend(unit["anchors"])
        if unit["anchors"]:
            out.append("")
        out.append(unit["heading"])

        cursor = unit["heading_idx"] + 1
        prev_level = unit["level"]

    out.extend(lines[cursor:])
    normalized = newline.join(out)
    normalized = collapse_hr_stacks(normalized)
    if text.endswith(newline) and not normalized.endswith(newline):
        normalized += newline
    return normalized


def collapse_hr_stacks(text: str) -> str:
    """Collapse adjacent ``---`` rules (blank lines only between them) to one."""
    return re.sub(r"(?m)(?:^---\s*\n+){2,}", "---\n\n", text)


def audit_separator_lines(lines: list[str], path_label: str) -> list[str]:
    """Fail stacked, sandwiched, or wrong-side ``---`` rules before headings."""
    violations: list[str] = []

    for idx in range(len(lines) - 1):
        if not is_hr(lines[idx]):
            continue
        nxt = idx + 1
        while nxt < len(lines) and not lines[nxt].strip():
            nxt += 1
        if nxt < len(lines) and is_hr(lines[nxt]):
            violations.append(
                f"{path_label}:{idx + 1}: stacked '---' separators; use exactly one "
                "horizontal rule between reader units"
            )
            continue
        look = nxt
        while look < len(lines) and (
            not lines[look].strip() or is_anchor(lines[look])
        ):
            look += 1
        if look < len(lines) and is_hr(lines[look]) and look != nxt:
            violations.append(
                f"{path_label}:{idx + 1}: sandwiched '---' around <a id> anchors; "
                "keep one rule above the anchors"
            )

        if idx > 0 and lines[idx - 1].strip():
            violations.append(
                f"{path_label}:{idx + 1}: horizontal rule '---' must be preceded by a "
                "blank line"
            )
        after = idx + 1
        if after < len(lines) and lines[after].strip() and not is_hr(lines[after]):
            violations.append(
                f"{path_label}:{idx + 1}: horizontal rule '---' must be followed by a "
                "blank line"
            )

    for heading_idx, raw in enumerate(lines):
        level = heading_level(raw)
        if level is None or level < 2:
            continue
        idx = heading_idx - 1
        while idx >= 0 and not lines[idx].strip():
            idx -= 1
        if idx < 0:
            continue

        # Wrong-side rule: --- sitting between this heading and its own anchors.
        if is_hr(lines[idx]):
            look = idx - 1
            while look >= 0 and not lines[look].strip():
                look -= 1
            if look >= 0 and is_anchor(lines[look]):
                violations.append(
                    f"{path_label}:{heading_idx + 1}: place the single '---' above the "
                    f"entry's <a id> anchors, not between the anchors and the title: "
                    f"{raw.rstrip()}"
                )
            continue

        if not is_anchor(lines[idx]):
            continue

        look = idx
        while look >= 0:
            stripped = lines[look].strip()
            if not stripped or is_anchor(lines[look]):
                look -= 1
                continue
            break
        if look >= 0 and heading_level(lines[look]) is not None:
            prev_level = heading_level(lines[look])
            if prev_level is not None and prev_level < level:
                continue
        if (
            level >= 4
            and is_trace_bearing(lines, heading_idx)
            and (look < 0 or not is_hr(lines[look]))
        ):
            violations.append(
                f"{path_label}:{heading_idx + 1}: trace-bearing heading should use a "
                f"single '---' above its <a id> anchors: {raw.rstrip()}"
            )

    return violations
