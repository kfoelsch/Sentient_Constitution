#!/usr/bin/env python3
"""Audit in-paragraph Markdown links against doc_architecture.md rule 14.

Default (blocking) mode enforces:
  - no Markdown links on ``See`` routing lines;
  - registered section proof cases (required / forbidden in-body links).

``--report`` inventories operative in-paragraph links outside nav blocks.
``--strict-companion`` also fails companion-file links that lack a recognized
interpretive trigger on the same line.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
from dataclasses import dataclass

_TOOLS = pathlib.Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from corpus_paths import binding_corpus_scope

DETAILS_BLOCK = re.compile(r"(?ms)<details>.*?</details>\s*")
INLINE_DEFINITION = re.compile(
    r"<strong><span style=\"color: #2563eb;\">Definition:</span></strong>"
)
MARKDOWN_LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
HEADING = re.compile(r"^(#{1,6})\s+(.+)$")
FOOTER_LINE = re.compile(r"^\*\*(?:Next|Previous) file:\*\*")

COMPANION_PREFIXES = (
    "corpus_joint_structure/",
    "corpus_institutions/",
    "corpus_systems/",
    "corpus_forum/",
)

TRIGGER_PHRASES = (
    "within the meaning of",
    "consistent with",
    "must remain consistent with",
    "must stay consistent with",
    "subject to",
    "implements ",
    "this section applies",
    "this section turns",
    "this subsection applies",
    "this subsection implements",
    "this subsection ties",
    "application baseline",
    "constitutional floor for",
    "constitutional tracing:",
    "under [chapter",
    "governed by [",
    "read through [",
    "scaled to [",
    "bounded by [",
    "evaluated under [",
    "satisfy chapter five [",
    "must satisfy chapter five [",
    "bypass [",
)

PROOFS_PATH = _TOOLS / "in_paragraph_link_proofs.json"


@dataclass(frozen=True)
class Finding:
    file: str
    line: int
    rule: str
    detail: str


@dataclass(frozen=True)
class LinkHit:
    file: str
    line: int
    label: str
    href: str
    line_text: str
    companion: bool
    has_trigger: bool


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=pathlib.Path, default=pathlib.Path("."))
    parser.add_argument(
        "--scope",
        nargs="+",
        default=None,
        help="Markdown paths relative to --root (default: binding corpus scope).",
    )
    parser.add_argument(
        "--report",
        action="store_true",
        help="Print operative in-paragraph link inventory (non-blocking).",
    )
    parser.add_argument(
        "--strict-companion",
        action="store_true",
        help="Fail companion operative links that lack a recognized trigger phrase.",
    )
    parser.add_argument(
        "--proofs",
        type=pathlib.Path,
        default=PROOFS_PATH,
        help="JSON proof-case registry (default: tools/in_paragraph_link_proofs.json).",
    )
    return parser.parse_args()


def load_proofs(path: pathlib.Path) -> list[dict]:
    if not path.is_file():
        raise SystemExit(f"Missing proof registry: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise SystemExit(f"Proof registry must be a JSON list: {path}")
    return data


def is_companion(rel: str) -> bool:
    return rel.startswith(COMPANION_PREFIXES)


def strip_nav_blocks(text: str) -> str:
    text = DETAILS_BLOCK.sub("", text)
    lines = []
    for line in text.splitlines():
        if INLINE_DEFINITION.search(line):
            continue
        lines.append(line)
    return "\n".join(lines)


def is_excluded_operative_line(stripped: str) -> bool:
    if not stripped:
        return True
    if stripped.startswith("#"):
        return True
    if FOOTER_LINE.match(stripped):
        return True
    if stripped.startswith("|"):
        return True
    if stripped == "---" or stripped.startswith("---"):
        return True
    if stripped.startswith("<") and not stripped.startswith("- "):
        return True
    return False


def line_has_trigger(stripped: str) -> bool:
    lower = stripped.lower()
    return any(phrase in lower for phrase in TRIGGER_PHRASES)


def split_sections(text: str) -> list[tuple[str, str, int]]:
    """Return (heading_title, body_text, heading_line_1based)."""
    lines = text.splitlines()
    sections: list[tuple[str, str, int]] = []
    current_title = ""
    current_start = 1
    current_lines: list[str] = []

    def flush(end_line: int) -> None:
        nonlocal current_title, current_lines, current_start
        if current_title or current_lines:
            sections.append(
                (
                    current_title,
                    "\n".join(current_lines),
                    current_start,
                )
            )
        current_lines = []

    for idx, line in enumerate(lines, start=1):
        match = HEADING.match(line)
        if match and len(match.group(1)) <= 4:
            flush(idx - 1)
            current_title = match.group(2).strip()
            current_start = idx
            current_lines = []
            continue
        current_lines.append(line)
    flush(len(lines))
    return sections


def operative_body_text(section_body: str) -> str:
    kept: list[str] = []
    for line in section_body.splitlines():
        stripped = line.strip()
        if stripped.startswith(">"):
            continue
        if is_excluded_operative_line(stripped):
            continue
        kept.append(line)
    return "\n".join(kept)


def section_matches(section_title: str, proof: dict) -> bool:
    if "heading_exact" in proof:
        return section_title == proof["heading_exact"].lstrip("#").strip()
    needle = proof.get("heading_contains")
    if needle:
        return needle.lower() in section_title.lower()
    return False


def body_for_proof(stripped_file: str, proof: dict) -> tuple[str, int] | None:
    anchor = proof.get("text_anchor_contains")
    if anchor:
        idx = stripped_file.find(anchor)
        if idx < 0:
            return None
        start_line = stripped_file.count("\n", 0, idx) + 1
        tail = stripped_file[idx:]
        # Stop at the next role preface or major heading boundary.
        stop = re.search(
            r"(?m)^(?:#{1,4}\s|(?:Constitutional|Local|Delegated|Deposition)\b)",
            tail[len(anchor) :],
        )
        chunk = tail if stop is None else tail[: len(anchor) + stop.start()]
        return operative_body_text(chunk), start_line

    sections = split_sections(stripped_file)
    matched = [s for s in sections if section_matches(s[0], proof)]
    if not matched:
        return None
    return operative_body_text(matched[0][1]), matched[0][2]


def audit_proof_cases(
    rel: str, text: str, proofs: list[dict]
) -> list[Finding]:
    findings: list[Finding] = []
    stripped_file = strip_nav_blocks(text)

    for proof in proofs:
        if proof.get("file") != rel:
            continue
        proof_id = proof.get("id", "<unnamed>")
        located = body_for_proof(stripped_file, proof)
        if located is None:
            findings.append(
                Finding(
                    file=rel,
                    line=1,
                    rule="proof-section-missing",
                    detail=f"{proof_id}: no section matching proof locator.",
                )
            )
            continue

        body, line_hint = located
        for required in proof.get("body_must_contain", []):
            if required not in body:
                findings.append(
                    Finding(
                        file=rel,
                        line=line_hint,
                        rule="proof-required-missing",
                        detail=f"{proof_id}: operative body missing required fragment {required!r}.",
                    )
                )
        for forbidden_href in proof.get("body_must_not_link_href", []):
            for match in MARKDOWN_LINK.finditer(body):
                if forbidden_href in match.group(2):
                    findings.append(
                        Finding(
                            file=rel,
                            line=line_hint,
                            rule="proof-forbidden-link",
                            detail=(
                                f"{proof_id}: operative body must not link "
                                f"{forbidden_href!r} (route via D/E/C or bold text)."
                            ),
                        )
                    )

    return findings


def collect_operative_links(
    rel: str, stripped_text: str, line_offset: int = 0
) -> list[LinkHit]:
    hits: list[LinkHit] = []
    companion = is_companion(rel)
    for i, line in enumerate(stripped_text.splitlines(), start=1):
        stripped = line.strip()
        if is_excluded_operative_line(stripped):
            continue
        if stripped.startswith(">"):
            continue
        if not MARKDOWN_LINK.search(line):
            continue
        trigger = line_has_trigger(stripped)
        for match in MARKDOWN_LINK.finditer(line):
            hits.append(
                LinkHit(
                    file=rel,
                    line=line_offset + i,
                    label=match.group(1),
                    href=match.group(2),
                    line_text=stripped,
                    companion=companion,
                    has_trigger=trigger,
                )
            )
    return hits


def audit_see_line_links(rel: str, stripped_text: str) -> list[Finding]:
    findings: list[Finding] = []
    for i, line in enumerate(stripped_text.splitlines(), start=1):
        stripped = line.strip()
        if not stripped.lower().startswith("see "):
            continue
        if MARKDOWN_LINK.search(stripped):
            findings.append(
                Finding(
                    file=rel,
                    line=i,
                    rule="see-line-link",
                    detail="See routing lines must use bold stable IDs, not Markdown links (rule 14).",
                )
            )
    return findings


def audit_strict_companion(hits: list[LinkHit]) -> list[Finding]:
    findings: list[Finding] = []
    for hit in hits:
        if not hit.companion:
            continue
        if hit.has_trigger:
            continue
        if hit.href.startswith("#"):
            continue
        findings.append(
            Finding(
                file=hit.file,
                line=hit.line,
                rule="companion-untriggered-link",
                detail=(
                    f"Companion operative link [{hit.label}]({hit.href}) lacks a "
                    "recognized interpretive trigger on the same line (rule 14)."
                ),
            )
        )
    return findings


def audit_file(
    rel: str,
    path: pathlib.Path,
    proofs: list[dict],
    *,
    strict_companion: bool,
) -> tuple[list[Finding], list[LinkHit]]:
    text = path.read_text(encoding="utf-8")
    stripped = strip_nav_blocks(text)
    findings: list[Finding] = []
    findings.extend(audit_see_line_links(rel, stripped))
    findings.extend(audit_proof_cases(rel, text, proofs))

    hits = collect_operative_links(rel, stripped)
    if strict_companion:
        findings.extend(audit_strict_companion(hits))
    return findings, hits


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    proofs = load_proofs(args.proofs.resolve())
    scope = args.scope or binding_corpus_scope(root)

    all_findings: list[Finding] = []
    all_hits: list[LinkHit] = []

    for rel in scope:
        path = root / rel
        if not path.is_file():
            continue
        findings, hits = audit_file(
            rel,
            path,
            proofs,
            strict_companion=args.strict_companion,
        )
        all_findings.extend(findings)
        all_hits.extend(hits)

    if args.report:
        print("file\tline\tcompanion\ttrigger\tlabel\thref")
        for hit in sorted(all_hits, key=lambda h: (h.file, h.line, h.href)):
            print(
                f"{hit.file}\t{hit.line}\t{int(hit.companion)}\t"
                f"{int(hit.has_trigger)}\t{hit.label}\t{hit.href}"
            )
        print(f"\nTotal operative in-paragraph links: {len(all_hits)}")
        if all_findings:
            print(f"Findings: {len(all_findings)}", file=sys.stderr)

    if all_findings:
        print("In-paragraph link audit failures:", file=sys.stderr)
        for item in all_findings:
            print(f"  - {item.file}:{item.line} [{item.rule}] {item.detail}", file=sys.stderr)
        print(f"Total: {len(all_findings)}", file=sys.stderr)
        return 1

    mode = "report-only PASS" if args.report else "PASS"
    print(
        f"In-paragraph link audit {mode} "
        f"({len(all_hits)} operative links inventoried)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
