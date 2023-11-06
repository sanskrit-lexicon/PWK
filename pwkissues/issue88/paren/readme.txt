paren/readme.txt

11-02-2023 begin

--------------------------------------------------------------
Part 1: Resolve differences in parenthetical text fragments

cp temp_pw_12.txt temp_pw_13_work.txt
cp temp_pw_ab_12.txt temp_pw_ab_13_work.txt

python ../ablists/regex_compare_texts1.py '\(.*?\)' ../temp_pw_13_work.txt ../temp_pw_ab_13_work.txt temp2.org  
 961 cases
 
python ../ablists/regex_compare_texts1.py '\([^[]*?\)' ../temp_pw_13_work.txt ../temp_pw_ab_13_work.txt temp1.org  ../temp_pw_13_work1.txt ../temp_pw_ab_13_work1.txt
905 cases
We exclude parenthetical groups which include '[' character;  this
  is because AB version has different markup for page breaks
Will revisit
For now, edit ../temp_pw_13_work1.txt ../temp_pw_ab_13_work1.txt and
  resolve differences.

# Generate changes
Remove temp markup ('* <L>' -> '<L>') in temp_pw_13_work1.txt, save as
  temp_pw_13_work.txt

python diff_to_changes_dict.py temp_pw_12.txt temp_pw_13_work.txt paren/temp_change_pw_13_1.txt
1167 changes written to paren/temp_change_pw_13_1.txt

touch change_pw_13.txt
# insert paren/temp_change_pw_13_1.txt into change_pw_13.txt

# generate temp_pw_13.txt
python updateByLine.py temp_pw_12.txt change_pw_13.txt temp_pw_13.txt
1167 change transactions from change_pw_13.txt
# check
diff temp_pw_13.txt temp_pw_13_work.txt | wc -l
# 0 as expected

-----
Remove temp markup ('* <L>' -> '<L>') in temp_pw_ab_13_work1.txt, save as
  temp_pw_ab_13_work.txt

# Generate changes for temp_pw_ab_12.txt
python diff_to_changes_dict.py temp_pw_ab_12.txt temp_pw_ab_13_work.txt paren/temp_change_pw_ab_13_1.txt
108 changes written to paren/temp_change_pw_ab_13_1.txt

touch change_pw_ab_13.txt

# manual insert paren/temp_change_pw_ab_13_1.txt into change_pw_ab_13.txt

# generate temp_pw_ab_13.txt
python updateByLine.py temp_pw_ab_12.txt change_pw_ab_13.txt temp_pw_ab_13.txt
108 change transactions from change_pw_13.txt
# check
diff temp_pw_ab_13.txt temp_pw_ab_13_work.txt | wc -l
python updateByLine.py temp_pw_ab_12.txt change_pw_ab_13.txt temp_pw_ab_13.txt
# 0 as expected

--------------------------------------------------------------
Part 2:  Resolve differences in <lex> tag

python ../ablists/regex_compare_texts1.py '<lex.*?</lex>' ../temp_pw_13_work.txt ../temp_pw_ab_13_work.txt temp1.org  ../temp_pw_13_work1.txt ../temp_pw_ab_13_work1.txt
143 cases

# Manual edit of temp_pw_13_work1.txt, temp_pw_ab_13_work1.txt to
# resolve differences

Remove temp markup ('* <L>' -> '<L>') in temp_pw_13_work1.txt, save as
  temp_pw_13_work.txt

# Generate changes 
python diff_to_changes_dict.py temp_pw_13.txt temp_pw_13_work.txt paren/temp_change_pw_13_2.txt
174 changes written to paren/temp_change_pw_13_2.txt

# insert paren/temp_change_pw_13_2.txt into change_pw_13.txt

# generate temp_pw_13.txt
python updateByLine.py temp_pw_12.txt change_pw_13.txt temp_pw_13.txt
1341 change transactions from change_pw_13.txt
# check
diff temp_pw_13.txt temp_pw_13_work.txt | wc -l
# 0 as expected

-----
Remove temp markup ('* <L>' -> '<L>') in temp_pw_ab_13_work1.txt, save as
  temp_pw_ab_13_work.txt

# Generate changes for temp_pw_ab_12.txt
python diff_to_changes_dict.py temp_pw_ab_13.txt temp_pw_ab_13_work.txt paren/temp_change_pw_ab_13_2.txt
3 changes written to paren/temp_change_pw_ab_13_2.txt

# manual insert paren/temp_change_pw_ab_13_2.txt into change_pw_ab_13.txt

# generate temp_pw_ab_13.txt
python updateByLine.py temp_pw_ab_12.txt change_pw_ab_13.txt temp_pw_ab_13.txt
111 change transactions from change_pw_13.txt
# check
diff temp_pw_ab_13.txt temp_pw_ab_13_work.txt | wc -l
# 0 as expected


--------------------------------------------------------------

Part 3
43 matches in 36 lines for "[.]</[^>]*>\." in buffer: temp_pw_13_work1.txt
 none for pw_ab_13.

python ../ablists/regex_compare_texts1.py '[.]</[^>]*>\.' ../temp_pw_13_work.txt ../temp_pw_ab_13_work.txt temp1.org  ../temp_pw_13_work1.txt ../temp_pw_ab_13_work1.txt
35 cases

# Manual edit of temp_pw_13_work1.txt, temp_pw_ab_13_work1.txt to
# resolve differences

Remove temp markup ('* <L>' -> '<L>') in temp_pw_13_work1.txt, save as
  temp_pw_13_work.txt

# Generate changes 
python diff_to_changes_dict.py temp_pw_13.txt temp_pw_13_work.txt paren/temp_change_pw_13_3.txt
36 changes written to paren/temp_change_pw_13_3.txt

# insert paren/temp_change_pw_13_3.txt into change_pw_13.txt

# generate temp_pw_13.txt
python updateByLine.py temp_pw_12.txt change_pw_13.txt temp_pw_13.txt
1377 change transactions from change_pw_13.txt
# check
diff temp_pw_13.txt temp_pw_13_work.txt | wc -l
# 0 as expected

-----
Remove temp markup ('* <L>' -> '<L>') in temp_pw_ab_13_work1.txt, save as
  temp_pw_ab_13_work.txt

# Generate changes for temp_pw_ab_12.txt
python diff_to_changes_dict.py temp_pw_ab_13.txt temp_pw_ab_13_work.txt paren/temp_change_pw_ab_13_3.txt
0 changes written to paren/temp_change_pw_ab_13_3.txt

# manual insert paren/temp_change_pw_ab_13_3.txt into change_pw_ab_13.txt

# generate temp_pw_ab_13.txt
python updateByLine.py temp_pw_ab_12.txt change_pw_ab_13.txt temp_pw_ab_13.txt
111 change transactions from change_pw_13.txt
# check
diff temp_pw_ab_13.txt temp_pw_ab_13_work.txt | wc -l
# 0 as expected


--------------------------------------------------------------
Part 4a
9 matches for "([^)]*?$" in buffer: temp_pw_13_work.txt

python ../ablists/regex_compare_texts1.py '\([^)]*?$' ../temp_pw_13_work.txt ../temp_pw_ab_13_work.txt temp1.org  ../temp_pw_13_work1.txt ../temp_pw_ab_13_work1.txt
8 cases written to temp1.org
# resolve these by edit of temp_pw_13_work.txt
#  Note: <L>114807<pc>6267-3<k1>SraTAy
    (nur <ab>Imper.</ab> {#Sr...    There is no matching ) in print.
    Changed to  nur <ab>Imper.</ab> {#Sr   is a print change.

Part 4b
26 matches for "[.])[.]" in buffer: temp_pw_13_work.txt
25 matches for "[.])[.]" in buffer: temp_pw_ab_13_work.txt

# resolve these by edits of the two work files, refer print
One remains Unchanged:
L>72667<pc>4162-3<k1>praBfti
 Lobliedes.).

Part 4c
19 matches in 18 lines for "[.])," in buffer: temp_pw_13_work.txt
Same for pw_ab_13.

These 5 remain Unchanged acc. to print:
<L>59297<pc>3215-1<k1>nirRayabindu
(<ls>OPP. CAT. 1</ls>.), {#nirRayaratnAkara#} 

<L>79344<pc>4258-3<k1>BAwwakOstuBa
(<ls>OPP. CAT. 1</ls>.), {#BAwwacintAmaRi#}

<L>95287<pc>5209-2<k1>lakzaRaratna
(<ls>OPP. CAT. 1</ls>.), {#°mAlikA#}

<L>101437<pc>6074-1<k1>vAsudevavijaya
(<ls>OPP. CAT. 1</ls>.), {#vAsudevatotra#}


<L>130874<pc>7207-1<k1>sTA
(page 7211-2)
{#prati#} <ls n="Chr.">39,15</ls>.), {%um zu%}
-------------------
# Generate changes 
python diff_to_changes_dict.py temp_pw_13.txt temp_pw_13_work.txt paren/temp_change_pw_13_4.txt
46 changes written to paren/temp_change_pw_13_4.txt

# insert paren/temp_change_pw_13_4.txt into change_pw_13.txt

# generate temp_pw_13.txt
python updateByLine.py temp_pw_12.txt change_pw_13.txt temp_pw_13.txt
1423 change transactions from change_pw_13.txt
# check
diff temp_pw_13.txt temp_pw_13_work.txt | wc -l
# 0 as expected

-----
# Generate changes for temp_pw_ab_12.txt
python diff_to_changes_dict.py temp_pw_ab_13.txt temp_pw_ab_13_work.txt paren/temp_change_pw_ab_13_4.txt
37 changes written to paren/temp_change_pw_ab_13_4.txt

# manual insert paren/temp_change_pw_ab_13_4.txt into change_pw_ab_13.txt

# generate temp_pw_ab_13.txt
python updateByLine.py temp_pw_ab_12.txt change_pw_ab_13.txt temp_pw_ab_13.txt
148 change transactions from change_pw_13.txt
# check
diff temp_pw_ab_13.txt temp_pw_ab_13_work.txt | wc -l
# 0 as expected

--------------------------------------------------------------
 div tag <div n="X"/>

python ../ablists/regex_compare_texts1.py '<div.*?>' ../temp_pw_13_work.txt ../temp_pw_ab_13_work.txt temp1.org  ../temp_pw_13_work1.txt ../temp_pw_ab_13_work1.txt
112 cases written to temp1.org

After manual adjustment, slightly different comparison.
python ../ablists/regex_compare_texts1.py '<div[^>]*>— Mit {#[^#]*#}' ../temp_pw_13_work.txt ../temp_pw_ab_13_work.txt temp1.org  ../temp_pw_13_work1.txt ../temp_pw_ab_13_work1.txt
14 cases
DONE

python ../ablists/regex_compare_texts1.py '<div[^>]*>— [^)〉}]+' ../temp_pw_13_work.txt ../temp_pw_ab_13_work.txt temp1.org  ../temp_pw_13_work1.txt ../temp_pw_ab_13_work1.txt
7 cases

All resolved

------
Mit/mit
python ../ablists/regex_compare_texts1.py '[mM]it ' ../temp_pw_13_work.txt ../temp_pw_ab_13_work.txt temp1.org  ../temp_pw_13_work1.txt ../temp_pw_ab_13_work1.txt
9 cases

-------------------
# Generate changes 
python diff_to_changes_dict.py temp_pw_13.txt temp_pw_13_work.txt paren/temp_change_pw_13_5.txt
303 changes written to paren/temp_change_pw_13_5.txt

# insert paren/temp_change_pw_13_5.txt into change_pw_13.txt

# generate temp_pw_13.txt
python updateByLine.py temp_pw_12.txt change_pw_13.txt temp_pw_13.txt
1726 change transactions from change_pw_13.txt
# check
diff temp_pw_13.txt temp_pw_13_work.txt | wc -l
# 0 as expected

-----
# Generate changes for temp_pw_ab_12.txt
python diff_to_changes_dict.py temp_pw_ab_13.txt temp_pw_ab_13_work.txt paren/temp_change_pw_ab_13_5.txt
19 changes written to paren/temp_change_pw_ab_13_5.txt

# manual insert paren/temp_change_pw_ab_13_5.txt into change_pw_ab_13.txt

# generate temp_pw_ab_13.txt
python updateByLine.py temp_pw_ab_12.txt change_pw_ab_13.txt temp_pw_ab_13.txt
167 change transactions from change_pw_ab_13.txt
# check
diff temp_pw_ab_13.txt temp_pw_ab_13_work.txt | wc -l
# 0 as expected


#*************************************************************************
11-06-2023
install in csl-orig, etc.
*************************************************************************

-------------------------------------
Install temp_pw_13.txt in csl-orig repository, and update displays
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue88

-----------------------
# do local install
cp temp_pw_13.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt

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
git commit -m "PW: Revise pw.txt based on temp_pw_13.txt (paren text, lex, div)
  Ref: https://github.com/sanskrit-lexicon/PWK/issues/88"
# 1712 lines changed
git push

--------------------------------------------
# update cologne displays
# login to cologne
---- csl-orig
git pull
#1712 ines changed

---- csl-pywork
cd v02
sh generate_dict.sh pw  ../../PWScan/2020/

--------------------------------------------
# sync this repository to Github
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue88

git add .
git commit -m "temp_pw_13, temp_pw_ab_13. (paren, lex, div) #88"
git push



*************************************************************
--------------------------------------------------------------
TODO: √ ??
---
*⁾   A footnote, page 5228-1 (top of page) ली hom 1
