pwkissues/issue111/readme.txt
bot tag analysis
Begun 12-11-2024

# this directory
cd /c/xampp/htdocs/sanskrit-lexicon/pwk/pwkissues/issue111

# issue 111 link
 https://github.com/sanskrit-lexicon/PWK/issues/111

# start with temp_pw_0.txt as copy of
  csl-orig/v02/pw/pw.txt at current commit
   2f98062a22a0b3be203471fc58f78cf695038a97
cd /c/xampp/htdocs/cologne/csl-orig
git show 2f98062a:v02/pw/pw.txt > /c/xampp/htdocs/sanskrit-lexicon/pwk/pwkissues/issue111/temp_pw_0.txt

# start with temp_mw_0.txt as copy of
  csl-orig/v02/mw/mw.txt at current commit
   2f98062a22a0b3be203471fc58f78cf695038a97
cd /c/xampp/htdocs/cologne/csl-orig
git show 2f98062a:v02/mw/mw.txt > /c/xampp/htdocs/sanskrit-lexicon/pwk/pwkissues/issue111/temp_mw_0.txt

python summary.py 1 temp_pw_0.txt summary_0_standard.txt summary_0_nonstandard.txt
170556 entries found
8301 instances of bot
findall_bot_entries: number of lines with duplicates= 3
5949 cases written to summary_0_standard.txt
2352 cases written to summary_0_nonstandard.txt

---------------------------------------------------
version 1: make species word lower case
python make_change.py species temp_pw_0.txt change_pw_1.txt
2099 change records written to change_pw_1.txt

python updateByLine.py temp_pw_0.txt change_pw_1.txt temp_pw_1.txt
643111 lines read from temp_pw_0.txt
643111 records written to temp_pw_1.txt
2099 change transactions from change_pw_1.txt

python summary.py 1 temp_pw_1.txt summary_1_standard.txt summary_1_nonstandard.txt
8301 instances of bot
8096 cases written to summary_1_standard.txt
205 cases written to summary_1_nonstandard.txt

---------------------------------------------------
version 2
change_pw_2.txt created manually.

# case 1 
revert <bot n="X">Y</bot> to <bot>X</bot>  11 cases

# case 2 capitalize Genus - 20 cases
python make_change.py genus temp_pw_1.txt temp_change_pw_2_genus.txt
# manual insert into change_pw_2.txt

# case 3 synonyms in parens - 7 cases (alternate genus)
python make_change.py paren temp_pw_1.txt temp_change_pw_2_paren.txt
7 change records written to temp_change_pw_2_paren.txt
# do some prettyfying of temp_change_pw_2_paren.txt
# manual insert into change_pw_2.txt

# case 4 single words (to be expanded)
python make_change.py single temp_pw_1.txt temp_change_pw_2_single.txt
167 change records written to temp_change_pw_2_single.txt
# manual edit. Most are print changes (add 'inherited' genus)
-----
python updateByLine.py temp_pw_1.txt change_pw_2.txt temp_pw_2.txt
205 change transactions from change_pw_2.txt

python summary.py 1 temp_pw_2.txt summary_2_standard.txt summary_2_nonstandard.txt
8302 instances of bot
8302 cases written to summary_2_standard.txt
0 cases written to summary_2_nonstandard.txt

So now, in temp_pw_2.txt, all <bot> tags are 'standard':
 <bot>Genus species</bot> or <bot>Genus species auth</bot>

---------------------------------------------------
cd freq
python bot_freq.py ../temp_pw_2.txt bot_freq_pw_2.txt
1301 distinct bot tags

Cross reference genus species to wcpw
gs = genus species

Add field : gs=N
  <bot>G S</bot> F -> <bot>G S</bot> F gs=N
  <bot>G S A</bot> F -> <bot>G S a</bot> F gs=N
  where N is the count of records in wcvp_names which match G and S
  Note F is the count of instances in pw digitization.

------------------------
# 'revise' cases where both the Genus and the species are not found in wcvp data
python bot_freq_gs.py bot_freq_pw_2.txt ../wcpw/temp_wcvp_gs.txt bot_freq_pw_2_gs.txt
1301 lines read from bot_freq_pw_2.txt
1021628 lines read from ../wcpw/temp_wcvp_gs.txt
1021628 distinct gs keys
39551 distinct g keys
182487 distinct s keys
1301 written to bot_freq_pw_2_gs.txt
grep 'g=0,s=0' bot_freq_pw_2_gs.txt > bot_freq_pw_2_gs_00.txt
wc -l bot_freq_pw_2_gs_00.txt
82 bot_freq_pw_2_gs_00.txt

# Manually add info to each line of bot_freq_pw_2_gs_00.txt
# cp bot_freq_pw_2_gs_00.txt bot_freq_pw_2_gs_00_edit.txt
# manual changes to bot_freq_pw_2_gs_00_edit.txt
# Generate change records from bot_freq_pw_2_gs_00_edit.txt

python make_change_pw_1_2c.py ../temp_pw_2.txt bot_freq_pw_2_gs_00_edit.txt temp_change_2_3a.txt
83 lines read from bot_freq_pw_2_gs_00_edit.txt
217 change records written to temp_change_2_3a.txt

# manual insert temp_change_2_3a.txt in ../change_pw_3.txt

cd ../
python updateByLine.py temp_pw_2.txt change_pw_3.txt temp_pw_3.txt
217 change transactions from change_pw_3.txt

cd freq
python bot_freq.py ../temp_pw_3.txt bot_freq_pw_3.txt
1231 written to bot_freq_pw_3.txt

----
python bot_freq_gs.py bot_freq_pw_3.txt ../wcpw/temp_wcvp_gs.txt bot_freq_pw_3_gs.txt
1234 written to bot_freq_pw_3_gs.txt

grep 'g=0,s=0' bot_freq_pw_3_gs.txt > bot_freq_pw_3_gs_00.txt
wc -l bot_freq_pw_3_gs_00.txt
# 0 bot_freq_pw_3_gs_00.txt

------------------------
# 'revise' cases where The Genus is not found in wcvp (but species is found)
grep 'g=0,' bot_freq_pw_3_gs.txt > bot_freq_pw_3_g_0.txt
wc -l bot_freq_pw_3_g_0.txt
242 bot_freq_pw_3_g_0.txt

python make_change_pw_1_2c.py ../temp_pw_2.txt bot_freq_pw_3_g_0_edit.txt temp_change_2_3b.txt
242 lines read from bot_freq_pw_3_g_0_edit.txt
548 change records written to temp_change_2_3b.txt

# manual insert temp_change_2_3b.txt in ../change_pw_3.txt

cd ../
python updateByLine.py temp_pw_2.txt change_pw_3.txt temp_pw_3.txt
126 change transactions from change_pw_3.txt

cd freq
python bot_freq.py ../temp_pw_3.txt bot_freq_pw_3.txt
7989 bot tags
1032 distinct bot tags
1032 written to bot_freq_pw_3.txt

python bot_freq_gs.py bot_freq_pw_3.txt ../wcpw/temp_wcvp_gs.txt bot_freq_pw_3_gs.txt
1032 written to bot_freq_pw_3_gs.txt

grep 'g=0,' bot_freq_pw_3_gs.txt > bot_freq_pw_3_g_0.txt
One item remains.



------------------------------------------------------------
Genus found, but not species

python summary.py 1 temp_pw_3.txt summary_3_standard.txt summary_3_nonstandard.txt
7988 cases written to summary_3_standard.txt
0 cases written to summary_3_nonstandard.txt

cd freq
grep ',s=0' bot_freq_pw_3_gs.txt > bot_freq_pw_3_s_0.txt
wc -l bot_freq_pw_3_s_0.txt
8 bot_freq_pw_3_s_0.txt

# Manually add info to each line of bot_freq_pw_3_s_00.txt
# cp bot_freq_pw_2_gs_00.txt bot_freq_pw_2_gs_00_edit.txt
# manual changes to bot_freq_pw_2_gs_00_edit.txt

# generate changes
python make_change_pw_1_2c.py ../temp_pw_3.txt bot_freq_pw_3_s_0_edit.txt temp_change_2_3c.txt
164 lines read from bot_freq_pw_3_s_0_edit.txt
490 Change records returned by make_changes
490 change records written to temp_change_2_3c.txt

# manual insert temp_change_2_3c.txt at bottom of ../change_pw_3.txt

cd ../
python updateByLine.py temp_pw_2.txt change_pw_3.txt temp_pw_3.txt
1554 change transactions from change_pw_3.txt

python summary.py 1 temp_pw_3.txt summary_3_standard.txt summary_3_nonstandard.txt
7987 cases written to summary_3_standard.txt
0 cases written to summary_3_nonstandard.txt

cd freq
python bot_freq.py ../temp_pw_3.txt bot_freq_pw_3.txt
7988 bot tags
872 distinct bot tags


python bot_freq_gs.py bot_freq_pw_3.txt ../wcpw/temp_wcvp_gs.txt bot_freq_pw_3_gs.txt
873 written to bot_freq_pw_3_gs.txt

grep ',s=0' bot_freq_pw_3_gs.txt > bot_freq_pw_3_s_0.txt
<bot>Curcuma amhaldi</bot> 9 gs=0,g=213,s=0

grep 'g=0,' bot_freq_pw_3_gs.txt 
<bot>Daemia extensa</bot> 1 gs=0,g=0,s=92

python bot_freq_gs_revised.py bot_freq_pw_3.txt ../wcpw/temp_wcvp_gs.txt bot_freq_pw_3_gs_revised2.txt


grep 'gs=0,' bot_freq_pw_3_gs_revised2.txt > bot_freq_pw_3_gs_0_revised2.txt
wc -l bot_freq_pw_3_gs_0_revised1.txt
12 bot_freq_pw_3_gs_0_revised1.txt

WFO: https://www.worldfloraonline.org/

cat bot_freq_pw_3_gs_0_revised2.txt

Amphidonax karka(9)
Artemisia sternutatoria Roxb. (1)  kew has 'sternutatoria' wfo has same as pw
Artemisia sternutatoria (5)  kew has 'stemutatoria'
Basilicum pilosum Benth. (1)
Chenopodium vasica (1)
Clerodendrum phlomoides (16)
Cucumis sulcatus (1)
Curcuma amhaldi (9)
Daemia extensa (1)
Schoenanthus indicus (1)
Wrightia sirissa (1)
Zanthoxylum hastile (2)

Also,
Acacia sirissa (38) (not in db, but is at https://powo.science.kew.org/)


python make_change_gs.py ../temp_pw_3.txt bot_freq_pw_3_gs_0.txt temp_change_gs.txt

python make_change_gs.py ../temp_pw_3.txt bot_freq_pw_3_gs_0_revised.txt temp_change_gs.txt
49 lines read from bot_freq_pw_3_gs_0_revised.txt
251 Change records returned by make_changes
251 change records written to temp_change_gs.txt


python make_change_pw_auth.py ../temp_pw_3.txt bot_freq_pw_3_gs_0_revised.txt temp_change_gs.txt


As of this writing (12-19-2024), the
----------------------------------------------------------

python summary.py 1 temp_pw_3.txt summary_3_standard.txt summary_3_nonstandard.txt
<bot>Curcuma amhaldi</bot> 9 gs=0,g=213,s=0   Might be same as Curcuma amada
<bot>Daemia extensa</bot> 1 gs=0,g=0,s=92 bot sp.
 "Daemia extensa"  Acc. to wikipeia a synonym of Pergularia daemia
 
python summary.py 3a temp_pw_3.txt wcpw/temp_wcvp_primary_auth.txt summary_3a_auth_known.txt summary_3a_auth_unknown.txt

A list of the 'unknown' auths. 
They are identified KEW authors. 
For instance 'A. Juss. == A.Juss. (2)' is understood as:
 - The author 'A. Juss.' occurs twice in pw_3
 - 'A.Juss.' is the spelling in the KEW database
 - 'Adrien-Henri de Jussieu (1797–1853)' is the name, according to this wikipedia article:
    https://en.wikipedia.org/wiki/List_of_botanists_by_author_abbreviations
    
A. Juss. == A.Juss. (2)  Adrien-Henri de Jussieu (1797–1853)
Ait. == Aiton (8) William Aiton (1731–1793)
Bl. == Blume  (3) (but not Amorphophallus campanulatus Bl.) Carl Ludwig Blume (1796–1862)
Chois. == Choisy (3) Jacques Denys Choisy (1799–1859)
Dec. == DC. (1)  Augustin Pyramus de Candolle (1778–1841)
Hamilt. Roxb. == ? (1) William Hamilton (1783–1856)  William Roxburgh (1751–1815)
Jon. == Jones (1) William Jones (1746–1794)
Koen. == J.Koenig (1) Johann Gerhard Koenig (1728–1785)
Lin. == L. (17) Carl Linnaeus (or Carolus Linnæus) (1707–1778)
R. Br. == R.Br.  (13)  Robert Brown (1773–1858)
Rottl. == Rottler (1)  Johan Peter Rottler (1749–1836)
Sch. == Schott  (1) Heinrich Wilhelm Schott (1794–1865)
Sch. u. Endl. (2) == Schott & Endl. Heinrich Wilhelm Schott (1794–1865), Stephan Friedrich Ladislaus Endlicher (1804–1849)
Spr. == Spreng. (2)  Curt Polycarp Joachim Sprengel (1766–1833)
Tournef. == Tourn. (2) Joseph Pitton de Tournefort (1656–1708) 
W. u. A. == Wight & Arn. (14) Robert Wight (1796–1872) George Arnott Walker-Arnott (1799–1868)
W. und A. == Wight & Arn. (1) Robert Wight (1796–1872), George Arnott Walker-Arnott (1799–1868)


The KEW database has been revised since Jim downloaded it 8 months ago.
Randomly, several differences have been noticed between
 - the KEW database used by the analysis of this issue
 - https://powo.science.kew.org/  
Clypea hernandifolia -> Clypea hernandiifolia  (dii)
Croton polyandrum -> Croton polyandrus


----------------------------------------

# Generate change records from 
# for 'auth' values which start with lower case letter.

python make_change_pw_auth.py lo temp_pw_3.txt pw_botauth_standard.txt temp_change_auth_lo.txt
32 lines read from pw_botauth_standard.txt
38 change records written to temp_change_auth_lo.txt
# cp temp_change_auth_lo.txt temp_change_auth_lo_edit.txt, and
#manual change temp_change_auth_lo.txt.

#insert temp_change_auth_lo.txt into change_pw_3.txt
Note: temp_change_auth_lo.txt. no longer needed
python updateByLine.py temp_pw_2.txt change_pw_3.txt temp_pw_3.txt

python summary.py 1 temp_pw_3.txt summary_3_standard.txt summary_3_nonstandard.txt
7988 cases written to summary_3_standard.txt
0 cases written to summary_3_nonstandard.txt

cd freq
python bot_freq.py ../temp_pw_3.txt bot_freq_pw_3.txt
888
python bot_freq_gs.py bot_freq_pw_3.txt ../wcpw/temp_wcvp_gs.txt bot_freq_pw_3_gs.txt
grep 'g=0,' bot_freq_pw_3_gs.txt > bot_freq_pw_3_g_0.txt
One item remains. see above

grep ',s=0' bot_freq_pw_3_gs.txt > bot_freq_pw_3_s_0.txt
 wc -l bot_freq_pw_3_s_0.txt
2 bot_freq_pw_3_s_0.txt

cd ../
python summary.py 3 temp_pw_3.txt summary_3_auth.txt
47 cases written to summary_3_auth.txt

-------
print change Cyperus hexastachyus communis Nees -> Cyperus hexastachyus Nees  (3)
1294 change transactions.

cd freq
python bot_freq.py ../temp_pw_3.txt bot_freq_pw_3.txt
884 written to bot_freq_pw_3.txt

python bot_freq_gs.py bot_freq_pw_3.txt ../wcpw/temp_wcvp_gs.txt bot_freq_pw_3_gs.txt
grep 'g=0,s=0' bot_freq_pw_3_gs.txt > bot_freq_pw_3_gs_00.txt
wc -l bot_freq_pw_3_gs_00.txt
# 0 bot_freq_pw_3_gs_00.txt

readme_printchange.txt: all the 'pc:' lines from change_pw_3.txt,
 with some editing. 1063 instances.
These print changes will be inserted into pw_printchange.txt in
csl-corrections repository.

file readme_change.txt provides a summary of the three change files
  change_pw_1.txt, and _2 and _3.

----------------------------------------------------
12-21-2024  Install

# local install
sh redo_pw.sh 3
# this copies temp_pw_3.txt to csl-orig/v02/pw/pw.txt

# sync pw.txt to github
cd /c/xampp/htdocs/cologne/csl-orig
git add .
git commit -m "PW: bot tags
Ref: https://github.com/sanskrit-lexicon/PWK/issues/111"
# 3106 lines changed
git push

# csl-corrections
cd /c/xampp/htdocs/cologne/csl-corrections
# insert print changes into dictionaries/pw/pw_printchanges.txt
  from file readme_printchange.txt
  
# sync repo to github
git add .
git commit -m "PW: bot tag print changes
Ref: https://github.com/sanskrit-lexicon/PWK/issues/111"
# 1067 insertions
git push

# sync cologne with github
# login to cologne server
pull csl-orig
pull csl-corrections
cd csl-pywork
# remake pw display.
sh generate_dict.sh pw  ../../PWScan/2020/

-------------------
# return 'home'
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue111

Sync this repo to github
git add .
git commit -m "#111  bot tag revisions"
git push
