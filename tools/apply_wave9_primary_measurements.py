#!/usr/bin/env python3
"""Apply Wave 9 primary-only *Measurements:* blocks to residual Chapter Five definitions."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from ch5_measurement_tier_audit import (  # noqa: E402
    HEADING_RE,
    MEASUREMENTS_RE,
    extract_definition_body,
    find_term_body,
    tier_checks,
)
from ch5_paths import CH5_ALL  # noqa: E402

E_START_RE = re.compile(r'^\s*(<a id="[^"]*-e"></a>|- \*?\*?E\*?\*?:)')

CAT_META: dict[str, tuple[str, str, str]] = {
    "3.1 Threshold and scaling": (
        "§3.1 *Measuring Threshold and Scaling*",
        "#measuring-threshold-and-scaling",
        "threshold and scaling",
    ),
    "3.2 Flourishing": (
        "§3.2 *Measuring Flourishing*",
        "#measuring-flourishing",
        "flourishing",
    ),
    "3.3 Continuity": (
        "§3.3 *Measuring Continuity*",
        "#measuring-continuity",
        "continuity",
    ),
    "3.4 Participation": (
        "§3.4 *Measuring Participation*",
        "#measuring-participation",
        "participation",
    ),
    "3.5 Oversight": (
        "§3.5 *Measuring Oversight*",
        "#measuring-oversight",
        "oversight",
    ),
    "3.6 Accountability": (
        "§3.6 *Measuring Accountability*",
        "#measuring-accountability",
        "accountability",
    ),
    "3.7 Timeliness": (
        "§3.7 *Measuring Timeliness*",
        "#measuring-timeliness",
        "timeliness",
    ),
    "3.8 Constitutional performance": (
        "§3.8 *Measuring Constitutional Performance*",
        "#measuring-constitutional-performance",
        "constitutional performance",
    ),
}

TETRAD_LEG_LABEL = {
    "Participation": "participation",
    "Oversight": "oversight",
    "Accountability": "accountability",
    "Timeliness": "timeliness",
}


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", default=".", help="Repository root.")
    p.add_argument(
        "--seeds",
        default="tools/architecture/measurement_tier_seeds.json",
        help="Measurement tier seed path.",
    )
    p.add_argument(
        "--registry",
        default="ai_corpus/indexes/definition_registry.json",
        help="Definition registry JSON path.",
    )
    p.add_argument(
        "--hierarchy",
        default="doc_architecture/generated/definition_hierarchy.json",
        help="Hierarchy index JSON path.",
    )
    p.add_argument("--dry-run", action="store_true", help="Report only; do not write files.")
    return p.parse_args()


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sort_categories(categories: list[str]) -> list[str]:
    return sorted(categories, key=lambda c: CAT_META.get(c, ("", "", ""))[0])


def category_links(categories: list[str]) -> list[str]:
    links: list[str] = []
    for cat in sort_categories(categories):
        label, anchor, _ = CAT_META[cat]
        links.append(f"[Chapter Zero {label}](../core_00_preamble.md{anchor})")
    return links


def build_measurements_block(term: str, categories: list[str], aim_role: str) -> str:
    links = category_links(categories)
    if aim_role == "tetrad_leg_head":
        leg = TETRAD_LEG_LABEL.get(term, term.casefold())
        cat = sort_categories(categories)[0]
        label, anchor, _ = CAT_META[cat]
        primary = (
            f"- **Primary:** [Chapter Zero {label}](../core_00_preamble.md{anchor}) "
            f"— link-only rollup for the **{leg}** Tetrad leg; operative tiers on leaf primaries below. "
            "Progress: [measurement rollout status](doc_architecture/generated/measurement_rollout_status.md)."
        )
    elif len(links) == 1:
        _, _, short = CAT_META[sort_categories(categories)[0]]
        primary = (
            f"- **Primary:** {links[0]} — supporting measure under the {short} measurement family."
        )
    else:
        primary = (
            f"- **Primary:** {' and '.join(links)} "
            "— supporting measure where multiple measurement families co-apply."
        )
    return f"  - *Measurements:*\n\n  {primary}\n"


def find_heading_index(lines: list[str], term: str) -> int | None:
    for idx, raw in enumerate(lines):
        match = HEADING_RE.match(raw.strip())
        if match and match.group(1).strip() == term:
            return idx
    return None


def find_insert_line(lines: list[str], heading_idx: int) -> int | None:
    depth = len(lines[heading_idx].strip()) - len(lines[heading_idx].strip().lstrip("#"))
    e_line: int | None = None

    for i in range(heading_idx + 1, len(lines)):
        stripped = lines[i].strip()
        m2 = HEADING_RE.match(stripped)
        if m2 and len(m2.group(0)) - len(m2.group(0).lstrip("#")) <= depth:
            break
        if MEASUREMENTS_RE.match(stripped) or MEASUREMENTS_RE.match(lines[i]):
            return None
        if E_START_RE.match(stripped):
            if stripped.startswith("<a id="):
                continue
            e_line = i
            break

    return e_line


def patch_definition_text(text: str, term: str, block: str) -> tuple[str, bool]:
    lines = text.splitlines()
    heading_idx = find_heading_index(lines, term)
    if heading_idx is None:
        return text, False
    insert_at = find_insert_line(lines, heading_idx)
    if insert_at is None:
        return text, False
    new_lines = lines[: insert_at + 1] + block.splitlines() + lines[insert_at + 1 :]
    return "\n".join(new_lines) + ("\n" if text.endswith("\n") else ""), True


def locate_source_file(root: Path, term: str, registry: dict) -> Path | None:
    located = find_term_body(root, term, registry)
    if not located:
        return None
    return root / located[0]


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    seeds_path = root / args.seeds
    seeds = load_json(seeds_path)
    registry = load_json(root / args.registry)
    hierarchy = load_json(root / args.hierarchy)

    approved = set(seeds.get("terms", {}))
    file_cache: dict[Path, str] = {}
    patched_terms: list[str] = []
    skipped: list[str] = []

    for entry in hierarchy.get("entries", []):
        term = entry["term"]
        if term in approved:
            continue
        if entry.get("aim_role") == "aim_head":
            continue

        categories = entry.get("ch00_measurement") or []
        if not categories:
            skipped.append(f"{term}: no ch00_measurement")
            continue

        source = locate_source_file(root, term, registry)
        if source is None:
            skipped.append(f"{term}: source not found")
            continue

        if source not in file_cache:
            file_cache[source] = source.read_text(encoding="utf-8")

        block = build_measurements_block(term, categories, entry.get("aim_role", ""))
        updated, ok = patch_definition_text(file_cache[source], term, block)
        if not ok:
            skipped.append(f"{term}: could not insert (missing O or already has measurements)")
            continue
        file_cache[source] = updated
        patched_terms.append(term)

        primary_cat = sort_categories(categories)[0]
        seeds.setdefault("terms", {})[term] = {
            "ch00_category": primary_cat,
            "tier_depth": "primary_only",
            "status": "approved",
        }

    if not args.dry_run:
        for path, content in file_cache.items():
            path.write_text(content, encoding="utf-8")
        seeds_path.write_text(json.dumps(seeds, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    # Verify patched terms pass tier audit
    failures: list[str] = []
    for term in patched_terms:
        located = find_term_body(root, term, registry)
        if not located:
            failures.append(f"{term}: body missing after patch")
            continue
        _, body = located
        errs = tier_checks(body, "primary_only")
        if errs:
            failures.append(f"{term}: " + "; ".join(errs))

    print(f"wave9-primary-measurements: patched {len(patched_terms)} definitions")
    if skipped:
        print(f"  skipped {len(skipped)}", file=sys.stderr)
        for line in skipped[:20]:
            print(f"    - {line}", file=sys.stderr)
        if len(skipped) > 20:
            print(f"    ... and {len(skipped) - 20} more", file=sys.stderr)
    if failures:
        for line in failures:
            print(f"  - {line}", file=sys.stderr)
        return 1
    if args.dry_run:
        print("(dry run — no files written)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
