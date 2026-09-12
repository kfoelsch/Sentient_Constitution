#!/usr/bin/env python3
"""Historical helper: rewrote **constitutional** phrasing to **charter** in companion files.

**Do not run on the current corpus.** `make regression` now enforces `corpus-no-bare-charter`
(the opposite vocabulary). To mechanically undo this script’s phrase map after a mistaken run,
use `corpus_charter_vocab_revert.py`.

Preserves: Constitutional Systems; *Name (Constitutional)* / (Constitutional) labels;
unconstitutional; non-constitutional; constitutional sense; constitutional hook.
"""

from __future__ import annotations

import pathlib
import re
import sys

# Longest-first phrase replacements (substring safety).
# Run before bare ``constitutional`` → ``charter`` to avoid grammar glitches
# (e.g. "constraints are constitutional" → "constraints are charter").
PHRASES: list[tuple[str, str]] = sorted(
    [
        ("aggravated-constitutional-crime", "aggravated-charter-crime"),
        ("constitutional amendment requirements", "charter amendment requirements"),
        ("constitutional review/accountability", "charter review/accountability"),
        ("constitutional forums", "charter forums"),
        ("constitutional rights-floor", "charter rights-floor"),
        ("constitutional review body", "charter forums"),
        ("constitutional review channels", "charter review channels"),
        ("constitutional authority assertions", "charter authority assertions"),
        ("constitutional term layer", "charter term layer"),
        ("constitutional parameter change", "charter parameter change"),
        ("constitutional conformance pass", "charter conformance pass"),
        ("constitutional regression scenarios", "charter regression scenarios"),
        ("constitutional rights-floor verification", "charter rights-floor verification"),
        ("second constitutional source", "second charter source"),
        ("presumption of constitutional crime", "presumption of charter crime"),
        ("is aggravated constitutional crime", "is aggravated charter crime"),
        ("equivalent constitutional criminal process protections", "equivalent charter criminal process protections"),
        ("constitutional interpretation and review safeguards", "charter interpretation and review safeguards"),
        ("constitutional challenge rights", "charter challenge rights"),
        ("constitutional classifications", "charter classifications"),
        ("constitutional requirements", "charter requirements"),
        ("constitutional protections", "charter protections"),
        ("constitutional constraints", "charter constraints"),
        ("constitutional obligations", "charter obligations"),
        ("constitutional accountability", "charter accountability"),
        ("constitutional compliance", "charter compliance"),
        ("constitutional violation", "charter violation"),
        ("constitutional objectives", "charter goals"),
        ("constitutional outcomes", "charter outcomes"),
        ("constitutional alignment", "charter alignment"),
        ("constitutional interpretation", "charter interpretation"),
        ("constitutional legitimacy", "charter legitimacy"),
        ("constitutional safeguards", "charter safeguards"),
        ("constitutional enforcement", "charter enforcement"),
        ("constitutional continuity", "charter continuity"),
        ("constitutional performance", "charter performance"),
        ("constitutional operations", "charter operations"),
        ("constitutional challenges", "charter challenges"),
        ("constitutional harms", "charter harms"),
        ("constitutional claims", "charter claims"),
        ("constitutional remedies", "charter remedies"),
        ("constitutional authority", "charter authority"),
        ("constitutional invariants", "charter invariants"),
        ("constitutional decision", "charter decision"),
        ("constitutional controls", "charter controls"),
        ("constitutional control coverage", "charter control coverage"),
        ("constitutional control", "charter control"),
        ("constitutional redesign", "charter redesign"),
        ("constitutional revision", "charter revision"),
        ("constitutional guarantee", "charter guarantee"),
        ("constitutional guarantees", "charter guarantees"),
        ("constitutional behavior", "charter behavior"),
        ("constitutional language", "charter language"),
        ("constitutional regression", "charter regression"),
        ("constitutional change", "charter change"),
        ("constitutional amendment", "charter amendment"),
        ("constitutional effect", "charter effect"),
        ("constitutional hierarchy", "charter hierarchy"),
        ("constitutional status", "charter status"),
        ("constitutional shield", "charter shield"),
        ("constitutional review", "charter review"),
        ("constitutional floors", "charter floors"),
        ("constitutional floor", "charter floor"),
        ("constitutional care", "charter-aligned conduct"),
        ("constitutional criteria", "charter criteria"),
        ("constitutional parameter", "charter parameter"),
        ("constitutional harms", "charter harms"),
        ("constitutional challenges", "charter challenges"),
        ("constitutional legitimacy checks", "charter legitimacy checks"),
        ("constitutional challenges", "charter challenges"),
        ("constitutional rights", "charter rights"),
        ("constitutional validity", "charter validity"),
        ("constitutional supremacy", "charter supremacy"),
        ("constitutional adoption", "charter adoption"),
        ("constitutional minimums", "charter minimums"),
        ("constitutional requirements", "charter requirements"),
        ("constitutional findings", "charter findings"),
        ("constitutional ecosystem", "charter ecosystem"),
        ("constitutional systems", "charter systems"),
        ("constitutional constraints", "charter constraints"),
        ("constitutional constraint", "charter constraint"),
        ("constitutional terms", "charter terms"),
        ("constitutional term", "charter term"),
        ("constitutional layer", "charter layer"),
        ("constitutional text", "charter text"),
        ("constitutional hook", "§§HOOK§§"),  # restore later
        ("constitutional sense", "§§SENSE§§"),
        ("non-constitutional", "§§NONC§§"),
        ("unconstitutional", "§§UNCON§§"),
        ("constitutionally required", "charter-required"),
        ("constitutionally aligned", "charter-aligned"),
        ("constitutionally compliant", "charter-compliant"),
        ("constitutional-crime", "charter-crime"),
        # Phrase-level fixes before bare-word swap:
        ("constraints are constitutional", "constraints are charter-compliant"),
        ("on the system when constitutional", "on the system when charter-valid"),
        ("at the constitutional provisions layer", "at the provisions layer of this charter"),
        ("constitutional", "charter"),
    ],
    key=lambda x: len(x[0]),
    reverse=True,
)


def protect_paren_constitutional(text: str) -> tuple[str, list[str]]:
    """Replace (*... (Constitutional) ...) with placeholders."""
    stored: list[str] = []

    def _sub(m: re.Match[str]) -> str:
        stored.append(m.group(0))
        return f"§§PAREN{len(stored)-1}§§"

    # *Title (Constitutional)* or (Something (Constitutional))
    pattern = re.compile(r"\([^)]*\(Constitutional\)[^)]*\)")
    text = pattern.sub(_sub, text)
    return text, stored


def restore_paren(text: str, stored: list[str]) -> str:
    for i, s in enumerate(stored):
        text = text.replace(f"§§PAREN{i}§§", s)
    return text


def transform(text: str) -> str:
    text = text.replace("Constitutional Systems", "§§CSYS§§")
    text, paren_store = protect_paren_constitutional(text)
    for old, new in PHRASES:
        text = text.replace(old, new)
    text = text.replace("§§CSYS§§", "Constitutional Systems")
    text = restore_paren(text, paren_store)
    text = text.replace("§§HOOK§§", "constitutional hook")
    text = text.replace("§§SENSE§§", "constitutional sense")
    text = text.replace("§§NONC§§", "non-constitutional")
    text = text.replace("§§UNCON§§", "unconstitutional")
    return text


def main() -> int:
    root = pathlib.Path(__file__).resolve().parents[1]
    paths = [
        root / "corpus_joint_structure.md",
        root / "corpus_systems.md",
        root / "CONSTITUTIONAL_REGRESSION_SCENARIOS.md",
    ]
    for p in paths:
        if not p.is_file():
            print(f"skip missing: {p}", file=sys.stderr)
            continue
        raw = p.read_text(encoding="utf-8")
        out = transform(raw)
        p.write_text(out, encoding="utf-8")
        print(f"updated {p.relative_to(root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
