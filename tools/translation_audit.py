#!/usr/bin/env python3
"""Audit translation freshness, structure, links, glossary use, and review status.

This tool checks reader-language Markdown against the canonical English sources
listed in each locale's README file table. Structural and glossary findings are
review aids; they do not judge semantic translation quality.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = ROOT / "translations" / "review_status.json"
LOCALE_RE = re.compile(r"^[a-z]{2,3}$")
README_MAP_RE = re.compile(
    r"^\|\s*\[([^\]]+\.md)\]\(([^)]+)\)\s*\|\s*"
    r"\[[^\]]+\]\(([^)]+)\)\s*\|\s*$",
    re.MULTILINE,
)
ANCHOR_RE = re.compile(r"<a\b[^>]*\bid\s*=\s*['\"]([^'\"]+)['\"]", re.I)
HEADING_RE = re.compile(r"^\s{0,3}(#{1,6})\s+", re.MULTILINE)
FENCE_RE = re.compile(r"^\s{0,3}(`{3,}|~{3,})", re.MULTILINE)
LIST_RE = re.compile(r"^\s*(?:[-+*]|\d+[.)])\s+", re.MULTILINE)
TABLE_ROW_RE = re.compile(r"^\s*\|.*\|\s*$", re.MULTILINE)


@dataclass(frozen=True)
class Pair:
    locale: str
    translation: str
    source: str


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_revision() -> str | None:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return None


def locale_dirs(locale: str | None = None) -> list[Path]:
    dirs = [
        path for path in (ROOT / "translations").iterdir()
        if path.is_dir() and (path / "README.md").is_file()
        and LOCALE_RE.fullmatch(path.name)
    ]
    if locale:
        dirs = [path for path in dirs if path.name == locale]
        if not dirs:
            raise ValueError(f"Unknown translation locale: {locale}")
    return sorted(dirs)


def readme_source_map(locale_dir: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    for local_name, _local_href, source_href in README_MAP_RE.findall(
        (locale_dir / "README.md").read_text(encoding="utf-8")
    ):
        source_part = source_href.split("#", 1)[0]
        source_path = (locale_dir / source_part).resolve()
        try:
            rel = source_path.relative_to(ROOT).as_posix()
        except ValueError:
            continue
        if source_path.is_file():
            result[local_name] = rel
    return result


def all_source_mappings() -> dict[str, str]:
    mappings: dict[str, set[str]] = defaultdict(set)
    for directory in locale_dirs():
        for local_name, source in readme_source_map(directory).items():
            mappings[local_name].add(source)
    conflicts = {name: sorted(sources) for name, sources in mappings.items() if len(sources) > 1}
    if conflicts:
        detail = "; ".join(f"{name}: {sources}" for name, sources in conflicts.items())
        raise ValueError(f"Locale README tables disagree about source files: {detail}")
    return {name: next(iter(sources)) for name, sources in mappings.items()}


def translation_pairs(locale: str | None = None) -> tuple[list[Pair], list[str]]:
    global_map = all_source_mappings()
    pairs: list[Pair] = []
    unmapped: list[str] = []
    for directory in locale_dirs(locale):
        local_map = readme_source_map(directory)
        for path in sorted(directory.glob("*.md")):
            if path.name == "README.md":
                continue
            source = local_map.get(path.name) or global_map.get(path.name)
            if source is None and (ROOT / path.name).is_file():
                source = path.name
            if source is None or not (ROOT / source).is_file():
                unmapped.append(path.relative_to(ROOT).as_posix())
                continue
            pairs.append(Pair(directory.name, path.relative_to(ROOT).as_posix(), source))
    return pairs, unmapped


def sub_sequence(needle: list[str], haystack: list[str]) -> bool:
    position = 0
    for item in haystack:
        if position < len(needle) and item == needle[position]:
            position += 1
    return position == len(needle)


def marker_counts(text: str) -> dict[str, object]:
    return {
        "heading_levels": dict(sorted(Counter(len(x) for x in HEADING_RE.findall(text)).items())),
        "lists": len(LIST_RE.findall(text)),
        "tables": len(TABLE_ROW_RE.findall(text)),
        "details_open": text.count("<details>"),
        "details_close": text.count("</details>"),
        "fences": len(FENCE_RE.findall(text)),
    }


def structure_audit(locale: str | None = None, verbose: bool = False) -> tuple[int, list[str]]:
    pairs, unmapped = translation_pairs(locale)
    problems: list[str] = []
    counts: Counter[str] = Counter()
    examples: dict[str, list[str]] = defaultdict(list)
    for item in pairs:
        translated = (ROOT / item.translation).read_text(encoding="utf-8")
        source = (ROOT / item.source).read_text(encoding="utf-8")
        source_ids = ANCHOR_RE.findall(source)
        translated_ids = ANCHOR_RE.findall(translated)
        if not sub_sequence(source_ids, translated_ids):
            counts["source_ids_missing_or_reordered"] += 1
            examples["source_ids_missing_or_reordered"].append(item.translation)
            problems.append(f"{item.translation}: source HTML ids missing or reordered")
        src = marker_counts(source)
        dst = marker_counts(translated)
        for key in ("heading_levels", "lists", "tables", "details_open", "details_close", "fences"):
            if src[key] != dst[key]:
                counts[f"{key}_differences"] += 1
                examples[f"{key}_differences"].append(
                    f"{item.translation} (source={src[key]}, translation={dst[key]})"
                )
                problems.append(
                    f"{item.translation}: {key} differs (source={src[key]}, translation={dst[key]})"
                )
        if dst["details_open"] != dst["details_close"]:
            counts["unbalanced_details"] += 1
            examples["unbalanced_details"].append(item.translation)
            problems.append(f"{item.translation}: unbalanced <details> blocks")
        if int(dst["fences"]) % 2:
            counts["unbalanced_fences"] += 1
            examples["unbalanced_fences"].append(item.translation)
            problems.append(f"{item.translation}: unbalanced fenced code blocks")
    for name in unmapped:
        counts["unmapped_files"] += 1
        examples["unmapped_files"].append(name)
        problems.append(f"{name}: no English source mapping")
    print(
        f"Structure: {len(pairs)} translated files; "
        f"source-ID issues={counts['source_ids_missing_or_reordered']}; "
        f"marker-count differences={sum(v for k, v in counts.items() if k.endswith('_differences'))}; "
        f"unbalanced details={counts['unbalanced_details']}; "
        f"unbalanced fences={counts['unbalanced_fences']}; unmapped={counts['unmapped_files']}."
    )
    for kind, items in examples.items():
        for example in items if verbose else items[:3]:
            print(f"  REVIEW {kind}: {example}")
        if not verbose and len(items) > 3:
            print(f"  ... {len(items) - 3} additional {kind} findings")
    # Marker-count differences are review findings, while missing IDs and
    # unbalanced containers are blocking integrity failures.
    blocking = any(
        "source HTML ids missing" in problem
        or "unbalanced" in problem
        or "no English source mapping" in problem
        for problem in problems
    )
    return (1 if blocking else 0), problems


def link_audit(locale: str | None = None, verbose: bool = False) -> int:
    pairs, _ = translation_pairs(locale)
    # Reuse the corpus link parser and heading/HTML-anchor resolver, but omit
    # its editor-preview style warning. Translation pilots deliberately retain
    # English custom IDs while translating the headings beneath them.
    sys.path.insert(0, str(ROOT / "tools"))
    import local_markdown_fragment_audit as markdown_links

    paths = [ROOT / item.translation for item in pairs]
    paths.extend(directory / "README.md" for directory in locale_dirs(locale))
    anchor_cache: dict[Path, set[str]] = {}
    findings: list[tuple[str, int, str, str]] = []
    for source_path in paths:
        text = source_path.read_text(encoding="utf-8")
        for link in markdown_links.links_in(source_path, text):
            parsed = urlsplit(link.raw_target)
            if parsed.scheme or parsed.netloc or link.raw_target.startswith("//"):
                continue
            relpath = unquote(parsed.path)
            fragment = unquote(parsed.fragment) if parsed.fragment else None
            target = (source_path if not relpath else source_path.parent / relpath).resolve()
            try:
                target.relative_to(ROOT)
            except ValueError:
                findings.append((source_path.relative_to(ROOT).as_posix(), link.line, "unsafe-target", link.raw_target))
                continue
            if not target.is_file():
                findings.append((source_path.relative_to(ROOT).as_posix(), link.line, "missing-file", link.raw_target))
                continue
            if fragment and target.suffix.lower() == ".md":
                if target not in anchor_cache:
                    anchor_cache[target] = markdown_links.anchor_info(
                        target.read_text(encoding="utf-8")
                    )[0]
                if fragment not in anchor_cache[target]:
                    findings.append((source_path.relative_to(ROOT).as_posix(), link.line, "missing-fragment", link.raw_target))

    counts = Counter(row[2] for row in findings)
    print(
        f"Links: {len(paths)} translated/README files scanned; "
        f"{len(findings)} unresolved or unsafe targets. "
        + ", ".join(f"{kind}={counts[kind]}" for kind in ("missing-file", "missing-fragment", "unsafe-target") if counts[kind])
    )
    locale_counts: dict[str, Counter[str]] = defaultdict(Counter)
    for source, _line, kind, _target in findings:
        locale_name = Path(source).parts[1] if len(Path(source).parts) > 1 else "?"
        locale_counts[locale_name][kind] += 1
    for locale_name, by_kind in sorted(locale_counts.items()):
        summary = ", ".join(f"{kind}={by_kind[kind]}" for kind in ("missing-file", "missing-fragment", "unsafe-target") if by_kind[kind])
        print(f"  {locale_name}: {summary}")
    if verbose:
        selected = findings[:100]
        for source, line, kind, target in selected:
            print(f"  {source}:{line} {kind}: {target}")
        if len(findings) > 100:
            print(f"  ... {len(findings) - 100} additional link findings")
    else:
        seen: set[tuple[str, str]] = set()
        for source, line, kind, target in findings:
            locale_name = Path(source).parts[1] if len(Path(source).parts) > 1 else "?"
            key = (locale_name, kind)
            if key in seen:
                continue
            seen.add(key)
            print(f"  SAMPLE {locale_name}: {source}:{line} {kind}: {target}")
            if len(seen) >= 20:
                break
    return 1 if findings else 0


def read_glossary(locale_dir: Path) -> list[tuple[str, str]]:
    lines = (locale_dir / "README.md").read_text(encoding="utf-8").splitlines()
    headings = [i for i, line in enumerate(lines) if line.startswith("## ")]
    if not headings:
        return []
    section = lines[headings[-1] + 1:]
    rows: list[tuple[str, str]] = []
    table_started = False
    for line in section:
        if not line.lstrip().startswith("|"):
            if table_started:
                break
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 2:
            continue
        if not table_started:
            table_started = True  # header row
            continue
        if all(set(cell) <= set("-: ") for cell in cells):
            continue
        left, right = cells[0], cells[1]
        left = re.sub(r"[*_`]", "", left).strip()
        right = re.sub(r"[*_`]", "", right).strip()
        if left and right:
            rows.append((left, right))
    return rows


def variants(term: str) -> list[str]:
    return [
        value.strip().strip("*_`")
        for value in re.split(r"\s*/\s*|\s*[·•]\s*", term)
        if value.strip()
    ]


def occurrences(text: str, term: str) -> int:
    if len(term) < 3:
        return text.casefold().count(term.casefold())
    return len(re.findall(re.escape(term), text, re.IGNORECASE))


def terminology_audit(locale: str | None = None, verbose: bool = False) -> int:
    pairs, _ = translation_pairs(locale)
    by_locale: dict[str, list[Pair]] = defaultdict(list)
    for pair in pairs:
        by_locale[pair.locale].append(pair)
    total_checks = 0
    potential = 0
    for directory in locale_dirs(locale):
        terms = read_glossary(directory)
        local_pairs = by_locale[directory.name]
        source_text = "\n".join((ROOT / pair.source).read_text(encoding="utf-8") for pair in local_pairs)
        translated_text = "\n".join((ROOT / pair.translation).read_text(encoding="utf-8") for pair in local_pairs)
        review_items: list[str] = []
        found = 0
        for source_term, local_term in terms:
            source_hits = sum(occurrences(source_text, v) for v in variants(source_term))
            local_hits = sum(occurrences(translated_text, v) for v in variants(local_term))
            total_checks += 1
            if local_hits:
                found += 1
            elif source_hits:
                potential += 1
                review_items.append(
                    f"{source_term} → {local_term} (source term occurs {source_hits} times; "
                    "check inflection, alternate wording, or intentional English retention)"
                )
        print(
            f"Terminology {directory.name}: {len(terms)} glossary rows; "
            f"{found} exact local forms found; {len(review_items)} surface-form review flags."
        )
        if verbose:
            for item in review_items:
                print(f"  REVIEW {item}")
    print(
        f"Terminology summary: {total_checks} glossary rows scanned; "
        f"{potential} advisory surface-form flags. This is not a semantic translation check."
    )
    return 0


def manifest_inventory() -> list[dict[str, object]]:
    pairs, unmapped = translation_pairs()
    if unmapped:
        raise ValueError("Cannot initialize review manifest; unmapped translation files: " + ", ".join(unmapped))
    revision = git_revision()
    rows = []
    for item in pairs:
        translation_path = ROOT / item.translation
        source_path = ROOT / item.source
        rows.append({
            "locale": item.locale,
            "translation_file": item.translation,
            "source_file": item.source,
            "translation_sha256": sha256(translation_path),
            "source_sha256": sha256(source_path),
            "translation_revision": revision,
            "source_revision": revision,
            "reviewer": None,
            "reviewed_at": None,
        })
    return rows


def manifest_init(path: Path) -> int:
    if path.exists():
        print(f"Refusing to overwrite existing manifest: {path}", file=sys.stderr)
        return 2
    payload = {
        "schema_version": 1,
        "seeded_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "seed_note": "Inventory snapshot only; no human review is implied.",
        "files": manifest_inventory(),
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Initialized {path.relative_to(ROOT)} with {len(payload['files'])} translation/source pairs.")
    print("Every entry starts unreviewed; hashes are drift baselines, not proof of sync.")
    return 0


def manifest_sync(path: Path) -> int:
    """Add newly mapped translations without changing any existing baselines."""
    if not path.is_file():
        return manifest_init(path)
    payload = json.loads(path.read_text(encoding="utf-8"))
    rows = payload.setdefault("files", [])
    known = {(row.get("locale"), row.get("translation_file")) for row in rows}
    added = 0
    for row in manifest_inventory():
        key = (row["locale"], row["translation_file"])
        if key not in known:
            rows.append(row)
            added += 1
    rows.sort(key=lambda row: (row.get("locale", ""), row.get("translation_file", "")))
    payload["last_inventory_sync_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Added {added} new translation/source pairs; existing hashes and review records were preserved.")
    return 0


def freshness_audit(path: Path, locale: str | None = None) -> int:
    if not path.is_file():
        print(f"Review manifest not found: {path}; run manifest-init first.", file=sys.stderr)
        return 2
    payload = json.loads(path.read_text(encoding="utf-8"))
    pairs, _ = translation_pairs(locale)
    current = {(item.locale, item.translation): item for item in pairs}
    records = {
        (row["locale"], row["translation_file"]): row
        for row in payload.get("files", [])
        if locale is None or row.get("locale") == locale
    }
    counts = Counter()
    findings: list[str] = []
    source_changes: dict[str, set[str]] = defaultdict(set)
    translation_changes: dict[str, set[str]] = defaultdict(set)
    for key, item in current.items():
        row = records.get(key)
        if row is None:
            counts["untracked"] += 1
            findings.append(f"UNTRACKED {item.translation}: add/review this file in the manifest")
            continue
        source_changed = (
            item.source != row.get("source_file")
            or sha256(ROOT / item.source) != row.get("source_sha256")
        )
        translation_changed = sha256(ROOT / item.translation) != row.get("translation_sha256")
        reviewed = bool(row.get("reviewer") and row.get("reviewed_at"))
        if source_changed:
            counts["source_changed"] += 1
            source_changes[item.source].add(item.locale)
        if translation_changed:
            counts["translation_changed"] += 1
            translation_changes[item.translation].add(item.locale)
        if not reviewed:
            counts["unreviewed"] += 1
        elif not source_changed and not translation_changed:
            counts["reviewed_current"] += 1
    obsolete = set(records) - set(current)
    counts["manifest_entries_without_files"] = len(obsolete)
    print("Freshness / review status:")
    for label in ("source_changed", "translation_changed", "unreviewed", "reviewed_current", "untracked", "manifest_entries_without_files"):
        print(f"  {label}: {counts[label]}")
    for source, locales in sorted(source_changes.items()):
        print(f"  SOURCE_CHANGED {source}: {len(locales)} locale translation(s)")
    for translation, locales in sorted(translation_changes.items()):
        print(f"  TRANSLATION_CHANGED {translation}")
    if findings:
        for finding in findings[:100]:
            print(f"  {finding}")
        if len(findings) > 100:
            print(f"  ... {len(findings) - 100} additional findings")
    return 1 if counts["source_changed"] or counts["translation_changed"] or counts["untracked"] or obsolete else 0


def record_review(path: Path, locale: str, translation_file: str, reviewer: str, confirmed: bool) -> int:
    if not confirmed:
        print("Refusing to record review without --confirm-fluent-independent-review.", file=sys.stderr)
        return 2
    if not path.is_file():
        print(f"Review manifest not found: {path}; run manifest-init first.", file=sys.stderr)
        return 2
    payload = json.loads(path.read_text(encoding="utf-8"))
    pairs, _ = translation_pairs(locale)
    item = next((x for x in pairs if x.translation == translation_file), None)
    if item is None:
        print(f"No current translation/source mapping for {locale}:{translation_file}", file=sys.stderr)
        return 2
    rows = payload.setdefault("files", [])
    row = next((x for x in rows if x.get("locale") == locale and x.get("translation_file") == translation_file), None)
    if row is None:
        row = {"locale": locale, "translation_file": translation_file}
        rows.append(row)
    revision = git_revision()
    row.update({
        "source_file": item.source,
        "translation_sha256": sha256(ROOT / item.translation),
        "source_sha256": sha256(ROOT / item.source),
        "translation_revision": revision,
        "source_revision": revision,
        "reviewer": reviewer,
        "reviewed_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    })
    rows.sort(key=lambda x: (x.get("locale", ""), x.get("translation_file", "")))
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Recorded review for {locale}:{translation_file} by {reviewer}.")
    return 0


def chapter_five_definitions_audit() -> int:
    result = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "ch5_translation_definition_audit.py")],
        cwd=ROOT,
    )
    return result.returncode


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=str(ROOT), help="Repository root (default: this checkout).")
    sub = parser.add_subparsers(dest="command", required=True)
    for name, help_text in (
        ("all", "Run freshness, structure, links, and glossary review aids."),
        ("freshness", "Compare files with the review-status hash manifest."),
        ("structure", "Compare anchors and Markdown structure to English sources."),
        ("links", "Resolve links and fragments from translated files and locale READMEs."),
        ("terminology", "Report exact glossary-form usage as a human review aid."),
    ):
        cmd = sub.add_parser(name, help=help_text)
        cmd.add_argument("--locale", help="Restrict the audit to one locale.")
        if name in ("structure", "links"):
            cmd.add_argument("--verbose", action="store_true", help="List all structural/link findings.")
        if name in ("all", "freshness"):
            cmd.add_argument("--manifest", default=str(DEFAULT_MANIFEST))
        if name == "terminology":
            cmd.add_argument("--verbose", action="store_true", help="List every possible surface-form review flag.")
    init = sub.add_parser("manifest-init", help="Create the initial inventory-only review manifest.")
    init.add_argument("--manifest", default=str(DEFAULT_MANIFEST))
    sub.add_parser("manifest-sync", help="Add new translations to the manifest without resetting existing status.").add_argument(
        "--manifest", default=str(DEFAULT_MANIFEST)
    )
    mark = sub.add_parser("record-review", help="Record a completed independent fluent-reader review.")
    mark.add_argument("--manifest", default=str(DEFAULT_MANIFEST))
    mark.add_argument("--locale", required=True)
    mark.add_argument("--file", required=True, help="Locale-relative translation file name.")
    mark.add_argument("--reviewer", required=True)
    mark.add_argument("--confirm-fluent-independent-review", action="store_true", required=True)
    args = parser.parse_args()
    root = Path(args.root).resolve()
    if root != ROOT:
        print("This checkout-root override is not supported by the bundled source mapper.", file=sys.stderr)
        return 2
    manifest = Path(getattr(args, "manifest", DEFAULT_MANIFEST))
    if not manifest.is_absolute():
        manifest = ROOT / manifest
    try:
        if args.command == "manifest-init":
            return manifest_init(manifest)
        if args.command == "manifest-sync":
            return manifest_sync(manifest)
        if args.command == "record-review":
            return record_review(manifest, args.locale, f"translations/{args.locale}/{args.file}", args.reviewer, args.confirm_fluent_independent_review)
        if args.command == "freshness":
            return freshness_audit(manifest, args.locale)
        if args.command == "structure":
            code, _ = structure_audit(args.locale, args.verbose)
            return code
        if args.command == "links":
            return link_audit(args.locale, args.verbose)
        if args.command == "terminology":
            return terminology_audit(args.locale, args.verbose)
        results = [freshness_audit(manifest, args.locale)]
        structure_code, _ = structure_audit(args.locale)
        results.append(structure_code)
        results.append(link_audit(args.locale))
        results.append(terminology_audit(args.locale))
        if args.locale is None:
            results.append(chapter_five_definitions_audit())
        return int(any(results))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"Translation audit failed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
