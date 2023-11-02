ls

10-31-2023 begin.



--------------------------------------------------------------
Version 11a
Systematic difference in punctuation:

grep -E '[0-9][.]</ls>' temp_pw_11.txt | wc -l
51082
grep -E '[0-9][.]</ls>' temp_pw_ab_11.txt | wc -l
5
----
grep -E '[0-9]</ls>[.]' temp_pw_11.txt | wc -l
790
----
grep -E '[0-9]</ls>[.]' temp_pw_ab_11.txt | wc -l
51720

# Change to cdsl to remove most differences in this detail.
python period_outside.py ../temp_pw_11.txt ../temp_pw_11a.txt
51082 lines changed

grep -E '[0-9]</ls>[.]' temp_pw_11a.txt | wc -l
51851
There are still differences, but these should get resolved later,


--------------------------------------------------------------
Version 11b
python ../ablists/regex_compare_texts1.py '<ls>.*?</ls>' ../temp_pw_11a.txt ../temp_pw_ab_11.txt temp1.org 
3556 cases written to temp1.org
Example:
cdsl: <ab>Comm.</ab> zu <ls>KĀTY. ŚR. 20,3,14</ls>
  ab: <ls><ab>Comm.</ab> zu KĀTY. ŚR. 20,3,14</ls>
# change cdsl form to ab form 
python comm_in_ls.py ../temp_pw_11a.txt ../temp_pw_11b.txt
1667 lines changed

--------------------------------------------------------------
Version 11c
728 matches in 719 lines for "[0-9])[.]</ls> in temp_pw_11b.txt
0 matches in temp_pw_ab_11.txt

# move the period outside in this context
python period_outside1.py ../temp_pw_11b.txt ../temp_pw_11c.txt
# 719 lines changed

python ../ablists/regex_compare_texts1.py '<ls>.*?</ls>' ../temp_pw_11c.txt ../temp_pw_ab_11.txt temp1.org 
1399 cases

--------------------------------------------------------------
Version 11d
417 matches in 359 lines for "<ls><ab>ebend.</ab></ls>" in buffer: temp_pw_ab_11.txt
336 matches in 316 lines for "[^>]<ab>ebend.</ab>" in buffer: temp_pw_11b.txt

python ebend.py ../temp_pw_11c.txt ../temp_pw_11d.txt
324 lines changed

--------------------------------------------------------------
Version 11e
9 matches for "<ls>Nachtr\." in buffer: temp_pw_11b.txt
373 matches in 368 lines for "<ls>Nachtr. [0-9]+</ls>" in buffer: temp_pw_ab_11.txt

python nachtr.py ../temp_pw_11d.txt ../temp_pw_11e.txt
360 lines changed

python ../ablists/regex_compare_texts1.py '<ls>.*?</ls>' ../temp_pw_11e.txt ../temp_pw_ab_11.txt temp1.org 
811


--------------------------------------------------------------
version 11f

215 matches in 213 lines for "<ab>Sch.</ab></ls>" in buffer: temp_pw_ab_11.txt
9 matches for "<ab>Sch.</ab></ls>" in buffer: temp_pw_11e.txt
219 matches in 217 lines for "<ab>Sch.</ab>" in buffer: temp_pw_11e.txt
189 matches in 188 lines for "<ls>\([^<]*\)</ls>, <ab>Sch.</ab>" in buffer: temp_pw_11e.txt


python sch_ls.py ../temp_pw_11e.txt ../temp_pw_11f.txt
204 lines changed

python ../ablists/regex_compare_texts1.py '<ls>.*?</ls>' ../temp_pw_11f.txt ../temp_pw_ab_11.txt temp1.org 
610 cases written to temp1.org


--------------------------------------------------------------
version 11g
61 matches in 60 lines for "<ls>Einl\. zu" in buffer: temp_pw_ab_11.txt
2 matches for "<ls>Einl\. zu" in buffer: temp_pw_11f.txt

python einl_zu.py ../temp_pw_11f.txt ../temp_pw_11g.txt
58 lines changed

python ../ablists/regex_compare_texts1.py '<ls>.*?</ls>' ../temp_pw_11g.txt ../temp_pw_ab_11.txt temp1.org 
553 cases written to temp1.org


--------------------------------------------------------------
version 11h

84 matches for "</ls>, <ls>Vārtt\." in buffer: temp_pw_11g.txt
none in temp_pw_ab_11.txt

python vartt.py ../temp_pw_11g.txt ../temp_pw_11h.txt
124 lines changed

python ../ablists/regex_compare_texts1.py '<ls>.*?</ls>' ../temp_pw_11h.txt ../temp_pw_ab_11.txt temp1.org 
435 cases written to temp1.org

--------------------------------------------------------------
version 11i

52 matches for "Text zu <ls>" in buffer: temp_pw_11g.txt
54 matches for "<ls>Text zu " in buffer: temp_pw_ab_11.txt


python text_zu.py ../temp_pw_11h.txt ../temp_pw_11i.txt
52 lines changed

python ../ablists/regex_compare_texts1.py '<ls>.*?</ls>' ../temp_pw_11i.txt ../temp_pw_ab_11.txt temp1.org 
388 cases written to temp1.org

--------------------------------------------------------------
Version 11j

52 matches in 48 lines for "<ls><ab>ebend.</ab></ls> <ls " in buffer: temp_pw_11i.txt
None in temp_pw_ab_11.txt

python ebend1.py ../temp_pw_11i.txt ../temp_pw_11j.txt
48 lines changed

python ../ablists/regex_compare_texts1.py '<ls>.*?</ls>' ../temp_pw_11j.txt ../temp_pw_ab_11.txt temp1.org 
384 cases
--------------------------------------------------------------
Version 11k
 Miscellaneous
 1. '<ls>VP.² 1,' -> '<ls>VP.² 1, '   15
 2. ')\.</ls>'    -> ')</ls>.'        17
 3. '</ls> im <ls>ŚKDR.</ls>'  -> ' im ŚKDR.</ls>'  8
 4. Example: (35 cases)
cdsl: <ls>ŚAṂK. zu BĀDAR. 2,2,17</ls> (S. 539, Z. 1 <ab>v. u.</ab>)
  AB: <ls>ŚAṂK. zu BĀDAR. 2,2,17 (S. 539, Z. 1 <ab>v. u.</ab>)</ls>



python misc1.py ../temp_pw_11j.txt ../temp_pw_11k.txt


python ../ablists/regex_compare_texts1.py '<ls>.*?</ls>' ../temp_pw_11k.txt ../temp_pw_ab_11.txt temp1.org 
326


--------------------------------------------------------------
temp_pw_ab_11a.txt, temp_pw_11m.txt  (skipping temp_pw_11l.txt - hard to read)

python ebend2.py ../temp_pw_ab_11.txt ../temp_pw_ab_11a.txt
28 lines changed

python ebend2.py ../temp_pw_11k.txt ../temp_pw_11m.txt
8 lines changed

python ../ablists/regex_compare_texts1.py '<ls>.*?</ls>' ../temp_pw_11m.txt ../temp_pw_ab_11a.txt temp1.org 
306 cases


--------------------------------------------------------------

Manual adjust of the 349 cases

cp ../temp_pw_11m.txt ../temp_pw_12_work.txt
cp ../temp_pw_ab_11a.txt ../temp_pw_ab_12_work.txt

cp ../
Also include '<ls n="...">X</ls>' forms:

python ../ablists/regex_compare_texts1.py '<ls.*?</ls>' ../temp_pw_12_work.txt ../temp_pw_ab_12_work.txt temp1.org  ../temp_pw_12_work1.txt ../temp_pw_ab_12_work1.txt
349 cases

Manual edit of ../temp_pw_12_work1.txt ../temp_pw_ab_12_work1.txt to
resolve differences.

Remove temp markup ('* <L>' -> '<L>') in temp_pw_12_work1.txt, save as
  temp_pw_12_work.txt

# Generate changes 
python diff_to_changes_dict.py temp_pw_11m.txt temp_pw_12_work.txt ls/temp_change_pw_12_1.txt
360 changes written to ls/temp_change_pw_12_1.txt

touch change_pw_12.txt
# insert ls/temp_change_pw_12_1.txt into change_pw_12.txt

# generate temp_pw_12.txt
python updateByLine.py temp_pw_11m.txt change_pw_12.txt temp_pw_12.txt
360 change transactions from change_pw_12.txt
# check
diff temp_pw_12.txt temp_pw_12_work.txt | wc -l
# 0 as expected

-----
Remove temp markup ('* <L>' -> '<L>') in temp_pw_ab_12_work1.txt, save as
  temp_pw_ab_12_work.txt

# Generate changes for temp_pw_ab_11a.txt
python diff_to_changes_dict.py temp_pw_ab_11.txt temp_pw_ab_11a.txt ls/temp_change_pw_ab_12_1.txt
28 changes written to ls/temp_change_pw_ab_12_1.txt

touch change_pw_ab_12.txt

# manual insert ls/temp_change_pw_ab_12_1.txt into change_pw_ab_12.txt

# Generate changes 
python diff_to_changes_dict.py temp_pw_ab_11a.txt temp_pw_ab_12_work.txt ls/temp_change_pw_ab_12_2.txt
26 changes written to ls/temp_change_pw_ab_12_2.txt

# manual insert ls/temp_change_pw_ab_12_2.txt

# generate temp_pw_ab_12.txt
python updateByLine.py temp_pw_ab_11.txt change_pw_ab_12.txt temp_pw_ab_12.txt
54 change transactions from change_pw_12.txt
# check
diff temp_pw_ab_12.txt temp_pw_ab_12_work.txt | wc -l
# 0 as expected

# check that the version 12 files are the same relative to '<ls>' markup:
python ../ablists/regex_compare_texts1.py '<ls.*?</ls>' ../temp_pw_12.txt ../temp_pw_ab_12.txt temp1.org 
0 cases written to temp1.org  # as expected

**************************************************************

--------------------------------------------------------------

#*************************************************************************
11-02-2023
install in csl-orig, etc.
*************************************************************************

-------------------------------------
Install temp_pw_12.txt in csl-orig repository, and update displays
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue88

-----------------------
# do local install
cp temp_pw_12.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt

# check local installation
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pw  ../../pw
sh xmlchk_xampp.sh pw
# ok
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue88

# push repositories to GitHub
----- csl-orig
cd /c/xampp/htdocs/cologne/csl-orig
git pull # check for other revisions. 
git status  # v02/pw/pw.txt
git add .
git commit -m "PW: Revise pw.txt based on temp_pw_12.txt (ls tag)
  Ref: https://github.com/sanskrit-lexicon/PWK/issues/88"
# 52733 lines changed
git push

--------------------------------------------
# update cologne displays
# login to cologne
---- csl-orig
git pull
# 52733 lines changed

---- csl-pywork
cd v02
sh generate_dict.sh pw  ../../PWScan/2020/

--------------------------------------------
# sync this repository to Github
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue88

git add .
git commit -m "temp_pw_12, temp_pw_ab_12. (ls resolution) #88"
git push



*************************************************************
--------------------------------------------------
QUESTIONS:
 <L>22553<pc>1275-3<k1>ElaDAna
----
<L>35287<pc>2164-1<k1>gAnDarva<
(<ab>compon.</ab> 116,21)
----
