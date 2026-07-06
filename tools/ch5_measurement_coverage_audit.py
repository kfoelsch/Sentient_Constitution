#!/usr/bin/env python3
"""Audit MEAS-DEF seed/hierarchy sync and bidirectional Chapter Zero owner links."""

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
    MEASUREMENTS_RE,
    find_term_body,
)

CH00_FILE = "core_00_preamble.md"
SKIP_AIM_ROLES = frozenset({"aim_head"})
CLUSTER_ANCHOR_SUFFIXES = ("-cluster", "-semi-independent")

SECTION_RE = re.compile(r"^#### (3\.\d+ Measuring[^\n]+)$", re.MULTILINE)
CH5_LINK_RE = re.compile(r"\]\((core_05[^)#]+)(#([^)]+))?\)")
PRIMARY_OWNER_RE = re.compile(
    r"primary owner:\s*\[([^\]]+)\]\((core_05[^)#]+)#([^)]+)\)",
    re.IGNORECASE,
)
CH00_ANCHOR_RE = re.compile(r"core_00_preamble\.md#([a-z0-9-]+)")


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


def category_for_section(title: str, ch00_categories: dict[str, str]) -> str | None:
    section_num = title.split()[0]
    for cat, _anchor in ch00_categories.items():
        if cat.startswith(section_num + " "):
            return cat
    return None


def anchor_for_category(category: str, ch00_categories: dict[str, str]) -> str:
    return ch00_categories.get(category, "").lstrip("#")


def build_anchor_term_maps(
    hierarchy: dict, registry: dict
) -> tuple[dict[str, str], dict[str, str]]:
    by_anchor: dict[str, str] = {}
    by_term: dict[str, str] = {}
    for row in hierarchy.get("entries", []):
        anchor = row.get("anchor", "").lstrip("#")
        term = row.get("term")
        if anchor and term:
            by_anchor[anchor] = term
            by_term[term] = anchor
    for entry in registry.get("definitions", []):
        anchor = entry.get("anchor", "").lstrip("#")
        term = entry.get("term")
        if anchor and term:
            by_anchor.setdefault(anchor, term)
            by_term.setdefault(term, anchor)
    return by_anchor, by_term


def resolve_anchor(anchor: str, by_anchor: dict[str, str]) -> str | None:
    if anchor in by_anchor:
        return anchor
    if anchor.endswith("-constitutional"):
        base = anchor[: -len("-constitutional")]
        if base in by_anchor:
            return base
    for candidate, _term in by_anchor.items():
        if candidate == anchor or candidate == f"{anchor}-constitutional":
            return candidate
        if anchor == f"{candidate}-constitutional":
            return candidate
    return None


def is_cluster_anchor(anchor: str) -> bool:
    return any(anchor.endswith(suffix) for suffix in CLUSTER_ANCHOR_SUFFIXES)


def ch00_measurement_sections(root: Path, ch00_categories: dict[str, str]) -> dict[str, dict]:
    text = (root / CH00_FILE).read_text(encoding="utf-8")
    start = text.find("#### 3.1 Measuring")
    end = text.find("### 4. Governance and Stewardship")
    body = text[start:end] if start != -1 and end != -1 else text

    sections: dict[str, dict] = {}
    matches = list(SECTION_RE.finditer(body))
    for idx, match in enumerate(matches):
        title = match.group(1)
        section_start = match.end()
        section_end = matches[idx + 1].start() if idx + 1 < len(matches) else len(body)
        section_text = body[section_start:section_end]
        category = category_for_section(title, ch00_categories)
        if not category:
            continue
        linked_anchors: set[str] = set()
        for _file, _hash, anchor in CH5_LINK_RE.findall(section_text):
            if anchor:
                linked_anchors.add(anchor)
        primary_owners: list[tuple[str, str]] = []
        for term_label, _file, anchor in PRIMARY_OWNER_RE.findall(section_text):
            primary_owners.append((term_label.strip(), anchor))
        sections[category] = {
            "title": title,
            "anchor": anchor_for_category(category, ch00_categories),
            "linked_anchors": linked_anchors,
            "primary_owners": primary_owners,
        }
    return sections


def measurements_block(body: str) -> str:
    match = MEASUREMENTS_RE.search(body)
    if not match:
        return ""
    start = match.end()
    rest = body[start:]
    end_match = re.search(
        r"^\s*(<a id=\"[^\"]*-e\"></a>|- \*?\*?E\*?\*?:)",
        rest,
        re.MULTILINE,
    )
    return rest[: end_match.start()] if end_match else rest[:800]


def block_links_ch00_anchor(block: str, expected_anchor: str) -> bool:
    anchors = set(CH00_ANCHOR_RE.findall(block))
    return expected_anchor in anchors


def category_applies(category: str, seed_cat: str | None, hier_cats: list[str]) -> bool:
    if seed_cat == category:
        return True
    return category in hier_cats


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    seeds = load_json(root / args.seeds)
    registry = load_json(root / args.registry)
    hierarchy = load_json(root / args.hierarchy)
    ch00_categories = seeds.get("ch00_categories", {})

    hier_by_term = {row["term"]: row for row in hierarchy.get("entries", [])}
    by_anchor, _by_term = build_anchor_term_maps(hierarchy, registry)
    ch00_sections = ch00_measurement_sections(root, ch00_categories)

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

    for category, section in sorted(ch00_sections.items()):
        section_anchor = section["anchor"]
        for raw_anchor in sorted(section["linked_anchors"]):
            if is_cluster_anchor(raw_anchor):
                continue
            resolved = resolve_anchor(raw_anchor, by_anchor)
            if not resolved:
                findings.append(
                    f"Ch00 {category}: linked anchor #{raw_anchor} not found in hierarchy/registry"
                )
                continue
            term = by_anchor[resolved]
            seed = seeds.get("terms", {}).get(term)
            if not seed or seed.get("status") != "approved":
                findings.append(
                    f"Ch00 {category}: linked term {term} (#{raw_anchor}) lacks approved seed"
                )
                continue
            seed_cat = seed.get("ch00_category")
            hier_cats = hier_by_term.get(term, {}).get("ch00_measurement") or []
            if not category_applies(category, seed_cat, hier_cats):
                findings.append(
                    f"Ch00 {category}: linked term {term} not tagged for this measurement family"
                )
                continue
            located = find_term_body(root, term, registry)
            if not located:
                findings.append(f"Ch00 {category}: linked term {term} definition body not found")
                continue
            _source, body = located
            meas_block = measurements_block(body)
            if not meas_block:
                findings.append(f"Ch00 {category}: linked term {term} missing *Measurements:* block")
                continue
            owner_anchor = anchor_for_category(seed_cat or category, ch00_categories)
            if not block_links_ch00_anchor(meas_block, section_anchor) and not block_links_ch00_anchor(
                meas_block, owner_anchor
            ):
                findings.append(
                    f"Ch00 {category}: linked term {term} measurements block does not link "
                    f"#{section_anchor} or seed owner #{owner_anchor}"
                )

        for owner_label, owner_anchor in section["primary_owners"]:
            resolved = resolve_anchor(owner_anchor, by_anchor)
            if not resolved:
                findings.append(
                    f"Ch00 {category}: primary owner {owner_label!r} anchor #{owner_anchor} not in hierarchy/registry"
                )
                continue
            term = by_anchor[resolved]
            seed = seeds.get("terms", {}).get(term)
            if not seed or seed.get("status") != "approved":
                findings.append(f"Ch00 {category}: primary owner {term} lacks approved seed")
            elif seed.get("ch00_category") != category:
                findings.append(
                    f"Ch00 {category}: primary owner {term} seed category is {seed.get('ch00_category')!r}"
                )

    approved = sum(
        1 for meta in seeds.get("terms", {}).values() if meta.get("status") == "approved"
    )
    ch00_links = sum(
        1
        for section in ch00_sections.values()
        for anchor in section["linked_anchors"]
        if not is_cluster_anchor(anchor)
    )
    print(
        f"ch5-measurement-coverage-audit: {approved} approved seeds; "
        f"{ch00_links} Ch00 §3 leaf links checked"
    )
    if findings:
        for line in findings:
            print(f"  - {line}", file=sys.stderr)
        return 1
    print("ch5-measurement-coverage-audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
