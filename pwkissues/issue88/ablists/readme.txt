2023-08-11
Downloaded from https://github.com/sanskrit-lexicon/PWK/issues/88#issuecomment-1662350962

globals are in the form <ab>X</ab>
locals are in the form <ab n="TIP">X</ab>

global.abbr.pwk.txt  list of global abbreviations from Andhrabharati.

----------------------------------------------
# comparison of <ab>X</ab> 

python ab_glob0.py ../temp_pw_0.txt ../temp_pw_ab_1.txt ../pwab_input_0.txt ab_glob0.txt
62 distinct <ab>X</ab> from ../temp_pw_0.txt
295 distinct <ab>X</ab> from ../temp_pw_ab_1.txt
64 read from ../pwab_input_0.txt
64 tips read from ../pwab_input_0.txt
312 lines written to ab_glob0.txt

Format of ab_glob0.txt by examples:
3.	0,25	?
 instances of '<ab>3.</ab>'.
 0 instances in temp_pw_0
 25 instances in temp_pw_ab_1
 ? means '3.' is not in the abbreviation tooltip file
Abl.	1367,1375	Ablativ - ablative (case)
 instances of '<ab>Abl.</ab>'
 1367 instances in temp_pw_0
 1375 instances in temp_pw_ab_1
 'Abl.' is in the abbreviation tooltip file,
    with tooltip 'Ablativ - ablative (case)'
    
----------------------------------------------------------------
# Begin work to
a. reconcile differences between cdsl and ab versions re <ab>X</ab>
b. revise pwab_input.txt

We will be revising the cdsl digitization. Start with a copy:
cp ../temp_pw_0.txt ../temp_pw_1.txt

It may be convenient to iterate tooltips by revising ab_glob1.txt
cp ab_glob0.txt ab_glob1.txt
# ab_glob1.py reads format of ab_globX.txt rather than pwab_input.xt
# When all is resolved, we can construct pwab_input_new.txt 

# start by redoing the first step:
python ab_glob1.py ../temp_pw_1.txt ../temp_pw_ab_1.txt ab_glob0.txt temp_ab_glob1.txt
As a check, ab_glob0.txt is the same as temp_ab_glob1.txt
----------------------------------------------------------------
# spaces in abbrev
9 cases where cdsl uses 'XY' and ab uses 'X Y' for abbreviation
See change_pw_1_notes.txt : temp_change_1.txt

python make_change.py '1a' ../temp_pw_0.txt temp_change_1ax.txt
30899 changes in 26383 entries
python updateByLine.py ../temp_pw_0.txt temp_change_1a.txt ../temp_pw_1.txt
30899 lines changed

# Revise ab_glob1 manual
# redo ab_glob1
python ab_glob1.py ../temp_pw_1.txt ../temp_pw_ab_1.txt ab_glob1.txt temp_ab_glob1.txt

python pre_change1b.py ../temp_pw_1.txt ab_glob1.txt temp_pre_change1b.txt
# This writes replacements for 149 items from glob1 where
# (a) there are 0 cdsl instances of <ab>X</ab>
# (b) And, there N ab marked instances <ab>X</ab>
# (c) And, there are N unmarked instances of X
Thus, the change X -> <ab>X</ab> can be applied to temp_pw_1 to get
the same number of instances in temp_pw_ab_1.
This list of 149 is put into change_1b of make_change.py

python make_change.py '1b' ../temp_pw_1.txt temp_change_1b.txt
 (1837 changes in 1618 entries)

python updateByLine.py ../temp_pw_1.txt temp_change_1b.txt ../temp_pw_1.txt
1837 changes

# redo ab_glob1
python ab_glob1.py ../temp_pw_1.txt ../temp_pw_ab_1.txt ab_glob1.txt ab_glob1.txt
o
----------------------------------------
python pre_change1c.py ../temp_pw_1.txt ab_glob1.txt temp_pre_change1c.txt

# This writes replacements for 39 items from glob1 where
# (a) there are 0 cdsl instances of <ab>X</ab>
# (b) And, there N ab marked instances <ab>X</ab>
# (c) And, there are M unmarked instances of X
and abs(N-M) < 5.
Thus, the change X -> <ab>X</ab> can be applied to temp_pw_1 to get
ALMOST the same number of instances in temp_pw_ab_1.
This list of 39 is put into change_1c of make_change.py

python make_change.py '1c' ../temp_pw_1.txt temp_change_1c.txt
 (1721 changes in 1502 entries)

python updateByLine.py ../temp_pw_1.txt temp_change_1c.txt ../temp_pw_1.txt
1721 changes

# redo ab_glob1
python ab_glob1.py ../temp_pw_1.txt ../temp_pw_ab_1.txt ab_glob1.txt ab_glob1.txt
temp_change_1c.txt  (1741 changes in 1516 entries)

python temp_change1c1.py ../temp_pw_1.txt ab_glob1.txt temp_pre_change1c1.txt


----------------------------------------
python make_change.py '1d' ../temp_pw_1.txt temp_change_1d.txt
(12684 changes in 10984 entries)

python updateByLine.py ../temp_pw_1.txt temp_change_1d.txt ../temp_pw_1.txt
12684 of type new

# redo ab_glob1
python ab_glob1.py ../temp_pw_1.txt ../temp_pw_ab_1.txt ab_glob1.txt ab_glob1.txt
303 lines 

<lex>X</lex>
python lex_glob0.py ../temp_pw_1.txt ../temp_pw_ab_1.txt lex_glob0.txt
10 distinct <lex>X</lex> from ../temp_pw_1.txt
674189 lines from ../temp_pw_ab_1.txt
11 distinct <lex>X</lex> from ../temp_pw_ab_1.txt
11 lines written to lex_glob0.txt

======================================================
There are still several unresolved differences in ab or lex markup
between pw_1 and pw_ab_1.  We switch techniques to
identify these.  There are also differences in number of headwords.
We address that also.
======================================================
# modified from /c/xampp/htdocs/sanskrit-lexicon/BHS/issues/issue3/compare/compare_texts.py

We start with copies of the two digitizations:
cp ../temp_pw_1.txt ../temp_pw_2.txt
cp ../temp_pw_ab_1.txt ../temp_pw_ab_2.txt

Ref: change_2_notes.txt

python compare_texts.py ../temp_pw_2.txt ../temp_pw_ab_2.txt temp.txt
1441 cases written to temp.txt
1364 cases written to temp.txt
1243 cases written to temp.txt
1196 cases written to temp.txt
1088 cases written to temp.txt
--- 08-28-2023



======================================================

suggest changes to temp_pw_ab_1.txt

<L>91175<pc>5148-2<k1>yuva<k2>yuva<h>1<e>000
<hom>1.</hom> {#yuva#}¦ <ab>Pron.</ab> <ab>s. u.</ab> <hom>1.</hom> {#yu#} 1〉.
  <lex>Pron.</lex>

L>78979   replace TAB with space
-----
* <L>95087<pc>5206-1<k1>romASrayakalA<k2>*romASrayakalA<e>100
PalA  (both versions) 

Tabs after broken bar. ?

-----
<L>29427<pc>2084-3<k1>kuSabindu
m. Pl. pr. -> m. Pl. N. pr.    (print change ?)
-----
<L>31283<pc>2106-2<k1>kOYcikI
Bz. -> Bez. PC = print change
-----
* <L>43244<pc>2273-3<k1>jEna
m. pr -> m. N. pr. PC?
-----
<L>57038<pc>3184-3<k1>nalina
<bot n="Nelumbium speciosum">N. sp.</bot>
-----
<L>58054<pc>3198-1<k1>nArmada
<is n="Narmadā">N.</is>
-----
<L>109229<pc>6191-2<k1>SakawAra<k2>SakawAra<e>100
{#SakawAra#}¦ <lex>m.</lex> <ab>N. pr.</ab>  text has m. pr. print change?
---
<L>131955<pc>7230-3<k1>sva
seine <sic/> Zuflucht
-----
odd forms
(<ls><ab>ebend.</ab></ls>)
<bot n="Bassia latifolia"
fgg.  mark as <ab>
;%}  why not outside?
;; comments  (e.g. 89275)
¦<TAB>
dass.  When is it an abbreviation?

--------------------------------------
temp.org
change_2_notes.txt
temp_pw_2_version3.txt
temp_pw_ab_2_version3.txt

<ab>trans.</ab>


python compare_texts.py temp_pw_2_version3.txt temp_pw_ab_2_version3.txt temp1.org
56
python compare_texts.py temp_pw_2_version3.txt temp_pw_ab_2_version3.txt temp2.org
17
python compare_texts.py temp_pw_2_version3.txt temp_pw_ab_2_version3.txt temp3.org
8
python compare_texts.py temp_pw_2_version3.txt temp_pw_ab_2_version3.txt temp4.org
3
python compare_texts.py temp_pw_2_version3.txt temp_pw_ab_2_version3.txt temp5.org
3
python compare_texts.py temp_pw_2_version3.txt temp_pw_ab_2_version3.txt temp6.org
1
python compare_texts.py temp_pw_2_version3.txt temp_pw_ab_2_version3.txt temp7.org
0 cases written to temp7.org  FINALLY!

# confirm counts are same for all abbreviations:
python ab_glob1.py ../temp_pw_2.txt ../temp_pw_ab_2.txt ab_glob1.txt ab_glob2.txt

-------------------------------------------------------------
check validity of temp_pw_2

cp temp_pw_2_version3.txt ../temp_pw_2.txt
cd ../
sh redo_prod.sh 2
# ok validated

sh redo_dev.sh ab_2
************************************************************
08-31-2023
local abbreviations: <ab T>X</ab>
***********************************************************
python ab_local1.py ../temp_pw_2.txt ../temp_pw_ab_2.txt ab_local1.txt
65 distinct <ab []>X</ab> from ../temp_pw_2.txt
580 distinct <ab []>X</ab> from ../temp_pw_ab_2.txt
583 lines written to ab_local1.txt
527 differences in local abbreviations
241 distinct abbreviations

Now we need to make changes to resolve the differences.
python compare_local_ab.py ../temp_pw_2.txt ../temp_pw_ab_2.txt temp.txt

cp ../temp_pw_ab_2.txt temp_pw_ab_2_version4.txt

python compare_local_ab.py temp_pw_2_version4.txt temp_pw_ab_2_version4.txt temp.txt
temp_pw_ab_2_version4.txt changed manually for 'u.' (unter/und) local abbrevs.

python ../diff_to_changes_dict.py ../temp_pw_2.txt temp_pw_2_version4.txt temp_change_3a.txt
148 changes written to temp_change_3a.txt

python ../updateByLine.py ../temp_pw_2.txt temp_change_3a.txt temp_pw_3_version1.txt
148 change transactions from temp_change_3a.txt
diff temp_pw_2_version4.txt temp_pw_3_version1.txt
 NO DIFFERENCE.  We will have no further use for temp_pw_2_version4.txt

------------------
temp_change_3b.txt
python change_3b.py temp_pw_3_version1.txt temp_pw_ab_2_version4.txt  temp_change_3b.txt
382 changes written to temp_change_3b.txt

# apply to get temp_pw_3_version2.txt

python ../updateByLine.py temp_pw_3_version1.txt temp_change_3b.txt temp_pw_3_version2.txt
382 of type new

------------------
temp_pw_3_version3.txt

python ab_local1.py temp_pw_3_version2.txt ../temp_pw_ab_2.txt temp_ab_local1_version2.txt
246 differences in local abbreviations
241 distinct abbreviations

We must resolve the remaining differences manually.
cp temp_pw_3_version2.txt temp_pw_3_version3.txt
edit temp_pw_3_version3.txt

python premark_work.py temp_pw_3_version2.txt temp1.org temp_pw_3_version3_work.txt
python premark_work.py temp_pw_ab_2_version4.txt temp1.org temp_pw_ab_2_version4_work.txt


python compare_local_ab_work.py temp_pw_3_version2.txt temp_pw_ab_2_version4.txt temp_pw_3_version2_work1.txt temp_pw_ab_2_version4_work.txt
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Two additional changes from
  https://github.com/sanskrit-lexicon/PWK/files/12500349/change_pw_ab_2.AB.txt
----------------------------

python ../diff_to_changes_dict.py temp_pw_3_version2.txt temp_pw_3_version3.txt temp_change_3c.txt
272 changes written to temp_change_3c.txt


-----------------------------------------------------------------------
Still some unresolved differences in local abbreviations

cp temp_pw_3_version3.txt temp_pw_3_version4.txt
# reuse temp_pw_ab_2_version4.txt

python ab_local1.py temp_pw_3_version4.txt temp_pw_ab_2_version4.txt temp_ab_local1_version4.txt

python compare_local_ab.py temp_pw_3_version4.txt temp_pw_ab_2_version4.txt temp1.org

30 differences in local abbreviations
manual changes.
Rerun.
python compare_local_ab.py temp_pw_3_version4.txt temp_pw_ab_2_version4.txt temp1.org
Iterate until there are no differences.

python ../diff_to_changes_dict.py temp_pw_3_version3.txt temp_pw_3_version4.txt temp_change_3d.txt
31 changes written to temp_change_3d.txt

---------------------------------------------------
Aggregate all the temp_change_3X.txt into ../change_3.txt

touch ../change_3.txt
Insert temp_change_3a.txt into ../change_3.txt
insert temp_change_3b.txt
insert temp_change_3c.txt
insert temp_change_3d.txt
cd ../
python updateByLine.py temp_pw_2.txt change_3.txt temp_pw_3a.txt
835 lines changed
--------------------------------
cp temp_pw_ab_2_version4.txt ../temp_pw_ab_3a.txt
cd ../
python diff_to_changes_dict.py temp_pw_ab_2.txt temp_pw_ab_3a.txt change_pw_ab_3.txt

Proof that these latest versions have the same local abbreviations.
python ab_local1.py ../temp_pw_3.txt ../temp_pw_ab_3a.txt ab_local1_version3.txt
580 distinct <ab []>X</ab> from ../temp_pw_3.txt
580 distinct <ab []>X</ab> from ../temp_pw_ab_3.txt
580 lines written to ab_local1_version3.txt
0 differences in local abbreviations

************************************************************

--------------------------------
https://github.com/sanskrit-lexicon/PWK/files/12500349/change_pw_ab_2.AB.txt

475926 old [Fußnote: *Wäre bis auf das {#la#} ein regelmässiges Imperfect von {#ay#}, {#ayate#} mit {#nis#}.]
475926 new <FN>*⁾Wäre bis auf das {#la#} ein regelmässige Imperfect von {#ay#}, {#ayate#} mit {#nis#}.</FN>
;; AB note. This is to be relocated from 475944 to 475926. And, as in other CDSL works, <FN> is used for footnote tagging on either side of it; no need to devise another format "[Fußnote: xxx]".
;; And Jim might revert the *⁾ to *) as he he had done in GRA recently.

; Jim note: use <F>...</F> instead of <FN>...</FN>
There are NO <FN> tags.  But there is an <F> tag.
Based on make_xml.py,  this <F> tag is present for these dictionaries:
  krm, skd, inm, bop.
  And it is handled differently in all cases.
revised form for AB:
<F>*⁾Wäre bis auf das {#la#} ein regelmässige Imperfect von {#ay#}, {#ayate#} mit {#nis#}.</F>


************************************************************
09-04-2023
temp_pw_ab_4.txt and temp_pw_4.txt
cd ../
cp temp_pw_ab_3.txt temp_pw_ab_4.txt
cp temp_pw_3.txt temp_pw_4.txt

Ref: https://github.com/sanskrit-lexicon/PWK/issues/88#issuecomment-1704004332

--------------------------------
<L>9297<pc>1108-3<k1>arkASvameDa
<is n="Arka">A.</is>  and similar.  Print code must handle
  this as a local abbreviation (i.e. provide a tooltip)
---
0,1	a. u.=???	`<ab n="???">a. u.</ab> ;; could this be "u. a." instead?`
  a. u. not changed
+ 0,3	Chr.=???	`<ab n="nach">n.</ab> <ab n="???">Chr.</ab> ;; <ab n="nach Christus">n. Chr.</ab>`
+ 3,3	N. N.=???	`<ab n="???">N. N.</ab> ;; <ab n="Nomen Nescio">N. N.</ab>`
+ 0,2	NO=???	`<ab n="???">NO</ab> ;; <ab n="Nord-Ost">NO</ab>`
+ 0,1	NW=???	`<ab n="???">NW</ab> ;; <ab n="Nord-West">NW</ab>`
+ 0,1	SO=???	`<ab n="???">SO</ab> ;; <ab n="Süd-Ost">SO</ab>`
+ 0,1	SW=???	`<ab n="???">SW</ab> ;; <ab n="Süd-West">SW</ab>`
+ 0,1	u.=???	`<ab n="???">u.</ab> ;; <ab n="unterthan">u.</ab>`

'>{' -> '> {'  3 in pw_ab_, 12 in pw_
'}<' -> '} <'  1 in pw_ab_, 16 in pw_
=============================
 
python diff_to_changes_dict.py temp_pw_3.txt temp_pw_4.txt temp_change_4.txt
36 changes written to temp_change_4.txt

touch change_pw_4.txt
insert temp_change_4.txt

python diff_to_changes_dict.py temp_pw_ab_3.txt temp_pw_ab_4.txt temp_change_ab_4.txt
12 changes written to temp_change_ab_4.txt
touch change_pw_ab_4.txt
insert temp_change_ab_4.txt
******************************************************
Inline display of local abbreviations
 change to basicadjust.php in csl-websanlexicon:
 This done in dev4_tm version.
 diff /c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue88/dev4_tm/web/webtc/basicadjust.php
851a852
>   |<ab(.*?)>(.*?)</ab>|
860c861,868
<   $ans = $x;
---
>   $ans = $x; // local abbreviation
>   // for pwk, prepare for displaying the tooltip without the abbreviation
>   if (in_array($this->dict,array('pwg','pw','pwkvn'))) {
>    $tip = $matches1[1];
>    $style = "color:blue;";
>    $tipa = "@$tip";  // for debugging
>    $ans = "<span style='$style'>$tipa</span>";
>   }
 
******************************************************
09-04-2023
python ab_local_tm.py ../temp_pw_4.txt ab_local_tm_0.txt
843 entries contain a local abbreviation
******************************************************
09-09-2023
User corrections to pw.  20 lines changed
These are reflected in ../change_pw_4.txt and change_pw_ab_4.txt.
See also user_change_notes.txt and user_change_notes_ab.txt
******************************************************
09-18-2023
ab_local_tm_0_corr.txt  received from Thomas.
 See also ab_local_tm_corr_note.txt
----------------------
Jim changes
----------------------
----
 4 errors corrected
----
change 'N. N.' to a global abbreviation 
 <ab n="Nomen Nescio">N. N.</ab> -> <ab>N. N.</ab>   (3 cases)
 Add global abbreviation in csl-pywork/...pwab_input.txt.
----
<ab n="Person">P.</ab> -> <ab>P.</ab>  (5 cases)
Add global abbreviation 
----
<ab n="nach Christus">n. Chr.</ab> -> <ab>n. Chr.</ab> (3)
Global abbrev pwab_input
tooltip = nach Christus - after Christ

----------------------
Jim questions for Thomas
----------------------
---- TODO  done
case 141 sic! ??
---- TODO
<ab n="???">a. u.</ab>
; case 135 ??"ab usu" = "as usual" or "ad usum" = "for the use" 2 occurrences in pw, 0 in pwg
---- TODO 
<ab n="medicinischem">med.</ab> -> <ab>med.</ab>  ?
  <ab n="medicinischen">med.</ab> (13)
13 matches for "<ab n="medicinischen">med.</ab>"
2 matches for "<ab n="medicinischem">med.</ab>" in buffer: ab_local_tm_0_corr.txt
4 matches for "<ab n="medicinisches">med.</ab>" in buffer: ab_local_tm_0_corr.txt
---- TODO done
case 339
-----
Case 404
Jmd is abbreviation of Jemand 'someone, somebody' Jmdes Jmden
----
; case 605 dto. Adj.  what does 'dto' mean?
---- TODO ?
; case 738 <is>R</is>.abbr for  [Nakshatra] Revati1
---- TODO
; case 842 abbr. 'H.' seems to be  some source (Hemacandra's Abhidanacintamani 468 in pwg): "according to H." -> hikkA 'Schluchzer' = a single sob (sobbing) or rather hiccup (in pwg) singultus [singulus to be corrected in pwg]

------
end of Jim questions for Thomas
----------------------

----------------------
# Generate change file ../change_pw_5.txt
----------------------

python ab_local_tm_process.py ab_local_tm_0.txt ab_local_tm_0_corr.txt ../temp_pw_4.txt ../change_pw_5.txt
843 cases from ab_local_tm_0.txt
843 cases from ab_local_tm_0_corr.txt
111 lines to change from 107 cases
682608 lines read from ../temp_pw_4.txt
135771 entries found
112 Change records
112 cases written to ../change_pw_5.txt

##

cd ../
python updateByLine.py temp_pw_4.txt change_pw_5.txt temp_pw_5.txt

******************************************************
temp_pw_ab_5.txt
cp ../temp_pw_ab_4.txt ../temp_pw_ab_5_work.txt
  Manually apply chanage_pw_5.txt to temp_pw_ab_5_work.txt

python diff_to_changes_dict.py temp_pw_ab_4.txt temp_pw_ab_5_work.txt change_pw_ab_5.txt
109 changes written to change_pw_ab_5.txt

python updateByLine.py temp_pw_ab_4.txt change_pw_ab_5.txt temp_pw_ab_5.txt
674189 lines read from temp_pw_ab_4.txt
674189 records written to temp_pw_ab_5.txt
110 change transactions from change_pw_ab_5.txt
110 of type new

# compare <ab>X</ab>
python compare_texts.py ../temp_pw_5.txt ../temp_pw_ab_5.txt temp.txt
0 cases written
temp_pw_5.txt and temp_pw_ab_5.txt agree

# compare <ab n="TIP">X</ab>
python compare_local_ab.py ../temp_pw_5.txt ../temp_pw_ab_5.txt temp.txt
0 cases written
temp_pw_5.txt and temp_pw_ab_5.txt agree

These need to be added to pwab_input_1.txt.

 
# ab_glob5.txt
 Frequency count of global abbreviations, along with current tooltips.
python ab_glob0.py ../temp_pw_5.txt ../temp_pw_ab_5.txt ../pwab_input_1.txt ab_glob5.txt
299 distinct <ab>X</ab> from ../temp_pw_5.txt
299 distinct <ab>X</ab> from ../temp_pw_ab_5.txt
68 read from ../pwab_input_1.txt
307 lines written to ab_glob5.txt


There are many with no tooltip 

# ../pwab_input_2.txt
Add 'dummy' tooltips ('??')
# revise ab_glob5
# global abbreviations with (a) counts, (b) current tooltips (via pwab_input_2.txt)
python ab_glob0.py ../temp_pw_5.txt ../temp_pw_ab_5.txt ../pwab_input_2.txt ab_glob5.txt
299 distinct <ab>X</ab> from ../temp_pw_5.txt
299 distinct <ab>X</ab> from ../temp_pw_ab_5.txt
307 read from ../pwab_input_2.txt
307 lines written to ab_glob5.txt

# local abbreviations with counts
python ab_local1.py ../temp_pw_5.txt ../temp_pw_ab_5.txt ab_local5.txt
581 distinct <ab []>X</ab> from ../temp_pw_5.txt
581 distinct <ab []>X</ab> from ../temp_pw_ab_5.txt
581 lines written to ab_local5.txt
0 differences in local abbreviations
238 distinct abbreviations


******************************************************
******************************************************
Use 'inline display of abbreviations'
cp /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue88/dev4_tm/web/webtc/basicadjust.php /c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php 


******************************************************
09-24-2023
Local abbreviations just for 'u.' (und/unter)
python ab_local_tm1.py ../temp_pw_5.txt ab_local_tm_1.txt
******************************************************
09-25-2023
temp_pw_6.txt,  temp_pw_ab_6.txt, pwab_input_3.txt
------------------------------------------------------
---------
Ref https://github.com/sanskrit-lexicon/PWK/issues/88#issuecomment-1732958845
  and following comments.
-----
<ab>inbes.</ab> -> <ab>insbes.</ab>  (18) typo
<ab>instebs.</ab> -> <ab>insbes.</ab>  (1) typo
<ab>Kalb.</ab> -> Kalb (1) typo
<ab>Pt.</ab> -> <ab>Pl.</ab>  (1) typo?
<ab>Red.</ab> -> <ab>Bed.</ab> (5) typo

cp pwab_input_2.txt pwab_input_3.txt
Remove from pwab_input_3.txt : inbes, instebs, Kalb, Pt, Red

------------------------------------------------------
******************************************************
 'is changes'
<is n="X">Y</is> and <is>Y<is>
Generally assume pw_ab is correct for <is>X</is>.
******************************************************
Generate changes (to temp_pw_6).
cp temp_pw_6.txt temp_pw_6a.txt
cp temp_pw_ab_6.txt temp_pw_ab_6a.txt
touch ../change_pw_6a.txt

------------------------------------------------------
-----
change 
158 matches in 151 lines for "<is>[*]" in buffer: temp_pw_6.txt
157 matches in 150 lines for "[*]<is>" in buffer: temp_pw_ab_6.txt
126 matches in 125 lines for "</is>-<is>" in buffer: temp_pw_6a.txt


# 
manually edit temp_pw_6a.txt
 change <is>* to *<is> --- to agree with Andhrabharati
 change </is>-<is> --- to agree with Andhrabharati
 <is>Rc</is> -> <is>Ṛc</is>  (2)
 <is>Rtu</is> -> <is>Ṛtu</is> (1)
 <is>Rṣi</is> -> <is>Ṛṣi</is> (6)
 <is>Civa</is> -> <is>Śiva</is> (12)
 
72 matches for "<is>Viśve Devās</is>" in buffer: temp_pw_ab_6a.txt
<is>Viśve</is> <is>Devās</is> -> <is>Viśve Devās</is> (51)

 <is n="1">Prākrit</is> -> <lang>Prākrit</lang (127) 
 <is n="1">prākritisch</is> -> prākritisch (2)
 <is n="1">Pāli</is> -> <lang>Pāli</lang>  (9)
 several other is n="1" changes
 
insert temp_is_compare_texts_change0.txt into ../change_pw_6a.txt

python diff_to_changes_dict.py temp_pw_6.txt temp_pw_6a.txt ablists/temp_is_compare_texts_change0.txt
817 changes written to ablists/temp_is_compare_texts_change0.txt

python updateByLine.py temp_pw_6.txt change_pw_6a.txt temp_pw_6a.txt
817 lines changed

---------------------------------------
cd ../
touch change_pw_ab_6a.txt
manual changes to temp_pw_ab_6a.txt

------------------------------------
Partial resolution of is differences -- get the Number of <is>X</is> to be
the same for all entries

python is_compare_texts_changelen.py ../temp_pw_6a.txt ../temp_pw_ab_6a.txt temp_is_compare_texts_changelen.txt
230 cases written to temp_is_compare_texts_changelen.txt

Resolve these manually by changes to ../temp_pw_6a.txt, ../temp_pw_ab_6a.txt
--------

python diff_to_changes_dict.py temp_pw_ab_6.txt temp_pw_ab_6a.txt ablists/temp_is_compare_texts_change0_ab.txt
12 changes written to ablists/temp_is_compare_texts_change0_ab.txt

insert ablists/temp_is_compare_texts_change0_ab.txt into change_pw_ab_6a.txt
START HERE problem with updateByLine.py next ...??
python updateByLine.py temp_pw_ab_6.txt change_pw_ab_6a.txt temp.txt
diff temp_pw_ab_6a.txt temp.txt | wc -l
# expect 0

--------------------------------------------------------
# get first difference in each entry w.r.t. <is>X</is>
This is don
# iteration 1
python is_compare_texts_change.py ../temp_pw_6a.txt ../temp_pw_ab_6a.txt temp_is_compare_texts_change1.txt
1835 cases written to temp_is_compare_texts_change1.txt

insert temp_is_compare_texts_change1.txt into ../change_pw_6a.txt

cd ../
python updateByLine.py temp_pw_6.txt change_pw_6a.txt temp_pw_6a.txt
# 2774 lines changed.
cd ablists

# iteration 2
python is_compare_texts_change.py ../temp_pw_6a.txt ../temp_pw_ab_6a.txt temp_is_compare_texts_change2.txt
289 cases written to temp_is_compare_texts_change2.txt

insert temp_is_compare_texts_change2.txt at end of ../change_pw_6a.txt

cd ../
python updateByLine.py temp_pw_6.txt change_pw_6a.txt temp_pw_6a.txt
# 2440 change transactions from change_pw_6a.txt
cd ablists

# iteration 3
python is_compare_texts_change.py ../temp_pw_6a.txt ../temp_pw_ab_6a.txt temp_is_compare_texts_change3.txt
107 cases written to temp_is_compare_texts_change3.txt

insert temp_is_compare_texts_change3.txt at end of ../change_pw_6a.txt

cd ../
python updateByLine.py temp_pw_6.txt change_pw_6a.txt temp_pw_6a.txt
# 2547 change transactions from change_pw_6a.txt
cd ablists

# iteration 4
python is_compare_texts_change.py ../temp_pw_6a.txt ../temp_pw_ab_6a.txt temp_is_compare_texts_change4.txt
68 cases written to temp_is_compare_texts_change4.txt

insert temp_is_compare_texts_change4.txt at end of ../change_pw_6a.txt

cd ../
python updateByLine.py temp_pw_6.txt change_pw_6a.txt temp_pw_6a.txt
# 2615 change transactions from change_pw_6a.txt
cd ablists

# iteration 5
python is_compare_texts_change.py ../temp_pw_6a.txt ../temp_pw_ab_6a.txt temp_is_compare_texts_change5.txt
56 cases written to temp_is_compare_texts_change5.txt

insert temp_is_compare_texts_change5.txt at end of ../change_pw_6a.txt

cd ../
python updateByLine.py temp_pw_6.txt change_pw_6a.txt temp_pw_6a.txt
# 2671 change transactions from change_pw_6a.txt
cd ablists

# iteration 6
python is_compare_texts_change.py ../temp_pw_6a.txt ../temp_pw_ab_6a.txt temp_is_compare_texts_change6.txt
48 cases written to temp_is_compare_texts_change6.txt

insert temp_is_compare_texts_change6.txt at end of ../change_pw_6a.txt

cd ../
python updateByLine.py temp_pw_6.txt change_pw_6a.txt temp_pw_6a.txt
# 2719 change transactions from change_pw_6a.txt
cd ablists

# iteration 7
python is_compare_texts_change.py ../temp_pw_6a.txt ../temp_pw_ab_6a.txt temp_is_compare_texts_change7.txt
45 cases written to temp_is_compare_texts_change7.txt

insert temp_is_compare_texts_change7.txt at end of ../change_pw_6a.txt

cd ../
python updateByLine.py temp_pw_6.txt change_pw_6a.txt temp_pw_6a.txt
# 2764 change transactions from change_pw_6a.txt
cd ablists

# iteration 8
python is_compare_texts_change.py ../temp_pw_6a.txt ../temp_pw_ab_6a.txt temp_is_compare_texts_change8.txt
45 cases written to temp_is_compare_texts_change8.txt

insert temp_is_compare_texts_change8.txt at end of ../change_pw_6a.txt

cd ../
python updateByLine.py temp_pw_6.txt change_pw_6a.txt temp_pw_6a.txt
# 2809 change transactions from change_pw_6a.txt
cd ablists

# iteration 9
python is_compare_texts_change.py ../temp_pw_6a.txt ../temp_pw_ab_6a.txt temp_is_compare_texts_change9.txt
44 cases written to temp_is_compare_texts_change9.txt

insert temp_is_compare_texts_change9.txt at end of ../change_pw_6a.txt

cd ../
python updateByLine.py temp_pw_6.txt change_pw_6a.txt temp_pw_6a.txt
# 2853 change transactions from change_pw_6a.txt
cd ablists

# iteration 10
python is_compare_texts_change.py ../temp_pw_6a.txt ../temp_pw_ab_6a.txt temp_is_compare_texts_change10.txt
43 cases written to temp_is_compare_texts_change10.txt

insert temp_is_compare_texts_change10.txt at end of ../change_pw_6a.txt

cd ../
python updateByLine.py temp_pw_6.txt change_pw_6a.txt temp_pw_6a.txt
# 2896 change transactions from change_pw_6a.txt
cd ablists

# iteration 11
python is_compare_texts_change.py ../temp_pw_6a.txt ../temp_pw_ab_6a.txt temp_is_compare_texts_change11.txt
41 cases written to temp_is_compare_texts_change11.txt

insert temp_is_compare_texts_change11.txt at end of ../change_pw_6a.txt

cd ../
python updateByLine.py temp_pw_6.txt change_pw_6a.txt temp_pw_6a.txt
# 2937 change transactions from change_pw_6a.txt
cd ablists

# iteration 12
python is_compare_texts_change.py ../temp_pw_6a.txt ../temp_pw_ab_6a.txt temp_is_compare_texts_change12.txt
40 cases written to temp_is_compare_texts_change12.txt

insert temp_is_compare_texts_change12.txt at end of ../change_pw_6a.txt

cd ../
python updateByLine.py temp_pw_6.txt change_pw_6a.txt temp_pw_6a.txt
# 2937 change transactions from change_pw_6a.txt
cd ablists

------------------------------------------------------
python is_glob0.py ../temp_pw_6a.txt ../temp_pw_ab_6a.txt is_glob6a.txt

------------------------------------------------------
------------------------------------------------------
-----------------------------------------------------
python is_compare_texts.py ../temp_pw_6a.txt ../temp_pw_ab_6a.txt temp.txt
2305 cases written to temp.txt

python is_glob0.py ../temp_pw_6.txt ../temp_pw_ab_6.txt is_glob6.txt

---------------------------
NEW TAG:
26 matches in 22 lines for "<iw>" in buffer: temp_pw_ab_6a.txt
Ref: https://github.com/sanskrit-lexicon/PWK/issues/95#issuecomment-1652090274
all the wide-spaced entities whether Sanskrit [tagged as <is strings--
whether being full word(s), or abbreviated] and non-Sanskrit
[tagged as <iw strings] in "straight face", never in italics
(even if it is a single letter abbr., at some places).
cd

---------------------------

<ls>ṚV. 1,61,3. 122,2. 6,67,1. 10,99,1.</ls>  Add n=...


python regex_compare_texts.py '<is>Tithi</is>' ../temp_pw_6b.txt ../temp_pw_ab_6a.txt temp.txt

python is_glob0.py ../temp_pw_6a.txt ../temp_pw_ab_6a.txt is_glob6a.txt
3700 distinct <ab>X</ab> from ../temp_pw_6a.txt
3700 distinct <is>X</is> from ../temp_pw_ab_6a.txt
0 instances with different counts
3700 lines written to is_glob6a.txt

python is_local1.py ../temp_pw_6a.txt ../temp_pw_ab_6a.txt is_local6a.txt

python regex_compare_texts.py '<iw>.*?</iw>' ../temp_pw_6b.txt ../temp_pw_ab_6a.txt temp.txt

********************************************************************
09-28-2023
<is...> or <iw...> within italic markup -- there should be NONE
cp temp_pw_6a.txt temp_pw_7.txt
cp temp_pw_ab_6a.txt temp_pw_ab_7.txt
touch change_pw_7.txt
touch change_pw_ab_7.txt

9851 matches in 9665 lines for "{%[^%]*<is" in temp_pw_6a.txt
1 match for "{%[^%]*<iw" in temp_pw_6a.txt

We want to recode to get rid of all of these -- Note none of these
appear in temp_pw_ab_6a.txt

--------------------
 Part 1: <iw>
cp temp_pw_7.txt temp_pw_7_work.txt
# manual change temp_pw_7_work.txt
<iw>Kuttak</iw>
python diff_to_changes_dict.py temp_pw_7.txt temp_pw_7_work.txt temp_change_pw_7_1.txt
# insert temp_change_pw_7_1.txt into change_pw_7.txt
python updateByLine.py temp_pw_6a.txt change_pw_7.txt temp_pw_7.txt
# 1 change transactions from change_pw_7.txt
# check
diff temp_pw_7.txt  temp_pw_7_work.txt | wc -l
# 0 as expected

--------------------
Part 2
It is somewhat tricky to get 'good' corrections.
Thus I try a sequence of 'good' corrections
This is the first one
Example:
Old: {%die Function des <is>Hotraka</is>%}
New: {%die Function des%} <is>Hotraka</is>

# manual edit in Emacs of temp_pw_7_work.txt
Y = <is>Z</is> or <is n="W">Z</is>
{%X Y%} -> {%X%} Y
1172 matches in 1164 lines for "{%\([^<%]*\) \(<is[^>%]*>[^<%]*</is>\)%}"

# replaced 1172 occurrences:
{%\([^<%]*\) \(<is[^>%]*>[^<%]*</is>\)%} → {%\1%} \2

python diff_to_changes_dict.py temp_pw_7.txt temp_pw_7_work.txt temp_change_pw_7_2.txt
# insert temp_change_pw_7_2.txt into change_pw_7.txt

python updateByLine.py temp_pw_6a.txt change_pw_7.txt temp_pw_7.txt
# 1165 change transactions from change_pw_7.txt
# check
diff temp_pw_7.txt  temp_pw_7_work.txt | wc -l
# 0 as expected

8679 matches in 8578 lines for "{%[^%]*<is" in buffer: temp_pw_7_work.txt

--------------------
Part 3:
Same as part 2, except that there is a period before closing italics
Example:
old: {%ein <is>Buddha</is>.%}
new: {%ein%} <is>Buddha</is>.

2162 matches in 2159 lines for "{%\([^<%]*\) \(<is[^>%]*>[^<%]*</is>\)\.%}" in buffer: temp_pw_7_work.txt

Replacement:
{%\([^<%]*\) \(<is[^>%]*>[^<%]*</is>\)\.%} → {%\1%} \2.
replace 2162 occurrences

python diff_to_changes_dict.py temp_pw_7.txt temp_pw_7_work.txt temp_change_pw_7_3.txt
2159 changes
# insert temp_change_pw_7_3.txt into change_pw_7.txt

python updateByLine.py temp_pw_6a.txt change_pw_7.txt temp_pw_7.txt
# 3324 change transactions from change_pw_7.txt
# check
diff temp_pw_7.txt  temp_pw_7_work.txt | wc -l
# 0 as expected

6517 matches in 6439  for "{%[^%]*<is" in buffer: temp_pw_7_work.txt

--------------------
Part 4:
Example:
old: {%<is>Agni</is>'s Gattin.%}
new: {%<is>Agni</is>%}ʼs Gattin.
Note use of ʼ instead of apostrophe  (there are many more)

453 matches in 451 lines for "{%\(<is[^<%]*</is>\)ʼs 

manual replacements in temp_pw_7_work.txt
{%\(<is[^<%]*</is>\)'s  → \1ʼs {%

python diff_to_changes_dict.py temp_pw_7.txt temp_pw_7_work.txt temp_change_pw_7_4.txt
451 lines changed
# insert temp_change_pw_7_4.txt into change_pw_7.txt

python updateByLine.py temp_pw_6a.txt change_pw_7.txt temp_pw_7.txt
# 3775 lines changed
# check
diff temp_pw_7.txt  temp_pw_7_work.txt | wc -l
# 0 as expected

6093 matches in 6023 lines for "{%[^%]*<is" in buffer: temp_pw_7_work.txt

--------------------
Part 5:
Example:
old: {%<is>Pavamāna</is> versehen.%}
new: <is>Pavamāna</is> {%<versehen.%}

manual replacement in temp_pw_7_work
{%\(<is[^<%]*</is>\)  → \1 {%

348 replacements
Note: This results in some problems with commas
Example: <is>Ketu</is> {%, der niedersteigende Knoten.%}

125 matches for "{%, " in buffer: temp_pw_7_work.txt
Correct these manually
"{%, "  → , {%

python diff_to_changes_dict.py temp_pw_7.txt temp_pw_7_work.txt temp_change_pw_7_5.txt
450 changes

# insert temp_change_pw_7_5.txt into change_pw_7.txt

python updateByLine.py temp_pw_6a.txt change_pw_7.txt temp_pw_7.txt
# 4225 lines changed
# check
diff temp_pw_7.txt  temp_pw_7_work.txt | wc -l
# 0 as expected

5846 matches  for "{%[^%]*<is" in buffer: temp_pw_7_work.txt

--------------------
Part 6

Example:
old: {%ein <ab>best.</ab> <is>Samādhi</is>%}
new: {%ein <ab>best.</ab>%} <is>Samādhi</is>
Also
old: {%und <is>Soma</is>.%}
new: {%und%} <is>Soma</is>.

modify temp_pw_7_work.txt
 \(<is[^<]*</is>\.?\)%} → %} \1
1470 replacements
There are a 6 cases left with ', %}' which are changed to '%}, '

python diff_to_changes_dict.py temp_pw_7.txt temp_pw_7_work.txt temp_change_pw_7_6.txt
1468 lines changed

# insert temp_change_pw_7_6.txt into change_pw_7.txt

python updateByLine.py temp_pw_6a.txt change_pw_7.txt temp_pw_7.txt
# 5693 lines changed
# check
diff temp_pw_7.txt  temp_pw_7_work.txt | wc -l
# 0 as expected

4769 matches for "{%[^%]*<is" in buffer: temp_pw_7_work.txt

--------------------
Part 7

Example:
old: {%<is>Soma</is>-Stengel%}
new: <is>Soma</is>-{%Stengel%}

135 matches for "{%<is[^<]*</is>-"

{%\(<is[^<]*</is>\)-\([^ ]\)  -> \1-{%\2
129 replacements
additional adjustments in 6 lines
Example:
old: {%<is>Soma</is>- Opfer.%}
new: <is>Soma</is>-{%Opfer.%}

Question:
17 matches in 13 lines for "-</is>"  should these be "</is>-" ?

python diff_to_changes_dict.py temp_pw_7.txt temp_pw_7_work.txt temp_change_pw_7_7.txt
134 lines changed

# insert temp_change_pw_7_7.txt into change_pw_7.txt

python updateByLine.py temp_pw_6a.txt change_pw_7.txt temp_pw_7.txt
# 5827 lines changed
# check
diff temp_pw_7.txt  temp_pw_7_work.txt | wc -l
# 0 as expected

4634 matches for "{%[^%]*<is" in buffer: temp_pw_7_work.txt

--------------------
Part 8
Example
old: {%beschleunigte <is>Soma</is>-Kelterung%}
new: {%beschleunigte%} <is>Soma</is>-{%Kelterung%}

486 matches in 485 lines for " <is[^<]*</is>-[^{% ]*%}"

 \(<is[^<]*</is>\)-\([^{% ]*\)%} → %} \1-{%\2%}
486 replacements

python diff_to_changes_dict.py temp_pw_7.txt temp_pw_7_work.txt temp_change_pw_7_8.txt
485 lines changed

# insert temp_change_pw_7_8.txt into change_pw_7.txt

python updateByLine.py temp_pw_6a.txt change_pw_7.txt temp_pw_7.txt
# 6312 lines changed
# check
diff temp_pw_7.txt  temp_pw_7_work.txt | wc -l
# 0 as expected

4170 matches for "{%[^%]*<is" in buffer: temp_pw_7_work.txt

--------------------
Part 9
Example:
old: {%noch nicht in die <is>Saṃhitā</is> umgesetzt%}
new: {%noch nicht in die%} <is>Saṃhitā</is> {%umgesetzt%}

2718 matches for "{%[^%<]* <is[^<]*</is> [^%<]*%}"

Replacement in temp_pw_7_work:
2718 replacements

python diff_to_changes_dict.py temp_pw_7.txt temp_pw_7_work.txt temp_change_pw_7_9.txt
2709 lines changed

# insert temp_change_pw_7_9.txt into change_pw_7.txt

python updateByLine.py temp_pw_6a.txt change_pw_7.txt temp_pw_7.txt
# 9021 lines changed
# check
diff temp_pw_7.txt  temp_pw_7_work.txt | wc -l
# 0 as expected

1452 matches for "{%[^%]*<is" in buffer: temp_pw_7_work.txt

--------------------
Part 10:
Example:
old: {%reich an <is>Soma</is>-Pflanzen oder -Saft.%}
new: {%reich an%} <is>Soma</is>-{%Pflanzen oder -Saft.%}

243 matches for "{%[^%<]+ <is>[^<]*</is>-[^%<]*%}"

{%\([^%<]+\) \(<is>[^<]*</is>\)-\([^%<]*\)%} → {%\1%} \2-{%\3%}
243 replacements in temp_pw_7_work.txt

python diff_to_changes_dict.py temp_pw_7.txt temp_pw_7_work.txt temp_change_pw_7_10.txt
241 lines changed

# insert temp_change_pw_7_10.txt into change_pw_7.txt

python updateByLine.py temp_pw_6a.txt change_pw_7.txt temp_pw_7.txt
# 9262 lines changed
# check
diff temp_pw_7.txt  temp_pw_7_work.txt | wc -l
# 0 as expected

1209 matches for "{%[^%]*<is" in buffer: temp_pw_7_work.txt

--------------------
Part 11
Example:
old: {%mit <is>Agni</is>'s Schärfe%}
new: {%mit%} <is>Agni</is>ʼs {%Schärfe%}
 Note use of ʼ

296 matches for "{%[^%<]+ <is>[^<]*</is>'s\.?%}"

{%\([^%<]+\) \(<is>[^<]*</is>\)'s\(\.?\)%} → {%\1%} \2ʼs\3
296 replacements in temp_pw_7_work.txt

python diff_to_changes_dict.py temp_pw_7.txt temp_pw_7_work.txt temp_change_pw_7_11.txt
295 lines changed

# insert temp_change_pw_7_11.txt into change_pw_7.txt

python updateByLine.py temp_pw_6a.txt change_pw_7.txt temp_pw_7.txt
# 9557 lines changed
# check
diff temp_pw_7.txt  temp_pw_7_work.txt | wc -l
# 0 as expected

913 matches for "{%[^%]*<is" in buffer: temp_pw_7_work.txt

--------------------
Part 12
Example

old: {%eine <ab>best.</ab> mythische Waffe <is>Arjuna</is>'s.%}
new: {%eine <ab>best.</ab> mythische Waffe%} <is>Arjuna</is>'s.
51 matches for "</is>'s\.?%}"

49 Replacements 
{%\([^%]+\) \(<is>[^<]*</is>\)'s\(\.?\)%} → {%\1%} \2ʼs\3
Many manual adjustments to these 49 replacements.

python diff_to_changes_dict.py temp_pw_7.txt temp_pw_7_work.txt temp_change_pw_7_12.txt
51 lines changed

# insert temp_change_pw_7_12.txt into change_pw_7.txt

python updateByLine.py temp_pw_6a.txt change_pw_7.txt temp_pw_7.txt
# 9608 lines changed
# check
diff temp_pw_7.txt  temp_pw_7_work.txt | wc -l
# 0 as expected

864 matches for "{%[^%]*<is" in buffer: temp_pw_7_work.txt

--------------------
Part 13:
example
old: 
new: 

 \(<is[^<]*</is>\)-\([^{%]*\)%} → %} \1-{%\2%}
41 replacements -- further manual adjustments

python diff_to_changes_dict.py temp_pw_7.txt temp_pw_7_work.txt temp_change_pw_7_13.txt
41 lines changed

# insert temp_change_pw_7_13.txt into change_pw_7.txt

python updateByLine.py temp_pw_6a.txt change_pw_7.txt temp_pw_7.txt
# 9649 lines changed
# check
diff temp_pw_7.txt  temp_pw_7_work.txt | wc -l
# 0 as expected

825 matches for "{%[^%]*<is" in buffer: temp_pw_7_work.txt

--------------------
Part 14:
Example
old: {%über <is>Agni</is> und <is>Kaśyapa</is> handelnd.%}
new: {%über%} <is>Agni</is> {%und%} <is>Kaśyapa</is> {%handelnd.%}

164 matches for "{%[^%<]+ <is[^<]*</is> [^<%]* <is[^<]*</is> [^<%]+%}"

164 Replacements in temp_pw_7_work.txt
{%\([^%<]+\) \(<is[^<]*</is>\) \([^<%]*\) \(<is[^<]*</is>\) \([^<%]+\)%} → {%\1%} \2 {%\3%} \4 {%\5%}

python diff_to_changes_dict.py temp_pw_7.txt temp_pw_7_work.txt temp_change_pw_7_14.txt
163 lines changed

# insert temp_change_pw_7_14.txt into change_pw_7.txt

python updateByLine.py temp_pw_6a.txt change_pw_7.txt temp_pw_7.txt
# 9812 lines changed
# check
diff temp_pw_7.txt  temp_pw_7_work.txt | wc -l
# 0 as expected

661 matches for "{%[^%]*<is" in buffer: temp_pw_7_work.txt

--------------------
Part 15 
Example:
old: {%*<is>Indra</is>'s. Stadt.%}
new: <is>Indra</is>'s. {%*Stadt.%}

old: {%ein Feind <is>Viṣṇu</is>'s. Deren neun bei den%}
new: {%ein Feind%} <is>Viṣṇu</is>'s. {%Deren neun bei den%}

ʼ

21 matches for "{%[^%]*</is>'s[^ ]"
manually changed in temp_pw_7_work.txt

python diff_to_changes_dict.py temp_pw_7.txt temp_pw_7_work.txt temp_change_pw_7_15.txt
21 lines changed

# insert temp_change_pw_7_15.txt into change_pw_7.txt

python updateByLine.py temp_pw_6a.txt change_pw_7.txt temp_pw_7.txt
# 9833 lines changed
# check
diff temp_pw_7.txt  temp_pw_7_work.txt | wc -l
# 0 as expected

661 matches for "{%[^%]*<is" in buffer: temp_pw_7_work.txt

--------------------
Part 16:

187 matches for "{%[^%]*</is>'s.*?%}"

start line 550511 of temp_pw_7_work.txt
@ -> ʼ,  {{% -> {%


python diff_to_changes_dict.py temp_pw_7.txt temp_pw_7_work.txt temp_change_pw_7_16.txt
187 lines changed

# insert temp_change_pw_7_16.txt into change_pw_7.txt

python updateByLine.py temp_pw_6a.txt change_pw_7.txt temp_pw_7.txt
# 10020 lines changed
# check
diff temp_pw_7.txt  temp_pw_7_work.txt | wc -l
# 0 as expected

456 matches for "{%[^%]*<is" in buffer: temp_pw_7_work.txt


--------------------
Part 17

manual corrections to these 456
start L>70153

python diff_to_changes_dict.py temp_pw_7.txt temp_pw_7_work.txt temp_change_pw_7_17.txt
630 lines changed

# insert temp_change_pw_7_17.txt into change_pw_7.txt

python updateByLine.py temp_pw_6a.txt change_pw_7.txt temp_pw_7.txt
# 10650 lines changed
# check
diff temp_pw_7.txt  temp_pw_7_work.txt | wc -l
# 0 as expected

0 matches for "{%[^%]*<is" in buffer: temp_pw_7_work.txt

This completes the changes under temp_pw_7 relating to <is> and italics.

changes to temp_pw_ab_7.txt
change_pw_ab_7.txt  todo
python diff_to_changes_dict.py temp_pw_ab_6a.txt temp_pw_ab_7.txt temp_change_pw_ab_7_1.txt
5 change

Insert these into change_pw_ab_7.txt

==============================================================
resolve differences in number of italic groups
grep -E "{%" temp_pw_7.txt | wc -l
171442

grep -E "{%" temp_pw_ab_7.txt | wc -l
170297


python regex_compare_texts_count.py '{%.*?%}' ../temp_pw_7.txt ../temp_pw_ab_7.txt temp.txt
1805 cases 

Part 18:
move <lex> tags out of italics
211 matches for "{%[^%]*<lex" in buffer: temp_pw_7_work.txt
No cases in ab_7.
These removed.

python diff_to_changes_dict.py temp_pw_7.txt temp_pw_7_work.txt temp_change_pw_7_18.txt
211 lines changed

# insert temp_change_pw_7_18.txt into change_pw_7.txt

python updateByLine.py temp_pw_6a.txt change_pw_7.txt temp_pw_7.txt
10861 lines changed
# check
diff temp_pw_7.txt  temp_pw_7_work.txt | wc -l
# 0 as expected

python regex_compare_texts_count.py '{%.*?%}' ../temp_pw_7.txt ../temp_pw_ab_7.txt temp.txt
1648 cases

--------------------
Part 19
number of italic groups containing abbreviations
Resolve so these count the same.
python regex_compare_texts_count.py '{%[^%]*<ab' ../temp_pw_7.txt ../temp_pw_ab_7.txt temp.txt
1017 cases written to temp.txt

Many steps
352 matches in 350 lines for "{%[^%]*(<ab>Acc.</ab>)" in buffer: temp_pw_7_work.txt
Remove these from italic scope.

45 matches for "{%[^%]*(<ab>Dat.</ab>)"
120 matches for "{%[^%]*(<ab>Gen.</ab>)"
34 matches for "{%[^%]*(<ab>Abl.</ab>)"
38 matches for "{%[^%]*(<ab>Instr.</ab>)"
61 matches in 60 lines for "{%[^%]*<ab>d[.] i[.]</ab>"
19 matches for "{%[^%]*<ab>Pl[.]
532 matches in 523 lines 2for "{%[^%]*<ab>v[.] a[.]"
118 matches for "{%[^%]*<ab>u[.] s[.] w[.]"

489 matches in 1257 lines for "{%[^%]*<ab>[^b]" in buffer: temp_pw_7_work.txt
168 matches in 167 lines for "{%[^%]*<ab>[^b]" in buffer: temp_pw_ab_7.txt

6 matches for "{%[^%]*<ab>Med\."
9 matches for "{%[^%]*<ab>Abl.</ab>"
15 matches for "{%[^%]*<ab>Gen.</ab>"
72 matches for "{%[^%]*<ab>insbes.</ab>"
91 matches in 89 lines for "{%[^%]*<ab>Loc\.</ab>"
34 matches for "{%[^%]*<ab>überh.</ab>"
30 matches for "{%[^%]*<ab>Bez"
17 matches for "{%[^%]*<ab>[B]"

python diff_to_changes_dict.py temp_pw_7.txt temp_pw_7_work.txt temp_change_pw_7_19.txt
1629 lines changed

# insert temp_change_pw_7_19.txt into change_pw_7.txt

python updateByLine.py temp_pw_6a.txt change_pw_7.txt temp_pw_7.txt
12490 lines changed
# check
diff temp_pw_7.txt  temp_pw_7_work.txt | wc -l
#0 expected

python diff_to_changes_dict.py temp_pw_ab_6a.txt temp_pw_ab_7.txt temp_change_ab_7_1.txt
17 lines changed.

# insert temp_change_ab_7_1.txt into change_pw_ab_7.txt

python updateByLine.py temp_pw_ab_6a.txt change_pw_ab_7.txt temp.txt
12490 lines changed
# check
diff temp_pw_ab_7.txt  temp.txt | wc -l
#0 expected

---------------------------------------------
equalize the NUMBER of italic texts per entry
---------------------------------------------
python regex_compare_texts_count.py '{%[^%]*%}' ../temp_pw_7_work.txt ../temp_pw_ab_7.txt temp.txt
807 cases written to temp.txt

Subcase 'dangling paren'
175 matches for "{%[^%]*([^%)]*%}

python regex_compare_texts_count.py '{%[^%]*%}' ../temp_pw_7_work.txt ../temp_pw_ab_7.txt temp.txt
767 cases written to temp.txt
python regex_compare_texts_count1.py '{%[^%]*%}' ../temp_pw_7_work.txt ../temp_pw_ab_7.txt temp1.org

A few corrections were made manually.
update temp_pw_7 and temp_pw_ab_7

python diff_to_changes_dict.py temp_pw_7.txt temp_pw_7_work.txt temp_change_pw_7_20.txt
181  lines changed

# insert temp_change_pw_7_20.txt into change_pw_7.txt

python updateByLine.py temp_pw_6a.txt change_pw_7.txt temp_pw_7.txt
12671 lines changed

# check
diff temp_pw_7.txt  temp_pw_7_work.txt | wc -l
#0 expected

python diff_to_changes_dict.py temp_pw_ab_6a.txt temp_pw_ab_7.txt temp_change_ab_7_1.txt
18 lines changed.

# insert temp_change_ab_7_1.txt into change_pw_ab_7.txt

python updateByLine.py temp_pw_ab_6a.txt change_pw_ab_7.txt temp.txt
12490 lines changed
# check
diff temp_pw_ab_7.txt  temp.txt | wc -l
#0 expected

-------------------------------------------------------------
10-2-2023
Further work to resolve {%X%} count differences
Note two new temporary digitizations (.._work1.txt).
These have metalines of form '* <L>...' for easier comparisons.

python regex_compare_texts_count1.py '{%[^%]*%}' ../temp_pw_7_work.txt ../temp_pw_ab_7.txt temp1.org ../temp_pw_7_work1.txt ../temp_pw_ab_7_work1.txt


Intermediate work - derive changes
Remove temporary markup in temp_pw_7_work1.txt save as temp_pw_7_work2.txt
python diff_to_changes_dict.py temp_pw_7.txt temp_pw_7_work2.txt temp_change_pw_7_21.txt
276  lines changed

# insert temp_change_pw_7_21.txt into change_pw_7.txt

python updateByLine.py temp_pw_6a.txt change_pw_7.txt temp_pw_7.txt
12947 lines changed

# check
diff temp_pw_7.txt  temp_pw_7_work2.txt | wc -l
#0 expected

python diff_to_changes_dict.py temp_pw_ab_6a.txt temp_pw_ab_7_work2.txt temp_change_ab_7_1.txt
27 lines changed.

# insert temp_change_ab_7_1.txt into change_pw_ab_7.txt

python updateByLine.py temp_pw_ab_6a.txt change_pw_ab_7.txt temp_pw_ab_7.txt
27 lines changed
# check
diff temp_pw_ab_7.txt  temp_pw_ab_7_work2.txt | wc -l
#0 expected

--------------------
Part 22
# Reconstruct the work
mv temp_pw_7_work2.txt temp_pw_7_work.txt

# reconstruct work1 files and temp1.org

python regex_compare_texts_count1.py '{%[^%]*%}' ../temp_pw_7_work.txt ../temp_pw_ab_7.txt temp1.org ../temp_pw_7_work1.txt ../temp_pw_ab_7_work1.txt
# 546 cases written to temp1.org

-----
observations during adjustments to temp_pw_7_work1 and temp_pw_ab_7_work1
Question:  Did Thomas insert Jāmadagnya for — ?
<L>42583<pc>2264-2<k1>jAmadagnyadvAdaSI<k2>jAmadagnyadvAdaSI<e>100
{#jAmadagnyadvAdaSI#}¦ <lex>f.</lex> {%der 12te Tag in der%} <is>Jāmadagnya</is>-Hälfte des <is>Vaiśākha</is>.
scan has:
{#jAmadagnyadvAdaSI#}¦ <lex>f.</lex> {%der 12te Tag in der — Hälfte des%} <is>Vaiśākha</is>.

¹⁄₆₀ !!

<L>68507<pc>4104-3<k1>puzkaramUlaka  odd markup involving bot, italics

<L>91144<pc>5147-3<k1>yuD
   need line break at `<div n="1">— 3) {%kämpfen lassen%}`

<L>104497<pc>6120-1<k1>viS
Page 6122-3,section 5 sich niederlassen, sich niederlegen
Remove extra text: zu lesen[), - "sich zur Ruhe begeben" auf oder in ...

10-05-2023  Finish
cp temp_pw_7_work1.txt temp_pw_7_work2.txt
cp temp_pw_ab_7_work1.txt temp_pw_ab_7_work2.txt
# remove temporary '* <L>' markup
# run redo_dev.sh and adjust for xml validity
sh redo_dev.sh 7_work2
sh redo_dev.sh ab_7_work2
# get change file between 7 and 7_work2

python diff_to_changes_dict.py temp_pw_7.txt temp_pw_7_work2.txt temp_change_pw_7_22.txt
381  lines changed

# insert temp_change_pw_7_22.txt into change_pw_7.txt

python updateByLine.py temp_pw_6a.txt change_pw_7.txt temp_pw_7.txt
13328 lines changed

# check
diff temp_pw_7.txt  temp_pw_7_work2.txt | wc -l
#0 expected

# get change file between ab_7 and ab_7_work2
python diff_to_changes_dict.py temp_pw_ab_7.txt temp_pw_ab_7_work2.txt temp_change_ab_7_2.txt
266 changes written to temp_change_ab_7_2.txt

# insert temp_change_ab_7_2.txt into change_pw_ab_7.txt

# revise
python updateByLine.py temp_pw_ab_6a.txt change_pw_ab_7.txt temp_pw_ab_7.txt
293 lines changed

# check
diff temp_pw_ab_7.txt  temp_pw_ab_7_work2.txt | wc -l
#0 expected

--------------------
Did we miss any ? rerun

python regex_compare_texts_count1.py '{%[^%]*%}' ../temp_pw_7.txt ../temp_pw_ab_7.txt temp1.org ../temp_pw_7_work3.txt ../temp_pw_ab_7_work3.txt
12 cases written to temp1.org   yes, we missed 12

Revise temp_pw_7_work3.txt ../temp_pw_ab_7_work3.txt for these cases.

Finish
cp temp_pw_7_work3.txt temp_pw_7_work4.txt
cp temp_pw_ab_7_work3.txt temp_pw_ab_7_work4.txt
# remove temporary '* <L>' markup from the two work4 files
# run redo_dev.sh and adjust for xml validity
sh redo_dev.sh 7_work4
sh redo_dev.sh ab_7_work4
# get change file between 7 and 7_work4

python diff_to_changes_dict.py temp_pw_7.txt temp_pw_7_work4.txt temp_change_pw_7_23.txt
9  lines changed

# insert temp_change_pw_7_23.txt into change_pw_7.txt

python updateByLine.py temp_pw_6a.txt change_pw_7.txt temp_pw_7.txt
13337 lines changed

# check
diff temp_pw_7.txt  temp_pw_7_work4.txt | wc -l
#0 expected

# get change file between ab_7 and ab_7_work4
python diff_to_changes_dict.py temp_pw_ab_7.txt temp_pw_ab_7_work4.txt temp_change_ab_7_3.txt
9 changes written to temp_change_ab_7_3.txt

# insert temp_change_ab_7_3.txt into change_pw_ab_7.txt

# revise
python updateByLine.py temp_pw_ab_6a.txt change_pw_ab_7.txt temp_pw_ab_7.txt
302 lines changed

# check
diff temp_pw_ab_7.txt  temp_pw_ab_7_work4.txt | wc -l
#0 expected
=========================================================================
THIS FINISHES THIS PHASE:  Now, temp_pw_7.txt and temp_pw_ab_7.txt are
the same in that each entry has the same NUMBER of italic text fragments.
=========================================================================

--------------------
Handle the few revisions mentioned by Andhrabharati at
 https://github.com/sanskrit-lexicon/PWK/issues/88#issuecomment-1740414273
 https://github.com/sanskrit-lexicon/PWK/issues/88#issuecomment-1740433718

cp temp_pw_7.txt temp_pw_7_work.txt
cp temp_pw_ab_7.txt temp_pw_ab_7_work.txt

Manual edits per the github comments.
REVIEW !!! AB comment discussion.

# get change file between 7 and 7_work

python diff_to_changes_dict.py temp_pw_7.txt temp_pw_7_work.txt temp_change_pw_7_24.txt
4  lines changed

# insert temp_change_pw_7_24.txt into change_pw_7.txt

python updateByLine.py temp_pw_6a.txt change_pw_7.txt temp_pw_7.txt
13341 lines changed

# check
diff temp_pw_7.txt  temp_pw_7_work.txt | wc -l
#0 expected

-------
# get change file between ab_7 and ab_7_work
python diff_to_changes_dict.py temp_pw_ab_7.txt temp_pw_ab_7_work.txt temp_change_ab_7_3.txt
6 changes written to temp_change_ab_7_3.txt

# insert temp_change_ab_7_3.txt into change_pw_ab_7.txt

# revise
python updateByLine.py temp_pw_ab_6a.txt change_pw_ab_7.txt temp_pw_ab_7.txt
308 lines changed

# check
diff temp_pw_ab_7.txt  temp_pw_ab_7_work.txt | wc -l
#0 expected

--------------------
Regen count frequency summaries using version 7.
python is_local1.py ../temp_pw_7.txt ../temp_pw_ab_7.txt is_local7.txt
105 lines written to is_local7.txt
0 differences in local abbreviations
42 distinct abbreviations

python is_glob0.py ../temp_pw_7.txt ../temp_pw_ab_7.txt is_glob7.txt
2 instances with different counts
3701 lines written to is_glob7.txt
Uttara Phalgunī	0,2	Different counts
Uttarā Phalgunī	2,0	Different counts
This is intentional.
  Ref: https://github.com/sanskrit-lexicon/PWK/issues/88#issuecomment-1740414273
       and following comments
       
--------------------
--------------------
--------------------
--------------------
--------------------
