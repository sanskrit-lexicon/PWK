hom

10-30-2023 begin.

Version 11. In issue88, start with a copy of version 10
cp temp_pw_10.txt temp_pw_11.txt
cp temp_pw_ab_10.txt temp_pw_ab_11.txt

9055 matches in 8673 lines for "<hom>" in buffer: temp_pw_ab_11.txt
263 matches in 256 lines for "<hom>" in buffer: temp_pw_11.txt

We want to resolve this difference.

--------------------------------------------------------------
Part 1: systematic changes
-----------------------
The first systematic difference is in the first line, such as
old: 1. {#a#}¦
new: <hom>1.</hom> {#a#}¦

python hom_add.py 1 ../temp_pw_10.txt ../temp_pw_11_worka.txt
6894 lines changed

-----------------------
The second systematic difference:
old: ' ^1. '
new: ' <hom>1.</hom> '

python hom_add.py 2 ../temp_pw_11_worka.txt ../temp_pw_11_workb.txt
470 lines changed

temp_pw_11_worka.txt now has most of the hom markup of pw_ab.
Noticed there are almost 1000 of '  +' in temp_pw_11.
Go ahead and change these now

python single_space.py ../temp_pw_11_workb.txt ../temp_pw_11_workc.txt
129 lines changed

-----------------------
A third systematic difference:
old: '3. {#aNga#}'
new: '<hom>3.</hom> {#aNga#}'

python hom_add.py 3 ../temp_pw_11_workc.txt ../temp_pw_11_workd.txt
1321 lines changed


cp temp_pw_11_workd.txt temp_pw_11.txt

# This ends the systematic differences.
# Generate changes
python diff_to_changes_dict.py temp_pw_10.txt temp_pw_11.txt hom/temp_change_pw_11_0.txt
8518  changes written to hom/temp_change_pw_11_0.txt

touch change_pw_11.txt
# manual insert hom/temp_change_pw_11_1.txt into change_pw_11.txt

# regenerate temp_pw_11.txt
python updateByLine.py temp_pw_10.txt change_pw_11.txt temp_pw_11.txt
# 8518 change transactions
# check
diff temp_pw_11.txt temp_pw_11_workd.txt | wc -l
# 0 as expected

--------------------------------------------------------
Part 2: Resolve remaining hom-markup differences
After these systematic changes, we can do a case by case
comparison between pw and pw_ab versions.

cp temp_pw_11.txt temp_pw_11_work.txt
cp temp_pw_ab_11.txt temp_pw_ab_11_work.txt

python ../ablists/regex_compare_texts1.py '<hom>.*?</hom>' ../temp_pw_11_work.txt ../temp_pw_ab_11_work.txt temp1.org ../temp_pw_11_work1.txt ../temp_pw_ab_11_work1.txt

82 cases written to temp1.org

Manual edit the work1 files to resolve differences

#install changes

# remove temp markup (* <L> -> <L>) in  temp_pw_11_work1.txt, and
  save as  temp_pw_11_work.txt
# generate changes
python diff_to_changes_dict.py temp_pw_11.txt temp_pw_11_work.txt hom/temp_change_pw_11_1.txt
83 changes written to hom/temp_change_pw_11_1.txt


# manual insert hom/temp_change_pw_11_1.txt into change_pw_11.txt

# regenerate temp_pw_11.txt
python updateByLine.py temp_pw_10.txt change_pw_11.txt temp_pw_11.txt
# 8601 change transactions
# check
diff temp_pw_11.txt temp_pw_11_work.txt | wc -l
# 0 as expected

There are no changes for pw_ab_11


#*************************************************************************
10-31-2023
install in csl-orig, etc.
*************************************************************************

-------------------------------------
Install temp_pw_11.txt in csl-orig repository, and update displays
cd ../  # issue88

-----------------------
# do local install
cp temp_pw_11.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt

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
git commit -m "PW: Revise pw.txt based on temp_pw_11.txt
  Ref: https://github.com/sanskrit-lexicon/PWK/issues/88"
git push

----- csl-websanlexicon
# Revision to basicadjust.php and basicdisplay.php for display of hom tag
cd /c/xampp/htdocs/cologne/csl-websanlexicon
git status
git add .
git commit -m "hom markup added to pw.
  Ref: https://github.com/sanskrit-lexicon/PWK/issues/88"
git push

----- csl-apidev
cp /c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php /c/xampp/htdocs/cologne/csl-apidev/
cp /c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/webtc/basicdisplay.php /c/xampp/htdocs/cologne/csl-apidev/

cd /c/xampp/htdocs/cologne/csl-apidev
git status
git add .
git commit -m "hom markup added to pw, as per csl-websanlexicon.
  Ref: https://github.com/sanskrit-lexicon/PWK/issues/88"
git push

--------------------------------------------
update cologne displays
login to cologne
---- csl-orig
git pull
# 8553 lines changed

---- csl-websanlexicon
git pull

---- csl-apidev
git pull

---- csl-pywork
cd v02
sh generate_dict.sh pw  ../../PWScan/2020/

--------------------------------------------
sync this repository to Github
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue88
२
git add .
git commit -m "temp_pw_11, temp_pw_ab_11. #88"
git push

TODO: Oddity.
 Should these be considered print errors in PW?
9 matches for "</hom> <is>" in buffer: temp_pw_11_work.txt
e.g.
 <L>33341<pc>2135-2<k1>KaRqakAvya<k2>KaRqakAvya<e>100
{#KaRqakAvya#}¦ <lex>n.</lex> {%ein Stück von einem%} <hom>3.</hom> <is>Kāvya</is> 4〉a〉, {%Quasi%}-<is>Kāvya</is>.

<L>76133<pc>4213-3<k1>balva<k2>balva<e>100
{#balva#}¦
<div n="1">— 1〉 <lex>n.</lex> Name {%des 2ten%} <hom>2.</hom> <is>Karaṇa</is> 4〉n〉.

<L>76140<pc>4213-3<k1>bava<k2>bava<e>100
{#bava#}¦ <lex>n.</lex> Name {%des ersten%} <hom>2.</hom> <is>Karaṇa</is> 4〉n〉.
<L>76191<pc>4214-2<k1>bahirniDana<k2>bahirniDana<e>100
{#bahirniDana#}¦ <lex>n.</lex>, {%ein ausserhalb befindliches%} <hom>1.</hom> <is>Nidhana</is> 5〉


*************************************************************
