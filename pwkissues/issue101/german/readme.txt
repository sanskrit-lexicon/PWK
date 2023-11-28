pwkissues/issue101/german/readme.txt

Begun 11-27-2023

# directory
cd /c/xampp/htdocs/sanskrit-lexicon/pwk/pwkissues/issue101/german

# issue 101 link
 https://github.com/sanskrit-lexicon/PWK/issues/101

# start with temp_pw_1.txt as copy of
  csl-orig/v02/pw/pw.txt at commit 67c4915f73170f51e887a44bc1bc7faa502b5b8a
cp cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw_1.txt

# malten's file:
corrections_from_thomas_skype.txt  (192 lines)
Separated into
  corrections_normal.txt (163)
    Note: manually changed to utf-8 format for umlauts
  corrections_special.txt (29)
 check: 163 + 29 = 192 (as expected)
 
'normal corrections' of form OLD -> NEW

# Some corrections are almost normal, and included in corrections_normal.txt
#  after removal of the [X]
Title  -> Titel [5x]
freudlich  ->  freundlich [5x]
freudliche  -> freundliche [3x]
nacht  -> Nacht [2x]
paederia  -> Paederia [2x; <bot>]
premna  -> Premna [<bot>]
ven  -> von [2x]

# The 'normal' corrections to generate corrections to pw.txt by a program

corrections_normal_count.txt
 Format: N old -> new
 Takes into account:
  (a) the 7 nx items
  (b) 34 other non-reported dups
python corrections_count.py corrections_normal.txt corrections_normal_count.txt
txt
40 duplicate inputs found
129 records written to corrections_normal_count.txt

-------------------

There are numerous old -> new instances where
a) the count (including duplicates) is wrong.
   Example: Arl has count of 2 in Thomas's list (a duplicate),
     but the string 'Arl' occurs only once in ANY text (global find)
     
python find_counts.py temp_pw_1.txt corrections_normal_count.txt corrections_normal_count_any.txt

python italic_word_change.py temp_pw_1.txt corrections_normal_count.txt change_pw_2.txt correctsions_normal_observed.txt

cp corrections_normal_count.txt  corrections_normal_count_revised.txt

# manually edit corrections_normal_count_revised.txt changing the first number
  based on corrections_normal_count_any.txt.
  
init_correction_input: 163 read from corrections_normal.txt
34 duplicates found

python italic_word_change.py temp_pw_1.txt corrections_normal_count_revised.txt change_pw_2.txt correctsions_normal_revised_observed.txt

# Apply change_pw_2.txt to get temp_pw_2.txt
python updateByLine.py temp_pw_1.txt change_pw_2.txt temp_pw_2.txt
128 change transactions from change_pw_2.txt

--------------------------------------------
cp temp_pw_2.txt temp_pw_3.txt
Manual changes to temp_pw_3.txt

python diff_to_changes_dict.py temp_pw_2.txt temp_pw_3.txt change_pw_3.txt
33 changes written to change_pw_3.txt

python updateByLine.py temp_pw_2.txt change_pw_3.txt temp3.txt
--------------------------------------------

See unchanged.txt for items mentioned in corrections_from_thomas_skype.txt
but either not found or not changed. 15 such items.
-------------------------------------------
11-28-2023
Regenerate temp_pw_3_hk.txt from temp_pw_3.txt
(refer c:/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue95/pwtranscode/)

cp temp_pw_3.txt /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue95/pwtranscode/temphk/temp_pw_3.txt
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue95/pwtranscode/

python pw_transcode.py slp1 hk temphk/temp_pw_3.txt temphk/temp_pw_3_hk.txt
# check invertibility
python pw_transcode.py hk slp1 temphk/temp_pw_3_hk.txt temphk/temp_pw_3_hk_slp1.txt
diff temphk/temp_pw_3.txt temphk/temp_pw_3_hk_slp1.txt | wc -l
# 148  - known differences
# mv temp_pw_3_hk.txt back to german directory
mv temphk/temp_pw_3_hk.txt /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue101/german/
# remove unneeded
rm temphk/temp_pw_3.txt
rm temphk/temp_pw_3_hk_slp1.txt

# return to this german directory
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue101/german

******************************************************
push to github and update local/cologne
******************************************************
-----------------------
# do local install
cp temp_pw_3.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt

# check local installation
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pw  ../../pw
sh xmlchk_xampp.sh pw
# ok
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue101/german

# push repositories to GitHub
----- csl-orig
cd /c/xampp/htdocs/cologne/csl-orig
git pull # check for other revisions. 
git status  # v02/pw/pw.txt
git add .
git commit -m "PW: German word corrections
  Ref: https://github.com/sanskrit-lexicon/PWK/issues/101"
# 161 lines changed
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

--------------------------------------------
# sync this repository to Github
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue101

git add .
git commit -m "#101"
git push

******************************************************
zip temp_pw_3_hk.zip temp_pw_3_hk.txt change_pw_2.txt change_pw_3.txt unchanged.txt
Send temp_pw_3_hk.zip to thomas

make comment in https://github.com/sanskrit-lexicon/PWK/issues/101
