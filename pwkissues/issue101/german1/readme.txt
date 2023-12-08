pwkissues/issue101/german1/readme.txt

Begun 11-29-2023
Purpose: German words in NON-ITALICS

# directory
cd /c/xampp/htdocs/sanskrit-lexicon/pwk/pwkissues/issue101/german1

# issue 101 link
 https://github.com/sanskrit-lexicon/PWK/issues/101

# start with temp_pw_3.txt version
  
cp cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw_1.txt


init_correction_input: 163 read from corrections_normal.txt
34 duplicates found

python words.py ../german/temp_pw_3.txt words.txt words_freq.txt


python word_freq_de.py words_freq.txt tempsave_german.txt words_freq_de.txt
8053 cases written to words_freq_de.txt
----

# similar analysis for words marked as italics
python itwords.py ../german/temp_pw_3.txt itwords.txt itwords_freq.txt
48723 cases written to itwords_freq.txt

python word_freq_de_it.py words_freq_de.txt itwords_freq.txt  words_freq_de_it.txt
8053 cases written to words_freq_de_it.txt

# word_change.txt adapted manually from words_freq_de_it.txt
python word_change_page.py word_change.txt words.txt word_change_page.org
TODO:
-> niwfla
<L>58427<pc>3-202-c<k1>niwwala<k2>niwwala<e>100
{#niwwala#}¦ <lex>m.</lex> <ab>N. pr.</ab> einer Brahmanenfamilie.

12-06-2023
388 matches for ": CHG :" in buffer: word_change_page.org
 pre_change1.txt  has these 388 lines
   Note the '* ' markup is removed.

 Split into
 354 pre_change1_regular.txt
     Also removed ';;' comments
     These are inputs for make_change1 program below
 28 pre_change1_irregular.txt - change generation manual.

python make_change_regular.py  pre_change1_regular.txt ../german/temp_pw_3.txt change_word_regular.txt

360 records read from pre_change1_regular.txt
674019 lines read from ../german/temp_pw_3.txt
135764 entries found
360 cases written to change_word_regular.txt

## apply the changes: temp_pw_3a.txt
python ../german/updateByLine.py ../german/temp_pw_3.txt change_word_regular.txt temp_pw_3a.txt
# 674019 lines read from ../german/temp_pw_3.txt
674019 records written to temp_pw_3a.txt
360 change transactions from change_word_regular.txt

----------------------
## manually apply pre_change1_irregular.txt
cp temp_pw_3a.txt temp_pw_3b.txt
# manual change to temp_pw_3b.txt based on pre_change1_irregular.txt

# generate change file
 python ../german/diff_to_changes_dict.py temp_pw_3a.txt temp_pw_3b.txt change_word_irregular.txt
# 24 changes written to change_word_irregular.txt

-----------------------------
# pre_change1_thomas.txt
# Items marked for change by Thomas.
cp temp_pw_3b.txt temp_pw_3c.txt
#manually change temp_pw_3c.txt

# generate change file
 python ../german/diff_to_changes_dict.py temp_pw_3b.txt temp_pw_3c.txt change_word_thomas.txt
# 45 changes written to change_word_thomas.txt
-----------------------------


-----------------------------
308 matches for ": CHG :[^;]*$" in buffer: word_change_page.org

40 matches for "italic" in buffer: word_change_page.org




------------------------------------------
moded change_word_regular.txt for italic
python ../german/updateByLine.py ../german/temp_pw_3.txt change_word_regular.txt temp_pw_3a.txt

python ../german/updateByLine.py temp_pw_3a.txt change_word_irregular.txt temp_pw_3b.txt

python ../german/updateByLine.py temp_pw_3b.txt change_word_thomas.txt temp_pw_3c.txt

=====================================================================
-----------------------
# do local install
cp temp_pw_3c.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt

# check local installation
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pw  ../../pw
sh xmlchk_xampp.sh pw
# ok
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue101/german1

# push repositories to GitHub
----- csl-orig
cd /c/xampp/htdocs/cologne/csl-orig
git pull # check for other revisions. 
git status  # v02/pw/pw.txt
git add .
git commit -m "PW: German word corrections
  Ref: https://github.com/sanskrit-lexicon/PWK/issues/101  (german1)"
# 429 lines changed
git push

--------------------------------------------
# update cologne displays
# login to cologne
---- csl-orig
git pull
#161 lines changed

---- csl-pywork
cd v02
git pull # no change
sh generate_dict.sh pw  ../../PWScan/2020/


******************************************************
prepare temp_pw_3c_hk.txt for Thomas
-------------------------------------------
11-28-2023
Regenerate temp_pw_3c_hk.txt from temp_pw_3c.txt
(refer c:/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue95/pwtranscode/)

cp temp_pw_3c.txt /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue95/pwtranscode/temphk/temp_pw_3c.txt
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue95/pwtranscode/

python pw_transcode.py slp1 hk temphk/temp_pw_3c.txt temphk/temp_pw_3c_hk.txt
# check invertibility
python pw_transcode.py hk slp1 temphk/temp_pw_3c_hk.txt temphk/temp_pw_3c_hk_slp1.txt
diff temphk/temp_pw_3c.txt temphk/temp_pw_3c_hk_slp1.txt | wc -l
# 148  - known differences
# mv temp_pw_3c_hk.txt back to german1 directory
mv temphk/temp_pw_3c_hk.txt /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue101/german1/
# remove unneeded
rm temphk/temp_pw_3c.txt
rm temphk/temp_pw_3c_hk_slp1.txt

# return to this german1 directory
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue101/german1

zip temp_pw_3c_hk.zip temp_pw_3c_hk.txt change_word_regular.txt change_word_irregular.txt change_word_thomas.txt
Send temp_pw_3_hk.zip to thomas

-----------------------------------------------------
--------------------------------------------
# sync this repository to Github
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue101

git add .
git commit -m "#101"
git push

make comment in https://github.com/sanskrit-lexicon/PWK/issues/101
