#!/usr/bin/env python3
"""Check that every time reference in the binding corpus shows its logic.

A **time reference** is a stated length of time (a number with a unit: 24 hours,
seven days, 12 months, 30 years) or a vague stand-in for one ("reasonable
period", "reasonable timeframe", "promptly", "as soon as feasible", "without
undue delay").

Every time reference must show where its length comes from, in the same
sentence:

* **Scaled** reference: it names a **bound kind** (outer bound, intake target,
  stage target, certification interval, restore-challenge window, ...) and the
  **tier or class** that sets it (Tier B, Class C, "the matching tier", ...).
* **Fixed** reference: it uses a **registered window name** (cooling-off period,
  watch period, order term, ...) whose owner holds the length.
* **Scaled window** name (response window, resolution window): the name is a
  bound kind whose length comes from a tier or class column. A number beside it
  still needs the tier or class that sets it.

A table row is read together with its header row and the line that introduces
the table, so a column headed "Tier B" supplies the tier for every cell under it.

The vocabulary lives in `tools/time_reference_registry.json`: bound kinds, basis
patterns, fixed periods with their owners, and a short list of exempt contexts.
To add a new fixed length, register its name and owner there first.

References that predate the rule are recorded in
`tools/time_reference_baseline.json`, keyed by file and sentence text. That list
only shrinks: a new or edited reference that does not show its logic fails, and
a baseline entry that has become compliant (or disappeared) is reported as
stale so the list cannot rot. `--all` prints the backlog.

Rule ID: TIME-REF-01
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from corpus_paths import binding_corpus_scope  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
RULE = "TIME-REF-01"
REGISTRY_PATH = _TOOLS / "time_reference_registry.json"
BASELINE_PATH = _TOOLS / "time_reference_baseline.json"

_NUM_WORDS = (
    r"(?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|"
    r"(?:twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety)(?:-(?:one|two|three|four|five|six|seven|eight|nine))?|"
    r"hundred)"
)
DURATION_RE = re.compile(
    rf"(?:\b(?:\d+|{_NUM_WORDS})(?:[-\s]|\s*\*\*\s*)?(?:calendar\s+)?(?:hour|day|week|month|year)s?\b"
    r"|\ba\s+(?:week|month|year)\b)",
    re.IGNORECASE,
)
VAGUE_RE = re.compile(
    r"reasonable\s+(?:period|timeframe|time\s+frame)s?"
    r"|\bpromptly\b"
    r"|as\s+soon\s+as\s+(?:feasible|possible|lawfully\s+feasible)"
    r"|without\s+(?:unjustified|undue|unreasonable)\s+delay",
    re.IGNORECASE,
)
SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+(?=[A-Z“\"*\[(])")
LINK_RE = re.compile(r"\]\([^)]*\)")
HTML_RE = re.compile(r"<[^>]+>")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
TABLE_ROW_RE = re.compile(r"^\s*\|")
TABLE_RULE_RE = re.compile(r"^\s*\|?[\s:|-]+\|[\s:|-]*$")


@dataclass(frozen=True)
class Finding:
    file: str
    line: int
    kind: str  # "duration" | "vague"
    text: str  # the unit that was checked, cleaned
    missing: tuple[str, ...]  # subset of ("bound", "basis")

    def key(self) -> str:
        return f"{self.file}::{self.kind}::{_digest(self.text)}"


class Registry:
    def __init__(self, data: dict) -> None:
        # A scaled window is a registered name whose length comes from a tier or
        # class column (response window, resolution window). Its name is a bound
        # kind, but unlike a fixed period it does not excuse a number: "a 7-day
        # response window" still needs the tier or class that sets the length.
        scaled_names = [re.escape(item["name"]) for item in data.get("scaled_windows", [])]
        self.bound = re.compile("|".join(list(data["bound_terms"]) + scaled_names), re.IGNORECASE)
        self.basis = re.compile("|".join(data["basis_terms"]))
        self.fixed = re.compile(
            "|".join(re.escape(p["name"]) for p in data["fixed_periods"]), re.IGNORECASE
        )
        self.exempt = [
            re.compile(item["pattern"], re.IGNORECASE) for item in data.get("exempt_unit_patterns", [])
        ]
        # Vague wording that stays open on purpose, each with a stated reason.
        self.qualitative = [
            (item["file"], item["contains"]) for item in data.get("qualitative_on_purpose", [])
        ]

    def is_qualitative(self, rel_path: str, unit: str) -> bool:
        return any(rel_path == f and needle in unit for f, needle in self.qualitative)


def load_registry(path: Path = REGISTRY_PATH) -> Registry:
    return Registry(json.loads(path.read_text(encoding="utf-8")))


def _digest(text: str) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest()[:12]


def clean(text: str) -> str:
    text = LINK_RE.sub("]", text)
    text = HTML_RE.sub("", text)
    text = text.replace("**", "").replace("`", "")
    return re.sub(r"\s+", " ", text).strip()


def references(text: str) -> list[str]:
    """Return the kinds of time reference found in text."""
    kinds = []
    if DURATION_RE.search(text):
        kinds.append("duration")
    if VAGUE_RE.search(text):
        kinds.append("vague")
    return kinds


def check_unit(unit: str, context: str, registry: Registry) -> tuple[str, ...]:
    """Return what the unit is missing; empty means compliant.

    `unit` is the sentence or table row holding the reference. `context` is
    extra text that may supply the logic (table header and lead-in line).
    """
    whole = f"{context} {unit}".strip()
    if registry.fixed.search(whole):
        return ()
    missing = []
    if not registry.bound.search(whole):
        missing.append("bound")
    if not registry.basis.search(whole):
        missing.append("basis")
    return tuple(missing)


def scan_text(rel_path: str, text: str, registry: Registry) -> list[Finding]:
    findings: list[Finding] = []
    lines = text.split("\n")
    in_fence = False
    table_lead = ""
    table_header = ""
    in_table = False
    last_prose = ""
    for index, raw in enumerate(lines):
        if FENCE_RE.match(raw):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        stripped = raw.strip()
        if not stripped or stripped.startswith("<a id=") or stripped.startswith("#"):
            if not stripped.startswith("|"):
                in_table = False
            if stripped and not stripped.startswith("<a id="):
                last_prose = ""
            continue
        if TABLE_ROW_RE.match(raw):
            if not in_table:
                in_table = True
                table_lead = last_prose
                table_header = clean(raw)
                continue
            if TABLE_RULE_RE.match(raw):
                continue
            units = [(clean(raw), f"{clean(table_lead)} {table_header}")]
        else:
            in_table = False
            body = re.sub(r"^\s*(?:[-*+]|\d+\.)\s+", "", raw)
            sentences = SENTENCE_SPLIT_RE.split(body)
            units = [(clean(s), "") for s in sentences]
            last_prose = raw
        for unit, context in units:
            if not unit:
                continue
            kinds = references(unit)
            if not kinds:
                continue
            if any(p.search(unit) for p in registry.exempt):
                continue
            if kinds == ["vague"] and registry.is_qualitative(rel_path, unit):
                continue
            missing = check_unit(unit, context, registry)
            if not missing:
                continue
            for kind in kinds:
                findings.append(Finding(rel_path, index + 1, kind, unit, missing))
    return findings


def scan(root: Path, scope: list[str], registry: Registry) -> list[Finding]:
    findings: list[Finding] = []
    for rel_path in scope:
        path = root / rel_path
        if path.is_file():
            findings.extend(scan_text(rel_path, path.read_text(encoding="utf-8"), registry))
    return findings


def load_baseline() -> dict[str, str]:
    if not BASELINE_PATH.is_file():
        return {}
    data = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
    return {entry["key"]: entry.get("snippet", "") for entry in data.get("known", [])}


def write_baseline(findings: list[Finding]) -> None:
    seen: dict[str, Finding] = {}
    for finding in findings:
        seen.setdefault(finding.key(), finding)
    entries = [
        {"key": key, "snippet": item.text[:140]}
        for key, item in sorted(seen.items())
    ]
    BASELINE_PATH.write_text(
        json.dumps(
            {
                "rule": RULE,
                "note": (
                    "Time references that predate TIME-REF-01 and do not yet name a bound "
                    "kind and a tier or class (or a registered fixed period). Shrink this list; "
                    "do not grow it. Regenerate with --write-baseline only when removing entries."
                ),
                "known": entries,
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--all", action="store_true", help="List the whole backlog, new and baselined.")
    parser.add_argument("--write-baseline", action="store_true", help="Rewrite the baseline from the current tree.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    registry = load_registry()
    findings = scan(root, binding_corpus_scope(root), registry)

    if args.write_baseline:
        write_baseline(findings)
        print(f"Wrote {BASELINE_PATH.relative_to(root)} ({len({f.key() for f in findings})} entries)")
        return 0

    baseline = load_baseline()
    current = {f.key() for f in findings}
    new = [f for f in findings if f.key() not in baseline]
    stale = sorted(set(baseline) - current)

    if args.all:
        print(f"{RULE}: {len(current)} time reference(s) without a stated bound and tier or class")
        for finding in findings:
            flag = " " if finding.key() in baseline else "NEW"
            print(f"  {flag} {finding.file}:{finding.line} [{finding.kind}; missing {', '.join(finding.missing)}]")
            print(f"        {finding.text[:160]}")

    if stale:
        print(f"FAIL: {len(stale)} baseline entr(ies) no longer needed ({RULE}); remove with --write-baseline", file=sys.stderr)
        for key in stale:
            print(f"  {key}  {baseline[key][:100]}", file=sys.stderr)
        return 1

    if new:
        print(f"FAIL: {len(new)} time reference(s) without a stated bound and tier or class ({RULE})", file=sys.stderr)
        for finding in new:
            print(f"  {finding.file}:{finding.line}: [{finding.kind}] missing {' and '.join(finding.missing)}: {finding.text[:140]}", file=sys.stderr)
        print(
            "  Name the bound kind (e.g. outer bound, intake target) and the tier or class that sets it, "
            "or use a registered fixed-period name (tools/time_reference_registry.json).",
            file=sys.stderr,
        )
        return 1

    print(f"PASS: {RULE} — every new time reference shows its bound and tier or class ({len(baseline)} older references baselined in {BASELINE_PATH.name})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
