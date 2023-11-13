lineadj/readme.txt
Begin 11-10-2023

Work with files from Andhrabharti posted at
  https://github.com/sanskrit-lexicon/PWK/issues/88#issuecomment-1805934572
AB prepared a cdsl version and an AB version WITH SAME NUMBER OF LINES
 wc -l temp*.txt
  682113 lineadj/temp_pw-d.txt   (From AB, based on ../temp_pw_15.txt)
  682113 lineadj/temp_pw_ab_15d.txt  (fron AB, based on ../temp_pw_ab_15.txt)
matching.line.counts.in.pw.with.pw_ab_15.txt describes the steps AB took
  in order to get the number of lines the same.

By contrast,  
 wc -l temp_pw_15.txt temp_pw_ab_15.txt
  682608 temp_pw_15.txt
  674189 temp_pw_ab_15.txt

Thus, there are (- 682608 682113) = 495 more lines
  in temp_pw_15.txt than in temp_pw-d.txt

-----------------------------------------------
Part 0:
Resolve metaline diffs between temp_pw-d.txt and temp_pw_ab_15d.txt
It was noticed that the location of metalines differs slightly.

# make temp 'next versions' of these
cp temp_pw_ab_15d.txt temp_pw_ab_15e.txt
cp temp_pw-d.txt temp_pw-e.txt

# manually adjust temp_pw_ab_15e.txt, temp_pw-e.txt to resolve metaline diffs
# Iteratively, run first_L_diff.py to identify first
# case where a given metaline occurs at different line-numbers in the
# two files.   Modify temp_pw-e.txt to resolve this difference.
# Keep doing this until no differences remain.
# Note this required no change to 
python first_L_diff.py temp_pw_ab_15e.txt temp_pw-e.txt

# After resolution, list the diffs
diff temp_pw-d.txt temp_pw-e.txt > diff_pw-d_pw-e.txt  # only 19 lines

diff temp_pw_ab_15d.txt temp_pw_ab_15e.txt | wc -l
#0  (no diff)

wc -l temp_pw-e.txt temp_pw_ab_15e.txt
  682113 temp_pw-e.txt
  682113 temp_pw_ab_15e.txt

These two files still have same number of lines.


-------------------------------------------------

Part 1: 

# make 'systematic' adjustments (remove blank lines, etc.)
#  to the previous cdsl version (../temp_pw_15.txt). 
 python lineadj.py ../temp_pw_15.txt ../temp_pw_16a.txt

python lineadj.py ../temp_pw_15.txt ../temp_pw_16a.txt
1: # lines 682608 -> 682073
 remove blank lines within entry
 lines starting with <LEND> must = <LEND>
2: # lines 682073 -> 682149
 <div X> markup occurs at beginning of lines
 e.g., X<divY>Z -> X\n<divY>Z
3: # lines 682149 -> 682093
 at most one blank line between entries
4: # lines 682093 -> 682101
  at least one blank line between entries
682101 written to ../temp_pw_16a.txt

Provide a records of the diffs.  
diff ../temp_pw_15.txt ../temp_pw_16a.txt > diff_pw_15-pw_16a.txt
 (1519 lines in  diff_pw_15-pw_16a.txt)
 
-------------------------------------------------
Part 2:
cp ../temp_pw_16a.txt ../temp_pw_16b.txt

# make manual changes to ../temp_pw_16b.txt so metaline agreement with
   temp_pw-e.txt
   
python first_L_diff.py ../temp_pw_16b.txt temp_pw-e.txt
# When adjusted, All metalines are the same, and occur at the same line-number.

diff ../temp_pw_16a.txt ../temp_pw_16b.txt > diff_pw_16a-pw_16b.txt
# 98 lines in diff. about 20 changes.

# check that ../temp_pw_16b.txt and temp_pw_ab_15e.txt are aligned.
# 
wc -l ../temp_pw_16b.txt temp_pw_ab_15e.txt
  682113 ../temp_pw_16b.txt
  682113 temp_pw_ab_15e.txt
 
--- so same number of lines

python first_L_diff.py ../temp_pw_16b.txt temp_pw_ab_15e.txt
# All metalines are the same, and occur at the same line-number

# To summarize:
when comparing temp_pw_16b.txt (cdsl) and temp_pw_ab_15e.txt (ab)
a.  the two files have same number of lines (682113)
b.  metalines occur at the same line-numbers
c.  metaline texts are identical

-----------------------------------------------
Part 3:

We can now resolve all diffs between temp_pw_16b.txt and temp_pw_ab_15e.txt

# There are 1544 lines which are different.
python ../diff_to_changes_dict.py ../temp_pw_16b.txt temp_pw_ab_15e.txt temp.txt
1544 lines are different.

# Adjustments to temp_pw_16b will be done in copy temp_pw_16c.
cp temp_pw_16b.txt temp_pw_16c.txt

# Recall temp_pw_ab_15d.txt == temp_pw_ab_15e.txt
# Prepare a copy of temp_pw_ab_15e, where changes will be made.
cp lineadj/temp_pw_ab_15e.txt lineadj/temp_pw_ab_15e_work.txt

touch change_pw_16.txt

--------------------------
We begin resolving differences by several programmatic changes to
the cdsl version.  These changes are made by comparing
  lines in 16c and ab_15e_work, and modifying 16c accordingly
the process is iterative, done in 8 steps (Part 3.1 through 3.8)

Part 3.1:
  16c has an extra period
python diff_to_changes_dict1.py 1 ../temp_pw_16c.txt temp_pw_ab_15e_work.txt temp_change_1.txt
457 changes written to temp_change_1.txt

# install these changes
# manually insert temp_change_1.txt into change_pw_16.txt

# regenerate temp_pw_16c.txt
python updateByLine.py temp_pw_16b.txt change_pw_16.txt temp_pw_16c.txt
457 change transactions

python ../diff_to_changes_dict.py ../temp_pw_16c.txt temp_pw_ab_15e.txt temp.txt
1087 changes written to temp.txt

--------------------------
Part 3.2:
X<ab> -> X <ab> (one instance)
python diff_to_changes_dict1.py 2 ../temp_pw_16c.txt temp_pw_ab_15e_work.txt temp_change_2.txt
195 lines changed

# manually insert temp_change_2.txt into change_pw_16.txt

# regenerate temp_pw_16c.txt
python updateByLine.py temp_pw_16b.txt change_pw_16.txt temp_pw_16c.txt
652 change transactions

python ../diff_to_changes_dict.py ../temp_pw_16c.txt temp_pw_ab_15e.txt temp.txt
892 changes written to temp.txt

--------------------------
Part 3.3:
# cdsl missing period at end of line

python diff_to_changes_dict1.py 3 ../temp_pw_16c.txt temp_pw_ab_15e_work.txt temp_change_3.txt
272 lines changed

# manually insert temp_change_3.txt into change_pw_16.txt
# regenerate temp_pw_16c.txt
python updateByLine.py temp_pw_16b.txt change_pw_16.txt temp_pw_16c.txt
924 change transactions

python ../diff_to_changes_dict.py ../temp_pw_16c.txt temp_pw_ab_15e.txt temp.txt
620 changes written to temp.txt

--------------------------
Part 3.4:
# cdsl has an extra comma

python diff_to_changes_dict1.py 4 ../temp_pw_16c.txt temp_pw_ab_15e_work.txt temp_change_4.txt
26 lines changed

# manually insert temp_change_4.txt into change_pw_16.txt
# regenerate temp_pw_16c.txt
python updateByLine.py temp_pw_16b.txt change_pw_16.txt temp_pw_16c.txt
950 change transactions

python ../diff_to_changes_dict.py ../temp_pw_16c.txt temp_pw_ab_15e.txt temp.txt
594 changes written to temp.txt

--------------------------
Part 3.5
</ab>X -> </ab> X:

python diff_to_changes_dict1.py 5 ../temp_pw_16c.txt temp_pw_ab_15e_work.txt temp_change_5.txt
9 lines changed

# manually insert temp_change_5.txt into change_pw_16.txt

# regenerate temp_pw_16c.txt
python updateByLine.py temp_pw_16b.txt change_pw_16.txt temp_pw_16c.txt
959 change transactions

python ../diff_to_changes_dict.py ../temp_pw_16c.txt temp_pw_ab_15e.txt temp.txt
585 changes written to temp.txt

--------------------------
Part 3.6
cdsl and AB lines differ in length by 1, and have <= 200 characters

python diff_to_changes_dict1.py 6 ../temp_pw_16c.txt temp_pw_ab_15e_work.txt temp_change_6.txt
210 lines 

# manually edit temp_change_6.txt and confirm the corrections
#  Several changes were excluded, and these differences will be
#  revisited in a later step.
#  179 changes remain
# manually insert revised temp_change_6.txt into change_pw_16.txt

# regenerate temp_pw_16c.txt
python updateByLine.py temp_pw_16b.txt change_pw_16.txt temp_pw_16c.txt
1138 change transactions

python ../diff_to_changes_dict.py ../temp_pw_16c.txt temp_pw_ab_15e.txt temp.txt
406 changes written to temp.txt

--------------------------
Part 3.7
cdsl and AB have same length. They differ in one character

python diff_to_changes_dict1.py 7 ../temp_pw_16c.txt temp_pw_ab_15e_work.txt temp_change_7.txt
192 lines 

# accept, without check,
#  all the changes in temp_change_7.txt and confirm the corrections
# manually insert revised temp_change_6.txt into change_pw_16.txt

# regenerate temp_pw_16c.txt
python updateByLine.py temp_pw_16b.txt change_pw_16.txt temp_pw_16c.txt
1330 change transactions

python ../diff_to_changes_dict.py ../temp_pw_16c.txt temp_pw_ab_15e.txt temp.txt
214 changes written to temp.txt

--------------------------
Part 3.8
cdsl and AB have same length. 

python diff_to_changes_dict1.py 8 ../temp_pw_16c.txt temp_pw_ab_15e_work.txt temp_change_8.txt
53 lines 

# accept, with check,
#  all the changes in temp_change_8.txt 
# manually insert revised temp_change_6.txt into change_pw_16.txt

# regenerate temp_pw_16c.txt
python updateByLine.py temp_pw_16b.txt change_pw_16.txt temp_pw_16c.txt
1383 change transactions

python ../diff_to_changes_dict.py ../temp_pw_16c.txt temp_pw_ab_15e.txt temp.txt
161 changes written to temp.txt


-----------------------------------------------
Part 4
Manual examination of remaining 161 cases.
May have changes to temp_pw_ab_15e.
The two work1 files are constructed with
temporary markup to identify lines to change.
The temp1.org file helps find the location within the corresponding
 lines that are different.
 
python diff_to_changes_dict2.py 1 ../temp_pw_16c.txt temp_pw_ab_15e_work.txt temp1.org ../temp_pw_16c_work1.txt ../temp_pw_ab_15e_work1.txt

# manual changes to ../temp_pw_16c_work1.txt ../temp_pw_ab_15e_work1.txt
# to resolve differences.

# remove temporary markup in the work1 files, saving as work files:
../temp_pw_16c_work.txt ../temp_pw_ab_15e_work.txt
# These files are NOW IDENTICAL

# generate changes for cdsl version
python ../diff_to_changes_dict.py ../temp_pw_16c.txt ../temp_pw_16c_work.txt temp_change_9.txt
165 changes

# manually insert temp_change_9.txt into ../change_pw_16.txt
# regenerate ../temp_pw_16c.txt
cd ../
python updateByLine.py temp_pw_16b.txt change_pw_16.txt temp_pw_16c.txt
# check
diff temp_pw_16c.txt temp_pw_16c_work.txt | wc -l
#0  as expected

# generate changes for AB version
cd lineadj
python ../diff_to_changes_dict.py temp_pw_ab_15e.txt ../temp_pw_ab_15e_work.txt temp_change_ab_1.txt
# 51 changes

cd ../
# initialize change file for AB changes
touch change_pw_ab_16.txt

# manually insert lineadj/temp_change_ab_1.txt into change_pw_ab_16.txt
# generate temp_pw_ab_16.txt
python updateByLine.py lineadj/temp_pw_ab_15e.txt change_pw_ab_16.txt temp_pw_ab_16.txt
# 51 changes

# check
diff temp_pw_ab_16.txt temp_pw_ab_15e_work.txt | wc -l
# 0, as expected

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
At this point, temp_pw_16c.txt and temp_pw_ab_16.txt are the same!
diff temp_pw_16c.txt temp_pw_ab_16.txt | wc -l
# 0
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
-----------------------------------------------

Misc changes from https://github.com/sanskrit-lexicon/PWK/issues/88 comments
 starting at  https://github.com/sanskrit-lexicon/PWK/issues/88#issuecomment-1804408756
 ending at https://github.com/sanskrit-lexicon/PWK/issues/88#issuecomment-1807039552

# changes will be made in temp_pw_17_work.txt
cp temp_pw_ab_16.txt temp_pw_17.txt
cp temp_pw_17.txt temp_pw_17_work.txt  # work starts as same

touch change_pw_17.txt

--------------------------------
Part 1
## ¦  vs <L> in temp_pw_16c.txt
Counts are the same.
grep -E '<L>' temp_pw_16c.txt | wc -l
135771
grep -E '¦' temp_pw_16c.txt | wc -l
135771

# also, check that
 (a) no line has more than 1 ¦
 (b) the first entry line after metaline contains ¦

python broken_bar_check.py ../temp_pw_17.txt

Manually corrected in temp_pw_17_work.txt

# generate change
python diff_to_changes_dict.py temp_pw_17.txt temp_pw_17_work.txt lineadj/temp_change_pw_17_1.txt
# 2 changes
# manual insert lineadj/temp_change_pw_17_1.txt into change_pw_17.txt

# regenerate temp_pw_17.txt
python updateByLine.py temp_pw_ab_16.txt change_pw_17.txt temp_pw_17.txt
2 change transactions from change_pw_17.txt

# check
diff temp_pw_17_work.txt temp_pw_17.txt | wc -l
# 0 as expected

# confirm no broken-bar errors
python broken_bar_check.py ../temp_pw_17.txt
0 error(s) found by broken_bar_check

-----------------------------------------------
Part 2:
First revision of 'das.' abbreviation
Ref: https://github.com/sanskrit-lexicon/PWK/issues/88#issuecomment-1806238062

Manual change in temp_pw_17_work
<ab>das.</ab> -> <ab n="at the same place">das.</ab> in two places.

# Generate change

python diff_to_changes_dict.py temp_pw_17.txt temp_pw_17_work.txt lineadj/temp_change_pw_17_2.txt
2 changes

# insert lineadj/temp_change_pw_17_2.txt into change_pw_17

# regenerate temp_pw_17.txt
python updateByLine.py temp_pw_ab_16.txt change_pw_17.txt temp_pw_17.txt
4 change transactions from change_pw_17.txt

# check
diff temp_pw_17_work.txt temp_pw_17.txt | wc -l
# 0 as expected

-----------------------------------------------
Part 3  Malten's changes re 'das.'
https://github.com/sanskrit-lexicon/PWK/issues/88#issuecomment-1806790910

# manual edit of temp_pw_17_work

# Generate change

python diff_to_changes_dict.py temp_pw_17.txt temp_pw_17_work.txt lineadj/temp_change_pw_17_3.txt
15 changes

# insert lineadj/temp_change_pw_17_3.txt into change_pw_17

# regenerate temp_pw_17.txt
python updateByLine.py temp_pw_ab_16.txt change_pw_17.txt temp_pw_17.txt
19 change transactions from change_pw_17.txt

# check
diff temp_pw_17_work.txt temp_pw_17.txt | wc -l
# 0 as expected

NOTE: Remain uncertain: !?  (slp1 spelling)
<L>68482<pc>4104-1<k1>puz
bisweilen verwechselt mit {#puSpy#}; <ab>s.</ab> <ab>das.</ab>

<L>79617<pc>4262-3<k1>BAvay
<ab>Caus.</ab> von <hom>1.</hom> {#BU#}; <ab>s.</ab> <ab n="at the same place">das.</ab>


-----------------------------------------------
Part 4
<ab n="at the same place">das.</ab> -> <ab>das.</ab>
Refer https://github.com/sanskrit-lexicon/PWK/issues/88#issuecomment-1807039552
 and next comment.
There is no need for 'local abbreviation', since global abbreviation expansion
for 'das.' is 'daselbst - at that same place'

# Manual edit temp_pw_17_work.txt
# Generate change

python diff_to_changes_dict.py temp_pw_17.txt temp_pw_17_work.txt lineadj/temp_change_pw_17_4.txt
2 changes

# insert lineadj/temp_change_pw_17_4.txt into change_pw_17

# regenerate temp_pw_17.txt
python updateByLine.py temp_pw_ab_16.txt change_pw_17.txt temp_pw_17.txt
21 change transactions from change_pw_17.txt

# check
diff temp_pw_17_work.txt temp_pw_17.txt | wc -l
# 0 as expected

-----------------------------------------------
# Note added 'Dass.' (capitalized) to pwab_input.txt in csl_pywork repo.
# Thus, csl_pywork repo needs to be updated at github and cologne.

#*************************************************************************
11-13-2023
install in csl-orig, etc.
*************************************************************************

First, install temp_pw_16c.txt (same as temp_pw_ab_16.txt) in csl-orig

cp temp_pw_16c.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt

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
git commit -m "PWK: CDSL and AB version unified at last!
  Ref: https://github.com/sanskrit-lexicon/PWK/issues/88"
# 1736 insertions(+), 2231 deletions(-)
git push

-----------------------------------------------
Next, Install pw_17.txt (which has a few changes relative to pw_16c.txt

cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue88

-------------------------------------
Install temp_pw_17.txt in csl-orig repository, and update displays
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue88

-----------------------
# do local install
cp temp_pw_17.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt

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
git commit -m "PWK: 'das.' corrections; a few misc. changes
  Ref: https://github.com/sanskrit-lexicon/PWK/issues/88"
# 17 lines changed
#
git push

----- csl-pywork
cd /c/xampp/htdocs/cologne/csl-pywork
git pull # check for other revisions. 
git status  # v02/pw/pw.txt
git add .
git commit -m "Revise pwab_input.txt 'Dass.'
  Ref: https://github.com/sanskrit-lexicon/PWK/issues/88"

#  
git push
commit: d847fe33dd4e2626ebf8869325e0bca452a5f20d

--------------------------------------------
# update cologne displays
# login to cologne
---- csl-orig
git pull

---- csl-pywork
cd v02
git pull
sh generate_dict.sh pw  ../../PWScan/2020/


--------------------------------------------
# sync this repository to Github
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue88

git add .
git commit -m "unified CDSL and AB versions of pwk.  'das.' corrections #88"
git push

-----------------------------------------------
-----------------------------------------------
-----------------------------------------------

-----------------------------------------------

-----------------------------------------------
