This note is a 'dev' readme.txt pertaining to changes in ls markup of pwk.
This work was done in two phases.
The first (through temp_pw_05.txt) was based primarily on the pwk version
pw_AB_L0 produced by user @Andrabharati.

The second phase (ending with temp_pw_13.txt) was based on various 'internal'
analyses.  In this phase, changes were made to both Cologne  and
Andhrabharati versions.  While the Cologne website uses only the Cologne version,
there may be further use of ideas in Andrabharati digitization, so it was felt
worth the trouble to keep the ls-markup of the two generally 'in sync'.

****************************************************************
Begin the work leading to temp_pw_05.txt
****************************************************************

See https://github.com/sanskrit-lexicon/PWK/issues/79.

Note: The notes below were originally made in a separate temporary directory.

BEGUN (10-25-2021)
ejf.

temp_pw_00.txt copy of
 /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt 
 at commit 0f1acec54fe55acaf55e3f1b2665ae10672f7a8f
 
temp_pw_AB_L0.txt from https://github.com/sanskrit-lexicon/PWK/issues/72#issuecomment-951207921
# temp_pw_AB_00.txt  unix line endings
cp temp_pw_AB_L0.txt temp_pw_AB_00.txt
 python /c/xampp/htdocs/cologne/unixify.py temp_pw_AB_00.txt
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
    
temp_pw_AB_01.txt :
cp temp_pw_AB_L0.txt temp_pw_AB_01.txt
Manually change headword in L=33744
changes 33744. 
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
 
****************************************************************
begin second phase, leading to temp_pw_13.txt and temp_pw_AB_08.txt
Note: a reference to zipped copy pw_AB_08.txt
  (which is same as temp_pw_AB_08.txt)
 is provided in comment
 https://github.com/sanskrit-lexicon/PWK/issues/79#issuecomment-977402992
****************************************************************
---------------------------------------------------------------------------
11-09-2021
pwk_ls.list.AB.txt from
   https://github.com/sanskrit-lexicon/PWK/issues/79#issuecomment-954037199
pwk_ls.list.AB_alpha.txt
  sorted alphabetically.
  
python listls.py pw temp_pw_05.txt temp_listls_pw_05.txt

python listls1.py temp_pw_05.txt temp_pwbib_input.txt temp_listls1_pw_05.txt temp_ls1_pw_05_nomatch.txt

temp_pw_06.txt
  revisions to temp_pw_05.txt
Make various changes to temp_pwbib_input.txt
python listls1.py temp_pw_06.txt temp_pwbib_input.txt temp_listls1_pw_06.txt temp_ls1_pw_06_nomatch.txt


pwbib_input_unused.txt
  Removed from temp_pwbib_input.txt.
  Boetlingk mentions as a source.
  32 items as of 11/11/2021
  
; -------------------------------------------
 cp temp_pw_06.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
 cp temp_pwbib_input.txt /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pw/pywork/pwauth/pwbib_input.txt

# change_06.txt  The changes from temp_pw_05.txt to temp_pw_06.txt
python diff_to_changes.py temp_pw_05.txt temp_pw_06.txt change_06.txt
#check:
python updateByLine.py temp_pw_05.txt change_06.txt temp.txt
diff temp_pw_06.txt temp.txt | wc -l
 # 0 (no difference)
; -------------------------------------------
python listls1_ab.py temp_pw_AB_04.txt pwk_ls.list.AB_alpha_rev.txt temp_listls1_ab_04.txt temp_ls1_ab_04_nomatch.txt
; -------------------------------------------
Now temp_pw_06.txt and pwbib_input.txt are consistent.
Similarly,
pw_ab_04.txt and pwk_ls.list.AB_alpha_rev.txt are consistent.

And pwbib_input.txt (in csl-pywork - see path above) is consistent with
pwk_ls.list.AB_alpha_rev.txt.
Both files have 842 lines.
In fact, the number of instances of the ls are also the same for pw and pw_ab:

listls1_pw_06.txt shows the frequencies for the pw version
python listls1.py temp_pw_06.txt temp_pwbib_input.txt listls1_pw_06.txt temp_pw_nomatch.txt

listls1_ab_04.txt shows the frequencies for the AB version.
python listls1_ab.py temp_pw_AB_04.txt pwk_ls.list.AB_alpha_rev.txt listls1_ab_04.txt temp_ab_nomatch.txt

When listls1_pw_06.txt and listls1_ab_04.txt are compared side by side,
there are, with one major exception, no differences.

The exception has to do with the spacing of the multiword 'ls' elements.
In general, there are spaces between words in the AB 'ls' elements,
but there are NOT spaces in the pw 'ls' elements. For example:
AB has 'AIT. UP.' while pw has 'AIT.UP.'.

The spacing of AB ls elements is preferred, as it almost always is in
better correspondence with the printed text.
[IMAGE ]


ls_spacemap.txt and ls_nochange.txt
Start with listls1_pw_06.txt
  replace ' [0-9]+$' with ' : '
  move lines with (a) no space or (b) one space at end
   into ls_nochange.txt (511 lines)
  the remaining 331 lines are in ls_spacemap.txt

Now copy the string to after the ending ': ', and add spaces to the copy
as needed
python ls_spacemap_make.py listls1_pw_06.txt ls_spacemap.txt ls_spacemap_nochange.txt
322 written to ls_spacemap.txt
520 written to ls_spacemap_nochange.txt
842 written to temp_spacemap_check.txt
  diff temp_spacemap_check.txt listls1_ab_04.txt | wc -l
  # 0   (no difference).  i.e., the spelling changes AND counts agree

## change_07
Use ls_spacemap.txt to write change transactions that will change
 temp_pw_06 into temp_pw_07
python make_spacechange.py temp_pw_06.txt ls_spacemap.txt change_07.txt
682616 lines read from temp_pw_06.txt
135787 entries found
322 read from ls_spacemap.txt
18198 records written to change_07.txt

python updateByLine.py temp_pw_06.txt change_07.txt temp_pw_07.txt

It is also necessary to introduce the spaces in pwbib_input.txt

python pwbib_update_space.py temp_pwbib_input.txt ls_spacemap.txt temp_space_change_pwbib_input.txt

python updateByLine.py temp_pwbib_input.txt temp_space_change_pwbib_input.txt temp_pwbib_input_rev.txt

# redo listls1 program with version 7 and revised pwbib
python listls1.py temp_pw_07.txt temp_pwbib_input_rev.txt listls1_pw_07.txt temp_pw_nomatch.txt

Is now identical with AB version:
diff listls1_pw_07.txt listls1_ab_04.txt | wc -l
# 0  i.e., no difference

; install version 07
 cp temp_pwbib_input_rev.txt /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pw/pywork/pwauth/pwbib_input.txt

 cp temp_pw_07.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt

; version 08:
 <ls>TS.6,4,8,2.</ls> -> <ls>TS. 6,4,8,2.</ls>
 python change_numbers.py temp_pw_07.txt 

python make_numberchange.py temp_pw_07.txt temp_pwbib_input_rev.txt change_08.txt
python updateByLine.py temp_pw_07.txt change_08.txt temp_pw_08.txt
41019 lines changed

; version 09:
<L>51594<pc>3107-1<k1>duzwaBAva
<ls>MBH. 1,152,26.3,62,15.</ls> ->
<ls>MBH. 1,152,26. 3,62,15.</ls>

<L>55724<pc>3166-1<k1>DftapUrva
<ls>MUDRĀR. 118,7.18.119,3(179,14.180,3).</ls> ->
<ls>MUDRĀR. 118,7. 18. 119,3 (179,14. 180,3).</ls>

python make_numberchange1.py temp_pw_08.txt temp_pwbib_input_rev.txt change_09.txt

python updateByLine.py temp_pw_08.txt change_09.txt temp_pw_09.txt

; ----------------------------------------
pwk_ls.list.AB_alpha_rev1.txt  and 
  changes 'zu.' to 'zu' in
<ls>CAKR. zu. SUŚR.</ls>   5 instances
<ls>DURGA. zu. NIR.</ls>  5
<ls>DURGĀDĀSA. zu. VOP.</ls> 1  (also 'DURGĀDĀSA.' -> 'DURGĀDĀSA'
<ls>ŚAṂK. zu. BĀDAR.</ls>  400

cp temp_pw_AB_04.txt  temp_pw_AB_05.txt
 and make similar changes.
 Also make addition 118 changes ' zu. ' -> ' zu '
only 380 of ŚAṂK. zu. BĀDAR. ? Why the difference from 400 for AB above?
python listls1_ab.py temp_pw_AB_05.txt pwk_ls.list.AB_alpha_rev1.txt temp_listls1_ab_05.txt temp_ls1_ab_05_nomatch.txt

; ----------------------------------------------
; version 10
temp_pw_10.txt
and temp_pwbib_input_rev1.txt
cp temp_pw_09.txt temp_pw_10.txt
cp temp_pwbib_input_rev.txt temp_pwbib_input_rev1.txt
# Manually, Similar changes regarding 'zu.'

# note: listls2_ab.py is better see below
python listls1_ab.py temp_pw_AB_05.txt pwk_ls.list.AB_alpha_rev1.txt temp_listls1_ab_05.txt temp_ls1_ab_05_nomatch.txt

python listls1.py temp_pw_10.txt temp_pwbib_input_rev1.txt listls1_pw_10.txt temp_pw_nomatch.txt

; ---------------------------------------
; version 11:
<L>65<pc>1001-3<k1>aka<k2>aka<h>2<e>100
<ls>238,6.239,3.4.</ls> ->
<ls>238,6. 239,3. 4.</ls>

A program makes initial estimate of changes.
python make_numberchange2.py temp_pw_10.txt temp_change_11.txt
 914 lines changed.
python make_nu
change_11.txt is manually edited from temp_change_11.txt.
The programmatic changes are examined individually.
For those subjectively thought suspicious, the print is consulted and
changes are altered where needed.

Similarlly, changes are made to a new copy of AB: temp_pw_AB_06.txt
cp temp_pw_AB_05.txt temp_pw_AB_06.txt.


# this examines the multiple numbers in named <ls>, evaluates the
# number coding as 'correct' or 'possibly incorrect',
and prints candidate change records for the 'possibly incorrect'.
These are examined manually, and any 'real' change records are added to
change_11.txt

change_11.txt is made from parts:
 change_11a.txt 
 change_11b.txt
cat change_11a.txt change_11b.txt > change_11.txt
 python updateByLine.py temp_pw_10.txt change_11.txt temp_pw_11.txt
  2871 changes (some lines changed more than once.)
    (2839 lines changed excluding lines changed more than once.)
The changes of change_11 are also made (where needed) to temp_pw_ab_06.txt.

; summary of ls names for pw_11 and pw_AB_06
python listls1.py temp_pw_11.txt temp_pwbib_input_rev1.txt listls1_pw_11.txt temp_pw_nomatch.txt

python listls2_ab.py temp_pw_AB_06.txt pwk_ls.list.AB_alpha_rev1.txt temp_listls2_ab_06.txt temp_ls2_ab_06_nomatch.txt


diff listls1_pw_11.txt temp_listls1_ab_06.txt
No difference!

#----------------------------------------------------------
debugging differences between listls1 and listls2_ab.


python listls1_dbg.py 'RĀJAT.' temp_pw_11.txt temp_pwbib_input_rev1.txt temp_listls1_dbg_rajat.txt
RĀJAT. occurs  391 times in 384 entries

python listls2_ab_dbg.py 'RĀJAT.' temp_pw_AB_06.txt pwk_ls.list.AB_alpha_rev1.txt temp_listls2_ab_dbg_rajat.txt
RĀJAT. occurs 392 times in 385 entries

diff temp_listls1_dbg_rajat.txt temp_listls2_ab_dbg_rajat.txt
>  1 <L>31176<pc>2104-3<k1>koSa
  So, 31176 has RĀJAT. in temp_pw_AB_06.txt but not in temp_pw_11.txt
  Which is right?
  Text at page 2104-3  (actually 2105-1) has RĀJAT.
  Add correct to change_11b.txt for temp_pw_11.txt

python listls1_dbg.py 'VP.²' temp_pw_11.txt temp_pwbib_input_rev1.txt temp_listls1_dbg_vp2.txt
VP.² occurs 543 times in 536 entries

python listls2_ab_dbg.py 'VP.²' temp_pw_AB_06.txt pwk_ls.list.AB_alpha_rev1.txt temp_listls2_ab_dbg_vp2.txt
VP.² occurs 542 times in 534 entries

diff temp_listls1_dbg_vp2.txt temp_listls2_ab_dbg_vp2.txt
<  1 <L>30614<pc>2098-2<k1>ketumAla  VP. 2,1,18. 2,22.
   change_11b.txt : pw_ab_06 ok
369d367
<  1 <L>69502<pc>4118-1<k1>pfTuDarma VP.² 4,62. 63.
   pw_11 ok.   correct pw_ab_06
382c380
<  1 <L>75872<pc>4209-3<k1>barbara  VP.² 2,341. (twice)
   one additional correction to pw_11 (change_11b)
   pw_ab_06 ok
---
>  2 <L>75872<pc>4209-3<k1>barbara
So VP.² occurs 2 extra times in pw_11 (in 30614 and 69502)
And VP.² occurs 1 extra time in pw_ab_06
START HERE <<<<<<
; --------------------------------------------------------------
Installation of temp_pw_11.txt and temp_pwbib_input_rev1.txt
cp temp_pw_11.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
cp temp_pwbib_input_rev1.txt /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pw/pywork/pwauth/pwbib_input.txt
Then in local csl-pywork/v02:
1. Regenerate pw
sh generate_dict.sh pw  ../../pw
2. Check xml valid and conforms to one.dtd
sh xmlchk_xampp.sh pw
# ok

 
python make_numberchange2b.py temp_pw_11.txt temp_pwbib_input_rev1.txt temp_change_11b.txt

temp_change11_work.txt

python edit_helper.py temp_change_11b.txt tempchange.txt temp_change_11b.txt

# for those consider
python make_numberchange2a.py temp_pw_11.txt temp_pwbib_input_rev1.txt temp_change_11a.txt

# in make_numberchange2b.py, attempt to recognize Boehtlingk's compression
# algorithm.
python make_numberchange2b.py temp_pw_11.txt temp_pwbib_input_rev1.txt temp_change_11b.txt

python diff_to_changes.py temp_pw_AB_05.txt temp_pw_AB_06.txt change_AB_06.txt
 81 changes
; ----------------------------------

listls2_ab.py

python listls2_ab.py temp_pw_AB_05.txt pwk_ls.list.AB_alpha_rev1.txt temp_listls2_ab_05.txt temp_ls2_ab_05_nomatch.txt
listls2_ab.py uses a different simpler method
  Main difference.  Suppose abbreviation X is in pwk_ls.list.AB_alpha_rev1.txt
  and we find in temp_pw_AB_05.txt  <ls>X.</ls>  Then 'X.' will show up in
  the nomatch list.
  There are 63 of these
  These need to be corrected. THESE HAVE BEEN CORRECTED. 
  We need to change <ls>X.</ls> to either
   <ls>X</ls>.  (at end of sentence)
   <ls>X</ls>   (not at end of sentence)
  The 'end of sentence' condition is somewhat vague.
  THESE corrections made in temp_pw_AB_05 (manually).

# consistency between pw_AB_05 and pw_10 and the corresponding
abbreviation files

python listls2_ab.py temp_pw_AB_05.txt pwk_ls.list.AB_alpha_rev1.txt temp_listls2_ab_05.txt temp_ls2_ab_05_nomatch.txt

python listls1.py temp_pw_10.txt temp_pwbib_input_rev1.txt listls1_pw_10.txt temp_pw_nomatch.txt

diff listls1_pw_10.txt temp_listls2_ab_05.txt | wc -l
# 0 : the files are identical as desired.

; --------------------------------------------------------------
temp_pw_12.txt  change_12.txt
cp temp_pw_11.txt temp_pw_12.txt  # initialization
# ls  with non-numeric characters in lsnum.

python make_numberchange2c.py temp_pw_12.txt temp_pwbib_input_rev1.txt temp_change_12.txt

# modify change_regex in make_change_regex.py 
python make_change_regex.py temp_pw_12.txt temp_pwbib_input_rev1.txt temp_change_regex.txt
add generated changes into change_12.txt
 python updateByLine.py temp_pw_11.txt change_12.txt temp_pw_12.txt


a. ',Z.' -> ', Z.'  52
b. lsnum1 = re.sub(r'([^ ])(fgg?[.])', r'\1 \2',lsnum)  43
c. Like: 'HEMĀDRI 2,a. 111,21.' -> 'HEMĀDRI 2,a,111,21.' 63
d. lsnum.replace(',Śl.', ', Śl.')  17

; summary of ls names for pw_12 and pw_AB_07
python listls1.py temp_pw_12.txt temp_pwbib_input_rev1.txt listls1_pw_12.txt temp_pw_nomatch.txt

python listls2_ab.py temp_pw_AB_07.txt pwk_ls.list.AB_alpha_rev1.txt temp_listls2_ab_07.txt temp_ls2_ab_07_nomatch.txt

diff listls1_pw_12.txt temp_listls2_ab_07.txt
#  no difference, as expected.

; --------------------------------------------------------------
Installation of temp_pw_12.txt and temp_pwbib_input_rev1.txt
cp temp_pw_12.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
cp temp_pwbib_input_rev1.txt /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pw/pywork/pwauth/pwbib_input.txt
Then in local csl-pywork/v02:
1. Regenerate pw
sh generate_dict.sh pw  ../../pw
2. Check xml valid and conforms to one.dtd
sh xmlchk_xampp.sh pw
# ok

; --------------------------------------------------------------
python listls1_all.py temp_pw_12.txt temp_pwbib_input_rev1.txt listls1_all_12.txt
ls instances examined by eye, and about 1000 identified to be examined for change,
 These in temporary file listls1_all_12_look.txt
python make_change_ls.py temp_pw_12.txt listls1_all_12_look.txt temp_change_13.txt
  1086 strings read; 1109 potential changes written.
  
change_13.txt examine the potential changes and keep those actually changed.

python updateByLine.py temp_pw_12.txt change_13.txt temp_pw_13.txt
  1065 change transactions.
  
Also make new revision of temp_pw_AB_07.txt manually
cp temp_pw_AB_07.txt temp_pw_AB_08.txt, and change 08 in place.
Generate changes:

python diff_to_changes.py temp_pw_AB_07.txt temp_pw_AB_08.txt change_AB_08.txt
 953 changes

; summary of ls names for pw_13 and pw_AB_08
python listls1.py temp_pw_13.txt temp_pwbib_input_rev1.txt listls1_pw_summary.txt temp_pw_nomatch.txt

python listls2_ab.py temp_pw_AB_08.txt pwk_ls.list.AB_alpha_rev1.txt temp_listls2_ab_08.txt temp_ls2_ab_07_nomatch.txt

diff listls1_pw_summary.txt temp_listls2_ab_08.txt
#  no difference, as expected.

python listls1_all.py temp_pw_13.txt temp_pwbib_input_rev1.txt listls1_pw_detail.txt
 75200 instances listed.
 
; --------------------------------------------------------------
Installation of temp_pw_13.txt and temp_pwbib_input_rev1.txt
cp temp_pw_13.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
cp temp_pwbib_input_rev1.txt /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pw/pywork/pwauth/pwbib_input.txt
Then in local csl-pywork/v02:
1. Regenerate pw
sh generate_dict.sh pw  ../../pw
2. Check xml valid and conforms to one.dtd
sh xmlchk_xampp.sh pw
# ok

; --------------------------------------------------------------
Versions of pw_AB
temp_pw_AB_L0.txt
 1. https://github.com/sanskrit-lexicon/PWK/issues/72#issuecomment-951207921
    unzip pw_AB_L0.zip
 2. mv pw_AB_L0.txt temp_pw_AB_L0.txt
temp_pw_AB_00.txt
1. cp temp_pw_AB_L0.txt temp_pw_AB_00.txt
2. python /c/xampp/htdocs/cologne/unixify.py temp_pw_AB_00.txt
temp_pw_AB_01.txt
1. # change_AB_01.txt changes L=33744 from KAditaMr to KAditar
2. python updateByLine.py temp_pw_AB_00.txt change_AB_01.txt temp_pw_AB_01.txt

temp_pw_AB_02.txt
  This is a major change of notation:  notably <x> -> <ln>x</ln>.
  There are many special cases.
  It was done in several manual steps (as indicated in notes above)
The change-file from _01 to _02 can be generated, but is quite large (22MB)
python diff_to_changes.py temp_pw_AB_01.txt temp_pw_AB_02.txt temp_change_AB_02.txt

temp_pw_AB_03.txt
 Manually created. Various small changes related to <ls> and <ln>
python diff_to_changes.py temp_pw_AB_02.txt temp_pw_AB_03.txt change_AB_03.txt
349 line changed

temp_pw_AB_04.txt
manually created. More ls changes
python diff_to_changes.py temp_pw_AB_03.txt temp_pw_AB_04.txt change_AB_04.txt
 143 lines changed

temp_pw_AB_05.txt
 manually created
 Most of these are removed superfluous periods at end of <ls>, e.g.
OLD:  '<ls>HEMĀDRI.</ls> <ln>1,127,23.</ln>'
NEW:  '<ls>HEMĀDRI</ls> <ln>1,127,23.</ln>'
The period is absent since this is an un-abbreviated proper name.

python diff_to_changes.py temp_pw_AB_04.txt temp_pw_AB_05.txt change_AB_05.txt
2405 lines changed.
55782 new <L>13867<pc>1164-1<k1>Ajarjarita<k2>Ajarjarita<e>100

extra blank line at 497012

python diff_to_changes.py temp_pw_AB_05.txt temp_pw_AB_06.txt change_AB_06.txt
 991 changes

python diff_to_changes.py temp_pw_AB_06.txt temp_pw_AB_07.txt change_AB_07.txt
 606 changes
 
