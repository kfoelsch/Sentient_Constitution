#!/usr/bin/env python3
"""A/B the Chapter Seven default constraint stack: run `make regression` per variant.

Swaps only the **Default constraint stack.** paragraph in core_constitution.md, runs
`make regression`, restores the file. Writes logs under evidence/<date>/ch7_stack_ab/.

Note: Mechanical audits usually tie on a small wording change; interpretive tradeoffs
need tabletop review (see implementation/CH7_CONSTRAINT_STACK_AB_REGRESSION.md).
"""

from __future__ import annotations

import argparse
import datetime as dt
import pathlib
import re
import shutil
import subprocess
import sys


STACK_BLOCK_RE = re.compile(
    r"(^\*\*Default constraint stack\.\*\*.*?)(?=^\*\*Interpretive hubs\.\*\*)",
    re.MULTILINE | re.DOTALL,
)

EVAL_BLOCK_START = re.compile(r"^- Evaluation \(SCORING-v1 snapshot, section 10\.5\):")

# Canonical **Default constraint stack.** paragraph (qualified Ch 1 §7.2). Keep in sync with
# `core_constitution.md` (Chapter Seven); the harness runs regression with disk text vs this
# constant to detect drift.
OPTION_B_STACK = (
    "**Default constraint stack.** Unless a provision in this chapter expressly states otherwise, "
    "rights in this chapter are subject to: **Chapter One** (Safety, Truth, Necessity, Proportionality, "
    "systemic evaluation including local, aggregate, delayed, and cross-system effects, and section 6 "
    "interaction rules); **Chapter One**, section **7.2** (*Incentive Alignment and System Capture* and "
    "related subsections), **only where materially relevant** to the right at issue, the conduct or "
    "practice being evaluated, or the limitation being defended (including incentive-sensitive trust, "
    "fidelity, and market-structure contexts addressed there); **Chapters Two through Four** "
    "(definition integrity, burden and traceability, observability, and verification accessibility, "
    "including security-constrained observability where applicable); **Chapter Five** definitions "
    "materially relevant to the right; and scaling with **Materiality**, **Dependency**, and incorporated "
    "classification or tier rules where adopting instruments supply them. Articles need not repeat this "
    "stack where it applies generically.\n"
)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", default=".", help="Repository root (contains Makefile, core_constitution.md).")
    p.add_argument(
        "--date",
        default=dt.date.today().isoformat(),
        help="Evidence subdirectory date YYYY-MM-DD.",
    )
    p.add_argument(
        "--skip-make",
        action="store_true",
        help="Only print metrics and write variants; do not run make or mutate core file.",
    )
    return p.parse_args()


def paragraph_metrics(label: str, text: str) -> None:
    words = len(re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", text))
    sents = max(1, len(re.split(r"(?<=[.!?])\s+", text.strip())))
    print(f"{label}: ~{words} words, ~{sents} sentence(s), {len(text)} chars")


def extract_evaluation_block(make_stdout: str) -> str:
    """Pull scenario_audit evaluation echo from full `make regression` stdout."""
    lines = make_stdout.splitlines()
    for i, line in enumerate(lines):
        if EVAL_BLOCK_START.match(line):
            chunk = [line]
            for j in range(i + 1, len(lines)):
                nxt = lines[j]
                if nxt.startswith("  - "):
                    chunk.append(nxt)
                else:
                    break
            return "\n".join(chunk)
    return ""


def main() -> int:
    args = parse_args()
    root = pathlib.Path(args.root).resolve()
    core_path = root / "core_constitution.md"
    if not core_path.is_file():
        print(f"Missing {core_path}", file=sys.stderr)
        return 1

    original = core_path.read_text(encoding="utf-8")
    m = STACK_BLOCK_RE.search(original)
    if not m:
        print("Could not locate Default constraint stack block before Interpretive hubs.", file=sys.stderr)
        return 1

    option_a = m.group(1)
    if not option_a.strip().startswith("**Default constraint stack.**"):
        print("Unexpected stack block shape.", file=sys.stderr)
        return 1

    out_dir = root / "evidence" / args.date / "ch7_stack_ab"
    out_dir.mkdir(parents=True, exist_ok=True)

    (out_dir / "option_a_stack.txt").write_text(option_a, encoding="utf-8")
    (out_dir / "option_b_stack.txt").write_text(OPTION_B_STACK, encoding="utf-8")

    print("--- Paragraph metrics (operative stack only) ---")
    paragraph_metrics("From core_constitution.md (disk)", option_a)
    paragraph_metrics("Canonical OPTION_B_STACK (tool)", OPTION_B_STACK.rstrip("\n"))
    if option_a.strip() != OPTION_B_STACK.strip():
        print(
            "Note: disk stack text differs from OPTION_B_STACK in this script — update one to match.",
            file=sys.stderr,
        )

    if args.skip_make:
        print("--skip-make: not running regression or editing core_constitution.md")
        return 0

    make_bin = shutil.which("make")
    if not make_bin:
        print("make not found on PATH; cannot run regression.", file=sys.stderr)
        return 1

    def run_variant(name: str, stack_para: str) -> tuple[int, str]:
        replaced, n_subs = STACK_BLOCK_RE.subn(stack_para, original, count=1)
        if n_subs != 1:
            print(f"Expected one stack substitution for {name}, got {n_subs}", file=sys.stderr)
            return 1, ""
        core_path.write_text(replaced, encoding="utf-8")
        log_path = out_dir / f"make_regression_option_{name.lower()}.log"
        proc = subprocess.run(
            [make_bin, "regression"],
            cwd=str(root),
            capture_output=True,
            text=True,
        )
        log_path.write_text(
            f"exit_code={proc.returncode}\n\n--- stdout ---\n{proc.stdout}\n--- stderr ---\n{proc.stderr}",
            encoding="utf-8",
        )
        print(f"Variant {name}: make regression exit {proc.returncode} (log {log_path})")
        return proc.returncode, proc.stdout

    exit_a = exit_b = 0
    out_a = out_b = ""
    try:
        exit_a, out_a = run_variant("A", option_a)
        exit_b, out_b = run_variant("B", OPTION_B_STACK)
    finally:
        core_path.write_text(original, encoding="utf-8")
        print("Restored core_constitution.md from backup.")

    eval_a = extract_evaluation_block(out_a)
    eval_b = extract_evaluation_block(out_b)
    (out_dir / "evaluation_option_a.txt").write_text(
        (eval_a or "(evaluation block not found in make stdout)\n") + "\n", encoding="utf-8"
    )
    (out_dir / "evaluation_option_b.txt").write_text(
        (eval_b or "(evaluation block not found in make stdout)\n") + "\n", encoding="utf-8"
    )

    print()
    print("--- Evaluation scores (SCORING-v1 snapshot, echoed by scenario_audit) ---")
    print("Disk (variant A):")
    print(eval_a or "(not found)")
    print("OPTION_B_STACK (variant B):")
    print(eval_b or "(not found)")
    if eval_a and eval_b:
        if eval_a == eval_b:
            print()
            print(
                "Comparison: identical. §10.5 in CONSTITUTIONAL_REGRESSION_SCENARIOS.md is unchanged by "
                "this paragraph swap, so both mechanical regressions read the same authored snapshot. "
                "To compare different numeric scores across variants, update §10.5 after tabletop scoring "
                "for each variant (or maintain separate snapshot files and point audits at them—out of "
                "scope for this harness)."
            )
        else:
            print()
            print("Comparison: evaluation text differs between runs (diff evaluation_option_a.txt evaluation_option_b.txt).")

    summary = (
        f"Chapter Seven default stack A/B regression ({args.date})\n"
        f"- Variant A (from core_constitution.md): make regression exit {exit_a}\n"
        f"- Variant B (OPTION_B_STACK in tool): make regression exit {exit_b}\n"
        f"- Logs: {out_dir}/make_regression_option_a.log , make_regression_option_b.log\n"
        f"- Evaluation extracts: {out_dir}/evaluation_option_a.txt , evaluation_option_b.txt\n"
    )
    (out_dir / "SUMMARY.txt").write_text(summary, encoding="utf-8")
    print(summary)
    return 0 if exit_a == 0 and exit_b == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
