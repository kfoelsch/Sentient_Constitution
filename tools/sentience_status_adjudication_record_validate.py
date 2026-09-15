#!/usr/bin/env python3
"""Validate a Sentience-Status Adjudication Record against the dedicated schema.

The schema is machine-checkable form, not who-counts and not a standing record.
This tool asks a mechanical question: does the file carry the Chapter Eleven
minimum fields — including independent representative and intake-decline log —
plus the review trigger, without extra keys?

Rule ID: SSAR-01
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_REL = "implementation/schemas/sentience_status_adjudication_record.schema.json"
SCHEMA_ID = "sentience_status_adjudication_record"
SCHEMA_VERSION = "2"
REQUIRED = (
    "schema_id",
    "schema_version",
    "subject_entity",
    "status_determination_or_live_contested_posture",
    "lead_forum_family",
    "chapter_eleven_special_route",
    "indicators_and_expert_evidence",
    "interim_contested_sentient_life_treatment",
    "review_trigger",
    "narrowing",
    "reopening_evidence_standard",
    "independent_representative",
    "intake_decline_log",
)
OPTIONAL = ("recorded_at", "case_id")
STATUS_VALUES = (
    "affirmed",
    "narrowed",
    "revoked",
    "restored",
    "still contested",
)
LEAD_FAMILIES = (
    "Technical Forum Domains",
    "Constitutional",
    "Integrity",
    "Institutional",
    "Environment",
    "Sentient",
)
SPECIAL_ROUTES = ("none", "Constitutional", "Integrity", "Institutional")
EVIDENCE_REQUIRED = (
    "indicators",
    "expert_evidence",
    "material_uncertainty_noted",
)
INTERIM_REQUIRED = ("status_remains_live", "treatment")
NARROWING_REQUIRED = ("expected_closure_timeline", "periodic_review_trigger")
REPRESENTATIVE_REQUIRED = (
    "appointed",
    "appointment_path",
    "conflict_screen",
    "access_terms",
)
INTAKE_DECLINE_REQUIRED = (
    "this_filing_declined",
    "log_location",
    "integrity_sample_cadence",
    "floor_indicator_set",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "record",
        nargs="?",
        type=Path,
        help="Path to a Sentience-Status Adjudication Record JSON file. "
        "Omit with --self-check.",
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


def require_object(value: object, where: str) -> tuple[dict | None, list[str]]:
    if not isinstance(value, dict):
        return None, [f"{where}: must be an object (SSAR-01)"]
    return value, []


def require_nonempty_string(value: object, where: str) -> list[str]:
    if not isinstance(value, str) or not value.strip():
        return [f"{where}: must be a non-empty string (SSAR-01)"]
    return []


def require_nullable_string(value: object, where: str) -> list[str]:
    if value is None:
        return []
    return require_nonempty_string(value, where)


def validate_record(record: object) -> list[str]:
    obj, errors = require_object(record, "record")
    if obj is None:
        return errors

    unknown = sorted(set(obj) - set(REQUIRED) - set(OPTIONAL))
    if unknown:
        errors.append(
            "record: unknown keys "
            + ", ".join(unknown)
            + " (SSAR-01; additionalProperties false)"
        )

    for key in REQUIRED:
        if key not in obj:
            errors.append(f"record: missing required field {key!r} (SSAR-01)")

    if obj.get("schema_id") != SCHEMA_ID:
        errors.append(
            f"schema_id: must be {SCHEMA_ID!r} (SSAR-01)"
        )
    if obj.get("schema_version") != SCHEMA_VERSION:
        errors.append(
            f"schema_version: must be {SCHEMA_VERSION!r} (SSAR-01)"
        )

    subject, subject_errors = require_object(
        obj.get("subject_entity"), "subject_entity"
    )
    errors.extend(subject_errors)
    if subject is not None:
        if "id" not in subject:
            errors.append("subject_entity: missing required field 'id' (SSAR-01)")
        else:
            errors.extend(require_nonempty_string(subject.get("id"), "subject_entity.id"))
        extra = sorted(set(subject) - {"id", "label"})
        if extra:
            errors.append(
                "subject_entity: unknown keys "
                + ", ".join(extra)
                + " (SSAR-01)"
            )

    status = obj.get("status_determination_or_live_contested_posture")
    if status not in STATUS_VALUES:
        errors.append(
            "status_determination_or_live_contested_posture: "
            f"must be one of {STATUS_VALUES} (SSAR-01)"
        )

    if obj.get("lead_forum_family") not in LEAD_FAMILIES:
        errors.append(
            f"lead_forum_family: must be one of {LEAD_FAMILIES} (SSAR-01)"
        )
    if obj.get("chapter_eleven_special_route") not in SPECIAL_ROUTES:
        errors.append(
            "chapter_eleven_special_route: "
            f"must be one of {SPECIAL_ROUTES} (SSAR-01)"
        )

    evidence, evidence_errors = require_object(
        obj.get("indicators_and_expert_evidence"),
        "indicators_and_expert_evidence",
    )
    errors.extend(evidence_errors)
    if evidence is not None:
        for key in EVIDENCE_REQUIRED:
            if key not in evidence:
                errors.append(
                    f"indicators_and_expert_evidence: missing {key!r} (SSAR-01)"
                )
            else:
                errors.extend(
                    require_nonempty_string(
                        evidence.get(key),
                        f"indicators_and_expert_evidence.{key}",
                    )
                )

    interim, interim_errors = require_object(
        obj.get("interim_contested_sentient_life_treatment"),
        "interim_contested_sentient_life_treatment",
    )
    errors.extend(interim_errors)
    if interim is not None:
        for key in INTERIM_REQUIRED:
            if key not in interim:
                errors.append(
                    "interim_contested_sentient_life_treatment: "
                    f"missing {key!r} (SSAR-01)"
                )
        if "status_remains_live" in interim and not isinstance(
            interim.get("status_remains_live"), bool
        ):
            errors.append(
                "interim_contested_sentient_life_treatment.status_remains_live: "
                "must be a boolean (SSAR-01)"
            )
        if "treatment" in interim:
            errors.extend(
                require_nonempty_string(
                    interim.get("treatment"),
                    "interim_contested_sentient_life_treatment.treatment",
                )
            )

    errors.extend(require_nonempty_string(obj.get("review_trigger"), "review_trigger"))

    narrowing, narrowing_errors = require_object(obj.get("narrowing"), "narrowing")
    errors.extend(narrowing_errors)
    if narrowing is not None:
        for key in NARROWING_REQUIRED:
            if key not in narrowing:
                errors.append(f"narrowing: missing {key!r} (SSAR-01)")
            elif status == "narrowed":
                errors.extend(
                    require_nonempty_string(
                        narrowing.get(key), f"narrowing.{key}"
                    )
                )
            else:
                errors.extend(
                    require_nullable_string(
                        narrowing.get(key), f"narrowing.{key}"
                    )
                )

    reopening, reopening_errors = require_object(
        obj.get("reopening_evidence_standard"),
        "reopening_evidence_standard",
    )
    errors.extend(reopening_errors)
    if reopening is not None:
        if reopening.get("standard") != "new verified evidence":
            errors.append(
                "reopening_evidence_standard.standard: "
                "must be 'new verified evidence' (SSAR-01)"
            )
        if reopening.get("calendar_only_reopening") != "forbidden":
            errors.append(
                "reopening_evidence_standard.calendar_only_reopening: "
                "must be 'forbidden' (SSAR-01)"
            )

    representative, representative_errors = require_object(
        obj.get("independent_representative"),
        "independent_representative",
    )
    errors.extend(representative_errors)
    if representative is not None:
        extra = sorted(
            set(representative)
            - set(REPRESENTATIVE_REQUIRED)
            - {"appointee_id"}
        )
        if extra:
            errors.append(
                "independent_representative: unknown keys "
                + ", ".join(extra)
                + " (SSAR-01)"
            )
        for key in REPRESENTATIVE_REQUIRED:
            if key not in representative:
                errors.append(
                    f"independent_representative: missing {key!r} (SSAR-01)"
                )
        if "appointed" in representative and not isinstance(
            representative.get("appointed"), bool
        ):
            errors.append(
                "independent_representative.appointed: must be a boolean (SSAR-01)"
            )
        for key in ("appointment_path", "conflict_screen", "access_terms"):
            if key in representative:
                errors.extend(
                    require_nonempty_string(
                        representative.get(key),
                        f"independent_representative.{key}",
                    )
                )
        if representative.get("appointee_id") is not None:
            errors.extend(
                require_nonempty_string(
                    representative.get("appointee_id"),
                    "independent_representative.appointee_id",
                )
            )

    decline, decline_errors = require_object(
        obj.get("intake_decline_log"),
        "intake_decline_log",
    )
    errors.extend(decline_errors)
    if decline is not None:
        extra = sorted(
            set(decline)
            - set(INTAKE_DECLINE_REQUIRED)
            - {"indicator_cited", "reason"}
        )
        if extra:
            errors.append(
                "intake_decline_log: unknown keys "
                + ", ".join(extra)
                + " (SSAR-01)"
            )
        for key in INTAKE_DECLINE_REQUIRED:
            if key not in decline:
                errors.append(
                    f"intake_decline_log: missing {key!r} (SSAR-01)"
                )
        declined = decline.get("this_filing_declined")
        if "this_filing_declined" in decline and not isinstance(declined, bool):
            errors.append(
                "intake_decline_log.this_filing_declined: "
                "must be a boolean (SSAR-01)"
            )
        for key in (
            "log_location",
            "integrity_sample_cadence",
            "floor_indicator_set",
        ):
            if key in decline:
                errors.extend(
                    require_nonempty_string(
                        decline.get(key),
                        f"intake_decline_log.{key}",
                    )
                )
        if declined is True:
            for key in ("indicator_cited", "reason"):
                errors.extend(
                    require_nonempty_string(
                        decline.get(key),
                        f"intake_decline_log.{key}",
                    )
                )
        else:
            for key in ("indicator_cited", "reason"):
                if key in decline:
                    errors.extend(
                        require_nullable_string(
                            decline.get(key),
                            f"intake_decline_log.{key}",
                        )
                    )

    return errors


def self_check(root: Path) -> list[str]:
    schema_path = root / SCHEMA_REL
    examples = root / "implementation" / "schemas" / "examples"
    errors: list[str] = []
    try:
        schema = load_json(schema_path)
    except (OSError, json.JSONDecodeError) as exc:
        return [f"{SCHEMA_REL}: cannot load ({exc})"]
    if not isinstance(schema, dict):
        return [f"{SCHEMA_REL}: schema root must be an object"]
    if schema.get("$id") != "sentience_status_adjudication_record.schema.json":
        errors.append(f"{SCHEMA_REL}: unexpected $id")

    valid_names = (
        "sentience_status_adjudication_record.valid.json",
        "sentience_status_adjudication_record.narrowed.valid.json",
    )
    for name in valid_names:
        path = examples / name
        try:
            record = load_json(path)
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{name}: cannot load ({exc})")
            continue
        found = validate_record(record)
        if found:
            errors.append(f"{name}: expected to pass; {found[0]}")

    invalid_path = examples / "sentience_status_adjudication_record.invalid.json"
    try:
        invalid = load_json(invalid_path)
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(
            "sentience_status_adjudication_record.invalid.json: "
            f"cannot load ({exc})"
        )
        return errors
    found = validate_record(invalid)
    if not found:
        errors.append(
            "sentience_status_adjudication_record.invalid.json: "
            "expected failures (empty subject id and missing review_trigger)"
        )
    else:
        blob = " ".join(found)
        if "subject_entity.id" not in blob:
            errors.append(
                "sentience_status_adjudication_record.invalid.json: "
                "did not flag empty subject_entity.id"
            )
        if "review_trigger" not in blob:
            errors.append(
                "sentience_status_adjudication_record.invalid.json: "
                "did not flag missing review_trigger"
            )
    return errors


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    if args.self_check:
        errors = self_check(root)
        if errors:
            print("\n".join(errors), file=sys.stderr)
            return 1
        print("Sentience-Status Adjudication Record fixtures match SSAR-01.")
        return 0
    if args.record is None:
        print("Provide a record path or --self-check.", file=sys.stderr)
        return 2
    try:
        record = load_json(args.record)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"{args.record}: cannot load ({exc})", file=sys.stderr)
        return 1
    errors = validate_record(record)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"{args.record}: valid Sentience-Status Adjudication Record (SSAR-01).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
