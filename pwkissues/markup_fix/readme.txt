PWK markup-fixer drop, counterpart of PWG/pwgissues/issue174/08_markup_fix.py
(see https://github.com/sanskrit-lexicon/PWG/issues/175).

Files
-----
  08_markup_fix.py        the fixer + audit, runnable against pw.txt
  test_markup_fix.py      synthetic-input tests of the fix functions
  markup_audit.txt        human-review list produced by the run on pw.txt
  markup_fix_changes.txt  change log (updateByLine format) — empty for
                          the current pw.txt because no auto-fixes were
                          needed; the file is the template for any
                          re-run after a wrap/overlay pass introduces
                          something to fix
  pw_fixed.txt            output file (byte-identical to pw.txt for the
                          current run; tracked so future diffs are clean)
  comment_markup_fix.md   draft of the GitHub opening-issue comment

Run
---
From `pwkissues/<this-folder>/`:

  python 08_markup_fix.py
  python test_markup_fix.py

Defaults assume the CDSL layout where `csl-orig/` is a sibling of `PWK/`:
  PWK/pwkissues/<this-folder>/08_markup_fix.py
  csl-orig/v02/pw/pw.txt

If pw.txt sits beside the script, it is picked up there too.
