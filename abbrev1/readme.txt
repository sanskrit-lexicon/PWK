abbrev1/readme.txt
NOTE:  08-15-2023  THIS DIRECTORY ORPHANED.
  Work moved to pwkissues/issue88
  
Improve abbreviation markup in PWK.
August 2023
This continues the work of 'abbrev' directory.

# this directory
cd /c/xampp/htdocs/sanskrit-lexicon/pwk/abbrev1

Ref: https://github.com/sanskrit-lexicon/PWK/issues/88

temp_pw_0.txt  take from csl-orig

cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw_0.txt
(commit 7c848d6546389c6c8d7612819dde0cce89601a6d)

cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pw/pywork/pwab/pwab_input.txt pwab_input_0.txt
  (commit 2bbf9918b768b9fdb934bf63b53999773b488f27)

Andhrabharati lists of abbreviations
ablists/

---------------------------------------------------------------------
temp_pw_ab_0.txt
  from https://github.com/sanskrit-lexicon/PWK/files/12148898/pw.AB.v1.zip
  Andhrabharati version.

wc -l temp_pw*
  682608 temp_pw_0.txt
  674189 temp_pw_ab_0.txt
 so the ab version has about 8000+ fewer lines.

cp temp_pw_ab_0.txt temp_pw_ab_0_orig.txt
Make a few changes in temp_pw_ab_0.txt for xml validity (see dev0_ab below)
See file corrections_ab_0.txt

change one.dtd to 
====================================================================
construct dev versions
--- dev0  based on temp_pw_0.txt
sh redo_dev.sh 0

--- devab_0
sh redo_dev.sh ab_0
9 records not valid xml
====================================================================
====================================================================
====================================================================
====================================================================

********************************************************************
OLD NOTES FROM ABBREV directory
********************************************************************
freq_ab.txt   Frequency of <ab>X</ab> OR <lex>X</lex>
# cp /c/xampp/htdocs/sanskrit-lexicon/INM/greek/issue9/freq_greek.py freq_ab.py
python freq_ab.py temp_pw_0.txt temp_pwab_input.txt freq_ab.txt

682616 lines read from temp_pw_0.txt
135787 entries found
64 abbreviations read from temp_pwab_input.txt
62 different greek strings
62 records written to freq_ab.txt
1 abbreviations without tooltip
   Prol. 1 unknown
3 abbreviation tips unused:
   best. bestimmte - a certain (kind of)
   v.a. vor allem - above all, especially
   gedr. gedruckt - printed

====================================================================
abbreviations in italics.  A potential problem for english translation
773 matches in 757 lines for "{%[^%]*<ab" in buffer: temp_pw_0.txt
====================================================================
Find unmarked abbreviations.
Generate changes for markup of abbreviations not yet marked.
python unmarked_ab.py temp_pw_0.txt temp_pwab_input.txt change_1.txt

date;python unmarked_ab.py temp_pw_0.txt temp_pwab_input.txt change_1.txt;date
Tue Jun  7 17:08:13 EDT 2022
682616 lines read from temp_pw_0.txt
135787 entries found
64 abbreviations read from temp_pwab_input.txt
6496 lines changed
change records written to change_1.txt
Abl. 1
Adv. 1
best. 224
ebend. 6
gedr. 234
Hdschr. 26
Med. 1
s. 547
Sch. 8
Schol. 33
u.s.w. 1790
v.a. 4025
v.u. 92
vgl. 8
6996 abbreviations marked
Tue Jun  7 17:10:24 EDT 2022

# implement changes in temp_pw_1.txt
python updateByLine.py temp_pw_0.txt change_1.txt temp_pw_1.txt
6496 change transactions from change_1.txt

====================================================================
installation of temp_pw_1.txt

install: csl-orig/v02/pw/pw.txt
cp temp_pw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt

# check xml validity
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pw  ../../pw
sh xmlchk_xampp.sh pw
 # ok 
# commit/push to csl-orig
cd /c/xampp/htdocs/cologne/csl-orig/v02/pw
# return home
cd /c/xampp/htdocs/sanskrit-lexicon/pwk/abbrev
========================================================
# generate new frequency count with revised pw:
python freq_ab.py temp_pw_1.txt temp_pwab_input.txt freq_ab_1.txt

====================================================================
# ab markup within italic texts
====================================================================
python unmarked_ab_italic.py temp_pw_1.txt temp_pwab_input.txt change_2.txt

682616 lines read from temp_pw_1.txt
135787 entries found
64 abbreviations read from temp_pwab_input.txt
10450 lines changed
change records written to change_2.txt
best. 9792
f. 2
m. 2
s. 13
Sch. 11
Schol. 1
u.s.w. 125
v.a. 542
10488 abbreviations marked

# implement changes in temp_pw_2.txt
python updateByLine.py temp_pw_1.txt change_2.txt temp_pw_2.txt
10450 change transactions from change_2.txt
====================================================================
installation of temp_pw_2.txt

install: csl-orig/v02/pw/pw.txt
cp temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt

# check xml validity
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pw  ../../pw
sh xmlchk_xampp.sh pw
 # ok 
# commit/push to csl-orig
cd /c/xampp/htdocs/cologne/csl-orig/v02/pw
# return home
cd /c/xampp/htdocs/sanskrit-lexicon/pwk/abbrev
====================================================================
# generate new frequency count with revised pw:
python freq_ab.py temp_pw_2.txt temp_pwab_input.txt freq_ab_2.txt
====================================================================
