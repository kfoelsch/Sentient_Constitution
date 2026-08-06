#!/usr/bin/env python3
"""Migrate Chapter Five dependent-cluster IDs from §3.x to Def.{band}{n}.

Retires bare §3.2–§3.16 cluster numbers and corrupted Chapter One §8.x
cluster cites. Title-gates replacements so real Chapter One / Seven / Eight
section cites are not rewritten.

  python3 tools/ch5_def_cluster_id_migration.py [--dry-run]
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# old §3.x → (Def ID, title suffix as used in #### headings)
CLUSTER_MAP: dict[str, tuple[str, str]] = {
    "3.2": ("Def.O1", "Transparency, Auditability, and Verification"),
    "3.3": ("Def.O2", "Truth and Epistemic Integrity"),
    "3.5": ("Def.P1", "Animal Life, Sentient Life, and Sentience Status"),
    "3.6": ("Def.P2", "Binding Stakeholder Choice"),
    "3.7": (
        "Def.P3",
        "Self-Determination, Meaningful Agency, Expression, Educational Agency, and Volitional Integrity",
    ),
    "3.8": (
        "Def.A1",
        "Collective Harm Boundary, Harm, and Harassment and Bullying",
    ),
    "3.9": ("Def.A2", "Forum Families and Dispute Routing"),
    "3.10": ("Def.A3", "Standing State, Contribution, and Violation"),
    "3.11": (
        "Def.A4",
        "Use of Force, Autonomous Coercion, Autonomous Lethal Systems, and Weapons of Mass Harm",
    ),
    "3.12": (
        "Def.C1",
        "Labor and Economic Floor: Compensation, Organization, Safe Conditions, Leisure, and Creative Work",
    ),
    "3.13": (
        "Def.C2",
        "Stewardship, Governance Discipline, and Shared-System Capacity",
    ),
    "3.14": ("Def.C3", "Privacy (Informational) — peer-level cluster head"),
    "3.15": ("Def.C4", "Trust and Trustworthiness"),
    "3.16": ("Def.I1", "Corpus and Authority Stack"),
}

# Distinctive title starts used to gate cite rewrites (avoid Ch1 §3.x collisions).
TITLE_GATE: dict[str, str] = {
    "3.2": r"Transparency",
    "3.3": r"Truth and Epistemic",
    "3.5": r"Animal Life",
    "3.6": r"Binding Stakeholder",
    "3.7": r"Self-Determination",
    "3.8": r"Collective Harm",
    "3.9": r"Forum Families",
    "3.10": r"Standing State",
    "3.11": r"Use of Force",
    "3.12": r"Labor and Economic",
    "3.13": r"Stewardship",
    "3.14": r"Privacy \(Informational\)",
    "3.15": r"Trust and Trustworthiness",
    "3.16": r"Corpus(?: and|,) Authority",
}

# Semi-independent topic groups that picked up bogus numbered cites.
# Strip the bogus prefix only; leave the existing title/markup intact.
SEMI_INDEPENDENT_PREFIXES = [
    "Chapter Five Chapter One §8.20 ",
    "Chapter Five Chapter One §8.22 ",
    "Chapter Five Chapter One §8.25 ",
    "Chapter Five Chapter One §8.27 ",
    "§3.32 ",
]

BAND_FILES = {
    "core_05_band_oversight.md",
    "core_05_band_participation.md",
    "core_05_band_accountability.md",
    "core_05_band_continuity.md",
    "core_05_band_integrative.md",
    "core_05__definitions_home.md",
}

CH5_MAP_FILES = BAND_FILES | {
    "core_05_apex_oversight_leg.md",
    "core_05_apex_participation_leg.md",
    "core_05_apex_accountability_leg.md",
    "core_05_apex_continuity_aim.md",
    "core_05_apex_flourishing_aim.md",
    "core_05_apex_timeliness_leg.md",
    "core_05_band_performance.md",
    "README.md",
    "doc_architecture.md",
}

OPERATIVE_GLOBS = [
    "core_*.md",
    "corpus_*/**/*.md",
    "corpus_*.md",
    "doc_architecture.md",
    "README.md",
]

SKIP_DIR_PARTS = {
    "archive",
    "evidence",
    "implementation",
    "node_modules",
    ".git",
    "ai_corpus",
}


def iter_targets(root: Path) -> list[Path]:
    files: list[Path] = []
    for pattern in OPERATIVE_GLOBS:
        for path in root.glob(pattern):
            if not path.is_file():
                continue
            if any(part in SKIP_DIR_PARTS for part in path.parts):
                continue
            files.append(path)
    seen: set[Path] = set()
    out: list[Path] = []
    for path in files:
        if path not in seen:
            seen.add(path)
            out.append(path)
    return out


def replace_cluster_cites(text: str, *, rewrite_headings: bool = False) -> str:
    items = sorted(CLUSTER_MAP.items(), key=lambda kv: -len(kv[0]))

    for old, (new, _title) in items:
        gate = TITLE_GATE[old]
        old8 = old.replace("3.", "8.")

        if rewrite_headings:
            text = text.replace(f"#### {old} ", f"#### {new} ")
            # Directory / bold keys that open with the bare number + matching title
            text = re.sub(rf"\[{re.escape(old)}\s+(?={gate})", f"[{new} ", text)
            text = re.sub(rf"\*\*{re.escape(old)}\s+(?={gate})", f"**{new} ", text)

        # Chapter Five §3.x — title-gated when a title follows; bare meta cites otherwise.
        text = re.sub(
            rf"Chapter Five §{re.escape(old)}(?=\s+\*?{gate})",
            f"**{new}**",
            text,
        )
        text = re.sub(
            rf"Chapter Five §{re.escape(old)}(?=[\s)*\],.;:]|$)",
            f"**{new}**",
            text,
        )

        # Title-gated cluster pointers (with or without Chapter Five / Chapter One).
        # Keep an existing opening italic marker so "[… §3.2 *Title*]" → "[Def.O1 *Title*]".
        for num in (old, old8):
            text = re.sub(
                rf"\[(?:Chapter Five )?(?:Chapter One )?§{re.escape(num)}\s+(?=\*?{gate})",
                f"[{new} ",
                text,
            )
            text = re.sub(
                rf"\*\*(?:Chapter Five )?(?:Chapter One )?§{re.escape(num)}\s+(?=\*?{gate})",
                f"**{new} ",
                text,
            )
            text = re.sub(
                rf"(?<![.\w])(?:Chapter Five )?(?:Chapter One )?§{re.escape(num)}(?=\s+\*{gate})",
                new,
                text,
            )
            text = re.sub(
                rf"Chapter Five Chapter One §{re.escape(num)}(?=\s+\*{gate})",
                f"**{new}**",
                text,
            )

        text = re.sub(rf"§{re.escape(old)} cluster\b", f"**{new}** cluster", text)
        text = re.sub(
            rf"\bcluster {re.escape(old)}\b",
            f"**{new}**",
            text,
            flags=re.IGNORECASE,
        )

    # Semi-independent: strip bogus prefixes only.
    text = text.replace(
        "Chapter Five Chapter One §8.12 *Constitutional Contract Layer",
        "*Constitutional Contract Layer",
    )
    for prefix in SEMI_INDEPENDENT_PREFIXES:
        text = text.replace(prefix, "")

    range_replacements = [
        (r"Chapter One §8\.2–§3\.3", "**Def.O1–Def.O2**"),
        (r"§3\.2–§3\.3", "**Def.O1–Def.O2**"),
        (r"§3\.5–§3\.7", "**Def.P1–Def.P3**"),
        (r"§3\.8–Chapter One §8\.11", "**Def.A1–Def.A4**"),
        (r"Chapter One §3\.8–§8\.11", "**Def.A1–Def.A4**"),
        (r"§3\.8–§3\.11", "**Def.A1–Def.A4**"),
        (r"Chapter One §8\.12–Chapter One §8\.15", "**Def.C1–Def.C4**"),
        (r"§3\.12–§3\.15", "**Def.C1–Def.C4**"),
        # Bare Chapter One §8.16 only when it is the Integrative cluster range cell /
        # map phrase — require trailing end or punctuation, not principle subsections.
        (r"\*\*Chapter One §8\.16\*\*", "**Def.I1**"),
        (r"§3\.2–§3\.16", "**Def.O1–Def.I1**"),
        (
            r"Numbered clusters \*\*§3\.2–§3\.16\*\*",
            "Dependent clusters **Def.O1–Def.I1**",
        ),
        (
            r"numbered clusters \*\*§3\.2–§3\.16\*\*",
            "dependent clusters **Def.O1–Def.I1**",
        ),
        (
            r"renumbers §3 dependent clusters \*\*§3\.2–§3\.16\*\*",
            "assigns dependent clusters **Def.O1–Def.I1**",
        ),
        (r"\| §3 cluster range \|", "| **Def.** cluster range |"),
        (r"§3 cluster range", "**Def.** cluster range"),
    ]
    for pattern, replacement in range_replacements:
        text = re.sub(pattern, replacement, text)

    text = text.replace("****", "**")
    text = re.sub(r"\*\*\*\*([^*]+)\*\*\*\*", r"**\1**", text)
    text = re.sub(r"\*\*\*([^*]+)\*\*\*", r"**\1**", text)
    return text


def update_directory_clusters(text: str) -> str:
    if "#### Clusters A-Z" not in text:
        return text

    rows = [
        (
            "Def.P1",
            "Animal Life, Sentient Life, and Sentience Status",
            "core_05_band_participation.md#animal-life-sentient-life-and-sentience-status-cluster",
        ),
        (
            "Def.P2",
            "Binding Stakeholder Choice",
            "core_05_band_participation.md#binding-stakeholder-choice-cluster",
        ),
        (
            "Def.A1",
            "Collective Harm Boundary, Harm, and Harassment and Bullying",
            "core_05_band_accountability.md#collective-harm-boundary-and-harm-cluster",
        ),
        (
            "Def.I1",
            "Corpus and Authority Stack",
            "core_05_band_integrative.md#corpus-authority-stack-supremacy-and-enforceability-cluster",
        ),
        (
            "Def.A2",
            "Forum Families and Dispute Routing",
            "core_05_band_accountability.md#forum-families-and-dispute-routing-cluster",
        ),
        (
            "Def.C1",
            "Labor and Economic Floor: Compensation, Organization, Safe Conditions, Leisure, and Creative Work",
            "core_05_band_continuity.md#labor-and-economic-floor-cluster",
        ),
        (
            "Def.C3",
            "Privacy (Informational) — peer-level cluster head",
            "core_05_band_continuity.md#privacy-informational-cluster",
        ),
        (
            "Def.P3",
            "Self-Determination, Meaningful Agency, Expression, Educational Agency, and Volitional Integrity",
            "core_05_band_participation.md#self-determination-and-meaningful-agency-cluster",
        ),
        (
            "Def.A3",
            "Standing State, Contribution, and Violation",
            "core_05_band_accountability.md#standing-state-contribution-and-violation-cluster",
        ),
        (
            "Def.C2",
            "Stewardship, Governance Discipline, and Shared-System Capacity",
            "core_05_band_continuity.md#stewardship-governance-discipline-and-shared-system-capacity-cluster",
        ),
        (
            "Def.O1",
            "Transparency, Auditability, and Verification",
            "core_05_band_oversight.md#transparency-auditability-and-verification-cluster",
        ),
        (
            "Def.C4",
            "Trust and Trustworthiness",
            "core_05_band_continuity.md#trust-and-trustworthiness-cluster",
        ),
        (
            "Def.O2",
            "Truth and Epistemic Integrity",
            "core_05_band_oversight.md#truth-and-epistemic-integrity-cluster",
        ),
        (
            "Def.A4",
            "Use of Force, Autonomous Coercion, Autonomous Lethal Systems, and Weapons of Mass Harm",
            "core_05_band_accountability.md#use-of-force-autonomous-coercion-and-mass-harm-cluster",
        ),
    ]
    rows_sorted = sorted(rows, key=lambda r: r[1].casefold())
    new_block = "\n".join(f"- [{cid} {title}]({href})" for cid, title, href in rows_sorted)
    pattern = re.compile(
        r"(#### Clusters A-Z\n\n)(.*?)(\n\n</details>)",
        re.DOTALL,
    )
    return pattern.sub(rf"\1{new_block}\3", text, count=1)


def update_band_tables(text: str, path: Path) -> str:
    tables = {
        "core_05_band_oversight.md": [
            ("**Def.O1**", "Transparency, Auditability, and Verification"),
            ("**Def.O2**", "Truth and Epistemic Integrity"),
        ],
        "core_05_band_participation.md": [
            ("**Def.P1**", "Animal Life, Sentient Life, and Sentience Status"),
            ("**Def.P2**", "Binding Stakeholder Choice"),
            (
                "**Def.P3**",
                "Self-Determination, Meaningful Agency, Expression, Educational Agency, and Volitional Integrity",
            ),
        ],
        "core_05_band_accountability.md": [
            (
                "**Def.A1**",
                "Collective Harm Boundary, Harm, and Harassment and Bullying",
            ),
            ("**Def.A2**", "Forum Families and Dispute Routing"),
            ("**Def.A3**", "Standing State, Contribution, and Violation"),
            (
                "**Def.A4**",
                "Use of Force, Autonomous Coercion, Autonomous Lethal Systems, and Weapons of Mass Harm",
            ),
        ],
        "core_05_band_continuity.md": [
            (
                "**Def.C1**",
                "Labor and Economic Floor: Compensation, Organization, Safe Conditions, Leisure, and Creative Work",
            ),
            (
                "**Def.C2**",
                "Stewardship, Governance Discipline, and Shared-System Capacity",
            ),
            ("**Def.C3**", "Privacy (Informational) — peer-level cluster head"),
            ("**Def.C4**", "Trust and Trustworthiness"),
        ],
        "core_05_band_integrative.md": [
            ("**Def.I1**", "Corpus and Authority Stack"),
        ],
    }
    rows = tables.get(path.name)
    if not rows:
        return text
    new_table = "| Cluster | Section |\n|---|---|\n" + "\n".join(
        f"| {cid} | {title} |" for cid, title in rows
    )
    pattern = re.compile(
        r"\| Cluster \| Section \|\n\|---\|---\|\n(?:\|.*\|\n)+",
        re.MULTILINE,
    )
    if pattern.search(text):
        text = pattern.sub(new_table + "\n", text, count=1)
    return text


def add_def_alias_anchors(text: str, path: Path) -> str:
    if path.name not in BAND_FILES - {"core_05__definitions_home.md"}:
        return text
    for _old, (new, _title) in CLUSTER_MAP.items():
        m = re.search(rf"^#### {re.escape(new)} .+$", text, re.MULTILINE)
        if not m:
            continue
        heading_line = m.group(0)
        alias_anchor = f'<a id="{new.lower().replace(".", "")}"></a>'
        if alias_anchor in text:
            continue
        text = text.replace(heading_line, f"{alias_anchor}\n\n{heading_line}", 1)
    return text


def migrate_file(path: Path, dry_run: bool) -> bool:
    original = path.read_text(encoding="utf-8")
    text = original
    rewrite_headings = path.name in BAND_FILES
    text = replace_cluster_cites(text, rewrite_headings=rewrite_headings)
    if path.name in CH5_MAP_FILES and not rewrite_headings:
        for old, (new, _title) in sorted(CLUSTER_MAP.items(), key=lambda kv: -len(kv[0])):
            gate = TITLE_GATE[old]
            text = re.sub(rf"\[{re.escape(old)}\s+(?={gate})", f"[{new} ", text)
            text = re.sub(rf"\*\*{re.escape(old)}\s+(?={gate})", f"**{new} ", text)
    if path.name == "core_05__definitions_home.md":
        text = update_directory_clusters(text)
        # Meta prose still saying "Numbered clusters"
        text = text.replace(
            "Numbered clusters **Def.O1–Def.I1**",
            "Dependent clusters **Def.O1–Def.I1**",
        )
        text = text.replace(
            "numbered clusters **Def.O1–Def.I1**",
            "dependent clusters **Def.O1–Def.I1**",
        )
    text = update_band_tables(text, path)
    text = add_def_alias_anchors(text, path)

    if text == original:
        return False
    if not dry_run:
        path.write_text(text, encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--root", default=str(ROOT))
    args = parser.parse_args()
    root = Path(args.root).resolve()

    changed = []
    for path in iter_targets(root):
        if migrate_file(path, args.dry_run):
            changed.append(path.relative_to(root))

    prefix = "DRY-RUN would update" if args.dry_run else "Updated"
    print(f"{prefix} {len(changed)} files:")
    for rel in changed:
        print(f"  - {rel}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
