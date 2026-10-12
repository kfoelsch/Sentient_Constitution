# Project files

Working files for the people who maintain the Sentient Constitution. Readers do not need anything here; start at the [main README](../README.md).

| File | What it is for |
|---|---|
| [VISION.md](VISION.md) | Where the corpus stands and the path to maturity |
| [TODO.md](TODO.md) | Open task list |
| [MEMLOG.md](MEMLOG.md) | Session log of recent decisions and changes |
| [CONSTITUTIONAL_REGRESSION_SCENARIOS.md](CONSTITUTIONAL_REGRESSION_SCENARIOS.md) | Regression scenario catalog checked by `make scenario-audit` |
| [plans/](plans/) | Working plans for larger changes |
| [plain_language/](plain_language/) | Plain-language companion for each Article (`Article_<numeral>_plain_language.md`). Not binding; the `core_*` files are |

How to contribute: [CONTRIBUTING.md](../CONTRIBUTING.md).

Keep the repository root for the public door and the numbered corpus. Plain-language companions, drafts, and WIP files go here, not in the root. Git bundles (`*.bundle`) never belong in the repository, and no file may exceed 1 MB (`make file-size-audit`). `make root-layout-audit` (part of `make regression`) fails on strays; `python3 tools/root_layout_audit.py --fix` moves plain-language files and repairs their links.
