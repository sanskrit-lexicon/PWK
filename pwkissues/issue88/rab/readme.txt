rab/readme.txt

11-06-2023 begin
Adopt Andhrabharati's invention of using 〉 (Right Angle Bracket) for
section references in PW.

# construct temp_pw_15.txt from temp_pw_14.txt


python rab_div.py ../temp_pw_14.txt ../temp_pw_15a.txt

120287 lines changed for option 1
4152 lines changed for option 2
1285 lines changed for option 3

There will still be some unmatched.
cp temp_pw_15a.txt temp_pw_15a_work.txt

python ../ablists/regex_compare_texts1.py '[^ ]*〉' ../temp_pw_15a_work.txt ../temp_pw_ab_15_work.txt temp1.org  ../temp_pw_15a_work1.txt ../temp_pw_ab_15_work1.txt
# approxmately 300 manual corrections
# iterate until ../temp_pw_15a_work.txt ../temp_pw_ab_15_work.txt are as
# desired.

# no change_pw_15.txt, since there are so many changes.
cp temp_pw_15a_work.txt temp_pw_15b.txt

# Generate changes for temp_pw_ab_15.txt
python diff_to_changes_dict.py temp_pw_ab_14.txt temp_pw_ab_15_work.txt rab/temp_change_pw_ab_15_1.txt
10 changes written to dhatu/temp_change_pw_ab_15_1.txt

touch change_pw_ab_15.txt
# manual insert dhatu/temp_change_pw_ab_15_1.txt into change_pw_ab_15.txt
# manual two corrections from AB at Issue #88
# generate temp_pw_ab_15.txt
python updateByLine.py temp_pw_ab_14.txt change_pw_ab_15.txt temp_pw_ab_15.txt
12 change transactions from change_pw_15.txt
# check
diff temp_pw_ab_15.txt temp_pw_ab_15_work.txt | wc -l
# 0 as expected

---------------------------------------------------------------------
Part 2
Noticed this difference in markup between AB and CDSL.
Change cdsl
* = -> *=   652

cp temp_pw_15a_work.txt temp_pw_15b.txt
------
# manual edit of temp_pw_15b.txt and temp_pw_ab_15.txt
 Two additional changes from AB

-------------------------------------
# final version 15
cp temp_pw_15b.txt temp_pw_15.txt

#*************************************************************************
11-07-2023
install in csl-orig, etc.
*************************************************************************

-------------------------------------
Install temp_pw_15.txt in csl-orig repository, and update displays
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue88

-----------------------
# do local install
cp temp_pw_15.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt

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
git commit -m "PW: Revise pw.txt based on temp_pw_15.txt (right angle bracket)
  Ref: https://github.com/sanskrit-lexicon/PWK/issues/88"
# 122910 lines changed
git push

----- csl-pywork
cd /c/xampp/htdocs/cologne/csl-pywork
git pull # check for other revisions. 
git status  # v02/pw/pw.txt
git add .
git commit -m "pwab_input (abbreviation 'das.', 'Das.')
  Ref: https://github.com/sanskrit-lexicon/PWK/issues/88"
#  1 file changed, 2 insertions(+), 2 deletions(-)
git push

--------------------------------------------
# update cologne displays
# login to cologne
---- csl-orig
git pull
#1712 ines changed

---- csl-pywork
cd v02
git pull
sh generate_dict.sh pw  ../../PWScan/2020/

--------------------------------------------
# sync this repository to Github
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue88

git add .
git commit -m "temp_pw_15, temp_pw_ab_15. (right-angle-bracket, misc.) #88"
git push

Add comment to issue88.

*************************************************************
--------------------------------------------------------------
---
*⁾   A footnote, page 5228-1 (top of page) ली hom 1
