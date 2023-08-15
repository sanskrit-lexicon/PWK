issue95/compare1/readme.txt

07-24-2023
Examination(s) of pw_AB_1txt

../temp_pw_0.txt copied from issue95/pwtranscode/temp_pw_0.txt

temp_pw_ab_1.txt
  pw.AB.v1.zip
    Ref: https://github.com/sanskrit-lexicon/PWK/issues/95#issuecomment-1648404419
  unzip pw_AB.v1.zip  # 'pw (AB v1).txt'
  mv 'pw (AB v1).txt' ../temp_pw_ab_1.txt

Som
-----------------------------------
check xml and displays for errors.
# in issue95 directory
sh redo.sh 1
  change to temp_pw_ab_1.txt
55397 old <L>55397  
55397 new


cp ../temp_pw_ab_1.txt ../temp_pw_ab_1_orig.txt  # save original version
manually edit ../temp_pw_ab_1.txt and correct for xml.
python ../diff_to_changes_dict.py ../temp_pw_ab_1_orig.txt ../temp_pw_ab_1.txt change_ab_1.txt
12 changes written to change_ab_1.txt

Now dev1/pywork/pw.xml is well-formed xml.

Check for validity re pw.dtd
cd ../
python /c/xampp/htdocs/cologne/xmlvalidate.py dev1/pywork/pw.xml dev1/pywork/pw.dtd
-------------------
changes to one.dtd
<is n="1">Prākrit</is>
<zoo> tag:  should use bio
<iw> tag:  ?
n attribute of bot
<lang n="???">X</lang>    DTD attlist cannot be ???.
 Change to "unknown" and modify one.dtd

------------
# number of lines
 wc -l temp_pw_ab*.txt
  674189 temp_pw_ab_0.txt
  674189 temp_pw_ab_1.txt
 SAME 
------------
# number of characters
wc -c temp_pw_ab*.txt
27480314 temp_pw_ab_0.txt
27967926 temp_pw_ab_1.txt
(/ 2797.0 2748.0) 1.8% more characters in ab_1
------------
headwords

python compare_hw.py ../temp_pw_ab_0.txt ../temp_pw_ab_1.txt compare_ab_0_1.txt
ab0 has 135785 entries
ab1 has 135771 entries

ab1 has 14 fewer metalines than ab0!.
---------------------------------------------------------
07-25-2023
take into account 4 AB comments ending at
  https://github.com/sanskrit-lexicon/PWK/issues/95#issuecomment-1649160875
 

Revise temp_pw_ab_1.txt,
python ../diff_to_changes_dict.py ../temp_pw_ab_1_orig.txt ../temp_pw_ab_1.txt change_ab_1.txt
10 changes written to change_ab_1.txt

remake dev1
cd ../
sh redo.sh 1
python /c/xampp/htdocs/cologne/xmlvalidate.py dev1/pywork/pw.xml dev1/pywork/pw.dtd
-------------------------------------------------------
compare_hw  step 2
python compare_hw.py ../temp_pw_ab_0.txt ../temp_pw_ab_1.txt compare_ab_0_1.txt

ab0 has 135785 entries
ab1 has 135771 entries
135761 metalines are identical
24 metalines are in ab0 only
10 metalines are in ab1 only

ab1 errors ?  (based on differences between metalines in ab0, ab1 versions.

only ab0: <L>13353<pc>1158-1<k1>Akarika<k2>Akarika<e>100
only ab1: <L>13353<pc>1158-1<k1>AkAraka<k2>AkAraka<e>100
   ab1 error?  cf pwg, alphabetical order  (Note: 'pw print error')
   yes. AB agrees
   
only ab0: <L>19684<pc>1240-3<k1>upanikzepa<k2>upanikzepa<e>100
only ab1: <L>19684<pc>1240-3<k1>upanikzepa<k2>upanikzepa<e>100ṇ
   ab1 error? ṇ
   yes: AB agrees
   
only ab0: <L>78979<pc>4253-2<k1>Barb<k2>°Barb<e>500
only ab1: <L>78979<pc>4253-2<k1>Barb<k2>*Barb<e>500
      ab1 error?  
      No. AB disagrees. Ref: https://github.com/sanskrit-lexicon/PWK/issues/95#issuecomment-1650835794
      
only ab0: <L>120161<pc>7058-2<k1>samaha<k2>samaha.<e>100
only ab1: <L>120161<pc>7058-2<k1>samaha<k2>sa\ma\ha\<e>100
     ab1 correction.
     additionally, ab1 error?: (add comma) {#praSasta#}, {#saDana#}
     yes: AB agrees.
---------------------
 The rest are ab0 errors corrected in ab1
only ab0: <L>2585<pc>1030-3<k1>adyAraBya<k2>adyAraBya<e>100 merged into 2584-adya
only ab0: <L>5654<pc>1067-1<k1>anyadAsTita<k2>*anyadAsTita<e>100 merged into 5653-anyadASA

   
only ab0: <L>13614<pc>1161-1<k1>matsya<k2>*°matsya<e>108 merged into 13613-Agatanandin

only ab0: <L>15675<pc>1185-2<k1>ArDadroRika<k2>*ArDadroRika<e>100 merged into 15674-ArDakaMsika

   
only ab0: <L>22636<pc>1276-3<k1>ojasvant<k2>o/jasvant<e>100 merged into 22635-ojasya
only ab0: <L>22840<pc>1279-1<k1>Odanyi<k2>*Odanyi<e>100 merged into 22839-OdanyAyani
only ab0: <L>27164<pc>2057-1<k1>dIpikA<k2>°dIpikA<e>100 merged ionto 27163-kAlanirRaya

only ab0: <L>35708<pc>2169-2<k1>guRadiDitiwippaRI<k2>guRadiDitiwippaRI<e>100
only ab1: <L>35708<pc>2169-2<k1>guRadIDitiwippaRI<k2>guRadIDitiwippaRI<e>100
  ab1 corrects error in ab0
  
only ab0: <L>42554<pc>2264-1<k1>tika<k2>*°tika<e>100 merged into 42553-jAnuprahUta

only ab0: <L>44029<pc>2284-3<k1>ta<k2>ta/<h>1<e>500
only ab1: <L>44029<pc>3001-1<k1>ta<k2>ta/<h>1<e>500
       ab1 corrections pc
       
only ab0: <L>61551<pc>3246-2<k1>pa<k2>pa<h>1<e>500
only ab1: <L>61551<pc>4001-1<k1>pa<k2>pa<h>1<e>500
       ab1 corrects pc
       
only ab0: <L>61775<pc>4004-2<k1>pacaMbacA<k2>*pacaMbacA<e>100 merged into 61774-pacaMpacA
only ab0: <L>68374<pc>4102-2<k1>pattraJaMkAra<k2>pattraJaMkAra<e>000 merged into 68373-purowi
only ab0: <L>78596<pc>4247-3<k1>BawwasvAmin<k2>BawwasvAmin<e>100 merged into 78595-BawwaviSveSvara

      
only ab0: <L>80064<pc>4270-3<k1>BujagASana<k2>*BujagASana<e>100 merged into 80063-BujagAntaka

only ab0: <L>83062<pc>5025-3<k1>mantUya<k2>*mantUya<e>500
only ab1: <L>83062<pc>5025-3<k1>mantUy<k2>*mantUy<e>500
     ab1 correction
     
only ab0: <L>99939<pc>6054-2<k1>nirveda<k2>nirveda<e>100 merged into 99938-vAgya

only ab0: <L>106581<pc>6151-1<k1>vfdDasuSuta<k2>vfdDasuSuta<e>100
only ab1: <L>106581<pc>6151-1<k1>vfdDasuSruta<k2>vfdDasuSruta<e>100
     ab1 correction
     
only ab0: <L>117791<pc>7022-1<k1>saccaritrasuDAniDi<k2>saccaritrasuDAniDi<e>100 merged into 117790-saccaritraparitrARa

    
only ab0: <L>129746<pc>7190-3<k1>somAmbuya<k2>somAmbuya<e>100
only ab1: <L>129746<pc>7190-3<k1>somAmbupa<k2>somAmbupa<e>100
     ab1 correction
     
RERUN
python ../diff_to_changes_dict.py ../temp_pw_ab_1_orig.txt ../temp_pw_ab_1.txt change_ab_1.txt
15 changes written to change_ab_1.txt
----------------------------------------------------------------------
