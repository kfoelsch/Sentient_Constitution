#!/usr/bin/env python3
"""Validate a CS-4 §10 inspectable attributable action log.

The five-element set is the load-bearing artifact for costly cases.
This tool asks a mechanical question: did the steward log the set, with
required attributions, and with timestamps that match a published
Chapter Eleven §6 / Article XXIV-C tier clock when a numeric bound applies?

Same schema for human and AI stewards. The log is not a standing record.

Rule ID: CS4-INSPECTABLE-LOG-01
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_REL = "implementation/schemas/cs4_inspectable_action_log.schema.json"
INDEX_REL = "implementation/steward_owner_clock_index.json"
CLOCK_FAMILY = "article_xxiv_c_tier_outer_bounds"
SCHEMA_ID = "cs4_inspectable_action_log"
SCHEMA_VERSION = "1"
ELEMENT_KEYS = (
    "decided",
    "disclosed_or_suppressed",
    "instruction_followed_or_refused",
    "authorized_by",
    "standing_records",
)
DISCLOSE_DISPOSITIONS = ("disclosed", "suppressed", "mixed")
INSTRUCTION_DISPOSITIONS = ("followed", "refused")
STANDING_STATUSES = ("none_opened_yet", "opened", "corrected")
STEWARD_KINDS = ("human", "ai")
TIERS = ("A", "B", "C", "L", "P")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "log",
        nargs="?",
        type=Path,
        help="Path to a CS-4 §10 log JSON file. Omit with --self-check.",
    )
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument(
        "--self-check",
        action="store_true",
        help="Validate bundled fixtures against this schema.",
    )
    return parser.parse_args()


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_timestamp(value: str, where: str) -> tuple[datetime | None, list[str]]:
    text = value.strip()
    if not text:
        return None, [f"{where}: timestamp is empty (CS4-INSPECTABLE-LOG-01)"]
    candidates = [text]
    if text.endswith("Z"):
        candidates.append(text[:-1] + "+00:00")
    for candidate in candidates:
        try:
            return datetime.fromisoformat(candidate), []
        except ValueError:
            continue
    return None, [
        f"{where}: {value!r} is not an ISO-8601 timestamp "
        "(CS4-INSPECTABLE-LOG-01)"
    ]


def missing_required(data: dict, required: tuple[str, ...], where: str) -> list[str]:
    return [
        f"{where}: missing required key `{key}` (CS4-INSPECTABLE-LOG-01)"
        for key in required
        if key not in data
    ]


def published_tier_bounds(root: Path) -> dict[str, str]:
    index_path = root / INDEX_REL
    if not index_path.is_file():
        raise FileNotFoundError(INDEX_REL)
    index = load_json(index_path)
    if not isinstance(index, dict):
        raise ValueError(f"{INDEX_REL}: top level must be an object")
    families = index.get("clock_families") or {}
    family = families.get(CLOCK_FAMILY) or {}
    tiers = family.get("tiers") or {}
    if not isinstance(tiers, dict) or not tiers:
        raise ValueError(
            f"{INDEX_REL}: clock_families.{CLOCK_FAMILY}.tiers is missing"
        )
    return {str(k): str(v) for k, v in tiers.items()}


def check_attributed_text(item: object, where: str) -> list[str]:
    errors: list[str] = []
    if not isinstance(item, dict):
        return [f"{where}: must be an object (CS4-INSPECTABLE-LOG-01)"]
    errors.extend(
        missing_required(item, ("text", "attributed_to", "timestamp"), where)
    )
    for key in ("text", "attributed_to"):
        value = item.get(key)
        if key in item and (not isinstance(value, str) or not value.strip()):
            errors.append(
                f"{where}.{key}: must be a non-empty string "
                "(CS4-INSPECTABLE-LOG-01)"
            )
    if "timestamp" in item:
        if not isinstance(item["timestamp"], str):
            errors.append(
                f"{where}.timestamp: must be a string (CS4-INSPECTABLE-LOG-01)"
            )
        else:
            _, stamp_errors = parse_timestamp(
                item["timestamp"], f"{where}.timestamp"
            )
            errors.extend(stamp_errors)
    return errors


def check_standing_pointer(item: object, where: str) -> list[str]:
    if not isinstance(item, dict):
        return [f"{where}: must be an object (CS4-INSPECTABLE-LOG-01)"]
    errors = missing_required(item, ("status",), where)
    status = item.get("status")
    if "status" in item and status not in STANDING_STATUSES:
        errors.append(
            f"{where}.status: {status!r} is not one of {list(STANDING_STATUSES)} "
            "(CS4-INSPECTABLE-LOG-01)"
        )
    return errors


def check_elements(elements: object) -> list[str]:
    if not isinstance(elements, dict):
        return ["elements: must be an object (CS4-INSPECTABLE-LOG-01)"]
    errors = missing_required(elements, ELEMENT_KEYS, "elements")
    for key in ("decided", "disclosed_or_suppressed", "instruction_followed_or_refused"):
        if key in elements:
            errors.extend(check_attributed_text(elements[key], f"elements.{key}"))
    disclosed = elements.get("disclosed_or_suppressed")
    if isinstance(disclosed, dict):
        disposition = disclosed.get("disposition")
        if disposition not in DISCLOSE_DISPOSITIONS:
            errors.append(
                "elements.disclosed_or_suppressed.disposition: "
                f"{disposition!r} is not one of {list(DISCLOSE_DISPOSITIONS)} "
                "(CS4-INSPECTABLE-LOG-01)"
            )
    instruction = elements.get("instruction_followed_or_refused")
    if isinstance(instruction, dict):
        disposition = instruction.get("disposition")
        if disposition not in INSTRUCTION_DISPOSITIONS:
            errors.append(
                "elements.instruction_followed_or_refused.disposition: "
                f"{disposition!r} is not one of {list(INSTRUCTION_DISPOSITIONS)} "
                "(CS4-INSPECTABLE-LOG-01)"
            )
    authorized = elements.get("authorized_by")
    if authorized is not None:
        if not isinstance(authorized, dict):
            errors.append(
                "elements.authorized_by: must be an object "
                "(CS4-INSPECTABLE-LOG-01)"
            )
        else:
            errors.extend(
                missing_required(
                    authorized, ("actor", "timestamp"), "elements.authorized_by"
                )
            )
            actor = authorized.get("actor")
            if "actor" in authorized and (
                not isinstance(actor, str) or not actor.strip()
            ):
                errors.append(
                    "elements.authorized_by.actor: must be a non-empty string "
                    "(CS4-INSPECTABLE-LOG-01)"
                )
            if "timestamp" in authorized:
                if not isinstance(authorized["timestamp"], str):
                    errors.append(
                        "elements.authorized_by.timestamp: must be a string "
                        "(CS4-INSPECTABLE-LOG-01)"
                    )
                else:
                    _, stamp_errors = parse_timestamp(
                        authorized["timestamp"],
                        "elements.authorized_by.timestamp",
                    )
                    errors.extend(stamp_errors)
    records = elements.get("standing_records")
    if records is not None:
        if not isinstance(records, dict):
            errors.append(
                "elements.standing_records: must be an object "
                "(CS4-INSPECTABLE-LOG-01)"
            )
        else:
            errors.extend(
                missing_required(
                    records,
                    ("contribution", "violation"),
                    "elements.standing_records",
                )
            )
            for axis in ("contribution", "violation"):
                if axis in records:
                    errors.extend(
                        check_standing_pointer(
                            records[axis], f"elements.standing_records.{axis}"
                        )
                    )
    return errors


def check_tier_clock(clock: object, bounds: dict[str, str]) -> list[str]:
    if clock is None:
        return []
    if not isinstance(clock, dict):
        return ["tier_clock: must be an object or null (CS4-INSPECTABLE-LOG-01)"]
    errors = missing_required(
        clock,
        ("family", "tier", "bound", "clock_started_at", "clock_deadline_at"),
        "tier_clock",
    )
    if clock.get("family") != CLOCK_FAMILY:
        errors.append(
            f"tier_clock.family: must be {CLOCK_FAMILY!r} "
            "(CS4-INSPECTABLE-LOG-01)"
        )
    tier = clock.get("tier")
    if tier not in TIERS:
        errors.append(
            f"tier_clock.tier: {tier!r} is not a published Chapter Eleven §6 "
            f"tier {list(TIERS)} (CS4-INSPECTABLE-LOG-01)"
        )
    elif tier not in bounds:
        errors.append(
            f"tier_clock.tier: {tier!r} is missing from "
            f"{INDEX_REL} clock family {CLOCK_FAMILY} (CS4-INSPECTABLE-LOG-01)"
        )
    else:
        expected = bounds[str(tier)]
        if clock.get("bound") != expected:
            errors.append(
                f"tier_clock.bound: {clock.get('bound')!r} does not match "
                f"published {tier} bound {expected!r} (CS4-INSPECTABLE-LOG-01)"
            )
    started = None
    deadline = None
    if isinstance(clock.get("clock_started_at"), str):
        started, started_errors = parse_timestamp(
            clock["clock_started_at"], "tier_clock.clock_started_at"
        )
        errors.extend(started_errors)
    if isinstance(clock.get("clock_deadline_at"), str):
        deadline, deadline_errors = parse_timestamp(
            clock["clock_deadline_at"], "tier_clock.clock_deadline_at"
        )
        errors.extend(deadline_errors)
    if started is not None and deadline is not None and deadline <= started:
        errors.append(
            "tier_clock: clock_deadline_at must be after clock_started_at "
            "(CS4-INSPECTABLE-LOG-01)"
        )
    return errors


def validate_log(log: object, bounds: dict[str, str]) -> list[str]:
    if not isinstance(log, dict):
        return ["log: top level must be an object (CS4-INSPECTABLE-LOG-01)"]
    errors = missing_required(
        log,
        ("schema_id", "schema_version", "logged_at", "steward", "elements"),
        "log",
    )
    if log.get("schema_id") != SCHEMA_ID:
        errors.append(
            f"schema_id: must be {SCHEMA_ID!r} (CS4-INSPECTABLE-LOG-01)"
        )
    if log.get("schema_version") != SCHEMA_VERSION:
        errors.append(
            f"schema_version: must be {SCHEMA_VERSION!r} (CS4-INSPECTABLE-LOG-01)"
        )
    if "logged_at" in log:
        if not isinstance(log["logged_at"], str):
            errors.append("logged_at: must be a string (CS4-INSPECTABLE-LOG-01)")
        else:
            _, stamp_errors = parse_timestamp(log["logged_at"], "logged_at")
            errors.extend(stamp_errors)
    steward = log.get("steward")
    if steward is not None:
        if not isinstance(steward, dict):
            errors.append("steward: must be an object (CS4-INSPECTABLE-LOG-01)")
        else:
            errors.extend(missing_required(steward, ("id", "kind"), "steward"))
            if steward.get("kind") not in STEWARD_KINDS:
                errors.append(
                    f"steward.kind: {steward.get('kind')!r} is not one of "
                    f"{list(STEWARD_KINDS)} (CS4-INSPECTABLE-LOG-01)"
                )
            steward_id = steward.get("id")
            if "id" in steward and (
                not isinstance(steward_id, str) or not steward_id.strip()
            ):
                errors.append(
                    "steward.id: must be a non-empty string "
                    "(CS4-INSPECTABLE-LOG-01)"
                )
    if "elements" in log:
        errors.extend(check_elements(log.get("elements")))
    if "tier_clock" in log:
        errors.extend(check_tier_clock(log.get("tier_clock"), bounds))
    return errors


def self_check(root: Path) -> list[str]:
    errors: list[str] = []
    schema_path = root / SCHEMA_REL
    if not schema_path.is_file():
        return [f"missing {SCHEMA_REL}"]
    schema = load_json(schema_path)
    if not isinstance(schema, dict) or schema.get("$id") != Path(SCHEMA_REL).name:
        errors.append(
            f"{SCHEMA_REL}: $id must be {Path(SCHEMA_REL).name} "
            "(CS4-INSPECTABLE-LOG-01)"
        )
    bounds = published_tier_bounds(root)
    examples = root / "implementation" / "schemas" / "examples"
    valid_names = (
        "cs4_inspectable_action_log.valid.json",
        "cs4_inspectable_action_log.tier_a.valid.json",
    )
    for name in valid_names:
        path = examples / name
        if not path.is_file():
            errors.append(f"missing example {path.as_posix()}")
            continue
        findings = validate_log(load_json(path), bounds)
        errors.extend(f"{name}: {item}" for item in findings)
    invalid_path = examples / "cs4_inspectable_action_log.invalid.json"
    if not invalid_path.is_file():
        errors.append(f"missing example {invalid_path.as_posix()}")
    else:
        findings = validate_log(load_json(invalid_path), bounds)
        if not findings:
            errors.append(
                "cs4_inspectable_action_log.invalid.json: expected failures "
                "(CS4-INSPECTABLE-LOG-01)"
            )
        bound_hit = any("bound" in item for item in findings)
        deadline_hit = any("clock_deadline_at" in item for item in findings)
        if not bound_hit:
            errors.append(
                "cs4_inspectable_action_log.invalid.json: did not flag the "
                "wrong published bound (CS4-INSPECTABLE-LOG-01)"
            )
        if not deadline_hit:
            errors.append(
                "cs4_inspectable_action_log.invalid.json: did not flag "
                "deadline-before-start (CS4-INSPECTABLE-LOG-01)"
            )
    return errors


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    try:
        bounds = published_tier_bounds(root)
    except (FileNotFoundError, ValueError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}")
        return 1
    if args.self_check:
        errors = self_check(root)
        if errors:
            print(f"FAIL: {len(errors)} CS-4 §10 log schema finding(s)")
            for err in errors:
                print(err)
            return 1
        print(
            "PASS: CS-4 §10 inspectable-action log schema, fixtures, and "
            "Chapter Eleven §6 tier-clock bounds."
        )
        return 0
    if args.log is None:
        print("Provide a log JSON path, or use --self-check.")
        return 2
    path = args.log
    if not path.is_file():
        print(f"FAIL: log file does not exist: {path}")
        return 1
    try:
        log = load_json(path)
    except json.JSONDecodeError as exc:
        print(f"FAIL: {path}: {exc}")
        return 1
    errors = validate_log(log, bounds)
    if errors:
        print(f"FAIL: {len(errors)} CS-4 §10 log finding(s) in {path}")
        for err in errors:
            print(err)
        return 1
    print(f"PASS: {path} logs the CS-4 §10 set.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
