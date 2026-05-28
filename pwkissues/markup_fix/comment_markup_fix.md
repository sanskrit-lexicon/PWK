### Location

Counterpart of https://github.com/sanskrit-lexicon/PWG/issues/175 for `pw.txt`.

I ran Claude over `csl-orig/v02/pw/pw.txt` with the same two-job
recipe used for PWG (auto-fix the few things that have a single safe
resolution; audit everything else with line refs).  Proposing to add
`08_markup_fix.py` plus its outputs to a new `pwkissues/` folder
(e.g. `pwkissues/issue_markup_fix/`).  @funderburkjim
@Andhrabharati — would value a look at the 4,171 adjacent `</ab> <ab>`
list and the two `<ls>` cases inside `{{…}}` correction blocks.

## Markup fixer + audit for `pw.txt`

### What it auto-fixes

| Pattern | Result |
|---|---|
| `<ab><ab>vor.</ab> W.</ab>` | `<ab>vor. W.</ab>` |
| `<ab n="X"><ab>St.</ab></ab>` | `<ab n="X">St.</ab>` |
| `<ab>foo<ab>bar</ab>baz</ab>` | `<ab>foobarbaz</ab>` |
| `<ls> GORR. 1,69,9 </ls>` | `<ls>GORR. 1,69,9</ls>` |
| `<bot> Musa sapientum </bot>` | `<bot>Musa sapientum</bot>` |
| `<lang n="greek"> ἀ</lang>` | `<lang n="greek">ἀ</lang>` |

Whitespace trimming applies to every paired tag that actually occurs
in `pw.txt`: `<ls>`, `<ab>`, `<lex>`, `<is>`, `<lang>`, `<hom>`,
`<bot>`, `<zoo>`, `<gk>`, `<iw>`, `<arab>`, `<span>`.  The original
file is never modified — output goes to `pw_fixed.txt`, with the full
diff in `markup_fix_changes.txt` (updateByLine format).

### Closing-tag inventory in current `pw.txt`

| Tag | Count |
|---|---:|
| `</lex>` | 177,783 |
| `</ab>`  | 107,807 |
| `</ls>`  |  98,476 |
| `</is>`  |  32,667 |
| `</hom>` |  10,052 |
| `</bot>` |   7,987 |
| `</zoo>` |     364 |
| `</lang>` |    265 |
| `</gk>`  |      90 |
| `</arab>` |     48 |
| `</iw>`  |      31 |
| `</span>` |      4 |
| `<sic/>` (self-closing) | 27 |

Every open/close count matches, so `pw.txt` is tag-balanced at the
file level.  Several tags that are zero-usage in PWG are real in PWK:
`<bot>`, `<zoo>`, `<iw>`, `<arab>`.

### What it found in current `pw.txt`

- **0** nested `<ab>` — clean.
- **0** whitespace trims — `pw.txt` is currently free of leading/trailing
  spaces inside tag pairs.  The fixer is kept for re-runs after any
  future wrap / overlay pass.
- **0** `<ab n="?">` placeholders (PWG has 91; PWK already filled them
  in — `<ab n="…">` is present 1,142 times with 618 unique German
  expansions, top values `unter` 129, `und` 127, `Zeit` 39).
- **2** nested `<ls>` — both at `BHĀG. P.` lines (L84708 and L202888),
  both **inside `{{ … }}` correction records**.  These are part of the
  correction format `{{old -> new || date | author | URL |}}` from
  PWK#109 work; the fixer flags them informationally and leaves them
  alone.
- **1** `{%…%}<is>` boundary collision — L96894
  `{%des%}<is>Agni</is>` (missing space).
- **1** `</ls>.[Page…]` glued — L634460
  `<ls>DĀRILA zu KAUŚ. 25,18</ls>.[Page7-363-b]<info n="sup_7"/>`.
- **4,171** adjacent `</ab> <ab>` — listed for verification.  Spot
  checks (`<ab>Pl.</ab> <ab>Bez.</ab>`, `<ab>u. s. w.</ab>
  <ab>Vgl.</ab>`, `<ab>3.</ab> <ab>Pl.</ab>`) all look intentional;
  not auto-merged.

### Broader cleanup checklist (in `markup_audit.txt`)

1. **Adjacent `</ab> <ab>`** — 4,171 occurrences.  Vast majority are
   two separate intended abbreviations; only flag if a pair *should*
   collapse into a single `<ab>`.
2. **Nested `<ls>` inside `{{ … }}`** — 2 occurrences.  Awareness
   only; the correction-record format intentionally embeds the prior
   `<ls>`.
3. **Boundary-collision singletons** — `{%…%}<is>` (1 hit, L96894)
   and `</ls>.[Page…]` (1 hit, L634460).  Two trivial hand-fixes.
4. **`<ab n="?">` placeholders** — 0 in `pw.txt` today; the check is
   kept so any future auto-wrap pass can be re-validated.
5. **PWK-specific tag content** — `<bot>` 7,987, `<zoo>` 364, `<iw>`
   31, `<arab>` 48.  Low enough that visual review is cheap; not
   addressed by this script.
6. **Residual hyphenation** — line-break hyphens carried over from
   earlier digitisation (cf. PWG#175 item 5, ApteES thread); not
   addressed here, needs a dedicated pass.

### Usage

```sh
cd pwkissues/issue_markup_fix
python 08_markup_fix.py
# default in:  ../../../csl-orig/v02/pw/pw.txt
# default out: pw_fixed.txt

# Or on a wrapped output:
python 08_markup_fix.py pw_with_abs.txt pw_with_abs_fixed.txt
```

Synthetic-input tests of the nesting fixer and the trim fixer all
pass (`python test_markup_fix.py` — 9/9).

### What's wrong with the current markup?

Almost nothing structural.  `pw.txt` is in better shape than `pwg.txt`
on the dimensions this script measures:

- Tag-balanced (every open has a matching close).
- No nested `<ab>`.
- No whitespace-inside-tag oddities.
- No `<ab n="?">` placeholders (already filled in with German).

The five non-zero findings are:

1. 4,171 adjacent `</ab> <ab>` (review, not auto-merge).
2. 2 nested `<ls>` inside `{{ … }}` (intentional correction records).
3. 1 `{%des%}<is>Agni</is>` boundary at L96894.
4. 1 `</ls>.[Page7-363-b]` boundary at L634460.
5. 27 `<sic/>` markers (no action — informational).

### Proposed change

Land the four files under a new `pwkissues/issue_markup_fix/`
(or `pwkissues/issueNNN/` once this issue gets a number):

- `08_markup_fix.py` — the fixer + audit.
- `markup_audit.txt` — human-review list with line refs.
- `markup_fix_changes.txt` — change log (empty for the first run; this
  is the format any future re-run will populate).
- `pw_fixed.txt` — output (byte-identical to `pw.txt` for this first
  run; tracked so diffs against future runs are clean).
- `test_markup_fix.py` — synthetic-input tests (9 cases, all pass).

Fix the two singletons (L96894, L634460) by hand at the same time.

### Severity

minor — handful of entries.
