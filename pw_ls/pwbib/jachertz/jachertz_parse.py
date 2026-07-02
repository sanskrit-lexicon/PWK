# -*- coding: utf-8 -*-
"""
jachertz_parse.py  (Opus 4.8, 2026-07-02)

Parse the digitized Jachertz 1983 bibliography (pw-jachertz-utf8.txt) into a
structured, queryable table, and attempt a conservative backfill of the
UNRESOLVED entries in the pwbib "list of works" (mergebibnew.txt, flag=0 / '?').

Outputs (all in this folder; none overwrite canonical pwbib data):
  jachertz_bib.tsv                 - one row per Jachertz entry
  jachertz_backfill_candidates.tsv - pwbib stub -> Jachertz match candidates (REVIEW)
  jachertz_parse_log.txt           - counts + how to read the outputs

Run:  python jachertz_parse.py
"""
import re, sys, os
sys.stdout.reconfigure(encoding='utf-8'); sys.stderr.reconfigure(encoding='utf-8')

HERE = os.path.dirname(os.path.abspath(__file__))
PWBIB = os.path.normpath(os.path.join(HERE, '..'))
JTXT = os.path.join(HERE, 'orig', 'pw-jachertz-utf8.txt')
MERGE = os.path.join(PWBIB, 'pwbib_new_work', 'mergebibnew.txt')

def norm_key(s):
    """Match key across differing AS digit schemes: drop digits/punct, uppercase.
    Jachertz a1=a-macron and pwbib A7=A-macron both collapse to the base letter."""
    return re.sub(r'[^A-Za-z]', '', s).upper()

YEAR = re.compile(r'\b(1[5-9]\d\d)\b')
IO   = re.compile(r'\[I\.O\.\s*(\d+)\]')
GILD = re.compile(r'\[Gild\.\s*(\d+)\]')
PWJ  = re.compile(r'\[pwj\d+\]')
DICTS= re.compile(r'\b(PW,\s*pw|PW|pw)\b')

def parse_editions(edlines):
    eds = []
    for raw in edlines:
        t = raw.strip()
        t = re.sub(r'^<p>--\.*\s*', '', t)          # strip the "--..." lead
        io = IO.search(t)
        gild = GILD.search(t)
        yr = YEAR.findall(t)
        di = DICTS.findall(t)
        clean = PWJ.sub('', GILD.sub('', IO.sub('', t))).strip().rstrip(';,')
        eds.append({
            'text': clean,
            'year': yr[-1] if yr else '',
            'io': io.group(1) if io else '',
            'gild': gild.group(1) if gild else '',
            'dicts': ('PW,pw' if any(',' in d for d in di) else
                      'PW' if 'PW' in di else 'pw' if 'pw' in di else ''),
        })
    return eds

def parse():
    lines = open(JTXT, encoding='utf-8').read().splitlines()
    entries = []
    i = 0
    hb = re.compile(r'^\s*<p><b>(.+?)</b>(.*)$')
    while i < len(lines):
        m = hb.match(lines[i])
        if not m:
            i += 1; continue
        head, rest = m.group(1).strip(), m.group(2).strip()
        if rest.startswith('='):
            entries.append({'head': head, 'type': 'abbrev', 'target': rest[1:].strip(),
                            'editions': []})
            i += 1
        elif rest.startswith('s.') or rest.startswith('s '):
            entries.append({'head': head, 'type': 'xref',
                            'target': rest[2:].strip().lstrip('.').strip(), 'editions': []})
            i += 1
        else:
            # a work: gather following '--' edition lines
            eds = []
            j = i + 1
            while j < len(lines):
                s = lines[j].strip()
                if s.startswith('<p>--'):
                    eds.append(lines[j]); j += 1
                elif s == '':
                    j += 1
                    # allow a blank between head and first edition, but stop at next <b>
                    if j < len(lines) and hb.match(lines[j]):
                        break
                    if eds:  # blank after editions ends the block
                        break
                else:
                    break
            entries.append({'head': head, 'type': 'work',
                            'target': '', 'editions': parse_editions(eds)})
            i = j
    return entries

def write_bib(entries):
    out = os.path.join(HERE, 'jachertz_bib.tsv')
    with open(out, 'w', encoding='utf-8', newline='\n') as f:
        f.write('head_as\tkey\ttype\ttarget\tn_ed\teditions\tio_shelfmarks\tgild_shelfmarks\tdicts\n')
        for e in entries:
            eds = e['editions']
            edtext = ' | '.join(x['text'] for x in eds)
            ios = ','.join(x['io'] for x in eds if x['io'])
            gilds = ','.join(x['gild'] for x in eds if x['gild'])
            dic = ','.join(sorted({x['dicts'] for x in eds if x['dicts']}))
            f.write(f"{e['head']}\t{norm_key(e['head'])}\t{e['type']}\t{e['target']}\t"
                    f"{len(eds)}\t{edtext}\t{ios}\t{gilds}\t{dic}\n")
    return out

def load_stubs():
    stubs = []
    for ln in open(MERGE, encoding='utf-8'):
        p = ln.rstrip('\n').split(':')
        if len(p) >= 5 and p[3] == '0' and p[4].strip() in ('?', ''):
            stubs.append({'abbrvsort': p[0], 'abbrv': p[1], 'id': p[2]})
    return stubs

def backfill(entries, stubs):
    # index works + resolve xrefs to their work
    works = {e['head']: e for e in entries if e['type'] == 'work'}
    xref  = {norm_key(e['head']): e['target'] for e in entries if e['type'] == 'xref'}
    work_by_key = {}
    for e in entries:
        if e['type'] == 'work':
            work_by_key.setdefault(norm_key(e['head']), e)
    cands = []
    for st in stubs:
        k = norm_key(st['abbrvsort'])
        match, how = None, ''
        # 1) exact key hit on a work
        if k in work_by_key:
            match, how = work_by_key[k], 'exact'
        else:
            # 2) via xref abbreviation -> work
            if k in xref:
                tk = norm_key(xref[k])
                if tk in work_by_key:
                    match, how = work_by_key[tk], 'xref'
            # 3) prefix: stub key is a prefix of a work key (>=5 chars, unique)
            if match is None and len(k) >= 5:
                pref = [w for wk, w in work_by_key.items() if wk.startswith(k)]
                if len(pref) == 1:
                    match, how = pref[0], 'prefix'
        if match:
            eds = match['editions']
            cands.append((st['abbrvsort'], st['id'], how, match['head'],
                          ' | '.join(x['text'] for x in eds),
                          ','.join(x['io'] for x in eds if x['io']),
                          ','.join(x['gild'] for x in eds if x['gild'])))
    out = os.path.join(HERE, 'jachertz_backfill_candidates.tsv')
    with open(out, 'w', encoding='utf-8', newline='\n') as f:
        f.write('pwbib_abbrv\tpwbib_id\tmatch_how\tjachertz_head\teditions\tio_shelfmarks\tgild_shelfmarks\n')
        for c in cands:
            f.write('\t'.join(c) + '\n')
    return out, cands

if __name__ == '__main__':
    entries = parse()
    nb = write_bib(entries)
    stubs = load_stubs()
    bf, cands = backfill(entries, stubs)
    byhow = {}
    for c in cands: byhow[c[2]] = byhow.get(c[2], 0) + 1
    ntyp = {}
    for e in entries: ntyp[e['type']] = ntyp.get(e['type'], 0) + 1
    ned = sum(len(e['editions']) for e in entries)
    nio = sum(1 for e in entries for x in e['editions'] if x['io'])
    ngild = sum(1 for e in entries for x in e['editions'] if x['gild'])
    log = os.path.join(HERE, 'jachertz_parse_log.txt')
    with open(log, 'w', encoding='utf-8', newline='\n') as f:
        f.write("jachertz_parse.py run summary\n")
        f.write(f"entries parsed: {len(entries)}  by type: {ntyp}\n")
        f.write(f"total editions: {ned}   with I.O. shelfmark: {nio}   with Gild. shelfmark: {ngild}\n")
        f.write(f"pwbib unresolved stubs (flag=0/'?'): {len(stubs)}\n")
        f.write(f"backfill candidates: {len(cands)}  by method: {byhow}\n")
        f.write("\nNOTE: candidates are for HUMAN REVIEW; nothing is written back to\n")
        f.write("mergebibnew.txt or any canonical pwbib file. 'prefix' matches are the\n")
        f.write("least certain (stub abbreviation is a prefix of exactly one work key).\n")
    print(open(log, encoding='utf-8').read())
    print('wrote:', os.path.basename(nb), os.path.basename(bf), os.path.basename(log))
