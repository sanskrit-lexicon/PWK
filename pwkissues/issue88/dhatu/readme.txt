dhatu/readme.txt

11-06-2023 begin
Add root markup to cdsl based on AB version.

cp temp_pw_ab_13.txt temp_pw_ab_14.txt

--------------------------------------------------------------
Part 1: '!√' markup changes 
python root_add.py 1 ../temp_pw_13.txt ../temp_pw_ab_13.txt temp_change_pw_14_1.txt
3093 changes written to temp_change_pw_14_1.txt

touch change_pw_14.txt  # in issue88

# insert dhatu/temp_change_pw_14_1.txt into change_pw_14.txt

# generate temp_pw_14.txt
python updateByLine.py temp_pw_13.txt change_pw_14.txt temp_pw_14.txt
3093 change transactions from change_pw_14.txt
# check -- not relevant
# diff temp_pw_14.txt temp_pw_14_work.txt | wc -l
# 0 as expected

touch change_pw_ab_14.txt
 # no changes required.

--------------------------------------------------
Part 2:  Additional root markup identify and change

cp temp_pw_14.txt temp_pw_14_work.txt
cp temp_pw_ab_14.txt temp_pw_ab_14_work.txt

python ../ablists/regex_compare_texts1.py '!?√{#[^#]*#}' ../temp_pw_14_work.txt ../temp_pw_ab_14_work.txt temp1.org  ../temp_pw_14_work1.txt ../temp_pw_ab_14_work1.txt
46 cases written to temp1.org

# Generate changes
Remove temp markup ('* <L>' -> '<L>') in temp_pw_14_work1.txt, save as
  temp_pw_14_work.txt

python diff_to_changes_dict.py temp_pw_14.txt temp_pw_14_work.txt dhatu/temp_change_pw_14_2.txt
46 changes written to dhatu/temp_change_pw_14_2.txt

# insert dhatu/temp_change_pw_14_2.txt into change_pw_14.txt

# generate temp_pw_14.txt
python updateByLine.py temp_pw_13.txt change_pw_14.txt temp_pw_14.txt
3139 change transactions from change_pw_14.txt
# check
diff temp_pw_14.txt temp_pw_14_work.txt | wc -l
# 0 as expected

-----
Remove temp markup ('* <L>' -> '<L>') in temp_pw_ab_14_work1.txt, save as
  temp_pw_ab_14_work.txt

# Generate changes for temp_pw_ab_14.txt
python diff_to_changes_dict.py temp_pw_ab_14.txt temp_pw_ab_14_work.txt dhatu/temp_change_pw_ab_14_2.txt
3 changes written to dhatu/temp_change_pw_ab_14_2.txt

# manual insert dhatu/temp_change_pw_ab_14_2.txt into change_pw_ab_14.txt

# generate temp_pw_ab_14.txt
python updateByLine.py temp_pw_ab_13.txt change_pw_ab_14.txt temp_pw_ab_14.txt
3 change transactions from change_pw_14.txt
# check
diff temp_pw_ab_14.txt temp_pw_ab_14_work.txt | wc -l
# 0 as expected
@
--------------------------------------------------
Part 3: [.])[.,]  6 cases.
Ref: https://github.com/sanskrit-lexicon/PWK/issues/88#issuecomment-1799374467

# manual changes to temp_pw_14_work.txt, temp_pw_ab_14_work.txt

@# generate changes
python diff_to_changes_dict.py temp_pw_14.txt temp_pw_14_work.txt dhatu/temp_change_pw_14_3.txt
6 changes written to dhatu/temp_change_pw_14_3.txt

# insert dhatu/temp_change_pw_14_3.txt into change_pw_14.txt

# generate temp_pw_14.txt
python updateByLine.py temp_pw_13.txt change_pw_14.txt temp_pw_14.txt
3145 change transactions from change_pw_14.txt
# check
diff temp_pw_14.txt temp_pw_14_work.txt | wc -l
# 0 as expected

-----

# Generate changes for temp_pw_ab_14.txt
python diff_to_changes_dict.py temp_pw_ab_14.txt temp_pw_ab_14_work.txt dhatu/temp_change_pw_ab_14_3.txt
6 changes written to dhatu/temp_change_pw_ab_14_3.txt

# manual insert dhatu/temp_change_pw_ab_14_3.txt into change_pw_ab_14.txt

# generate temp_pw_ab_14.txt
python updateByLine.py temp_pw_ab_13.txt change_pw_ab_14.txt temp_pw_ab_14.txt
9 change transactions from change_pw_14.txt
# check
diff temp_pw_ab_14.txt temp_pw_ab_14_work.txt | wc -l
# 0 as expected

--------------------------------------------------
Part 4:  Misc. from AB response to version 13

# manual changes to temp_pw_14_work.txt, temp_pw_ab_14_work.txt

Part 4a:  4 cases
Space after broken bar
Ref: https://github.com/sanskrit-lexicon/PWK/issues/88#issuecomment-1797691320

Part 4b: mongolian  1 case
Ref: https://github.com/sanskrit-lexicon/PWK/issues/88#issuecomment-1797814926

<lang n="mongolian">ᠪᠠᠭᠠᠲᠦᠷ???</lang>
NOTE: modify dtd

Part 4c:  19
  mark 'das.' as abbreviation <ab>das.</ab> 15 
  mark 'Das.' as abbreviation <ab>Das.</ab>  4 


Modify csl-pywork abbreviations for 'das.' Same as 'dass.'

# generate changes
python diff_to_changes_dict.py temp_pw_14.txt temp_pw_14_work.txt dhatu/temp_change_pw_14_4.txt
24 changes written to dhatu/temp_change_pw_14_4.txt

# insert dhatu/temp_change_pw_14_4.txt into change_pw_14.txt

# generate temp_pw_14.txt
python updateByLine.py temp_pw_13.txt change_pw_14.txt temp_pw_14.txt
3169 change transactions from change_pw_14.txt
# check
diff temp_pw_14.txt temp_pw_14_work.txt | wc -l
# 0 as expected

-----

# Generate changes for temp_pw_ab_14.txt
python diff_to_changes_dict.py temp_pw_ab_14.txt temp_pw_ab_14_work.txt dhatu/temp_change_pw_ab_14_4.txt
23 changes written to dhatu/temp_change_pw_ab_14_4.txt

# manual insert dhatu/temp_change_pw_ab_14_4.txt into change_pw_ab_14.txt

# generate temp_pw_ab_14.txt
python updateByLine.py temp_pw_ab_13.txt change_pw_ab_14.txt temp_pw_ab_14.txt
32 change transactions from change_pw_14.txt
# check
diff temp_pw_ab_14.txt temp_pw_ab_14_work.txt | wc -l
# 0 as expected

--------------------------------------------------
MODIFY one.dtd 'n="mongolian"' in csl-pywork
#*************************************************************************
11-07-2023
install in csl-orig, etc.
*************************************************************************

-------------------------------------
Install temp_pw_14.txt in csl-orig repository, and update displays
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue88

-----------------------
# do local install
cp temp_pw_14.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt

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
git commit -m "PW: Revise pw.txt based on temp_pw_14.txt (dhatu)
  Ref: https://github.com/sanskrit-lexicon/PWK/issues/88"
# 3055 lines changed
git push

----- csl-pywork
cd /c/xampp/htdocs/cologne/csl-pywork
git pull # check for other revisions. 
git status  # v02/pw/pw.txt
git add .
git commit -m "PW: one.dtd, pwab_input modified
  Ref: https://github.com/sanskrit-lexicon/PWK/issues/88"
#  2 files changed, 3 insertions(+), 1 deletion(-)
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
git commit -m "temp_pw_14, temp_pw_ab_14. (dhatu mark, misc.) #88"
git push



*************************************************************
--------------------------------------------------------------
TODO: √ ??
---
*⁾   A footnote, page 5228-1 (top of page) ली hom 1
