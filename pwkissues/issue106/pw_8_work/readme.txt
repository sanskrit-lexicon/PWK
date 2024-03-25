pw_8_work
continue alternate headword (k2) work.
Ref: https://github.com/sanskrit-lexicon/PWK/issues/106
03-19-2024 begin

cdsl starts with ../temp_pw_7b.txt
----------------------------------------------------------------
AB's supporting files:
  2812 diff.pwk7b.metalines.txt
  5909 diff.pwk7b.non-metalines.txt
   104 diff.pwkvn.7b.metalines.txt
  8825 total number of lines

----------------------------------------------------------------
01: diff.pwkvn.7b.metalines.txt

 26 cases.
 The numbers in this pwkvn AB file are a mystery - (as in previous
 pwkvn files).
 This file is simple, each 'case' having (CDSL) and (AB) versions.
 and these are all metalines, so we can match on L.
 
python make_change_01.py ../temp_pw_7b.txt diff.pwkvn.7b.metalines.txt temp_change_7b_8_01.txt

 25 of the cases are where AB prefers to put (X) into metaline.
   This is OK with Jim
  1 other case <L>206886 is correction to Jim.
So, Jim agrees with the changes.

# start file of changes from 7b to 8
touch ../change_7b_8.txt
# manual insert temp_change_7b_8_01.txt into ../change_7b_8.txt

# calculate ../temp_pw_8.txt
cd ../
python updateByLine.py temp_pw_7b.txt change_7b_8.txt temp_pw_8.txt
764917 records written to temp_pw_8.txt
26 change transactions from change_7b_8.txt

----------------------------------------------------------------
02: diff.pwk7b.metalines.txt


 This file is almost simple, each 'case' having (CDSL) and (AB) versions.
 and these are all metalines, so we can match on L.
 However, in 33 cases, AB for some reason groups two metalines
 
python alter_diff_02.py diff.pwk7b.metalines.txt diff.pwk7b.metalines1.txt
2812 from diff.pwk7b.metalines.txt
684 groups found
722 normalized groups
722 groups found
2888 lines written to diff.pwk7b.metalines1.txt

# make_change_01.py should work for diff.pwk7b.metalines1.txt
# but make minor changes to the python code for easier analysis
python make_change_02.py ../temp_pw_8.txt diff.pwk7b.metalines1.txt temp_change_7b_8_02.txt

# edit temp_change_7b_8_02.txt
# examine the 'cat=other' cases.

BEGIN  Jim disagrees with AB for 02 (diff.pwk7b.metalines) 
AB should also check the bbline for these
These are all slp1-hiatus, except for sAradIya
---
<L>65285<pc>4-059-b<k1>paSvaizwi<k2>pa/Sva_izwi
  pa/Sva_izwi -> pa/Svaizwi 
---
<L>70206<pc>4-126-c<k1>praugya<k2>pra_ugya^
  pra_ugya^ -> praugya^
---
<L>73947<pc>4-181-b<k1>prAghAra<k2>prAg_hAra
  prAg_hAra -> prAghAra
---
<L>82771<pc>5-021-c<k1>manaU<k2>mana_U
  mana_U -> manaU
---
<L>110933<pc>6-215-a<k1>SavasauSInara<k2>Savasa_uSInara
  Savasa_uSInara -> SavasauSInara
---
 AB: <L>124385<pc>7-121-b<k1>sAradIyanAmamAlA<k2>sAradIyanAmamAlA, (SAradIyanAmamAlA)
Jim: <L>124385<pc>7-121-b<k1>sAradIya<k2>sAradIya, (SAradIya), SAradIyanAmamAlA
 Note: Also bbline change {#nAmamAlA#} -> {#°nAmamAlA#}  PRINT CHANGE done
---
<L>124654<pc>7-124-c<k1>sAvairisole<k2>sAva_irisole
  sAva_irisole -> sAvairisole
END    Jim disagrees with AB:

# manual insert temp_change_7b_8_02.txt into ../change_7b_8.txt

# calculate ../temp_pw_8.txt
cd ../
python updateByLine.py temp_pw_7b.txt change_7b_8.txt temp_pw_8.txt

764917 records written to temp_pw_8.txt
748 change transactions from change_7b_8.txt

----------------------------------------------------------------
03: diff.pwk7b.non-metalines.txt
  1468 cases
--------------------------------
Removed last 'section' of AB file
673576a673594
(AB): 
673581d673598
(CDSL): 
-------------------------------
Some sections change the number of lines (e.g. 310253)
cp diff.pwk7b.non-metalines.txt diff.pwk7b.non-metalines1.txt

edit diff.pwk7b.non-metalines1.txt:
  remove these 'multiline' sections from diff.pwk7b.non-metalines1.txt and
  put into diff_multiline.txt

TODO 11 cases into diff_multiline.txt

-------------------------------
11 sections are multiline.
The rest are 4-line sections.
As above, make all the sections 4-line sections
python alter_diff_03.py diff.pwk7b.non-metalines1.txt diff.pwk7b.non-metalines2.txt

# Some revisions to diff.pwk7b.non-metalines2.txt will be needed,
# when a (CDSL) line in this file differs from the text in pw_7b.txt
cp diff.pwk7b.non-metalines2.txt diff.pwk7b.non-metalines3.txt
# manual edits will be made to diff.pwk7b.non-metalines3.txt
#
-------------------------------
Analyze diff.pwk7b.non-metalines3.txt

python analyze_03.py '00' ../temp_pw_8.txt diff.pwk7b.non-metalines3.txt temp.txt
-5 48  ab text has 5 or fewer characters less than cdsdl text
-4 104
-3 7
-2 6
-1 31
0 232 ab text and cdsl text have same number of characters 
1 838 ab text has 1 more character than cdsl text
2 39
3 4
4 127
5 26
----------------------------------------------------------------
03: 0  ab text and cdsl text have same number of characters  (232)
python make_change_03.py '0' ../temp_pw_8.txt diff.pwk7b.non-metalines2.txt temp_change_7b_8_03_0.txt

# manually edit temp_change_7b_8_03_0.txt. A few adjustments
# insert revised temp_change_7b_8_03_0.txt into change_7b_8.txt

# calculate ../temp_pw_8.txt
cd ../
python updateByLine.py temp_pw_7b.txt change_7b_8.txt temp_pw_8.txt
764917 records written to temp_pw_8.txt
980 change transactions from change_7b_8.txt

----------------------------------------------
03: 1  ab text has 1 more character than cdsl text

python make_change_03.py '1' ../temp_pw_8.txt diff.pwk7b.non-metalines3.txt temp_change_7b_8_03_1.txt

# manually edit temp_change_7b_8_03_1.txt. A few adjustments
# insert revised temp_change_7b_8_03_1.txt into change_7b_8.txt

# calculate ../temp_pw_8.txt
cd ../
python updateByLine.py temp_pw_7b.txt change_7b_8.txt temp_pw_8.txt
764917 records written to temp_pw_8.txt
1811 change transactions from change_7b_8.txt

----------------------------------------------------------------
03: 2  The rest. len(ab) - len(cdsl) is > 1 or < 0

python make_change_03.py '2' ../temp_pw_8.txt diff.pwk7b.non-metalines3.txt temp_change_7b_8_03_2.txt

# manually edit temp_change_7b_8_03_2.txt. A few adjustments
# insert revised temp_change_7b_8_03_2.txt into change_7b_8.txt

# calculate ../temp_pw_8.txt
cd ../
python updateByLine.py temp_pw_7b.txt change_7b_8.txt temp_pw_8.txt
764917 records written to temp_pw_8.txt
2193 change transactions from change_7b_8.txt

--------------------

BEGIN Jim disagrees with AB for 03 (diff.pwk7b.non-metalines)
  Jim request AB to make these changes --
  some of these changes were mentioned previously by Jim
     but not yet changed by AB.
---
; <L>8008<pc>1-093-c<k1>aByeza<k2>*aByeza, *aByezIya, aByezya cat=0:¦other ?
;36205 old *{#aByeza#} <lex>m.</lex> und *<lex>Adj.</lex> {#aByezIya#}, {#aByezya#}¦ <is>gaṇa</is> {#apUpAdi#}.
;36205 new *{#aByeza#} <lex>m.</lex> und *{#aByezIya#}, {#aByezya#} <lex>Adj.</lex>¦ <is>gaṇa</is> {#apUpAdi#}.
  Jim: No need for this print change
---
; <L>8010<pc>1-094-a<k1>aByoza<k2>*aByoza, *aByozIya, aByozya cat=0:¦other ?
;36213 old *{#aByoza#} <lex>m.</lex> und *<lex>Adj.</lex> {#aByozIya#}, {#aByozya#}¦ = {#aByuza#} <ab>u. s. w.</ab>
;
;36213 new *{#aByoza#} <lex>m.</lex> und *{#aByozIya#}, {#aByozya#} <lex>Adj.</lex>¦ = {#aByuza#} <ab>u. s. w.</ab>
  Jim: No need for this print change
---
113841 old <L>24215<pc>2-014-c<k1>kapicUqa<k2>*kapicUqa, *kapicUqa, *kapicUta
113841 new <L>24215<pc>2-014-c<k1>kapicUqa<k2>*kapicUqa, *kapicUqA, *kapicUta
 AB to make additional metaline change
---
131617 old <L>27670<pc>2-063-b<k1>kAsa<k2>2. kAsa, kAsa
131617 new <L>27670<pc>2-063-b<k1>kAsa<k2>2. kAsa, kAsA
 AB to make additional metaline change
---
{#pa/Sva_izwi#}¦ <lex>Adj.</lex> {%Heerden begehrend%}.
  pa/Sva_izwi -> pa/Sva_izwi
---
{#prAg_hAra#}¦ <lex>m.</lex> fehlerhaft für {#pragBAra#}.
  prAg_hAra -> prAghAra
---
{#mana_U#}¦ <lex>m.</lex> = <arab>منع</arab> {%eine <ab>best.</ab> Constellation%} <ls>Ind. St. 2,282</ls>.
  mana_U -> manaU
---
{#va/syazwi#}¦ <lex>f.</lex> = {#vasya_izwi#} (in der concreten ....
  vasya_izwi -> vasyaizwi
---
{#Savasa_uSInara#}¦, {#°rezu#} <ls>GOP. BR. 1,2 ...
  Savasa_uSInara -> SavasauSInara
---
{#sAva_irisole#}¦ <ab>N. pr.</ab> eines Districts.
  sAva_irisole -> sAvairisole
---
{#hemakuqya#}, {#°kuRdDya#} oder {#°kUwya#}¦ <ab>N. pr.</ab> einer Oertlichkeit.
  kuRdDya -> kuRqya
---
{#aBizwipA/si#}¦ <ls>ṚV. 2,20,2</ls> nach <ls>GRASSMANN.</ls> für {#aBi/zwI pAsi#}.
  aBizwipA/si -> aBizwipA/(si)  by print
---
{#pra_ugya^#}¦ <lex>Adj.</lex> {%am%} {#pra_uga#} 1〉a〉 {%befindlich%}.
  pra_uga -> prauga
---
<div n="p">— Mit {#na#} {%aufhören zu sein, vergehen, zu Nichte werden, zu Grunde gehen, sterben;%} mit {#iha-na#} {%auf ...
  {#iha-na#} -> {#iha na#}   [No - in print]
---
{#mantraratna#} <lex>n.</lex>, {#°ratnakoSa#} <lex>m.</lex>, {#°ratrAkara#}, {#°ratnvalI#} <lex>f.</lex> und {#mantrarahasyaprakASikA#} <lex>f.</lex>¦ Titel von Werken.
  {#°ratrAkara#} -> {#°ratnAkara#}
  {#°ratnvalI#}  -> {#°ratnAvalI#}
---
{#muhUrtawIkA#} <lex>f.</lex>, {#muhUrtatattva#} <lex>n.</lex>, {#muhUrtadarSana#} <lex>n.</lex>, {#muhUrtadIpaka#} <lex>m.</lex>, {#°dIpikA#} <lex>f.</lex>, {#muhUrtanirRaya#} <lex>m.</lex> (<ls>BURNELL, T.</ls>), {#muhUrtapadavI#} <lex>f.</lex>, {#muhUrtaparIkzA#} <lex>f.</lex>, {#muhUrtaBAga#} <lex>m.</lex>, {#muhUrtaBUzaRa#} <lex>n.</lex>, {#muhUrtaBErava#}, {#muhUrtamaRi#} <lex>m.</lex>, {#muhUrtamADavIya#} <lex>n.</lex>, {#muhUrtamArtaRqa#} <lex>m.</lex> ({#°mArtARqa#} fehlerhaft), {#muhUrtamAlA#} <lex>f.</lex>, {#muhUrtaratna#} <lex>n.</lex>, {#muhUrtaratnAkara#} <lex>m.</lex>, {#muhUrtarAjIya#}, {#muhUrtalakzaRapawala#}, {#muhUrtavallaBA#} <lex>f.</lex>, {#muhUrtaSAstra#} <lex>n.</lex>, {#muhUrtasaMgraha#} <lex>m.</lex>, {#muhUrtasarvasva#} <lex>n.</lex>, {#muhUrtasAra#} <lex>m.</lex> <ls>BURNELL, T.</ls> und {#muhUrtasidDi#} <lex>f.</lex>¦ Titel von Werken <ls>OPP. CAT. 1</ls>.
  {#muhUrtarAjIya#} -> {#muhUrtarAjIya#} <lex>n.</lex>
---
<div n="1">— 1〉 {%Jagd%}. Der <ab>Acc.</ab> wird verbunden mit {#Aw#}, {#pari-Aw#}, {#gam#}, {#car#}, {#pari-DAv#} (<ls n="Chr.">58,12</ls>), {#yA#}, {#nis-yA#}, {#pra-yA#} und {#vi-har#}; der <ab>Dat.</ab> mit {#yA#}, {#nis-gA#} und {#vi-har#}
   {#Aw#}, {#pari-Aw#} -> {#aw#}, {#pari-aw#}
---
<div n="p">— Mit {#aBini#} {%untergehen über%} (<ab>Acc.</ab>) <ls>MAITR. S. 1,8,7 (125,18. 21)</ls> {#aBinimrukta#} {%derjenige, welchen die untergehende Sonne schlafend findet%} <ls>ĀPAST. 2,12,13. 22</ls>. Häufig fehlerhaft {#aBinirmukta#} geschrieben.
  <ls>MAITR. S. 1,8,7 (125,18. 21)</ls> {#aBinimrukta#} ->
  <ls>MAITR. S. 1,8,7 (125,18. 21)</ls>. {#aBinimrukta#}
  [ period missing ]
---
<div n="1">— 9〉 {%Mittel,%} <ab>insbes.</ab> {%Zaubermittel, ein fein ausgedachtes Mittel, Kunstgriff, Kniff;%} die Ergänzung ein Nomen <ab>act.</ab> im <ab>Loc.</ab> oder <ab>Dat.</ab>, oder ein Satz mit {#yaTA#} und <ab>Potent.</ab> {#yuktiM ar#} {%ein Mittel finden, eine List anwenden, — angeben%}. {#°yu/ktyA#}, {#°yuktitas#}, {#°yuktiBis#} und {#°yukti°#} {%vermittelst, vermöge%}. {#yuktyA#}, {#yuktitas#} (<ls n="Chr.">115,17</ls>. <ls n="Chr.">117,14</ls>), {#yuktiBis#} und {#yukti°#} {%auf eine feine, schlaue, versteckte Weise, durch —, mit List, vermittelst einer List, unter irgend einem Vorwande%}.
  {#yuktiM ar#} -> {#yuktiM kar#}
---
<div n="p">— Mit {#ativi#} ({#ati-vi#}) {%in hohem Grade prangen, — glänzen%}. <ls>ṚV. 3,10,7</ls>, ist {#a/ti#} mit {#sri/DaH#}. zu verbinden.
  {#ati-vi#}  ->  {#ati vi#}
---
 <div n="1">— 4〉 {%das Ausschliessen, Ausnehmen%} <ls n="Chr.">228,15</ls>. <ls n="Chr.">31,31</ls>.
  <ls n="Chr.">31,31</ls>  -> <ls n="Chr.">231,31</ls>  [per print]
---
{#zaqgaRa#}¦ <ls>HARIV. 7225 und 7432</ls> wohl fehlerhaft für {#zaqguRa#}, wie die andere <ab>Ausg.</ab> liest.
 <ls>HARIV. 7225 und 7432</ls> ->
 <ls>HARIV. 7225</ls> und <ls n="HARIV.">7432</ls>
---
{%Uebergangszeit, Morgen- oder Abenddämmerung%}. <ab>Acc.</ab> mit {#As#}, {#anu-As#} und {#upa-As#} {%die Morgen-%} oder Abendandacht verrichten.
  oder Abendandacht verrichten  -> oder {%Abendandacht verrichten%}
---
{#ISvarItantra#} <lex>n.</lex> und {#ISvare (<ab>Loc.</ab>) nityasuKAvasTApanam#}¦ Titel von Werken.
  {#ISvare (<ab>Loc.</ab>) nityasuKAvasTApanam#}  ->
  {#ISvare#} (<ab>Loc.</ab>) {#nityasuKAvasTApanam#}
---
<div n="3">— δ〉 verschiedener Männer. Auch {#°tIrTa, °Bawwa#} und {#°miSra#}
  {#°tIrTa, °Bawwa#} und {#°miSra#} -> {#°tIrTa#}, {#°Bawwa#} und {#°miSra#}
   [cf. ACC]
---
<div n="p">— Mit{#anu#}, {#°pAhi#} zu <ls>Spr. 2597</ls> wohl nur fehlerhaft für {#°yAhi#}.
  Mit{#anu#} -> Mit {#anu#}
---
<div n="2">— b〉 {#plakzaH prAstravaRaH#} {%die Quelle der%} <is>Sarasvatī</is> {%oder der Ort des Wiedersichtbarwerdens der%} <is n="Sarasvatī">S.</is>
  {#plakzaH prAstravaRaH#} -> {#plakzaH prAsravaRaH#}
---
END Jim disagrees with AB (03)

----------------------------------------------
manual changes to diff.pwk7b.non-metalines3.txt
Note: the CDSL text of diff.pwk7b.non-metalines3 is
      made to agree with temp_pw_7b.txt
      When AB reviews, he can ignore this section.
---
617156
OLD:
(CDSL): {#sArparAja#}, {#prajApatestisraH sArparAjAH#} (!)¦ Name von <is>Sāman</is> <ls>ĀRṢ. BR.</ls>
NEW:
(CDSL): {#sArparAja#}, {#prajApatestisraH sArparAjAH#}¦ (!) Name von <is>Sāman</is> <ls>ĀRṢ. BR.</ls>

---
478493
OLD:
(CDSL): {#loBAyana#} (!)¦ <lex>m.</lex> <ab>Patron.</ab> Auch <ab>Pl.</ab> <ab>Vgl.</ab> {#AlohAyana#}
NEW:
(CDSL): {#loBAyana#}¦ (!) <lex>m.</lex> <ab>Patron.</ab> Auch <ab>Pl.</ab> <ab>Vgl.</ab> {#AlohAyana#}
---
608306
OLD:
(CDSL): *{#sazki#} (!)¦ <is>gaṇa</is> {#siDmAdi#} Davon <lex>Adj.</lex> {#sazkila#}.
NEW:
(CDSL): *{#sazki#}¦ (!) <is>gaṇa</is> {#siDmAdi#} Davon <lex>Adj.</lex> {#sazkila#}.
---
62943
OLD:
(CDSL): {#AGatana#} (!)¦ <lex>n.</lex> {#AGAtana#} {%Schlachthaus%}.
NEW:
(CDSL): {#AGatana#}¦ (!) <lex>n.</lex> {#AGAtana#} {%Schlachthaus%}.
---
151423
OLD:
(CDSL): <div n="1">— 2〉 {%angreifen, einen Angriff machen auf (?)%}.
NEW:
(CDSL): <div n="1">— 2〉 {%angreifen, einen Angriff machen auf(?)%}.
---
183476
OLD:
(CDSL): {#Guwwi#} (?)¦ <ls>Ind. St. 14,102</ls>; <ab>vgl.</ab> {#GuwikA#} 〔15,384〕.
NEW:
(CDSL): {#Guwwi#}¦ (?) <ls>Ind. St. 14,102</ls>; <ab>vgl.</ab> {#GuwikA#} 〔15,384〕.
---
387310
OLD:
(CDSL): <div n="1">— 2〉 <ab>N. pr.</ab> eines <is>Ṛṣi</is>. {#BaradvAjasya adArasft#} und {#adArasftO#}, {#arkE upahavO, gADam, nakAni, pfSninI, prAsAham, bfhat, mokzE, yajYAyajYIyam, lomanI, vAjakarmIyam, vAjaBft, vizamARi, vratam, SunDyuH#} und {#sEnDukzitAni#} Namen von <is>Sāman</is> <ls>ĀRṢ. BR.</ls>
NEW:
(CDSL): <div n="1">— 2〉 <ab>N. pr.</ab> eines <is>Ṛṣi</is>. {#BaradvAjasya adArasft#} und {#adArasftO#}, {#arkE upahavO, gADam, nakAni, pfSninI, prAsAham, bfhajaBft, vizamARi, vratam, SunDyuH#} und {#sEnDukzitAni#} Namen von <is>Sāman</is> <ls>ĀRṢ. BR.</ls>
---
--------------------------------------------------------
diff_multiline.txt
15 cases.
In all but 1 case, one cdsl line is to be replaced by 2 or more AB lines
In the exception case, two cdsl lines are to be replaced .
  Jim rewrites this exception case so it is like the other cases
cp diff_multiline.txt diff_multiline1.txt
# manually edit diff_multiline1.txt
OLD:
526011,526012
(CDSL): <div n="p">— Mit {#anu#} <ab>Caus.</ab> <ab>Partic.</ab> {#°vIjita#} {%angeweht%}. — Mit {#aBi#} <ab>Caus.</ab> {%befächeln%}.
(CDSL): <div n="p">— Mit {#A#} <ab>Caus.</ab> <ab>dass.</ab>- Mit {#ud#} <ab>Caus.</ab> {%anwehen%}.
(AB): <div n="p">— Mit {#anu#} <ab>Caus.</ab> <ab>Partic.</ab> {#°vIjita#} {%angeweht%}.
(AB): <div n="p">— Mit {#aBi#} <ab>Caus.</ab> {%befächeln%}.
(AB): <div n="p">— Mit {#A#} <ab>Caus.</ab> <ab>dass.</ab>
(AB): <div n="p">— Mit {#ud#} <ab>Caus.</ab> {%anwehen%}.
------------------------

NEW:
526011
(CDSL): <div n="p">— Mit {#anu#} <ab>Caus.</ab> <ab>Partic.</ab> {#°vIjita#} {%angeweht%}. — Mit {#aBi#} <ab>Caus.</ab> {%befächeln%}.
(AB): <div n="p">— Mit {#anu#} <ab>Caus.</ab> <ab>Partic.</ab> {#°vIjita#} {%angeweht%}.
(AB): <div n="p">— Mit {#aBi#} <ab>Caus.</ab> {%befächeln%}.
------------------------
526012
(CDSL): <div n="p">— Mit {#A#} <ab>Caus.</ab> <ab>dass.</ab>- Mit {#ud#} <ab>Caus.</ab> {%anwehen%}.
(AB): <div n="p">— Mit {#A#} <ab>Caus.</ab> <ab>dass.</ab>
(AB): <div n="p">— Mit {#ud#} <ab>Caus.</ab> {%anwehen%}.
------------------------

Now, we use a program to do the replacement of one cdsl by 2 or more ab lines

python split_lines.py ../temp_pw_8.txt diff_multiline1.txt ../temp_pw_8a.txt

764917 from ../temp_pw_8.txt
16 groups found in diff_multiline1.txt
764934 lines written to ../temp_pw_8a.txt

# A check that all is well:
diff ../temp_pw_8.txt ../temp_pw_8a.txt > diff_8_8a.txt
#  quick review says new file as expected.

17 additional lines:

33 (AB)
16 (CDSL)
(- 33 16) = 17

(+ 764917 17) = 764934
---
Check that display construction with 8a works properly
cd ../
sh redolocal.sh 8a
# xml file is fine
-----------------------------------------------------------
THE END
-----------------------------------------------------------
