#!/usr/bin/env python3
"""Validate the base Materially Binding Act Record form.

This validator asks whether an Act Record carries the mechanically checkable
Chapter Seven §7 minimum. It does not decide the merits, validate the claimed
authority, or replace independent verification.

Rule ID: ACT-RECORD-01
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_REL = "implementation/schemas/materially_binding_act_record.schema.json"
EXAMPLES_REL = "implementation/schemas/examples"
SCHEMA_ID = "materially_binding_act_record"
SCHEMA_VERSION = "1"
RULE = "ACT-RECORD-01"

ROOT_KEYS = (
    "schema_id",
    "schema_version",
    "record_id",
    "record_version",
    "recorded_at",
    "updated_at",
    "act",
    "seats",
    "determination",
    "custody",
    "contest",
    "events",
    "clocks",
    "links",
)
SEAT_KEYS = ("initiating", "verify_or_authorize", "record", "contest")
PLACEMENT_STATUSES = (
    "held",
    "substitute",
    "permitted_merged_hosting",
    "vacant_routed",
    "conflicted_routed",
    "unplaced_gap",
)
ACT_STATUSES = (
    "initiated",
    "pending_verification",
    "authorized",
    "conditioned",
    "declined",
    "implemented",
    "suspended",
    "superseded",
    "emergency_pending_review",
    "closed",
)
DETERMINATION_STATUSES = (
    "pending",
    "verified",
    "authorized",
    "conditioned",
    "declined",
    "emergency_pending_review",
)
CONTEST_STATUSES = (
    "none_received",
    "open",
    "routed",
    "resolved",
    "correction_required",
)
EVENT_TYPES = (
    "initiation",
    "determination",
    "record_entry",
    "handoff",
    "delegation",
    "recusal",
    "substitution",
    "permitted_merger",
    "emergency_departure",
    "refusal",
    "condition",
    "objection",
    "challenge",
    "routing",
    "correction",
    "supersession",
    "implementation",
    "suspension",
    "closure",
)
CLOCK_STATUSES = ("running", "paused", "satisfied", "expired", "not_applicable")
LINK_KEYS = (
    "evidence",
    "source_logs",
    "process_records",
    "superseded_versions",
    "corrections",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "record",
        nargs="?",
        type=Path,
        help="Path to an Act Record JSON file. Omit with --self-check.",
    )
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument(
        "--self-check",
        action="store_true",
        help="Validate the schema and bundled fixtures.",
    )
    return parser.parse_args()


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def finding(where: str, message: str) -> str:
    return f"{where}: {message} ({RULE})"


def missing_required(data: dict, required: tuple[str, ...], where: str) -> list[str]:
    return [
        finding(where, f"missing required key `{key}`")
        for key in required
        if key not in data
    ]


def require_nonempty_string(data: dict, key: str, where: str) -> list[str]:
    if key not in data:
        return []
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        return [finding(f"{where}.{key}", "must be a non-empty string")]
    return []


def parse_timestamp(value: object, where: str, *, nullable: bool = False) -> tuple[datetime | None, list[str]]:
    if value is None and nullable:
        return None, []
    if not isinstance(value, str) or not value.strip():
        return None, [finding(where, "must be an ISO-8601 timestamp")]
    text = value.strip()
    candidates = [text]
    if text.endswith("Z"):
        candidates.append(text[:-1] + "+00:00")
    for candidate in candidates:
        try:
            return datetime.fromisoformat(candidate), []
        except ValueError:
            continue
    return None, [finding(where, f"{value!r} is not an ISO-8601 timestamp")]


def check_seats(value: object) -> list[str]:
    if not isinstance(value, dict):
        return [finding("seats", "must be an object")]
    errors = [
        finding(f"seats.{key}", "missing required seat")
        for key in SEAT_KEYS
        if key not in value
    ]
    for name in SEAT_KEYS:
        seat = value.get(name)
        where = f"seats.{name}"
        if seat is None:
            continue
        if not isinstance(seat, dict):
            errors.append(finding(where, "must be an object"))
            continue
        errors.extend(
            missing_required(seat, ("placement_status", "holder_or_route", "authority"), where)
        )
        if seat.get("placement_status") not in PLACEMENT_STATUSES:
            errors.append(
                finding(
                    f"{where}.placement_status",
                    f"must be one of {list(PLACEMENT_STATUSES)}",
                )
            )
        errors.extend(require_nonempty_string(seat, "holder_or_route", where))
        errors.extend(require_nonempty_string(seat, "authority", where))

    holders: dict[str, str] = {}
    for name in SEAT_KEYS:
        seat = value.get(name)
        if isinstance(seat, dict) and seat.get("placement_status") in {
            "held",
            "substitute",
            "permitted_merged_hosting",
        }:
            holder = seat.get("holder_or_route")
            if isinstance(holder, str) and holder.strip():
                holders[name] = holder.strip()
    prohibited = (
        ("initiating", "verify_or_authorize"),
        ("verify_or_authorize", "record"),
        ("verify_or_authorize", "contest"),
    )
    for left, right in prohibited:
        if left in holders and holders.get(left) == holders.get(right):
            errors.append(
                finding(
                    "seats",
                    f"{left} and {right} identify the same holder {holders[left]!r}",
                )
            )
    return errors


def check_act(value: object) -> list[str]:
    if not isinstance(value, dict):
        return [finding("act", "must be an object")]
    required = ("act_id", "description", "material_scope", "status", "governing_authority")
    errors = missing_required(value, required, "act")
    for key in ("act_id", "description", "material_scope", "governing_authority"):
        errors.extend(require_nonempty_string(value, key, "act"))
    if value.get("status") not in ACT_STATUSES:
        errors.append(finding("act.status", f"must be one of {list(ACT_STATUSES)}"))
    return errors


def check_determination(value: object) -> list[str]:
    if not isinstance(value, dict):
        return [finding("determination", "must be an object")]
    required = (
        "status",
        "standard_applied",
        "determined_by",
        "determined_at",
        "reasons",
        "conditions",
    )
    errors = missing_required(value, required, "determination")
    status = value.get("status")
    if status not in DETERMINATION_STATUSES:
        errors.append(
            finding(
                "determination.status",
                f"must be one of {list(DETERMINATION_STATUSES)}",
            )
        )
    errors.extend(require_nonempty_string(value, "standard_applied", "determination"))
    pending = status in {"pending", "emergency_pending_review"}
    if not pending:
        errors.extend(require_nonempty_string(value, "determined_by", "determination"))
        _, stamp_errors = parse_timestamp(value.get("determined_at"), "determination.determined_at")
        errors.extend(stamp_errors)
    elif value.get("determined_at") is not None:
        _, stamp_errors = parse_timestamp(
            value.get("determined_at"), "determination.determined_at", nullable=True
        )
        errors.extend(stamp_errors)
    for key in ("reasons", "conditions"):
        if key in value and not isinstance(value[key], list):
            errors.append(finding(f"determination.{key}", "must be an array"))
    return errors


def check_custody(value: object, record_version: object) -> list[str]:
    if not isinstance(value, dict):
        return [finding("custody", "must be an object")]
    required = ("entered_by", "custody_authority", "version_entered", "entered_at")
    errors = missing_required(value, required, "custody")
    for key in ("entered_by", "custody_authority"):
        errors.extend(require_nonempty_string(value, key, "custody"))
    version = value.get("version_entered")
    if not isinstance(version, int) or isinstance(version, bool) or version < 1:
        errors.append(finding("custody.version_entered", "must be an integer of at least 1"))
    elif isinstance(record_version, int) and version != record_version:
        errors.append(
            finding(
                "custody.version_entered",
                f"{version} does not match record_version {record_version}",
            )
        )
    if "entered_at" in value:
        _, stamp_errors = parse_timestamp(value.get("entered_at"), "custody.entered_at")
        errors.extend(stamp_errors)
    return errors


def check_contest(value: object) -> list[str]:
    if not isinstance(value, dict):
        return [finding("contest", "must be an object")]
    errors = missing_required(value, ("route", "status"), "contest")
    errors.extend(require_nonempty_string(value, "route", "contest"))
    status = value.get("status")
    if status not in CONTEST_STATUSES:
        errors.append(finding("contest.status", f"must be one of {list(CONTEST_STATUSES)}"))
    received = value.get("challenge_received_at")
    if status != "none_received" and received is None:
        errors.append(
            finding(
                "contest.challenge_received_at",
                "is required when a challenge is open, routed, resolved, or requires correction",
            )
        )
    elif received is not None:
        _, stamp_errors = parse_timestamp(received, "contest.challenge_received_at")
        errors.extend(stamp_errors)
    return errors


def check_events(value: object) -> list[str]:
    if not isinstance(value, list):
        return [finding("events", "must be an array")]
    errors: list[str] = []
    for index, event in enumerate(value):
        where = f"events[{index}]"
        if not isinstance(event, dict):
            errors.append(finding(where, "must be an object"))
            continue
        errors.extend(missing_required(event, ("event_type", "at", "actor", "description"), where))
        if event.get("event_type") not in EVENT_TYPES:
            errors.append(finding(f"{where}.event_type", f"must be one of {list(EVENT_TYPES)}"))
        for key in ("actor", "description"):
            errors.extend(require_nonempty_string(event, key, where))
        if "at" in event:
            _, stamp_errors = parse_timestamp(event.get("at"), f"{where}.at")
            errors.extend(stamp_errors)
    return errors


def check_clocks(value: object) -> list[str]:
    if not isinstance(value, list):
        return [finding("clocks", "must be an array")]
    errors: list[str] = []
    for index, clock in enumerate(value):
        where = f"clocks[{index}]"
        if not isinstance(clock, dict):
            errors.append(finding(where, "must be an object"))
            continue
        errors.extend(missing_required(clock, ("clock_id", "authority", "status", "started_at"), where))
        for key in ("clock_id", "authority"):
            errors.extend(require_nonempty_string(clock, key, where))
        status = clock.get("status")
        if status not in CLOCK_STATUSES:
            errors.append(finding(f"{where}.status", f"must be one of {list(CLOCK_STATUSES)}"))
        for key in ("started_at", "deadline_at", "satisfied_at"):
            if key in clock and clock[key] is not None:
                _, stamp_errors = parse_timestamp(clock[key], f"{where}.{key}")
                errors.extend(stamp_errors)
        if status != "not_applicable" and clock.get("started_at") is None:
            errors.append(finding(f"{where}.started_at", "is required for an applicable clock"))
    return errors


def check_links(value: object) -> list[str]:
    if not isinstance(value, dict):
        return [finding("links", "must be an object")]
    errors = missing_required(value, LINK_KEYS, "links")
    for key in LINK_KEYS:
        items = value.get(key)
        where = f"links.{key}"
        if items is None:
            continue
        if not isinstance(items, list):
            errors.append(finding(where, "must be an array"))
            continue
        for index, item in enumerate(items):
            item_where = f"{where}[{index}]"
            if not isinstance(item, dict):
                errors.append(finding(item_where, "must be an object"))
                continue
            errors.extend(missing_required(item, ("id", "relation"), item_where))
            for field in ("id", "relation"):
                errors.extend(require_nonempty_string(item, field, item_where))
    return errors


def validate_record(record: object) -> list[str]:
    if not isinstance(record, dict):
        return [finding("record", "top level must be an object")]
    errors = missing_required(record, ROOT_KEYS, "record")
    if record.get("schema_id") != SCHEMA_ID:
        errors.append(finding("schema_id", f"must be {SCHEMA_ID!r}"))
    if record.get("schema_version") != SCHEMA_VERSION:
        errors.append(finding("schema_version", f"must be {SCHEMA_VERSION!r}"))
    errors.extend(require_nonempty_string(record, "record_id", "record"))
    version = record.get("record_version")
    if not isinstance(version, int) or isinstance(version, bool) or version < 1:
        errors.append(finding("record_version", "must be an integer of at least 1"))

    recorded = updated = None
    if "recorded_at" in record:
        recorded, stamp_errors = parse_timestamp(record.get("recorded_at"), "recorded_at")
        errors.extend(stamp_errors)
    if "updated_at" in record:
        updated, stamp_errors = parse_timestamp(record.get("updated_at"), "updated_at")
        errors.extend(stamp_errors)
    if recorded is not None and updated is not None and updated < recorded:
        errors.append(finding("updated_at", "must not precede recorded_at"))

    if "act" in record:
        errors.extend(check_act(record.get("act")))
    if "seats" in record:
        errors.extend(check_seats(record.get("seats")))
    if "determination" in record:
        errors.extend(check_determination(record.get("determination")))
    if "custody" in record:
        errors.extend(check_custody(record.get("custody"), version))
    if "contest" in record:
        errors.extend(check_contest(record.get("contest")))
    if "events" in record:
        errors.extend(check_events(record.get("events")))
    if "clocks" in record:
        errors.extend(check_clocks(record.get("clocks")))
    if "links" in record:
        errors.extend(check_links(record.get("links")))
    return errors


def self_check(root: Path) -> list[str]:
    errors: list[str] = []
    schema_path = root / SCHEMA_REL
    if not schema_path.is_file():
        return [f"missing {SCHEMA_REL}"]
    schema = load_json(schema_path)
    if not isinstance(schema, dict) or schema.get("$id") != Path(SCHEMA_REL).name:
        errors.append(finding(SCHEMA_REL, f"$id must be {Path(SCHEMA_REL).name!r}"))
    examples = root / EXAMPLES_REL
    valid_path = examples / "materially_binding_act_record.valid.json"
    invalid_path = examples / "materially_binding_act_record.invalid.json"
    if not valid_path.is_file():
        errors.append(f"missing example {valid_path.as_posix()}")
    else:
        errors.extend(
            f"{valid_path.name}: {item}" for item in validate_record(load_json(valid_path))
        )
    if not invalid_path.is_file():
        errors.append(f"missing example {invalid_path.as_posix()}")
    else:
        findings = validate_record(load_json(invalid_path))
        if not findings:
            errors.append(finding(invalid_path.name, "expected validation failures"))
        for expected in ("record_id", "seats.contest", "determined_by", "version_entered"):
            if not any(expected in item for item in findings):
                errors.append(
                    finding(invalid_path.name, f"did not flag expected `{expected}` failure")
                )
    return errors


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    if args.self_check:
        try:
            errors = self_check(root)
        except (OSError, json.JSONDecodeError) as exc:
            print(f"FAIL: {exc}")
            return 1
        if errors:
            print(f"FAIL: {len(errors)} Act Record schema finding(s)")
            for error in errors:
                print(error)
            return 1
        print("PASS: Materially Binding Act Record schema and fixtures.")
        return 0
    if args.record is None:
        print("Provide an Act Record JSON path, or use --self-check.")
        return 2
    if not args.record.is_file():
        print(f"FAIL: record file does not exist: {args.record}")
        return 1
    try:
        record = load_json(args.record)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"FAIL: {args.record}: {exc}")
        return 1
    errors = validate_record(record)
    if errors:
        print(f"FAIL: {len(errors)} Act Record finding(s) in {args.record}")
        for error in errors:
            print(error)
        return 1
    print(f"PASS: {args.record} satisfies the base Act Record form.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
