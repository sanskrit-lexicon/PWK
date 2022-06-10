Gorresio links to Ramayana in pwk.


****************************************************************
Begin the work leading to temp_pw_05.txt
****************************************************************

See https://github.com/sanskrit-lexicon/PWK/issues/90.


temp_pw_0.txt copy of
   /c/xampp/htdocs/cologne/csl-orig/v02/pw at commit
   2cf2608d2b5e3a5b5d6624982e65960cfef36c33
cd /c/xampp/htdocs/cologne/csl-orig/v02/pw
git show 2cf2608d2b5:v02/pw/pw.txt > /c/xampp/htdocs/sanskrit-lexicon/pwk/pw_ls/gorr/temp_pw_0.txt
cd /c/xampp/htdocs/sanskrit-lexicon/pwk/pw_ls/gorr/
----------------------------------
cp temp_pw_0.txt temp_pw_1.txt
# temp_pw_1.txt manual changes to GORR ls markup

NOTES:
1. aBiruta  Reference appears to be R. ed. GORR. 6,70,19
 but https://sanskrit-lexicon-scans.github.io/ramayanagorr/?6,70,19 shows
 no mention of aBiruta
2. {#varzArAtra#}¦ (<ls>R. 4,26,24.</ls> <ls n="R.">7,64,10</ls>)
  varzArAtra is in 4,26,24 of R. Gorr.,  but not in 7,64,10.

python diff_to_changes.py temp_pw_0.txt temp_pw_1.txt change_1.txt
12 changes written to change_1.txt

----------------------------------
18 matches for "<ls>R\. [0-9]+,[0-9]+,[0-9]\.[^<]" in buffer: temp_pw_1.txt
cp temp_pw_1.txt temp_pw_2.txt
# temp_pw_2.txt manual changes to R. ls markup

; --------------------------------------------------------------
# Installation of temp_pw_2.txt 
cp temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
# Then in local csl-pywork/v02:
cd /c/xampp/htdocs/cologne/csl-pywork/v02

sh generate_dict.sh pw  ../../pw

sh xmlchk_xampp.sh pw
# ok
cd /c/xampp/htdocs/cologne/csl-orig/v02
# push
cd /c/xampp/htdocs/sanskrit-lexicon/pwk/pw_ls/gorr/

; --------------------------------------------------------------
