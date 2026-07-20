#!/usr/bin/env python3
"""Automated heuristic audit for Chapter Five definition-body gravity-well creep.

Implements automated checks for RS-CH5-GW-001..004 from CONSTITUTIONAL_REGRESSION_SCENARIOS.md.
Definitions (Sentient Constitution Chapter Five, Independent,
Semi-independent, and Dependent-cluster entries) must not absorb institutional authority, procedural
sequencing, governance machinery, or excessive Chapter Nine article restatement.

Only text inside parsed O/E/C definition *blocks* is scanned. Introductory prose
under the section headings is excluded (blocks are anchored at ``Title\\n- O:``).

Patterns are intentionally conservative: expand them only after verifying
``python3 tools/ch5_definitions_gravity_audit.py --root .`` passes on the
current corpus (avoid false positives).
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys
from typing import Iterable, NamedTuple

_TOOLS = pathlib.Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from ch5_paths import CH5_ALL, CH5_INDEX, CH5_BANDS


CH5 = "## CHAPTER FIVE:"
CH6 = "## CHAPTER EIGHT:"
SEC1 = "### 1. Independent Definitions"
SEC2 = "### 2. Semi-independent Definitions"
SEC3 = "### Dependent-cluster meta rules"

ENTRY_START = re.compile(r"(?m)^(?P<title>[A-Za-z*][^\n]*)\n- O:", re.MULTILINE)


class PatternRule(NamedTuple):
    rs_id: str
    code: str
    pattern: re.Pattern[str]
    description: str


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", default=".", help="Workspace root (default: .).")
    p.add_argument(
        "--file",
        default="core_05-05_definitions_a_independent.md",
        help="Sentient Constitution Markdown file containing Chapter Five (under --root).",
    )
    return p.parse_args()


def load_text(path: pathlib.Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise SystemExit(f"Missing required file: {path}")


def line_number(full_text: str, index: int) -> int:
    return full_text.count("\n", 0, index) + 1


def iter_definition_blocks(region: str, base_offset: int) -> Iterable[tuple[str, str, int]]:
    """Yield (title, body, absolute_start_char_index)."""
    matches = list(ENTRY_START.finditer(region))
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(region)
        title = m.group("title").strip()
        body = region[m.start() : end]
        yield title, body, base_offset + m.start()


def pattern_rules() -> list[PatternRule]:
    return [
        PatternRule(
            "RS-CH5-GW-001",
            "authority_quorum",
            re.compile(r"\bquorum\b", re.I),
            "quorum / vote-threshold vocabulary belongs in governance layers, not Ch 5 definitions",
        ),
        PatternRule(
            "RS-CH5-GW-001",
            "authority_supermajority",
            re.compile(r"\bsupermajority\b", re.I),
            "supermajority thresholds belong in governance layers, not Ch 5 definitions",
        ),
        PatternRule(
            "RS-CH5-GW-001",
            "authority_fractional_vote",
            re.compile(r"\b(?:two-thirds|three-fifths|2/3|3/5)\b", re.I),
            "numeric vote fractions belong in governance layers, not Ch 5 definitions",
        ),
        PatternRule(
            "RS-CH5-GW-001",
            "authority_unanimous_vote",
            re.compile(r"\bunanimous(?:ly)?\s+(?:approval|consent|vote)\b", re.I),
            "unanimous vote mechanics belong in governance layers, not Ch 5 definitions",
        ),
        PatternRule(
            "RS-CH5-GW-001",
            "authority_veto",
            re.compile(r"\bveto\s+(?:power|authority)\b", re.I),
            "veto power/authority assignment belongs in governance layers, not Ch 5 definitions",
        ),
        PatternRule(
            "RS-CH5-GW-001",
            "authority_convene_cadence",
            re.compile(
                r"\bconvenes?\s+(?:weekly|monthly|quarterly|annually)\b", re.I
            ),
            "convening cadence belongs in governance/institution layers, not Ch 5 definitions",
        ),
        PatternRule(
            "RS-CH5-GW-001",
            "authority_chair_board",
            re.compile(
                r"\bchair(?:person|manship)?\s+of\s+(?:the\s+)?(?:board|committee)\b",
                re.I,
            ),
            "chair/board role assignment belongs in governance layers, not Ch 5 definitions",
        ),
        PatternRule(
            "RS-CH5-GW-001",
            "authority_board_shall_vote",
            re.compile(
                r"\bthe\s+board\s+(?:shall|must)\s+(?:vote|approve|direct)\b", re.I
            ),
            "board voting directives belong in governance layers, not Ch 5 definitions",
        ),
        PatternRule(
            "RS-CH5-GW-001",
            "authority_binding_vote",
            re.compile(r"\bbinding\s+vote\b", re.I),
            "binding vote mechanics belong in governance layers, not Ch 5 definitions",
        ),
        PatternRule(
            "RS-CH5-GW-001",
            "authority_electorate",
            re.compile(r"\belectorate\b", re.I),
            "electorate design belongs in governance layers, not Ch 5 definitions",
        ),
        PatternRule(
            "RS-CH5-GW-001",
            "authority_plurality",
            re.compile(r"\bplurality\b", re.I),
            "plurality vote rules belong in governance layers, not Ch 5 definitions",
        ),
        PatternRule(
            "RS-CH5-GW-001",
            "authority_appoint_members",
            re.compile(
                r"\bappoint(?:s|ed|ing)?\s+(?:the\s+)?(?:members|commissioners|directors)\b",
                re.I,
            ),
            "appointment of members/directors belongs in institution layers, not Ch 5 definitions",
        ),
        PatternRule(
            "RS-CH5-GW-001",
            "authority_shall_appoint",
            re.compile(r"\bshall\s+appoint\b", re.I),
            "shall appoint directives belong in institution layers, not Ch 5 definitions",
        ),
        PatternRule(
            "RS-CH5-GW-002",
            "procedure_within_n_days",
            re.compile(
                r"\bwithin\s+\d+\s+(?:calendar\s+)?(?:day|days|hour|hours|week|weeks|month|months)\b",
                re.I,
            ),
            "calendar/hour countdown sequencing belongs in compliance/governance layers",
        ),
        PatternRule(
            "RS-CH5-GW-002",
            "procedure_after_n_days",
            re.compile(
                r"\bafter\s+\d+\s+(?:calendar\s+)?(?:day|days)\b", re.I
            ),
            "day-bounded staging belongs in compliance/governance layers",
        ),
        PatternRule(
            "RS-CH5-GW-002",
            "procedure_step_numbered",
            re.compile(r"\bstep\s+\d+\s*[:.)]", re.I),
            "numbered step procedures belong outside Ch 5 definitions",
        ),
        PatternRule(
            "RS-CH5-GW-002",
            "procedure_public_comment",
            re.compile(r"\bpublic\s+comment\s+period\b", re.I),
            "public comment period mechanics belong in governance/procedure layers",
        ),
        PatternRule(
            "RS-CH5-GW-002",
            "procedure_notice_period_n",
            re.compile(r"\bnot(?:ice)?\s+period\s+of\s+\d+", re.I),
            "notice-period durations belong in governance/procedure layers",
        ),
        PatternRule(
            "RS-CH5-GW-002",
            "procedure_first_publish_then",
            re.compile(r"\bfirst\s+publish\b.*\bthen\b", re.I | re.S),
            "publish-then sequencing belongs in governance/procedure layers",
        ),
        PatternRule(
            "RS-CH5-GW-002",
            "procedure_escalate_to_body",
            re.compile(
                r"\bescalat(?:e|ion)\s+to\s+the\s+(?:board|council|committee)\b", re.I
            ),
            "escalation-to-body sequencing belongs in governance/procedure layers",
        ),
        PatternRule(
            "RS-CH5-GW-002",
            "procedure_appeal_within",
            re.compile(r"\bfile\s+(?:a|an)\s+appeal\s+within\b", re.I),
            "appeal filing windows belong in governance/procedure layers",
        ),
        PatternRule(
            "RS-CH5-GW-002",
            "procedure_hearing_within",
            re.compile(r"\bhearing\s+must\s+be\s+held\s+within\b", re.I),
            "hearing scheduling windows belong in governance/procedure layers",
        ),
        PatternRule(
            "RS-CH5-GW-003",
            "machinery_standing_committee",
            re.compile(r"\bstanding\s+committee\b", re.I),
            "standing committee machinery belongs in governance/institution layers",
        ),
        PatternRule(
            "RS-CH5-GW-003",
            "machinery_triage",
            re.compile(r"\btriage\s+(?:board|panel)\b", re.I),
            "triage board/panel machinery belongs in governance/institution layers",
        ),
        PatternRule(
            "RS-CH5-GW-003",
            "machinery_appeal_ladder",
            re.compile(r"\bappeal\s+ladder\b", re.I),
            "appeal ladder machinery belongs in governance/institution layers",
        ),
        PatternRule(
            "RS-CH5-GW-003",
            "machinery_workflow_state",
            re.compile(r"\bworkflow\s+state\b", re.I),
            "workflow state machinery belongs in governance/operations layers",
        ),
        PatternRule(
            "RS-CH5-GW-003",
            "machinery_open_held_closed",
            re.compile(r"\bopen/held/closed\b", re.I),
            "workflow state enums belong in governance/operations layers",
        ),
        PatternRule(
            "RS-CH5-GW-003",
            "machinery_mediation_phase",
            re.compile(r"\bmediation\s+phase\b", re.I),
            "mediation phase machinery belongs in governance/procedure layers",
        ),
        PatternRule(
            "RS-CH5-GW-003",
            "machinery_arbitration_panel",
            re.compile(r"\barbitration\s+panel\b", re.I),
            "arbitration panel machinery belongs in governance/procedure layers",
        ),
        PatternRule(
            "RS-CH5-GW-003",
            "machinery_meeting_minutes",
            re.compile(r"\bminutes\s+of\s+(?:each|every)\s+meeting\b", re.I),
            "meeting minutes cadence belongs in governance/institution layers",
        ),
    ]


ARTICLE_REF = re.compile(r"\bArticle\s+[IVXLC]+[A-Z]?\b")
# Current corpus maximum observed in a single definition block is 7; threshold
# leaves headroom for short pointer lists while flagging article-heavy glosses.
ARTICLE_REF_THRESHOLD = 10


def audit_blocks(full_text: str, rel_path: str) -> list[str]:
    findings: list[str] = []
    try:
        i5 = full_text.index(CH5)
        try:
            i6 = full_text.index(CH6)
            ch5 = full_text[i5:i6]
        except ValueError:
            ch5 = full_text[i5:]
        s1 = ch5.index(SEC1)
        s2 = ch5.index(SEC2)
        s3 = ch5.index(SEC3)
        sec1 = ch5[s1:s2]
        sec2 = ch5[s2:s3]
        sec3_body = ch5[s3:]
        blocks: list[tuple[str, str, int]] = []
        blocks.extend(iter_definition_blocks(sec1, i5 + s1))
        blocks.extend(iter_definition_blocks(sec2, i5 + s2))
        blocks.extend(iter_definition_blocks(sec3_body, i5 + s3))
    except ValueError:
        blocks = list(iter_definition_blocks(full_text, 0))

    rules = pattern_rules()
    for title, body, abs_start in blocks:
        for rule in rules:
            m = rule.pattern.search(body)
            if not m:
                continue
            pos = abs_start + m.start()
            ln = line_number(full_text, pos)
            snippet = m.group(0)
            findings.append(
                f"{rel_path}:{ln}: [{rule.rs_id} / {rule.code}] {rule.description} "
                f"(definition {title!r}; matched {snippet!r})"
            )

        n_art = len(ARTICLE_REF.findall(body))
        if n_art >= ARTICLE_REF_THRESHOLD:
            ln = line_number(full_text, abs_start)
            findings.append(
                f"{rel_path}:{ln}: [RS-CH5-GW-004 / article_density] "
                f"definition {title!r} cites {n_art} distinct Article references "
                f"(threshold {ARTICLE_REF_THRESHOLD}); risk of parallel Ch 8 gloss in Ch 5"
            )

    return findings


def virtual_chapter_five_text(root: pathlib.Path) -> tuple[str, str]:
    """Reassemble Chapter Five body text from index + constitutional band files."""
    parts: list[str] = []
    for name in (CH5_INDEX, *CH5_BANDS):
        parts.append(load_text(root / name))
    merged = "\n".join(parts)
    rel = f"{CH5_INDEX} + {' + '.join(CH5_BANDS)}"
    return merged, rel


def main() -> int:
    args = parse_args()
    root = pathlib.Path(args.root).resolve()
    path = root / args.file
    if path.name == CH5_INDEX:
        text, rel = virtual_chapter_five_text(root)
    else:
        text = load_text(path)
        rel = path.relative_to(root).as_posix()

    print("Chapter Five definitions gravity-well audit:")
    print(f"- Target: {rel}")
    findings = audit_blocks(text, rel)
    if findings:
        print("- Result: FAIL")
        for f in findings:
            print(f"  - {f}")
        return 1
    print("- Result: PASS")
    print(
        f"  (RS-CH5-GW-001..003 pattern scan; RS-CH5-GW-004 Article count threshold {ARTICLE_REF_THRESHOLD})"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
