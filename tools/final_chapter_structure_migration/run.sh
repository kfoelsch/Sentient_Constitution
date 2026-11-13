#!/bin/bash
# One-off record of the final chapter structure move (492nd move, 2026-11-12).
# Usage: bash tools/final_chapter_structure_migration/run.sh [REPO_ROOT]
# Runs against the tree as it stood BEFORE the move (45 core files, Chapters 0-20).
# It will not work on the post-move tree; it is kept as the reproducible record.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
W="$(cd "${1:-.}" && pwd)"
S="${TMPDIR:-/tmp}/final_chapter_structure_spec.json"
cd "$W"
python3 "$HERE/mkspecs2.py" "$W" "$S" > /dev/null
python3 "$HERE/split_parts.py" "$W" "$S" --apply | tail -1
python3 "$HERE/patch_tools.py" "$W" "$S" ch1 | tail -1
python3 "$HERE/chapters.py" "$W" --apply | tail -6
python3 "$HERE/patch_words.py"
python3 "$HERE/post2.py"
python3 "$HERE/handedits.py"
python3 "$HERE/autoname.py"
python3 tools/time_reference_audit.py --write-baseline | tail -1
python3 tools/emit_regression_scenarios.py | tail -1
python3 tools/ch10_duplication_audit.py --write-baseline | tail -1
make architecture-index boundary-chunks plain-terms-edition ai-manifest-regenerate > /dev/null
python3 tools/part_cite_chapter_audit.py > "${TMPDIR:-/tmp}/part_cites.txt" 2>&1
python3 "$HERE/fix_part_cites.py" . "${TMPDIR:-/tmp}/part_cites.txt" | tail -2
python3 tools/part_cite_chapter_audit.py | tail -1
echo "Then: make audit-report; compare obligation totals with"
echo "  python3 $HERE/obligation_totals.py OLD_ROOT NEW_ROOT"
