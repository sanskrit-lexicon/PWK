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
09-04-2023
python ab_local_tm.py ../temp_pw_4.txt ab_local_tm_0.txt
843 entries contain a local abbreviation
******************************************************
09-09-2023
User corrections to pw.  20 lines changed
These are reflected in ../change_pw_4.txt and change_pw_ab_4.txt.
See also user_change_notes.txt and user_change_notes_ab.txt
******************************************************

