#!/usr/bin/env python3
"""Unified definition appropriateness audit for the Sentient Constitution corpus.

Verifies constitutional definitions live in core Chapter Five files and
cross-implementation operational definitions live in CJS-3, with implementation
layers applying rather than redefining canonical terms.

Produces:
- evidence/<date>/definition_appropriateness_report_<date>.md
- evidence/<date>/definition_appropriateness_matrix_<date>.csv
- evidence/<date>/definition_appropriateness_log_<date>.json
- evidence/definition_audit/ledger.json (persistent cross-run findings)

Usage:
  python tools/definition_appropriateness_audit.py --repo-root .
  python tools/definition_appropriateness_audit.py --repo-root . --output-dir evidence/2026-07-05
  python tools/definition_appropriateness_audit.py --repo-root . --strict
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
import sys
from dataclasses import asdict, dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from ch1_ch5_alignment_audit import AlignmentAuditor  # noqa: E402
from ch1_cjs3_alignment_audit import Ch1Cjs3AlignmentAuditor  # noqa: E402
from ch5_definitions_gravity_audit import audit_blocks, virtual_chapter_five_text  # noqa: E402
from ch5_paths import CH5_ALL, CH5_INDEX  # noqa: E402
from corpus_paths import binding_corpus_scope  # noqa: E402
from definition_index import (  # noqa: E402
    Cjs3Cluster,
    Ch5Entry,
    collect_ch5_entries,
    collect_cjs3_clusters,
    ch5_term_lookup,
    ch5_term_lookup_with_tetrad_apex,
    normalize_term_label,
)
from owner_discipline_audit import CH5_OWNERS, scan_file  # noqa: E402

import cjs_operational_cluster_audit as cjs_placement  # noqa: E402
from ci_cjs_relocation_audit import (  # noqa: E402
    KEEP_SIGNALS,
    RELOCATION_SIGNALS,
    count_occurrences,
    strip_cjs_pointer_sentences,
    strip_details as strip_relocation_details,
    words as relocation_words,
)

WORKFLOW = "DEFINITION_APPROPRIATENESS_AUDIT"
LEDGER_PATH = "evidence/definition_audit/ledger.json"
LEDGER_SCHEMA_VERSION = 1

IMPL_DIRS = (
    "corpus_institutions",
    "corpus_systems",
    "corpus_forum",
)

CH5_ESCALATION_KEYWORDS = (
    "is defined as",
    "definition of",
    "canonical home for",
    "rights floor",
    "supremacy and enforceability",
    "definition integrity",
)

POINTER_DISCIPLINE_PHRASES: tuple[str, ...] = (
    "does not repeat",
    "does not redefine",
    "must not redefine",
    "not a second home",
    "shared rules live elsewhere",
    "shared cross-layer rules live in",
    "points there instead of repeating",
    "one canonical home",
    "canonical home",
    "apply chapter five",
    "not duplicate shared",
    "does not duplicate",
    "does not restate",
    "do not reinvent",
    "implementation-only",
    "institution-specific",
    "states the institutional",
    "states only",
    "supplies the institutional",
    "this file states",
    "this section states",
    "this subsection states",
)

RELOCATION_MIN_SCORE = 16

DEFINITIONAL_LEADIN_RE = re.compile(
    r"(?:^|\b)(?:"
    r"(?P<term>[A-Z][A-Za-z0-9'’\- /]+?)\s+(?:means|is defined as|refers to)"
    r"|"
    r"(?:definition of|canonical home for)\s+(?P<term2>[A-Z][A-Za-z0-9'’\- /]+?)"
    r")",
    re.MULTILINE,
)

OEC_BLOCK_RE = re.compile(
    r"^\s*(?:-\s*)?(?:\*\*)?O(?:bjective)?(?:\*\*)?\s*[:.]",
    re.I,
)


@dataclass
class Finding:
    check: str
    term: str
    current_layer: str
    line: int
    message: str
    severity: str = "review"
    expected_layer: str = ""
    action: str = ""
    finding_id: str = ""

    def __post_init__(self) -> None:
        if not self.finding_id:
            raw = f"{self.check}|{self.current_layer}|{self.line}|{self.term}"
            digest = hashlib.sha256(raw.encode()).hexdigest()[:12]
            self.finding_id = f"{self.check}:{digest}"


@dataclass
class AuditRun:
    timestamp: str
    ch5_entries: list[Ch5Entry] = field(default_factory=list)
    cjs3_clusters: list[Cjs3Cluster] = field(default_factory=list)
    findings: list[Finding] = field(default_factory=list)
    metrics: dict[str, Any] = field(default_factory=dict)
    regressions: list[str] = field(default_factory=list)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".", help="Repository root.")
    parser.add_argument(
        "--output-dir",
        default=None,
        help="Evidence snapshot directory. Defaults to evidence/<today>.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit non-zero when severity=error findings exist.",
    )
    parser.add_argument(
        "--skip-subprocess-audits",
        action="store_true",
        help="Skip subprocess checks for ch5-single-definition and constitutional-cluster audits.",
    )
    return parser.parse_args()


def _parse_location(raw: str) -> tuple[str, int]:
    if ":" in raw:
        file_part, line_part = raw.rsplit(":", 1)
        if line_part.isdigit():
            return file_part, int(line_part)
    return raw, 0


def _add_finding(
    findings: list[Finding],
    *,
    check: str,
    term: str,
    current_layer: str,
    line: int,
    message: str,
    severity: str = "review",
    expected_layer: str = "",
    action: str = "",
) -> None:
    findings.append(
        Finding(
            check=check,
            term=term,
            current_layer=current_layer,
            line=line,
            message=message,
            severity=severity,
            expected_layer=expected_layer,
            action=action,
        )
    )


def _split_audit_hit(hit: str, default_file: str = "") -> tuple[str, int, str]:
    """Parse `file:line: message` audit hit strings."""
    parts = hit.split(":", 2)
    if len(parts) >= 2 and parts[1].strip().isdigit():
        return parts[0], int(parts[1]), parts[2].strip() if len(parts) > 2 else hit
    return default_file or hit, 0, hit


def run_core_gravity(root: Path, findings: list[Finding]) -> int:
    text, rel = virtual_chapter_five_text(root)
    hits = audit_blocks(text, rel)
    for hit in hits:
        file_part, line, message = _split_audit_hit(hit, rel)
        _add_finding(
            findings,
            check="CORE-GRAVITY",
            term="(definition body)",
            current_layer=file_part,
            line=line,
            message=message,
            severity="review",
            expected_layer="implementation layer (cite owner home)",
            action="de-bundle from Chapter Five",
        )
    return len(hits)


def run_core_trace(root: Path, findings: list[Finding]) -> dict[str, int]:
    auditor = AlignmentAuditor(root)
    auditor.run_audit()
    counts = {
        "completeness": len(auditor.completeness_gaps),
        "accuracy": len(auditor.accuracy_gaps),
        "coverage": len(auditor.coverage_gaps),
        "cluster_integrity": len(auditor.cluster_gaps),
    }
    for gap in auditor.completeness_gaps:
        _add_finding(
            findings,
            check="CORE-TRACE",
            term=gap.get("principle", ""),
            current_layer="core_01_a_values_principles.md",
            line=0,
            message=gap.get("issue", "Principle missing definition anchors"),
            severity="error",
            expected_layer="Chapter Five band file",
            action="add D/A/C anchors",
        )
    for gap in auditor.accuracy_gaps:
        _add_finding(
            findings,
            check="CORE-TRACE",
            term=gap.get("definition", ""),
            current_layer="Chapter Five",
            line=0,
            message=f"Missing components: {', '.join(gap.get('missing_components', []))}",
            severity="error",
            expected_layer="complete O/E/C in Chapter Five",
            action="complete O/E/C",
        )
    for gap in auditor.cluster_gaps:
        _add_finding(
            findings,
            check="CORE-TRACE",
            term=gap.get("cluster", ""),
            current_layer="Chapter Five",
            line=0,
            message=f"Cluster segmentation: missing {', '.join(gap.get('missing_terms', []))}",
            severity="review",
            expected_layer="joint cluster invocation",
            action="reference cluster members together",
        )
    return counts


def run_cjs_placement(root: Path, findings: list[Finding]) -> int:
    hits: list[str] = []
    hits.extend(cjs_placement.audit_cjs3_op_clusters(root))
    hits.extend(cjs_placement.audit_cjs3_letter_headings(root))
    hits.extend(cjs_placement.audit_cjs3_compass_and_frames(root))
    hits.extend(cjs_placement.audit_letter_cluster_citations(root))
    for hit in hits:
        file_part, line, message = _split_audit_hit(hit)
        _add_finding(
            findings,
            check="CJS-PLACEMENT",
            term="(cluster placement)",
            current_layer=file_part,
            line=line,
            message=message,
            severity="error",
            expected_layer="corpus_joint_structure/cjs_03*.md",
            action="relocate to CJS-3",
        )
    return len(hits)


def run_cjs_trace(root: Path, findings: list[Finding]) -> dict[str, int]:
    auditor = Ch1Cjs3AlignmentAuditor(root)
    auditor.run()
    counts = {key: len(items) for key, items in auditor.gaps.items()}
    for gap in auditor.gaps.get("weak_trace", []):
        _add_finding(
            findings,
            check="CJS-TRACE",
            term=gap.get("cluster_id", ""),
            current_layer=gap.get("file", ""),
            line=int(gap.get("line", 0)),
            message=gap.get("issue", "Weak Chapter One trace"),
            severity="review",
            expected_layer="direct Chapter One citation in Trace",
            action="add Read it with / Chapter One basis",
        )
    for gap in auditor.gaps.get("op_component_gap", []):
        _add_finding(
            findings,
            check="CJS-TRACE",
            term=gap.get("rule", gap.get("cluster_id", "")),
            current_layer=gap.get("file", ""),
            line=int(gap.get("line", 0)),
            message=f"Missing oDef guidepost components: {', '.join(gap.get('missing', []))}",
            severity="error",
            expected_layer="complete What it is / How to measure and assess / What must hold",
            action="complete guidepost oDef entry",
        )
    for gap in auditor.gaps.get("overreach", []):
        _add_finding(
            findings,
            check="CJS-TRACE",
            term=gap.get("cluster_id", ""),
            current_layer=gap.get("file", ""),
            line=int(gap.get("line", 0)),
            message=gap.get("issue", "Potential overreach language"),
            severity="error",
            expected_layer="operational layer only",
            action="remove supremacy/overreach language",
        )
    for gap in auditor.gaps.get("inventory", []):
        _add_finding(
            findings,
            check="CJS-PLACEMENT",
            term=gap.get("cluster_id", ""),
            current_layer=gap.get("file", "corpus_joint_structure"),
            line=int(gap.get("line", 0)),
            message=gap.get("issue", "Cluster inventory mismatch"),
            severity="error",
            expected_layer="CJS-3.2–CJS-3.23 inventory",
            action="fix cluster heading inventory",
        )
    return counts


def run_cjs_constitutional_creep(
    ch5_lookup: dict[str, Ch5Entry],
    clusters: list[Cjs3Cluster],
    findings: list[Finding],
) -> int:
    count = 0
    for cluster in clusters:
        if cluster.cluster_id in {"CJS-3.0", "CJS-3.1"}:
            continue
        for rule in cluster.rules:
            key = normalize_term_label(rule.label)
            ch5 = ch5_lookup.get(key)
            if ch5 is None:
                continue
            has_ch5_link = bool(rule.ch5_links or cluster.ch5_links)
            read_with_ch5 = any("chapter five" in item.lower() or "core_05" in item.lower() for item in cluster.read_with)
            if not has_ch5_link and not read_with_ch5 and rule.complete:
                count += 1
                _add_finding(
                    findings,
                    check="CJS-CONSTITUTIONAL-CREEP",
                    term=rule.label,
                    current_layer=cluster.file,
                    line=rule.line,
                    message=(
                        f"CJS-3 rule label matches Chapter Five term {ch5.term!r} "
                        f"but lacks explicit Chapter Five pointer; risk of competing constitutional gloss."
                    ),
                    severity="review",
                    expected_layer=ch5.source_file,
                    action="add Chapter Five pointer; keep OP operational only",
                )
    return count


def run_impl_competing_gloss(root: Path, findings: list[Finding]) -> int:
    count = 0
    for rel in binding_corpus_scope(root):
        path = root / rel
        if not path.is_file():
            continue
        for hit in scan_file(root, path):
            file_part, line = _parse_location(hit)
            count += 1
            _add_finding(
                findings,
                check="IMPL-COMPETING-GLOSS",
                term="(O/E/C block)",
                current_layer=file_part,
                line=line,
                message=hit.split(":", 2)[-1].strip() if hit.count(":") >= 2 else hit,
                severity="review",
                expected_layer="Chapter Five canonical home",
                action="replace with pointer to Chapter Five",
            )
    return count


def _normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower()).strip()


def _strip_details(text: str) -> str:
    text = re.sub(r"<details>.*?</details>", "", text, flags=re.S)
    text = re.sub(r"</?[^>]+>", " ", text)
    return text


def _operative_relocation_body(body: str) -> str:
    return strip_cjs_pointer_sentences(strip_relocation_details(body))


def _has_relocation_pointer_discipline(operative_body: str) -> bool:
    haystack = _normalize(operative_body)
    return any(phrase in haystack for phrase in POINTER_DISCIPLINE_PHRASES)


def _relocation_score(operative_body: str) -> tuple[int, list[str]]:
    haystack = operative_body
    score = 0
    signals: list[str] = []
    for signal_name, needles, weight in RELOCATION_SIGNALS:
        hits = count_occurrences(haystack, needles)
        if hits:
            score += min(hits, 4) * weight
            signals.append(signal_name)
    keep_hits = sum(1 for needle in KEEP_SIGNALS if needle in _normalize(haystack))
    if keep_hits and score < 9:
        score -= min(keep_hits, 2)
    return max(score, 0), signals


def _escalate_to_ch5(operative_body: str) -> bool:
    haystack = _normalize(operative_body)
    if DEFINITIONAL_LEADIN_RE.search(operative_body):
        return True
    if OEC_BLOCK_RE.search(operative_body, re.M):
        return True
    return any(keyword in haystack for keyword in CH5_ESCALATION_KEYWORDS)


@dataclass
class ImplSection:
    file: str
    section_id: str
    title: str
    start_line: int
    body: str


def _extract_impl_sections(root: Path, subdir: str, prefix: str) -> list[ImplSection]:
    base = root / subdir
    if not base.is_dir():
        return []
    sections: list[ImplSection] = []
    heading_re = re.compile(rf"^(#{{2,3}})\s+({prefix}-\d+(?:\.\d+)*):?\s+(.+)$")
    for path in sorted(base.glob("*.md")):
        rel = path.relative_to(root).as_posix()
        lines = path.read_text(encoding="utf-8").splitlines()
        starts: list[tuple[int, str, str]] = []
        for idx, line in enumerate(lines):
            match = heading_re.match(line)
            if match:
                starts.append((idx, match.group(2), match.group(3).strip()))
        for pos, (start_idx, section_id, title) in enumerate(starts):
            end_idx = starts[pos + 1][0] if pos + 1 < len(starts) else len(lines)
            body = "\n".join(lines[start_idx + 1 : end_idx])
            sections.append(
                ImplSection(
                    file=rel,
                    section_id=section_id,
                    title=title,
                    start_line=start_idx + 1,
                    body=body,
                )
            )
    return sections


def run_impl_relocation(root: Path, findings: list[Finding]) -> int:
    """Flag CI sections that may restate shared CJS doctrine without pointer discipline.

    CS and CF owner layers are out of scope here; they are checked via integration
    maps and `ci-cjs-relocation-audit`. Scoring uses operative body text after
    stripping Trace widgets and accepted CJS pointer sentences.
    """
    count = 0
    for section in _extract_impl_sections(root, "corpus_institutions", "CI"):
        operative_body = _operative_relocation_body(section.body)
        if _has_relocation_pointer_discipline(operative_body):
            continue
        if len(relocation_words(operative_body)) < 8:
            continue
        score, signals = _relocation_score(operative_body)
        if score < RELOCATION_MIN_SCORE:
            continue
        escalate = _escalate_to_ch5(operative_body)
        expected = "core_05 band file" if escalate else "corpus_joint_structure/cjs_03*.md"
        action = "escalate-to-Ch5" if escalate else "split-or-pointer-to-CJS"
        count += 1
        _add_finding(
            findings,
            check="IMPL-RELOCATION",
            term=section.section_id,
            current_layer=section.file,
            line=section.start_line,
            message=(
                f"Cross-layer relocation candidate (score={score}; signals={', '.join(signals)}): "
                f"{section.title}"
            ),
            severity="review",
            expected_layer=expected,
            action=action,
        )
    return count


def run_impl_non_redefinition(
    root: Path,
    ch5_lookup: dict[str, Ch5Entry],
    findings: list[Finding],
) -> int:
    count = 0
    ch5_terms_sorted = sorted(ch5_lookup.keys(), key=len, reverse=True)
    for rel in binding_corpus_scope(root):
        if rel in CH5_OWNERS or rel.startswith("core_02-03") or rel.startswith("core_04-04"):
            continue
        path = root / rel
        if not path.is_file() or not any(rel.startswith(d) for d in IMPL_DIRS):
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        for idx, line in enumerate(lines, start=1):
            stripped = line.strip()
            if OEC_BLOCK_RE.match(stripped):
                continue
            for match in DEFINITIONAL_LEADIN_RE.finditer(line):
                term_raw = (match.group("term") or match.group("term2") or "").strip()
                key = normalize_term_label(term_raw)
                if key not in ch5_lookup:
                    continue
                ch5 = ch5_lookup[key]
                count += 1
                _add_finding(
                    findings,
                    check="IMPL-NON-REDEFINITION",
                    term=ch5.term,
                    current_layer=rel,
                    line=idx,
                    message=f"Definitional lead-in for Chapter Five term outside canonical home: {stripped[:160]}",
                    severity="review",
                    expected_layer=ch5.source_file,
                    action="replace with pointer to Chapter Five canonical home",
                )
            lowered = stripped.lower()
            for term_key in ch5_terms_sorted:
                ch5 = ch5_lookup[term_key]
                if len(term_key) < 6:
                    continue
                if term_key in lowered and any(
                    phrase in lowered
                    for phrase in ("must not redefine", "does not redefine", "not a second home", "apply chapter five")
                ):
                    continue
                if re.search(rf"\b{re.escape(ch5.term)}\b.*\b(?:means|is defined as|refers to)\b", line, re.I):
                    count += 1
                    _add_finding(
                        findings,
                        check="IMPL-NON-REDEFINITION",
                        term=ch5.term,
                        current_layer=rel,
                        line=idx,
                        message=f"Possible competing definition prose for canonical term: {stripped[:160]}",
                        severity="review",
                        expected_layer=ch5.source_file,
                        action="replace with pointer",
                    )
                    break
    return count


def run_subprocess_placement_audits(root: Path, findings: list[Finding]) -> dict[str, int]:
    """Run blocking Ch5 placement audits via subprocess; capture failures as findings."""
    scripts = (
        ("CORE-PLACEMENT", "tools/ch5_single_definition_audit.py"),
        ("CORE-PLACEMENT", "tools/ch5_constitutional_cluster_audit.py"),
    )
    counts: dict[str, int] = {"CORE-PLACEMENT": 0}
    for check, script in scripts:
        result = subprocess.run(
            [sys.executable, str(root / script), "--root", str(root)],
            capture_output=True,
            text=True,
            cwd=root,
        )
        if result.returncode == 0:
            continue
        output = (result.stdout + result.stderr).strip()
        for line in output.splitlines():
            line = line.strip()
            if not line or line.startswith("-") and "Result:" in line:
                continue
            if line.startswith("- "):
                line = line[2:]
            file_part, line_no = _parse_location(line)
            counts["CORE-PLACEMENT"] += 1
            _add_finding(
                findings,
                check=check,
                term="(Chapter Five structure)",
                current_layer=file_part if "/" in file_part or file_part.endswith(".md") else script,
                line=line_no,
                message=line,
                severity="error",
                expected_layer="Chapter Five band file",
                action="fix Chapter Five placement invariant",
            )
    return counts


def merge_ledger(root: Path, run: AuditRun) -> dict[str, Any]:
    ledger_file = root / LEDGER_PATH
    ledger_file.parent.mkdir(parents=True, exist_ok=True)
    if ledger_file.is_file():
        ledger = json.loads(ledger_file.read_text(encoding="utf-8"))
    else:
        ledger = {"schema_version": LEDGER_SCHEMA_VERSION, "last_run": "", "findings": []}

    existing_by_id = {item["finding_id"]: item for item in ledger.get("findings", [])}
    seen_ids: set[str] = set()
    regressions: list[str] = []

    for finding in run.findings:
        seen_ids.add(finding.finding_id)
        if finding.finding_id in existing_by_id:
            record = existing_by_id[finding.finding_id]
            record["last_seen"] = run.timestamp
            record["message"] = finding.message
            record["severity"] = finding.severity
            if record.get("status") == "resolved":
                record["status"] = "open"
                record.pop("resolved_in", None)
                regressions.append(finding.finding_id)
        else:
            existing_by_id[finding.finding_id] = {
                "finding_id": finding.finding_id,
                "check": finding.check,
                "term": finding.term,
                "current_layer": finding.current_layer,
                "expected_layer": finding.expected_layer,
                "severity": finding.severity,
                "status": "open",
                "action": finding.action,
                "first_seen": run.timestamp,
                "last_seen": run.timestamp,
                "notes": "",
                "message": finding.message,
                "line": finding.line,
            }

    for finding_id, record in existing_by_id.items():
        if finding_id not in seen_ids and record.get("status") == "open":
            record["status"] = "stale"
            record["last_seen"] = run.timestamp

    ledger["schema_version"] = LEDGER_SCHEMA_VERSION
    ledger["last_run"] = run.timestamp
    ledger["findings"] = sorted(existing_by_id.values(), key=lambda item: item["finding_id"])
    ledger_file.write_text(json.dumps(ledger, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    run.regressions = regressions
    return ledger


def build_matrix_rows(
    ch5_entries: list[Ch5Entry],
    cjs3_clusters: list[Cjs3Cluster],
    findings: list[Finding],
) -> list[dict[str, str]]:
    finding_by_term: dict[str, list[str]] = {}
    for finding in findings:
        key = finding.term.casefold()
        finding_by_term.setdefault(key, []).append(finding.finding_id)

    rows: list[dict[str, str]] = []
    for entry in ch5_entries:
        related_clusters = [
            c.cluster_id
            for c in cjs3_clusters
            if any(normalize_term_label(r.label) == entry.term.casefold() for r in c.rules)
        ]
        ids = finding_by_term.get(entry.term.casefold(), [])
        status = "ok" if not ids else "review"
        rows.append(
            {
                "term": entry.term,
                "kind": "constitutional",
                "constitutional_home": entry.source_file,
                "cjs_cluster": ";".join(related_clusters),
                "impl_references": "",
                "placement_status": status,
                "finding_ids": ";".join(ids),
            }
        )

    for cluster in cjs3_clusters:
        if cluster.cluster_id in {"CJS-3.0", "CJS-3.1"}:
            continue
        ids = [
            f.finding_id
            for f in findings
            if f.term == cluster.cluster_id or f.current_layer == cluster.file and f.line >= cluster.start_line
        ]
        status = "ok" if not ids else "review"
        rows.append(
            {
                "term": cluster.cluster_id,
                "kind": "operational_cluster",
                "constitutional_home": "",
                "cjs_cluster": cluster.cluster_id,
                "impl_references": cluster.file,
                "placement_status": status,
                "finding_ids": ";".join(sorted(set(ids))),
            }
        )
    return rows


def write_report(output_dir: Path, run: AuditRun, ledger: dict[str, Any]) -> Path:
    path = output_dir / f"definition_appropriateness_report_{run.timestamp}.md"
    by_check: dict[str, int] = {}
    for finding in run.findings:
        by_check[finding.check] = by_check.get(finding.check, 0) + 1

    open_count = sum(1 for item in ledger["findings"] if item.get("status") == "open")
    stale_count = sum(1 for item in ledger["findings"] if item.get("status") == "stale")

    lines = [
        "# Definition Appropriateness Audit Report",
        "",
        f"**Date:** {run.timestamp}",
        f"**Workflow:** {WORKFLOW}",
        "**Auditor:** Automated unified definition placement and anti-redefinition pass",
        "",
        "## Executive Summary",
        "",
        "| Metric | Result |",
        "|---|---:|",
        f"| Chapter Five terms indexed | {len(run.ch5_entries)} |",
        f"| CJS-3 clusters indexed | {len(run.cjs3_clusters)} |",
        f"| Findings this run | {len(run.findings)} |",
        f"| Ledger open findings | {open_count} |",
        f"| Ledger stale findings | {stale_count} |",
        f"| Regressions (resolved → reopened) | {len(run.regressions)} |",
        "",
        "## Findings by Check",
        "",
        "| Check | Count |",
        "|---|---:|",
    ]
    for check, count in sorted(by_check.items()):
        lines.append(f"| {check} | {count} |")
    lines.extend(["", "## Top Findings", ""])
    for finding in run.findings[:40]:
        lines.append(
            f"- **{finding.check}** `{finding.finding_id}` — {finding.term} @ "
            f"`{finding.current_layer}:{finding.line}`: {finding.message}"
        )
    if len(run.findings) > 40:
        lines.append(f"- … and {len(run.findings) - 40} more (see log JSON)")
    lines.extend(
        [
            "",
            "## Manual Review Notes",
            "",
            "Review CJS-3.7–5.10, 5.11–5.13, 5.16–5.18, and 5.19–5.21 cluster families for semantic adequacy.",
            "Treat `weak_trace` and `IMPL-RELOCATION` hits as advisory unless escalation to Chapter Five is indicated.",
            "`IMPL-RELOCATION` scopes to **CI** sections with relocation score >= 16 on operative body text (CS/CF owner layers excluded; see `ci-cjs-relocation-audit`).",
            "Update `evidence/definition_audit/ledger.json` statuses (`accepted`, `deferred`, `resolved`) after triage.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def write_matrix(output_dir: Path, run: AuditRun, rows: list[dict[str, str]]) -> Path:
    path = output_dir / f"definition_appropriateness_matrix_{run.timestamp}.csv"
    fieldnames = [
        "term",
        "kind",
        "constitutional_home",
        "cjs_cluster",
        "impl_references",
        "placement_status",
        "finding_ids",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return path


def write_log(output_dir: Path, run: AuditRun, ledger: dict[str, Any]) -> Path:
    path = output_dir / f"definition_appropriateness_log_{run.timestamp}.json"
    payload = {
        "timestamp": run.timestamp,
        "workflow": WORKFLOW,
        "metrics": run.metrics,
        "ch5_definition_count": len(run.ch5_entries),
        "cjs3_cluster_count": len(run.cjs3_clusters),
        "findings": [asdict(f) for f in run.findings],
        "regressions": run.regressions,
        "ledger_summary": {
            "open": sum(1 for item in ledger["findings"] if item.get("status") == "open"),
            "stale": sum(1 for item in ledger["findings"] if item.get("status") == "stale"),
            "accepted": sum(1 for item in ledger["findings"] if item.get("status") == "accepted"),
            "deferred": sum(1 for item in ledger["findings"] if item.get("status") == "deferred"),
            "resolved": sum(1 for item in ledger["findings"] if item.get("status") == "resolved"),
        },
    }
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return path


def main() -> int:
    args = parse_args()
    root = Path(args.repo_root).resolve()
    timestamp = datetime.now().strftime("%Y-%m-%d")
    output_dir = Path(args.output_dir) if args.output_dir else root / "evidence" / timestamp
    output_dir.mkdir(parents=True, exist_ok=True)

    run = AuditRun(timestamp=timestamp)
    run.ch5_entries = collect_ch5_entries(root)
    run.cjs3_clusters = collect_cjs3_clusters(root)
    ch5_lookup = ch5_term_lookup(run.ch5_entries)
    # Include Tetrad apex leg heads (not ####-indexed) so bare oDef labels like
    # "Participation" are caught as competing-gloss risks.
    creep_lookup = ch5_term_lookup_with_tetrad_apex(run.ch5_entries)

    if not args.skip_subprocess_audits:
        run.metrics["core_placement"] = run_subprocess_placement_audits(root, run.findings)

    run.metrics["core_gravity"] = run_core_gravity(root, run.findings)
    run.metrics["core_trace"] = run_core_trace(root, run.findings)
    run.metrics["cjs_placement"] = run_cjs_placement(root, run.findings)
    run.metrics["cjs_trace"] = run_cjs_trace(root, run.findings)
    run.metrics["cjs_constitutional_creep"] = run_cjs_constitutional_creep(
        creep_lookup, run.cjs3_clusters, run.findings
    )
    run.metrics["impl_competing_gloss"] = run_impl_competing_gloss(root, run.findings)
    run.metrics["impl_relocation"] = run_impl_relocation(root, run.findings)
    run.metrics["impl_non_redefinition"] = run_impl_non_redefinition(root, ch5_lookup, run.findings)

    ledger = merge_ledger(root, run)
    matrix_rows = build_matrix_rows(run.ch5_entries, run.cjs3_clusters, run.findings)

    report_path = write_report(output_dir, run, ledger)
    matrix_path = write_matrix(output_dir, run, matrix_rows)
    log_path = write_log(output_dir, run, ledger)

    print(f"Definition appropriateness audit complete ({len(run.findings)} findings).")
    print(f"- Report: {report_path}")
    print(f"- Matrix: {matrix_path}")
    print(f"- Log: {log_path}")
    print(f"- Ledger: {root / LEDGER_PATH}")

    if args.strict and any(f.severity == "error" for f in run.findings):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
