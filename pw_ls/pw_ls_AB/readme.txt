Corrections to PW based on version pw_AB_L0 produced by user @Andrabharati.

See https://github.com/sanskrit-lexicon/PWK/issues/79.

Note: The notes below were originally made in a separate temporary directory.

BEGUN (10-25-2021)
ejf.

temp_pw_00.txt copy of
 /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt 
 at commit 0f1acec54fe55acaf55e3f1b2665ae10672f7a8f
 
temp_pw_AB_L0.txt from https://github.com/sanskrit-lexicon/PWK/issues/72#issuecomment-951207921  
 NOTE: I also changed from Windows line-endings to Unix line endings.
 python /c/xampp/htdocs/cologne/unixify.py temp_pw_AB_L0.txt
Features noted: (Use pw00 and pwAB as abbreviations for file names)
pw00 has 682619 lines
pwAB has 553739 lines

$ grep '^<L>' temp_pw_00.txt | wc -l
135788

$ grep '^<L>' temp_pw_AB_L0.txt | wc -l
135787
Note (* 135787 4) = 543148 (4 lines per entry). And 
  (- 553739 543148) = 10591.  So 
So, the number of entries differs only by (1)

Metalines:  Appear to be untouched in pwAB.
grep '^<L>' temp_pw_00.txt > temp_pw_00_metalines.txt
grep '^<L>' temp_pw_AB_L0.txt > temp_pw_AB_L0_metalines.txt
diff temp_pw_00_metalines.txt temp_pw_AB_L0_metalines.txt | wc -l
  Examine differences:
diff temp_pw_00_metalines.txt temp_pw_AB_L0_metalines.txt
17194d17193
< <L>17194<pc>1207-3<k1>imAn<k2>imA/n<e>107
33744c33743
< <L>33744<pc>2140-1<k1>KAditar<k2>KAditar<e>100
---
> <L>33744<pc>2140-1<k1>KAditaMr<k2>KAditaMr<e>100

(1) entry '17194 imAn' is in pw00 but not pwAB
   PWAB has note: ";<L>17194 merged with the prev. entry." (L=17193, ima)
   NOTE: pw00 to be changed by merging 17194 into 17193.
(2) In entry 33744, pw00 spelling is KAditar and pwAB spelling is KAditaMr.
    Based on scan,  KAditar is correct.
    NOTE: pwAB to be changed.

temp_pw_01.txt merges 17194 into 17193.
 installed in csl-orig as pw.txt at commit
    62991ae1e64b117291792cb808ee1fb021201e8f
    
temp_pw_AB_01.txt changes 33744. (?)
-----------------------------------------------------------------------
temp_pw_02.txt  Corrections from https://github.com/sanskrit-lexicon/PWK/issues/72.
 installed in csl-orig as pw.txt at commit
    66fa46b5cf25343c626c8026546ea5f1cf64b439.

Now temp_pw_AB_01.txt and temp_pw_02.txt have same metalines:
grep '^<L>' temp_pw_02.txt > temp_pw_02_metalines.txt
grep '^<L>' temp_pw_AB_01.txt > temp_pw_AB_01_metalines.txt
diff temp_pw_02_metalines.txt temp_pw_AB_01_metalines.txt | wc -l
 >> 0 differences

-----------------------------------------------------------------------
temp_pw_AB_02.txt
 Revise temp_pw_AB_01 by adding
 <\([0-9].*?\)> → <ln>\1</ln>    <Dxxx> -> <ln>Dxxx</ln>  D a digit
 <\(S[.] .*?\)> → <ln>\1</ln>    <S. x> -> <ln>S. x</ln>
 <\(Einl.*?\)> → <ln>\1</ln>     <Einlx> -> <ln>Einlx</ln>  (13)
 <\(No.*?\)> → <ln>\1</ln>     <Nox> -> <ln>Nox</ln>  (403)
   NOTE: There are some additional '<ln>' markup discovered later
   and there are several 'manual' changes made and noted in this AB_02.
See diff_AB_02.txt for the changes I made to temp_pw_AB_02.txt in the
course of developing changes_04.txt.
-----------------------------------------------------------------------
ls markup.
pwAB uses <ls>X</ls> <N1,N2> form -- i.e., the name of the literary source
is within <ls> tag,  and the chapter, verse, etc. (if any) are in a
following un-named <> tag.

Example:
pwAB: <ls>BHĀG. P.</ls> <ls>ŚIŚ.</ls> <15,33>
pw01: <ls>BHĀG.P.</ls> <ls>ŚIŚ.15,33</ls>
 Note also the differences in  spacing.

In pwAB, there can also be ones of the <15,33> type NOT preceded by an <ls>.

Let's do a sequential listing of all these in pwAB and pw01

cp ../../AP90/ap57_verbs01/parseheadline.py .  # parser helper


python listls.py pw temp_pw_02.txt listls_pw_02.txt
python listls.py ab temp_pw_AB_02.txt listls_ab_02.txt
python listls.py ab1 temp_pw_AB_02.txt listls_ab1_02.txt
  listls_pw_02.txt and listls_ab1_02.txt should be comparable.
  diff listls_pw_02.txt listls_ab1_02.txt | wc -l
    18744 : So roughly 18744/4 or 5000 differences.
  diff listls_pw_02.txt listls_ab1_01.txt > tempdiff_listls_pw02_ab101.txt
  
temp_pw_03.txt
 Altered from temp_pw_02.txt:
 ',Sch.</ls>' -> '</ls>, <ab>Sch.</ab>'  (184)
 '.Sch.</ls>' -> '.</ls> <ab>Sch.</ab>'  (2)
 '<ls>Sch.</ls>' -> '<ab>Sch.</ab>'  (24)
    NOTE: Sch. now removed from pwbib_input.txt.
 ' </ls> ' -> '</ls> ' (4)
 ' </ls>' -> '</ls> ' (5)
 '<ls>VĀMANA.</ls>' -> '<ls>VĀMANA</ls>.' (8)
 '<ls>VĀMANA.' -> '<ls>VĀMANA '  
    next character is either a digit or S (2)
 '<ls>ebend.</ls>' -> '<ab>ebend.</ab>' (400) ibid.
 '<ls>ebend.' -> '<ab>ebend.</ab> <ls>' (47)
 '<ls>VP.².' -> 'VP.²'  (443)

',</ls>' -> '</ls>,'  (844) ?? REVERT THIS

cp temp_pw_03.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
  temp_pw_03.txt is now (10-26-2021) the same as csl-orig pw.txt at commit
  4222d80e56137d5067e477bd8b351e78f75b513e

python listls.py pw temp_pw_03.txt listls_pw_03.txt
python listls.py ab1 temp_pw_AB_02.txt listls_ab1_02.txt
  diff listls_pw_03.txt listls_ab1_02.txt | wc -l
    14100 Fewer, as expected
  diff listls_pw_03.txt listls_ab1_02.txt > tempdiff_listls_pw03_ab102.txt

# temp_pw_04.txt
# diffls
python diffls.py temp_pw_03.txt temp_pw_AB_02.txt temp_diffls.txt
135787 entries found
2017 entries have different ls

# change_04.txt  got  by editing temp_diffls.txt
# Note numerous changes also made to temp_pw_AB_02.txt
python updateByLine.py temp_pw_03.txt change_04.txt temp_pw_04.txt
 600 changes
# rerun diffls with pw_04
python diffls.py temp_pw_04.txt temp_pw_AB_02.txt temp_diffls_04.txt
 1413 entries have different ls

cp temp_pw_04.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
Installed this as commit 32e0d45258148939c5e82e0d32b9028b1e69ca0b of pw.txt.

# -------------------------------------------------------------
change_05
 Applied to temp_pw_04
 comparing to temp_pw_AB_03.txt, which starts as copy of temp_pw_AB_02.txt
python updateByLine.py temp_pw_04.txt change_05.txt temp_pw_05.txt

cp temp_pw_05.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt


# diffls1: entries where no ls in pw, but with ls in AB
python diffls1.py temp_pw_04.txt temp_pw_AB_03.txt temp_diffls1_05.txt
 temp_diffls1_05 feeds into change_05.  85 entries to examine

python diffls1.py temp_pw_05.txt temp_pw_AB_03.txt temp_diffls1_05-rev.txt
  0 
python diffls.py temp_pw_05.txt temp_pw_AB_03.txt temp_diffls_05_03.txt
 1 remains with #ls in pw == 1
 
# diffls2:  1 pw ls in entry
python diffls2.py temp_pw_05.txt temp_pw_AB_03.txt temp_diffls2_05_03.txt
  feed these into change_05

# diffls3:  2 pw ls in entry
python diffls3.py temp_pw_05.txt temp_pw_AB_03.txt temp_diffls3_05_03.txt
  feed these into change_05
Some of these are OK by assertion  (i.e., the comparison logic is known to
show a difference, but that difference is not material)
python diffls3.py temp_pw_05.txt temp_pw_AB_03.txt temp_diffls3_05_03-rev.txt

# diffls4:  all remaining differences
python diffls4.py temp_pw_05.txt temp_pw_AB_03.txt temp_diffls4_05_03.txt
# diffls4a simplifies the comparisons
python diffls4a.py temp_pw_05.txt temp_pw_AB_03.txt temp_diffls4a_05_03.txt
# diffls4bthis is attempt to print fewer lines,
python diffls4b.py temp_pw_05.txt temp_pw_AB_03.txt temp_diffls4b_05_03.txt
  feed these into change_05
Some of these are OK by assertion  (i.e., the comparison logic is known to
show a difference, but that difference is not material)
python diffls4b.py temp_pw_05.txt temp_pw_AB_03.txt temp_diffls4b_05_03-rev.txt


# -------------------------------------------------------------
# revisions to pwab_input.txt
xxcp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pw/pywork/pwab/pwab_input.txt temp_pwab_input.txt
#Revise temp_pwab_input.txt, then copy back
cp temp_pwab_input.txt /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pw/pywork/pwab/pwab_input.txt

# revisions to pwbib_input.txt

xxcp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pw/pywork/pwauth/pwbib_input.txt temp_pwbib_input.txt
Revise temp_pwbib_input.txt, then copy back
cp temp_pwbib_input.txt /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pw/pywork/pwauth/pwbib_input.txt
 
