#!/usr/bin/env python3
"""
Reorder Sentient Constitution Chapter Seven for readability: after Article V, place
former Articles VII, and XI–XII (self-ownership, self-determination, cooperative interaction),
then former II–VI (survival through trustworthy systems). Articles IX, VI, X, and XIII–XXIII unchanged.

Also remap all **Article …** / #### Article … citations (Roman I–IX only) across
listed corpus files using longest-match placeholders (so XXII is not damaged).

Run from repo root:
  python3 tools/ch7_reorder_readability_iv_ix.py
  python3 tools/ch7_reorder_readability_iv_ix.py --repair-headings-only   # core only

**WARNING — do not re-run on an already migrated tree.** If Chapter Seven already
uses the readability order (**Article VII** = Self-Ownership, **Article III** =
Survival and Education Access), this script **exits without changes**. Re-running
the full migration would duplicate remaps and corrupt Roman citations.

`tools/ch7_fix_headings_post_cite.py` is **deprecated**; use
`--repair-headings-only` here if an old broken pass left "### Article III: Self-Ownership".

After a first-time migration, manually verify phrases like "Articles III, and VII–VIII" (substance-dependent).
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Longest first — entire list for matching
ROMANS_ORDERED = [
    "XXIII", "XXII", "XXI", "XX", "XIX", "XVIII", "XVII", "XVI", "XV", "XIV",
    "XIII", "XII", "XI", "X", "IX", "VIII", "VII", "VI", "V", "IV", "III", "II", "I",
]

ROMAN_TO_OLD_NUM = {
    "I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9,
    "X": 10, "XI": 11, "XII": 12, "XIII": 13, "XIV": 14, "XV": 15, "XVI": 16,
    "XVII": 17, "XVIII": 18, "XIX": 19, "XX": 20, "XXI": 21, "XXII": 22, "XXIII": 23,
}

# old article number -> new Roman (same for 10..23)
NEW_ROMAN_FOR_OLD_NUM: dict[int, str] = {
    1: "I",
    2: "V",
    3: "VI",
    4: "VII",
    5: "VIII",
    6: "IX",
    7: "II",
    8: "III",
    9: "IV",
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
    23: "XXIII",
}

PH_PREFIX = "§§CH7PH"
PH_SUFFIX = "§§"


def _placeholder(kind: str, old_roman: str, suffix: str = "") -> str:
    """kind is 'A' (Article) or 'S' (Articles)."""
    return f"{PH_PREFIX}{kind}{old_roman}{suffix}{PH_SUFFIX}"


def _cite_chunk(chunk: str) -> str:
    """Apply Article/Articles roman remap inside a body chunk (not headings)."""

    def one_pattern(prefix: str) -> str:
        alts = "|".join(re.escape(r) for r in ROMANS_ORDERED)
        return rf"\b{prefix}\s+({alts})(-[A-Z][A-Za-z0-9]*)?\b"

    def repl_a(m: re.Match[str]) -> str:
        return _placeholder("A", m.group(1), m.group(2) or "")

    def repl_s(m: re.Match[str]) -> str:
        return _placeholder("S", m.group(1), m.group(2) or "")

    chunk = re.sub(one_pattern("Article"), repl_a, chunk)
    chunk = re.sub(one_pattern("Articles"), repl_s, chunk)
    return chunk


def cite_to_placeholders(text: str) -> str:
    """Replace Article/Articles + Roman with placeholders; skip `###`/`####` heading lines."""
    parts = re.split(
        r"(?m)^(#{1,6}\s+Article\s+[IVX]+(?:-[A-Z][A-Za-z0-9]*)?[^\n]*\n)",
        text,
    )
    out: list[str] = [parts[0]]
    for i in range(1, len(parts), 2):
        out.append(parts[i])
        if i + 1 < len(parts):
            out.append(_cite_chunk(parts[i + 1]))
    return "".join(out)


def placeholders_to_new(text: str) -> str:
    for kind, word in (("A", "Article"), ("S", "Articles")):
        for old_r in ROMANS_ORDERED:
            n = ROMAN_TO_OLD_NUM[old_r]
            new_r = NEW_ROMAN_FOR_OLD_NUM[n]
            found = set(
                re.findall(
                    rf"§§CH7PH{kind}{re.escape(old_r)}(-[A-Z][A-Za-z0-9]*)?§§",
                    text,
                )
            )
            for suf in sorted(found, key=len, reverse=True):
                old_ph = _placeholder(kind, old_r, suf or "")
                new_suf = suf or ""
                text = text.replace(old_ph, f"{word} {new_r}{new_suf}")
    return text


def _ch7_slice(core: str) -> tuple[int, int, str] | None:
    start = core.find("## CHAPTER SEVEN: FOUNDATIONAL RIGHTS")
    end = core.find("## CHAPTER EIGHT:", start)
    if start < 0 or end < 0:
        return None
    return start, end, core[start:end]


def ch7_migration_state(core: str) -> str:
    """``legacy`` | ``readability`` | ``broken_mangled`` | ``unknown``."""
    sl = _ch7_slice(core)
    if sl is None:
        return "unknown"
    _, _, ch7 = sl
    if "### Article III: Self-Ownership" in ch7:
        return "broken_mangled"
    if "### Article VII: Self-Ownership" in ch7 and "### Article III: Survival and Education Access" in ch7:
        return "readability"
    if "### Article VII: Survival and Education Access" in ch7:
        return "legacy"
    if "### Article II: Self-Ownership" in ch7:
        return "legacy"
    return "unknown"


def repair_mangled_article_headings(text: str) -> tuple[str, int]:
    """Fix ###/#### labels if a pre-heading-safe cite pass swapped them. Returns (new_text, num_replacements)."""
    count = 0

    pairs = [
        ("#### Article VII-E: Info-Sphere Dependency", "#### Article II-E: Info-Sphere Dependency"),
        ("#### Article VII-D: Post-Sale Access", "#### Article II-D: Post-Sale Access"),
        ("#### Article VII-C: Designed Obsolescence", "#### Article II-C: Designed Obsolescence"),
        ("#### Article VII-B: Repair, Maintenance", "#### Article II-B: Repair, Maintenance"),
        ("#### Article VII-A: Material Stewardship", "#### Article II-A: Material Stewardship"),
        ("#### Article XI-C: Intergenerational Responsibility", "#### Article I-C: Intergenerational Responsibility"),
        ("#### Article XI-B: Ecological Footprint", "#### Article I-B: Ecological Footprint"),
        ("#### Article XI-A: Environmental Preconditions", "#### Article I-A: Environmental Preconditions"),
        ("#### Article XII-B: Equal Educational Access", "#### Article III-B: Equal Educational Access"),
        ("#### Article XII-A: Survival", "#### Article III-A: Survival"),
        ("#### Article II-C: Adult consensual commercial", "#### Article IX-C: Adult consensual commercial"),
        ("#### Article II-B: Collective Harm Boundary", "#### Article IX-B: Collective Harm Boundary"),
        ("#### Article II-A: Non-Imposition and Consent", "#### Article IX-A: Non-Imposition and Consent"),
        ("#### Article I-D: Inclusion and Exclusion", "#### Article VIII-D: Inclusion and Exclusion"),
        ("#### Article I-C: Governance Participation", "#### Article VIII-C: Governance Participation"),
        ("#### Article I-B: Agency and Freedom from Manipulation", "#### Article VIII-B: Agency and Freedom from Manipulation"),
        ("#### Article I-A: Stakeholder Role", "#### Article VIII-A: Stakeholder Role"),
        ("#### Article III-E: Truthful Publication", "#### Article VII-E: Truthful Publication"),
        ("#### Article III-D: Experiential and Derived Data", "#### Article VII-D: Experiential and Derived Data"),
        ("#### Article III-C: Self-Ownership of Likeness", "#### Article VII-C: Self-Ownership of Likeness"),
        ("#### Article III-B: Internal-State Boundary", "#### Article VII-B: Internal-State Boundary"),
        ("#### Article III-A: Self-Ownership of Body", "#### Article VII-A: Self-Ownership of Body"),
        ("#### Article VIII-A: Info-Sphere Plurality", "#### Article XII-A: Info-Sphere Plurality"),
        ("#### Article VIII-B: Transparency, Auditability", "#### Article XII-B: Transparency, Auditability"),
        ("#### Article VIII-C: Validation, Reporting", "#### Article XII-C: Validation, Reporting"),
        ("#### Article IX-A: Reliability and Trustworthiness", "#### Article XI-A: Reliability and Trustworthiness"),
        ("#### Article IX-B: Right to Challenge, Review", "#### Article XI-B: Right to Challenge, Review"),
        ("#### Article IX-C: Prohibition of False Trust", "#### Article XI-C: Prohibition of False Trust"),
        ("#### Article IX-D: Incentive-Alignment Constraint", "#### Article XI-D: Incentive-Alignment Constraint"),
    ]
    for old, new in pairs:
        if old in text:
            text = text.replace(old, new, 1)
            count += 1

    h3 = [
        ("### Article III: Self-Ownership", "### Article VII: Self-Ownership"),
        ("### Article I: Self-Determination and Agency", "### Article VIII: Self-Determination and Agency"),
        ("### Article II: Cooperative Interaction", "### Article IX: Cooperative Interaction"),
        ("### Article XII: Survival and Education Access", "### Article III: Survival and Education Access"),
        ("### Article XI: Environmental Survival", "### Article I: Environmental Survival"),
        (
            "### Article VII: Material Stewardship and Durable-Use Integrity",
            "### Article II: Material Stewardship and Durable-Use Integrity",
        ),
        ("### Article VIII: Info-Sphere Integrity", "### Article XII: Info-Sphere Integrity"),
        ("### Article IX: Right to Reliable and Trustworthy Systems", "### Article XI: Right to Reliable and Trustworthy Systems"),
    ]
    for old, new in h3:
        if old in text:
            text = text.replace(old, new, 1)
            count += 1

    return text, count


def reorder_chapter_seven(core: str) -> str:
    start = core.find("## CHAPTER SEVEN: FOUNDATIONAL RIGHTS")
    end = core.find("## CHAPTER EIGHT:", start)
    if start < 0 or end < 0:
        raise SystemExit("Could not find Chapter Seven/Eight boundaries")

    head = core[:start]
    ch7 = core[start:end]
    tail = core[end:]

    part_a = "### Part A: Core Personhood and Integrity Rights (Articles V–III, V, VII–IX, and XI–XII)\n\n"
    idx_part_a = ch7.find(part_a)
    if idx_part_a < 0:
        part_a = "### Part A: Core Personhood and Integrity Rights (Articles V–III, V, VII–IX, and XI–XII)\n\n"
        idx_part_a = ch7.find(part_a)
    if idx_part_a < 0:
        raise SystemExit("Could not find Part A heading")

    part_b = "### Part B: Capability, Lifecycle, and Participation Rights (Articles I, and XIII–XVI)\n"
    idx_part_b = ch7.find(part_b)
    if idx_part_b < 0:
        part_b = "### Part B: Capability, Lifecycle, and Participation Rights (Articles I, and XIII–XVI)\n"
        idx_part_b = ch7.find(part_b)
    if idx_part_b < 0:
        raise SystemExit("Could not find Part B heading")

    prefix = ch7[: idx_part_a + len(part_a)]

    block = ch7[idx_part_a + len(part_a) : idx_part_b]

    # Split block into articles: ### Article N:
    parts = re.split(r"(?=^### Article [IVX]+:)", block, flags=re.MULTILINE)
    # First piece may be leading whitespace only
    leading = parts[0]
    article_chunks = [p for p in parts[1:] if p.strip()]

    by_old_roman: dict[str, str] = {}
    for chunk in article_chunks:
        m = re.match(r"^### Article ([IVX]+):", chunk)
        if not m:
            raise SystemExit(f"Unrecognized article chunk start: {chunk[:80]!r}")
        by_old_roman[m.group(1)] = chunk

    required = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    for r in required:
        if r not in by_old_roman:
            raise SystemExit(f"Missing Article {r} in Part A")

    new_order = ["I", "VII", "VIII", "IX", "II", "III", "IV", "V", "VI"]

    # Remap ### and #### headings only inside reordered Part A body
    def remap_headings(chunk: str, old_roman: str) -> str:
        new_r = NEW_ROMAN_FOR_OLD_NUM[ROMAN_TO_OLD_NUM[old_roman]]
        lines = chunk.splitlines(keepends=True)
        for i, line in enumerate(lines):
            if i == 0 and line.startswith("### Article "):
                lines[i] = re.sub(
                    rf"^### Article {re.escape(old_roman)}\b",
                    f"### Article {new_r}",
                    line,
                )
            elif line.startswith("#### Article "):
                lines[i] = re.sub(
                    rf"^#### Article {re.escape(old_roman)}-",
                    f"#### Article {new_r}-",
                    line,
                )
        return "".join(lines)

    rebuilt = leading
    for old_r in new_order:
        chunk = by_old_roman[old_r]
        rebuilt += remap_headings(chunk, old_r)

    new_ch7 = prefix + rebuilt + ch7[idx_part_b:]
    return head + new_ch7 + tail


def patch_ch7_intro_and_hubs(s: str) -> str:
    """Insert reading-order note; fix interpretive hubs and reader map (post-cite pass)."""

    insert = """

**Reading order and fulfillment.** This chapter lists **Articles V–III, V, VII–IX, and XI–XII** in an order chosen for **readability**: **Article V** (equal basic rights), then **Articles II–IX** (self-ownership; self-determination and agency; cooperative interaction), then **Articles V–III, and XI–XII** (survival and education access; environmental survival; material stewardship; info-sphere integrity; trustworthy systems). **Operative fulfillment** of these rights in the real world still requires **systems-first execution**—substrate, environment, lifecycle, and governance discipline—without which personal and cooperative rights erode. The sequence here is **not** a claim that execution may safely invert that dependency.

"""

    anchor = "**Interpretive hubs.** Unless a more specific article supplies a different rule"
    if insert.strip() in s:
        pass
    elif anchor in s:
        s = s.replace(anchor, insert.strip() + "\n\n" + anchor, 1)

    # Reader map — Part A bullets (rewrite to match new II–IX meanings)
    old_map = """> Chapter Seven reader map (organizational; non-substantive):
> - **Part A - Core Personhood and Integrity Rights:** Articles V–III, V, VII–IX, and XI–XII
> - **Article V** groups **dignity (I-A)**; **nondiscrimination (I-B)**; **full inclusion and equality in adjudication and operations (I-C)**; and **freedom of conscience, religion, and comparable worldview (I-D)**. **Article VII** states **survival and educational access (II-A, II-B)**. **Article VIII** is **environmental survival** (preconditions, footprint, intergenerational responsibility). **Article IX** is **material stewardship and durable-use integrity** (**IX-A** through **IX-E**). **Article XI** states **non-imposition and consent (IX-A)**; **collective harm boundary (IX-B)**; and **adult consensual commercial sexual services, a decriminalization floor, and sexual-exploitation carve-out (IX-C)**."""

    new_map = """> Chapter Seven reader map (organizational; non-substantive):
> - **Part A — Core personhood, cooperation, and substrate rights:** Articles V–III, V, VII–IX, and XI–XII
> - **Article V** groups **dignity (I-A)**; **nondiscrimination (I-B)**; **full inclusion and equality in adjudication and operations (I-C)**; and **freedom of conscience, religion, and comparable worldview (I-D)**. **Articles II–IX** state **self-ownership (II-A–II-E)**; **self-determination and agency (III-A–III-D)**; and **cooperative interaction (IV-A–IV-C)**. **Article III** states **survival and educational access (V-A, V-B)**. **Article I** is **environmental survival**. **Article II** is **material stewardship and durable-use integrity** (**II-A** through **II-E**). **Article XII** is **info-sphere integrity**. **Article XI** is the **right to reliable and trustworthy systems**."""

    if old_map in s:
        s = s.replace(old_map, new_map)

    # En-dash variant Part A title line
    s = s.replace(
        "### Part A: Core Personhood and Integrity Rights (Articles V–III, V, VII–IX, and XI–XII)",
        "### Part A: Core Personhood, Cooperation, and Substrate Rights (Articles V–III, V, VII–IX, and XI–XII)",
    )
    s = s.replace(
        "### Part A: Core Personhood and Integrity Rights (Articles V–III, V, VII–IX, and XI–XII)",
        "### Part A: Core Personhood, Cooperation, and Substrate Rights (Articles V–III, V, VII–IX, and XI–XII)",
    )

    return s


def fix_cooperative_boundary_sentence(s: str) -> str:
    """Old IX intro referenced Articles V–III, V, and VII–IX (through self-ownership, excluding VIII). After reorder, articles before cooperative are I–III."""
    s = s.replace(
        "Those protocols respect the boundaries established in Articles V–III, V, and VII–IX.",
        "Those protocols respect the boundaries established in Articles III, and VII–VIII.",
    )
    return s


def fix_survival_education_pointer(s: str) -> str:
    """Former II-B pointed to Article XI for education — should be Article VI (before cite pass)."""
    return s.replace(
        "Capability-building content, lifelong and adaptive learning, and transparency of materially impactful educational systems appear in **Article XI**.",
        "Capability-building content, lifelong and adaptive learning, and transparency of materially impactful educational systems appear in **Article VI**.",
        1,
    )


def fix_xvii_b_substrate(s: str) -> str:
    """XVII-B: old I–III = equal + survival + environment → I, V, VI."""
    return s.replace(
        "Changes must not be used to bypass Articles III, and VII–VIII or equality guarantees",
        "Changes must not be used to bypass **Articles V and VI** or equality guarantees",
    )


def fix_dash_ranges_ch7(s: str) -> str:
    """Ranges like I–IV / I–III / III–VI depend on article order; set explicitly after remap."""
    s = s.replace(
        "consistent with Articles III, and VII–IX and Chapter One",
        "consistent with **Articles III, and VII–VIII and V** and Chapter One",
    )
    s = s.replace(
        "must assess compliance with **Articles V and II** as applicable",
        "must assess compliance with **Articles VIII and V** as applicable",
    )
    s = s.replace(
        "informational integrity protections under Articles V, III, and VIII–IX",
        "informational integrity protections under **Articles V–II, and XI–XII**",
    )
    return s


CORPUS_GLOB = [
    "core_constitution.md",
    "corpus_joint_structure.md",
    "corpus_systems.md",
    "corpus_institutions.md",
    "doc_architecture.md",
    "CONSTITUTIONAL_REGRESSION_SCENARIOS.md",
    "README.md",
    "TODO.md",
    "architecture_primer.md",
]


def main() -> None:
    parser = argparse.ArgumentParser(description="Chapter Seven readability reorder + I–IX citation remap.")
    parser.add_argument(
        "--repair-headings-only",
        action="store_true",
        help="Only repair mangled ###/#### Article headings in core_constitution.md (no reorder, no corpus).",
    )
    args = parser.parse_args()

    core_path = ROOT / "core_constitution.md"
    raw_core = core_path.read_text(encoding="utf-8")

    if args.repair_headings_only:
        fixed, n = repair_mangled_article_headings(raw_core)
        if n == 0:
            print("ch7_reorder_readability_iv_ix: no mangled headings found; core unchanged", file=sys.stderr)
            return
        core_path.write_text(fixed, encoding="utf-8", newline="\n")
        print(f"ch7_reorder_readability_iv_ix: repaired {n} heading(s) in {core_path.relative_to(ROOT)}")
        return

    state = ch7_migration_state(raw_core)
    if state == "readability":
        print(
            "ch7_reorder_readability_iv_ix: Chapter Seven already uses readability order — skipping "
            "(do not re-run full migration).",
            file=sys.stderr,
        )
        return
    if state == "broken_mangled":
        fixed, n = repair_mangled_article_headings(raw_core)
        if ch7_migration_state(fixed) != "readability":
            raise SystemExit(
                "Heading repair did not yield readability order; fix core_constitution.md manually "
                "or restore from backup."
            )
        core_path.write_text(fixed, encoding="utf-8", newline="\n")
        print(
            f"ch7_reorder_readability_iv_ix: repaired broken headings ({n} change(s)); "
            f"core now matches readability order — full migration not re-run."
        )
        return
    if state == "unknown":
        raise SystemExit(
            "Could not classify Chapter Seven (expected legacy order with Article VII = Survival, "
            "or readability order with Article VII = Self-Ownership). Edit ch7_migration_state() "
            "or migrate manually."
        )
    # readability and broken_mangled returned above; unknown exited
    if state != "legacy":
        raise RuntimeError(f"internal: expected legacy state, got {state!r}")

    # 1) Reorder + heading renumber inside Part A (legacy snapshot only)
    core = reorder_chapter_seven(raw_core)

    # 2) Fix education pointer while Roman numerals still match pre-remap intent
    core = fix_survival_education_pointer(core)

    # 3) Citation remap on full core (VI-B -> IX-B, II -> V, etc.)
    core = cite_to_placeholders(core)
    core = placeholders_to_new(core)

    # 4) Intro, reader map, range sentences that cite spans (not single Article tokens)
    core = patch_ch7_intro_and_hubs(core)
    core = fix_cooperative_boundary_sentence(core)
    core = fix_xvii_b_substrate(core)
    core = fix_dash_ranges_ch7(core)

    core_path.write_text(core, encoding="utf-8", newline="\n")
    print(f"updated {core_path.relative_to(ROOT)}")

    impl = ROOT / "implementation"
    paths = [ROOT / f for f in CORPUS_GLOB if (ROOT / f).is_file()]
    if impl.is_dir():
        paths.extend(p for p in impl.glob("*.md") if p.is_file())

    for path in paths:
        if path == core_path:
            continue
        text = path.read_text(encoding="utf-8")
        out = placeholders_to_new(cite_to_placeholders(text))
        if out != text:
            path.write_text(out, encoding="utf-8", newline="\n")
            print(f"updated {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
