pw_9_work
continue alternate headword (k2) work 
Ref: https://github.com/sanskrit-lexicon/PWK/issues/106
03-22-2024 begin

----------------------------------------------------------------
AB's supporting files:
  764942 temp.pw.cdsl.8a.txt
  764942 temp.pw.integrated.AB.v1.for.CDSL.txt

-------------
begin Jim notes re L=124384
temp_pw_8a
<L>124385<pc>7-121-b<k1>sAradIya<k2>sAradIya, (SAradIya), SAradIyanAmamAlA
{#sAradIya#} (besser {#SA°#}) <lex>Adj.</lex> (<lex>f.</lex> {#A#}) {#°nAmamAlA#}¦ <lex>f.</lex> Titel eines Werkes <ls>BÜHLER, Rep. No. 780</ls>.
cdsl.8a
<L>124385<pc>7-121-b<k1>sAradIya<k2>sAradIya, (SAradIya), SAradIyanAmamAlA
{#sAradIya#} (besser {#SA°#}) <lex>Adj.</lex> (<lex>f.</lex> {#A#}) {#°nAmamAlA#}¦ <lex>f.</lex> Titel eines Werkes <ls>BÜHLER, Rep. No. 780</ls>.

integrated
{#sAradIya#} (besser {#SA°#}) <lex>Adj.</lex> (<lex>f.</lex> {#A#}) {#°nAmamAlA#}¦ <lex>f.</lex> Titel eines Werkes <ls>BÜHLER, Rep. No. 780</ls>.
end Jim notes re L=124384


----------------------------------------------------------------
create change_8a_9.txt and temp_pw_9.txt
Add extra blank lines to temp_pw_8a.txt to facilitate comparison with
AB's two files.
touch ../change_8a_9.txt
# manually create 'ins' change transactions and put into change_8a_9.txt

# compute ../temp_pw_9.txt
cd ../
python updateByLine.py temp_pw_8a.txt change_8a_9.txt temp_pw_9.txt
764934 lines read from temp_pw_8a.txt
764942 records written to temp_pw_9.txt
8 change transactions from change_8a_9.txt
8 of type ins
----------------------------------------------------------------
0a  revise change_8a_9.txt and temp_pw_9.txt
L=2991  Remove an un-needed '_' at hiatus in temp_pw_9.txt
Manual addition to change_8a_9.txt  Change to 2 lines

# recompute ../temp_pw_9.txt
cd ../
python updateByLine.py temp_pw_8a.txt change_8a_9.txt temp_pw_9.txt
764934 lines read from temp_pw_8a.txt
764942 records written to temp_pw_9.txt
10 change transactions from change_8a_9.txt
8 of type ins, 2 of type new

----------------------------------------------------------------
create temp_pw_ab_1.txt and temp_pw_ab_2.txt
Reason: add the <info n="sup_N"/> field to the pwkvn records of AB's two files.
  This field is needed by the displays, and thus should be present in the pwX version.
  It is convenient to alter AB's two files before considering other differences
  between temp_pw_9.txt and AB's two files.
grep -E '<info n="sup_."/>' ../temp_pw_9.txt | wc -l
22611
22611 matches for "<info n="sup_."/>LINE_BREAK<LEND>" in temp_pw_9.txt

22611 will be the number of lines changed
------------------
create temp_pw_ab_1.txt =  temp.pw.cdsl.8a.txt with sups added.

python add_sup.py temp.pw.cdsl.8a.txt ../temp_pw_9.txt  temp_pw_ab_1.txt
764942 from temp.pw.cdsl.8a.txt
764942 from ../temp_pw_9.txt
nvns=22611, nsups=22611
add_sup changes 22611 lines
764942 lines written to temp_pw_ab_1.txt

diff ../temp_pw_9.txt temp_pw_ab_1.txt | wc -l
2272 about 500 lines changed

------------------
create temp_pw_ab_2.txt = temp.pw.integrated.AB.v1.for.CDSL.txt with sups added
python add_sup.py temp.pw.integrated.AB.v1.for.CDSL.txt ../temp_pw_9.txt  temp_pw_ab_2.txt

764942 from temp.pw.integrated.AB.v1.for.CDSL.txt
764942 from ../temp_pw_9.txt
nvns=22611, nsups=22611
add_sup changes 22611 lines
764942 lines written to temp_pw_ab_2.txt

diff temp.pw.cdsl.8a.txt temp.pw.integrated.AB.v1.for.CDSL.txt | wc -l
2984

diff temp_pw_ab_1.txt temp_pw_ab_2.txt | wc -l
2984 Same as above, as expected

Now, Let's anaylze further changes to ../temp_pw_9.txt based on
 - temp_pw_ab_1.txt and
 - temp_pw_ab_2.txt
 
----------------------------------------------------------------
1 Begin analysis of the temp_pw_ab_1.txt changes
construct ../change_9_9a.txt and ../temp_pw_9a.txt

python make_change_01.py '1' ../temp_pw_9.txt temp_pw_ab_1.txt temp_change_9_9a.txt

# manual edit of temp_change_9_9a.txt
  comment out the 2 lines which otherwise would change aDoakza to 'aDo_akza'.
# cp temp_change_9_9a.txt ../change_9_9a.txt
------------------
Begin explanation of change_9_9a.txt
 (refer function get_cat_1 in make_change_01.py)
 By observation, the differences between corresponding lines
 of ../temp_pw_9.txt and temp_pw_ab_1.txt
 can be categorized.
; cat=1:a: 364 changes  '¦ (!) ' -> ' (!)¦ '
  When '¦ (!) ' in a line of temp_pw_9 is changed to ' (!)¦ ', the result is
  the corresponding line of temp_pw_ab_1.txt.
  This explains the difference in 364 lines.
; cat=1:b: 19 changes   '¦(!) ' -> ' (!)¦ '
; cat=1:c: 138 changes  '¦ (?) ' -> ' (?)¦ '
; cat=1:d: 19 changes   '¦ (?) ' -> ' (?)¦ '
;  All of these 4 kinds of changes are accepted by Jim without further review.
; cat=1:other: 30 changes
  These differences must be examined manually, as none of the above transforms
  explains the difference.
  Jim accepts all but 2, namely the metaline and bbline of
 <L>2991<pc>1-035-c<k1>aDoakza. temp_pw_ removes the '_'.
End explanation of change_9_9a.txt
------------------

# compute ../temp_pw_9a.txt
cd ../
python updateByLine.py temp_pw_9.txt change_9_9a.txt temp_pw_9a.txt
764942 lines read from temp_pw_9.txt
764942 records written to temp_pw_9a.txt
568 change transactions from change_9_9a.txt
568 of type new

cd pw_9_work
diff ../temp_pw_9a.txt temp_pw_ab_1.txt | wc -l
# 6 (2 lines changed)

diff ../temp_pw_9a.txt temp_pw_ab_1.txt | wc -l
# 2

----------------------------------------------------------------
2 Begin analysis of the temp_pw_ab_2.txt changes
construct ../change_9a_9b.txt and ../temp_pw_9b.txt

python make_change_01.py '2' ../temp_pw_9a.txt temp_pw_ab_2.txt temp_change_9a_9b.txt

# manual edit of temp_change_9a_9b.txt
  
# cp temp_change_9a_9b.txt ../change_9a_9b.txt

# compute ../temp_pw_9b.txt
cd ../
python updateByLine.py temp_pw_9a.txt change_9a_9b.txt temp_pw_9b.txt
764942 lines read from temp_pw_9a.txt
764942 records written to temp_pw_9b.txt
735 change transactions from change_9a_9b.txt
735 of type new



remake multik2a.txt from multik2.txt
4 k1/k2 inconsitencies uncovered:  Changes added to ../change_9a_9b.txt
319220 old <L>64978<pc>4-054-c<k1>palAgratas<k2>palAgra, palAgratas
319220 new <L>64978<pc>4-054-c<k1>palAgra<k2>palAgra, palAgratas
; ----------------------------------------------
; <L>86893<pc>5-078-c<k1>miTaHspfDya<k2>miTaspf/Dya, miTaHspf/Dya
427692 old <L>86893<pc>5-078-c<k1>miTaHspfDya<k2>miTaspf/Dya, miTaHspf/Dya
427692 new <L>86893<pc>5-078-c<k1>miTaspfDya<k2>miTaspf/Dya, miTaHspf/Dya
; ----------------------------------------------
; <L>103170<pc>6-100-c<k1>viniHsfptAhuti<k2>vinisfptAhuti, viniHsfptAhuti
512055 old <L>103170<pc>6-100-c<k1>viniHsfptAhuti<k2>vinisfptAhuti, viniHsfptAhuti
512055 new <L>103170<pc>6-100-c<k1>vinisfptAhuti<k2>vinisfptAhuti, viniHsfptAhuti
; ----------------------------------------------
; <L>114226<pc>6-260-b<k1>SElavAlukAs<k2>SElavAlukA, SElavAlukAs
566805 old <L>114226<pc>6-260-b<k1>SElavAlukAs<k2>SElavAlukA, SElavAlukAs
566805 new <L>114226<pc>6-260-b<k1>SElavAlukA<k2>SElavAlukA, SElavAlukAs
;
# remake temp_pw_9b.txt
cd ../
python updateByLine.py temp_pw_9a.txt change_9a_9b.txt temp_pw_9b.txt
764942 records written to temp_pw_9b.txt
741 change transactions from change_9a_9b.txt

--------------------------
diff ../temp_pw_9b.txt temp_pw_ab_2.txt | wc -l
# 68 lines in diff
diff ../temp_pw_9b.txt temp_pw_ab_2.txt > diff_9b_ab_2.txt

--------------------------
revised:  (Jim disagrees with AB and AB's change is revised
---
; <L>219911<pc>7-363-a<k1>PARway<k2>PARway
753997 old !√{#PARway#}¦ <ab>Denomin.</ab> von {#PARwa#} <ls>DĀRILA</ls> [Page7-363-b] zu <ls>KAUŚ. 25,18</ls>.<info n="sup_7"/>
;
;753997 new !√{#PARway#}¦ <ab>Denomin.</ab> von {#PARwa#} <ls>DĀRILA [Page7-363-b] zu KAUŚ. 25,18</ls>.<info n="sup_7"/>
753997 new !√{#PARway#}¦ <ab>Denomin.</ab> von {#PARwa#} <ls>DĀRILA zu KAUŚ. 25,18</ls>.[Page7-363-b]<info n="sup_7"/>

--------------------------
questions TODO
-------------------
; <L>214779<pc>7-322-d<k1>uttaratantra<k2>uttaratantra
733270 old {#uttaratantra#}¦ I. <ab>Vgl.</ab> <ab>Anm.</ab> zu <ls>KAUŚ. 5,5</ls>.<info n="sup_7"/>
;
733270 new {#uttaratantra#}¦ I. <ab>Vgl.</ab> <ls><ab>Anm.</ab> zu KAUŚ. 5,5</ls>.<info n="sup_7"/>
TODO Such changes as this will make the ls-tooltips inaccessible.
 How to solve this problem?
Similarly, we will lose a link to RV. for 50+ such as
<ls>SĀY. zu ṚV. 5,30,1</ls>
----------------------------------------------------------------
Check that display construction with 9b works properly
cd ../
sh redolocal.sh 9b
# xml file is fine
***********************************************************
-----------------------------------------------------------
test reconstruction of csl-orig/v02/pw/pw_hwextra.txt
First, work in temporary folder /c/xampp/htdocs/cologne/csl-orig/v02/pw/temp_to_install/
cp temp_pw_9b.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/temp_to_install/pw.txt
cd /c/xampp/htdocs/cologne/csl-orig/v02/pw/temp_to_install/
cd althws
# reconstructs ../pw_hwextra.txt
sh redo.sh
---------------------


-----------------------------------------------------------
-----------------------------------------------------------
-----------------------------------------------------------
THE END
-----------------------------------------------------------
