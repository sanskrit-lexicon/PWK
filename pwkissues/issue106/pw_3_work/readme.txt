Analysis of AB feedback for version 3 of pw.
Files from Andhrabharati

3367191 Feb 22 20:39 pwkvn_2.CDSL.txt       separate vndata 
2286032 Feb 22 20:40 temp_pwkvn_2.CDSL.txt  delete metaline
1902984 Feb 22 20:40 temp_pwkvn_2.AB.txt    AB corresponding
   5668 Feb 22 20:41 dhAtu.header.lines.txt 

temp_pwkvn_2.CDSL.txt -> temp1_pwkvn_2.CDSL.txt
 remove <info n="sup.*$>

diff -w temp1_pwkvn_2.CDSL.txt temp_pwkvn_2.AB.txt | wc -l
1800
(/ 1800 4) = 450

157 matches in 156 lines for "!√" in buffer: temp_diff_pwkvn_cdsl_ab.txt

Another large category: difference in placement of ¦

---------------------------------------------------------
touch ../change_2_3.txt
cp ../temp_pw_2.txt ../temp_pw_3.txt
-----------------------------------
01: root markup !√
python make_change.py 01 ../temp_pw_3.txt temp_pwkvn_2.CDSL.txt temp_pwkvn_2.AB.txt temp_change_2_3_01.txt temp_pwkvn_2.CDSL_01.txt
764479 from ../temp_pw_2.txt
90460 from temp_pwkvn_2.CDSL.txt
90460 from temp_pwkvn_2.AB.txt
22611 22611
adjust_lines2a: nsame=22161, ndiff=450
149 changes
150 records written to temp_change_2_3_01.txt
22611 lines written to temp_pwkvn_2.CDSL_01.txt

# insert temp_change_2_3_01.txt into change_2_3.txt
# revise temp_pw_3.txt
python ../updateByLine.py ../temp_pw_2.txt ../change_2_3.txt ../temp_pw_3.txt
764479 lines read from ../temp_pw_2.txt
764479 records written to ../temp_pw_3.txt
149 change transactions from ../change_2_3.txt

-----------------------------------
02: root markup √
python make_change.py 02 ../temp_pw_3.txt temp_pwkvn_2.CDSL_01.txt temp_pwkvn_2.AB.txt temp_change_2_3_02.txt temp_pwkvn_2.CDSL_02.txt

764479 from ../temp_pw_3.txt
22611 from temp_pwkvn_2.CDSL_01.txt
90460 from temp_pwkvn_2.AB.txt
22611 22611
adjust_lines2a: nsame=22310, ndiff=301
243 changes
244 records written to temp_change_2_3_02.txt
22611 lines written to temp_pwkvn_2.CDSL_02.txt

# insert temp_change_2_3_02.txt into change_2_3.txt
# revise temp_pw_3.txt
python ../updateByLine.py ../temp_pw_2.txt ../change_2_3.txt ../temp_pw_3.txt
764479 lines read from ../temp_pw_2.txt
764479 records written to ../temp_pw_3.txt
392 change transactions from ../change_2_3.txt

-----------------------------------
03: broken-bar placement ¦
python make_change.py 03 ../temp_pw_3.txt temp_pwkvn_2.CDSL_02.txt temp_pwkvn_2.AB.txt temp_change_2_3_03.txt temp_pwkvn_2.CDSL_03.txt

764479 from ../temp_pw_3.txt
22611 from temp_pwkvn_2.CDSL_02.txt
90460 from temp_pwkvn_2.AB.txt
22611 22611
adjust_lines2a: nsame=22553, ndiff=58
47 changes
48 records written to temp_change_2_3_03.txt
22611 lines written to temp_pwkvn_2.CDSL_03.txt

# insert temp_change_2_3_03.txt into change_2_3.txt
# Note: Add manual change to metalines for some of these
#      40 metalines changed
Note: 207313 ?  Diff in accent only. This impacts 'althws' program in csl-orig
Note: 208905 ? two identical {#X#} before ¦

# revise temp_pw_3.txt
python ../updateByLine.py ../temp_pw_2.txt ../change_2_3.txt ../temp_pw_3.txt
764479 lines read from ../temp_pw_2.txt
764479 records written to ../temp_pw_3.txt
479 (439 + 40) change transactions from ../change_2_3.txt

-----------------------------------
04:  the rest  BUT THESE ARE NOT CHANGED in temp_pw_3 ! Root markup retained
python make_change.py 04 ../temp_pw_3.txt temp_pwkvn_2.CDSL_03.txt temp_pwkvn_2.AB.txt temp_change_2_3_04.txt temp_pwkvn_2.CDSL_04.txt

764479 from ../temp_pw_3.txt
22611 from temp_pwkvn_2.CDSL_03.txt
90460 from temp_pwkvn_2.AB.txt
22611 22611
adjust_lines2a: nsame=22600, ndiff=11
11 changes
12 records written to temp_change_2_3_04.txt
22611 lines written to temp_pwkvn_2.CDSL_04.txt

NOTE: These 11 REMOVE root markup.
However, These really ARE roots!
So, the root markup is proper
-----------------------------------------------------------------------
02-26-2024  continue with the change_2_3 work, based on
AB comments starting at
https://github.com/sanskrit-lexicon/PWK/issues/106#issuecomment-1962257729

-------------
L=208905  correct change_2_3
  'und {#cAturvedya#}' -> 'und {#cAturvEdya#}'
------------
temp_change_2_3.AB.txt downloaded from issues/106 comment
 This file has 28 lines
AB corrections to change_2_3.txt
--- 1.
202368  aBramupriya  - keep aBramupriyatama as 2nd hw
<L>202368<pc>2-291-a<k1>aBramupriya<k2>aBramupriya, aBramupriyatama
--- 2.
<L>208941 metaline two words:
 <L>208941<pc>6-301-c<k1>QuRQika<k2>QuRQika, QuRQikA
--- 3.
<L>220478  metaline two words:
755923 new <L>220478<pc>7-368-a<k1>mArjana<k2>mArjana, mArjanA
--- 4. accent on 2nd word in metaline
<L>222605<pc>7-389-d<k1>vaDASaNka<k2>vaDASaNka, vaDASaNkA/

-----------------------------------------------------------------------
The 11 entries where Jim had √ markup temp_change_23_04.txt
https://github.com/sanskrit-lexicon/PWK/issues/106#issuecomment-1962284200
This relates to temp_change_23_04.txt
From AB: temp_change_2_3_04.AB.txt
 Manually edit temp_change_23_04.txt
 Summary:
--- 1. 
 <L>207223<k1>cawacaw  Jim: Accept root markup
 √{#cawacaw#}¦, {#°wati#}
  The comp. with L-202889 [{#kawakkawiti#} is not applicable due to 'wati'
--- 2. 
  <L>208158<k1>ripav
  !√{#ripav#}¦, {#°vati#}
--- 3.
  <L>208840<k1>kElAs
  !√{#kElAs#}
--- 3.
  <L>208856<k1>kzIrod
  !√{#kzIrod#}
--- 4.
  <L>208980<k1>darpaR
  !√{#darpaR#}
--- 5.
  <L>209138<k1>pratibimb
  <pc>6-303-c
--- 6.
  <L>209263<k1>mAtaNgavedi
  spelling correction: varaRqaka -> vAraRqaka
--- 7.
  <L>209811<k1>aNku
  !√{#aNkur#}¦
--- 8.
  <L>211639<k1>apattana
  spelling correction: DIVYĀDAD. -> DIVYĀVAD.
--- 9.
  <L>217651<pc>7-344-b<k1>JaMkfti<k2>JaMkfti, Jaw
  Add JaRajJaRatkArin to k2 in metaline
--- 10. <L>220244<pc>7-366-a<k1>Bramaraketu<k2>Bramaraketu, BramarAy
  Add BrastA to k2 in metaline

# Manually insert temp_change_2_3_04.txt (as revised) into change_2_3.txt
# recompute temp_pw_3.txt
python ../updateByLine.py ../temp_pw_2.txt ../change_2_3.txt ../temp_pw_3.txt

764479 lines read from ../temp_pw_2.txt
764479 records written to ../temp_pw_3.txt
490 change transactions from ../change_2_3.txt


-----------------------------------------------------------------------
05: Additional dhatu markup
Based on dhAtu.header.lines.txt (206 lines)
python make_change_dhatu_header.py ../temp_pw_3.txt dhAtu.header.lines.txt temp_change_2_3_05.txt
764479 from ../temp_pw_3.txt
206 from dhAtu.header.lines.txt
206 changes
statuses =  [116, 11, 54, 5, 20]
211 records written to temp_change_2_3_05.txt

# manually edit temp_change_2_3_05.txt: (the 20 under '05.5')

# manually insert temp_change_2_3_05.txt into change_2_3.txt
# recompute temp_pw_3.txt
python ../updateByLine.py ../temp_pw_2.txt ../change_2_3.txt ../temp_pw_3.txt

764479 lines read from ../temp_pw_2.txt
764479 records written to ../temp_pw_3.txt
716 change transactions from ../change_2_3.txt
---------
NOTES: from above 05.05 section
---
!√{#jaNgah#}  Not denominative, but intensive
---
L=113514, √{#sunD#} -> √{#SunD#}

764479 from ../temp_pw_3.txt
206 from dhAtu.header.lines.txt


-----------------------------------------------------------------------
02-26-2024
06: Chr markup corrections
https://github.com/sanskrit-lexicon/PWK/issues/106#issuecomment-1962267606
https://github.com/sanskrit-lexicon/PWK/issues/106#issuecomment-1962272047
https://github.com/sanskrit-lexicon/PWK/issues/106#issuecomment-1962275700

Process AB files:
non-Chr.citations.txt       30 lines in file
non-Chr.citation.lines.txt 120 lines

python make_change_non_chr_lines.py ../temp_pw_3.txt non-Chr.citation.lines.txt non-Chr.citations.txt temp_change_2_3_06.txt

764479 from ../temp_pw_3.txt
120 from non-Chr.citation.lines.txt
n=120, k=4, q=30, len(groups)=30
30 records initialized from non-Chr.citation.lines.txt
30 from non-Chr.citations.txt
30 changes
statuses =  [30]
30 records written to temp_change_2_3_06.txt

# manual insert temp_change_2_3_06.txt into change_2_3.txt
python ../updateByLine.py ../temp_pw_2.txt ../change_2_3.txt ../temp_pw_3.txt

746 change transactions from ../change_2_3.txt

--------------------------------------------------------
07: 'ks' -> 'kz' corrections in pw
106 matches in 102 lines for "{#[^#]*ks" in buffer: temp_pw_3.txt
cp temp_pw_3.txt temp_pw_3work.txt
# manually edit temp_pw_3work.txt, examining those 106 and making changes.
# generate changes
python ../diff_to_changes_dict.py ../temp_pw_3.txt ../temp_pw_3work.txt temp_change_2_3_07.txt
# 19 changes written to temp_change_2_3_07.txt

# manual insert temp_change_2_3_07.txt into change_2_3.txt
python ../updateByLine.py ../temp_pw_2.txt ../change_2_3.txt ../temp_pw_3.txt

# recompute temp_pw_3
python ../updateByLine.py ../temp_pw_2.txt ../change_2_3.txt ../temp_pw_3.txt

765 change transactions from ../change_2_3.txt

rm temp_pw_3work.txt


--------------------------------------------------------
08:  corrections where more than one ¦ (3 instances)

# manual insert pw_4_work/temp_bbmulti_errors.txt into change_2_3.txt

# recompute temp_pw_3
python ../updateByLine.py ../temp_pw_2.txt ../change_2_3.txt ../temp_pw_3.txt

768 change transactions from ../change_2_3.txt

--------------------------------------------------------
09: regarding altheadwords
1 instance so far

# manual add to change_2_3.txt

# recompute temp_pw_3
python ../updateByLine.py ../temp_pw_2.txt ../change_2_3.txt ../temp_pw_3.txt

770 change transactions from ../change_2_3.txt
----------------------------------------------------------
----------------------------------------------------------

TODO: BTW, it is noted that ~1000 Chr. instances having multiple citations together are still not expanded as individual (separate) citations.
For example, the entry aMhas has <ls n="Chr.">1,10. 6,18</ls> that does not lead to the 6,18 link.

46 matches for "<ls>Chr. [^<]* " in buffer: temp_pw_3.txt
749 matches in 706 lines for "<ls n="Chr\..*?> [^<]* " in buffer: temp_pw_3.txt


--------------------------------------------------------
TODO: 
/c/xampp/htdocs/cologne/csl-orig/v02/pw/temp_to_install
move 'up' to pw directory
Modify to handle accent-equivalents

-----------------------------------------------------------------------
TODO:  correct pdf page display problems (
-----------------------------------------------------------------------
