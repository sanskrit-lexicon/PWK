
issue83fixa
"SCHL" occurs  only once in pwkvn.txt/

change:

12301 : aBiziYcana : SCHL. : SCHL. 2,107,9 : print change

========================================
pwkvnb "SCHL."

python lsfix2.py pwkvnb temp_pwkvn_1.txt lsfix2_pwkvn_1_b.txt
(True,1),(all,1) lsfix2_pwkvn_1_b.txt

-----------------------------------------------------------
# remake xml from temp_pwkvn_1.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue83fixa
cp temp_pwkvn_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwkvn  ../../pwkvn
sh xmlchk_xampp.sh pwkvn
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue83fixa
-- end of 'remake xml ...'

-------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pwkvn_0.txt temp_pwkvn_1.txt change_pwkvn_1.txt
1 changes written to change_pwkvn_1.txt




