
issue83fix

========================================
scha "R. Gorr."

python lsfix2.py scha temp_sch_0.txt lsfix2_sch_0_a.txt
(None,1),(True,45),(all,46) lsfix2_sch_0_a.txt

cp temp_sch_0.txt temp_sch_1.txt
Correct the 'None' case.

No changes

python lsfix2.py scha temp_sch_1.txt lsfix2_sch_1_a.txt
(True,46),(all,46) lsfix2_sch_1_a.txt


========================================
schb "Gorr."

python lsfix2.py schb temp_sch_0.txt lsfix2_sch_0_b.txt
(all,0) lsfix2_sch_0_b.txt


No changes
=============================
schc "R. ed. Gorr."

python lsfix2.py schc temp_sch_0.txt lsfix2_sch_0_c.txt

No changes 
=============================
1 change to sch.txt

-----------------------------------------------------------
# remake xml from temp_sch_1.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue83fix
cp temp_sch_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh sch  ../../sch
sh xmlchk_xampp.sh sch
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue83fix
-- end of 'remake xml ...'


-------------------------------------------------
---- documentation in change file
python diff_to_changes_dict.py temp_sch_0.txt temp_sch_1.txt change_sch_1.txt
1 changes written to change_sch_1.txt
