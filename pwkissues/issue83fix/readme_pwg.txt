
issue83fix

========================================
pwga "R. GORR."
"GORR."
python lsfix2.py pwga temp_pwg_0.txt lsfix2_pwg_0_a.txt
(False,1),(None,43),(True,7071),(fixed,4),(all,7119) lsfix2_pwg_0_a.txt

cp temp_pwg_0.txt temp_pwg_1.txt 

Make changes to temp_pwg_1 for the 1 None/

2 parameters -- not reference to verse
16 matches for "<ls>R. GORR. [0-9]+,[0-9]+\.?</ls>"
 3 matches for "<ls n="R. GORR.">[0-9]+,[0-9]+\.?</ls>"

About 160 coded as R. GORR 7,N,N.  These need further work
See pwg_kanda7.txt
</ls> <ls n="R. GORR.">

---------------------------

python lsfix2.py pwga temp_pwg_1.txt lsfix2_pwg_1_a.txt
(None,55),(True,7072),(fixed,5),(all,7132) lsfix2_pwg_1_a.txt
16 matches for "<ls>R. GORR. [0-9]+,[0-9]+\( fg+\)?\.?</ls>"
 2 matches for "<ls>R. GORR. [0-9]+,[0-9]+\(\. fg+\)?\.?</ls>"
 8 matches for "<ls>R. GORR. [0-9]+\( fg+\)?\.?</ls>"
14 matches for "<ls n="R. GORR.">[0-9]+\( fg+\)?\.?</ls>"
 4 matches for "<ls n="R. GORR.">[0-9]+,[0-9]+\(\. fg+\)?\.?</ls>"
 8 matches for "<ls>R. GORR. [IV+].*</ls>"
 3 more
   780981	lamb	<ls n="R. GORR.">7,23,1,18.</ls>	
   972472	saMdarSana	<ls n="R. GORR. 2,">72</ls>	
   977193	saBAjay	<ls n="R. GORR.">7,37,5,61.</ls>	


========================================
pwgb "GORR."

python lsfix2.py pwgb temp_pwg_0.txt lsfix2_pwg_0_b.txt
(False,1),(None,9),(True,12),(True,1694),(all,1716) lsfix2_pwg_0_b.txt

make a few changes to temp_pwg_1.txt

python lsfix2.py pwgb temp_pwg_1.txt lsfix2_pwg_1_b.txt
(None,8),(True,13),(True,1695),(all,1716) lsfix2_pwg_1_b.txt

Here are the 8 None
None	2	291128	tIrTa	<ls>GORR. Bd. VII, S. 341.</ls>	
None	2	351955	DarmADyakza	<ls>GORR. VII,341</ls>	
None	2	411963	padAtyaDyakza	<ls>GORR. VII, S. 341.</ls>	
None	2	434831	pAnIyADyakza	<ls>GORR. VII,341.</ls>	
None	2	614930	antarvESika	<ls>GORR. VII,341.</ls>	
None	2	757337	rasADyakza	<ls>GORR. VII, S. 341.</ls>	
None	2	772041	reRu	<ls>GORR. 4</ls>	
None	2	1050831	skanDa	<ls>GORR. X,303,76.</ls>

=============================
pwgc "R. ed. GORR."

python lsfix2.py pwgc temp_pwg_0.txt lsfix2_pwg_0_c.txt
(None,3),(True,13),(all,16) lsfix2_pwg_0_c.txt

None
837110	vigrahin	<ls>R. ed. GORR. Bd. VII, S. 341.</ls>	
882250	vEKAnasa	<ls>R. ed. GORR. Bd. III, S. 467.</ls>	
973495	saMDin	<ls>R. ed. GORR. Bd. VII, S. 341.</ls>	

No changes required.
=============================

-----------------------------

# generate temp_pwg_2.txt from temp_pwg_1.txt and the 'fixed' elements
# Change the original 2 fixed cases in temp_pwg_1_a.txt
python dict_replace2.py temp_pwg_1.txt lsfix2_pwg_1_a.txt temp_pwg_2.txt

apply_repls: 5 lines changed


-----------------------------------------------------------
# remake xml from temp_pwg_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue83fix
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue83fix
-- end of 'remake xml ...'

---------------------------------------------------

# final analysis with pwga, pwgb, pwgc and temp_pwg_2.txt

python lsfix2.py pwga temp_pwg_2.txt lsfix2_pwg_2_a.txt
(None,55),(True,7087),(all,7142) lsfix2_pwg_2_a.txt


python lsfix2.py pwgb temp_pwg_2.txt lsfix2_pwg_2_b.txt
(None,8),(True,13),(True,1695),(all,1716) lsfix2_pwg_2_b.txt

python lsfix2.py pwgc temp_pwg_2.txt lsfix2_pwg_2_c.txt
(None,3),(True,13),(all,16) lsfix2_pwg_2_c.txt

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
11 changes written to change_pwg_1.txt

python diff_to_changes_dict.py temp_pwg_1.txt temp_pwg_2.txt change_pwg_2.txt
5 changes written to change_pwg_2.txt



