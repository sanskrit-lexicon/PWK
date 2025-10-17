
issue83fixa

========================================
pwa "R. SCHL."

python lsfix2.py pwa temp_pw_0.txt lsfix2_pw_0_a.txt
(True,1),(all,1) lsfix2_pw_0_a.txt

No changes

========================================
pwb "SCHL."

python lsfix2.py pwb temp_pw_0.txt lsfix2_pw_0_b.txt
(all,0) lsfix2_pw_0_b.txt

cp temp_pw_0.txt temp_pw_1.txt
One additional change

212301 : aBiziYcana : SCHL. : SCHL. 2,107,9 : print change

python lsfix2.py pwb temp_pw_1.txt lsfix2_pw_1_b.txt
(True,1),(all,1) lsfix2_pw_1_b.txt
=============================
pwc "R. ed. SCHL."

python lsfix2.py pwc temp_pw_0.txt lsfix2_pw_0_c.txt
(None,1),(all,1) lsfix2_pw_0_c.txt

None:
27998   aBiruta <ls>R. ed. SCHL. 17</ls>

Correct the None

-----------------------------

python lsfix2.py pwc temp_pw_1.txt lsfix2_pw_1_c.txt
(True,1),(all,1) lsfix2_pw_1_c.txt


=============================


# generate temp_pw_2.txt from temp_pw_1.txt and the 'fixed' elements
# Change the original 2 fixed cases in temp_pw_1_a.txt
# nothing to generate. The 1 fixed was changed manually
# python dict_replace2.py temp_pw_1.txt lsfix2_pw_1_a.txt temp_pw_2.txt

-----------------------------------------------------------
# remake xml from temp_pw_1.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue83fixa
cp temp_pw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pw  ../../pw
sh xmlchk_xampp.sh pw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue83fixa
-- end of 'remake xml ...'

-------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pw_0.txt temp_pw_1.txt change_pw_1.txt
2 changes written to change_pw_1.txt




