#!/usr/bin/env python3
"""Chapter 0/1 -> Chapter 6 alignment audit.

This audit treats Chapter 0 as the measurement frame, Chapter 1 as the
principle layer, and Chapter 6 as the Rights Floor. It emits a reader-facing
Markdown report plus machine-readable CSV/JSON evidence.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import re
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath
import sys
from typing import Iterable

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from definition_index import (  # noqa: E402
    collect_ch1_principles,
    extract_ch5_term_cites,
    extract_odef_cites,
)


CH0_FILE = "core_00_preamble.md"
CH1_FILES = [
    "core_01_a_values_principles.md",
    "core_01_b_interaction_interpretation.md",
    "core_01_c_stewardship_capacity_principles.md",
]
CH6_FILES = [
    "core_06_rights_part_a.md",
    "core_06_rights_part_b.md",
    "core_06_rights_part_c.md",
    "core_06_rights_part_d.md",
]

TETRAD_TERMS = ["participation", "oversight", "accountability", "timeliness"]
AIM_TERMS = ["flourishing", "continuity"]
MATERIAL_TERMS = ["material stake", "materiality", "material impact", "material risk"]

MEASUREMENT_FAMILIES = {
    "Wellbeing": [
        "wellbeing",
        "flourishing",
        "functional integrity",
        "participation capacity",
    ],
    "Safety / Harm / Risk": [
        "safety",
        "harm",
        "risk",
        "safe conditions",
        "irreversible harm",
        "cascading failure",
    ],
    "Survival-floor access": [
        "survival",
        "food",
        "water",
        "shelter",
        "bodily-maintenance",
        "occupancy continuity",
        "operating environment",
    ],
    "Constitutional Efficiency": [
        "constitutional efficiency",
        "efficient",
        "efficiency",
        "throughput",
        "docket",
    ],
    "Avoidable Burden": [
        "avoidable burden",
        "burden",
        "friction",
        "time",
        "attention",
    ],
    "Productive Capacity": [
        "productive capacity",
        "capacity",
        "capability",
    ],
    "Ecological Footprint / Environmental Preconditions": [
        "ecological footprint",
        "environmental preconditions",
        "environment",
        "ecological",
        "emissions",
        "materials",
        "land use",
    ],
    "Resilience / Systemic Risk": [
        "resilience",
        "reversibility",
        "self-healing",
        "existential risk",
        "systemic risk",
        "cascading",
    ],
    "Dependency / Resource Flow": [
        "dependency",
        "resource-flow",
        "resource flow",
        "resource allocation",
        "shared infrastructure",
    ],
    "Proportionate Cross-System Support": [
        "proportionate cross-system support",
        "cross-system support",
        "shared infrastructure",
        "foundational dependencies",
    ],
    "Substantive Fairness": [
        "substantive fairness",
        "nondiscrimination",
        "disparate impact",
        "protected characteristic",
        "equal basic rights",
    ],
    "Accessibility": [
        "accessibility",
        "accessible",
        "accommodation",
        "substantive participation",
    ],
    "Educational Agency": [
        "educational agency",
        "education",
        "learning",
        "capability-building",
        "retraining",
    ],
    "Truth / Epistemic Integrity": [
        "truth",
        "epistemic integrity",
        "disclosure",
        "misleading",
        "accuracy",
        "verification",
    ],
    "Privacy / Data Stewardship": [
        "privacy",
        "informational",
        "data handling",
        "segmentation",
        "lifecycle",
    ],
    "Trustworthiness": [
        "trustworthiness",
        "trustworthy",
        "reliable",
        "reliability",
        "false trust",
        "misleading reliance",
    ],
    "Incentive Alignment / Proxy Integrity": [
        "incentive alignment",
        "proxy divergence",
        "perverse incentive",
        "capture",
        "proxy metric",
    ],
    "Market Structure / Contestability": [
        "market structure",
        "concentration",
        "contestability",
        "anti-domination",
        "entry",
        "exit",
    ],
    "Timely Resolution": [
        "timely resolution",
        "anti-delay",
        "delay",
        "time limit",
        "deadline",
        "clock",
    ],
}

# Parent map: Preamble §2 eight categories → §3 measurement-family subcategories.
MEASUREMENT_CATEGORIES: dict[str, list[str]] = {
    "3.1 Threshold and scaling": ["Materiality"],
    "3.2 Flourishing": [
        "Wellbeing",
        "Safety / Harm / Risk",
        "Survival-floor access",
    ],
    "3.3 Continuity": [
        "Ecological Footprint / Environmental Preconditions",
        "Resilience / Systemic Risk",
        "Dependency / Resource Flow",
        "Proportionate Cross-System Support",
    ],
    "3.4 Participation": [
        "Substantive Fairness",
        "Accessibility",
        "Educational Agency",
        "Privacy / Data Stewardship",
    ],
    "3.5 Oversight": [
        "Truth / Epistemic Integrity",
        "Trustworthiness",
    ],
    "3.6 Accountability": [
        "Incentive Alignment / Proxy Integrity",
        "Market Structure / Contestability",
    ],
    "3.7 Timeliness": ["Timely Resolution"],
    "3.8 Constitutional performance": [
        "Constitutional Efficiency",
        "Avoidable Burden",
        "Productive Capacity",
    ],
}

CH00_SECTION3_ANCHOR_RE = re.compile(
    r"(?:core_00_preamble\.md#measuring-|Preamble §3\.?\d?)",
    re.IGNORECASE,
)

RIGHTS_FAMILIES = {
    "survival/resources": ["I", "II", "III", "IV"],
    "equality/access": ["V", "VI", "VII", "VIII"],
    "agency/participation": ["IX", "X", "XI"],
    "systems/trust/audit": ["XII", "XIII", "XIV", "XV", "XVI", "XVII"],
    "standing/interpretation": ["XVIII", "XIX", "XX", "XXI", "XXII"],
    "justice/emergency/transition": ["XXIII", "XXIV", "XXV", "XXVI"],
}

PRINCIPLE_RULES = [
    (("wellbeing", "dignity", "survival", "subsistence"), ["2", "3.1"]),
    (("safety", "harm", "risk", "emergency", "restriction"), ["3.1", "6.1", "6.3", "7"]),
    (("truth", "audit", "transparency", "disclosure", "record", "evidence"), ["3.2", "6.2", "8"]),
    (("trust", "reliability", "trustworthy", "misleading reliance"), ["4"]),
    (("freedom", "agency", "self-determination", "movement", "exit"), ["5", "5.1"]),
    (("collision", "conflict", "proportionality", "necessity", "least-restrictive"), ["6.1", "6.1.5", "6.3"]),
    (("override", "bypass", "non-contraction", "interpretation"), ["7", "8"]),
    (("stewardship", "distributed understanding", "comprehensibility"), ["9", "9.2"]),
    (("governance", "capture", "incentive", "authority"), ["10", "10.1"]),
    (("capacity", "resource", "market", "concentration", "dependency"), ["11", "12", "13"]),
]

OWNER_DRIFT_PATTERNS = [
    r"\bchapter one\b.{0,90}\b(create[s]?|establish(?:es)?|states?)\b.{0,90}\bright[s]?\s*floor",
    r"\bprinciple-layer\b.{0,90}\b(create[s]?|extend[s]?|narrow[s]?|replace[s]?)\b.{0,90}\bright[s]?\s*floor",
    r"\bchapter six\b.{0,90}\b(bypass(?:es)?|override[s]?|supersede[s]?)\b.{0,90}\bchapter one\b",
]

OVERREACH_PATTERNS = [
    r"notwithstanding\s+chapter\s+one",
    r"notwithstanding\s+foundational\s+rights",
    r"override[s]?\s+chapter\s+one",
    r"override[s]?\s+foundational\s+rights",
    r"supersede[s]?\s+chapter\s+one",
    r"supersede[s]?\s+foundational\s+rights",
    r"replace[s]?\s+chapter\s+one",
    r"replace[s]?\s+foundational\s+rights",
]

LOCAL_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
HTML_ANCHOR_RE = re.compile(r"<a\s+id=\"([^\"]+)\"")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
ARTICLE_RE = re.compile(r"^(###|####)\s+Article\s+([IVXLCDM]+(?:-[A-Z])?):\s+(.+?)\s*$")


@dataclass
class Principle:
    section: str
    title: str
    file: str
    line: int
    body: str = ""
    ch6_refs: list[str] = field(default_factory=list)


@dataclass
class Article:
    article_id: str
    title: str
    file: str
    line: int
    level: int
    family: str
    body: str = ""
    direct_ch1_refs: list[str] = field(default_factory=list)
    inferred_ch1_basis: list[str] = field(default_factory=list)
    tetrad_terms: list[str] = field(default_factory=list)
    aims: list[str] = field(default_factory=list)
    material_signals: list[str] = field(default_factory=list)
    expected_measurements: list[str] = field(default_factory=list)
    measurement_refs: list[str] = field(default_factory=list)
    ch00_section3_signals: list[str] = field(default_factory=list)
    owner_refs: list[str] = field(default_factory=list)
    ch5_refs: list[str] = field(default_factory=list)
    odef_refs: list[str] = field(default_factory=list)
    classifications: list[str] = field(default_factory=list)


@dataclass
class Finding:
    kind: str
    severity: str
    file: str
    line: int
    item: str
    issue: str
    detail: object = None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".", help="Repository root.")
    parser.add_argument("--root", dest="repo_root", help=argparse.SUPPRESS)
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


def read_text(root: Path, rel_path: str) -> str:
    return (root / rel_path).read_text(encoding="utf-8")


def slugify_heading(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\[[^\]]+\]\([^)]+\)", "", text)
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text


def collect_anchors(root: Path, rel_paths: Iterable[str]) -> dict[str, set[str]]:
    anchors: dict[str, set[str]] = {}
    for rel_path in rel_paths:
        text = read_text(root, rel_path)
        file_anchors = {match.group(1) for match in HTML_ANCHOR_RE.finditer(text)}
        for line in text.splitlines():
            match = HEADING_RE.match(line.strip())
            if match:
                file_anchors.add(slugify_heading(match.group(2)))
        anchors[rel_path] = file_anchors
    return anchors


def article_family(article_id: str) -> str:
    base = article_id.split("-")[0]
    for family, articles in RIGHTS_FAMILIES.items():
        if base in articles:
            return family
    return "unclassified"


def extract_principles(root: Path) -> list[Principle]:
    principles: list[Principle] = []
    for record in collect_ch1_principles(root):
        if record.file not in {CH0_FILE, *CH1_FILES}:
            continue
        ch6_refs = sorted(set(re.findall(r"core_06_rights_part_[a-d]\.md#[a-z0-9-]+", record.body)))
        principles.append(
            Principle(
                section=record.section,
                title=record.title,
                file=record.file,
                line=record.line,
                body=record.body,
                ch6_refs=ch6_refs,
            )
        )
    return principles


def extract_articles(root: Path) -> list[Article]:
    articles: list[Article] = []
    for rel_path in CH6_FILES:
        lines = read_text(root, rel_path).splitlines()
        starts: list[tuple[int, str, str, int]] = []
        for idx, line in enumerate(lines):
            match = ARTICLE_RE.match(line.strip())
            if match:
                level = 3 if match.group(1) == "###" else 4
                starts.append((idx, match.group(2), match.group(3).strip(), level))
        for pos, (start_idx, article_id, title, level) in enumerate(starts):
            end_idx = starts[pos + 1][0] if pos + 1 < len(starts) else len(lines)
            body = "\n".join(lines[start_idx + 1:end_idx])
            articles.append(
                Article(
                    article_id=article_id,
                    title=title,
                    file=rel_path,
                    line=start_idx + 1,
                    level=level,
                    family=article_family(article_id),
                    body=body,
                )
            )
    return articles


def ch1_fragment_section_map(root: Path) -> dict[str, str]:
    """Map core_01 file#fragment to the live numbered heading that owns it."""
    mapping: dict[str, str] = {}
    num_re = re.compile(r"^(\d+(?:\.\d+)*)\.\s+")
    for rel in CH1_FILES:
        pending: list[str] = []
        for line in read_text(root, rel).splitlines():
            pending.extend(HTML_ANCHOR_RE.findall(line))
            match = HEADING_RE.match(line.strip())
            if not match:
                continue
            title = match.group(2)
            numbered = num_re.match(title)
            if numbered:
                section = numbered.group(1)
                for anchor_id in pending:
                    mapping[f"{rel}#{anchor_id}"] = section
                mapping[f"{rel}#{slugify_heading(title)}"] = section
            pending = []
    return mapping


def extract_direct_ch1_refs(
    text: str,
    fragment_map: dict[str, str] | None = None,
    live_sections: set[str] | None = None,
) -> list[str]:
    refs: set[str] = set()
    for match in re.finditer(r"\[([^]]+)\]\((core_01_[^)#]+\.md)#([^)]+)\)", text):
        key = f"{match.group(2)}#{match.group(3)}"
        if fragment_map and key in fragment_map:
            refs.add(fragment_map[key])
            continue
        label = match.group(1)
        section_match = re.search(r"§\s*([0-9]+(?:\.[0-9]+)*)", label)
        refs.add(section_match.group(1) if section_match else "linked")
    # Ignore the fossil nickname "Chapter Twelve Chapter One §N".
    for match in re.finditer(r"(?<!Twelve )Chapter One\s+§+\s*([0-9]+(?:\.[0-9]+)*)", text):
        num = match.group(1)
        if live_sections is not None and num not in live_sections:
            continue
        refs.add(num)
    if any(name in text for name in CH1_FILES):
        refs.add("linked")
    return sorted(refs, key=sort_ref)


def sort_ref(value: str) -> list[int | str]:
    if value == "linked":
        return [999, value]
    return [int(part) for part in value.split(".")]


def infer_ch1_basis(article: Article) -> list[str]:
    haystack = f"{article.article_id} {article.title} {article.body}".lower()
    refs: set[str] = set()
    for terms, principles in PRINCIPLE_RULES:
        if any(term in haystack for term in terms):
            refs.update(principles)
    return sorted(refs, key=sort_ref)


def present_terms(text: str, terms: list[str]) -> list[str]:
    low = text.lower()
    return [term for term in terms if term in low]


def measurement_families_for(text: str) -> list[str]:
    low = text.lower()
    families = []
    for family, terms in MEASUREMENT_FAMILIES.items():
        if any(term in low for term in terms):
            families.append(family)
    return families


def ch00_section3_signals_for(text: str) -> list[str]:
    """Explicit Preamble §3 read-with links or canonical #measuring-* anchors."""
    signals: list[str] = []
    if CH00_SECTION3_ANCHOR_RE.search(text):
        signals.append("explicit_ch00_section3_trace")
    for category, subcategories in MEASUREMENT_CATEGORIES.items():
        if category.lower() in text.lower():
            signals.append(category)
            continue
        for subcategory in subcategories:
            if subcategory.lower() in text.lower():
                signals.append(f"{category} ({subcategory})")
                break
    return signals


def is_measurement_dependent(article: Article) -> bool:
    text = f"{article.title}\n{article.body}".lower()
    if any(term in text for terms in MEASUREMENT_FAMILIES.values() for term in terms):
        return True
    return article.article_id.split("-")[0] in {
        "I", "III", "IV", "V", "VI", "XII", "XV", "XVIII", "XX", "XXIV"
    }


def collect_owner_refs(text: str) -> list[str]:
    refs: set[str] = set()
    for pattern in (
        r"\bChapter One\b",
        r"\bChapter Five\b",
        r"\bChapter Seven\b",
        r"\bChapter Eight\b",
        r"\bChapter Eleven\b",
        r"\bArticle\s+[IVXLCDM]+(?:-[A-Z])?\b",
        r"`?corpus_[a-z_]+\.md`?",
        r"`?core_[^`\s)]+\.md`?",
    ):
        refs.update(match.group(0).strip("`") for match in re.finditer(pattern, text))
    return sorted(refs)


def normalize_target(source_rel: str, raw_target: str) -> tuple[str, str] | None:
    if raw_target.startswith(("http://", "https://", "mailto:")):
        return None
    target = raw_target.split("#", 1)
    raw_path = target[0]
    anchor = target[1] if len(target) == 2 else ""
    if not raw_path:
        rel_path = source_rel
    else:
        rel_path = str((PurePosixPath(source_rel).parent / raw_path).as_posix())
        parts: list[str] = []
        for part in PurePosixPath(rel_path).parts:
            if part in {"", "."}:
                continue
            if part == "..":
                if parts:
                    parts.pop()
                continue
            parts.append(part)
        rel_path = "/".join(parts)
    return rel_path, anchor


def cross_layer_broken_links(root: Path, anchors: dict[str, set[str]]) -> list[Finding]:
    findings: list[Finding] = []
    audited = [CH0_FILE, *CH1_FILES, *CH6_FILES]
    source_sets = {
        "ch0": {CH0_FILE},
        "ch1": set(CH1_FILES),
        "ch6": set(CH6_FILES),
    }

    def relevant(source: str, target: str) -> bool:
        return (
            source in source_sets["ch1"] and target in source_sets["ch6"]
        ) or (
            source in source_sets["ch6"] and target in source_sets["ch1"] | source_sets["ch0"]
        ) or (
            source == CH0_FILE and target in source_sets["ch1"] | source_sets["ch6"]
        )

    for source in audited:
        for idx, line in enumerate(read_text(root, source).splitlines(), start=1):
            for match in LOCAL_LINK_RE.finditer(line):
                normalized = normalize_target(source, match.group(1))
                if normalized is None:
                    continue
                target, anchor = normalized
                if not relevant(source, target):
                    continue
                if not (root / target).is_file():
                    findings.append(
                        Finding(
                            kind="broken_link",
                            severity="high",
                            file=source,
                            line=idx,
                            item=match.group(1),
                            issue=f"Target file `{target}` does not exist.",
                        )
                    )
                    continue
                if anchor and anchor not in anchors.get(target, set()):
                    findings.append(
                        Finding(
                            kind="broken_link",
                            severity="high",
                            file=source,
                            line=idx,
                            item=match.group(1),
                            issue=f"Target anchor `#{anchor}` not found in `{target}`.",
                        )
                    )
    return findings


class Ch1Ch6AlignmentAuditor:
    def __init__(self, repo_root: Path, date_stamp: str):
        self.repo_root = repo_root
        self.date_stamp = date_stamp
        self.principles: list[Principle] = []
        self.articles: list[Article] = []
        self.findings: list[Finding] = []
        self.fragment_map: dict[str, str] = {}
        self.live_sections: set[str] = set()

    def run(self) -> None:
        anchors = collect_anchors(self.repo_root, [CH0_FILE, *CH1_FILES, *CH6_FILES])
        self.principles = extract_principles(self.repo_root)
        self.fragment_map = ch1_fragment_section_map(self.repo_root)
        self.live_sections = {principle.section for principle in self.principles}
        self.articles = extract_articles(self.repo_root)
        self.findings.extend(cross_layer_broken_links(self.repo_root, anchors))

        for article in self.articles:
            self._analyze_article(article)
        self._scan_owner_and_overreach()

    def _analyze_article(self, article: Article) -> None:
        text = f"{article.title}\n{article.body}"
        article.direct_ch1_refs = extract_direct_ch1_refs(
            text, self.fragment_map, self.live_sections
        )
        article.inferred_ch1_basis = infer_ch1_basis(article)
        article.tetrad_terms = present_terms(text, TETRAD_TERMS)
        article.aims = present_terms(text, AIM_TERMS)
        article.material_signals = present_terms(text, MATERIAL_TERMS)
        article.expected_measurements = measurement_families_for(text)
        article.measurement_refs = [
            family for family in article.expected_measurements
            if family.lower() in text.lower() or any(
                term in text.lower() for term in MEASUREMENT_FAMILIES[family]
            )
        ]
        article.ch00_section3_signals = ch00_section3_signals_for(text)
        article.owner_refs = collect_owner_refs(text)
        article.ch5_refs = extract_ch5_term_cites(text)
        article.odef_refs = extract_odef_cites(text)

        classifications: set[str] = set()
        if not article.direct_ch1_refs and not article.inferred_ch1_basis:
            classifications.add("missing_ch1_basis")
            self.findings.append(Finding(
                "missing_ch1_basis", "high", article.file, article.line,
                article.article_id, "No direct or inferred Chapter 1 principle basis found.",
            ))
        elif not article.direct_ch1_refs:
            classifications.add("weak_trace")
            self.findings.append(Finding(
                "weak_trace", "medium", article.file, article.line,
                article.article_id, "Chapter 1 basis is inferred from subject matter, not directly cited.",
                article.inferred_ch1_basis,
            ))

        if article.level == 3 and not (
            article.tetrad_terms and article.aims and article.material_signals
        ):
            classifications.add("missing_ch0_measurement_frame")
            missing = []
            if not article.tetrad_terms:
                missing.append("Tetrad")
            if not article.aims:
                missing.append("Aims")
            if not article.material_signals:
                missing.append("material stake")
            self.findings.append(Finding(
                "missing_ch0_measurement_frame", "medium", article.file, article.line,
                article.article_id, f"Missing top-level Chapter 0 frame signal(s): {', '.join(missing)}.",
            ))

        if is_measurement_dependent(article) and not article.expected_measurements:
            classifications.add("measurement_gap")
            self.findings.append(Finding(
                "measurement_gap", "medium", article.file, article.line,
                article.article_id, "Measurement-dependent right lacks clear Chapter 0/5 measurement-family routing.",
            ))

        text_low = text.lower()
        for pattern in OWNER_DRIFT_PATTERNS:
            if re.search(pattern, text_low, flags=re.DOTALL):
                classifications.add("owner_drift")
                self.findings.append(Finding(
                    "owner_drift", "high", article.file, article.line,
                    article.article_id, "Potential owner-boundary drift between principle layer and Rights Floor.",
                    pattern,
                ))
                break
        for pattern in OVERREACH_PATTERNS:
            if re.search(pattern, text_low):
                classifications.add("overreach")
                self.findings.append(Finding(
                    "overreach", "high", article.file, article.line,
                    article.article_id, "Potential overreach language detected.",
                    pattern,
                ))
                break

        article.classifications = sorted(classifications) if classifications else ["complete"]

    def _scan_owner_and_overreach(self) -> None:
        for rel_path in [*CH1_FILES, *CH6_FILES]:
            for idx, line in enumerate(read_text(self.repo_root, rel_path).splitlines(), start=1):
                low = line.lower()
                for pattern in OWNER_DRIFT_PATTERNS:
                    if re.search(pattern, low):
                        self.findings.append(Finding(
                            "owner_drift", "high", rel_path, idx,
                            "line-scan", "Potential owner-boundary drift in prose line.",
                            line.strip(),
                        ))
                        break
                for pattern in OVERREACH_PATTERNS:
                    if re.search(pattern, low):
                        self.findings.append(Finding(
                            "overreach", "high", rel_path, idx,
                            "line-scan", "Potential overreach language in prose line.",
                            line.strip(),
                        ))
                        break

    def status(self) -> str:
        if any(f.severity == "high" for f in self.findings if f.kind != "manual_review"):
            return "FAIL"
        if any(f.kind != "manual_review" for f in self.findings):
            return "REVIEW"
        return "PASS"

    def write_outputs(self, output_dir: Path) -> None:
        output_dir.mkdir(parents=True, exist_ok=True)
        self.write_report(output_dir)
        self.write_matrix(output_dir)
        self.write_log(output_dir)

    def write_report(self, output_dir: Path) -> Path:
        path = output_dir / f"ch1_ch6_alignment_report_{self.date_stamp}.md"
        total = len(self.articles)
        direct = sum(1 for article in self.articles if article.direct_ch1_refs)
        top_level = [article for article in self.articles if article.level == 3]
        ch0_framed = sum(
            1 for article in top_level
            if article.tetrad_terms and article.aims and article.material_signals
        )
        ch0_framed_denom = len(top_level)
        ch0_section3_traced = sum(1 for article in self.articles if article.ch00_section3_signals)
        measurement_routed = sum(
            1 for article in self.articles
            if not is_measurement_dependent(article) or article.expected_measurements
        )
        finding_counts = self._finding_counts()
        status = self.status()

        lines = [
            "# Chapter 0/1 -> Chapter 6 Alignment Audit Report",
            "",
            f"**Date:** {self.date_stamp}",
            "**Workflow:** CH0_CH1_CH6_ALIGNMENT_AUDIT",
            "**Auditor:** Automated static extraction with manual-review flags",
            "",
            "## Average-Reader Dashboard",
            "",
            f"**Overall status:** `{status}`",
            "",
            self._plain_language_assessment(status),
            "",
            "### What Is Strong",
            "",
            f"- Chapter 6 article/subarticle inventory was discovered across all four rights files: `{total}` items.",
            f"- Direct Chapter 1 trace exists for `{direct}/{total}` Chapter 6 items.",
            f"- Chapter 0 measurement frame signals are structurally visible on `{ch0_framed}/{ch0_framed_denom}` top-level articles.",
            f"- Explicit Preamble §3 category traces or anchors appear on `{ch0_section3_traced}/{total}` items.",
            "",
            "### What Needs Review",
            "",
            f"- Measurement-family routing is clear or not required for `{measurement_routed}/{total}` items.",
            f"- Structural findings remain: `{sum(v for k, v in finding_counts.items() if k != 'manual_review')}`.",
            "- Doctrinal semantic adequacy is out of scope of this structural pass.",
            "",
            "### What May Need Edits",
            "",
        ]
        edit_findings = [f for f in self.findings if f.kind != "manual_review"]
        if edit_findings:
            for finding in edit_findings[:10]:
                lines.append(
                    f"- `{finding.kind}` at `{finding.file}:{finding.line}` ({finding.item}): {finding.issue}"
                )
            if len(edit_findings) > 10:
                lines.append(f"- Plus `{len(edit_findings) - 10}` additional machine-review item(s).")
        else:
            lines.append("- No machine-detected edit candidates outside manual semantic review.")

        lines.extend([
            "",
            "### Rights-Family Dashboard",
            "",
            "| Rights family | Items | Direct Chapter 1 basis | Chapter 0 frame | Measurement routing | Status |",
            "|---|---:|---:|---:|---:|---|",
        ])
        for family in RIGHTS_FAMILIES:
            rows = [article for article in self.articles if article.family == family]
            direct_count = sum(1 for article in rows if article.direct_ch1_refs)
            frame_count = sum(1 for article in rows if article.tetrad_terms and article.aims and article.material_signals)
            measurement_count = sum(1 for article in rows if not is_measurement_dependent(article) or article.expected_measurements)
            family_status = self._family_status(rows)
            lines.append(
                f"| {family} | {len(rows)} | {direct_count}/{len(rows)} | {frame_count}/{len(rows)} | {measurement_count}/{len(rows)} | {family_status} |"
            )

        lines.extend([
            "",
            "## Maintainer Metrics",
            "",
            "| Metric | Result | Status |",
            "|---|---:|---|",
            f"| Chapter 6 articles/subarticles discovered | {total} | PASS |",
            f"| Items with direct Chapter 1 basis | {direct}/{total} | {'PASS' if direct == total else 'REVIEW'} |",
            f"| Top-level articles with Chapter 0 Tetrad/Aims/material-stake framing | {ch0_framed}/{ch0_framed_denom} | {'PASS' if ch0_framed_denom and ch0_framed == ch0_framed_denom else 'REVIEW'} |",
            f"| Items with explicit Preamble §3 trace or anchor signal | {ch0_section3_traced}/{total} | {'PASS' if ch0_section3_traced else 'REVIEW'} |",
            f"| Items with clear measurement routing or no measurement dependency | {measurement_routed}/{total} | {'PASS' if measurement_routed == total else 'REVIEW'} |",
            f"| Broken or ambiguous Chapter 0/1/6 links | {finding_counts.get('broken_link', 0)} | {'PASS' if finding_counts.get('broken_link', 0) == 0 else 'FAIL'} |",
            f"| Owner-boundary risks | {finding_counts.get('owner_drift', 0)} | {'PASS' if finding_counts.get('owner_drift', 0) == 0 else 'FAIL'} |",
            f"| Potential overreach flags | {finding_counts.get('overreach', 0)} | {'PASS' if finding_counts.get('overreach', 0) == 0 else 'FAIL'} |",
            f"| Manual semantic-review items | {finding_counts.get('manual_review', 0)} | {'PASS' if finding_counts.get('manual_review', 0) == 0 else 'REVIEW'} |",
            "",
            "## Chapter 6 Article Traceability",
            "",
            "| Article | Title | File | Chapter 1 basis | Inferred basis | Chapter 0 frame | Def.* | oDef | Measurements | Status |",
            "|---|---|---|---|---|---|---|---|---|---|",
        ])
        for article in self.articles:
            ch0_frame = ", ".join(
                filter(None, [
                    "Tetrad" if article.tetrad_terms else "",
                    "Aims" if article.aims else "",
                    "material stake" if article.material_signals else "",
                ])
            ) or "None"
            lines.append(
                f"| {article.article_id} | {article.title} | `{article.file}:{article.line}` | {', '.join(article.direct_ch1_refs) or 'None'} | {', '.join(article.inferred_ch1_basis) or 'None'} | {ch0_frame} | {', '.join(article.ch5_refs) or 'None'} | {', '.join(article.odef_refs) or 'None'} | {', '.join(article.expected_measurements) or 'None'} | {', '.join(article.classifications)} |"
            )

        lines.extend([
            "",
            "## Chapter 1 Rights Surface",
            "",
            "| Principle | Title | File | Chapter 6 references |",
            "|---|---|---|---:|",
        ])
        for principle in self.principles:
            lines.append(
                f"| {principle.section} | {principle.title} | `{principle.file}:{principle.line}` | {len(principle.ch6_refs)} |"
            )

        lines.extend([
            "",
            "## Chapter 0 Measurement Coverage",
            "",
            "| Measurement family | Chapter 6 items referencing family |",
            "|---|---:|",
        ])
        for family in MEASUREMENT_FAMILIES:
            count = sum(1 for article in self.articles if family in article.expected_measurements)
            lines.append(f"| {family} | {count} |")

        lines.extend(["", "## Findings", ""])
        if not self.findings:
            lines.append("No findings.")
        else:
            for kind in [
                "broken_link",
                "owner_drift",
                "overreach",
                "missing_ch1_basis",
                "missing_ch0_measurement_frame",
                "measurement_gap",
                "weak_trace",
                "rights_floor_contraction_risk",
                "manual_review",
            ]:
                rows = [f for f in self.findings if f.kind == kind]
                if not rows:
                    continue
                lines.extend([f"### {kind.replace('_', ' ').title()}", ""])
                for finding in rows:
                    lines.append(
                        f"- **{finding.severity.upper()}** `{finding.file}:{finding.line}` `{finding.item}` — {finding.issue}"
                    )
                lines.append("")

        lines.extend([
            "## Remediation Roadmap",
            "",
            "1. Fix any broken cross-layer links before semantic editing.",
            "2. Resolve owner-boundary and overreach findings before adding explanatory trace prose.",
            "3. Add or clarify Chapter 0 measurement-family routing only where the right actually depends on measurement.",
            "4. Doctrinal semantic adequacy is out of scope of this structural pass; do not treat its absence as a machine gap.",
        ])

        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return path

    def write_matrix(self, output_dir: Path) -> Path:
        path = output_dir / f"ch1_ch6_traceability_matrix_{self.date_stamp}.csv"
        with path.open("w", encoding="utf-8", newline="") as fh:
            writer = csv.DictWriter(
                fh,
                fieldnames=[
                    "article_id",
                    "title",
                    "family",
                    "file",
                    "line",
                    "direct_ch1_refs",
                    "inferred_ch1_basis",
                    "tetrad_terms",
                    "aims",
                    "material_signals",
                    "measurement_families",
                    "ch5_refs",
                    "odef_refs",
                    "owner_refs",
                    "status",
                ],
            )
            writer.writeheader()
            for article in self.articles:
                writer.writerow({
                    "article_id": article.article_id,
                    "title": article.title,
                    "family": article.family,
                    "file": article.file,
                    "line": article.line,
                    "direct_ch1_refs": "; ".join(article.direct_ch1_refs),
                    "inferred_ch1_basis": "; ".join(article.inferred_ch1_basis),
                    "tetrad_terms": "; ".join(article.tetrad_terms),
                    "aims": "; ".join(article.aims),
                    "material_signals": "; ".join(article.material_signals),
                    "measurement_families": "; ".join(article.expected_measurements),
                    "ch5_refs": "; ".join(article.ch5_refs),
                    "odef_refs": "; ".join(article.odef_refs),
                    "owner_refs": "; ".join(article.owner_refs),
                    "status": "; ".join(article.classifications),
                })
        return path

    def write_log(self, output_dir: Path) -> Path:
        path = output_dir / f"ch1_ch6_audit_log_{self.date_stamp}.json"
        payload = {
            "date": self.date_stamp,
            "workflow": "CH0_CH1_CH6_ALIGNMENT_AUDIT",
            "status": self.status(),
            "summary": {
                "articles": len(self.articles),
                "principles": len(self.principles),
                "findings": self._finding_counts(),
            },
            "findings": [
                {
                    "kind": finding.kind,
                    "severity": finding.severity,
                    "file": finding.file,
                    "line": finding.line,
                    "item": finding.item,
                    "issue": finding.issue,
                    "detail": finding.detail,
                }
                for finding in self.findings
            ],
        }
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        return path

    def _finding_counts(self) -> dict[str, int]:
        counts: dict[str, int] = {}
        for finding in self.findings:
            counts[finding.kind] = counts.get(finding.kind, 0) + 1
        return counts

    def _family_status(self, rows: list[Article]) -> str:
        row_ids = {row.article_id for row in rows}
        findings = [
            finding for finding in self.findings
            if finding.item in row_ids and finding.kind != "manual_review"
        ]
        if any(finding.severity == "high" for finding in findings):
            return "FAIL"
        if findings:
            return "REVIEW"
        return "PASS"

    def _plain_language_assessment(self, status: str) -> str:
        if status == "PASS":
            return (
                "The audit found the Chapter 6 rights surface structurally coherent with Chapter 0's "
                "measurement frame and Chapter 1's principles. Doctrinal semantic adequacy is out of "
                "scope of this pass."
            )
        if status == "FAIL":
            return (
                "The audit found at least one high-priority cross-layer issue, such as a broken link, "
                "owner-boundary risk, or overreach flag. The rights surface should be reviewed before "
                "treating this pass as clean."
            )
        return (
            "The audit found a mostly usable alignment map, with some review items where trace prose, "
            "measurement routing, or semantic fit may need editorial attention. The report separates "
            "machine-checkable issues from human doctrinal review."
        )


def main() -> None:
    args = parse_args()
    root = Path(args.repo_root).resolve()
    output_dir = Path(args.output_dir) if args.output_dir else root / "evidence" / args.date
    if not output_dir.is_absolute():
        output_dir = root / output_dir

    auditor = Ch1Ch6AlignmentAuditor(root, args.date)
    auditor.run()
    auditor.write_outputs(output_dir)
    print(f"Chapter 0/1 -> Chapter 6 alignment audit: {auditor.status()}")
    print(f"Evidence written to: {output_dir}")


if __name__ == "__main__":
    main()
