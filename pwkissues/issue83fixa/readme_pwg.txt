
issue83fixa

========================================
pwga "R. SCHL."

python lsfix2.py pwga temp_pwg_0.txt lsfix2_pwg_0_a.txt
(None,12),(True,238),(fixed,1),(all,251) lsfix2_pwg_0_a.txt

cp temp_pwg_0.txt temp_pwg_1.txt 

Make changes to temp_pwg_1 for the 12 None/

Check SCHL refs for kanda = 1 or 2 (~5 exceptions recoded to GORR)

---------------------------

python lsfix2.py pwga temp_pwg_1.txt lsfix2_pwg_1_a.txt
(True,245),(all,245) lsfix2_pwg_1_a.txt

========================================
pwgb "SCHL."

python lsfix2.py pwgb temp_pwg_0.txt lsfix2_pwg_0_b.txt
(None,1),(True,1),(True,125),(all,127) lsfix2_pwg_0_b.txt

python lsfix2.py pwgb temp_pwg_1.txt lsfix2_pwg_1_b.txt
(True,1),(True,121),(all,122) lsfix2_pwg_1_b.txt

=============================
pwgc "R. ed. SCHL."

python lsfix2.py pwgc temp_pwg_0.txt lsfix2_pwg_0_c.txt
(None,1),(True,1),(True,2),(all,4) lsfix2_pwg_0_c.txt

python lsfix2.py pwgc temp_pwg_1.txt lsfix2_pwg_1_c.txt
(None,2),(True,1),(True,5),(all,8) lsfix2_pwg_1_c.txt

None: 
svAgata	<ls>R. ed. SCHL. II,147, Z. 3</ls>	
 kataka <ls>R. ed. SCHL. I, XXXI.</ls>   (kataka is name of commentary)


=============================

-----------------------------

# generate temp_pwg_2.txt from temp_pwg_1.txt and the 'fixed' elements
# Change the original 2 fixed cases in temp_pwg_1_a.txt
# nothing to generate. The 1 fixed was changed manually
# python dict_replace2.py temp_pwg_1.txt lsfix2_pwg_1_a.txt temp_pwg_2.txt

-----------------------------------------------------------
# remake xml from temp_pwg_1.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue83fixa
cp temp_pwg_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue83fixa
-- end of 'remake xml ...'

---------------------------------------------------

# final analysis with pwga, pwgb, pwgc and temp_pwg_2.txt

python lsfix2.py pwga temp_pwg_2.txt lsfix2_pwg_2_a.txt


python lsfix2.py pwgb temp_pwg_2.txt lsfix2_pwg_2_b.txt

python lsfix2.py pwgc temp_pwg_2.txt lsfix2_pwg_2_c.txt

temp_pwg_2
pwga True  7087
pwgb True  1708
pwgc True    13
           8808 total
temp_pwg_0
pwga True  7071
pwgb True  1706
pwgc True    13
           8790  Total

18 additional links added

-------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
26 changes written to change_pwg_1.txt



