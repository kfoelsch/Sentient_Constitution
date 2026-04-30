#!/usr/bin/env python3
"""One-shot revert: restore constitutional wording where ``charter`` was used for Corpus sense.

Skips legal-instrument senses (corporate charter; treaty/compact/or charter; adoption/federation/or charter;
``supervise, charter, or``). Keeps **Constitutional Systems** and ``(Constitutional)`` definition titles intact.

Run from repo root:
  python3 tools/corpus_charter_vocab_revert.py
"""

from __future__ import annotations

import importlib.util
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]

TARGETS = [
    ROOT / "core_constitution.md",
    ROOT / "corpus_joint_structure.md",
    ROOT / "corpus_systems.md",
    ROOT / "corpus_institutions.md",
    ROOT / "CONSTITUTIONAL_REGRESSION_SCENARIOS.md",
]

_CS_PLACE = "§§CONSTITUTIONAL_SYSTEMS§§"

_ALLOW_PATTERNS = [
    re.compile(r"corporate charter(\s+law)?", re.I),
    re.compile(r"treaty,\s+compact,\s+or\s+charter", re.I),
    re.compile(r"adoption,\s+federation,\s+or\s+charter", re.I),
    re.compile(r"supervise,\s+charter,\s+or", re.I),
]

_PLACEHOLDER = "§§ALLOW{:d}§§"


def _load_phrase_pairs() -> list[tuple[str, str]]:
    spec = importlib.util.spec_from_file_location(
        "apply_charter_vocab",
        ROOT / "tools" / "apply_charter_vocab.py",
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(mod)
    pairs: list[tuple[str, str]] = []
    seen: set[str] = set()
    for old, new in mod.PHRASES:
        if old == "constitutional" and new == "charter":
            continue
        if new in seen:
            continue
        seen.add(new)
        pairs.append((new, old))
    pairs.sort(key=lambda x: len(x[0]), reverse=True)
    return pairs


def _protect_allowed(text: str) -> tuple[str, list[str]]:
    stored: list[str] = []

    def _sub(i: int, m: re.Match[str]) -> str:
        stored.append(m.group(0))
        return _PLACEHOLDER.format(len(stored) - 1)

    out = text
    for i, pat in enumerate(_ALLOW_PATTERNS):
        out = pat.sub(lambda m, idx=i: _sub(idx, m), out)
    return out, stored


def _restore_allowed(text: str, stored: list[str]) -> str:
    for i, s in enumerate(stored):
        text = text.replace(_PLACEHOLDER.format(i), s)
    return text


def _protect_constitutional_systems(text: str) -> str:
    return text.replace("Constitutional Systems", _CS_PLACE)


def _restore_constitutional_systems(text: str) -> str:
    return text.replace(_CS_PLACE, "Constitutional Systems")


def _protect_paren_constitutional(text: str) -> tuple[str, list[str]]:
    stored: list[str] = []

    def _sub(m: re.Match[str]) -> str:
        stored.append(m.group(0))
        return f"§§PAREN{len(stored)-1}§§"

    pattern = re.compile(r"\([^)]*\(Constitutional\)[^)]*\)")
    out = pattern.sub(_sub, text)
    return out, stored


def _restore_paren(text: str, stored: list[str]) -> str:
    for i, s in enumerate(stored):
        text = text.replace(f"§§PAREN{i}§§", s)
    return text


_CHARTER_WORD = re.compile(r"(?<![A-Za-z0-9])charter(?![A-Za-z0-9])")


def _bare_charter_to_constitutional(text: str) -> str:
    def _one(m: re.Match[str]) -> str:
        w = m.group(0)
        if w.isupper():
            return "CONSTITUTIONAL"
        if w[:1].isupper():
            return "Constitutional"
        return "constitutional"

    return _CHARTER_WORD.sub(_one, text)


def transform(text: str, phrase_pairs: list[tuple[str, str]]) -> str:
    text = _protect_constitutional_systems(text)
    text, paren_store = _protect_paren_constitutional(text)
    text, allow_store = _protect_allowed(text)
    for charter_phrase, const_phrase in phrase_pairs:
        text = text.replace(charter_phrase, const_phrase)
        text = text.replace(charter_phrase.capitalize(), const_phrase)
        # Title Case heuristic for headings like "Charter tracing"
        if charter_phrase[:1].islower():
            continue
        ct = charter_phrase.title()
        if ct != charter_phrase and ct in text:
            ctp = const_phrase.title() if const_phrase.islower() else const_phrase
            text = text.replace(ct, ctp)
    text = _bare_charter_to_constitutional(text)
    text = _restore_allowed(text, allow_store)
    text = _restore_paren(text, paren_store)
    text = _restore_constitutional_systems(text)
    return text


def main() -> int:
    pairs = _load_phrase_pairs()
    for path in TARGETS:
        if not path.is_file():
            print(f"skip missing {path}", file=sys.stderr)
            continue
        raw = path.read_text(encoding="utf-8")
        out = transform(raw, pairs)
        path.write_text(out, encoding="utf-8")
        print(f"updated {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
