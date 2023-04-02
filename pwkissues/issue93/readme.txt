Refer https://github.com/sanskrit-lexicon/PWK/issues/93

Implementation steps
Markup of 'Chr.' elements.
<ls>123,4> -> <ls n="Chr.</ls>123,4</ls>
---------------------------------------------------------
temp_pw_0.txt
This will be the latest version of csl-orig/v02/pw/pwtxt.
It's name starts with 'temp';
  By ./gitignore of this repository, files whose names start with 'temp'
  are not tracked by git.
Make 'pwk/pwissues/issue93/temp_pw_0.txt' to be a copy of
 'csl-orig/v02/pw/pw.txt'.  Do this however convenient.
Jim's method
cd /c/xampp/htdocs/sanskrit-lexicon/pwk/pwkissues/issue93
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw_0.txt
---------------------------------------------------------
temp_pw_tooltip.txt
start with a copy of latest pwbib_input.txt
cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pw/pywork/pwauth/pwbib_input.txt temp_pw_tooltip.txt
---------------------------------------------------------
lsextract_all.txt
cp /c/xampp/htdocs/sanskrit-lexicon/pwk/pw_ls/summary/lsextract_all.py .

python lsextract_all.py temp_pw_0.txt temp_pw_tooltip.txt lsextract_pw_0.txt

WARNING at line 92421 <L>19525<pc>1239-1<k1>upacitra<k2>upacitra<e>100
ls =  <ls></ls>

---------------------------------------------------------
At least two cases:
 <ls>p,l</ls> => <ls n="Chr.">p,l</ls>
 
---------------------------------------------------------
cp temp_pw_0.txt temp_pw_1.txt
touch change_1.txt

add change to change_1.txt
92421 old <div n="2">— b) {%<bot>Croton polyandrum Spr.</bot>%} <ls></ls>
92421 new <div n="2">— b) {%<bot>Croton polyandrum Spr.</bot>%}
# cp /c/xampp/htdocs/sanskrit-lexicon/pwk/pwkissues/issue91/updateByLine.py .
python updateByLine.py temp_pw_0.txt change_1.txt temp_pw_1.txt

---------------------------------------------------------
change_1.py 
---------------------------------------------------------
# option 1: <ls>p,l</ls> => <ls n="Chr.">p,l</ls>
python change_1.py 1 temp_pw_1.txt temp_change_1.txt
# temp_change_1.txt  (616 changes in 544 entries)

# edit temp_change_1.txt
# insert temp_change_1.txt into change_1.txt
# apply change_1
python updateByLine.py temp_pw_0.txt change_1.txt temp_pw_1.txt

617 change transactions from change_1.txt

---------------------------------------------------------
# option 2: <ls>p,l.</ls> => <ls n="Chr.">p,l.</ls>
  Period after line-number l
python change_1.py 2 temp_pw_1.txt temp_change_2.txt
temp_change_2.txt  (3695 changes in 3155 entries)

# edit temp_change_2.txt
# insert temp_change_2.txt into change_1.txt
# apply change_1
python updateByLine.py temp_pw_0.txt change_1.txt temp_pw_1.txt

4312 change transactions from change_1.txt
---------------------------------------------------------
# option 3:
<ls>p,l. l1.</ls> => <ls n="Chr.">p,l> <ls n="Chr. p,">l1</ls>
(the 2nd period is optional)
# temp_change_3.txt  (158 changes in 154 entries)

python change_1.py 3 temp_pw_1.txt temp_change_3.txt
#temp_change_3.txt  (158 changes in 154 entries)

# edit temp_change_3.txt
# insert temp_change_3.txt into change_1.txt

# apply change_1
python updateByLine.py temp_pw_0.txt change_1.txt temp_pw_1.txt

4470 change transactions from change_1.txt
---------------------------------------------------------
# option 4:
<ls>p,l. p1,l1.</ls> => <ls n="Chr.">p,l> <ls n="Chr.">p1,l1.</ls>
(the 2nd period is optional)
# temp_change_4.txt  (427 changes in 396 entries)

python change_1.py 4 temp_pw_1.txt temp_change_4.txt
# 

# edit temp_change_4.txt
# insert temp_change_4.txt into change_1.txt

# apply change_1
python updateByLine.py temp_pw_0.txt change_1.txt temp_pw_1.txt

4897 change transactions from change_1.txt

---------------------------------------------------------
# option 5:
old: <ls>p,l. p1,l1. p2,l2.</ls>
new: <ls n="Chr.">p,l> <ls n="Chr.">p1,l1.</ls> <ls n="Chr.">p2,l2.</ls>
(the 3rd period is optional)

python change_1.py 5 temp_pw_1.txt temp_change_5.txt
# temp_change_5.txt  (135 changes in 122 entries)

# edit temp_change_5.txt
# insert temp_change_5.txt into change_1.txt

# apply change_1
python updateByLine.py temp_pw_0.txt change_1.txt temp_pw_1.txt

5032 change transactions from change_1.txt

---------------------------------------------------------
# option 6:
old: <ls>p,l. p1,l1. p2,l2. ...</ls>
new: <ls n="Chr.">p,l> <ls n="Chr.">p1,l1.</ls> <ls n="Chr.">p2,l2.</ls> ...
(the 3rd period is optional)

python change_1.py 6 temp_pw_1.txt temp_change_6.txt
# temp_change_6.txt  (45 changes in 39 entries) 

# edit temp_change_6.txt
# insert temp_change_6.txt into change_1.txt

# apply change_1
python updateByLine.py temp_pw_0.txt change_1.txt temp_pw_1.txt

5077 change transactions from change_1.txt

---------------------------------------------------------
---------------------------------------------------------
At this point there are still quite a few <ls>[0-9].
695 matches in 664 lines for "<ls>[0-9]" in buffer: temp_pw_1.txt
A few of these may be Chr.,  but many are otherwise.
Handle manually

change_1a.py generates pro-forma change transactions.
python change_1a.py temp_pw_1.txt temp_change1a.txt
# temp_change1a.txt  (664 changes in 633 entries)
# manually edit
# insert into change_1.txt
# apply change1a
python updateByLine.py temp_pw_0.txt change_1.txt temp_pw_1.txt
5742 change transactions from change_1.txt

---------------------------------------------------------
Extra correction from Andhrabharati
<L>3663<pc>1043-1<k1>anavakASita
 HARIV. -> HARISV.  Added at 'MISC.' section of change_1.txt
 Also, add HARISV. to pwauth abbreviations.
 
---------------------------------------------------------
# put new version of pw.txt into csl-orig
cp temp_pw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt

---------------------------
# reconstruct local dictionary -- make sure new pw.xml validates
cd  /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'pw ' redo_xampp_all.sh
sh generate_dict.sh pw  ../../pw
# creates pw.xml and installs local displays into
# /c/xampp/htdocs/cologne/pw directory
---------------------------
# validation of local pw.xml
# this uses python program xmlvalidate.py in /c/xampp/htdocs/cologne/
# in Jim's installation.  At Cologne, this validation
# is done by the 'xmllint' program, but this is not part of git bash.
sh xmlchk_xampp.sh pw
python3 ../../xmlvalidate.py ../../pw/pywork/pw.xml ../../pw/pywork/pw.dtd
ok  # <<< this confirms that pw.xml validates in relation to pw.dtd.
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue93
---------------------------
# Now that we have checked the form based on the revised pw.txt,
# we can commit csl-orig and push to github
cd /c/xampp/htdocs/cologne/csl-orig/
git pull # in case someone else has pushed changes to github
# Already up to date.  -- No other changes at this time
git status
# v02/pw/pw.txt   << That's the only change, our new version, as expected
git add .
git status  # just to be sure we know what will be committed.
 # modified:   v02/pw/pw.txt
# commit , include reference to this issue 91.
git commit -m "PW ls markup
Ref: https://github.com/sanskrit-lexicon/PWK/issues/93"
git push  # sync csl-orig with github
---------------------------
# sync Cologne with github
# login to cologne site via ssh
# cd to location of scans directory at cologne. Then,
cd csl-orig
git pull
 #  v02/pw/pw.txt 
 # 1 file changed, A insertions(+), B deletions(-)
# regenerate pw displays at Cologne, using new pw.txt
cd ../csl-pywork/v02
grep 'pw ' redo_cologne_all.sh  # get the cologne command to regenerate pw
# execute the script
sh generate_dict.sh pw  ../../PWScan/2020/
# lots of output. Everything works ok.
# installation of new pw at Cologne FINISHED.
---------------------------------------------------------
Recompute the summary.
python lsextract_all.py temp_pw_1.txt temp_pw_tooltip.txt lsextract_pw_1.txt
