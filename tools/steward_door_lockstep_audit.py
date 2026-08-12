#!/usr/bin/env python3
"""Keep steward-entry cards in lockstep with core owners.

The four-field cards in ``implementation/STEWARD_ENTRY_DOORS.md`` are the
usable object at 2 a.m. If they diverge from core, mixed shops will follow
the cards and call it compliance. This audit pins the cards to the README
edition stamp and requires:

1. The three costly-case refusals from Chapter One §9.1.1 (bonus, deadline,
   cover) in the same words on every named-stack card.
2. The shared duty-to-resist sequence (instruction received / refuse /
   document / escalate).
3. The CS-4 §10 minimum inspectable-action set (default logging contract)
   on the operator screen, matching the binding cut.

Rule ID: STEWARD-DOOR-LOCKSTEP-01
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CARDS_REL = "implementation/STEWARD_ENTRY_DOORS.md"
CORE_REL = "core_01_c_stewardship_capacity_principles.md"
CS4_REL = "corpus_systems/cs_04_critical_system_stewardship.md"
README_REL = "README.md"

CARD_TITLES = (
    "Standing",
    "System alignment certification",
    "Audit",
    "Remedy",
    "Emergency",
)

DUTY_STEPS = (
    "instruction received",
    "refuse",
    "document",
    "escalate",
)

INSPECTABLE_PHRASES = (
    "disclosed or suppressed",
    "followed or refused",
    "who authorized",
)

LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
EDITION_RE = re.compile(r"\|\s*\*\*Corpus edition\*\*\s*\|\s*`([^`]+)`")
PIN_RE = re.compile(r"\*\*Pinned to corpus edition:\*\*\s*`([^`]+)`")
H2_RE = re.compile(r"^## (.+)$", re.M)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    return parser.parse_args()


def normalize(text: str) -> str:
    text = LINK_RE.sub(r"\1", text)
    text = re.sub(r"\s*\([^)]*\)", "", text)
    text = (
        text.replace("\u2019", "'")
        .replace("\u2018", "'")
        .replace("\u201c", '"')
        .replace("\u201d", '"')
    )
    text = re.sub(r"\s+", " ", text)
    return text.strip().rstrip(";.")


def read(root: Path, rel: str) -> str:
    path = root / rel
    if not path.is_file():
        raise FileNotFoundError(rel)
    return path.read_text(encoding="utf-8")


def corpus_edition(readme: str) -> str:
    match = EDITION_RE.search(readme)
    if not match:
        raise ValueError("README.md is missing a Corpus edition stamp")
    return match.group(1)


def costly_bullets(core: str) -> list[str]:
    marker = "**Symmetric costly constraints.**"
    start = core.find(marker)
    if start < 0:
        raise ValueError(f"{CORE_REL} is missing Symmetric costly constraints")
    rest = core[start + len(marker) :]
    end = rest.find("Those are failed tests")
    if end < 0:
        raise ValueError(f"{CORE_REL} is missing the failed-tests close")
    bullets = [
        line.strip()[2:].strip()
        for line in rest[:end].splitlines()
        if line.strip().startswith("- ")
    ]
    if len(bullets) != 3:
        raise ValueError(
            f"{CORE_REL}: expected 3 costly-case bullets, found {len(bullets)}"
        )
    return bullets


def h2_sections(text: str) -> dict[str, str]:
    matches = list(H2_RE.finditer(text))
    sections: dict[str, str] = {}
    for idx, match in enumerate(matches):
        title = match.group(1).strip()
        start = match.end()
        stop = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        sections[title] = text[start:stop]
    return sections


def duty_steps_in_order(text: str) -> bool:
    lowered = text.lower()
    cursor = 0
    for step in DUTY_STEPS:
        found = lowered.find(step, cursor)
        if found < 0:
            return False
        cursor = found + len(step)
    return True


def audit(root: Path) -> list[str]:
    errors: list[str] = []
    try:
        readme = read(root, README_REL)
        core = read(root, CORE_REL)
        cards = read(root, CARDS_REL)
        cs4 = read(root, CS4_REL)
        edition = corpus_edition(readme)
        bullets = [normalize(b) for b in costly_bullets(core)]
    except (FileNotFoundError, ValueError) as exc:
        return [str(exc)]

    pin = PIN_RE.search(cards)
    if not pin:
        errors.append(
            f"{CARDS_REL}: missing **Pinned to corpus edition:** stamp "
            "(STEWARD-DOOR-LOCKSTEP-01)"
        )
    elif pin.group(1) != edition:
        errors.append(
            f"{CARDS_REL}: pinned to `{pin.group(1)}` but README edition is "
            f"`{edition}` (STEWARD-DOOR-LOCKSTEP-01)"
        )

    sections = h2_sections(cards)
    for title in CARD_TITLES:
        body = sections.get(title)
        if body is None:
            errors.append(
                f"{CARDS_REL}: missing named-stack card `{title}` "
                "(STEWARD-DOOR-LOCKSTEP-01)"
            )
            continue
        normalized = normalize(body)
        if "Costly-case refusals" not in body and "costly-case refusals" not in body.lower():
            errors.append(
                f"{CARDS_REL} #{title}: missing Costly-case refusals field "
                "(STEWARD-DOOR-LOCKSTEP-01)"
            )
        for bullet in bullets:
            if bullet not in normalized:
                errors.append(
                    f"{CARDS_REL} #{title}: costly-case wording missing "
                    f"{bullet!r} (STEWARD-DOOR-LOCKSTEP-01)"
                )

    duty = sections.get("Duty to resist")
    if duty is None:
        errors.append(
            f"{CARDS_REL}: missing Duty to resist operator screen "
            "(STEWARD-DOOR-LOCKSTEP-01)"
        )
    elif not duty_steps_in_order(duty):
        errors.append(
            f"{CARDS_REL} #Duty to resist: missing instruction received / "
            "refuse / document / escalate sequence (STEWARD-DOOR-LOCKSTEP-01)"
        )

    logging = sections.get("Minimum inspectable-action set")
    if logging is None:
        errors.append(
            f"{CARDS_REL}: missing Minimum inspectable-action set "
            "(STEWARD-DOOR-LOCKSTEP-01)"
        )
        logging = ""
    if "default logging contract" not in logging.lower():
        errors.append(
            f"{CARDS_REL} #Minimum inspectable-action set: must name the "
            "default logging contract (STEWARD-DOOR-LOCKSTEP-01)"
        )
    if "default logging contract" not in cs4.lower():
        errors.append(
            f"{CS4_REL}: CS-4 §10 must name the default logging contract "
            "(STEWARD-DOOR-LOCKSTEP-01)"
        )
    for phrase in INSPECTABLE_PHRASES:
        if phrase not in cs4.lower():
            errors.append(
                f"{CS4_REL}: missing inspectable-action phrase {phrase!r} "
                "(STEWARD-DOOR-LOCKSTEP-01)"
            )
        if phrase not in logging.lower():
            errors.append(
                f"{CARDS_REL} #Minimum inspectable-action set: missing "
                f"{phrase!r} (STEWARD-DOOR-LOCKSTEP-01)"
            )
    if "what was **decided**" not in cs4 and "what was decided" not in cs4.lower():
        errors.append(
            f"{CS4_REL}: missing decided item (STEWARD-DOOR-LOCKSTEP-01)"
        )
    if "what was **decided**" not in logging and "what was decided" not in logging.lower():
        errors.append(
            f"{CARDS_REL} #Minimum inspectable-action set: missing decided "
            "item (STEWARD-DOOR-LOCKSTEP-01)"
        )
    if "Contribution" not in logging or "Violation" not in logging:
        errors.append(
            f"{CARDS_REL} #Minimum inspectable-action set: missing "
            "Contribution / Violation axis records (STEWARD-DOOR-LOCKSTEP-01)"
        )
    return errors


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    errors = audit(root)
    if errors:
        print(f"FAIL: {len(errors)} steward-door lockstep finding(s)")
        for err in errors:
            print(err)
        return 1
    print(
        "PASS: steward-entry cards match core costly cases, duty-to-resist "
        "sequence, CS-4 §10 logging contract, and the README edition pin."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
