#!/usr/bin/env python3
"""Block house jargon in easy-entry reader briefs.

Scoped to ``implementation/adoption/easy_entry/``. Terms live in
``easy_entry_jargon`` inside ``tools/architecture/lexical_guardrails.json``.
Does not bind ``core_*``. Official names may appear inside markdown links.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "tools" / "architecture" / "lexical_guardrails.json"
DEFAULT_SCOPE = Path("implementation/adoption/easy_entry")

LINK_RE = re.compile(r"\[[^\]]*\]\([^)]+\)")
CODE_SPAN_RE = re.compile(r"`[^`]+`")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
OBJECTION_PREFIX_RE = re.compile(r"^(?:-\s+)?\*\*[“\"].*?[”\"]\*\*\s*")
ALLOW_PHRASE_DEFAULT = ("Sentient Constitution", "Rights Floor")


@dataclass(frozen=True)
class JargonTerm:
    avoid: str
    pattern: re.Pattern[str]
    prefer: str


@dataclass(frozen=True)
class Finding:
    path: str
    line: int
    avoid: str
    snippet: str
    prefer: str


def load_jargon_config(config_path: Path = CONFIG_PATH) -> tuple[tuple[str, ...], tuple[JargonTerm, ...]]:
    data = json.loads(config_path.read_text(encoding="utf-8"))
    block = data.get("easy_entry_jargon")
    if not isinstance(block, dict):
        raise SystemExit("lexical_guardrails.json missing easy_entry_jargon object")
    allow = tuple(str(item) for item in block.get("allow_phrases", ALLOW_PHRASE_DEFAULT))
    terms: list[JargonTerm] = []
    raw_terms = block.get("terms", [])
    if not isinstance(raw_terms, list) or not raw_terms:
        raise SystemExit("easy_entry_jargon.terms must be a non-empty list")
    for item in raw_terms:
        if not isinstance(item, dict):
            continue
        avoid = str(item["avoid"]).strip()
        prefer = str(item.get("prefer", "")).strip()
        raw_pattern = item.get("pattern")
        if raw_pattern:
            pattern = re.compile(str(raw_pattern), re.IGNORECASE)
        else:
            pattern = re.compile(r"\b" + re.escape(avoid) + r"\b", re.IGNORECASE)
        terms.append(JargonTerm(avoid=avoid, pattern=pattern, prefer=prefer))
    terms.sort(key=lambda term: len(term.avoid), reverse=True)
    return allow, tuple(terms)


def iter_scope_files(root: Path, scope: Path) -> list[Path]:
    folder = root / scope
    if not folder.is_dir():
        raise SystemExit(f"Missing easy-entry folder: {folder}")
    return sorted(path for path in folder.glob("*.md") if path.is_file())


def _strip_allow_phrases(text: str, allow_phrases: tuple[str, ...]) -> str:
    cleaned = text
    for phrase in allow_phrases:
        cleaned = re.sub(re.escape(phrase), "", cleaned, flags=re.IGNORECASE)
    return cleaned


def visible_scan_text(line: str, allow_phrases: tuple[str, ...]) -> str:
    """Reader-visible remainder of a line after links, ticks, and allowlisted names."""
    working = LINK_RE.sub("", line)
    working = CODE_SPAN_RE.sub("", working)
    working = re.sub(r"<[^>]+>", "", working)
    return _strip_allow_phrases(working, allow_phrases)


def iter_scan_lines(text: str, allow_phrases: tuple[str, ...]) -> list[tuple[int, str]]:
    """Yield (line_no, visible_text) for lines the jargon gate inspects."""
    results: list[tuple[int, str]] = []
    in_fence = False
    in_comment = False
    details_depth = 0
    skip_section_level: int | None = None

    for line_no, raw in enumerate(text.splitlines(), start=1):
        stripped = raw.strip()

        if in_comment:
            if "-->" in raw:
                in_comment = False
            continue
        if "<!--" in raw:
            if "-->" not in raw.split("<!--", 1)[1]:
                in_comment = True
            continue

        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        lower = stripped.lower()
        if "<details" in lower:
            details_depth += 1
        if details_depth:
            if "</details>" in lower:
                details_depth -= 1
            continue

        heading = HEADING_RE.match(stripped)
        if heading:
            level = len(heading.group(1))
            title = heading.group(2).strip().lower()
            if skip_section_level is not None and level <= skip_section_level:
                skip_section_level = None
            if title.startswith("do not use"):
                skip_section_level = level
                continue
        if skip_section_level is not None:
            continue

        objection_prefix = OBJECTION_PREFIX_RE.match(stripped)
        if objection_prefix:
            remainder = stripped[objection_prefix.end() :]
            if not remainder:
                continue
            visible = visible_scan_text(remainder, allow_phrases)
        else:
            visible = visible_scan_text(raw, allow_phrases)
        if visible.strip():
            results.append((line_no, visible))
    return results


def audit_text(
    text: str,
    *,
    rel_path: str,
    terms: tuple[JargonTerm, ...],
    allow_phrases: tuple[str, ...],
) -> list[Finding]:
    findings: list[Finding] = []
    for line_no, visible in iter_scan_lines(text, allow_phrases):
        for term in terms:
            match = term.pattern.search(visible)
            if not match:
                continue
            snippet = visible.strip()
            if len(snippet) > 160:
                snippet = snippet[:157] + "..."
            findings.append(
                Finding(
                    path=rel_path,
                    line=line_no,
                    avoid=term.avoid,
                    snippet=snippet,
                    prefer=term.prefer,
                )
            )
            break
    return findings


def audit_files(
    root: Path,
    *,
    scope: Path = DEFAULT_SCOPE,
    config_path: Path = CONFIG_PATH,
) -> list[Finding]:
    allow_phrases, terms = load_jargon_config(config_path)
    findings: list[Finding] = []
    for path in iter_scope_files(root, scope):
        rel = path.relative_to(root).as_posix()
        findings.extend(
            audit_text(
                path.read_text(encoding="utf-8"),
                rel_path=rel,
                terms=terms,
                allow_phrases=allow_phrases,
            )
        )
    return findings


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Repository root.")
    parser.add_argument(
        "--scope",
        default=str(DEFAULT_SCOPE),
        help="Folder of easy-entry markdown to scan.",
    )
    parser.add_argument(
        "--config",
        default=str(CONFIG_PATH),
        help="lexical_guardrails.json path.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    findings = audit_files(
        root,
        scope=Path(args.scope),
        config_path=Path(args.config),
    )
    if not findings:
        print("easy-entry jargon audit: clean")
        return 0
    print(f"easy-entry jargon audit: {len(findings)} hit(s)")
    for item in findings:
        prefer = f" → {item.prefer}" if item.prefer else ""
        print(f"{item.path}:{item.line}: do not use `{item.avoid}`{prefer}")
        print(f"  {item.snippet}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
