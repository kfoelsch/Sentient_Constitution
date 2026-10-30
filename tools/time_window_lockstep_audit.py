#!/usr/bin/env python3
"""Keep every copy of the tier time windows in step with their sources.

Rule ID: TIME-LOCK-01

The tier windows have two owners:

* **Outer bounds** (7, 14, 30, 60, and 90 days for Tiers A, B, C, L, and P) are
  owned by Chapter Fourteen §6, *Tier outer bound*.
* **Intake targets** (24 hours, then 2, 4, 8, and 12 calendar days) and the
  stage table that must add up to the outer bounds are owned by CF-14.445 §3.1.

Other sections quote these figures so that a reader does not have to leave the
page: the Chapter Seven §1.6 summary table (response window = intake target,
resolution window = outer bound) and the prompt-review sentences. Those copies
are derived. This audit:

1. Reads the sources and checks that they agree with each other (the CF-14.445 §3.1
   header, its outer-bound row, and the Chapter Fourteen list). A conflict
   between sources is never repaired by the tool: a person decides which owner
   is right.
2. Rebuilds each registered copy from the sources and compares it with the file.
3. With ``--fix``, rewrites any copy that has drifted, so a change to the
   windows is made once, in the owner, and the downstream sections follow.

The registry is ``tools/time_window_lockstep_registry.json``. A registered table
or phrase that cannot be found is an error, so a copy cannot escape the check by
being moved or reworded.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RULE = "TIME-LOCK-01"
REGISTRY_PATH = Path(__file__).resolve().parent / "time_window_lockstep_registry.json"
TIERS = ("A", "B", "C", "L", "P")

CF_HEADER_RE = re.compile(r"\*\*Tier ([ABCLP])\*\* \(≤ (\d+) days\)")
CF_INTAKE_LABEL = "Forum access and intake acknowledgment"
CF_OUTER_LABEL = "Integrated resolution outer bound"
CH13_BOUND_RE = re.compile(r"^\s*-\s*\*\*Tier ([ABCLP]):\*\* at most \*\*(\d+) days\*\*", re.MULTILINE)
INTAKE_CELL_RE = re.compile(r"^(\d+) (hours?|calendar days?)$")
OUTER_CELL_RE = re.compile(r"(\d+) calendar days")

# "24 hours for Tier A, and 2, 4, 8, and 12 calendar days for Tiers B, C, L, and P"
INTAKE_PHRASE_RE = re.compile(
    r"(?P<a>\d+ hours?) (?P<p1>for|in) Tier A, and (?P<list>(?:\d+, )+and \d+) "
    r"(?P<cal>calendar )?days (?P<p2>for|in) Tiers B, C, L, and P"
)


class SourceError(Exception):
    """The sources are missing, unreadable, or disagree with each other."""


@dataclass
class Figures:
    intake: dict[str, str] = field(default_factory=dict)  # tier -> "24 hours" | "2 calendar days"
    outer_days: dict[str, int] = field(default_factory=dict)  # tier -> days

    def response_cell(self, tier: str) -> str:
        return self.intake[tier]

    def resolution_cell(self, tier: str) -> str:
        return f"{self.outer_days[tier]} calendar days"

    def intake_days(self, tier: str) -> int:
        match = INTAKE_CELL_RE.match(self.intake[tier])
        if not match or not match.group(2).startswith("calendar"):
            raise SourceError(f"intake target for Tier {tier} is not in calendar days: {self.intake[tier]!r}")
        return int(match.group(1))


@dataclass(frozen=True)
class Drift:
    file: str
    line: int
    what: str
    found: str
    expected: str


def _cells(row: str) -> list[str]:
    return [cell.strip() for cell in row.strip().strip("|").split("|")]


def _plain(cell: str) -> str:
    return cell.replace("**", "").strip()


def read_sources(root: Path, registry: dict) -> Figures:
    cf_path = root / registry["sources"]["stage_table"]
    ch13_path = root / registry["sources"]["outer_bounds"]
    for path in (cf_path, ch13_path):
        if not path.is_file():
            raise SourceError(f"source file not found: {path.relative_to(root)}")

    figures = Figures()
    header_days: dict[str, int] = {}
    row_days: dict[str, int] = {}

    lines = cf_path.read_text(encoding="utf-8").split("\n")
    start = next(
        (
            i
            for i, line in enumerate(lines)
            if line.lstrip().startswith("|") and "Pipeline stage" in line and CF_HEADER_RE.search(line)
        ),
        None,
    )
    if start is None:
        raise SourceError(f"{cf_path.name}: the tier stage-target table (header with 'Pipeline stage' and Tier columns) was not found")
    tier_columns: dict[str, int] = {}
    for index, cell in enumerate(_cells(lines[start])):
        match = CF_HEADER_RE.search(cell)
        if match:
            tier_columns[match.group(1)] = index
            header_days[match.group(1)] = int(match.group(2))
    if set(tier_columns) != set(TIERS):
        raise SourceError(f"{cf_path.name}: expected Tier columns {TIERS}, found {tuple(tier_columns)}")

    for line in lines[start + 2 :]:
        if not line.lstrip().startswith("|"):
            break
        cells = _cells(line)
        label = _plain(cells[0])
        if label.startswith(CF_INTAKE_LABEL):
            for tier, column in tier_columns.items():
                value = _plain(cells[column])
                if not INTAKE_CELL_RE.match(value):
                    raise SourceError(f"{cf_path.name}: intake target for Tier {tier} not understood: {value!r}")
                figures.intake[tier] = value
        elif label.startswith(CF_OUTER_LABEL):
            for tier, column in tier_columns.items():
                match = OUTER_CELL_RE.search(_plain(cells[column]))
                if not match:
                    raise SourceError(f"{cf_path.name}: outer bound for Tier {tier} not understood: {cells[column]!r}")
                row_days[tier] = int(match.group(1))
    if set(figures.intake) != set(TIERS):
        raise SourceError(f"{cf_path.name}: row '{CF_INTAKE_LABEL}' not found")
    if set(row_days) != set(TIERS):
        raise SourceError(f"{cf_path.name}: row '{CF_OUTER_LABEL}' not found")

    ch13_days = {tier: int(days) for tier, days in CH13_BOUND_RE.findall(ch13_path.read_text(encoding="utf-8"))}
    if set(ch13_days) != set(TIERS):
        raise SourceError(f"{ch13_path.name}: the 'Tier outer bound' list for Tiers {TIERS} was not found")

    conflicts = []
    for tier in TIERS:
        if not (header_days[tier] == row_days[tier] == ch13_days[tier]):
            conflicts.append(
                f"Tier {tier}: CF-14.445 §3.1 header {header_days[tier]}, CF-14.445 §3.1 outer-bound row {row_days[tier]}, Chapter Fourteen §6 {ch13_days[tier]}"
            )
    if conflicts:
        raise SourceError("the sources disagree; decide which owner is right (never auto-fixed): " + "; ".join(conflicts))

    figures.outer_days = ch13_days
    return figures


def render_intake_phrase(match: re.Match[str], figures: Figures) -> str:
    days = [figures.intake_days(tier) for tier in TIERS[1:]]
    listed = ", ".join(str(d) for d in days[:-1]) + f", and {days[-1]}"
    cal = match.group("cal") or ""
    return (
        f"{figures.intake['A']} {match.group('p1')} Tier A, and {listed} {cal}days "
        f"{match.group('p2')} Tiers B, C, L, and P"
    )


def check_table(rel: str, text: str, spec: dict, figures: Figures) -> tuple[list[Drift], str]:
    lines = text.split("\n")
    wanted = spec["header"]
    start = None
    for index, line in enumerate(lines):
        if line.lstrip().startswith("|") and [_plain(c) for c in _cells(line)] == wanted:
            start = index
            break
    if start is None:
        raise SourceError(f"{rel}: registered table with header {wanted} was not found")

    drifts: list[Drift] = []
    seen: set[str] = set()
    index = start + 2
    while index < len(lines) and lines[index].lstrip().startswith("|"):
        cells = _cells(lines[index])
        label = _plain(cells[0])
        tier = spec["rows"].get(label)
        if tier is not None and len(cells) == 3:
            seen.add(label)
            expected = [label, figures.response_cell(tier), figures.resolution_cell(tier)]
            if cells != expected:
                drifts.append(
                    Drift(rel, index + 1, f"table row '{label}'", " | ".join(cells[1:]), " | ".join(expected[1:]))
                )
                lines[index] = "| " + " | ".join(expected) + " |"
        index += 1
    missing = sorted(set(spec["rows"]) - seen)
    if missing:
        raise SourceError(f"{rel}: registered table rows not found: {missing}")
    return drifts, "\n".join(lines)


def check_phrases(rel: str, text: str, figures: Figures) -> tuple[list[Drift], str]:
    drifts: list[Drift] = []
    found = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal found
        found += 1
        expected = render_intake_phrase(match, figures)
        if expected != match.group(0):
            line = text.count("\n", 0, match.start()) + 1
            drifts.append(Drift(rel, line, "prompt-review intake figures", match.group(0), expected))
        return expected

    new_text = INTAKE_PHRASE_RE.sub(replace, text)
    if not found:
        raise SourceError(f"{rel}: registered intake-target sentence was not found")
    return drifts, new_text


def run(root: Path, fix: bool) -> int:
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    try:
        figures = read_sources(root, registry)
        drifts: list[Drift] = []
        rewritten: dict[str, str] = {}
        for spec in registry["tables"]:
            rel = spec["file"]
            text = rewritten.get(rel) or (root / rel).read_text(encoding="utf-8")
            found, new_text = check_table(rel, text, spec, figures)
            drifts.extend(found)
            rewritten[rel] = new_text
        for spec in registry["phrases"]:
            rel = spec["file"]
            text = rewritten.get(rel) or (root / rel).read_text(encoding="utf-8")
            found, new_text = check_phrases(rel, text, figures)
            drifts.extend(found)
            rewritten[rel] = new_text
    except SourceError as error:
        print(f"FAIL: {RULE} — {error}", file=sys.stderr)
        return 2

    if not drifts:
        print(
            f"PASS: {RULE} — the tier windows in {len(registry['tables'])} table(s) and "
            f"{len(registry['phrases'])} sentence(s) match their owners"
        )
        return 0

    for drift in drifts:
        print(f"  {drift.file}:{drift.line}: {drift.what}: found '{drift.found}', owners say '{drift.expected}'", file=sys.stderr)
    if fix:
        for rel, new_text in rewritten.items():
            path = root / rel
            if path.read_text(encoding="utf-8") != new_text:
                path.write_text(new_text, encoding="utf-8")
        print(
            f"FIXED: {RULE} — {len(drifts)} copy/copies rewritten from the owners. "
            "Now run: make architecture-index ai-corpus-sync plain-terms-edition boundary-chunks"
        )
        return 0
    print(
        f"FAIL: {RULE} — {len(drifts)} copy/copies of the tier windows differ from their owners "
        "(Chapter Fourteen §6 outer bounds, CF-14.445 §3.1 intake targets). Run: make time-window-lockstep-fix",
        file=sys.stderr,
    )
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--fix", action="store_true", help="Rewrite drifted copies from the owners.")
    args = parser.parse_args()
    return run(args.root.resolve(), args.fix)


if __name__ == "__main__":
    raise SystemExit(main())
