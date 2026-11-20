#!/usr/bin/env python3
"""Phase D: rebuild tools/architecture/chapter_numbers.json and chapter_crosswalk.json for the new numbering.
Each moved row keeps its old ids and gains ``pre_reorganization_2026_11_20`` (its machine id before this move),
which is the translation crosswalk for this renumbering. New rows: Chapter One (Constitutional Map) and Chapter
Seven (Independent Bodies). Old Chapters Two to Four become layer SUBCORE rows (Subcore 3-A, 3-B, 3-C).
"""
import json, re
SUB = {'02': ('03010', 'S3-A', 'subcore_03.010_definition_structure.md'),
       '03': ('03020', 'S3-B', 'subcore_03.020_definition_integrity.md'),
       '04': ('03030', 'S3-C', 'subcore_03.030_burden_traceability_verification.md')}
def newnum(n):
    if n == 0: return 0
    if n == 1: return 2
    if n in (2, 3, 4): return None
    if 5 <= n <= 8: return n - 2
    if 9 <= n <= 31: return n - 1
    return n
def disp(num): return f"{int(num[:2])}.{num[2:]}"
def tf(s):
    """Rewrite file names, machine ids, display ids and corpus fragments inside a string."""
    s = re.sub(r'(?<![\w])core_(\d\d)\.(\d{3})_', lambda m: m.group(0) if newnum(int(m.group(1))) in (None, int(m.group(1))) else 'core_%02d.%s_' % (newnum(int(m.group(1))), m.group(2)), s)
    s = re.sub(r'(?<![\w])(cjs|ci|cs|cf)_(\d\d)\.(\d{3})_', lambda m: m.group(0) if newnum(int(m.group(2))) in (None, int(m.group(2))) else '%s_%02d.%s_' % (m.group(1), newnum(int(m.group(2))), m.group(3)), s)
    s = re.sub(r'(?<![\w-])(CJS|CI|CS|CF)-(\d\d)(\d{3})(?!\d)', lambda m: m.group(0) if newnum(int(m.group(2))) in (None, int(m.group(2))) else '%s-%02d%s' % (m.group(1), newnum(int(m.group(2))), m.group(3)), s)
    s = re.sub(r'(?<![\w-])(CJS|CI|CS|CF)-(\d{1,2})\.(\d{3})(?!\d)', lambda m: m.group(0) if newnum(int(m.group(2))) in (None, int(m.group(2))) else '%s-%d.%s' % (m.group(1), newnum(int(m.group(2))), m.group(3)), s)
    s = re.sub(r'(?<![\w-])(cjs|ci|cs|cf)-(\d{1,2})(\d{3})(?=-)', lambda m: m.group(0) if newnum(int(m.group(2))) in (None, int(m.group(2))) else '%s-%d%s' % (m.group(1), newnum(int(m.group(2))), m.group(3)), s)
    return s
P = 'tools/architecture/chapter_numbers.json'
d = json.load(open(P))
rows = []
for r in d['chapters']:
    r = dict(r); old = r['machine_id']; home = int(r['core_home'])
    if r['layer'] == 'CORE' and r['core_home'] in SUB and r['machine_number'].endswith('000'):
        num, display, dest = SUB[r['core_home']]
        r.update(layer='SUBCORE', machine_id='SUB-' + num, machine_number=num, display_id=display, core_home='03',
                 destination_file=dest, title=display, ordinal_name=display, layer_digit='0')
    elif newnum(home) != home:
        nh = '%02d' % newnum(home); num = nh + r['machine_number'][2:]
        r.update(core_home=nh, machine_number=num, destination_file=tf(r['destination_file']))
        if r['layer'] == 'CORE':
            r.update(machine_id=num, display_id=disp(num), title=str(int(nh)), ordinal_name=str(int(nh)))
        else:
            r.update(machine_id=f"{r['layer']}-{num}", display_id=f"{r['layer']}-{disp(num)}")
    if r['machine_id'] != old:
        r['pre_reorganization_2026_11_20'] = old
    rows.append(r)
def core(num, dest, old_id, original):
    return {'old_id': old_id, 'original_file': original, 'machine_id': num, 'display_id': disp(num), 'layer': 'CORE',
            'core_home': num[:2], 'title': str(int(num[:2])), 'destination_file': dest, 'status': 'active',
            'machine_number': num, 'layer_digit': '0', 'ordinal_name': str(int(num[:2]))}
rows.append(core('01000', 'core_01.000_constitutional_map.md', 'Chapter 0 §3.2, §4–§9', 'core_00.000_preamble.md'))
rows.append(core('07000', 'core_07.000_independent_bodies.md', 'Chapter 8 §11', 'core_08.000_functional_independence_separation_of_duties.md'))
order = {'CORE': 0, 'SUBCORE': 0, 'CJS': 1, 'CI': 2, 'CS': 3, 'CF': 4}
rows.sort(key=lambda r: (order[r['layer']], r['machine_number'], r['layer']))
d['chapters'] = rows
json.dump(d, open(P, 'w'), indent=2); open(P, 'a').write('\n')
C = 'tools/architecture/chapter_crosswalk.json'
c = json.load(open(C))
KEYS = ('source_file', 'display_id', 'new_anchor')  # crosswalk machine ids are frozen legacy keys
def walk(o):
    if isinstance(o, dict):
        return {k: (tf(v) if k in KEYS and isinstance(v, str) else walk(v)) for k, v in o.items()}
    if isinstance(o, list):
        return [walk(x) for x in o]
    return o
c = walk(c)
json.dump(c, open(C, 'w'), indent=2); open(C, 'a').write('\n')
print('rows', len(rows))
