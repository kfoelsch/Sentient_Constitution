#!/usr/bin/env python3
"""Build an AI-only translation resync queue and passage review packet.

The tool reports English-source drift by locale, extracts changed English
sections and corresponding translated passages where stable anchors permit,
and adds mechanical structure/link/glossary advisories. It never edits the
translation review manifest or records a human review.
"""

from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import translation_audit as audit  # noqa: E402
import local_markdown_fragment_audit as markdown_links  # noqa: E402

MANIFEST = ROOT / "translations" / "review_status.json"
ANCHOR_RE = re.compile(r"<a\b[^>]*\bid\s*=\s*['\"]([^'\"]+)['\"]", re.I)
HEADING_RE = re.compile(r"^\s{0,3}(#{1,6})\s+(.+?)\s*#*\s*$")
_VALID_REFS: dict[str, bool] = {}
_COMMIT_TIMES: dict[str, int] = {}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_text(revision: str, relpath: str) -> str | None:
    try:
        return subprocess.check_output(
            ["git", "show", f"{revision}:{relpath}"], cwd=ROOT, text=True,
            encoding="utf-8", stderr=subprocess.DEVNULL,
        )
    except (OSError, subprocess.CalledProcessError):
        return None


def valid_revision(revision: str | None) -> bool:
    if not revision:
        return False
    if revision in _VALID_REFS:
        return _VALID_REFS[revision]
    result = subprocess.run(
        ["git", "cat-file", "-e", f"{revision}^{{commit}}"],
        cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    ).returncode == 0
    _VALID_REFS[revision] = result
    return result


def baseline_for(source: str, rows: list[dict], requested: str | None) -> tuple[str | None, str]:
    if requested:
        if not valid_revision(requested):
            raise ValueError(f"Not a valid Git commit/ref: {requested}")
        return requested, "requested baseline"
    revisions = Counter(
        row.get("source_revision") for row in rows
        if row.get("source_file") == source and valid_revision(row.get("source_revision"))
    )
    if revisions:
        # Use the most common recorded source snapshot; break ties by oldest
        # commit so updates since the last inventory are not silently skipped.
        choices = sorted(revisions, key=lambda rev: (-revisions[rev], commit_time(rev)))
        return choices[0], "recorded translation snapshot"
    return ("HEAD", "HEAD fallback") if valid_revision("HEAD") else (None, "no Git baseline")


def commit_time(revision: str) -> int:
    if revision in _COMMIT_TIMES:
        return _COMMIT_TIMES[revision]
    try:
        result = int(subprocess.check_output(
            ["git", "show", "-s", "--format=%ct", revision], cwd=ROOT, text=True,
        ).strip())
    except (OSError, subprocess.CalledProcessError, ValueError):
        result = 0
    _COMMIT_TIMES[revision] = result
    return result


def changed_spans(before: str, after: str) -> list[tuple[int, int, list[str]]]:
    old, new = before.splitlines(), after.splitlines()
    matcher = difflib.SequenceMatcher(a=old, b=new)
    spans: list[tuple[int, int, list[str]]] = []
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            continue
        old_lo, old_hi = max(0, i1 - 4), min(len(old), i2 + 4)
        new_lo, new_hi = max(0, j1 - 4), min(len(new), max(j2, j1 + 1) + 4)
        diff = list(difflib.unified_diff(
            old[old_lo:old_hi], new[new_lo:new_hi],
            fromfile="English baseline", tofile="Current English", n=3,
        ))
        spans.append((new_lo, new_hi, diff))
    return spans


def section_for_line(lines: list[str], line_no: int) -> tuple[str, str, int, int]:
    headings: list[tuple[int, int, str]] = []
    anchor = ""
    for i, line in enumerate(lines[:line_no + 1]):
        found = ANCHOR_RE.search(line)
        if found:
            anchor = found.group(1)
        heading = HEADING_RE.match(line)
        if heading:
            headings.append((i, len(heading.group(1)), heading.group(2)))
    active = headings[-1] if headings else (0, 1, "(file introduction)")
    end = len(lines)
    for i in range(active[0] + 1, len(lines)):
        heading = HEADING_RE.match(lines[i])
        if heading and len(heading.group(1)) <= active[1]:
            end = i
            break
    label = f"{anchor} · " if anchor else ""
    return f"{label}{active[2]}", anchor, active[0], end


@dataclass
class Passage:
    label: str
    start: int
    end: int
    source_excerpt: str
    anchors: list[str]


def passages(before: str, current: str) -> list[Passage]:
    current_lines = current.splitlines()
    spans = changed_spans(before, current)
    gathered: dict[tuple[str, int, int], Passage] = {}
    for lo, hi, excerpt in spans:
        label, nearest_anchor, start, end = section_for_line(current_lines, lo)
        key = (label, start, end)
        anchors = [nearest_anchor] if nearest_anchor else []
        passage = gathered.get(key)
        if passage:
            passage.source_excerpt += "\n…\n" + "\n".join(excerpt)
        else:
            gathered[key] = Passage(
                label, start, end, "\n".join(excerpt), anchors,
            )
    return sorted(gathered.values(), key=lambda p: p.start)


def target_excerpt(path: Path, anchors: list[str]) -> tuple[str, str]:
    if not path.is_file():
        return "missing", ""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not anchors:
        return "no stable source anchor in changed section", ""
    for anchor in anchors:
        matches = [i for i, line in enumerate(lines) if re.search(
            rf"<a\b[^>]*\bid\s*=\s*['\"]{re.escape(anchor)}['\"]", line, re.I
        )]
        if not matches:
            continue
        start = matches[0]
        end = len(lines)
        for i in range(start + 1, len(lines)):
            if ANCHOR_RE.search(lines[i]):
                end = i
                break
        return f"matched anchor `{anchor}`", "\n".join(lines[start:end]).strip()
    return "target anchor missing", ""


def glossary_hits(locale_dir: Path, source_excerpt: str, target_excerpt_text: str) -> list[str]:
    flags = []
    for source_term, local_term in audit.read_glossary(locale_dir):
        if not any(audit.occurrences(source_excerpt, variant) for variant in audit.variants(source_term)):
            continue
        if not any(audit.occurrences(target_excerpt_text, variant) for variant in audit.variants(local_term)):
            flags.append(f"{source_term} → {local_term}")
    return flags


def file_mechanics(source_path: Path, target_path: Path) -> dict[str, object]:
    source_text = source_path.read_text(encoding="utf-8")
    target_text = target_path.read_text(encoding="utf-8")
    src_ids = ANCHOR_RE.findall(source_text)
    dst_ids = ANCHOR_RE.findall(target_text)
    missing_order = not audit.sub_sequence(src_ids, dst_ids)
    src_marks, dst_marks = audit.marker_counts(source_text), audit.marker_counts(target_text)
    marker_diffs = [key for key in (
        "heading_levels", "lists", "tables", "details_open", "details_close", "fences"
    ) if src_marks[key] != dst_marks[key]]
    link_findings = []
    source_name = target_path.relative_to(ROOT).as_posix()
    for link in markdown_links.links_in(target_path, target_text):
        parsed = urlsplit(link.raw_target)
        if parsed.scheme or parsed.netloc or link.raw_target.startswith("//"):
            continue
        rel = unquote(parsed.path)
        fragment = unquote(parsed.fragment) if parsed.fragment else None
        target = (target_path if not rel else target_path.parent / rel).resolve()
        try:
            target.relative_to(ROOT)
        except ValueError:
            link_findings.append(f"{source_name}:{link.line} unsafe target {link.raw_target}")
            continue
        if not target.is_file():
            link_findings.append(f"{source_name}:{link.line} missing file {link.raw_target}")
        elif fragment and target.suffix.lower() == ".md":
            anchors = markdown_links.anchor_info(target.read_text(encoding="utf-8"))[0]
            if fragment not in anchors:
                link_findings.append(f"{source_name}:{link.line} missing fragment {link.raw_target}")
    return {
        "source_ids_missing_or_reordered": missing_order,
        "marker_count_differences": marker_diffs,
        "unbalanced_details": dst_marks["details_open"] != dst_marks["details_close"],
        "unbalanced_fences": int(dst_marks["fences"]) % 2 != 0,
        "unresolved_links": link_findings,
    }


def build_report(requested_base: str | None) -> str:
    if not MANIFEST.is_file():
        raise ValueError(f"Missing drift manifest: {MANIFEST}")
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    records = manifest.get("files", [])
    records_by_source: dict[str, list[dict]] = defaultdict(list)
    records_by_target: dict[tuple[str, str], dict] = {}
    for row in records:
        records_by_source[row.get("source_file", "")].append(row)
        records_by_target[(row.get("locale", ""), row.get("translation_file", ""))] = row

    locales = audit.locale_dirs()
    maps = {directory.name: audit.readme_source_map(directory) for directory in locales}
    source_targets: dict[str, dict[str, str]] = defaultdict(dict)
    all_sources: set[str] = set()
    for locale, mapping in maps.items():
        for local_name, source in mapping.items():
            source_targets[source][locale] = f"translations/{locale}/{local_name}"
            all_sources.add(source)

    source_work = []
    for source in sorted(all_sources):
        source_path = ROOT / source
        if not source_path.is_file():
            continue
        current_hash = sha256(source_path)
        source_rows = records_by_source.get(source, [])
        stale = not source_rows or any(
            row.get("source_sha256") != current_hash for row in source_rows
        )
        baseline, baseline_kind = baseline_for(source, source_rows, requested_base)
        before = git_text(baseline, source) if baseline else None
        current = source_path.read_text(encoding="utf-8")
        changed = before is not None and before != current
        if not stale and not changed:
            continue
        sections = passages(before or "", current) if changed and before is not None else []
        source_work.append({
            "source": source,
            "source_hash": current_hash,
            "baseline": baseline,
            "baseline_kind": baseline_kind,
            "stale": stale,
            "changed": changed,
            "sections": sections,
            "targets": source_targets[source],
        })

    out = [
        "# Pre-announcement translation resync packet",
        "",
        f"**Status:** AI-assisted work queue and mechanical review aid; not a translation certification.",
        f"**Baseline:** `{requested_base}` when specified; otherwise the most common/oldest valid recorded source revision per file.",
        "**Review manifest:** read-only. This command never changes reviewer, reviewed_at, or review hashes.",
        "",
        "## Queue summary",
        "",
        "| English source | Current SHA-256 | Changed sections | Stale locale snapshots | Missing locale files |",
        "|---|---|---:|---:|---:|",
    ]
    for item in source_work:
        stale_locales = []
        missing = []
        for locale in sorted(maps):
            target = item["targets"].get(locale)
            if not target or not (ROOT / target).is_file():
                missing.append(locale)
                continue
            row = records_by_target.get((locale, target))
            if not row or row.get("source_sha256") != item["source_hash"]:
                stale_locales.append(locale)
        out.append(
            f"| `{item['source']}` | `{item['source_hash']}` | {len(item['sections'])} | "
            f"{', '.join(stale_locales) or '—'} | {', '.join(missing) or '—'} |"
        )

    out += ["", "## Passage packets", ""]
    mechanics_cache: dict[str, dict[str, object]] = {}
    if not source_work:
        out += ["No mapped English sources differ from their recorded snapshots.", ""]
    for item in source_work:
        out += [f"### `{item['source']}`", "", f"- Baseline: `{item['baseline'] or 'unavailable'}` ({item['baseline_kind']})",
                f"- Current source SHA-256: `{item['source_hash']}`"]
        if not item["changed"]:
            out += ["- The manifest marks translations stale, but the English baseline content is unavailable; select a Git baseline with `--base` to generate passage diffs.", ""]
            continue
        if not item["sections"]:
            out += ["- No section-level diff was extracted; check the baseline and source file manually.", ""]
            continue
        for number, passage in enumerate(item["sections"], 1):
            out += [f"#### Passage {number}: {passage.label}", "", "**English source diff (including removed text):**", "", "```diff", passage.source_excerpt[:12000], "```", ""]
            for locale in sorted(maps):
                target_rel = item["targets"].get(locale)
                if not target_rel or not (ROOT / target_rel).is_file():
                    out += [f"**{locale}:** translation file missing.", ""]
                    continue
                target_path = ROOT / target_rel
                status, target_text = target_excerpt(target_path, passage.anchors)
                record = records_by_target.get((locale, target_rel))
                source_current = bool(record and record.get("source_sha256") == item["source_hash"])
                translation_changed = bool(record and record.get("translation_sha256") != sha256(target_path))
                out += [f"**{locale} — {target_rel}** ({status}; source snapshot {'current' if source_current else 'stale/untracked'}; translation file {'changed since inventory' if translation_changed else 'matches inventory'}).", ""]
                if target_text:
                    out += ["```markdown", target_text[:8000], "```", ""]
                else:
                    out += ["No target passage could be aligned by a source HTML anchor. Locate it by the English section label and review the whole target file as needed.", ""]
                flags = glossary_hits(locales[[d.name for d in locales].index(locale)], passage.source_excerpt, target_text)
                if flags:
                    out += ["Glossary surface-form advisories (may be inflection or intentional retention): " + "; ".join(flags), ""]
                if target_rel not in mechanics_cache:
                    mechanics_cache[target_rel] = file_mechanics(ROOT / item["source"], target_path)
                mechanics = mechanics_cache[target_rel]
                findings = []
                if mechanics["source_ids_missing_or_reordered"]: findings.append("source anchors missing/reordered")
                if mechanics["marker_count_differences"]: findings.append("whole-file structure differs: " + ", ".join(mechanics["marker_count_differences"]))
                if mechanics["unbalanced_details"]: findings.append("unbalanced details block")
                if mechanics["unbalanced_fences"]: findings.append("unbalanced code fence")
                if mechanics["unresolved_links"]: findings.append(f"{len(mechanics['unresolved_links'])} unresolved links in target file")
                out.append("Mechanical checks: " + ("; ".join(findings) if findings else "no findings in the checked categories") + ".")
                out.append("")
        out += ["**AI drafter prompt:** Translate or revise only the passages above using the locale glossary and existing target terminology. Preserve actors, scope, conditions, exceptions, negation, thresholds, duties, permissions, and certainty. Keep anchors and links intact. Label all output unreviewed.", "",
                "**Independent AI-check prompt:** Compare the target passages against English clause by clause. Report omissions, additions, actor/scope shifts, condition or exception shifts, negation changes, duty/permission strength changes, threshold/certainty shifts, terminology inconsistency, unnatural or mixed-language text, and unresolved links. Do not mark any human-review status.", ""]
    out += [
        "## Limits",
        "",
        "- Glossary and structure findings are mechanical/advisory; exact term forms may inflect or be intentionally retained in English.",
        "- Link checks scan each affected target file, so they may include pre-existing findings outside the changed passage.",
        "- Stable HTML anchors are used to align target excerpts. Where a target anchor is absent, the packet says so rather than guessing by translated heading text.",
        "- AI prompts prepare draft and cross-check work; they do not establish fluency, legal equivalence, or independent human review.",
        "- English controls. Review attestations remain untouched.",
        "",
    ]
    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", help="Git commit/ref to compare. Default uses recorded source revisions.")
    parser.add_argument("--output", type=Path, help="Write the packet to this path; default prints to stdout.")
    args = parser.parse_args()
    try:
        report = build_report(args.base)
        if args.output:
            path = args.output if args.output.is_absolute() else ROOT / args.output
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(report, encoding="utf-8")
            try:
                display_path = path.relative_to(ROOT)
            except ValueError:
                display_path = path
            print(f"Wrote AI-only resync packet to {display_path}")
        else:
            print(report, end="")
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"Translation pre-announcement check failed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
