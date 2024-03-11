pw_6_work
continue alternate headword (k2) work.
03-08-2024 begin

AB's supporting files:

pwkvn_5.differences.txt  (31)  remaining pwkvn portion
pw_5.differences.latest.txt (862)
  8571 matches for "<k2>.*," in buffer: temp_pw_5.txt
  1567 matches for "<L>2.....<pc>.*<k2>.*,"  (the pwkvn portion)
  (- 8571 1567) 7004 main part

  So (/ 862.0 7004.0 ) ~ 12% disagreement betwen Jim and AB.

Jim's objective: evaluate and install the differences, in temp_pw_6.txt
-----------------------------------------------------
01: pwkvn_5.differences.txt  (31)
cp ../temp_pw_5.txt temp_pw_5a.txt
Manually change temp_pw_5a.txt
Notes:
<L>217636<pc>7-344-b<k1>jyot  remove √
<L>214592<pc>7-321-c<k1>irasy add √
<L>220759<pc>7-370-d<k1>ran
 - already marked as √
 - AB not split {#pra, praraRita#} cdsl has split, ab has no split

# Generate standard change file
python ../diff_to_changes_dict.py ../temp_pw_5.txt temp_pw_5a.txt temp_change_5_6_01.txt
33 changes written to temp_change_6_01.txt

touch ../change_5_6.txt
# insert temp_change_5_6_01.txt into ../change_5_6.txt
# recompute temp_pw_6.txt from temp_pw_5a.txt

cd ../
python updateByLine.py temp_pw_5.txt change_5_6.txt temp_pw_6.txt
764912 lines read from temp_pw_5.txt
764912 records written to temp_pw_6.txt
33 change transactions from change_5_6.txt

diff temp_pw_5a.txt ../temp_pw_6.txt | wc -l
# 0
# temp_pw_5a.txt not needed.
rm temp_pw_5a.txt
------------------------------------------------------------------------
02: pw_5.differences.latest.txt (862)
862 matches for "^[0-9]" in buffer: pw_5.differences.latest.txt

639 matches for "(AB): <L" in buffer: pw_5.differences.latest.txt
80 matches for "(AB): <[^L]" in buffer: pw_5.differences.latest.txt
264 matches for "(AB): [^<]" in buffer: pw_5.differences.latest.txt
293 matches for "(AB): .*¦" in buffer: pw_5.differences.latest.txt

python make_change_02.py ../temp_pw_6.txt pw_5.differences.latest.txt temp_change_5_6_02.txt

# manual edit of temp_change_5_6_02.txt
 temporary replace '; <>' with '* ; <L>' and save as Emacs org mode
   change_5_6_02_edit.org
   Major editing

# insert change_5_6_02_edit.org into change_5_6.txt
# remove AB markup in change_5_6.txt
  AB uses notation ⁅kUwapU⁆° in many metaline replacements
  '⁆°' -> ''  (558)
  '⁅' -> ''   (609)
  '⁆' -> ''   (52)
# remove Emacs org-mode markup
  '^* ;' -> ';'  (regex-replace)  (864)

# Recompute temp_pw_6.txt
cd ../
python updateByLine.py temp_pw_5.txt change_5_6.txt temp_pw_6.txt
 Note: this also requires some editing of change_5_6.txt to remove errors.
764912 lines read from temp_pw_5.txt
764912 records written to temp_pw_6.txt
1213 change transactions from change_5_6.txt

 
*****
BEGIN NOTES RE change_5_6_02_edit.org
140548  blank line represents 'delete'
140553  blank line represents 'delete'
<L>2991<pc>1-035-c<k1>aDoakza<k2>aDo_akza/
Why _  in k2?  Remove in k1
   There are various uses by AB.  Keep the '_' to represent space ' ',
Why () in k2?  Remove in k1.  I've kept it in k2, but it seems odd. Remove in k1
why [] in k2?  Remove in k1.  I've kept it in k2, but it seems odd. Remove in k1
  <L>5223<pc>1-062-a<k1>antarantaHsTa<k2>antarantasTa, antaranta[H]sTa
Remove ' in k1
<L>9221<pc>1-107-c<k1>arere<k2>arere, (are_'re)
<L>12946<pc>1-153-b<k1>asTisneha<k2>*asTisneha, *asTisnehasaMjYaka cf. pwg
62945 new {#AGatana#} (!)¦  no other instances of (!)¦
  389 matches for "¦ (!)"
<L>15358<pc>1-181-c<k1>Ayurveda<k2>Ayurveda, AyurvedarasAyana, Ayurvedasarvasva, AyurvedasOKya
  Why does AB drop the last 3?

Here begin many items that Jim thinks are errors in pw_5.differences.latest.txt

<L>16299<pc>1-193-a<k1>Azwaka<k2>*Azwaka, *AzwakIya
---
<L>23050<pc>1-281-b<k1>OrDvadehikakalpavalli  cf. ACC
---
<L>37578<pc>2-194-a<k1>grAham<k2>grAham, *keSezu, *keSErgrAham
  Jim: only grAham is hw
---
<L>39638<pc>2-223-b<k1>cAmaraDAri<k2>cAmaraDAri, cAmaraDAriRI cf. MW
---
<L>42144<pc>2-259-a<k1>jalaraNka<k2>*jalaraNka, *⁅#jala⁆°raNku, *⁅#jala⁆°raYja
  # wrong
---
<L>42819<pc>2-267-c<k1>jinamantraSAstrastotrAdi<k2>jinamantraSAstrastotrAdi
Why not k2 = jinamantra, jinaSAstra jinastotra ?
---
<L>43377<pc>2-276-b<k1>jYAnaprakASikA<k2>jYAnaprakASikA, ⁅jYAna⁆°pradIpa, ⁅jYAna⁆°pradIpikA,   WRONG ⁅jYAna⁆°praboDvamaYjarI
---
<L>44209<pc>3-004-a<k1>tattvadIpa<k2>tattvadIpa, ⁅tattvadIpa⁆°na, ⁅tattva⁆°dipikA, ⁅tattva⁆°dIpinI
  dipikA wrong
---
<L>48106<pc>3-057-c<k1>tryakzara
  {#trayaksarI#}  wrong
---
<L>56185<pc>3-172-c<k1>nakzatrakUrma<k2>nakzatrakUrma, nakzatrakUrmacAra, nakzatrakUrmaviBAga   agrees with mw
---
275903 old <L>56253<pc>3-173-b<k1>naKanizpAvikA<k2>*naKanizpAvikA, *naKanizpAvI
  naKanizpAvI agrees with PW print.
---
<L>58585<pc>3-205-a<k1>niDipA<k2>niDipA/, ⁅niDipA/⁆°pAla
 ⁅niDipA/⁆°pAla wrong
---
<L>59021<pc>3-211-b<k1>nirAtmaka<k2>nirAtmaka, ⁅#nirA⁆°tman, ⁅#nirA⁆°tmavant
  # is typo
---
<L>60351<pc>3-229-b<k1>nistandra<k2>nistandra, ⁅nis⁆°tandri, ⁅nis⁆°tandrī
  tandrī is typo
---
<L>61473<pc>3-245-b<k1>nyAyapariSizwa<k2>nyAyapariSizwa, ⁅nyAyapariSizwa⁆°pariSudDi, ⁅nyAyapariSizwa⁆°prakASa, nyAyapariBAzA, nyAyaprakaraRa, nyAyaprakASa, nyAyaprakASikA, nyAyapraveSa, *tArakaSAstra
 -? ⁅nyAyapariSizwa⁆°pariSudDi  cannot find. mw has nyAyapariSudDi
    but nyAyapariSudDi would be out of alphabetical order.
 - *tArakaSAstra mw has nyAyapraveSatArakaSAstra
---
308603 new <L>62821<pc>4-023-a<k1>padArTakOmudI<k2>padArTakOmudI, padArTaKaRqana, ⁅padArTaKaRqana⁆°wippaRa, ⁅padArTaKaRqana⁆°wIkA, ⁅padArTaKaRqana⁆°vyAKyA, ⁅padArTaKaRqana⁆°SiromaRi, padArTacandrikA, ⁅padArTacandrikA⁆°vilAsa, padArTatatva, ⁅padArTatatva⁆°wIkA, ⁅padArTatatva⁆°nirUpaRa, ⁅padArTatatva⁆°nirRaya, ⁅padArTatatva⁆°vivecana, ⁅padArTatatva⁆°vivecanaprakASa, padArTadIpikA, padArTadIpinI, padArTaDarmasaMgraha, padArTanirUpaRa, padArTapArijAta, padArTaprakASa, padArTaboDa, padArTamaRimAlA, ⁅padArTamaRimAlA⁆°prakASa, padArTamAlA, ⁅padArTamAlA⁆°dIpikA, ⁅padArTamAlA⁆°prakASa, padArTaratnamaYjUzA, ⁅padArTa⁆°ratnamAlA, padArTaviveka, padArTasaMgraha, padArTAdarSa
  tatva -> tattva
---
<L>63194<pc>4-029-c<k1>paratattvanirRaya<k2>paratattvanirRaya, ⁅para⁆°tatvaprakARikA
  tatva -> tattva
---
<L>63546<pc>4-034-c<k1>parAmarSavAda
  could find neither parAmarSavAdahetuvicAra nor parAmarSahetuvicAra.
  parAmarSavAdahetuvicAra in correct alphabetical order.
  MW and acc have parAmarSahetutAvicAra.  PW typo?
---
<L>64256<pc>4-045-a<k1>parivedanIyA<k2>parivedanIyA, *⁅pariv⁆°vedinI
  ⁅pariv⁆ typo
---
<L>65120<pc>4-056-c<k1>pavitrA<k2>pavitrA
  Is this a verb? cf. MW pavitrAtipavitra
---
<L>65285<pc>4-059-b<k1>paSvaizwi<k2>pa/Sva_izwi  hiatus. _ not needed
---
<L>68317<pc>4-102-a<k1>puruzArTapraboDa<k2>puruzArTapraboDa, ⁅puruzA⁆°rTaratnAkara, ⁅puruzA⁆°rTasidByupAya, ⁅puruzA⁆°rTasuDAniDi, ⁅puruzA⁆°rTAnuSAsana
   sidByu -> sidDyu typo
---
<L>68375<pc>4-102-b<k1>puroqAS<k2>puroqA/S, ⁅puro⁆°lAS
 °lAS -> °LAS  ळाश्
---
341575 old {#pfTuzwu#} und {#°zwukA#}¦ <lex>Adj.</lex> <lex>f.</lex> {%einen breiten Zopf habend%}. Nach auch = {#pfTujaGana#}.
341575 new {#pfTuzwu#} <lex>Adj.</lex> und {#°zwukA#} <lex>f.</lex>¦ {%einen breiten Zopf habend%}. Nach auch = {#pfTujaGana#}.
  PRINT CHANGE
---
<L>70123<pc>4-125-b<k1>pOrvadehika<k2>pOrvadehika, ⁅pOrva⁆°dehika
  ⁅pOrva⁆°dehika -> ⁅pOrva⁆°dEhika typo
---
<L>70206<pc>4-126-c<k1>praugya<k2>pra_ugya^
  pra_ugya -> praugya  hiatus, _ not needed in slp1
---
<L>73947<pc>4-181-b<k1>prAGAra<k2>prAg_hAra   _ not needed with slp1
---
<L>77184<pc>4-227-a<k1>bIjavivftti<k2>bIjavivftti, (⁅bIja⁆°vivftti)
   bIjavivftti, (⁅bIja⁆°vivftti) -> bIjavivfti, (⁅bIja⁆°vivftti) typo
---
<L>79451<pc>4-260-b<k1>BAratacampU<k2>BAratacampU, BAratatAtparyanirRaya, ⁅BArata⁆°tAtparyasaMgraha, BAratanirvacana, BAratapadaprakASa, BArataBAvadIpa, BAratamaYjarI, BAravyAKyA, BArataSravaRaviDi, BAratasaMgrahadIpikA, BAratasAvitrI, BAratasUci
  BAravyAKyA -> BAratavyAKyA typo
---
<L>80147<pc>4-271-c<k1>Burizah<k2>Buriza/h, (⁅Buri⁆°za/h)
  (⁅Buri⁆°za/h) -> (⁅Buri⁆°zA/h)  typo
---
397523 new <L>80876<pc>4-283-b<k1>BedaDikkAra<k2>BedaDikkAra, ⁅BedaDikkAra⁆°vyAKyA, ⁅BedaDikkAravyAKyA⁆°prakASa, ⁅BedaDikkAravyAKyA⁆°satkriyA, kArAnyatkArahuMkfti
  kArAnyatkArahuMkfti -> BedaDikkArAnyatkArahuMkfti
  ? ACC has              BedaDikkAranyakkArahuMkfti
---
<L>81825<pc>5-007-b<k1>maRisAra<k2>maRisAra, ⁅maRisAra⁆°KaRqana, ⁅maRisAra⁆°darpaRa, ⁅maRisAra⁆°prAmAeyavAda
  ⁅maRisAra⁆°prAmAeyavAda -> ⁅maRisAra⁆°prAmARyavAda  typo
---
<L>82293<pc>5-014-b<k1>madyAsattaka<k2>madyAsattaka, (⁅madyA⁆°saktraka)
  saktraka -> saktaka  typo
---
<L>82771<pc>5-021-c<k1>manaU<k2>mana_U   '_' not needed in slp1
   probably '_' (or some such) also is not needed in HK
---
<L>83135<pc>5-027-a<k1>mantraratna<k2>mantraratna, ⁅mantra⁆°ratnakoSa, ⁅mantra⁆°ratrAkara, ⁅mantra⁆°ratnvalI, mantrarahasyaprakASikA
  ratrAkara -> ratnAkara, ratnvalI -> ratnAvalI  typos
---
<L>84303<pc>5-043-c<k1>mahAjambu<k2>*mahAjambu, *⁅mahA⁆°jambu
   *⁅mahA⁆°jambu -> *⁅mahA⁆°jambU  still another typo -- odd for AB
---
<L>84372<pc>5-044-b<k1>mahAtripurasundarItApanIyopanizad<k2>mahAtripurasundarItApanIyopanizad, ⁅mahAtripura⁆°sundaryutaratApanI
  'utara' -> uttara
---
<L>84385<pc>5-044-b<k1>mahAdAnapadDati<k2>mahAdAnapadDati, ⁅mahA⁆°dAnAnukamaRikA
  kamaRikA  -> kramaRikA
---
<L>84790<pc>5-049-c<k1>mahAmUzaka<k2>*mahAmUzaka, *⁅mahA⁆°muzika
  muzika -> mUzika
---
<L>84972<pc>5-052-a<k1>mahAvAkyanyAsa<k2>mahAvAkyanyAsa, ⁅mahA⁆°vAkyapaYcIkaraRa, ⁅mahA⁆°vAkyamantropadeSapadDati, ⁅mahA⁆°vAkyamutkAvalI, ⁅mahA⁆°vAkyaratnAvali, ⁅mahA⁆°vAkyarahasya, ⁅mahA⁆°vAkyavicAra, ⁅mahA⁆°vAkyavivaraRa, ⁅mahA⁆°vAkyaviveka, ⁅mahA⁆°vAkyavivekArTasAkzivivaraRa, ⁅mahA⁆°vAkyavyAKyA, ⁅mahA⁆°vAkyasidDAnta, ⁅mahA⁆°vAkyArTa, ⁅mahA⁆°vAkyArTadarpaRa, ⁅mahA⁆°vAkyArTapravoDa, ⁅mahA⁆°vAkyarTavicAra, ⁅mahA⁆°vAkyopanizad
  vAkyArTapravoDa -> vAkyArTapraboDa, vAkyarTavicAra -> vAkyArTavicAra
---
<L>85872<pc>5-064-b<k1>mAtfpUjana<k2>mAtfpUjana, ⁅mAtf⁆°pujA
   pujA -> pUjA
---
<L>86431<pc>5-072-b<k1>mArgaSIrzamAhAtmya<k2>mArgaSIrzamAhAtmya, ⁅mArga⁆°SIrzAdipujA
  pujA -> pUjA
---
<L>86745<pc>5-076-c<k1>mAheSvara<k2>mAheSvara
  Jim thinks <is>Śivait</is> is correct, based on wide-spacing in print.
---
<L>87257<pc>5-084-b<k1>muktivAda<k2>muktivAda, ⁅muktivAda⁆°vicAra, mutkisaptaSatI, mutkisAra
  mutki -> mukti
---
<L>87306<pc>5-085-a<k1>muKamaRqikA<k2>muKamaRqikA, ⁅muKa⁆°maRqanikA
  maRqanikA -> maRqinikA
---
<L>89656<pc>5-118-b<k1>yajYopavItadAna<k2>yajYopavItadAna, yajYopavItapratizWA, ⁅yajYopavItapratizWA⁆°saNcikA
  saNcikA -> saYcikA  (slp1 N = ङ् , Y = ञ् )
---
<L>89792<pc>5-121-b<k1>yaTAkrama<k2>yaTAkrama°, ⁅yaTA⁆°kramam, ⁅yaTA⁆°kramERa
  kramERa -> krameRa
---
<L>89834<pc>5-121-c<k1>yaTAtaTyam<k2>yaTAtaTyam, ⁅yaTA⁆°taTyEna
  taTyEna -> taTyena
---
<L>89909<pc>5-122-c<k1>yaTAprARam<k2>yaTAprARam, ⁅yaTA⁆°prAREna
  prAREna -> prARena
---
<L>90018<pc>5-124-a<k1>yaTAvittAnusAram<k2>yaTAvittAnusAram, ⁅yaTAvittAnu⁆°sArERa
  sArERa -> sAreRa 
---
<L>90025<pc>5-124-a<k1>yaTAviBava<k2>yaTAviBava°, ⁅yaTAvi⁆°Bavatas, (aTAvi°⁅Bavatas⁆), ⁅yaTAvi⁆°Bavam, ⁅yaTAvi⁆°BavamAnEna, ⁅yaTAvi⁆°Bavavistaram, ⁅yaTAvi⁆°BavavistarEs, ⁅yaTAvi⁆°BavavistAram, ⁅yaTAvi⁆°BavasaMBavAt
  yaTAviBavamAnEna -> yaTAviBavamAnena
---
<L>90058<pc>5-124-c<k1>yaTAsaMKyam<k2>yaTAsaMKyam, ⁅yaTA⁆°saMKyEna
  saMKyEna -> saMKyena
---
<L>92044<pc>5-160-a<k1>raNgopajIvin<k2>raNgopajIvin, ⁅aNgopa⁆°jIvya
 aNgopa -> raNgopa  typo
---
new <L>95371<pc>5-211-a<k1>lakzmInfsiMhapaYcaratnamAlikA<k2>lakzmInfsiMhapaYcaratnamAlikA, ⁅lakzmI⁆°nfsiMhamahAzwottara, (lakzmayazwottara), ⁅lakzmI⁆°nfsiMhastavarAja, ⁅lakzmI⁆°nfsiMhastotra
  lakzmayazwottara -> lakzmyazwottara
---
<L>95537<pc>5-213-c<k1>laGuvEyAkaraRaBUzaRa<k2>laGuvEyAkaraRaBUzaRa, ⁅laGu⁆°vEyAkaraRasidDAntamaYjIzA, laGuvyAkaraRaBUzaRasAra
  jIzA -> jUzA
---
<L>95668<pc>5-216-a<k1>latAkastUrikA<k2>latAkastUrikA, *⁅latA⁆°kasturI
  kasturI -> kastUrI
---
<L>97621<pc>6-008-c<k1>vawasAvitrIpUjA<k2>vawasAvitrIpUjA, ⁅vawa⁆°sAvitrIvrata, ⁅vawasAvitrI⁆°vratakAlaRirnaya
  Rirnaya -> nirRaya
---
<L>98431<pc>6-023-a<k1>vararucikArikA<k2>vararucikArikA, ⁅vara⁆°rUciprAkftasUtra, ⁅vara⁆°ruciliNgakArikA, ⁅vara⁆°rucivAkya
  rUci -> ruci
---
<L>99303<pc>6-044-b<k1>vas<k2>6. vas
  vas -> va/s
---
<L>99663<pc>6-048-c<k1>vasyazwi
  vasya_izwi -> vasyaizwi  hiatus. slp1 does not use _
---
<L>103763<pc>6-109-a<k1>vimalaka<k2>vimalaka, ⁅vimalaka⁆°maRi
  vimalakamaRi -> vimalamaRi  cf. pwg, mw
---
<L>110234<pc>6-205-a<k1>SabdaprakASa<k2>SabdaprakASa, ⁅Sabda⁆°prakASikAdvi/pakoSa, SabdapraBeda
  vi/pakoSa -> virUpakoSa
---
<L>110933<pc>6-215-a<k1>SavasauSInara<k2>Savasa_uSInara
  _ not needed in slp1 hiatus.
---
<L>111278<pc>6-219-b<k1>SAktatantra<k2>SAktatantra, SAktiBAzya, SAktAnandataraMgiRI
  SAktiBAzya -> SAktaBAzya
---
<L>111428<pc>6-221-a<k1>SARqilyaSatasUtra<k2>SARqilyaSatasUtra, ⁅SARqilyaSatasUtra⁆°pravacana, ⁅SARqilyaSatasUtra⁆°gazya, ⁅SARqilyaSatasUtra⁆°vyAKyA, ⁅SARqilyaSata⁆°sUtrIBAzya
   gazya -> BAzya
---
<L>112679<pc>6-238-b<k1>SivaliNgadAnaviDi<k2>SivaliNgadAnaviDi, ⁅Siva⁆°liNgaparIkzA, ⁅Siva⁆°liNapratizWAkrama, ⁅Siva⁆°liNgapratizWAprayoga, ⁅Siva⁆°liNgalakzaRa, ⁅Siva⁆°liNgAnandajYAnodaya, ⁅Siva⁆°liNgasUryodaya, SivalIlArRava
  SivaliNa -> SivaliNga
---
<L>112709<pc>6-238-c<k1>SivastavarAja<k2>SivastavarAja, Sivastuti, Sivastotra, ⁅Sivastotra⁆°vyAKyA, SivasTalamahimavarRana, SivasvarUpapUjA, ⁅SivasvarUpapUjA⁆°viDi, ⁅Siva⁆°SvarUpamantra
  SvarUpamantra -> svarUpamantra
---
<L>113514<pc>6-250-a<k1>SuD<k2>SuD, sunD
  sunD -> SunD
---
<L>115120<pc>6-274-a<k1>SrIdAmAnandadAtrI<k2>SrIdAmAnandadAtrI, ⁅SrI⁆°dAmeSvaravallaBa
  vallaBa -> vallaBA
---
<L>116294<pc>6-290-b<k1>zaqvidyAgama<k2>zaqvidyAgama, ⁅zaqvidyAgama⁆°zAMKyAyanatantra
  zAMKyAyanatantra -> sAMKyAyanatantra
---
<L>116438<pc>6-292-a<k1>zoqaSakAraRajayamAlA<k2>zoqaSakAraRajayamAlA, ⁅oqaSa⁆°kAraRapUjA, zoqaSakArikA, zoqaSakUrca, zoqaSagaRapatiDyAna, ⁅oqaSa⁆°gaRapatilakzaRa
 ⁅oqaSa⁆ -> ⁅zoqaSa⁆
---
<L>117618<pc>7-019-b<k1>saMgItakOmudI<k2>saMgItakOmudI, saMgItacUqAmaRI, saMgItadarpaRa, saMgItadAmodara, saMgInArAyaRa, saMgItamakaranda, saMgIttamuktAvalI, saMgItaratnamAlA, saMgItaratnAkara, ⁅saMgItaratnAkara⁆°kalAniDi, ⁅saMgItaratnAkara⁆°candrikA, ⁅saMgItaratnAkara⁆°wIkA, ⁅saMgIta⁆°rAGava
  saMgInArAyaRa -> saMgItanArAyaRa print change
  saMgIttamuktAvalI -> saMgItamuktAvalI typo
---
<L>117644<pc>7-020-a<k1>saMgrahaRIratna<k2>saMgrahaRIratna, saMgrahaprakASikA, saMgraharAmAyaRa, ⁅saMgraharAmAyaRa⁆°vivaraRa
  ⁅saMgraharAmAyaRa⁆°vivaraRa -> saMgrahavivaraRa (cf. MW)
---
<L>118222<pc>7-029-c<k1>satyajYAnAnandatIrTa<k2>satyajYAnAnandatIrTa, ⁅satyajYAnAnanda⁆°yati
  satyajYAnAnandayati -> satyajYAnAnandatIrTayati cf. MW
---
<L>119433<pc>7-048-b<k1>saptadina<k2>saptadina°, saptAdivasa°
  saptAdivasa -> saptadivasa
---
<L>124169<pc>7-118-a<k1>sAmAnyABAvagranTa<k2>sAmAnyABAvagranTa, ⁅#sAmAnyA⁆°BAvawippanI, ⁅#sAmAnyA⁆°BAvarahasya
  #sAmAnyA -> sAmAnyA 
---
<L>124654<pc>7-124-c<k1>sAvairisole<k2>sAva_irisole
  sAva_irisole -> sAvairisole  slp1 does not need _ for hiatus
  Note: mw:   sAvaisirole  MW print change?
---
<L>124811<pc>7-126-c<k1>sAhityakaRwakodDAra<k2>sAhityakaRwakodDAra, sAhityaka/mudI, sAhityacintAmaRi, sAhityacUqAmaRI, sAhityadarpaRa, sAhityamImAMsA, sAhityaratnamAlA, sAhityaratnAkara, sAhityasaraRivyAKyA, sAhityasarvasva, sAhityasAra, sAhityasUci
  sAhityaka/mudI -> sAhityakOmudI
---
<L>125248<pc>7-132-c<k1>sidDAntakalpataru<k2>sidDAntakalpataru, ⁅sidDAnta⁆°kalpalatA, ⁅sidDAnta⁆°kalpavallI, sidDAntakOmudrI, sidDAntagarBa, sidDAntagItA, sidDAntagranTa, sidDAntacandrikA, ⁅sidDAntacandrikA⁆°KaRqana, ⁅sidDAnta⁆°candrodaya, sidDAntacintAmaRi, sidDAntacUqAmaRi, sidDAntatattva, ⁅sidDAntatattva⁆°prakASikA, ⁅sidDAntatattva⁆°bindu, ⁅sidDAntatattva⁆°bindusaMdIpana, ⁅sidDAntatattva⁆°viveka, ⁅sidDAntatattva⁆°sarvasva, sidDAntadIpa, ⁅sidDAnta⁆°dIpikA
  sidDAntakOmudrI -> sidDAntakOmudI
---
<L>125254<pc>7-132-c<k1>sidDAntaratna<k2>sidDAntaratna, ⁅sidDAnta⁆°ratnAvali, ⁅sidDAnta⁆°ratnAvalI, sidDAntarahasya, sidDAntlakzaRa, ⁅sidDAntlakzaRa⁆°jAgadISI, ⁅sidDAnta⁆°lakzaRAkroqa, sidDAntalakzaRI, sidDAntalaGuKamARika, sidDAntaleSa, ⁅sidDAntaleSa⁆°saMgraha
  sidDAntlakzaRa -> sidDAntalakzaRa,
  sidDAntlakzaRajAgadISI -> sidDAntalakzaRajAgadISI
---
<L>125256<pc>7-132-c<k1>sidDAntavicAragATA<k2>sidDAntavicAragATA, sidDAntavelA, sidDAntavEjayantI, sidDAntavyAKyA, sidDAntavyutpattilakzaRa, sidDAntaSikzA, sidDAntaSiKAmaRi, sidDAntaSiromaRi, ⁅sidDAntaSiromaRi⁆°prakASa, sidDAntaSeKara, sidDAntasaMhitAsArasamuccaya, sidDAntasaMgraha, sidDAntasaMdarBa, sidDAntasAra, ⁅sidDAntasAra⁆°dipikA, ⁅sidDAntasAra⁆°kOstuBa, ⁅sidDAnta⁆°sArAvali, ⁅sidDAnta⁆°sArAvalI, sidDAntasArvaBOma, sidDAntasidDAjYana, sidDAntasundara, sidDAntasUktamaYjarI, sidDAntasvAnuBUtiprakASikA
  dipikA -> dIpikA
---
<L>126304<pc>7-147-a<k1>sudarSanakavaca<k2>sudarSanakavaca, sudarSanapaYjaropanizad, sudarSanapAYjanyapratizWA, sudarSanaBAzya, sudarSanamImA/sA, sudarSanavijaya, sudarSanaSataka, ⁅sudarSanaSataka⁆°wIkA, ⁅sudarSanaSataka⁆°vyAKyA, sudarSanasaMhitA, sudarSanasaMpAta, sudarSanAyantraviDi, sudarSanarADanakrama, sudarSanAzwaka
  sudarSanamImA/sA -> sudarSanamImAMsA
---
<L>128724<pc>7-177-c<k1>sUtimAs<k2>sUtimAs, ⁅sUtimA⁆°sAma
  ⁅sUtimA⁆°sAma -> ⁅sUtimA⁆°mAsa  cf. mw
---
<L>129327<pc>7-185-c<k1>sehuRqa<k2>sehuRqa, A
  A -> sehuRqA
---
<L>129624<pc>7-189-b<k1>somamad<k2>somama/d, (⁅soma⁆°mAd)
  ⁅soma⁆°mAd -> ⁅soma⁆°mA/d
---
<L>133798<pc>7-260-c<k1>hariBakti<k2>hariBakti
 hariBakti, hariBaktilatikAstava, hariBaktivilAsa, hariBaktisuDodaya  cf. ACC
---
<L>133869<pc>7-261-c<k1>hariSarman<k2>hariSarman, ⁅hari⁆°SarmIrya, hariSiKa
  ⁅hari⁆°SarmIrya -> ⁅hari⁆°SarmArya
---
<L>135204<pc>7-281-a<k1>hfdGawana<k2>hfdGawana, (hfdGawwana)
  hfdDawwana -> hfdGawwana
---
END NOTES RE change_5_6_02_edit.org


------------------------------------------------------------------------
TODO: print changes to note in csl-corrections for pw_printchange.txt
---
print change
old: <L>85520<pc>5-058-b<k1>mahOzaDi<k2>mahOzaDi, ⁅mahOza⁆°zI
new: <L>85520<pc>5-058-b<k1>mahOzaDi<k2>mahOzaDi, ⁅mahOza⁆°DI
---
print change
534720 old {#vEdyanATadIkzitIya#} <lex>n.</lex> und {#°nATaBew#}¦ Titel von Werken <ls>OPP. CAT. 1</ls>.
534720 new {#vEdyanATadIkzitIya#} <lex>n.</lex> und {#°nATaBEw#}¦ Titel von Werken <ls>OPP. CAT. 1</ls>. ;; print error (cf. ACC entry)  also PWG
---
print change
<L>117618<pc>7-019-b<k1>saMgItakOmudI
  saMgInArAyaRa -> saMgItanArAyaRa print change
---
print change?
<L>124385<pc>7-121-b<k1>sAradIya
 {#nAmamAlA#} -> {#°nAmamAlA#} ?
 Note: SAradIyanAmamAlA in ACC
------------------------------------------------------------------------
OLD NOTES from pw_5_work -- to be deleted
------------------------------------------------------------------------
temp_pw_6.txt
Constructed from ../temp_pw_5a.txt in 3 steps.

-- 01
cp ../temp_pw_5a.txt  ../temp_pw_5a1.txt
manual edit of temp_pw_5a1.txt.
Apply Changes per pwkvn_4.differences-1.metalines.and.header.lines.txt  (22)

# construct change file
python ../diff_to_changes_dict.py ../temp_pw_5a.txt  ../temp_pw_5a1.txt temp_change_4_5_01.txt

touch ../change_5a_6.txt
# manual insert temp_change_4_5_01.txt into change_5a_6.txt

# recompute temp_pw_6.txt from temp_pw_5a.txt
cd ../
python updateByLine.py temp_pw_5a.txt change_5a_6.txt temp_pw_6.txt
34 change transactions from change_5a_6.txt

-- 02
 Changes per pwkvn_4.differences-2.dhAtu.and.denominative.verbs.txt

# this is complicated for various reasons.
# the 'temp_unused_groups_02.txt have (about 30) have to be done manually
python make_change_01.py ../temp_pw_6.txt pwkvn_4.differences-2.dhAtu.and.denominative.verbs.txt temp_change_4_5_02.txt 
764912 from ../temp_pw_6.txt
372 from pwkvn_4.differences-2.dhAtu.and.denominative.verbs.txt
102 records written to temp_change_4_5_02.txt

# manual edit of temp_change_4_5_02.txt
 compare with pwkvn_4.differences-2
 a) remove a few in temp_change_4_5_02.txt
 b) accept 5 more ('i' see below)
# manual insert temp_change_4_5_02.txt into change_5a_6.txt

# recompute temp_pw_6.txt from temp_pw_5a.txt
cd ../
python updateByLine.py temp_pw_5a.txt change_5a_6.txt temp_pw_6.txt
132 change transactions from change_5a_6.txt

AB missed these
<L>204132<pc>3-256-b<k1>i<k2>3. i ?
<L>205418<pc>4-296-b<k1>i<k2>3. i ?
<L>206831<pc>5-249-c<k1>i<k2>3. i ?
<L>208655<pc>6-298-b<k1>i<k2>3. i  ?
<L>214506<pc>7-320-d<k1>i<k2>3. i  ?

-- 03
 Changes per pwkvn_4.differences-3.splits.and.miscellaneous.txt

# this is complicated for various reasons.
# the 'temp_unused_groups_02.txt have (about 30) have to be done manually
python make_change_03.py ../temp_pw_6.txt pwkvn_4.differences-3.splits.and.miscellaneous.txt temp_change_4_5_03.txt 
nit_ab_changes: 75 groups found
76 records written to temp_change_4_5_03.txt

# manual edit of temp_change_4_5_03.txt
 compare with pwkvn_4.differences-3
 many manual changes required due to <div n="p"/>
# manual insert temp_change_4_5_03.txt into change_5a_6.txt

# recompute temp_pw_6.txt from temp_pw_5a.txt
cd ../
python updateByLine.py temp_pw_5a.txt change_5a_6.txt temp_pw_6.txt
218 change transactions from change_5a_6.txt

Note: <L>222590<pc>7-389-d<k1>riktI
  Question !√{#riktI#}.  cf. <L>94190<pc>5-189-b<k1>riktI

