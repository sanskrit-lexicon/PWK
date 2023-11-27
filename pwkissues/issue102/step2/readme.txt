issue102/step2
examine how temp_pw_ab_17a.txt evolves from temp_pw_AB_v2.txt
11-24-2023 begin

cp ../temp_pw_ab_17a.txt ../temp_pw_v1_0.txt
cp ../temp_pw_AB_v2.txt ../temp_pw_v2_0.txt

-----
resolve cases where v2 has a comment (';;')
remove the comments from both files as part of the resolution
grep ';;' ../temp_pw_v2_0.txt | wc -l
# 49 comments
Remove extra blank lines from both
wc -l ../temp_pw_v?_0.txt
  674019 ../temp_pw_v1_0.txt
  674019 ../temp_pw_v2_0.txt
cd ../
diff temp_pw_AB_v2.txt temp_pw_v2_0.txt > diff_AB_v2_v2_0.txt
-----
Part 1: skipped (erroneous run of bb.py)
-----

Part 2:  minor difference
 (i.e., same after removal of ' .,;')
python minorchange.py ../temp_pw_v1_0.txt ../temp_pw_v2_0.txt temp_change_v1_02.txt
1725 changes written to temp_change_v1_02.txt

touch ../change_v1_1.txt

# manually insert temp_change_v1_02.txt into ../change_v1_1.txt
# generate ../temp_pw_v1_1.txt
cd ../
python updateByLine.py temp_pw_v1_0.txt change_v1_1.txt temp_pw_v1_1.txt
# 1725 change transactions from change_v1_1.txt

diff temp_pw_v1_1.txt temp_pw_v2_0.txt | wc -l
# 21456
diff temp_pw_v1_1.txt temp_pw_v2_0.txt > tempdiff.txt


-----
Part 3 Several manual changes. See change_v1_1.txt for more details
cp temp_pw_v1_1.txt temp_pw_v1_1_work.txt
# make the changes in temp_pw_v1_1_work.txt

# generate change file
python diff_to_changes_dict.py temp_pw_v1_1.txt temp_pw_v1_1_work.txt step2/temp_change_v1_03.txt
# 2088 changes written to step2/temp_change_v1_03.txt

# manually insert into change_v1_1.txt

# generate ../temp_pw_v1_1.txt
python updateByLine.py temp_pw_v1_0.txt change_v1_1.txt temp_pw_v1_1.txt
# 3813 change transactions
# check
diff temp_pw_v1_1.txt temp_pw_v1_1_work.txt | wc -l
# 0, as expected

diff temp_pw_v1_1_work.txt temp_pw_v2_0.txt > tempdiff.txt
# 13656  (about 3400 lines diff remain)

-----

Part 4:
python bb.py ../temp_pw_v1_1.txt ../temp_pw_v2_0.txt temp_change_v1_04.txt
1489 changes written to temp_change_v1_04.txt

# manually insert temp_change_v1_04.txt into change_v1_1.txt

# regenerate ../temp_pw_v1_1.txt
python updateByLine.py temp_pw_v1_0.txt change_v1_1.txt temp_pw_v1_1.txt
# 5302 change transactions

diff temp_pw_v1_1.txt temp_pw_v2_0.txt > tempdiff.txt
# 7700  (about 1900 lines diff remain)

-----
Part 5: diff only in bot tag
python bot.py ../temp_pw_v1_1.txt ../temp_pw_v2_0.txt temp_change_v1_05.txt
59 changes written to temp_change_v1_05.txt

# manually insert temp_change_v1_05.txt into change_v1_1.txt

# regenerate ../temp_pw_v1_1.txt
python updateByLine.py temp_pw_v1_0.txt change_v1_1.txt temp_pw_v1_1.txt
# 5361 change transactions

diff temp_pw_v1_1.txt temp_pw_v2_0.txt > tempdiff.txt
# 7464 (about 1860 lines diff remain)

-----
Part 6:  TODO one.dtd
<lang n="arabic">X</lang> -> <arab>X</arab>  48
<lang n="greek">X</lang> -> <gk>X</gk> 89
<lang n="mongolian">X</lang> -> <mong>X</mong> 1
<lang n="russian">X</lang> -> <rus>X</rus> 1

cp temp_pw_v1_1.txt temp_pw_v1_1_work.txt
# manually make the changes in temp_pw_v1_1_work.txt

# generate change file
python diff_to_changes_dict.py temp_pw_v1_1.txt temp_pw_v1_1_work.txt step2/temp_change_v1_06.txt
# 136 changes written to step2/temp_change_v1_03.txt

# manually insert step2/temp_change_v1_06.txt into change_v1_1.txt

# generate ../temp_pw_v1_1.txt from change_v1_1.txt
python updateByLine.py temp_pw_v1_0.txt change_v1_1.txt temp_pw_v1_1.txt
# 5497 change transactions
# check
diff temp_pw_v1_1.txt temp_pw_v1_1_work.txt | wc -l
# 0, as expected

diff temp_pw_v1_1_work.txt temp_pw_v2_0.txt > tempdiff.txt
# 6934  (about1730 lines diff remain)

-----
Part 7:  
cp temp_pw_v1_1.txt temp_pw_v1_1_work.txt
cp temp_pw_v2_0.txt temp_pw_v2_1_work.txt

# manually make changes in temp_pw_v1_1_work.txt
# and in temp_pw_v2_1_work.txt

changes to temp_pw_v1-1_work.txt.
'<ls>SĀY.</ls> zu <ls>' → '<ls>SĀY. zu ' 172
'<ls>KĀŚ.</ls> zu <ls>' → '<ls>KĀŚ. zu ' 163
'<ls>Vārtt.</ls> zu <ls>' → '<ls>Vārtt. zu ' 9
'<ls>BHAR.</ls> zu <ls>' → '<ls>BHAR. zu ' 1
'<ls>ŚAṂK.</ls> zu <ls>' → '<ls>ŚAṂK. zu ' 102
'<ls>UTPALA</ls> zu <ls>' → '<ls>UTPALA zu ' 97
'<ls>NĪLAK.</ls> zu <ls>' → '<ls>NĪLAK. zu ' 66
'<ls>VIṬṬHALA</ls> zu <ls>' → '<ls>VIṬṬHALA zu ' 1
'<ls>KUMĀRASV.</ls> zu <ls>' → '<ls>KUMĀRASV. zu ' 33
'<ls>CAKR.</ls> zu <ls>' → '<ls>CAKR. zu ' 12
'<ls>GARBE</ls> zu <ls>' → '<ls>GARBE zu ' 35
'<ls>KULL.</ls> zu <ls>' → '<ls>KULL. zu ' 76
'<ls>MAHĪDH.</ls> zu <ls>' → '<ls>MAHĪDH. zu ' 29
'<ls>HARISV.</ls> zu <ls>' → '<ls>HARISV. zu ' 1
'<ls>GAUḌAP.</ls> zu <ls>' → '<ls>GAUḌAP. zu ' 9
'<ls>UTPALA.</ls> zu <ls>' → '<ls>UTPALA. zu ' 15  ;; NOTE UTPALA above 
'<ls>SĀRAS.</ls> zu <ls>' → '<ls>SĀRAS. zu ' 1
'<ls>MALLIN.</ls> zu <ls>' → '<ls>MALLIN. zu ' 7
'<ls>ŚĀK.</ls> zu <ls>' → '<ls>ŚĀK. zu ' 4
'<ls>MIT.</ls> zu <ls>' → '<ls>MIT. zu ' 5 ?
'<ls>KAUŚ.</ls> zu <ls>' → '<ls>KAUŚ. zu ' 1
'<ls>KAIY.</ls> zu <ls>' → '<ls>KAIY. zu ' 1
'<ls>GOVINDĀN.</ls> zu <ls>' → '<ls>GOVINDĀN. zu ' 15
'<ls>UJJVAL.</ls> zu <ls>' → '<ls>UJJVAL. zu ' 6
'<ls>PADDH.</ls> zu <ls>' → '<ls>PADDH. zu ' 5
'<ls>RĀMADĀSA</ls> zu <ls>' → '<ls>RĀMADĀSA zu ' 1
'<ls>MEDHĀT.</ls> zu <ls>' → '<ls>MEDHĀT. zu ' 2
'<ls>VYĀSA</ls> zu <ls>' → '<ls>VYĀSA zu ' 4
'<ls>UVAṬA</ls> zu <ls>' → '<ls>UVAṬA zu ' 1
'<ls>SIDDH. K.</ls> zu <ls>'  '<ls>SIDDH. K. zu ' 5
'<ls>VIJÑĀNEŚVARA</ls> zu <ls>'  '<ls>VIJÑĀNEŚVARA zu ' 7
'<ls>DAŚAK.</ls> zu <ls>'  '<ls>DAŚAK. zu ' 1
'<ls>DĀRILA</ls> zu <ls>'  '<ls>DĀRILA zu ' 4
'<ls>SUD.</ls> zu <ls>'  '<ls>SUD. zu ' 1
'<ls>KAHĪRASV.</ls> zu <ls>'  '<ls>KAHĪRASV. zu ' 2

After these changes, only 1 instance of '</ls> <ls>'

# generate change file fpr v1
python diff_to_changes_dict.py temp_pw_v1_1.txt temp_pw_v1_1_work.txt step2/temp_change_v1_07.txt
# 917 changes written to step2/temp_change_v1_07.txt

# manually insert step2/temp_change_v1_07.txt into change_v1_1.txt

# generate ../temp_pw_v1_1.txt from change_v1_1.txt
python updateByLine.py temp_pw_v1_0.txt change_v1_1.txt temp_pw_v1_1.txt
# 6414 change transactions
# check
diff temp_pw_v1_1.txt temp_pw_v1_1_work.txt | wc -l
# 0, as expected

--
# generate change file fpr v2
python diff_to_changes_dict.py temp_pw_v2_0.txt temp_pw_v2_1_work.txt step2/temp_change_v2_07.txt
# 7 changes written to step2/temp_change_v2_07.txt
# touch change_v2_1.txt
# manually insert step2/temp_change_v2_07.txt into change_v2_1.txt

# generate ../temp_pw_v2_1.txt from change_v2_1.txt
python updateByLine.py temp_pw_v2_0.txt change_v2_1.txt temp_pw_v2_1.txt
#  change transactions
# check
diff temp_pw_v2_1.txt temp_pw_v2_1_work.txt | wc -l
# 0, as expected

3512
diff temp_pw_v1_1_work.txt temp_pw_v2_1_work.txt > tempdiff.txt
# 2428 lines approx. 600 lines are different.

---------------

Part 8  differences with broken bar and other minor differences

python bb1.py ../temp_pw_v1_1.txt ../temp_pw_v2_1.txt temp_change_v1_08.txt
113 changes written to temp_change_v1_08.txt

# manually insert step2/temp_change_v1_08.txt into change_v1_1.txt

# regenerate ../temp_pw_v1_1.txt from change_v1_1.txt
python updateByLine.py temp_pw_v1_0.txt change_v1_1.txt temp_pw_v1_1.txt
# 6527 change transactions

---------------

Part 09  differences in metaline

python metaline.py ../temp_pw_v1_1.txt ../temp_pw_v2_1.txt temp_change_v1_09.txt
4 changes written to temp_change_v1_09.txt

# manually examine step2/temp_change_v1_09.txt.
# manually insert step2/temp_change_v1_09.txt into change_v1_1.txt
# QUESTION These differences are in k2. We have k1=X and k2 = X_Y
#  This differs from other metalines with '_' in k2 (30 cases with '_' in k2)

# regenerate ../temp_pw_v1_1.txt from change_v1_1.txt
python updateByLine.py temp_pw_v1_0.txt change_v1_1.txt temp_pw_v1_1.txt
# 6531 change transactions

---------------
Part 10
 differences re root markup

python root.py ../temp_pw_v1_1.txt ../temp_pw_v2_1.txt temp_change_v1_10.txt
64 changes written to temp_change_v1_10.txt

# manually insert step2/temp_change_v1_10.txt into change_v1_1.txt

# regenerate ../temp_pw_v1_1.txt from change_v1_1.txt
python updateByLine.py temp_pw_v1_0.txt change_v1_1.txt temp_pw_v1_1.txt
# 6595 change transactions


---------------
Part 11
 differences in root/devanagari markup

python deva.py ../temp_pw_v1_1.txt ../temp_pw_v2_1.txt temp_change_v1_11.txt
22 changes written to temp_change_v1_11.txt

# manually insert step2/temp_change_v1_11.txt into change_v1_1.txt

# regenerate ../temp_pw_v1_1.txt from change_v1_1.txt
python updateByLine.py temp_pw_v1_0.txt change_v1_1.txt temp_pw_v1_1.txt
# 6617 change transactions

---------------

Part 12  differences ls markup

python ls.py ../temp_pw_v1_1.txt ../temp_pw_v2_1.txt temp_change_v1_12.txt
300 changes written to temp_change_v1_12.txt

# manually insert step2/temp_change_v1_12.txt into change_v1_1.txt
# QUESTION what does 
# regenerate ../temp_pw_v1_1.txt from change_v1_1.txt
python updateByLine.py temp_pw_v1_0.txt change_v1_1.txt temp_pw_v1_1.txt
# 6917  change transactions

---------------

Part 13  differences with broken bar and other non-minor differences

python bb2.py ../temp_pw_v1_1.txt ../temp_pw_v2_1.txt temp_change_v1_13.txt
160 changes written to temp_change_v1_13.txt

# manually edit step2/temp_change_v1_13.txt.
# Mark 11 as NOCHANGE, to be examined later
# manually insert step2/temp_change_v1_13.txt into change_v1_1.txt

# regenerate ../temp_pw_v1_1.txt from change_v1_1.txt
python updateByLine.py temp_pw_v1_0.txt change_v1_1.txt temp_pw_v1_1.txt
# 7066 change transactions



---------------
Part 14:
The rest of the differences
python alldiff.py ../temp_pw_v1_1.txt ../temp_pw_v2_1.txt temp_change_v1_14.txt
# 207 changes

# manually edit step2/temp_change_v1_14.txt.
# Mark 32 as NOCHANGE , to be examined later
# manually insert step2/temp_change_v1_14.txt into change_v1_1.txt

# regenerate ../temp_pw_v1_1.txt from change_v1_1.txt
python updateByLine.py temp_pw_v1_0.txt change_v1_1.txt temp_pw_v1_1.txt
# 7241 change transactions

---------------
Part 15:
The rest of the differences -- Note v2 (AB) is put first
python alldiff.py ../temp_pw_v2_1.txt ../temp_pw_v1_1.txt temp_change_v2_15.txt
# 32 changes

# manually edit step2/temp_change_v2_15.txt.
; Some additional changes to be resolved in next Part.
# manually insert step2/temp_change_v2_15.txt into change_v2_1.txt

# regenerate ../temp_pw_v2_1.txt from change_v2_1.txt
python updateByLine.py temp_pw_v2_0.txt change_v2_1.txt temp_pw_v2_1.txt
# 39 change transactions

---------------
Part 16:
The rest of the differences
python alldiff.py ../temp_pw_v1_1.txt ../temp_pw_v2_1.txt temp_change_v1_16.txt
# 9 changes 

# manually insert step2/temp_change_v1_16.txt into change_v1_1.txt

# regenerate ../temp_pw_v1_1.txt from change_v1_1.txt
python updateByLine.py temp_pw_v1_0.txt change_v1_1.txt temp_pw_v1_1.txt
# 7250 change transactions

----------------
Part 17:
diff temp_pw_v1_1.txt temp_pw_v2_1.txt | wc -l
4
What is this difference?

diff temp_pw_v1_1.txt temp_pw_v2_1.txt
596161c596161
< <LEND>
---
> <LEND> [Page7-059-c]

# Manually add Part17 change to change_v1_1.txt

# regenerate ../temp_pw_v1_1.txt from change_v1_1.txt
python updateByLine.py temp_pw_v1_0.txt change_v1_1.txt temp_pw_v1_1.txt
# 7251 change transactions

----------------
diff temp_pw_v1_1.txt temp_pw_v2_1.txt
# 0 
Now v1_1 = v2_1 Hurray!

--------------------------
Some open questions.
Part 13
1. Is 'Os sepiae' bot or zoo?  I think zoo
2.〔4,41〕 16 similar. Purpose?

TODO: part 14
TODO <is n="Patañjali">Pat.</is>   display? dtd?

*****************************************************************
We will now work with temp_pw_v1_1.txt
*****************************************************************

# further changes to temp_pw_v1_1.txt
# Add a part 18 to change_pw_v1_1.txt
# Manual additions to change_pw_v1_1.txt
# regenerate temp_pw_v1_1.txt from change_v1_1.txt
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue102  # back here
python updateByLine.py temp_pw_v1_0.txt change_v1_1.txt temp_pw_v1_1.txt
# 7252 change transactions

#Regenerate displays to find xml errors
cp temp_pw_v1_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pw  ../../pw
# generation no problems. All xml records are well-formed.

-----------------
# revise csl-pywork/v02/makotemplates/pywork/one.dtd
# arab, rus, mong tags.
# Now xmlvalidate:
sh xmlchk_xampp.sh pw
# ok  

--------------------
# revise csl-websanlexicon/v02/makotemplates/web/webtc/basicdisplay.php
1.  handle arab, rus, and mong tags (basicdisplay.php)
2.  Old form: vppp-c
    New form: v-ppp-c
2a. Modify /c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/webtc/servepdfClass.php
2b. /c/xampp/htdocs/cologne/csl-websanlexicon/v02/distinctfiles/pw/web/webtc/pdffiles.txt
2c. Note:  csl-apidev/servepdf seems to work fine for pw, with no
    further changes.
    new form works:
      http://localhost/cologne/csl-apidev/servepdf.php?dict=pw&page=2-173
    old form does not work:
    http://localhost/cologne/csl-apidev/servepdf.php?dict=pw&page=2173
3. lang tag for PW
3a.  revise basicadjust.php to treat 'lang' tag as 'ab' tag for PW
  /c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php
3b.  revise c:/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pw/pywork/pwab/pwab_input.txt
    ved. Vedic 
    Prākrit  Prākrit language
    ep.  epic
4. lex tags
   These are already treated as 'ab' tags in add_lex_markup function of basicadjust.php.
--------------------

# revise local csl-apidev for basicadjust and basicdisplay
cd /c/xampp/htdocs/cologne/csl-websanlexicon/v02
sh apidev_copy.sh


*****************************************************************
# push repositories to GitHub
*****************************************************************
---- csl-pywork
cd /c/xampp/htdocs/cologne/csl-pywork/
git pull # check for other revisions. Normally no action required
git status  # pwab_input.txt, one.dtd
git add .
git commit -m "PW: Ref: https://github.com/sanskrit-lexicon/PWK/issues/102"
git push

----- csl-orig
cd /c/xampp/htdocs/cologne/csl-orig
git pull # check for other revisions. Normally no action required
git status  # v02/pw/pw.txt
git add .
git commit -m "PW: Ref: https://github.com/sanskrit-lexicon/PWK/issues/102"
git push

----- csl-websanlexicon
cd /c/xampp/htdocs/cologne/csl-websanlexicon/
git pull # check for other revisions. Normally no action required
git status  # basicadjust.php, basicdisplay.php, pdffiles.txt for pw, servepdfClass.php
git add .
git commit -m "PW: Ref: https://github.com/sanskrit-lexicon/PWK/issues/102"
git push

----- csl-apidev
cd /c/xampp/htdocs/cologne/csl-apidev/
git pull # check for other revisions. Normally no action required
git status  # basicadjust.php, basicdisplay.php
git add .
git commit -m "PW: Ref: https://github.com/sanskrit-lexicon/PWK/issues/102"
git push

*****************************************************************
update Cologne server
*****************************************************************
# login via ssh
# cd to scans directory
----
cd csl-websanlexicon
git pull
----
cd ../csl-pywork
git pull
----
cd ../csl-apidev
git pull
----
cd ../csl-orig
git pull  # 149297 insertions(+), 157391 deletions(-)
----
# update displays for pw
cd ../csl-pywork/v02
grep 'pw ' redo_cologne_all.sh
# sh generate_dict.sh pw  ../../PWScan/2020/

sh generate_dict.sh pw  ../../PWScan/2020/


*****************************************************************
Some open questions.
*****************************************************************
Part 13
1. Is 'Os sepiae' bot or zoo?  I think zoo
2.〔4,41〕 16 similar. Purpose?

TODO: part 14
TODO <is n="Patañjali">Pat.</is>   display? dtd?

