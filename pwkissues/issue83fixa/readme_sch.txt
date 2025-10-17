
issue83fixa
"SCHL" occurs  only once in sch.txt/

change:

4200 : aBiziYcana: Schl. : Schl. 2,107,9 : print change
========================================
schb "Schl."

python lsfix2.py schb temp_sch_1.txt lsfix2_sch_1_b.txt
(True,1),(all,1) lsfix2_sch_1_b.txt

-----------------------------------------------------------
# remake xml from temp_sch_1.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue83fixa
cp temp_sch_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh sch  ../../sch
sh xmlchk_xampp.sh sch
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue83fixa
-- end of 'remake xml ...'

-------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_sch_0.txt temp_sch_1.txt change_sch_1.txt
1 changes written to change_sch_1.txt




