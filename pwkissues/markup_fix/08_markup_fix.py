"""
Markup fixer + audit for pw.txt (PWK).

Counterpart of pwgissues/issue174/08_markup_fix.py (PWG).

Two jobs:

  1. FIX problems that have a single safe automatic resolution.
       (a) nested <ab><ab>X</ab> Y</ab>  →  <ab>X Y</ab>           (rare-but-possible)
       (b) nested <ab><ab>X</ab></ab>    →  <ab>X</ab>             (degenerate dup)
       (c) whitespace inside tag pairs, for every paired tag that
           actually occurs in pw.txt (see TRIM_TAGS).

  2. AUDIT issues that need a human decision. These are reported but
     NOT auto-modified. Each finding lands in markup_audit.txt with
     enough surrounding context to act.

Why the nesting fixer exists even though pw.txt is currently clean
on <ab>: this script is meant to be re-run after any new auto-wrap
pass that overlays <ab n="…"> tags (PWK's analog of AB's local-
abbreviation overlay for PWG). Such a pass can produce
<ab><ab>…</ab>…</ab>; this is the cleanup tool for that contingency.

PWK-specific notes vs the PWG counterpart:
  - TRIM_TAGS expanded to include the paired tags actually used in
    pw.txt: <bot>, <zoo>, <iw>, <arab>, <gk>, <hom>, <span> are
    PWK-active and were not in the PWG list.
  - <is> is also paired-trim-eligible in PWK (used 32,667 times).
  - <ls> nesting that lives INSIDE a {{ … }} correction block is
    NOT auto-fixed: the inner <ls> is part of the correction format
    (old → new || date | author | URL). It is reported for review.
  - No <ab n="?"> placeholders exist in pw.txt (PWG had 91), so that
    audit row will report 0 — kept anyway in case a future pass
    introduces them.

Inputs:
  ../../../csl-orig/v02/pw/pw.txt        (when run from pwkissues/<folder>/)
  or argv[1] (any path)

Outputs:
  pw_fixed.txt              -- repaired copy
  markup_fix_changes.txt    -- updateByLine-style log of every auto-fix
  markup_audit.txt          -- everything that needs a human eye, with line ref

Usage:
  python 08_markup_fix.py            # uses default in/out paths
  python 08_markup_fix.py IN OUT     # custom paths
"""

import sys
import re
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

HERE = Path(__file__).resolve().parent

if len(sys.argv) >= 3:
    PW_TXT = Path(sys.argv[1])
    OUT_FIX = Path(sys.argv[2])
else:
    candidates = [
        HERE.parent.parent.parent / "csl-orig" / "v02" / "pw" / "pw.txt",
        HERE / "pw.txt",
    ]
    PW_TXT = next((p for p in candidates if p.exists()), candidates[0])
    OUT_FIX = HERE / "pw_fixed.txt"

OUT_LOG = HERE / "markup_fix_changes.txt"
OUT_AUDIT = HERE / "markup_audit.txt"


# ---------------------------------------------------------------------------
# Pattern 1: nested <ab> wrappings
# ---------------------------------------------------------------------------
#
# After any future auto-wrap + local-abbreviation overlay pass we may see:
#   <ab><ab>vor.</ab> W.</ab>             (case a)
#   <ab n="?"><ab>St.</ab></ab>           (case b — exact-duplicate)
#
# Rule of repair:
#  * If the inner wrap covers a strict prefix or suffix of the outer wrap,
#    drop the inner — the outer is canonical.
#  * If the inner wrap exactly matches the outer wrap's content, drop the
#    inner (degenerate duplicate).
#  * If the inner wrap covers something in the middle, leave it — that is
#    too ambiguous to resolve without semantic context.

NEST_RX = re.compile(
    r"<ab(?P<oa>\b[^>]*)>(?P<pre>[^<]*)<ab(?P<ia>\b[^>]*)>(?P<inner>[^<]*)</ab>(?P<post>[^<]*)</ab>"
)


def fix_nested_ab(line):
    n_fixed = 0
    while True:
        m = NEST_RX.search(line)
        if not m:
            return line, n_fixed
        oa = m.group("oa")
        pre = m.group("pre")
        inner = m.group("inner")
        post = m.group("post")
        repl = f"<ab{oa}>{pre}{inner}{post}</ab>"
        line = line[:m.start()] + repl + line[m.end():]
        n_fixed += 1


# ---------------------------------------------------------------------------
# Pattern 2: whitespace inside common tag pairs
# ---------------------------------------------------------------------------
# Paired tags that actually exist in pw.txt (closing-tag counts):
#   lex 177,783 | ab 107,807 | ls 98,476 | is 32,667 | hom 10,052
#   bot 7,987   | zoo 364    | lang 265  | gk 90     | arab 48
#   iw 31       | span 4     | (mong/rus/F = 1 each, omitted)
TRIM_TAGS = ["ls", "ab", "lex", "is", "lang", "hom", "bot", "zoo",
             "gk", "iw", "arab", "span"]


def fix_trim_whitespace(line):
    n = 0
    for tag in TRIM_TAGS:
        pat = re.compile(rf"(<{tag}\b[^>]*>)(\s+)([^<]*?)(\s*)(</{tag}>)")
        def _repl(m):
            nonlocal n
            inside = m.group(3).rstrip()
            if inside != m.group(2) + m.group(3) + m.group(4):
                n += 1
            return f"{m.group(1)}{inside}{m.group(5)}"
        line = pat.sub(_repl, line)
        pat2 = re.compile(rf"(<{tag}\b[^>]*>)([^<]*?)(\s+)(</{tag}>)")
        def _repl2(m):
            nonlocal n
            inside = m.group(2).rstrip()
            n += 1
            return f"{m.group(1)}{inside}{m.group(4)}"
        line = pat2.sub(_repl2, line)
    return line, n


# ---------------------------------------------------------------------------
# Audit (no auto-modification)
# ---------------------------------------------------------------------------

# Helper used by the nested <ls> audit: classify each <ls>…<ls> match by
# whether the *inner* <ls> opens inside a {{ … }} correction block (which
# is part of the correction-record format and not a real markup bug) or
# outside one (a genuine nested-tag error worth attention).
def _ls_nested_classify(line):
    inside = []
    outside = []
    for m in re.finditer(r"<ls\b[^>]*>([^<]*<ls\b[^>]*>)", line):
        inner_offset = m.group(1).find("<ls")
        inner_open = m.start(1) + (inner_offset if inner_offset >= 0 else 0)
        prefix = line[:inner_open]
        if prefix.rfind("{{") > prefix.rfind("}}"):
            inside.append(m)
        else:
            outside.append(m)
    return outside, inside


AUDIT_CHECKS = [
    ("Adjacent </ab> <ab> — possibly intentional but worth verifying",
     re.compile(r"</ab>\s*<ab")),
    ("Nested <ls> outside a {{ … }} correction record",
     None),  # custom handler below
    ("Nested <ls> INSIDE a {{ … }} correction record (informational)",
     None),  # custom handler below
    ("<ab n=\"?\"> with literal '?' placeholder — needs an expansion",
     re.compile(r'<ab\s+n="\?">')),
    ("Empty content tag",
     re.compile(r"<(ls|ab|lex|is|lang|hom|bot|zoo|gk|iw|arab)\b[^>]*></\1>")),
    ("{%…%} closing brace immediately followed by <is> (likely missing space)",
     re.compile(r"%\}<is\b")),
    ("{#…#} closing brace immediately followed by <ab>/<ls>/<is> (likely missing space)",
     re.compile(r"#\}<(?:ab|ls|is)\b")),
    ("[PageN-NNN-N] glued to preceding </ls>. (likely missing space or newline)",
     re.compile(r"</ls>\.\[Page\d")),
    ("Malformed tag with unescaped < inside its own attribute value",
     re.compile(r'<[A-Za-z][A-Za-z0-9]*\s+[A-Za-z]+="[^"]*<[^"]*"\s*[^>]*>')),
]


def main():
    print(f"Reading {PW_TXT} …", flush=True)
    lines = PW_TXT.read_text(encoding="utf-8").splitlines()
    print(f"  {len(lines):,} lines", flush=True)

    out_lines = []
    fix_log = []
    tot_nested = 0
    tot_trim = 0

    audit_hits = {label: [] for label, _ in AUDIT_CHECKS}

    for lineno, line in enumerate(lines, 1):
        orig = line
        line, n1 = fix_nested_ab(line)
        line, n2 = fix_trim_whitespace(line)
        tot_nested += n1
        tot_trim += n2
        if line != orig:
            fix_log.append((lineno, orig, line))
        out_lines.append(line)

        # custom handlers for nested <ls>
        outside_hits, inside_hits = _ls_nested_classify(orig)
        for m in outside_hits:
            start = max(0, m.start() - 40)
            end = min(len(orig), m.end() + 40)
            audit_hits["Nested <ls> outside a {{ … }} correction record"].append(
                (lineno, orig[start:end].replace("\t", " "))
            )
        for m in inside_hits:
            start = max(0, m.start() - 40)
            end = min(len(orig), m.end() + 40)
            audit_hits["Nested <ls> INSIDE a {{ … }} correction record (informational)"].append(
                (lineno, orig[start:end].replace("\t", " "))
            )

        for label, pat in AUDIT_CHECKS:
            if pat is None:
                continue
            for m in pat.finditer(orig):
                start = max(0, m.start() - 40)
                end = min(len(orig), m.end() + 40)
                snippet = orig[start:end].replace("\t", " ")
                audit_hits[label].append((lineno, snippet))
                if len(audit_hits[label]) >= 5000:
                    break
        if lineno % 200000 == 0:
            print(f"  {lineno:,}/{len(lines):,}", flush=True)

    print(f"Total nested <ab> repairs:    {tot_nested}", flush=True)
    print(f"Total whitespace trims:       {tot_trim}", flush=True)
    print(f"Total changed lines:          {len(fix_log)}", flush=True)

    print(f"Writing {OUT_FIX} …", flush=True)
    with OUT_FIX.open("w", encoding="utf-8", newline="\n") as f:
        for line in out_lines:
            f.write(line + "\n")

    print(f"Writing {OUT_LOG} …", flush=True)
    with OUT_LOG.open("w", encoding="utf-8") as f:
        f.write("; markup_fix log for pw.txt\n")
        f.write(f"; nested <ab>:    {tot_nested}\n")
        f.write(f"; whitespace:     {tot_trim}\n")
        f.write(f"; changed lines:  {len(fix_log)}\n;\n")
        for lineno, old, new in fix_log:
            f.write(f"{lineno} old {old}\n")
            f.write(f"{lineno} new {new}\n")

    print(f"Writing {OUT_AUDIT} …", flush=True)
    with OUT_AUDIT.open("w", encoding="utf-8") as f:
        f.write("PWK markup audit — findings requiring a human decision\n")
        f.write("=" * 60 + "\n\n")
        f.write("Generated by 08_markup_fix.py against pw.txt.\n")
        f.write("Items below were DETECTED but NOT modified by the fixer.\n")
        f.write("Each section explains the pattern and what to consider.\n\n")
        f.write("If a check has matches: 0, that pattern is currently absent\n")
        f.write("from pw.txt — the check is kept so this script can be re-run\n")
        f.write("after any future auto-wrap / local-overlay pass and still\n")
        f.write("catch what those passes might introduce.\n\n")
        f.write("------------------------------------------------------------\n")
        f.write("\nWHAT THIS FIXER AUTO-CORRECTS\n")
        f.write("------------------------------------------------------------\n")
        f.write("  - Nested <ab><ab>X</ab> Y</ab>          → <ab>X Y</ab>\n")
        f.write("  - Whitespace inside <ls>/<ab>/<lex>/<is>/<lang>/<hom>/\n")
        f.write("    <bot>/<zoo>/<gk>/<iw>/<arab>/<span>\n")
        f.write("\nThe original file is left untouched; results go to\n")
        f.write("pw_fixed.txt with the full change log in markup_fix_changes.txt.\n\n")
        f.write("------------------------------------------------------------\n")
        f.write("\nWHAT NEEDS HUMAN ATTENTION\n")
        f.write("------------------------------------------------------------\n")
        f.write("  1. Adjacent </ab> <ab> — pw.txt has ~4,171 of these. Most\n")
        f.write("     are clearly two separate intended abbreviations\n")
        f.write("     (<ab>Pl.</ab> <ab>Bez.</ab>, <ab>u. s. w.</ab>\n")
        f.write("     <ab>Vgl.</ab>, etc.) — verify rather than auto-merge.\n")
        f.write("     If any pair *should* be a single <ab>, fix by hand.\n\n")
        f.write("  2. Nested <ls> outside a correction record — pw.txt has 0\n")
        f.write("     of these at present. (The 2 nested-<ls> cases that do\n")
        f.write("     exist all live inside {{…}} correction blocks, which are\n")
        f.write("     legitimate — see informational row below.)\n\n")
        f.write("  3. Nested <ls> INSIDE {{…}} correction records — these are\n")
        f.write("     part of the correction-record format\n")
        f.write("     ({{old -> new || date | author | URL |}}).  Reported for\n")
        f.write("     awareness only; do not touch.\n\n")
        f.write("  4. {%…%}<is> and {#…#}<is>/<ab>/<ls> boundary collisions —\n")
        f.write("     usually a missing space after the closing brace.  Each\n")
        f.write("     is rare in pw.txt (≤ 2 occurrences) but easy to fix.\n\n")
        f.write("  5. [Page#-###-#] glued to a preceding </ls>. — currently\n")
        f.write("     1 occurrence (L634460).  Either insert a space or, more\n")
        f.write("     consistently with the rest of the file, break the line.\n\n")
        f.write("  6. <ab n=\"?\"> placeholders — pw.txt has 0 of these (PWG\n")
        f.write("     has 91).  Kept as a check so a future overlay can be\n")
        f.write("     re-validated.\n\n")
        f.write("  7. PWK-specific tags <bot>, <zoo>, <iw>, <arab> have low\n")
        f.write("     enough usage that visual review of their content is\n")
        f.write("     cheap; not addressed here.  See:\n")
        f.write("       grep -n '<bot>'  pw.txt | head\n")
        f.write("       grep -n '<zoo>'  pw.txt | head\n")
        f.write("       grep -n '<iw>'   pw.txt\n")
        f.write("       grep -n '<arab>' pw.txt\n\n")
        f.write("------------------------------------------------------------\n")
        f.write("\nAUTOMATED CHECKS BELOW\n")
        f.write("------------------------------------------------------------\n\n")
        for label, _ in AUDIT_CHECKS:
            hits = audit_hits[label]
            f.write(f"## {label}\n")
            f.write(f"   matches: {len(hits)} (showing up to 200)\n")
            for ln, snippet in hits[:200]:
                f.write(f"   L{ln}: {snippet}\n")
            f.write("\n")

    print("DONE", flush=True)


if __name__ == "__main__":
    main()
