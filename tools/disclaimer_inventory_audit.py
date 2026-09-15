#!/usr/bin/env python3
"""DISC-INV-01: inventory disclaimer / negative-scope clauses in Chapter Five.

Classifies recurring disclaimer text by theme, proposes canonical homes and
thin/fold/keep actions, and emits markdown + JSON reports for editorial waves.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from ch5_paths import CH5_ALL  # noqa: E402

HEADING_RE = re.compile(r"^(#{4,5})\s+(.+)$")
OEC_START_RE = re.compile(r"^- (O|E|C):\s*(.*)$")
THEMES_PATH = Path(__file__).resolve().parent / "architecture" / "disclaimer_themes.json"
DEFAULT_THEMES = "tools/architecture/disclaimer_themes.json"
DEFAULT_MD = "doc_architecture/generated/disclaimer_inventory.md"
DEFAULT_JSON = "doc_architecture/generated/disclaimer_inventory.json"


@dataclass
class Theme:
    id: str
    label: str
    patterns: list[str]
    canonical_home: str
    default_action: str
    notes: str
    canonical_terms: list[str] = field(default_factory=list)
    compiled: list[re.Pattern[str]] = field(repr=False, default_factory=list)


@dataclass
class Hit:
    file: str
    line: int
    term: str
    component: str
    theme_id: str
    theme_label: str
    action: str
    canonical_home: str
    excerpt: str
    pattern: str


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", default=".", help="Repository root.")
    p.add_argument(
        "--themes",
        default=DEFAULT_THEMES,
        help="Disclaimer theme JSON path (under --root).",
    )
    p.add_argument(
        "--output",
        default=DEFAULT_MD,
        help="Markdown report output path (under --root).",
    )
    p.add_argument(
        "--json-output",
        default=DEFAULT_JSON,
        help="JSON report output path (under --root).",
    )
    p.add_argument(
        "--max-excerpt",
        type=int,
        default=220,
        help="Max characters for excerpt snippets.",
    )
    return p.parse_args()


def load_themes(path: Path) -> list[Theme]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    themes: list[Theme] = []
    for row in raw.get("themes", []):
        compiled = [re.compile(pat, re.IGNORECASE) for pat in row["patterns"]]
        themes.append(
            Theme(
                id=row["id"],
                label=row["label"],
                patterns=row["patterns"],
                canonical_home=row["canonical_home"],
                default_action=row["default_action"],
                notes=row["notes"],
                canonical_terms=row.get("canonical_terms", []),
                compiled=compiled,
            )
        )
    return themes


def clip(text: str, limit: int) -> str:
    text = re.sub(r"\s+", " ", text.strip())
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def in_corpus_placement_block(lines: list[str], line_idx: int) -> bool:
    """True when line_idx sits inside a Corpus placement <details> block."""
    open_details = 0
    for i in range(line_idx):
        low = lines[i].lower()
        if "<details>" in low:
            open_details += 1
        if "</details>" in low:
            open_details = max(0, open_details - 1)
    if open_details <= 0:
        return False
    # Walk back to nearest <summary> for placement label.
    for j in range(line_idx, max(-1, line_idx - 40), -1):
        if "corpus placement" in lines[j].lower():
            return True
    return False


def collect_oec_blocks(lines: list[str]) -> list[tuple[int, str, str, str]]:
    """Return (line_no, term, component, text) for each O/E/C block."""
    blocks: list[tuple[int, str, str, str]] = []
    current_term = ""
    i = 0
    while i < len(lines):
        raw = lines[i]
        stripped = raw.strip()
        hm = HEADING_RE.match(stripped)
        if hm:
            current_term = hm.group(2).strip()
            i += 1
            continue

        m = OEC_START_RE.match(stripped)
        if not m:
            i += 1
            continue

        component = m.group(1)
        parts = [m.group(2)]
        start_line = i + 1
        j = i + 1
        while j < len(lines):
            nxt = lines[j]
            nst = nxt.strip()
            if not nst:
                j += 1
                continue
            if HEADING_RE.match(nst):
                break
            if OEC_START_RE.match(nst):
                break
            if "*Measurements:*" in nst and component == "O":
                break
            if nst == "---":
                break
            if nst.startswith("<details>"):
                break
            if nst.startswith("<a id=") and not parts[-1]:
                j += 1
                continue
            parts.append(nst)
            j += 1

        text = " ".join(parts)
        if text and not in_corpus_placement_block(lines, i):
            blocks.append((start_line, current_term, component, text))
        i = j
    return blocks


def match_themes(text: str, themes: list[Theme]) -> list[tuple[Theme, str]]:
    found: list[tuple[Theme, str]] = []
    for theme in themes:
        for pat, compiled in zip(theme.patterns, theme.compiled, strict=True):
            if compiled.search(text):
                found.append((theme, pat))
                break
    return found


def scan_file(path: Path, themes: list[Theme], max_excerpt: int) -> list[Hit]:
    rel = path.name
    lines = path.read_text(encoding="utf-8").splitlines()
    hits: list[Hit] = []
    for line_no, term, component, text in collect_oec_blocks(lines):
        for theme, pattern in match_themes(text, themes):
            if theme.default_action == "exclude":
                continue
            action = theme.default_action
            if term in theme.canonical_terms:
                action = "canonical"
            hits.append(
                Hit(
                    file=rel,
                    line=line_no,
                    term=term or "(no heading)",
                    component=component,
                    theme_id=theme.id,
                    theme_label=theme.label,
                    action=action,
                    canonical_home=theme.canonical_home,
                    excerpt=clip(text, max_excerpt),
                    pattern=pattern,
                )
            )
    return hits


def duplicate_clusters(hits: list[Hit]) -> list[dict]:
    """Terms where the same theme appears on multiple O/E/C components."""
    by_term_theme: dict[tuple[str, str], set[str]] = defaultdict(set)
    for h in hits:
        key = (h.term, h.theme_id)
        by_term_theme[key].add(h.component)
    rows = []
    for (term, theme_id), components in sorted(by_term_theme.items()):
        if len(components) < 2:
            continue
        rows.append(
            {
                "term": term,
                "theme_id": theme_id,
                "components": sorted(components),
            }
        )
    return rows


def render_markdown(
    hits: list[Hit],
    themes: list[Theme],
    dupes: list[dict],
    root: Path,
) -> str:
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    theme_counts = Counter(h.theme_id for h in hits)
    action_counts = Counter(h.action for h in hits)
    file_counts = Counter(h.file for h in hits)
    component_counts = Counter(h.component for h in hits)

    thin_candidates = [h for h in hits if h.action == "thin"]
    review_candidates = [h for h in hits if h.action == "review"]
    keep_candidates = [h for h in hits if h.action in {"keep", "canonical"}]
    canonical_hits = [h for h in hits if h.action == "canonical"]

    lines = [
        "# Disclaimer inventory (DISC-INV-01)",
        "",
        "Auto-generated. Do not edit by hand.",
        "",
        f"Generated: {now}",
        "",
        "Scopes **Chapter Five** band and aim files. Classifies disclaimer / "
        "negative-scope clauses on **O**, **E**, and **C** components using "
        "[tools/architecture/disclaimer_themes.json](../tools/architecture/disclaimer_themes.json).",
        "",
        "Editorial model: **safe redundancy** = one canonical exposition + pointers "
        "(see [doc_architecture.md](../doc_architecture.md) §12).",
        "",
        "## Summary",
        "",
        f"- **Total hits (actionable):** {len(hits)}",
        f"- **Thin candidates:** {len(thin_candidates)}",
        f"- **Review candidates:** {len(review_candidates)}",
        f"- **Keep (local boundary + canonical homes):** {len(keep_candidates)}",
        f"- **Canonical exposition (do not thin):** {len(canonical_hits)}",
        f"- **Same-theme duplicates across O/E/C (terms):** {len(dupes)}",
        "",
        "### By recommended action",
        "",
        "| Action | Count | Meaning |",
        "| --- | ---: | --- |",
        "| thin | "
        f"{action_counts.get('thin', 0)} | Replace with Trace read-with / single C line |",
        "| review | "
        f"{action_counts.get('review', 0)} | Triage per term — may stay local |",
        "| keep | "
        f"{action_counts.get('keep', 0)} | Term-pair or jurisdictional — do not fold |",
        "| canonical | "
        f"{action_counts.get('canonical', 0)} | Canonical home for theme — retain |",
        "",
        "### By O/E/C component",
        "",
        "| Component | Hits |",
        "| --- | ---: |",
    ]
    for comp in ("O", "E", "C"):
        lines.append(f"| {comp} | {component_counts.get(comp, 0)} |")

    lines.extend(
        [
            "",
            "### By source file",
            "",
            "| File | Hits |",
            "| --- | ---: |",
        ]
    )
    for file_name, count in file_counts.most_common():
        lines.append(f"| {file_name} | {count} |")

    lines.extend(["", "### By theme family", "", "| Theme | Hits | Default action | Canonical home |", "| --- | ---: | --- | --- |"])
    theme_by_id = {t.id: t for t in themes}
    for theme_id, count in theme_counts.most_common():
        t = theme_by_id[theme_id]
        home = clip(t.canonical_home, 80)
        lines.append(f"| {t.label} | {count} | {t.default_action} | {home} |")

    lines.extend(
        [
            "",
            "## Intra-entry redundancy (same theme, multiple components)",
            "",
            "Highest-yield thinning: drop duplicate theme on secondary components when "
            "one enforceable **C** line or principle-layer pointer remains.",
            "",
            "| Term | Theme | Components |",
            "| --- | --- | --- |",
        ]
    )
    if not dupes:
        lines.append("| — | — | — |")
    else:
        for row in dupes[:40]:
            t = theme_by_id.get(row["theme_id"])
            label = t.label if t else row["theme_id"]
            comps = ", ".join(row["components"])
            lines.append(f"| {row['term']} | {label} | {comps} |")
        if len(dupes) > 40:
            lines.append(f"| … | … | ({len(dupes) - 40} more) |")

    lines.extend(["", "## Thin candidates (sample)", "", "| File | Line | Term | Comp | Theme | Excerpt |", "| --- | ---: | --- | --- | --- | --- |"])
    for h in thin_candidates[:35]:
        lines.append(
            f"| {h.file} | {h.line} | {clip(h.term, 40)} | {h.component} | "
            f"{h.theme_id} | {clip(h.excerpt, 100)} |"
        )
    if len(thin_candidates) > 35:
        lines.append(f"| … | … | … | … | … | ({len(thin_candidates) - 35} more thin hits) |")

    lines.extend(
        [
            "",
            "## Suggested editorial waves",
            "",
            "1. **Wave A — Global integrity + proxy** (`global_integrity_negative`, `proxy_metrics`, "
            "`instrumental_only`, `symbolic_participation`): canonicalize in "
            "`core_01_c_stewardship_capacity_principles.md` §11; thin aim heads and cluster O lines.",
            "2. **Wave B — Layer separation** (`layer_separation`, `not_substitute`, `pointer_disclaimer`): "
            "one Ch00/Ch05i exposition + Trace pointers.",
            "3. **Wave C — Review queue** (`scope_exclusion`, `anti_formalism`): per-term triage; "
            "keep evasion blocks on gamed terms.",
            "4. **Wave D — Keep** (`neighbor_disambiguation`, `rights_floor_jurisdiction`): "
            "retain local O boundaries; optional standard Trace boilerplate only.",
            "",
            "## Theme reference",
            "",
        ]
    )
    for t in themes:
        if t.default_action == "exclude":
            continue
        lines.append(f"### {t.id}")
        lines.append("")
        lines.append(f"- **Label:** {t.label}")
        lines.append(f"- **Action:** {t.default_action}")
        lines.append(f"- **Canonical home:** {t.canonical_home}")
        lines.append(f"- **Notes:** {t.notes}")
        lines.append(f"- **Patterns:** {', '.join(f'`{p}`' for p in t.patterns)}")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append(f"Regenerate: `make disclaimer-inventory` (from `{root.name}`).")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    themes = load_themes(root / args.themes)

    all_hits: list[Hit] = []
    for rel in CH5_ALL:
        path = root / rel
        if not path.is_file():
            print(f"skip missing: {rel}", file=sys.stderr)
            continue
        file_hits = scan_file(path, themes, args.max_excerpt)
        all_hits.extend(file_hits)
        print(f"{rel}: {len(file_hits)} hits")

    dupes = duplicate_clusters(all_hits)

    md_path = root / args.output
    json_path = root / args.json_output
    md_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.parent.mkdir(parents=True, exist_ok=True)

    md_path.write_text(render_markdown(all_hits, themes, dupes, root), encoding="utf-8")
    payload = {
        "generated": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "total_hits": len(all_hits),
        "by_theme": dict(Counter(h.theme_id for h in all_hits)),
        "by_action": dict(Counter(h.action for h in all_hits)),
        "by_file": dict(Counter(h.file for h in all_hits)),
        "duplicate_clusters": dupes,
        "hits": [asdict(h) for h in all_hits],
    }
    json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    thin = sum(1 for h in all_hits if h.action == "thin")
    review = sum(1 for h in all_hits if h.action == "review")
    keep = sum(1 for h in all_hits if h.action == "keep")
    canonical = sum(1 for h in all_hits if h.action == "canonical")
    print(
        f"DISC-INV-01: {len(all_hits)} hits "
        f"(thin={thin}, review={review}, keep={keep}, canonical={canonical}, dup_terms={len(dupes)})"
    )
    print(f"Wrote {md_path.relative_to(root)}")
    print(f"Wrote {json_path.relative_to(root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
