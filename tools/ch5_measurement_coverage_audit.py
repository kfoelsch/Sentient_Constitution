#!/usr/bin/env python3
"""Audit MEAS-DEF seed/hierarchy sync for Chapter Five measurement tiers."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SKIP_AIM_ROLES = frozenset({"aim_head"})


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
    return p.parse_args()


def load_json(path: Path) -> dict:
    if not path.is_file():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    seeds = load_json(root / args.seeds)
    registry = load_json(root / args.registry)
    hierarchy = load_json(root / args.hierarchy)

    hier_by_term = {row["term"]: row for row in hierarchy.get("entries", [])}
    findings: list[str] = []

    for term, meta in sorted(seeds.get("terms", {}).items()):
        if meta.get("status") != "approved":
            findings.append(f"{term}: seed status is not approved ({meta.get('status')})")
            continue
        row = hier_by_term.get(term)
        if not row:
            findings.append(f"{term}: approved seed missing from hierarchy index")
            continue
        seed_cat = meta.get("ch00_category")
        hier_cats = row.get("ch00_measurement") or []
        if seed_cat and hier_cats and seed_cat not in hier_cats:
            findings.append(
                f"{term}: seed ch00_category {seed_cat!r} not in hierarchy ch00_measurement {hier_cats}"
            )

    for term, row in sorted(hier_by_term.items()):
        if row.get("aim_role") in SKIP_AIM_ROLES:
            continue
        if not row.get("ch00_measurement"):
            continue
        seed = seeds.get("terms", {}).get(term)
        if not seed or seed.get("status") != "approved":
            findings.append(f"{term}: hierarchy leaf missing approved seed")

    approved = sum(
        1 for meta in seeds.get("terms", {}).values() if meta.get("status") == "approved"
    )
    print(f"ch5-measurement-coverage-audit: {approved} approved seeds checked")
    if findings:
        for line in findings:
            print(f"  - {line}", file=sys.stderr)
        return 1
    print("ch5-measurement-coverage-audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
