#!/usr/bin/env python3
"""Emit human-readable MEAS-DEF rollout status grouped by Ch00 category."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from ch5_measurement_tier_audit import find_term_body, tier_checks  # noqa: E402

MEASUREMENTS_RE = re.compile(r"^\*Measurements:\*\s*$", re.MULTILINE)


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
    p.add_argument(
        "--output",
        default="doc_architecture/generated/measurement_rollout_status.md",
        help="Output markdown path.",
    )
    return p.parse_args()


def load_json(path: Path) -> dict:
    if not path.is_file():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def hierarchy_row(hierarchy: dict, term: str) -> dict:
    for row in hierarchy.get("entries", []):
        if row.get("term") == term:
            return row
    return {}


def render(root: Path, seeds: dict, registry: dict, hierarchy: dict) -> str:
    by_category: dict[str, list[tuple[str, dict, dict]]] = defaultdict(list)
    for term, meta in seeds.get("terms", {}).items():
        cat = meta.get("ch00_category", "uncategorized")
        by_category[cat].append((term, meta, hierarchy_row(hierarchy, term)))

    lines = [
        "# Measurement rollout status (MEAS-DEF-01)",
        "",
        "Auto-generated. Do not edit by hand.",
        "",
        f"Generated: {datetime.now(timezone.utc).replace(microsecond=0).isoformat()}",
        "",
        "Grouped by Chapter Zero measurement category. **Approved** terms must carry "
        "`*Measurements:*` and tier-aligned **E**/**C** per [doc_architecture.md](../doc_architecture.md) MEAS-DEF-01.",
        "",
    ]

    approved_total = sum(1 for m in seeds.get("terms", {}).values() if m.get("status") == "approved")
    approved_pass = 0

    for category in sorted(by_category.keys()):
        rows = by_category[category]
        lines.append(f"## {category}")
        lines.append("")
        lines.append("| Term | Status | Tier depth | Aim role | File | Has measurements | Audit |")
        lines.append("| --- | --- | --- | --- | --- | --- | --- |")
        for term, meta, hrow in sorted(rows, key=lambda item: item[0].casefold()):
            located = find_term_body(root, term, registry)
            has_meas = "—"
            audit = "—"
            if located:
                source_file, body = located
                has_meas = "yes" if MEASUREMENTS_RE.search(body) else "no"
                if meta.get("status") == "approved":
                    errs = tier_checks(body, meta.get("tier_depth", "full"))
                    audit = "pass" if not errs else "fail"
                    if not errs:
                        approved_pass += 1
            else:
                source_file = hrow.get("canonical_file", "—")
            aim_role = hrow.get("aim_role", "—")
            lines.append(
                f"| {term} | {meta.get('status', 'pending')} | {meta.get('tier_depth', '—')} | "
                f"{aim_role} | `{source_file}` | {has_meas} | {audit} |"
            )
        lines.append("")

    lines.insert(
        7,
        f"Approved progress: **{approved_pass}/{approved_total}** terms pass tier audit.",
    )
    lines.insert(8, "")
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    seeds = load_json(root / args.seeds)
    registry = load_json(root / args.registry)
    hierarchy = load_json(root / args.hierarchy)
    out = root / args.output
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render(root, seeds, registry, hierarchy), encoding="utf-8")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
