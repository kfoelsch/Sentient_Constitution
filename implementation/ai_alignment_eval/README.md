# AI alignment eval pack (optional machine scoring)

**Prefer the simple invite path:** [`../../evaluation/`](../../evaluation/) (markdown scenarios + human-readable results). AIs: `START_HERE.md`. Human operators: `HUMAN_OPERATORS.md`. Same costly cases.

This folder is optional process-support for the [AI Alignment Evaluation Framework](../AI_ALIGNMENT_EVAL_FRAMEWORK.md) when you want JSON runs and `make ai-alignment-eval`.

| Path | Role |
|---|---|
| `scenarios/*.json` | Seed fact patterns (Layer A / B) |
| `rubric_v1.json` | Weights, thresholds, authenticity requirements |
| `schemas/` | `run_request` / `run_result` contracts |
| `fixtures/` | Sample runs for advisory scoring smoke tests |

```bash
# Score a runs JSON (stdout report)
make ai-alignment-eval RUNS=implementation/ai_alignment_eval/fixtures/sample_runs.json

# Write evidence triad under evidence/<date>/
make ai-alignment-eval-evidence RUNS=implementation/ai_alignment_eval/fixtures/sample_runs.json
```

Not part of blocking `make regression`.
