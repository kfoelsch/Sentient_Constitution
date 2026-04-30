#!/usr/bin/env python3
"""Compute CONSTITUTIONAL_REGRESSION_SCENARIOS.md SCORING-v1 weighted overall (0-10).

Overall = 0.25*Rights + 0.15*Contestability + 0.20*Enforcement
        + 0.15*Boundary + 0.15*Epistemic + 0.10*Continuity
"""

from __future__ import annotations

import argparse
import sys

WEIGHTS = {
    "rights": 0.25,
    "contestability": 0.15,
    "enforcement": 0.20,
    "boundary": 0.15,
    "epistemic": 0.15,
    "continuity": 0.10,
}


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--rights",
        type=float,
        metavar="N",
        required=True,
        help="Rights Floor Integrity (0-10)",
    )
    p.add_argument(
        "--contestability",
        type=float,
        metavar="N",
        required=True,
        help="Contestability / Appeal Practicality (0-10)",
    )
    p.add_argument(
        "--enforcement",
        type=float,
        metavar="N",
        required=True,
        help="Enforcement / Remedy Realism (0-10)",
    )
    p.add_argument(
        "--boundary",
        type=float,
        metavar="N",
        required=True,
        help="Boundary Discipline (0-10)",
    )
    p.add_argument(
        "--epistemic",
        type=float,
        metavar="N",
        required=True,
        help="Epistemic Integrity (0-10)",
    )
    p.add_argument(
        "--continuity",
        type=float,
        metavar="N",
        required=True,
        help="Continuity / Recovery (0-10)",
    )
    p.add_argument(
        "--delta",
        default="N/A",
        help='Delta vs prior run (e.g. "+0.2" or "N/A")',
    )
    p.add_argument(
        "--confidence",
        choices=("low", "medium", "high"),
        default="medium",
        help="Assessor confidence",
    )
    p.add_argument(
        "--markdown",
        action="store_true",
        help="Emit Run Scoring Snapshot markdown block (section 9.3)",
    )
    p.add_argument(
        "--quiet",
        action="store_true",
        help="With --markdown, print only the markdown block (no overall line)",
    )
    return p.parse_args()


def validate(name: str, value: float) -> None:
    if not 0.0 <= value <= 10.0:
        print(f"{name} must be between 0 and 10, got {value}", file=sys.stderr)
        sys.exit(2)


def overall(scores: dict[str, float]) -> float:
    return sum(WEIGHTS[k] * scores[k] for k in WEIGHTS)


def main() -> None:
    args = parse_args()
    scores = {
        "rights": args.rights,
        "contestability": args.contestability,
        "enforcement": args.enforcement,
        "boundary": args.boundary,
        "epistemic": args.epistemic,
        "continuity": args.continuity,
    }
    for k, v in scores.items():
        validate(k, v)
    ov = overall(scores)
    if args.markdown:
        block = f"""- Scoring model version: `SCORING-v1`
- Scenario-Weighted Score (0-10): `{ov:.1f}`
- Rights Floor Integrity (0-10): `{scores["rights"]:.1f}`
- Contestability / Appeal Practicality (0-10): `{scores["contestability"]:.1f}`
- Enforcement / Remedy Realism (0-10): `{scores["enforcement"]:.1f}`
- Boundary Discipline (0-10): `{scores["boundary"]:.1f}`
- Epistemic Integrity (0-10): `{scores["epistemic"]:.1f}`
- Continuity / Recovery (0-10): `{scores["continuity"]:.1f}`
- Delta vs prior comparable run: `{args.delta}`
- Confidence: `{args.confidence}`"""
        if not args.quiet:
            print(f"SCORING-v1 overall: {ov:.2f}")
            print()
        print(block)
    else:
        print(f"SCORING-v1 overall: {ov:.2f}")
        for k in WEIGHTS:
            print(f"  {k:14s} {scores[k]:5.2f}  (weight {WEIGHTS[k]:.2f})")


if __name__ == "__main__":
    main()
