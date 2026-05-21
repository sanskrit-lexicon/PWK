"""Synthetic-input tests for 08_markup_fix.py.

Verifies the fixer behaves correctly on cases we DON'T have in pw.txt
today but could be introduced by a later wrap / overlay pass.
"""

import sys
import importlib.util
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("mfix", HERE / "08_markup_fix.py")
mfix = importlib.util.module_from_spec(spec)
# Skip running main() — we only want the functions
import types
mfix.__name__ = "mfix"
sys.modules["mfix"] = mfix
# load just the function definitions; main() is gated under __name__ == "__main__"
spec.loader.exec_module(mfix)

cases = [
    # 1. nested with strict prefix
    ("<ab><ab>vor.</ab> W.</ab>", "<ab>vor. W.</ab>"),
    # 2. degenerate exact-duplicate
    ('<ab n="x"><ab>St.</ab></ab>', '<ab n="x">St.</ab>'),
    # 3. inner covers prefix+suffix
    ("<ab>foo<ab>bar</ab>baz</ab>", "<ab>foobarbaz</ab>"),
    # 4. no nesting — unchanged
    ("<ab>N. pr.</ab> <ab>u. s. w.</ab>", "<ab>N. pr.</ab> <ab>u. s. w.</ab>"),
    # 5. whitespace trim ls
    ("<ls> GORR. 1,69,9 </ls>", "<ls>GORR. 1,69,9</ls>"),
    # 6. whitespace trim bot
    ("<bot> Musa sapientum </bot>", "<bot>Musa sapientum</bot>"),
    # 7. whitespace trim hom
    ("<hom> 1. </hom>", "<hom>1.</hom>"),
    # 8. whitespace trim iw
    ("<iw> Hussein </iw>", "<iw>Hussein</iw>"),
    # 9. attribute preserved
    ('<lang n="greek"> ἀ</lang>', '<lang n="greek">ἀ</lang>'),
]

ok = 0
fail = 0
for src, want in cases:
    line, _ = mfix.fix_nested_ab(src)
    line, _ = mfix.fix_trim_whitespace(line)
    if line == want:
        ok += 1
        print(f"  PASS  {src!r}  →  {line!r}")
    else:
        fail += 1
        print(f"  FAIL  {src!r}")
        print(f"        got:  {line!r}")
        print(f"        want: {want!r}")

print(f"\n{ok} passed, {fail} failed")
sys.exit(0 if fail == 0 else 1)
