pwkissues/issue106/readme.txt
https://github.com/sanskrit-lexicon/PWK/issues/106
Begin 02-10-2024

alternate headwords for pw  (with merged pwkvn see issue 104

local directory of this readme
cd /c/xampp/htdocs/sanskrit-lexicon/pwk/pwkissues/issue106

----------------------------------------------------------
initialize temp_pw_0.txt from csl-origing at commit on date 02-10-2024
 commit a63f7049bb3e238527ad7cf4b9b5ad4766a1a079
cd /c/xampp/htdocs/cologne/csl-orig/v02/pw
git show a63f7049:v02/pw/pw.txt > temp_pw_0.txt
mv temp_pw_0.txt /c/xampp/htdocs/sanskrit-lexicon/pwk/pwkissues/issue106/
cd /c/xampp/htdocs/sanskrit-lexicon/pwk/pwkissues/issue106

----------------------------------------------------------
temp_pw_1.txt  misc. corrections
cp temp_pw_0.txt temp_pw_1.txt
# Manual changes.  Preserve number of lines.
- parvan L=96646 merged into 69945 pora
- pravAla L=73144 merged into  73143, pravAqa
- AzwakIya L=16300 merge into 16299 Azwaka
- Dru L= 55950 merge into Dru 55949
- peSI L=69764 merge into peSI 69763

- tarkapaYcAnana L=44904  insert missing text
- darBamUlI L=49112 insert missing text
- dvAviMSatyakzara L=53788 insert missing text
- niranukroSakArin L=58874 insert missing text
- SIrzaktimant L=113078 insert missing text
- aDikArma L=2804 - Note this has empty text in pw print.
- a L=2 : move ¦ (see below)
- vas L=99303 accent in k2 (see homchk.py below)
- {#* -> *{# 1052 instances (see 'asterisk note' below)
- *#} -> #}*  1 instance (see 'asterisk note' below
- Remove '_' character (hiatus
  30 matches for "<L>.*_" in buffer: temp_pw_1.txt
  32 matches for "_.*¦" in buffer: temp_pw_1.txt
- Remove (?) or (!) in metaline k2 : 13 instances
   <L>37108<pc>2-186-b<k1>gOtamasa<k2>gOtamasa(?)
   <L>38573<pc>2-208-a<k1>catu<k2>catu(!)
   <L>40366<pc>2-233-b<k1>cIraRIya<k2>cIraRIya(?)
   <L>41341<pc>2-248-a<k1>jaNgapUga<k2>*jaNgapUga(!)
   <L>42137<pc>2-258-c<k1>jalambala<k2>*jalambala(!)
   <L>42838<pc>2-268-a<k1>jinendraBUti<k2>jinendraBUti(?)
   <L>43273<pc>2-274-a<k1>jEhmAkani<k2>jEhmAkani(!)
   <L>43912<pc>2-283-b<k1>qambura<k2>qambura(?)
   <L>45205<pc>3-021-a<k1>tAndana<k2>*tAndana(!)
   <L>45670<pc>3-027-b<k1>tigala<k2>tigala(?)
   <L>45919<pc>3-030-b<k1>tilakanija<k2>tilakanija(!)
   <L>102349<pc>6-087-c<k1>viWaNka<k2>*viWaNka(!)
   <L>102522<pc>6-090-a<k1>viTUtistotra<k2>viTUtistotra(!)
- Change k1, k2 from jinamantraSAstra -> jinamantraSAstrastotrAdi
   <L>42819<pc>2-267-c<k1>jinamantraSAstra<k2>jinamantraSAstra
   {#jinamantraSAstrastotrAdi#}¦
-  <h>[0-9]+ -> ''  (remove <h> in metaline) 7097
------------
02-16-2024
touch change_1.txt  # 
python diff_to_changes_dict.py temp_pw_0.txt temp_pw_1.txt temp_change_1.txt
1086 changes written to temp_change_1.txt

----------------------------------------------------------
1. 13252 matches for "¦ *$"
2. 13242 matches for "¦ *
<div" 
3. 10 matches for "¦ *
<[^d]"
  This generates some changes noted above.
  After changes, 3 matches.
----------------------------------------------------------
7097 matches for "<h>\([0-9]+\)<LB><hom>\1.</hom>"
7097 matches for "<h>\([0-9]+\)"
Conclude: <h>\([0-9]+\)  is consistent with next line - so <h>N can be removed.
---
a, L=2 : <hom>2.</hom> {#a°#} vor Consonanten, {#an°#} vor Vocalen¦
But also an L=3170: <hom>2.</hom> {#a°#} vor Consonanten, {#an°#} vor Vocalen¦
conclude: In L=2, move ¦

----------------------------------------------------------
homchk: check consistency of
  (a) <k2>X<h>N  in metaline  (<h> required 7097 cases)
  (b) markup of next line (broken-bar line) <hom>N.</hom> ..{#X#}
homchk.py in code subdirectory.
 Note: found correction L=99303 mentioned above.
----------------------------------------------------------
nohomchk: check consistency of
  (a) <k2>X  in metaline  (no <h>)
  (b) markup of next line (broken-bar line)  ..{#X#}
nohomchk.py in code subdirectory.
----------------------------------------------------------
02-11-2024
asterisk note:
936 matches for "{#[*].*¦" in buffer: temp_pw_1.txt
 Like: {#*akata#}¦  All within pwkvn sections
30434 matches in 28492 lines for "[*]{#" in buffer: temp_pw_1.txt

62 matches for "¦.*?{#[*]" in buffer: temp_pw_1.txt
 All within pwkvn sections
1 match for "[*]#}" Ayata, in pwkvn section
7 matches for "#}[*]" in buffer: temp_pw_1.txt

For consistency between pwkvn and pw,  change all
  {#* -> *{#  
  *#} -> #}*   
manually changed in temp_pw_1.txt

----------------------------------------------------------
temp_pw_1a.txt
# remove <h>N from metalines.
# python code/hremove.py temp_pw_1.txt temp_pw_1a.txt
7097 lines changed
----------------------------------------------------------

----------------------------------------------------------
temp_pw_2.txt
Misc. changes to 1a
touch change_1a_2.txt
 change_1a_2.txt may have several sections, iteratively made.
--- 01 markup of additional denominative roots
475 matches for "^!√{#[^#]*y#}¦, {#°yat[ie]#}"  already marked
102 matches for "^{#[^#]*y#}¦, {#°yat[ie]#}"  add !√ markup
---
python code/change_denom.py temp_pw_1a.txt temp_change.txt
103 records written to temp_change.txt
# Note: Why 103 and not 102?
# manually insert temp_change.txt into change_1a_2.txt
# update temp_pw_2.txt from change_1a_2.txt
python updateByLine.py temp_pw_1a.txt change_1a_2.txt temp_pw_2.txt
# 102 change transactions from change_1a_2.txt
# So now 102!
------------- 02
# from AB: found one entry L-45920, which has √ mark, but should be with the !√ mark; and it has a typo tilakaya for tilakay
# update temp_pw_2.txt from change_1a_2.txt
python updateByLine.py temp_pw_1a.txt change_1a_2.txt temp_pw_2.txt
104 change transactions from change_1a_2.txt
-------------
--- 03 possible root markup
identification
 consonant-vowel-consonant
python code/possible_roots.py ../temp_pw_2.txt temp_possible_roots.txt
Edit manually:  possible_roots_edit.txt
358 noted for √ markup

#  change transactions
python code/possible_roots_change.py temp_pw_2.txt possible_roots_edit.txt temp_possible_roots1_change.txt

# manually insert into change_1a_2.txt
# update temp_pw_2.txt
python updateByLine.py temp_pw_1a.txt change_1a_2.txt temp_pw_2.txt
764479 lines read from temp_pw_1a.txt
764479 records written to temp_pw_2x.txt
462 change transactions from change_1a_2.txt
462 of type new

--- 04 possible root markup, version 1
python code/possible_roots1.py temp_pw_2.txt temp_possible_roots1.txt
43 records
 
python code/possible_roots1_change.py temp_pw_2.txt temp_possible_roots1.txt temp_possible_roots1_change.txt

#add roots1 to change_1a_2.txt
# recompute temp_pw_2.txt
python updateByLine.py temp_pw_1a.txt change_1a_2.txt temp_pw_2.txt
495 change transactions

? noted for √ markup

--- typo
x002_	{#prAtimokza#}¦ ({#pAtimokKa#} im <lang>Pāli</lang>) <lex>m.</lex> = {#prAtimoksa#}. Ursprünglich Entlastung <ls>OLD. Buddha. 339. 379</ls>.	<L>74318<pc>4-186-b<k1>prAtimokza<k2>prAtimokza	364741
prAtimoksa -> pratimokza

--- roots TODO
002_	{#arD#}¦, {#fdDa/#} 3〉 {%gelungen%} <ls>VS. 18,11</ls>. — Mit {#vi, vyfdDa#} {%sündlich%} <ls>ĀPAST.</ls><info n="sup_1"/>	<L>201221<pc>1-294-a<k1>arD<k2>arD	678907
002_	{#tarq#}¦, {#saMtfqya#} <ls>ŚĀṄKH. ŚR. 17,12,1</ls> wohl nur fehlerhaft für {#saMtfdya#}.<info n="sup_6"/>	<L>208953<pc>6-301-c<k1>tarq<k2>tarq	709825
002_	{#parj#}¦, {#pfRajmi#} = {#parc#} <ls>ĀPAST. ŚR. 12,28,16</ls>.<info n="sup_6"/>	<L>209096<pc>6-303-b<k1>parj<k2>parj	710397
002_	{#plI#}¦, {#viplIyante#} <ls>SĀMAV. BR.</ls> fehlerhaft für {#vivlIyante#}.<info n="sup_6"/>	<L>209173<pc>6-304-a<k1>plI<k2>plI	710705
004_	{#spUrD#}¦ (= {#sparD#}), von Simplex nur {#spUrDa/se#} {%zur wetteifernden Bewerbung%}.	<L>131473<pc>7-221-c<k1>spUrD<k2>spUrD	651844
004_	{#nIkz#}¦ (= {#nikz#}) mit {#pra#} {%spiessen auf%} (<ab>Loc.</ab>) <ls>ĀPAST. ŚR. 7,22,9</ls>.<info n="sup_6"/>	<L>209068<pc>6-303-a<k1>nIkz<k2>nIkz	710285
004_	{#tij#}¦, (*{#tejati#}) {#te/jate#}	<L>45709<pc>3-027-c<k1>tij<k2>tij	223797
005_	{#UNK#}¦ mit {#ni#} in {#nyUNKa#} und {#nyUNKamAnaka#}.	<L>20969<pc>1-256-a<k1>UNK<k2>UNK	98220
006_	*{#parp#}¦ (?), {#parpati#} ({#gatO#}).	<L>64716<pc>4-051-b<k1>parp<k2>*parp	317966
007_	*{#kzaj#}¦ oder *{#kzaYj, kzajate#} oder {#kzaYjate#} ({#gatidAnayos#}) {#kzaYjayati#} ({#kacCrajIvane#}).	<L>32190<pc>2-119-c<k1>kzaj<k2>*kzaj	154062
007_	*{#kzIb#}¦ oder *{#kzIv, kzIbati#} oder {#kzIvati#} ({#nirAte#}).	<L>32588<pc>2-126-c<k1>kzIb<k2>*kzIb	156264
005_	{#UNK#}¦ mit {#ni#} in {#nyUNKa#} und {#nyUNKamAnaka#}.	<L>20969<pc>1-256-a<k1>UNK<k2>UNK	98220
004_	{#tij#}¦, (*{#tejati#}) {#te/jate#}	<L>45709<pc>3-027-c<k1>tij<k2>tij	223797

----------------------------------------------------------
02-19-2024
 Alternate headword candidates 'close to' broken bar

python code/bb_after.py temp_pw_2.txt temp_bb_after.txt temp_bbchange.txt
# temp_bbchange.txt:  those indicated JF or AB in bb_after.py
66 identified by AB
26 identified by JF
30610 candidates. 158370 metalines
30611 outrecs
30611 records written to temp_bb_after.txt
93 outrecs
93 records written to temp_bbchange.txt

manually edit temp_bbchange.txt
 - metaline edit <k2>
 - bbline edit ¦
insert edited temp_bbchange.txt into change_1a_2.txt  (05) 93 entries changed

# update temp_pw_2.txt
python updateByLine.py temp_pw_1a.txt change_1a_2.txt temp_pw_2.txt
679 change transactions from change_1a_2.txt


----------------------------------------------------------
02-20-2024  TOFINISH
--- 06 possible root markup, version 2
 Candidate criteria:
 a. in pwkvn section (L>=200000)
 b. k1 ends in consonant
NOT matching any of
¦ <lex>
¦ (!) <lex>
¦ <ab>Absol.</ab>
¦ [1-6]\. ?<info n="sup_7"/>
ar#}¦ <ab>Nom. ag.</ab>
a/?nt#}¦
#} und {#.*?¦

 
python code/possible_roots2.py temp_pw_2.txt temp_possible_roots2.txt

 
python code/possible_roots1_change.py temp_pw_2.txt temp_possible_roots1.txt temp_possible_roots1_change.txt

#add roots1 to change_1a_2.txt
# recompute temp_pw_2.txt
python updateByLine.py temp_pw_1a.txt change_1a_2.txt temp_pw_2.txt

----------------------------------------------------------
remake local display (temporary)
sh redolocal.sh
"""
cp temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pw  ../../pw
sh xmlchk_xampp.sh pw
cd /c/xampp/htdocs/cologne/csl-orig/v02/
git restore pw.txt
cd /c/xampp/htdocs/sanskrit-lexicon/pwk/pwkissues/issue106
"""
**********************************************************
Notes on earlier work, currently a false trail
**********************************************************
----------------------------------------------------------
Classification of broken-bar lines
X¦ Y 
From X, we will derive <k2>K2
The forms of X are various, so the derivations of K2 will be various
A classification of X will clarify the derivations.
python bbclass.py ../temp_pw_1.txt ../bbclass
  various classes ../bb_01.txt, ../bb_02.txt, etc. Total
  number of classes not yet known.

764479 lines read from ../temp_pw_2.txt
113180 records written to ../bb/bb_01.txt
25554 records written to ../bb/bb_01a.txt
1082 records written to ../bb/bb_01b.txt
1387 records written to ../bb/bb_01c.txt
5 records written to ../bb/bb_01d.txt
6316 records written to ../bb/bb_02.txt
730 records written to ../bb/bb_02a.txt
144 records written to ../bb/bb_02b.txt
411 records written to ../bb/bb_02c.txt
819 records written to ../bb/bb_03.txt
71 records written to ../bb/bb_03a.txt
97 records written to ../bb/bb_03b.txt
24 records written to ../bb/bb_03c.txt
1 records written to ../bb/bb_04.txt
1 records written to ../bb/bb_04a.txt
8548 records written to ../bb/bb_NA.txt

----------------------------------------------------------
temp_pw_2.txt
  Remove <h>N in metalines.  7096
  Namely, change <k2>X<h>N to <k2>N. X
  hremove.py
----------------------------------------------------------
temp_pw_3.txt
  Identify further althw candidates

----------------------------------------------------------

bb_k2prob.py analyzes 'simple' cases (no alternate headwords)
It examples 1 case for each of the 'bbcodes' (see bb.py above) except 'NA'
Using the regex associated with the bbcode (in bb.py), a k2 is COMPUTED from
 the broken-bar line.
The metaline k2 should equal the broken-bar k2.
Any exceptions are written to the output file
The script bb_k2prob_all.sh in code directory does this analysis for each
 bbcode.

----------------------------------------------------
NO SCAN: TODO
<L>209421<pc>7-289-a<k1>aMholiNga<k2>aMholiNga
https://www.sanskrit-lexicon.uni-koeln.de/scans/csl-apidev/servepdf.php?dict=pw&page=7-289

image is avail for pwkvn:
https://www.sanskrit-lexicon.uni-koeln.de/scans/csl-apidev/servepdf.php?dict=pwkvn&page=7-289
---------------------------------------------------------
Alternate headwords.
These are identified in bb_NA.txt.



***********************************************************
OLD NOTES
----------------------------------------------------------
Save a copy of the metalines of pw that have <e>
grep -E '<e>' temp_pw_0.txt > pw_e_metalines.txt

wc -l pw_e_metalines.txt
# 135764 pw_e_metalines.txt

----------------------------------------------------------
temp_pw_1.txt : remove <e>N
python remove_e.py temp_pw_0.txt temp_pw_1.txt
764479 lines read from temp_pw_0.txt
764479 lines written to temp_pw_1.txt

Note: In <e>N,  the code N is of form ddd  (3 digits)
--------
# test displays for pwk
 
cp temp_pw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pw  ../../pw
sh xmlchk_xampp.sh pw
# ok  


-------------------------------------------------------
install temp_pw_1 into csl-orig.
---
First, locally.
cd /c/xampp/htdocs/sanskrit-lexicon/pwk/pwkissues/issue106
cp temp_pw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt

--- pull csl-orig, to get latest repository
cd /c/xampp/htdocs/cologne/csl-orig/v02/
git pull # in case

# sync to github
cd /c/xampp/htdocs/cologne/csl-orig/v02/
git pull #
git add .
git commit -m "PW: remove <e>N codes from metaline.
Ref: https://github.com/sanskrit-lexicon/PWK/issues/106"
git push


---------------------
sync cologne from github for csl-orig repository
--- regenerate displays at Cologne
# login to cologne server
cd csl-pywork/v02, etc.
---------------------
Sync this repo to github
cd /c/xampp/htdocs/sanskrit-lexicon/pwk/pwkissues/issue106
git add .
git commit -m "PW: remove <e>N codes from metaline.
Ref: https://github.com/sanskrit-lexicon/PWK/issues/106"
---------------------

TODO 5-257-b (naw) L=207518) page not found
