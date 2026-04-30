# Chapter Nine default constraint stack — A/B regression harness

## Purpose

**Operative text:** `core_constitution.md` (Chapter Nine) now uses the **qualified section 7.2** formulation: **Chapter One** (Safety, Truth, Necessity, Proportionality, systemic effects, section 6) applies generally; **Chapter One**, section **7.2** (*Incentive Alignment and System Capture* and related subsections) applies **only where materially relevant** to the right, conduct or practice, or limitation (including incentive-sensitive trust, fidelity, and market-structure contexts there).

This harness still runs **`make regression` twice**: once with the stack paragraph taken from **`core_constitution.md` (variant A)** and once with the canonical string **`OPTION_B_STACK`** in `tools/ch7_constraint_stack_ab_regression.py` (variant B). When the repo is consistent, both variants are the **same wording**; the run is a **drift check** (disk vs tool constant) and preserves logs for future candidates if you change `OPTION_B_STACK` to a new proposal. Readability remains available separately through **`make regression-full`** when you want an editorial pass in addition to the blocking mechanical checks.

## How to run

From the repository root:

```bash
python3 tools/ch7_constraint_stack_ab_regression.py --root .
```

Optional: `--skip-make` prints paragraph metrics and writes frozen stack texts to `evidence/<date>/ch7_stack_ab/` without editing `core_constitution.md` or running Make.

Makefile shortcut:

```bash
make regression-ch7-stack-ab
```

## What “better” means here

1. **Mechanical regression (`make regression`)**  
   Both variants should **pass the same checks** when wording matches. If you introduce a **new** candidate in `OPTION_B_STACK` only, variant B exercises it without committing to `core_constitution.md`.

2. **Optional editorial regression (`make regression-full`)**  
   Adds the readability gate when you want prose-density failures to block the run as well.

3. **Paragraph metrics (printed by the tool)**  
   The qualified **7.2** formulation is longer than the old unconditional parenthetical; that is a **complexity vs. precision** tradeoff, not a pass/fail.

4. **Substantive “better” (rights vs. governance creep)**  
   Still use **tabletop scenarios** (e.g. simple privacy/disclosure vs. trust/markets/capture patterns) to validate that **7.2** is not over- or under-applied at the rights layer.

## Artifacts

After a full run, see `evidence/<date>/ch7_stack_ab/`:

- `option_a_stack.txt` / `option_b_stack.txt` — exact stack paragraphs tested  
- `make_regression_option_a.log` / `make_regression_option_b.log` — full `make regression` output  
- `evaluation_option_a.txt` / `evaluation_option_b.txt` — the **SCORING-v1** block echoed by `tools/scenario_audit.py` from each run (for side-by-side comparison)  
- `SUMMARY.txt` — exit codes and paths  

**Evaluation scores:** The harness prints both blocks after the runs. They will **match** unless you change `CONSTITUTIONAL_REGRESSION_SCENARIOS.md` section **10.5** between variants—mechanical regression does not re-score the constitution; it validates the **same** authored snapshot each time.

## Keeping disk and tool in sync

After editing the **Default constraint stack** paragraph in `core_constitution.md`, update the **`OPTION_B_STACK`** constant in `tools/ch7_constraint_stack_ab_regression.py` to the same text (or vice versa). If they diverge, the harness prints a **stderr note** and variant A vs B may exercise different wording.
