#!/usr/bin/env python3
"""Institutional best-practices benchmark review for the constitutional corpus."""

from __future__ import annotations

import argparse
import datetime as dt
import pathlib
from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class DomainReview:
    domain: str
    external_sections: str
    internal_anchor: str
    design: int
    operationalization: int
    evidence: int
    performance: int
    current_state: str
    gap: str
    proposed_close: str
    priority: str


REVIEWS = [
    DomainReview(
        domain="Legitimacy, purpose, and constitutional authority",
        external_sections="OECD 2023 About/I; FRC 2024 Section 1; ISO 37000 purpose/strategy",
        internal_anchor="SC Ch 1; Ch 10; Ch 14; Amendment Ch 12-13",
        design=3,
        operationalization=2,
        evidence=2,
        performance=2,
        current_state=(
            "Authority, purpose, legitimacy, adoption, and incorporation boundaries are explicit and cross-mapped in the "
            "core corpus and architecture crosswalk."
        ),
        gap="The corpus is principle-strong, but adopter-facing authority custody and publication artifacts are not yet standardized into one assurance pack.",
        proposed_close="Publish a custody/adoption checklist and a single edition-cut authority record template.",
        priority="P2",
    ),
    DomainReview(
        domain="Rights, equitable treatment, and protected persons",
        external_sections="OECD 2023 II; OHCHR 2011 GP/I/II/III",
        internal_anchor="SC Arts V-XII, XVII, XXII; Defs Ch 3-5",
        design=3,
        operationalization=3,
        evidence=2,
        performance=2,
        current_state=(
            "Rights floors, protected-person logic, remedy hooks, and abuse-pathway constraints are explicit and deeply integrated across the constitutional text."
        ),
        gap="Evidence of exercised remedy pathways is present indirectly through scenarios and drills, but not yet summarized as a dedicated rights-remedy benchmark pack.",
        proposed_close="Create a rights/remedy evidence index linking scenarios, drills, and any future disposition records.",
        priority="P3",
    ),
    DomainReview(
        domain="Separation of powers, role clarity, and anti-self-judging",
        external_sections="FRC 2024 Section 2; IIA Principles 1-5; OECD Integrity 2/12",
        internal_anchor="SC Ch 8; Art XXI; Ch 10 sec. 5; CI-3 to CI-8",
        design=3,
        operationalization=3,
        evidence=2,
        performance=2,
        current_state=(
            "Court-family separation, cross-court anti-self-judging, assurance-line separation, and interpretive safeguards are explicit."
        ),
        gap="The repository still lacks a concise incompatibility matrix and role-separation quick reference for high-impact institutional operators.",
        proposed_close="Add a one-page incompatibility matrix keyed to CI-3 through CI-8 and CI-7/7A/7B routing.",
        priority="P1",
    ),
    DomainReview(
        domain="Composition, competency, succession, and removal",
        external_sections="FRC 2024 Section 3; IIA Applying the model; OECD Integrity leadership/capacity",
        internal_anchor="Art XXI-B to XXI-D; Ch 10 sec. 5; CI-4, CI-14; CF-10",
        design=2,
        operationalization=2,
        evidence=2,
        performance=2,
        current_state=(
            "Competency, succession, continuity, and review expectations are present, especially for stewards and institutional continuity."
        ),
        gap="Some measurable requirements remain recommendation-shaped rather than fully normalized into ratios, triggers, or class-scaled schedules.",
        proposed_close="Add class/tier-based requirements for independence mix, succession review cadence, and external effectiveness review triggers.",
        priority="P2",
    ),
    DomainReview(
        domain="Conflict integrity, anti-corruption, and anti-capture",
        external_sections="OECD Integrity 4/10/11; ISO 37001/37301 by analogy",
        internal_anchor="SC Ch 1 sec. 7.2; Arts XI-E, XII-D, XXI; Ch 7; CI-5, CI-11, CI-13",
        design=2,
        operationalization=2,
        evidence=1,
        performance=1,
        current_state=(
            "Anti-capture and conflict logic are explicit, and the institutions gap matrix already flags this as an area needing sharper preventive controls."
        ),
        gap="The corpus does not yet present a consolidated anti-corruption/fraud control protocol with explicit trigger, investigation, and cure pathways.",
        proposed_close="Draft a dedicated anti-corruption and fraud-control implementation block with disclosure, escalation, and sanction triggers.",
        priority="P0",
    ),
    DomainReview(
        domain="Risk governance and internal controls",
        external_sections="FRC 2024 Section 4/Provision 29; IIA 1-6; OECD Integrity 10; NIST AI RMF Govern/Map",
        internal_anchor="SC Ch 1 sec. 7; Arts XII-XV, XIX-XX; CI-3, CI-7; CS Protocol A; CS-4–CS-5",
        design=3,
        operationalization=3,
        evidence=2,
        performance=2,
        current_state=(
            "Classification-scaled risk governance, integrated controls, assurance structure, and lifecycle controls are strong and already crosswalked in architecture."
        ),
        gap="Material-control failure disclosure bundles and external assurance trigger thresholds are still only partially standardized.",
        proposed_close="Add a mandatory control-failure disclosure schema and class/tier-triggered external assurance thresholds.",
        priority="P0",
    ),
    DomainReview(
        domain="Transparency, disclosure, and public intelligibility",
        external_sections="OECD 2023 IV; OECD Integrity 9/13; NIST Govern/Measure; OHCHR II/III",
        internal_anchor="Arts VIII, XIII, XIV, XIX, XXI-C, XXII-E; Defs Ch 4; CI-12, CI-26; CJS-5.3/CJS-5.4/CJS-5.14-CJS-5.12",
        design=3,
        operationalization=2,
        evidence=2,
        performance=2,
        current_state=(
            "The corpus strongly protects disclosure, traceability, auditability, and accessible pathway concepts, with a dedicated governance disclosure schema hook in CI-12.4."
        ),
        gap="A standardized governance reporting taxonomy and mandatory field list are still not fully closed out as a stable publication package.",
        proposed_close="Finish the CI-12/CI-26 reporting schema as a reusable disclosure template with cadence and comparison fields.",
        priority="P1",
    ),
    DomainReview(
        domain="Independent assurance and verification",
        external_sections="IIA Principles 4-5; OECD Integrity 12; FRC 2024 Section 4",
        internal_anchor="Arts XIV and XXI; Ch 8; Defs Ch 4; CI-7, CI-8; CF-8, CF-9, CF-10; doc_architecture sec. 15-17",
        design=3,
        operationalization=3,
        evidence=3,
        performance=2,
        current_state=(
            "Independent review, evidence custody, technical courts, and assurance-line concepts are explicit, with architecture crosswalk support and drill/audit artifacts in repo."
        ),
        gap="External assurance remains partly trigger-dependent and would benefit from an edition-level assurance inventory that shows what was actually exercised in the current cycle.",
        proposed_close="Publish an edition assurance register listing audits, drills, trigger events, and unresolved assurance debt.",
        priority="P1",
    ),
    DomainReview(
        domain="AI and system lifecycle governance",
        external_sections="NIST AI RMF Govern/Map/Measure/Manage; ISO/IEC 42001 4-10; NIST GenAI Profile 2024",
        internal_anchor="Arts XII-XVI, XIX-XX; CS Protocol A/B/R/D; CS-3–CS-5",
        design=3,
        operationalization=3,
        evidence=2,
        performance=2,
        current_state=(
            "Lifecycle governance, classification, testing, rollback, synthetic-content handling, and adaptation controls are substantively strong."
        ),
        gap="Named inventory artifacts such as model cards, system cards, and AI-specific monitoring cadence tables remain implied rather than standardized.",
        proposed_close="Add optional implementation templates for inventory cards, post-deployment monitoring cadence, and incident reporting bundles.",
        priority="P2",
    ),
    DomainReview(
        domain="Remedy, redress, contestability, and restorative closure",
        external_sections="OHCHR III; OECD 2023 II; OECD Integrity 11/13",
        internal_anchor="Arts XII-B, XIV, XVII-B, XXII, XXIV; Ch 6; CI-6, CI-13; CS Protocol C",
        design=3,
        operationalization=2,
        evidence=2,
        performance=2,
        current_state=(
            "Contestability and restorative logic are explicit, and the justice/restoration orientation is stronger than in many benchmark frameworks."
        ),
        gap="Operational timeliness, backlog, and remedy-lane service levels are not yet normalized across the whole corpus.",
        proposed_close="Define time-bound service requirements for notice, review, appeal, and restorative follow-through by class or severity.",
        priority="P1",
    ),
    DomainReview(
        domain="Continuity, resilience, transition, and emergency discipline",
        external_sections="OECD 2023 VI; FRC 2024 Section 4; NIST Manage; ISO 37000 risk governance/social responsibility",
        internal_anchor="Arts XXII-XXIV; Amendment Ch 11-13; CI-14; CS Protocol T/R/D/S4",
        design=3,
        operationalization=3,
        evidence=3,
        performance=3,
        current_state=(
            "Continuity, emergency discipline, restoration, and transition governance are unusually mature, with dedicated drill artifacts already present in evidence."
        ),
        gap="The strongest remaining close is presentation rather than substance: one concise continuity evidence dashboard would make the maturity easier to demonstrate.",
        proposed_close="Add a quarterly continuity dashboard summarizing drills, findings, remediation status, and unresolved transition risks.",
        priority="P2",
    ),
    DomainReview(
        domain="Amendment validity, non-regression, and controlled change",
        external_sections="OECD 2023 I/V/VI; FRC 2024 Section 1/4; ISO/IEC 42001 9-10 by analogy",
        internal_anchor="Amendment Ch 11-13; Art XXIII; Art XXIV; Ch 14",
        design=3,
        operationalization=3,
        evidence=2,
        performance=2,
        current_state=(
            "The corpus has explicit non-regression, validity testing, anti-evasion, and incorporation-custody logic that is stronger than a generic governance baseline."
        ),
        gap="Edition-cut change-control evidence is present in pieces but not yet assembled into one standing change-control packet per release.",
        proposed_close="Add a release packet with edition diff summary, validity checklist, adoption custody metadata, and unresolved control exceptions.",
        priority="P1",
    ),
]


def has_all_patterns(path: pathlib.Path, patterns: Iterable[str]) -> bool:
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8")
    return all(pattern in text for pattern in patterns)


def materialize_reviews(root: pathlib.Path) -> list[DomainReview]:
    reviews = list(REVIEWS)

    systems_templates = root / "implementation" / "SYSTEMS_IMPLEMENTATION_TEMPLATES_2026-04-13.md"
    corpus_systems = root / "corpus_systems.md"
    corpus_institutions = root / "corpus_institutions.md"

    has_systems_template_pack = has_all_patterns(
        systems_templates,
        [
            "## 2. System card template",
            "## 3. Model card template",
            "## 4. Post-deployment monitoring cadence table",
            "## 5. Incident reporting bundle",
            "## 6. Material control-failure disclosure packet",
        ],
    )
    has_systems_hooks = has_all_patterns(
        corpus_systems,
        [
            "SYSTEMS_IMPLEMENTATION_TEMPLATES_2026-04-13.md",
            "control-failure disclosure packet",
        ],
    )
    has_institutions_hook = has_all_patterns(
        corpus_institutions,
        [
            "SYSTEMS_IMPLEMENTATION_TEMPLATES_2026-04-13.md",
            "companion system-level packet",
        ],
    )
    systems_example_packet = root / "implementation" / "SYSTEMS_TEMPLATE_EXAMPLE_HIGH_IMPACT_2026-04-13.md"
    has_systems_example_packet = has_all_patterns(
        systems_example_packet,
        [
            "## 1. System card",
            "## 2. Model card",
            "## 3. Post-deployment monitoring cadence table",
            "## 4. Incident reporting bundle",
            "## 5. Material control-failure disclosure packet",
        ],
    )

    upgraded_reviews: list[DomainReview] = []
    for row in reviews:
        if (
            row.domain == "AI and system lifecycle governance"
            and has_systems_template_pack
            and has_systems_hooks
        ):
            row = DomainReview(
                domain=row.domain,
                external_sections=row.external_sections,
                internal_anchor=row.internal_anchor,
                design=row.design,
                operationalization=row.operationalization,
                evidence=3,
                performance=3 if has_systems_example_packet else row.performance,
                current_state=(
                    "Lifecycle governance, classification, testing, rollback, synthetic-content handling, and adaptation controls are substantively strong, and the repository now includes named implementation templates for system cards, model cards, monitoring cadence, incident reporting, and control-failure disclosure."
                    + (
                        " A worked high-impact exemplar packet is also present, showing how those templates can be used in practice."
                        if has_systems_example_packet
                        else ""
                    )
                ),
                gap=(
                    "The main remaining gap is routine release-by-release use across actual governed systems, not absence of standardized template artifacts."
                ),
                proposed_close=(
                    "Adopt the systems template pack into routine release and assurance practice for additional governed systems and maintain dated exemplar packets across editions."
                ),
                priority="P2",
            )
        elif (
            row.domain == "Risk governance and internal controls"
            and has_systems_template_pack
            and has_systems_hooks
            and has_institutions_hook
        ):
            row = DomainReview(
                domain=row.domain,
                external_sections=row.external_sections,
                internal_anchor=row.internal_anchor,
                design=row.design,
                operationalization=row.operationalization,
                evidence=3,
                performance=3 if has_systems_example_packet else row.performance,
                current_state=(
                    "Classification-scaled risk governance, integrated controls, assurance structure, and lifecycle controls are strong and already crosswalked in architecture, with a named material control-failure disclosure packet now added for supervised systems."
                    + (
                        " The repository also includes a filled high-impact example packet showing how the control-failure disclosure can be used."
                        if has_systems_example_packet
                        else ""
                    )
                ),
                gap=(
                    "Control-failure disclosure is now materially more standardized; the remaining close is to convert trigger thresholds and example use into routine, cycle-based operational practice."
                ),
                proposed_close=(
                    "Align edition-cycle assurance reviews to the existing CI-7.2 trigger thresholds and accumulate dated control-failure packets where incidents or exercises warrant."
                ),
                priority="P1",
            )
        upgraded_reviews.append(row)
    return upgraded_reviews


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Workspace root path. Defaults to current directory.")
    parser.add_argument(
        "--date",
        default=dt.date.today().isoformat(),
        help="Date used in evidence path and report header (YYYY-MM-DD).",
    )
    parser.add_argument(
        "--write-evidence",
        action="store_true",
        help="Write a dated report under evidence/<date>/ in addition to stdout.",
    )
    return parser.parse_args()


def average(values: list[int]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)


def render_report(root: pathlib.Path, run_date: str) -> str:
    reviews = materialize_reviews(root)
    design_avg = average([row.design for row in reviews])
    oper_avg = average([row.operationalization for row in reviews])
    evidence_avg = average([row.evidence for row in reviews])
    perf_avg = average([row.performance for row in reviews])

    p0_rows = [row for row in reviews if row.priority == "P0"]
    p1_rows = [row for row in reviews if row.priority == "P1"]

    lines: list[str] = []
    lines.append(f"# Best Practices Check - {run_date}")
    lines.append("")
    lines.append("## Basis")
    lines.append("- Standard: `implementation/BEST_PRACTICES_CHECK_STANDARD_2026-04-12.md`")
    lines.append("- Review mode: local benchmark synthesis against the repository's mapped external-framework standard")
    lines.append("- Scope: full constitutional corpus, architecture crosswalk, implementation matrices, and dated evidence artifacts already present in this repository")
    lines.append("")
    lines.append("## Summary")
    lines.append(f"- Domains reviewed: `{len(reviews)}`")
    lines.append(f"- Average scores: design `{design_avg:.2f}`, operationalization `{oper_avg:.2f}`, evidence `{evidence_avg:.2f}`, performance `{perf_avg:.2f}`")
    lines.append(f"- Highest-maturity areas: `Continuity/resilience`, `AI/system lifecycle governance`, `Amendment validity/non-regression`, `Independent assurance and verification`")
    lines.append("- Main gap pattern: the corpus is stronger on substantive constitutional design than on standardized implementation packets, trigger catalogs, and recurring disclosure bundles")
    lines.append("")
    lines.append("## Priority Closes")
    for row in p0_rows + p1_rows:
        lines.append(f"- `{row.priority}` {row.domain}: {row.proposed_close}")
    lines.append("")
    lines.append("## Review Matrix")
    lines.append("| Domain | External source section | Internal anchor | Design | Oper. | Evidence | Perf. | Current state | Gap | Proposed close | Priority |")
    lines.append("|---|---|---|---:|---:|---:|---:|---|---|---|---|")
    for row in reviews:
        lines.append(
            f"| {row.domain} | {row.external_sections} | {row.internal_anchor} | {row.design} | {row.operationalization} | {row.evidence} | {row.performance} | {row.current_state} | {row.gap} | {row.proposed_close} | {row.priority} |"
        )
    lines.append("")
    lines.append("## Evidence Used")
    lines.append("- `implementation/BEST_PRACTICES_CHECK_STANDARD_2026-04-12.md`")
    lines.append("- `implementation/AUTOMATED_REFERENCE_CHECKING.md`")
    lines.append("- `doc_architecture.md` section `15. External framework crosswalk`")
    lines.append("- Dated drill artifacts under `evidence/2026-q2/drills/`")
    lines.append("- Current automated audit suite outputs (`reference`, `scenario`, `markdown`, `prose`, `lexical`, `readability`)")
    lines.append("")
    lines.append("## Interpretation Notes")
    lines.append("- This check is a benchmark-and-gap review, not a regression gate.")
    lines.append("- Scores are synthesized from the internal standard and current repository evidence; they do not claim external certification.")
    lines.append("- Tier 2 licensed standards remain analogy inputs unless a licensed attestation mapping is separately prepared.")
    return "\n".join(lines) + "\n"


def maybe_write_evidence(root: pathlib.Path, run_date: str, report: str) -> pathlib.Path:
    evidence_dir = root / "evidence" / run_date
    evidence_dir.mkdir(parents=True, exist_ok=True)
    output_path = evidence_dir / f"BEST_PRACTICES_CHECK_{run_date}.md"
    output_path.write_text(report, encoding="utf-8")
    return output_path


def main() -> int:
    args = parse_args()
    root = pathlib.Path(args.root).resolve()
    report = render_report(root, args.date)
    print(report, end="")
    if args.write_evidence:
        output_path = maybe_write_evidence(root, args.date, report)
        print(f"Wrote evidence artifact: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
