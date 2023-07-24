issue95/compare0/readme.txt

07-24-2023
Examination(s) of pw_CDSL_0.txt

in issue95 directory:
temp_pw_0.txt copied from issue95/pwtranscode/temp_pw_0.txt

temp_pw_ab_0.txt
  pw_CDSL_0.zip
    Ref: https://github.com/sanskrit-lexicon/PWK/issues/95#issuecomment-1646867436
  unzip pw_CDSL_0.zip  # pw_CDSL_0.txt
  mv pw_CDSL_0.txt temp_pw_ab_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw_hwextra.txt temp_pw_hwextra.txt
-----------------------------------
check xml and displays for errors.
# in issue95 directory
sh redo.sh 0
  change to temp_pw_ab_0.txt
55397 old <L>55397  
55397 new

python /c/xampp/htdocs/cologne/xmlvalidate.py dev0/pywork/pw.xml dev0/pywork/pw.dtd
# 'Ok'   So no xml problems!
------------
# number of lines
wc -l temp_pw_*.txt
  682608 temp_pw_0.txt
  674189 temp_pw_ab_0.txt
 (/ (- 682608 674189) 682500.00)  1.2% more lines in pw_ab.
------------
# number of characters
wc -c temp_pw_*.txt
27455953 temp_pw_0.txt
27480314 temp_pw_ab_0.txt
(/ 27480.0 27455.0)  0.1% more characters in pw_ab
------------
headwords
python compare_head
python compare_hw.py ../temp_pw_0.txt ../temp_pw_ab_0.txt compare0_hw.txt
cdsl has 135785 entries
ab   has 135785 entries
0 differences in metalines
---------------------------------------------------------

  
