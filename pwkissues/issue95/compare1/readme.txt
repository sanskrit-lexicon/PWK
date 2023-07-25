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

