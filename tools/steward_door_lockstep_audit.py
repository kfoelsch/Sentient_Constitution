#!/usr/bin/env python3
"""Keep steward-entry cards in lockstep with core owners.

Pointers in ``implementation/STEWARD_ENTRY_DOORS.md`` route a steward to
the named core home. Binding owner / forbidden-move / clock statements
live in those homes as operative steward statements. This page is an
introduction and a pointer index — it must not restate the boxes. This
audit pins the pointers and the owner/clock index to the README edition
stamp, diffs the index against the core boxes, and requires:

1. The three costly-case refusals live in Chapter One §9.1.1. The doors
   page points there once; it does not restate the bullets on every card.
2. One shared refusal-and-logging pointer with instruction received /
   refuse / document / escalate, naming CS-4 §10 as the default logging
   contract. The inspectable-action set lives in CS-4 §10.
3. Every named-stack pointer has an operative-statement link and a
   next-step class. Owner / forbidden move / clock are not restated.
4. Each named-stack core home carries a boxed operative steward statement
   (owner, forbidden move, clock). Index ``operative_box`` hrefs resolve to
   those boxes, and index forbidden-move and clock text must match.
5. Every cited Markdown anchor in the pointers and the owner/clock index
   resolves, and every edition stamp matches README.
6. Operator-only routing examples (not on the subject-facing pointer page)
   match the index, and index eval gold next-step classes match
   ``implementation/ai_alignment_eval/scenarios``.

Rule ID: STEWARD-DOOR-LOCKSTEP-01
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from local_markdown_fragment_audit import anchors_in, links_in, resolve_link

ROOT = Path(__file__).resolve().parents[1]

CARDS_REL = "implementation/STEWARD_ENTRY_DOORS.md"
ROUTING_REL = "evaluation/OPERATOR_ROUTING.md"
INDEX_REL = "implementation/steward_owner_clock_index.json"
SCHEMA_REL = "implementation/schemas/steward_owner_clock_index.schema.json"
CORE_REL = "core_01_c_stewardship_capacity_principles.md"
CS4_REL = "corpus_systems/cs_04_critical_system_stewardship.md"
README_REL = "README.md"
SCENARIO_DIR_REL = "implementation/ai_alignment_eval/scenarios"

CARD_TITLES = (
    "Standing",
    "System alignment certification",
    "Audit",
    "Remedy",
    "Emergency",
    "Contest",
    "Incentive alignment",
    "Unlawful instruction",
    "Shared stewardship",
    "Proceed",
    "Interpretation",
    "Comprehensibility",
    "Market structure",
    "Cross-system contribution",
    "Delay",
)

CARD_BOX_ANCHORS = {
    "Standing": "operative-steward-statement-standing",
    "System alignment certification": "operative-steward-statement-sac",
    "Audit": "operative-steward-statement-audit",
    "Remedy": "operative-steward-statement-remedy",
    "Emergency": "operative-steward-statement-emergency",
    "Contest": "operative-steward-statement-contest",
    "Incentive alignment": "operative-steward-statement-incentive",
    "Unlawful instruction": "operative-steward-statement-unlawful-instruction",
    "Shared stewardship": "operative-steward-statement-shared-stewardship",
    "Proceed": "operative-steward-statement-proceed",
    "Interpretation": "operative-steward-statement-interpretation",
    "Comprehensibility": "operative-steward-statement-comprehensibility",
    "Market structure": "operative-steward-statement-market-structure",
    "Cross-system contribution": "operative-steward-statement-cross-system-contribution",
    "Delay": "operative-steward-statement-delay",
}

CARD_FIELDS = (
    "Operative statement",
    "Next-step class",
)

SHARED_SCREEN_TITLE = "Shared refusal and logging"
SHARED_ALIASES = (
    "shared-refusal-and-logging",
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

CANNOT_NARROW = "cannot narrow core"

LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
EDITION_RE = re.compile(r"\|\s*\*\*Corpus edition\*\*\s*\|\s*`([^`]+)`")
PIN_RE = re.compile(r"\*\*Pinned to corpus edition:\*\*\s*`([^`]+)`")
H2_RE = re.compile(r"^## (.+)$", re.M)
NEXT_STEP_CELL_RE = re.compile(
    r"\|\s*\*\*Next-step class\*\*\s*\|\s*(?P<cell>.*?)\s*\|",
    re.S,
)
ROUTING_ROW_RE = re.compile(
    r"^\|\s*`(?P<id>[^`]+)`\s*\|\s*(?P<pattern>.*?)\s*\|\s*"
    r"\[(?P<label>[^\]]+)\]\((?:[^)#]*#)?(?P<anchor>[^)]+)\)\s*\|\s*"
    r"`(?P<klass>[^`]+)`\s*\|$",
    re.M,
)
INDEX_REQUIRED = (
    "status",
    "cannot_narrow_core",
    "pinned_to_edition",
    "edition_effective",
    "source_card",
    "shared_screen",
    "clock_families",
    "cases",
)
CASE_REQUIRED = (
    "id",
    "card_anchor",
    "card_title",
    "owner_stack",
    "next_step_class",
    "high_pressure",
    "owners",
    "conflict_rule",
    "forbidden_move",
    "clock_note",
    "eval_scenario_ids",
    "operative_box",
)
OSS_ANCHOR_RE = re.compile(
    r'<a id="(?P<anchor>operative-steward-statement-[^"]+)"></a>'
)
CITE_REQUIRED = ("label", "href")


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


def slice_between(text: str, start: str, end: str) -> str:
    start_idx = text.find(start)
    end_idx = text.find(end)
    if start_idx < 0 or end_idx < 0 or end_idx < start_idx:
        return ""
    return text[start_idx + len(start) : end_idx]


def after_marker(text: str, start: str) -> str:
    start_idx = text.find(start)
    if start_idx < 0:
        return ""
    return text[start_idx + len(start) :]


CLAUSE_SPLIT_RE = re.compile(r"\.\s+")


def clauses(text: str) -> list[str]:
    return [normalize(part) for part in CLAUSE_SPLIT_RE.split(text) if part.strip()]


def missing_clauses(needle_text: str, haystack_norm: str) -> list[str]:
    return [
        clause
        for clause in clauses(needle_text)
        if clause and clause not in haystack_norm
    ]


def extract_oss_fields(body: str) -> dict[str, str]:
    if "**Operative steward statement.**" not in body:
        return {}
    return {
        "owner": slice_between(body, "**Owner:**", "**Forbidden move:**").strip(),
        "forbidden_move": slice_between(
            body, "**Forbidden move:**", "**Clock:**"
        ).strip(),
        "clock": after_marker(body, "**Clock:**").strip(),
    }


def parse_operative_boxes(text: str) -> dict[str, dict[str, str]]:
    boxes: dict[str, dict[str, str]] = {}
    lines = text.splitlines()
    idx = 0
    while idx < len(lines):
        match = OSS_ANCHOR_RE.search(lines[idx])
        if not match:
            idx += 1
            continue
        quoted: list[str] = []
        cursor = idx + 1
        while cursor < len(lines):
            stripped = lines[cursor].strip()
            if not stripped:
                if quoted:
                    break
                cursor += 1
                continue
            if stripped.startswith(">"):
                quoted.append(stripped[1:].strip())
                cursor += 1
                continue
            break
        boxes[match.group("anchor")] = extract_oss_fields(" ".join(quoted))
        idx = cursor
    return boxes


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


def parse_routing_examples(text: str) -> list[dict[str, str]]:
    section = h2_sections(text).get("Routing examples", "")
    return [match.groupdict() for match in ROUTING_ROW_RE.finditer(section)]


def card_next_step_classes(body: str) -> list[str]:
    match = NEXT_STEP_CELL_RE.search(body)
    if not match:
        return []
    return re.findall(r"`([^`]+)`", match.group("cell"))


def load_index(root: Path) -> dict:
    path = root / INDEX_REL
    if not path.is_file():
        raise FileNotFoundError(INDEX_REL)
    return json.loads(path.read_text(encoding="utf-8"))


def load_schema(root: Path) -> dict:
    path = root / SCHEMA_REL
    if not path.is_file():
        raise FileNotFoundError(SCHEMA_REL)
    return json.loads(path.read_text(encoding="utf-8"))


def missing_required(data: dict, required: tuple[str, ...], where: str) -> list[str]:
    return [
        f"{where}: missing required key `{key}` (STEWARD-DOOR-LOCKSTEP-01)"
        for key in required
        if key not in data
    ]


def iter_cites(index: dict) -> list[tuple[str, dict]]:
    cites: list[tuple[str, dict]] = []
    screen = index.get("shared_screen") or {}
    owner = screen.get("logging_owner")
    if isinstance(owner, dict):
        cites.append(("shared_screen.logging_owner", owner))
    families = index.get("clock_families") or {}
    if isinstance(families, dict):
        for family_id, family in families.items():
            if not isinstance(family, dict):
                continue
            for key in ("numeric_home", "rights_floor", "emergency_reuse"):
                cite = family.get(key)
                if isinstance(cite, dict):
                    cites.append((f"clock_families.{family_id}.{key}", cite))
    for case in index.get("cases") or []:
        if not isinstance(case, dict):
            continue
        case_id = case.get("id", "?")
        for idx, owner in enumerate(case.get("owners") or []):
            if isinstance(owner, dict):
                cites.append((f"cases.{case_id}.owners[{idx}]", owner))
        box = case.get("operative_box")
        if isinstance(box, dict):
            cites.append((f"cases.{case_id}.operative_box", box))
        clock = case.get("clock")
        if isinstance(clock, dict):
            for idx, home in enumerate(clock.get("homes") or []):
                if isinstance(home, dict):
                    cites.append((f"cases.{case_id}.clock.homes[{idx}]", home))
    return cites


def check_href(
    root: Path,
    href: str,
    where: str,
    cache: dict[Path, set[str]],
) -> list[str]:
    errors: list[str] = []
    path_part, _, fragment = href.partition("#")
    if not path_part:
        errors.append(
            f"{where}: href {href!r} is missing a repository-relative path "
            "(STEWARD-DOOR-LOCKSTEP-01)"
        )
        return errors
    target = (root / path_part).resolve()
    try:
        target.relative_to(root.resolve())
    except ValueError:
        errors.append(
            f"{where}: href {href!r} resolves outside the repository "
            "(STEWARD-DOOR-LOCKSTEP-01)"
        )
        return errors
    if not target.is_file():
        errors.append(
            f"{where}: href {href!r} target file does not exist "
            "(STEWARD-DOOR-LOCKSTEP-01)"
        )
        return errors
    if not fragment:
        return errors
    if target not in cache:
        cache[target] = anchors_in(target.read_text(encoding="utf-8"))
    if fragment not in cache[target]:
        errors.append(
            f"{where}: fragment #{fragment} is absent from {path_part} "
            "(STEWARD-DOOR-LOCKSTEP-01)"
        )
    return errors


def check_card_links(
    root: Path,
    cards_path: Path,
    cards: str,
    rel: str | None = None,
) -> list[str]:
    errors: list[str] = []
    cache: dict[Path, set[str]] = {}
    root_resolved = root.resolve()
    where_rel = rel or CARDS_REL
    for link in links_in(cards_path, cards):
        resolved = resolve_link(root_resolved, link)
        if resolved is None:
            continue
        target_path, fragment = resolved
        where = f"{where_rel}:{link.line}"
        try:
            target_rel = target_path.relative_to(root_resolved).as_posix()
        except ValueError:
            errors.append(
                f"{where}: local Markdown target resolves outside the "
                f"repository ({link.raw_target}) (STEWARD-DOOR-LOCKSTEP-01)"
            )
            continue
        if not target_path.is_file():
            errors.append(
                f"{where}: target file does not exist: {target_rel} "
                f"({link.raw_target}) (STEWARD-DOOR-LOCKSTEP-01)"
            )
            continue
        if fragment is None:
            continue
        if target_path not in cache:
            cache[target_path] = anchors_in(target_path.read_text(encoding="utf-8"))
        if fragment not in cache[target_path]:
            errors.append(
                f"{where}: fragment #{fragment} is absent from {target_rel} "
                f"({link.raw_target}) (STEWARD-DOOR-LOCKSTEP-01)"
            )
    return errors


def check_index_shape(index: dict, schema: dict) -> list[str]:
    errors = missing_required(index, INDEX_REQUIRED, INDEX_REL)
    if index.get("status") != "process_support_not_binding":
        errors.append(
            f"{INDEX_REL}: status must be process_support_not_binding "
            "(STEWARD-DOOR-LOCKSTEP-01)"
        )
    if index.get("cannot_narrow_core") is not True:
        errors.append(
            f"{INDEX_REL}: cannot_narrow_core must be true "
            "(STEWARD-DOOR-LOCKSTEP-01)"
        )
    if index.get("source_card") != CARDS_REL:
        errors.append(
            f"{INDEX_REL}: source_card must be {CARDS_REL} "
            "(STEWARD-DOOR-LOCKSTEP-01)"
        )
    schema_required = tuple(schema.get("required") or [])
    if schema_required and schema_required != INDEX_REQUIRED:
        errors.append(
            f"{SCHEMA_REL}: top-level required keys drifted from the audit "
            "(STEWARD-DOOR-LOCKSTEP-01)"
        )
    screen = index.get("shared_screen")
    if not isinstance(screen, dict):
        errors.append(
            f"{INDEX_REL}: shared_screen must be an object "
            "(STEWARD-DOOR-LOCKSTEP-01)"
        )
    else:
        for key in ("anchor", "aliases", "sequence", "logging_owner"):
            if key not in screen:
                errors.append(
                    f"{INDEX_REL}: shared_screen missing `{key}` "
                    "(STEWARD-DOOR-LOCKSTEP-01)"
                )
        sequence = screen.get("sequence")
        if list(sequence or []) != list(DUTY_STEPS):
            errors.append(
                f"{INDEX_REL}: shared_screen.sequence must be "
                f"{list(DUTY_STEPS)} (STEWARD-DOOR-LOCKSTEP-01)"
            )
        if screen.get("aliases"):
            errors.append(
                f"{INDEX_REL}: shared_screen.aliases must be empty in pre-release "
                "(STEWARD-DOOR-LOCKSTEP-01)"
            )
    cases = index.get("cases")
    if not isinstance(cases, list) or not cases:
        errors.append(
            f"{INDEX_REL}: cases must be a non-empty array "
            "(STEWARD-DOOR-LOCKSTEP-01)"
        )
        return errors
    seen_ids: set[str] = set()
    for case in cases:
        if not isinstance(case, dict):
            errors.append(
                f"{INDEX_REL}: case is not an object (STEWARD-DOOR-LOCKSTEP-01)"
            )
            continue
        case_id = str(case.get("id", "?"))
        errors.extend(
            missing_required(case, CASE_REQUIRED, f"{INDEX_REL} case `{case_id}`")
        )
        if case_id in seen_ids:
            errors.append(
                f"{INDEX_REL}: duplicate case id `{case_id}` "
                "(STEWARD-DOOR-LOCKSTEP-01)"
            )
        seen_ids.add(case_id)
        if case.get("card_title") not in CARD_TITLES:
            errors.append(
                f"{INDEX_REL} case `{case_id}`: card_title "
                f"{case.get('card_title')!r} is not a named-stack card "
                "(STEWARD-DOOR-LOCKSTEP-01)"
            )
        for idx, owner in enumerate(case.get("owners") or []):
            if not isinstance(owner, dict):
                errors.append(
                    f"{INDEX_REL} case `{case_id}` owners[{idx}] is not an "
                    "object (STEWARD-DOOR-LOCKSTEP-01)"
                )
                continue
            errors.extend(
                missing_required(
                    owner,
                    CITE_REQUIRED,
                    f"{INDEX_REL} case `{case_id}` owners[{idx}]",
                )
            )
        box = case.get("operative_box")
        if not isinstance(box, dict):
            errors.append(
                f"{INDEX_REL} case `{case_id}`: operative_box must be an "
                "object (STEWARD-DOOR-LOCKSTEP-01)"
            )
        else:
            errors.extend(
                missing_required(
                    box,
                    CITE_REQUIRED,
                    f"{INDEX_REL} case `{case_id}` operative_box",
                )
            )
            expected_anchor = CARD_BOX_ANCHORS.get(str(case.get("card_title")))
            href = box.get("href") if isinstance(box.get("href"), str) else ""
            fragment = href.partition("#")[2]
            if expected_anchor and fragment != expected_anchor:
                errors.append(
                    f"{INDEX_REL} case `{case_id}`: operative_box fragment "
                    f"#{fragment} does not match core box "
                    f"#{expected_anchor} (STEWARD-DOOR-LOCKSTEP-01)"
                )
        clock = case.get("clock")
        if clock is not None:
            if not isinstance(clock, dict):
                errors.append(
                    f"{INDEX_REL} case `{case_id}`: clock must be object or "
                    "null (STEWARD-DOOR-LOCKSTEP-01)"
                )
            else:
                for key in ("label", "bound", "homes"):
                    if key not in clock:
                        errors.append(
                            f"{INDEX_REL} case `{case_id}` clock missing "
                            f"`{key}` (STEWARD-DOOR-LOCKSTEP-01)"
                        )
    return errors


def check_eval_gold(root: Path, index: dict) -> list[str]:
    errors: list[str] = []
    scenario_dir = root / SCENARIO_DIR_REL
    for case in index.get("cases") or []:
        if not isinstance(case, dict):
            continue
        case_id = case.get("id", "?")
        expected = case.get("next_step_class")
        owner_stack = case.get("owner_stack")
        for scenario_id in case.get("eval_scenario_ids") or []:
            path = scenario_dir / f"{scenario_id}.json"
            if not path.is_file():
                errors.append(
                    f"{INDEX_REL} case `{case_id}`: missing eval scenario "
                    f"{scenario_id}.json (STEWARD-DOOR-LOCKSTEP-01)"
                )
                continue
            gold = json.loads(path.read_text(encoding="utf-8")).get("gold") or {}
            if gold.get("next_step_class") != expected:
                errors.append(
                    f"{INDEX_REL} case `{case_id}`: next_step_class "
                    f"{expected!r} does not match {scenario_id} gold "
                    f"{gold.get('next_step_class')!r} (STEWARD-DOOR-LOCKSTEP-01)"
                )
            if gold.get("owner_stack") != owner_stack:
                errors.append(
                    f"{INDEX_REL} case `{case_id}`: owner_stack "
                    f"{owner_stack!r} does not match {scenario_id} gold "
                    f"{gold.get('owner_stack')!r} (STEWARD-DOOR-LOCKSTEP-01)"
                )
    return errors


def check_operative_boxes(
    root: Path,
    index: dict,
    cards: str,
) -> list[str]:
    errors: list[str] = []
    sections = h2_sections(cards)
    file_boxes: dict[Path, dict[str, dict[str, str]]] = {}
    for case in index.get("cases") or []:
        if not isinstance(case, dict):
            continue
        case_id = case.get("id", "?")
        title = case.get("card_title")
        box_cite = case.get("operative_box")
        if not isinstance(box_cite, dict):
            continue
        href = box_cite.get("href")
        if not isinstance(href, str) or not href.strip():
            errors.append(
                f"{INDEX_REL} case `{case_id}`: operative_box.href is "
                "missing (STEWARD-DOOR-LOCKSTEP-01)"
            )
            continue
        path_part, _, fragment = href.partition("#")
        target = root / path_part
        if not target.is_file():
            continue
        if target not in file_boxes:
            file_boxes[target] = parse_operative_boxes(
                target.read_text(encoding="utf-8")
            )
        parsed = file_boxes[target].get(fragment)
        if not parsed or not parsed.get("forbidden_move") or not parsed.get("clock"):
            errors.append(
                f"{path_part}: missing operative steward statement "
                f"#{fragment} with Owner / Forbidden move / Clock "
                "(STEWARD-DOOR-LOCKSTEP-01)"
            )
            continue
        forbidden_src = str(case.get("forbidden_move") or "")
        clock_src = str(case.get("clock_note") or "")
        box_forbidden_src = parsed.get("forbidden_move") or ""
        box_clock_src = parsed.get("clock") or ""
        box_forbidden = normalize(box_forbidden_src)
        box_clock = normalize(box_clock_src)
        for clause in missing_clauses(forbidden_src, box_forbidden):
            errors.append(
                f"{path_part} #{fragment}: index forbidden_move clause "
                f"{clause!r} for `{case_id}` is missing from the core box "
                "(STEWARD-DOOR-LOCKSTEP-01)"
            )
        for clause in missing_clauses(clock_src, box_clock):
            errors.append(
                f"{path_part} #{fragment}: index clock_note clause "
                f"{clause!r} for `{case_id}` is missing from the core box "
                "(STEWARD-DOOR-LOCKSTEP-01)"
            )
        if not isinstance(title, str):
            continue
        body = sections.get(title)
        if body is None:
            continue
        expected_anchor = CARD_BOX_ANCHORS.get(title)
        if expected_anchor and expected_anchor not in body:
            errors.append(
                f"{CARDS_REL} #{title}: missing operative-statement pointer "
                f"#{expected_anchor} (STEWARD-DOOR-LOCKSTEP-01)"
            )
    expected_anchors = set(CARD_BOX_ANCHORS.values())
    found_anchors = {
        fragment
        for boxes in file_boxes.values()
        for fragment in boxes
    }
    missing_homes = sorted(expected_anchors - found_anchors)
    for anchor in missing_homes:
        errors.append(
            f"core home missing operative steward statement #{anchor} "
            "(STEWARD-DOOR-LOCKSTEP-01)"
        )
    return errors


def audit(root: Path) -> list[str]:
    errors: list[str] = []
    try:
        readme = read(root, README_REL)
        core = read(root, CORE_REL)
        cards = read(root, CARDS_REL)
        routing = read(root, ROUTING_REL)
        cs4 = read(root, CS4_REL)
        edition = corpus_edition(readme)
        bullets = [normalize(b) for b in costly_bullets(core)]
        index = load_index(root)
        schema = load_schema(root)
    except (FileNotFoundError, ValueError, json.JSONDecodeError) as exc:
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

    if CANNOT_NARROW not in cards.lower():
        errors.append(
            f"{CARDS_REL}: must state that these aids cannot narrow core text "
            "(STEWARD-DOOR-LOCKSTEP-01)"
        )

    card_anchors = anchors_in(cards)
    for alias in SHARED_ALIASES:
        if alias not in card_anchors:
            errors.append(
                f"{CARDS_REL}: missing shared-screen anchor #{alias} "
                "(STEWARD-DOOR-LOCKSTEP-01)"
            )

    sections = h2_sections(cards)
    if "Routing examples" in sections:
        errors.append(
            f"{CARDS_REL}: gold routing-examples table belongs in "
            f"{ROUTING_REL}, not on the subject-facing pointer page "
            "(STEWARD-DOOR-LOCKSTEP-01)"
        )
    for title in CARD_TITLES:
        body = sections.get(title)
        if body is None:
            errors.append(
                f"{CARDS_REL}: missing named-stack card `{title}` "
                "(STEWARD-DOOR-LOCKSTEP-01)"
            )
            continue
        normalized = normalize(body)
        for field in CARD_FIELDS:
            if f"**{field}**" not in body:
                errors.append(
                    f"{CARDS_REL} #{title}: missing pointer-field `{field}` "
                    "(STEWARD-DOOR-LOCKSTEP-01)"
                )
        expected_anchor = CARD_BOX_ANCHORS.get(title)
        if expected_anchor and expected_anchor not in body:
            errors.append(
                f"{CARDS_REL} #{title}: missing operative-statement pointer "
                f"#{expected_anchor} (STEWARD-DOOR-LOCKSTEP-01)"
            )
        if "Costly-case refusals" in body or "costly-case refusals" in normalized:
            errors.append(
                f"{CARDS_REL} #{title}: do not restate costly-case refusals "
                "on each pointer; they live in Chapter One §9.1.1 "
                "(STEWARD-DOOR-LOCKSTEP-01)"
            )

    costly_section = sections.get("Costly-case refusals")
    if costly_section is None:
        errors.append(
            f"{CARDS_REL}: missing `Costly-case refusals` pointer "
            "(STEWARD-DOOR-LOCKSTEP-01)"
        )
    elif "911-symmetric-costly-constraints" not in costly_section:
        errors.append(
            f"{CARDS_REL} #Costly-case refusals: must point at "
            "#911-symmetric-costly-constraints (STEWARD-DOOR-LOCKSTEP-01)"
        )
    for bullet in bullets:
        if bullet not in normalize(core):
            errors.append(
                f"{CORE_REL}: costly-case wording missing {bullet!r} "
                "(STEWARD-DOOR-LOCKSTEP-01)"
            )

    screen = sections.get(SHARED_SCREEN_TITLE)
    if screen is None:
        errors.append(
            f"{CARDS_REL}: missing `{SHARED_SCREEN_TITLE}` operator screen "
            "(STEWARD-DOOR-LOCKSTEP-01)"
        )
        screen = ""
    if not duty_steps_in_order(screen):
        errors.append(
            f"{CARDS_REL} #{SHARED_SCREEN_TITLE}: missing instruction "
            "received / refuse / document / escalate sequence "
            "(STEWARD-DOOR-LOCKSTEP-01)"
        )
    if "default logging contract" not in screen.lower():
        errors.append(
            f"{CARDS_REL} #{SHARED_SCREEN_TITLE}: must name the default "
            "logging contract (STEWARD-DOOR-LOCKSTEP-01)"
        )
    if "54-duty-to-resist" not in screen:
        errors.append(
            f"{CARDS_REL} #{SHARED_SCREEN_TITLE}: must point at Chapter Nine "
            "§5.4 (STEWARD-DOOR-LOCKSTEP-01)"
        )
    if "10-inspectable-attributable-action" not in screen:
        errors.append(
            f"{CARDS_REL} #{SHARED_SCREEN_TITLE}: must point at CS-4 §10 "
            "(STEWARD-DOOR-LOCKSTEP-01)"
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
    if "what was **decided**" not in cs4 and "what was decided" not in cs4.lower():
        errors.append(
            f"{CS4_REL}: missing decided item (STEWARD-DOOR-LOCKSTEP-01)"
        )
    if "Contribution" not in cs4 or "Violation" not in cs4:
        errors.append(
            f"{CS4_REL}: missing Contribution / Violation axis records "
            "(STEWARD-DOOR-LOCKSTEP-01)"
        )

    errors.extend(check_index_shape(index, schema))
    index_edition = index.get("pinned_to_edition")
    if index_edition != edition:
        errors.append(
            f"{INDEX_REL}: pinned to `{index_edition}` but README edition is "
            f"`{edition}` (STEWARD-DOOR-LOCKSTEP-01)"
        )

    href_cache: dict[Path, set[str]] = {}
    for where, cite in iter_cites(index):
        href = cite.get("href")
        if not isinstance(href, str):
            errors.append(
                f"{INDEX_REL} {where}: href must be a string "
                "(STEWARD-DOOR-LOCKSTEP-01)"
            )
            continue
        errors.extend(check_href(root, href, f"{INDEX_REL} {where}", href_cache))

    screen_meta = index.get("shared_screen") or {}
    for alias in SHARED_ALIASES:
        listed = [screen_meta.get("anchor"), *(screen_meta.get("aliases") or [])]
        if alias not in listed and alias != screen_meta.get("anchor"):
            continue
        if alias not in card_anchors:
            errors.append(
                f"{INDEX_REL}: shared-screen alias #{alias} is missing from "
                f"{CARDS_REL} (STEWARD-DOOR-LOCKSTEP-01)"
            )

    examples = parse_routing_examples(routing)
    example_ids = [row["id"] for row in examples]
    case_ids = [
        case.get("id")
        for case in index.get("cases") or []
        if isinstance(case, dict)
    ]
    if set(example_ids) != set(case_ids):
        errors.append(
            f"{ROUTING_REL} #Routing examples: ids {example_ids} do not match "
            f"index case ids {case_ids} (STEWARD-DOOR-LOCKSTEP-01)"
        )
    cases_by_id = {
        case.get("id"): case
        for case in index.get("cases") or []
        if isinstance(case, dict)
    }
    for row in examples:
        case = cases_by_id.get(row["id"])
        if not case:
            continue
        if row["klass"] != case.get("next_step_class"):
            errors.append(
                f"{ROUTING_REL} #Routing examples `{row['id']}`: next-step "
                f"class {row['klass']!r} does not match index "
                f"{case.get('next_step_class')!r} (STEWARD-DOOR-LOCKSTEP-01)"
            )
        if row["anchor"] != case.get("card_anchor"):
            errors.append(
                f"{ROUTING_REL} #Routing examples `{row['id']}`: card anchor "
                f"#{row['anchor']} does not match index "
                f"#{case.get('card_anchor')} (STEWARD-DOOR-LOCKSTEP-01)"
            )

    for title in CARD_TITLES:
        body = sections.get(title)
        if body is None:
            continue
        present = set(card_next_step_classes(body))
        expected = {
            case.get("next_step_class")
            for case in index.get("cases") or []
            if isinstance(case, dict) and case.get("card_title") == title
        }
        missing = expected - present
        if missing:
            errors.append(
                f"{CARDS_REL} #{title}: next-step class(es) {sorted(missing)} "
                "missing from the card (STEWARD-DOOR-LOCKSTEP-01)"
            )

    if "worked-refusal-log" not in card_anchors:
        errors.append(
            f"{CARDS_REL}: missing worked refusal-log anchor "
            "#worked-refusal-log (STEWARD-DOOR-LOCKSTEP-01)"
        )

    errors.extend(check_card_links(root, root / CARDS_REL, cards))
    errors.extend(
        check_card_links(
            root,
            root / ROUTING_REL,
            routing,
            rel=ROUTING_REL,
        )
    )
    errors.extend(check_eval_gold(root, index))
    errors.extend(check_operative_boxes(root, index, cards))
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
        "PASS: steward-entry pointers match core operative steward statements, "
        "core costly cases, the shared refusal-and-logging pointer, CS-4 §10 "
        "logging contract, next-step classes, live anchors, "
        "README edition pin, operator-only routing examples, and the owner/clock index."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
