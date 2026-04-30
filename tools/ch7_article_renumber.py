#!/usr/bin/env python3
"""
Legacy one-off: increment Chapter Seven article labels **III..XXI → IV..XXII**
(subsection hyphen forms only: ``Article N-``).

**Do not run on the current corpus** unless you are replaying that older migration
from a known-good snapshot. The 2026-04-10 structure inserts a new **Article IX**
(material stewardship) and bumps former **IV..XXII → V..XXIII**; that workflow uses
``ch7_bump_articles_iv_to_xxii.py`` (IV–XXII → V–XXIII with placeholders), manual
insert/split of material articles in ``core_constitution.md``, then
``ch7_map_iii_material_to_iv.py`` for **III-D…H → IV-A…E** remnants, then
contextual fixes (audit = **Article XIII** / **XIII-A**, lifecycle environments =
**XIV-A**, reversibility = **XIV-B**, etc.).

Does not change Article V or Article VII (including II-* subsections).
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ROMANS = {
    3: "III",
    4: "IV",
    5: "V",
    6: "VI",
    7: "VII",
    8: "VIII",
    9: "IX",
    10: "X",
    11: "XI",
    12: "XII",
    13: "XIII",
    14: "XIV",
    15: "XV",
    16: "XVI",
    17: "XVII",
    18: "XVIII",
    19: "XIX",
    20: "XX",
    21: "XXI",
    22: "XXII",
}

FILES = [
    "core_constitution.md",
    "corpus_joint_structure.md",
    "corpus_systems.md",
    "corpus_institutions.md",
    "doc_architecture.md",
    "CONSTITUTIONAL_REGRESSION_SCENARIOS.md",
    "README.md",
    "TODO.md",
]


def collect_paths() -> list[Path]:
    paths = [ROOT / f for f in FILES]
    impl = ROOT / "implementation"
    if impl.is_dir():
        paths.extend(p for p in impl.glob("*.md") if p.is_file())
    return paths


def renumber_text(text: str) -> str:
    for n in range(21, 2, -1):
        old = ROMANS[n]
        new = ROMANS[n + 1]
        text = text.replace(f"Article {old}-", f"Article {new}-")
        text = text.replace(f"article {old}-", f"article {new}-")
    return text


def main() -> None:
    for path in collect_paths():
        raw = path.read_text(encoding="utf-8")
        out = renumber_text(raw)
        if out != raw:
            path.write_text(out, encoding="utf-8", newline="\n")
            print(f"updated {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
