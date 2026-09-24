#!/usr/bin/env python3
"""Flag explicit anchors whose name has drifted from the heading they mark.

Roughly half of the corpus's `<a id="...">` anchors differ from the slug their
heading would generate, and most of that is deliberate:

* **Disambiguation.** Several headings share a title ("Tetrad Leg
  decomposition" appears once per apex leg), so the anchors must differ or
  they would collide.
* **Stable semantic ids.** `oversight-constitutional` marks the heading
  "Oversight"; `flourishing-measurement-family` marks "Measuring Flourishing".
  These are deliberate and are what other chapters cite.
* **Alias sets.** Two or more anchors stacked on one heading keep older links
  working across a rename.

None of those are defects. What this audit catches is narrower: a **single**
anchor on a numbered section whose number still matches the heading but whose
*name* no longer does — an id reading `345-chapter-eleven-floor-boundary` on a
heading that has since been retitled "3.4.5 Rights-Floor Boundary". Nothing
breaks, so no link audit sees it, but the anchor asserts something false about
where it points, and it is what a reader copies into the next cross-reference.

The corpus carries no such drift today: the baseline beside this file is empty
and the rule is enforced outright. It stays a baseline rather than a bare
assertion so a deliberate exception can be recorded and reviewed instead of
silently weakening the rule. Entries that no longer drift are reported as
stale, so the list cannot rot.

Rule ID: ANCHOR-HEADING-DRIFT-01
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from corpus_paths import binding_corpus_scope  # noqa: E402
from local_markdown_fragment_audit import github_slug  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
RULE = "ANCHOR-HEADING-DRIFT-01"
BASELINE_PATH = _TOOLS / "anchor_heading_drift_baseline.json"

ANCHOR_RE = re.compile(r'^<a id="([^"]+)"></a>\s*$')
HEADING_RE = re.compile(r"^#{1,6}\s+(.*?)\s*$")
NUMBERED_RE = re.compile(r"^(\d+(?:-\d+)*)-(.*)$")


@dataclass(frozen=True)
class Finding:
    file: str
    line: int
    anchor: str
    expected: str
    heading: str

    def key(self) -> str:
        return f"{self.file}#{self.anchor}"


def anchor_groups(text: str) -> list[tuple[int, list[str], str]]:
    """Return (line, anchor ids stacked together, heading text) triples."""
    lines = text.split("\n")
    groups: list[tuple[int, list[str], str]] = []
    index = 0
    while index < len(lines):
        if not ANCHOR_RE.match(lines[index]):
            index += 1
            continue
        ids: list[str] = []
        cursor = index
        while cursor < len(lines) and (
            ANCHOR_RE.match(lines[cursor]) or not lines[cursor].strip()
        ):
            match = ANCHOR_RE.match(lines[cursor])
            if match:
                ids.append(match.group(1))
            cursor += 1
        if cursor < len(lines):
            heading = HEADING_RE.match(lines[cursor])
            if heading:
                groups.append((index + 1, ids, heading.group(1)))
        index = cursor
    return groups


def scan(root: Path, scope: list[str]) -> list[Finding]:
    collected: list[tuple[str, int, list[str], str, str]] = []
    slug_counts: dict[str, int] = {}
    for rel_path in scope:
        path = root / rel_path
        if not path.is_file():
            continue
        for line, ids, heading in anchor_groups(path.read_text(encoding="utf-8")):
            slug = github_slug(heading)
            slug_counts[slug] = slug_counts.get(slug, 0) + 1
            collected.append((rel_path, line, ids, slug, heading))

    findings: list[Finding] = []
    for rel_path, line, ids, slug, heading in collected:
        if slug in ids:
            continue  # the heading's own slug is already reachable
        if slug_counts[slug] > 1:
            continue  # duplicate heading: the anchor must differ
        if len(ids) != 1:
            continue  # alias set: kept deliberately for link stability
        anchor = ids[0]
        anchor_parts = NUMBERED_RE.match(anchor)
        slug_parts = NUMBERED_RE.match(slug)
        if not anchor_parts or not slug_parts:
            continue  # unnumbered: a semantic id, not a section anchor
        if anchor_parts.group(1) != slug_parts.group(1):
            continue  # different section number: not a rename, leave it alone
        if anchor_parts.group(2) == slug_parts.group(2):
            continue
        findings.append(Finding(rel_path, line, anchor, slug, heading))
    return findings


def load_baseline() -> set[str]:
    if not BASELINE_PATH.is_file():
        return set()
    data = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
    return set(data.get("known_drift", []))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument(
        "--all",
        action="store_true",
        help="Report baselined drift too, as a backlog listing.",
    )
    parser.add_argument(
        "--write-baseline",
        action="store_true",
        help="Rewrite the baseline from the current tree.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    scope = binding_corpus_scope(root, include_support_docs=True)
    findings = scan(root, scope)

    if args.write_baseline:
        BASELINE_PATH.write_text(
            json.dumps(
                {
                    "rule": RULE,
                    "note": (
                        "Pre-existing anchor/heading drift. Shrink this list; "
                        "do not grow it. Regenerate with --write-baseline only "
                        "when removing entries."
                    ),
                    "known_drift": sorted(f.key() for f in findings),
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        print(f"Wrote {BASELINE_PATH.relative_to(root)} ({len(findings)} entries)")
        return 0

    baseline = load_baseline()
    current = {f.key() for f in findings}
    new = [f for f in findings if f.key() not in baseline]
    stale = sorted(baseline - current)

    if args.all:
        print(f"{RULE}: {len(findings)} drifted anchor(s) total")
        for finding in findings:
            flag = " " if finding.key() in baseline else "NEW"
            print(f"  {flag} {finding.file}:{finding.line}")
            print(f"        {finding.anchor}")
            print(f"     -> {finding.expected}   ({finding.heading})")

    if stale:
        print(
            f"FAIL: {len(stale)} baseline entr(ies) no longer drift — "
            "remove them with --write-baseline",
            file=sys.stderr,
        )
        for key in stale:
            print(f"  {key}", file=sys.stderr)
        return 1

    if new:
        print(f"FAIL: {len(new)} new anchor/heading drift ({RULE})", file=sys.stderr)
        for finding in new:
            print(
                f"  {finding.file}:{finding.line}: anchor "
                f"#{finding.anchor} no longer matches heading "
                f"{finding.heading!r} (expected #{finding.expected})",
                file=sys.stderr,
            )
        return 1

    print(
        f"PASS: {RULE} — no new anchor/heading drift "
        f"({len(baseline)} known, tracked in {BASELINE_PATH.name})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
