import re
p='tools/ch10_duplication_audit.py'; t=open(p).read()
t=t.replace('TARGET = "core_12.000_institutional_alignment_certification_evaluation.md"','TARGETS = (\n    "core_12.000_institutional_alignment_certification_evaluation.md",\n    "core_13.000_institutional_alignment_certification_forum_process_outcomes.md",\n    "core_14.000_institutional_alignment_certification_records_recertification.md",\n)')
t=t.replace('''    target_path = root / TARGET
    targets = extract_sentences(TARGET, target_path.read_text(encoding="utf-8")) if target_path.is_file() else []''','''    targets: list[Sentence] = []
    for TARGET in TARGETS:
        target_path = root / TARGET
        if target_path.is_file():
            targets += extract_sentences(TARGET, target_path.read_text(encoding="utf-8"))''')
t=t.replace('Sentence(f"Chapter Nine Part {part}"','Sentence(f"Chapters Nine to Eleven ({part})"')
open(p,'w').write(t); print('patched')
t=open(p).read()
t=t.replace('''        match = _HEADING.match(raw)
        if match:
            section = match.group(2)
            continue
        cleaned = _clean(raw)
        if not cleaned:
            continue
''','''        match = _HEADING.match(raw)
        if match:
            section = match.group(2)
            continue
        if raw.startswith("#"):
            continue  # chapter titles are parallel by design (Chapters 9-11 and 12-14)
        if stripped.startswith("*Draft pending steward review.*"):
            continue  # Purpose and Role placeholder stub, identical until drafted
        cleaned = _clean(raw)
        if not cleaned:
            continue
''')
open(p,'w').write(t); print('patched2')
