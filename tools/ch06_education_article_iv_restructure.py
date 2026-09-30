#!/usr/bin/env python3
"""Chapter Six: combine education into a new Article IV and renumber.

Label map (2026-09-26):

- Article III (*Survival and Equal Educational Access*) -> Article III (*Survival and Essential Access*)
- III-B (*Equal Educational Access*)                     -> IV-A
- III-C .. III-F                                         -> III-B .. III-E
- Article VI (*Right to Sentient-Centered Education*)    -> Article IV (same title), moved to Part A
- VI-A, VI-B                                             -> IV-B, IV-C
- Article IV (*Resource Allocation ...*), IV-A, IV-B     -> Article V, V-A, V-B
- Article V (*Equal Basic Rights*), V-A .. V-D           -> Article VI, VI-A .. VI-D

Phase ``labels`` rewrites article labels in prose. Subarticle labels (``V-C``)
are rewritten wherever they stand alone; whole-article labels (``V``) only
inside an ``Article``/``Articles`` citation run. Phase ``anchors`` rewrites
heading fragments (including the Part B -> Part A file move).

Scope follows the 2026-09-25/26 Article V reletterings: archive/, evidence/,
and project/MEMLOG.md are historical and left alone; translations/ and
evaluation/external_audit_2026-08/ get anchor retargeting only.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve()

TEXT_SUFFIXES = {".md", ".json", ".py", ".yml", ".yaml", ".txt", ".csv", ".html", ".js", ".toml"}
SKIP_DIRS = ("archive/", "evidence/", ".git/", "tools/__pycache__/", "_pages_site/")
SKIP_FILES = {"project/MEMLOG.md"}
ANCHOR_ONLY_DIRS = ("translations/", "evaluation/external_audit_2026-08/")

SUB_MAP = {
    "III-B": "IV-A",
    "III-C": "III-B",
    "III-D": "III-C",
    "III-E": "III-D",
    "III-F": "III-E",
    "IV-A": "V-A",
    "IV-B": "V-B",
    "V-A": "VI-A",
    "V-B": "VI-B",
    "V-C": "VI-C",
    "V-D": "VI-D",
    "VI-A": "IV-B",
    "VI-B": "IV-C",
}
WHOLE_MAP = {"IV": "V", "V": "VI", "VI": "IV"}

SUB_RE = re.compile(r"(?<![\w-])(III-[B-F]|IV-[AB]|V-[A-D]|VI-[AB])(?![\w-])")
WHOLE_RE = re.compile(r"(?<![\w-])(IV|VI|V)(?![\w]|-[A-Za-z0-9])")
ARTICLE_WORD_RE = re.compile(r"\bArticles?\b")
# What may sit between "Article(s)" and a label inside one citation run.
RUN_FILLER_RE = re.compile(
    r"^s?(?:\s|,|;|/|&|–|—|-|\band\b|\bor\b|\bthrough\b|\bto\b|"
    r"[IVXL]+(?:-[A-Z](?:\.\d+)?)?|\(|\))*$"
)
LINK_TARGET_RE = re.compile(r"\]\([^)]*\)")
HISTORY_RE = re.compile(r"\b(old|formerly|is now|was)\b|→", re.IGNORECASE)

ANCHOR_MAP_A = {  # stays in core_06_rights_part_a.md
    "article-iii-survival-and-equal-educational-access": "article-iii-survival-and-essential-access",
    "article-iii-b-equal-educational-access": "article-iv-a-equal-educational-access",
    "article-iii-c-bodily-maintenance-and-healthcare-access": "article-iii-b-bodily-maintenance-and-healthcare-access",
    "article-iii-d-labor-and-economic-floor": "article-iii-c-labor-and-economic-floor",
    "article-iii-e-safe-working-conditions": "article-iii-d-safe-working-conditions",
    "article-iii-f-rest-and-recuperation": "article-iii-e-rest-and-recuperation",
    "article-iv-resource-allocation-dependencies-and-ecosystem-funding": "article-v-resource-allocation-dependencies-and-ecosystem-funding",
    "article-iv-a-dependency-mapping-and-resource-flow-transparency": "article-v-a-dependency-mapping-and-resource-flow-transparency",
    "article-iv-b-cross-system-fairness-and-sustainability": "article-v-b-cross-system-fairness-and-sustainability",
}
ANCHOR_MAP_B = {  # stays in core_06_rights_part_b.md
    "article-v-equal-basic-rights": "article-vi-equal-basic-rights",
    "article-v-a-dignity-and-equal-moral-standing": "article-vi-a-dignity-and-equal-moral-standing",
    "article-v-b-sentience-status-adjudication-floor": "article-vi-b-sentience-status-adjudication-floor",
    "article-v-c-nondiscrimination": "article-vi-c-nondiscrimination",
    "article-v-d-accessibility": "article-vi-d-accessibility",
    "part-b-personhood-education-capability-agency-cooperation-and-stakeholder-system-participation":
        "part-b-personhood-agency-cooperation-and-stakeholder-system-participation",
}
ANCHOR_MOVE_B_TO_A = {  # core_06_rights_part_b.md -> core_06_rights_part_a.md
    "article-vi-right-to-sentient-centered-education": "article-iv-right-to-sentient-centered-education",
    "article-vi-a-capability-building-education-right": "article-iv-b-capability-building-education-right",
    "article-vi-b-lifelong-and-adaptive-learning-and-contestability": "article-iv-c-lifelong-and-adaptive-learning-and-contestability",
}
# Headings elsewhere that carry an article label in their text.
ANCHOR_MAP_OTHER = {
    "sentience-status-adjudication-article-v-b-sentience-status-adjudication-floor-implementation-hook":
        "sentience-status-adjudication-article-vi-b-sentience-status-adjudication-floor-implementation-hook",
}

TITLE_MAP = [
    ("Survival and Equal Educational Access", "Survival and Essential Access"),
]


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def iter_files():
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path.suffix not in TEXT_SUFFIXES or path == SELF:
            continue
        r = rel(path)
        if r.startswith(SKIP_DIRS) or r in SKIP_FILES:
            continue
        yield path, r


def in_article_run(line: str, start: int) -> bool:
    prefix = line[max(0, start - 240):start]
    last = None
    for last in ARTICLE_WORD_RE.finditer(prefix):
        pass
    if last is None:
        return False
    between = prefix[last.end():]
    between = LINK_TARGET_RE.sub("", between)
    between = between.replace("**", "").replace("*", "").replace("[", "").replace("]", "")
    return bool(RUN_FILLER_RE.match(between))


def relabel_line(line: str, report: list[str], where: str) -> str:
    if HISTORY_RE.search(line) and SUB_RE.search(line):
        report.append(f"HISTORY? {where}: {line.strip()[:220]}")
    out = []
    pos = 0
    events = []
    for m in SUB_RE.finditer(line):
        events.append((m.start(), m.end(), SUB_MAP[m.group(1)], "sub"))
    for m in WHOLE_RE.finditer(line):
        if in_article_run(line, m.start()):
            events.append((m.start(), m.end(), WHOLE_MAP[m.group(1)], "whole"))
    events.sort()
    for start, end, new, kind in events:
        if start < pos:
            continue
        # Subarticle labels outside an Article run are reported for review.
        if kind == "sub" and not in_article_run(line, start):
            ctx = line[max(0, start - 60):end + 40].strip()
            report.append(f"BARE-SUB {where}: …{ctx}…")
        out.append(line[pos:start])
        out.append(new)
        pos = end
    out.append(line[pos:])
    return "".join(out)


def relabel_text(text: str, report: list[str], r: str) -> str:
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if SUB_RE.search(line) or WHOLE_RE.search(line):
            lines[i] = relabel_line(line, report, f"{r}:{i + 1}")
    text = "\n".join(lines)
    for old, new in TITLE_MAP:
        text = text.replace(old, new)
    return text


def reanchor_text(text: str, r: str) -> str:
    here = Path(r).name
    # Part B -> Part A moves: explicit file references first.
    for old, new in ANCHOR_MOVE_B_TO_A.items():
        text = re.sub(
            rf"core_06_rights_part_b\.md#{re.escape(old)}(?![\w-])",
            f"core_06_rights_part_a.md#{new}",
            text,
        )
        if here == "core_06_rights_part_b.md":
            text = re.sub(rf"\(#{re.escape(old)}\)", f"(core_06_rights_part_a.md#{new})", text)
        text = re.sub(rf"#{re.escape(old)}(?![\w-])", f"#{new}", text)
    for mapping in (ANCHOR_MAP_A, ANCHOR_MAP_B, ANCHOR_MAP_OTHER):
        for old, new in mapping.items():
            text = re.sub(rf"(?<![\w-]){re.escape(old)}(?![\w-])", new, text)
    if here == "core_06_rights_part_a.md":
        text = text.replace("](core_06_rights_part_a.md#", "](#")
    return text


LINK_RE = re.compile(r'(\]\(|href=")([^)"\s#]*)(#[^)"\s]*)')


def reanchor_outbound_links(text: str, path: Path) -> str:
    """Translations keep pinned local ids; only retarget links into English files."""

    def fix(match: re.Match[str]) -> str:
        prefix, target, fragment = match.groups()
        if not target:
            return match.group(0)
        try:
            resolved = rel((path.parent / target).resolve())
        except ValueError:
            return match.group(0)
        if resolved.startswith("translations/"):
            return match.group(0)
        return prefix + reanchor_text(target + fragment, "outbound.md")

    return LINK_RE.sub(fix, text)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("phase", choices=["labels", "anchors"])
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--report", default="-")
    args = ap.parse_args()

    if args.phase == "labels" and args.write:
        part_a = (ROOT / "core_06_rights_part_a.md").read_text(encoding="utf-8")
        if "### Article IV: Right to Sentient-Centered Education" in part_a:
            print("labels: already applied (Part A has the new Article IV); refusing to relabel twice.")
            return 1

    report: list[str] = []
    changed = []
    for path, r in iter_files():
        original = path.read_text(encoding="utf-8")
        if args.phase == "labels":
            if r.startswith(ANCHOR_ONLY_DIRS):
                continue
            # Protect anchors from label rewriting (handled in phase 2).
            updated = relabel_text(original, report, r)
        elif r.startswith("translations/"):
            updated = reanchor_outbound_links(original, path)
        else:
            updated = reanchor_text(original, r)
        if updated != original:
            changed.append(r)
            if args.write:
                path.write_text(updated, encoding="utf-8")
    out = sys.stdout if args.report == "-" else open(args.report, "w", encoding="utf-8")
    print(f"{args.phase}: {len(changed)} file(s) {'changed' if args.write else 'would change'}", file=out)
    for line in report:
        print(line, file=out)
    for r in changed:
        print(f"  - {r}", file=out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
