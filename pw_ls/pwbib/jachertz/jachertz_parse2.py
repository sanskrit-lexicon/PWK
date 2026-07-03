# -*- coding: utf-8 -*-
"""
jachertz_parse2.py  (Sonnet 5, 2026-07-03)

Re-run of jachertz_parse.py's backfill against the CORRECT current stub
baseline. jachertz_parse.py matched against pw_ls/pwbib/pwbib_new_work/
mergebibnew.txt, which has been frozen since 2016-08-05 (287 stubs). The
live, actively-maintained abbreviation source is actually
csl-pywork/v02/distinctfiles/pw/pywork/pwauth/pwbib_input.txt (a sibling
repo checkout), last touched 2025-10-24, with 352 unresolved entries
(tooltip == "[unknown literary source]"). See PWK issue #128.

This script re-parses the Jachertz bibliography (same source as
jachertz_parse.py) and backfills against the live pwbib_input.txt instead,
using a diacritic-aware normalizer so IAST house forms (pwbib) compare
correctly against Jachertz's ASCII AS-digit forms (e.g. "Kātantra" and
"Ka1tantra" both normalize to "KATANTRA").

Outputs (this folder; nothing overwrites canonical pwbib/csl-pywork data):
  jachertz_backfill_candidates2.tsv - stub -> Jachertz match candidates (REVIEW)
  jachertz_parse2_log.txt           - counts + how to read the outputs

Run:  python jachertz_parse2.py
"""
import re, sys, os, unicodedata
sys.stdout.reconfigure(encoding='utf-8'); sys.stderr.reconfigure(encoding='utf-8')

HERE = os.path.dirname(os.path.abspath(__file__))
PWK_ROOT = os.path.normpath(os.path.join(HERE, '..', '..', '..'))
JTXT = os.path.join(HERE, 'orig', 'pw-jachertz-utf8.txt')
LIVE_PWBIB_INPUT = os.path.normpath(os.path.join(
    PWK_ROOT, '..', 'csl-pywork', 'v02', 'distinctfiles', 'pw', 'pywork',
    'pwauth', 'pwbib_input.txt'))

sys.path.insert(0, HERE)
from jachertz_parse import parse, YEAR, IO, GILD, PWJ, DICTS  # noqa: E402


def norm_key(s):
    """Diacritic-aware cross-scheme key: NFKD-decompose, drop combining
    marks, keep ASCII letters, uppercase. Matches IAST (pwbib_input.txt,
    e.g. 'Kātantra.') against Jachertz's ASCII AS-digit scheme
    (e.g. 'Ka1tantra') -- both collapse to 'KATANTRA'."""
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^A-Za-z]', '', s).upper()


def load_live_stubs():
    if not os.path.exists(LIVE_PWBIB_INPUT):
        raise SystemExit(f"csl-pywork not found as a sibling checkout: {LIVE_PWBIB_INPUT}")
    stubs = []
    with open(LIVE_PWBIB_INPUT, encoding='utf-8') as f:
        for ln in f:
            p = ln.rstrip('\n').split('\t')
            if len(p) < 4:
                continue
            ident, abbrev, abbrev_disp, tooltip = p[0], p[1], p[2], p[3]
            if '[unknown literary source]' in tooltip:
                stubs.append({'id': ident, 'abbrev': abbrev, 'abbrev_disp': abbrev_disp,
                               'tooltip': tooltip})
    return stubs


def backfill(entries, stubs):
    works = {}
    xref = {}
    for e in entries:
        if e['type'] == 'work':
            works.setdefault(norm_key(e['head']), e)
        elif e['type'] == 'xref':
            xref[norm_key(e['head'])] = e['target']

    cands = []
    for st in stubs:
        k = norm_key(st['abbrev'])
        match, how = None, ''
        if k in works:
            match, how = works[k], 'exact'
        else:
            if k in xref:
                tk = norm_key(xref[k])
                if tk in works:
                    match, how = works[tk], 'xref'
            if match is None and len(k) >= 5:
                pref = [w for wk, w in works.items() if wk.startswith(k)]
                if len(pref) == 1:
                    match, how = pref[0], 'prefix'
        if match:
            eds = match['editions']
            cands.append((st['abbrev'], st['id'], how, match['head'],
                          ' | '.join(x['text'] for x in eds),
                          ','.join(x['io'] for x in eds if x['io']),
                          ','.join(x['gild'] for x in eds if x['gild'])))
    out = os.path.join(HERE, 'jachertz_backfill_candidates2.tsv')
    with open(out, 'w', encoding='utf-8', newline='\n') as f:
        f.write('pwbib_input_abbrev\tpwbib_input_id\tmatch_how\tjachertz_head\teditions\tio_shelfmarks\tgild_shelfmarks\n')
        for c in cands:
            f.write('\t'.join(c) + '\n')
    return out, cands


if __name__ == '__main__':
    entries = parse()
    stubs = load_live_stubs()
    bf, cands = backfill(entries, stubs)
    byhow = {}
    for c in cands:
        byhow[c[2]] = byhow.get(c[2], 0) + 1
    log = os.path.join(HERE, 'jachertz_parse2_log.txt')
    with open(log, 'w', encoding='utf-8', newline='\n') as f:
        f.write("jachertz_parse2.py run summary\n")
        f.write(f"live stub source: {LIVE_PWBIB_INPUT}\n")
        f.write(f"live unresolved stubs ('[unknown literary source]'): {len(stubs)}\n")
        f.write(f"backfill candidates: {len(cands)}  by method: {byhow}\n")
        f.write("\nNOTE: candidates are for HUMAN REVIEW; nothing is written back to\n")
        f.write("pwbib_input.txt or any canonical file. Compare against\n")
        f.write("jachertz_backfill_candidates.tsv (the earlier run against the stale\n")
        f.write("2016 mergebibnew.txt, 287 stubs) to see how much the live baseline changes results.\n")
    print(open(log, encoding='utf-8').read())
    print('wrote:', os.path.basename(bf), os.path.basename(log))
