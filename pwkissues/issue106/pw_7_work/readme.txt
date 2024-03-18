pw_7_work
continue alternate headword (k2) work.
Ref: https://github.com/sanskrit-lexicon/PWK/issues/106
03-16-2024 begin

----------------------------------------------------------------
AB's supporting files:

   52 diff_pwkvn_6a.txt
  322 diff_pwk.v6a.metalines.txt
  182 diff_pwk.v6a.addl.upasarga.split.lines.txt changes # of lines

----------------------------------------------------------------
01: diff_pwkvn_6a.txt
cp ../temp_pw_6a.txt temp_pw_7_work.txt

Based on AB's diff_pwkvn_6a.txt
 13 cases.  All changed.
 Note In two cases, jim also makes corresponding change in metaline
 - 18957 <hom>2.</hom> {#ta#}, {#te#}¦
 - 20965 {#aBiDarma#}, {#°jYAnaprasTAna#} ...

# generate change file
python ../diff_to_changes_dict.py ../temp_pw_6a.txt temp_pw_7_work.txt temp_change_6a_7_01.txt
15 changes written to temp_change_6a_7_01.txt

# manual: insert temp_change_6a_7_01.txt into ../change_6a_7.txt
# recompute temp_pw_7.txt
cd ../  #issue106
python updateByLine.py temp_pw_6a.txt change_6a_7.txt temp_pw_7.txt
764912 lines read from temp_pw_6a.txt
764912 records written to temp_pw_7.txt
15 change transactions from change_6a_7.txt
cd pw_7_work

diff ../temp_pw_7.txt temp_pw_7_work.txt | wc -l
# 0 no diff

# temp_pw_7_work.txt unneeded.
rm temp_pw_7_work.txt

----------------------------------------------------------------
02: diff_pwk.v6a.metalines.txt

Based on AB's diff_pwk.v6a.metalines.txt
  61 cases
# We can generate prototype changes as in pw_6_work
# cp ../pw_6_work/make_change_02.py make_change_02a.py
python make_change_02a.py ../temp_pw_7.txt diff_pwk.v6a.metalines.txt temp_change_6a_7_02.txt
764912 from ../temp_pw_7.txt
322 from diff_pwk.v6a.metalines.txt
61 groups found
62 records written to temp_change_6a_7_02.txt (1 extra as expected)

cp temp_change_6a_7_02.txt temp_change_6a_7_02_edit.org
#Add temp markup for EMACS org mode convenience
   '; <L>' -> '* ; <L>'

#manually edit temp_change_6a_7_02_edit.org

BEGIN NOTES: where Jim disagrees with AB
---
<L>22061<pc>1-270-a<k1>ekAdaSakapAlaM<k2>e/kAdaSakapAlaM
  laM -> la
<L>31692<pc>2-111-a<k1>krandaM<k2>kra/ndaM
  daM -> da
---
<L>36928<pc>2-184-b<k1>govindanATa<k2>govindanATa, ⁅go⁆°vindanAyaka, ⁅go⁆°vindanyAyAlaM_kAraBawwAcArya
  laM_kAra -> laMkAra   (print has लं-कार  the '-' is line break.)
---
<L>70206<pc>4-126-c<k1>praugya<k2>pra_ugya
  pra_ugya -> praugya (_ not needed for slp1 hiatus)
---
<L>73947<pc>4-181-b<k1>prAghAra<k2>prAg_hAra
  prAg_hAra -> prAghAra  (_ not needed in slp1)
---
<L>80876<pc>4-283-b<k1>BedaDikkAra<k2>BedaDikkAra, ⁅BedaDikkAra⁆°vyAKyA, ⁅BedaDikkAravyAKyA⁆°prakASa, ⁅BedaDikkAravyAKyA⁆°satkriyA, kArAnyatkArahuMkfti
  kArAnyatkArahuMkfti -> BedaDikkArAnyatkArahuMkfti
  Note: in MW and ACC: BedaDikkAranyakkArahuMkfti
---
<L>82746<pc>5-020-b<k1>maDvaBAzya<k2>maDvaBAzya, ⁅maDvaBAzya⁆°wIkA, ⁅maDvaBAzya⁆°vyAKyA, maDvamataKaRqana, ⁅maDva⁆°mataprakaraRa, ⁅maDva⁆°matamuKaBaNga, ⁅maDva⁆°matamuKamardana, ⁅maDva⁆°mataviDvMsa, ⁅maDva⁆°mataviDcMsana, maDvamuKaBaNga, maDvamuKamardana
 ⁅maDva⁆°mataviDvMsa, ⁅maDva⁆°mataviDcMsana ->
 ⁅maDva⁆°mataviDvaMsa, ⁅maDva⁆°mataviDvaMsana
---
<L>82771<pc>5-021-c<k1>manaU<k2>mana_U
  mana_U -> manaU  (_ not needed for slp1 hiatus)
---
<L>87109<pc>5-082-a<k1>mIm<k2>1. mIm, a/mImet, mImayat
  remove ', a/mImet, mImayat'   these are verb forms
---
<L>87785<pc>5-093-b<k1>muhUrtawIkA<k2>muhUrtawIkA, muhUrtatattva, muhUrtadarSana, muhUrtadIpaka, ⁅muhUrta⁆°dIpikA, muhUrtanirRaya, muhUrtapadavI, muhUrtarIkzA, muhUrtaBAga, muhUrtaBUzaRa, muhUrtaBErava, muhUrtamaRi, muhUrtamADavIya, muhUrtamArtaRqa, (⁅muhUrta⁆°mArtARqa), muhUrtamAlA, muhUrtaratna, muhUrtaratnAkara, muhUrtarAjAjIyan, muhUrtalakzaRapawala, muhUrtavallaBA, muhUrtaSAstra, muhUrtasaMgraha, muhUrtasarvasva, muhUrtasAra, muhUrtasidDi
  muhUrtarIkzA -> muhUrtaparIkzA
  muhUrtarAjAjIyan -> muhUrtarAjIya
  {#muhUrtarAjAjIyan#} -> {#muhUrtarAjIya#} <lex>n.</lex>  (in bbline)
---
<L>89573<pc>5-117-b<k1>yajYavoQave<k2>yajYavoQave, yajYaM vo°⁅Qave⁆
  yajYaM vo°⁅Qave⁆ -> yajYaM_vo°⁅Qave⁆
---
<L>89639<pc>5-118-a<k1>yajYAsah<k2>yajYAsa/h, (⁅yajYA⁆°sA/ha)
  (⁅yajYA⁆°sA/ha) -> (⁅yajYA⁆°sA/h)
---
557024 new <L>112233<pc>6-232-c<k1>SitivAraM<k2>SitivA/raM
  SitivA/raM -> SitivA/ra ; also in bbline
---
<L>110933<pc>6-215-a<k1>SavasauSInara<k2>Savasa_uSInara
  Savasa_uSInara -> SavasauSInara (_ not needed for slp1 hiatus)
---
<L>116438<pc>6-292-a<k1>zoqaSakAraRajayamAlA<k2>zoqaSakAraRajayamAlA, ⁅oqaSa⁆°kAraRapUjA, zoqaSakArikA, zoqaSakUrca, zoqaSagaRapatiDyAna, ⁅zoqaSa⁆°gaRapatilakzaRa
  ⁅oqaSa⁆°kAraRapUjA -> ⁅zoqaSa⁆°kAraRapUjA
---
<L>121662<pc>7-084-a<k1>sarpizmant<k2>sa/rpizmant, sarpizvant
  sarpizvant -> sarpi/zvant  (also bbline)
---
<L>124385<pc>7-121-b<k1>sAradIya<k2>sAradIya_nAmamAlA, (SAradIya_nAmamAlA)
 (SAradIya_nAmamAlA) -> SAradIyanAmamAlA  cf. ACC
   Also bbline change {#nAmamAlA#} -> {#°nAmamAlA#}  PRINT CHANGE
---
<L>124654<pc>7-124-c<k1>sAvairisole<k2>sAva_irisole
 sAva_irisole -> sAvairisole (_ not needed for slp1 hiatus)
 Also bbline
---
END OF AB-JIM diff comments
----------------------------
# remove temporary markup 
cp temp_change_6a_7_02_edit.org temp_change_6a_7_02_edit.txt
'* DONE ;' -> ';'
'⁅' -> ''
'⁆°' -> ''

# manual insert temp_change_6a_7_02_edit.txt into ../change_6a_7.txt
# recompute temp_pw_7.txt
cd ../  #issue106
python updateByLine.py temp_pw_6a.txt change_6a_7.txt temp_pw_7.txt
764912 lines read from temp_pw_6a.txt
764912 records written to temp_pw_7.txt
96 change transactions from change_6a_7.txt

-----------------------------------------------------------
03: changes based on diff_pwk.v6a.addl.upasarga.split.lines.txt

There are 35 sections.  The idea is to merge some lines.
# The following program does the mergers
python make_change_03.py ../temp_pw_7.txt diff_pwk.v6a.addl.upasarga.split.lines.txt temp_pw_7_work.txt

# generate a standard 'diff' comparison
diff ../temp_pw_7.txt temp_pw_7_work.txt > diff_03.txt

# check the work by comparing AB's file with diff_03.txt
 diff_03_ab.org  slight reorg of diff_pwk.v6a.addl.upasarga.split.lines.txt
 diff_03_cdsl.org slight reorg of diff_03.txt

diff diff_03_cdsl.org diff_03_ab.org > diffdiff.txt
diffdiff.txt contains only 'diff markup' differences.
This confirms the changes in temp_pw_7_work.txt are as intended.


-----------------------------------------------------------
# removal of some extra blank lines (per AB)

python remove_lines.py '2,3' temp_pw_7_work.txt temp_pw_7_work1.txt
 # remove lines 2 and 3 and remove 'extra' blank lines
remove_lnums: line #  3
remove_lnums: line #  4
drop blank line at lnum =  140548
drop blank line at lnum =  140553
remove_extra_in: 2 lines dropped
remove_extra_in: 764944 lines returned
remove_extra_out: 27 lines dropped
remove_extra_out: 764917 lines returned
764917 lines written to temp_pw_7_work1.txt


temp_pw_7_work1 has all the AB changes in the 3 files above

-----------------------------------------------------------
Correct the mrit/mruc mess noted by AB:
 (ref: https://github.com/sanskrit-lexicon/PWK/issues/106#issuecomment-2001997496)

cp temp_pw_7_work1.txt ../temp_pw_7a.txt
# Manually edit ../temp_pw_7a.txt

OLD:
<L>89274<pc>5-113-a<k1>mrit<k2>mrit
√{#mrit#}¦, {#mritya/ti#} {%zerfallen, sich auflösen%}.
<div n="p">— Mit {#nis#} in {#nirmrEtuka#}.
<div n="p">— Mit {#vi#} {%zerfallen, zerbröckeln%}. {#mruc#} {#mro/cati#} {#gatyarTa#}.
<div n="p">— Mit {#ni#} {%untergehen%} (von der Sonne).
<div n="p">— Mit {#aBini#} {%untergehen über%} (<ab>Acc.</ab>) <ls>MAITR. S. 1,8,7 (125,18. 21)</ls> {#aBinimrukta#} {%derjenige, welchen die untergehende Sonne schlafend findet%} <ls>ĀPAST. 2,12,13. 22</ls>. Häufig fehlerhaft {#aBinirmukta#} geschrieben.
<LEND>

<L>89275<pc>5-113-a<k1>mruc<k2>mruc
√{#mruc#}¦ {#mro/cati#} ({#gatyarTa#}). — Mit {#ni#} untergehen (von der Sonne). — Mit {#aBini#} untergehen über (<ab>Acc.</ab>) <ls>MAITR. S. 1,8,7 (125,18. 21)</ls>. {#aBinirmukta#} derjenige, welchen die untergehende Sonne schlafend findet, <ls>ĀPAST. 2,12,13. 22</ls>. Häufig fehlerhaft {#aBinirmukta#} geschrieben.
<LEND>

NEW:
<L>89274<pc>5-113-a<k1>mrit<k2>mrit
√{#mrit#}¦, {#mritya/ti#} {%zerfallen, sich auflösen%}.
<div n="p">— Mit {#nis#} in {#nirmretuka#}.
<div n="p">— Mit {#vi#} {%zerfallen, zerbröckeln%}.
<LEND>

<L>89275<pc>5-113-a<k1>mruc<k2>mruc
√{#mruc#}¦ {#mro/cati#} ({#gatyarTa#}).
<div n="p">— Mit {#ni#} {%untergehen%} (von der Sonne).
<div n="p">— Mit {#aBini#} {%untergehen über%} (<ab>Acc.</ab>) <ls>MAITR. S. 1,8,7 (125,18. 21)</ls>. {#aBinirmukta#} {%derjenige, welchen die untergehende Sonne schlafend findet,%} <ls>ĀPAST. 2,12,13. 22</ls>. Häufig fehlerhaft {#aBinirmukta#} geschrieben.
<LEND>

Note: This solution slightly different from that of AB in link above.
Note: nirmrEtuka -> nirmretuka.
  cf. arkE upahavO in <L>78905<pc>4-252-b<k1>BaradvAja.
      also an error (not corrected)
-----------------------------------------------------------
temp_pw_7b:  Expand the 'Chr.' references.
Use material from 'issue106/chr' directory. (step3 )

python ../chr/ls_expand_make_change.py 'Chr.' ../chr/chr_expand.txt ../temp_pw_7a.txt ../change_pw_7a_7b.txt

4546 from ../chr/chr_expand.txt
764917 from ../temp_pw_7a.txt
941 lines changed
942 records written to ../change_pw_7a_7b.txt
check: len(a) = 5995
check_instance_strings fails: <ls>Chr. 351. fg.</ls> [this expected]
check_instance_strings finds 1 non-standard strings

# compute temp_pw_7b.txt
cd ../
python updateByLine.py temp_pw_7a.txt change_pw_7a_7b.txt temp_pw_7b.txt
764917 lines read from temp_pw_7a.txt
764917 records written to temp_pw_7b.txt
941 change transactions from change_pw_7a_7b.txt

-----------------------------------------------------------
check that 7b version is compatible with xml, and that
displays are generated.

cd ../
sh redolocal.sh 7b
# ok !

-----------------------------------------------------------
TODO: notes for PW print change(s) to be documented in csl-corrections
---
 <L>63546<pc>4-034-c<k1>parAmarSavAda
 hetuvicAra -> hetutAvicAra    cf. MW
---
<L>124385<pc>7-121-b<k1>sAradIya<k2>sAradIya_nAmamAlA, SAradIyanAmamAlA
   {#nAmamAlA#} -> {#°nAmamAlA#}
---
