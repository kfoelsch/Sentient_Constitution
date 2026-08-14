#!/usr/bin/env python3
"""Four-layer alignment audit: principles, Def.*, oDef, and Articles.

Runs the Chapter One ↔ Chapter Five, Chapter One ↔ CJS-3, and Chapter 0/1 ↔
Chapter Six auditors in-process and writes a combined index plus each layer's
existing report / CSV / JSON artifacts.

Usage:
  python tools/alignment_audit.py --repo-root .
  python tools/alignment_audit.py --repo-root . --output-dir evidence/2026-08-13
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from collections import defaultdict
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from ch1_ch5_alignment_audit import AlignmentAuditor  # noqa: E402
from ch1_ch6_alignment_audit import Ch1Ch6AlignmentAuditor  # noqa: E402
from ch1_cjs3_alignment_audit import Ch1Cjs3AlignmentAuditor  # noqa: E402
from definition_index import extract_ch5_term_cites  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".", help="Repository root.")
    parser.add_argument(
        "--output-dir",
        default=None,
        help="Evidence directory. Defaults to evidence/<date>.",
    )
    parser.add_argument(
        "--date",
        default=dt.date.today().isoformat(),
        help="Evidence date stamp, YYYY-MM-DD.",
    )
    return parser.parse_args()


def _write_index(
    output_dir: Path,
    date_stamp: str,
    ch5: AlignmentAuditor,
    cjs3: Ch1Cjs3AlignmentAuditor,
    ch6: Ch1Ch6AlignmentAuditor,
) -> Path:
    odef_by_principle: dict[str, list[str]] = defaultdict(list)
    for cluster in cjs3.clusters:
        for section in cluster.direct_ch1_refs + cluster.inferred_principles:
            if section == "linked":
                continue
            odef_by_principle[section].append(cluster.cluster_id)

    articles_by_principle: dict[str, list[str]] = defaultdict(list)
    articles_by_def: dict[str, list[str]] = defaultdict(list)
    articles_by_odef: dict[str, list[str]] = defaultdict(list)
    for article in ch6.articles:
        for section in article.direct_ch1_refs + article.inferred_ch1_basis:
            if section == "linked":
                continue
            articles_by_principle[section].append(article.article_id)
        for term in article.ch5_refs:
            articles_by_def[term.casefold()].append(article.article_id)
        for cite in article.odef_refs:
            articles_by_odef[cite].append(article.article_id)

    lines = [
        "# Alignment Audit Index",
        "",
        f"**Date:** {date_stamp}",
        "**Workflow:** ALIGNMENT_AUDIT",
        "**Layers:** principles · Def.* · oDef · Articles",
        "",
        "Structural trace and completeness only. Semantic adequacy is out of scope of this pass, not a gap count.",
        "",
        "## Inventory",
        "",
        "| Layer | Count |",
        "|---|---:|",
        f"| Principles (Preamble + Chapter One) | {len(ch5.ch1_principles)} |",
        f"| Chapter Five Def.* (including apex heads) | {len(ch5.ch5_definitions)} |",
        f"| CJS-3 oDef clusters | {len(cjs3.clusters)} |",
        f"| Chapter Six articles / subarticles | {len(ch6.articles)} |",
        "",
        "## Layer findings",
        "",
        "| Layer | Completeness / inventory | Accuracy / guideposts | Other review |",
        "|---|---:|---:|---:|",
        f"| Principles ↔ Def.* | {len(ch5.completeness_gaps)} | {len(ch5.accuracy_gaps)} | {len(ch5.coverage_gaps) + len(ch5.cluster_gaps)} |",
        f"| Principles ↔ oDef | {len(cjs3.gaps['inventory']) + len(cjs3.gaps['missing_anchor'])} | {len(cjs3.gaps['op_component_gap'])} | {len(cjs3.gaps['weak_trace']) + len(cjs3.gaps['owner_drift']) + len(cjs3.gaps['overreach'])} |",
        f"| Principles ↔ Articles | {sum(1 for f in ch6.findings if f.kind == 'missing_ch1_basis')} | — | {sum(1 for f in ch6.findings if f.kind != 'manual_review')} |",
        "",
        "## Principles",
        "",
        "| Section | Title | Def.* anchors | oDef clusters | Articles |",
        "|---|---|---|---|---|",
    ]
    for section, data in sorted(ch5.ch1_principles.items()):
        odefs = sorted(set(odef_by_principle.get(section, [])))
        articles = sorted(set(articles_by_principle.get(section, [])))
        lines.append(
            f"| {section} | {data['title']} | {', '.join(data['anchors']) or '—'} | "
            f"{', '.join(odefs) or '—'} | {', '.join(articles) or '—'} |"
        )

    lines.extend([
        "",
        "## Chapter Five Def.*",
        "",
        "| Term | Category | Guideposts | Principles | oDef | Articles |",
        "|---|---|---|---|---|---|",
    ])
    for term, data in sorted(ch5.ch5_definitions.items(), key=lambda item: item[0].casefold()):
        complete = data["has_o"] and data["has_m"] and data["has_c"]
        guide = "complete" if complete else "incomplete"
        articles = sorted(set(articles_by_def.get(term.casefold(), [])))
        lines.append(
            f"| {term} | {data['category']} | {guide} | "
            f"{', '.join(data['referenced_principles']) or '—'} | "
            f"{', '.join(data['odef_clusters']) or '—'} | "
            f"{', '.join(articles) or '—'} |"
        )

    lines.extend([
        "",
        "## CJS-3 oDef clusters",
        "",
        "| Cluster | Title | Guideposts | Chapter One basis | Chapter Five cites | Owner routing | Status |",
        "|---|---|---|---|---|---|---|",
    ])
    for cluster in cjs3.clusters:
        complete = all(not rule.missing for rule in cluster.rules) if cluster.rules else True
        ch5_cites = extract_ch5_term_cites(cluster.body)
        lines.append(
            f"| {cluster.cluster_id} | {cluster.title} | {'complete' if complete else 'incomplete'} | "
            f"{', '.join(cluster.direct_ch1_refs) or ', '.join(cluster.inferred_principles) or '—'} | "
            f"{', '.join(ch5_cites) or '—'} | "
            f"{', '.join(cluster.owner_refs[:4]) or '—'} | "
            f"{', '.join(cluster.classifications)} |"
        )

    lines.extend([
        "",
        "## Chapter Six Articles",
        "",
        "| Article | Title | Chapter One | Def.* | oDef | Status |",
        "|---|---|---|---|---|---|",
    ])
    for article in ch6.articles:
        lines.append(
            f"| {article.article_id} | {article.title} | "
            f"{', '.join(article.direct_ch1_refs) or ', '.join(article.inferred_ch1_basis) or '—'} | "
            f"{', '.join(article.ch5_refs) or '—'} | "
            f"{', '.join(article.odef_refs) or '—'} | "
            f"{', '.join(article.classifications)} |"
        )

    lines.extend([
        "",
        "## Per-layer artifacts",
        "",
        f"- `ch1_ch5_alignment_report_{date_stamp}.md`",
        f"- `ch1_cjs3_principle_alignment_report_{date_stamp}.md`",
        f"- `ch1_ch6_alignment_report_{date_stamp}.md`",
        "",
        "Unexpected orphan Def.* terms (operative Chapter One cite, no D/A/C widget) are coverage findings. Remaining unused cluster leaves and Preamble-only terms are expected non-anchors under NAV-DAC-12. Semantic adequacy of principle-to-article mapping is out of scope of ALIGNMENT_AUDIT.",
        "",
    ])

    path = output_dir / f"alignment_audit_index_{date_stamp}.md"
    path.write_text("\n".join(lines), encoding="utf-8")

    log_path = output_dir / f"alignment_audit_log_{date_stamp}.json"
    log_path.write_text(
        json.dumps(
            {
                "date": date_stamp,
                "workflow": "ALIGNMENT_AUDIT",
                "counts": {
                    "principles": len(ch5.ch1_principles),
                    "definitions": len(ch5.ch5_definitions),
                    "odef_clusters": len(cjs3.clusters),
                    "articles": len(ch6.articles),
                },
                "ch5_gaps": {
                    "completeness": len(ch5.completeness_gaps),
                    "accuracy": len(ch5.accuracy_gaps),
                    "coverage": len(ch5.coverage_gaps),
                    "cluster_integrity": len(ch5.cluster_gaps),
                },
                "cjs3_gaps": {key: len(items) for key, items in cjs3.gaps.items()},
                "ch6_status": ch6.status(),
                "ch6_findings": ch6._finding_counts(),
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    return path


def main() -> int:
    args = parse_args()
    root = Path(args.repo_root).resolve()
    output_dir = Path(args.output_dir) if args.output_dir else root / "evidence" / args.date
    if not output_dir.is_absolute():
        output_dir = root / output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    ch5 = AlignmentAuditor(root, timestamp=args.date)
    ch5.run_audit()
    ch5.write_outputs(output_dir)

    cjs3 = Ch1Cjs3AlignmentAuditor(root, timestamp=args.date)
    cjs3.run()
    cjs3.write_report(output_dir)
    cjs3.write_matrix(output_dir)
    cjs3.write_log(output_dir)

    ch6 = Ch1Ch6AlignmentAuditor(root, args.date)
    ch6.run()
    ch6.write_outputs(output_dir)

    index = _write_index(output_dir, args.date, ch5, cjs3, ch6)
    print("Four-layer alignment audit complete.")
    print(f"Index: {index}")
    print(f"Evidence written to: {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
