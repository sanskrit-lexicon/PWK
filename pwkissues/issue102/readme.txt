pwkissues/issue88102/readme.txt

Begun 11-14-2023

# this directory
cd /c/xampp/htdocs/sanskrit-lexicon/pwk/pwkissues/issue102

# issue 102 link
 https://github.com/sanskrit-lexicon/PWK/issues/102

# cdsl version start with temp_pw_17.txt as copy of
  csl-orig/v02/pw/pw.txt at commit d847fe33dd4e2626ebf8869325e0bca452a5f20d
# AB version start with temp_pw_ab_17.txt ([temp_pw_ab_17.zip](https://github.com/sanskrit-lexicon/PWK/files/13346594/temp_pw_ab_17.zip)).

-----------------------------
Part 1
There are only a few differences between these two versions, cleanup of 'das'.
python diff_to_changes_dict.py temp_pw_17.txt temp_pw_ab_17.txt temp_change_17_1.txt
4 changes written to temp_change_17_1.txt
insert these into change_17a.txt

generate temp_pw_17a.txt

python updateByLine.py temp_pw_17.txt change_17a.txt temp_pw_17a.txt
# 4 change transactions from change_17a.txt

# check same as temp_pw_ab_17.txt
diff temp_pw_ab_17.txt temp_pw_17a.txt | wc -l
# 0, as expected.

Install to csl-orig, and update cologne

# do local install
cp temp_pw_17a.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt

# check local installation
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pw  ../../pw
sh xmlchk_xampp.sh pw
# ok
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue102

# push repositories to GitHub
----- csl-orig
cd /c/xampp/htdocs/cologne/csl-orig
git pull # check for other revisions. 
git status  # v02/pw/pw.txt
git add .
git commit -m "das cleanup. #102 temp_pw_17a"
# 4 lines changed
git push

--------------------------------------------
# update cologne displays
# login to cologne
---- csl-orig
git pull
#1712 ines changed

---- csl-pywork
cd v02
# git pull
sh generate_dict.sh pw  ../../PWScan/2020/

--------------------------------------------
# sync this repository to Github
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue102

git add .
git commit -m "#102 initial commit: temp_pw_17a "
git push
-----------------------------------------------------------

***********************************************************
11-16-2023
AB provides two files:
1. temp_pw_ab_17a.txt [Pagexxx] lines merged
2. 'pw (AB v2).txt', renamed temp_pw_AB_v2.txt

-----------------------------------------------------------
step1
see step1/readme.txt

Reproduce temp_pw_ab_17a.txt from temp_pw_ab_17.txt.
i.e., these two versions are the same.

***********************************************************
11-24-2023
Work on the differences between
temp_pw_ab_17a.txt and temp_pw_AB_v2.txt

The files have the same number of lines:
wc -l temp_pw_AB_v2.txt temp_pw_ab_17a.txt
  674062 temp_pw_AB_v2.txt
  674062 temp_pw_ab_17a.txt

-----
step2 directory
Methodically examine the diffs
Examine crude 'diff' to start with
diff temp_pw_ab_17a.txt temp_pw_AB_v2.txt > tempdiff_v2.txt
# 28426 lines in diff, so about 28426/4 ~= 7000 lines are different.

Refer to step2/readme.txt for further details.
