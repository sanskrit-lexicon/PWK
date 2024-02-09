pwkissues/issue105/readme.txt
https://github.com/sanskrit-lexicon/PWK/issues/105
Begin 02-00-2024


Remove <e>N from pw metalines 

local directory of this readme
cd /c/xampp/htdocs/sanskrit-lexicon/pwk/pwkissues/issue105

----------------------------------------------------------
initialize temp_pw_0.txt from csl-origing at commit on date 02-09-2024
 commit 04d06196fd868a23748401168f848e14aa226601
cd /c/xampp/htdocs/cologne/csl-orig/v02/pw
git show 04d06196:v02/pw/pw.txt > temp_pw_0.txt
mv temp_pw_0.txt /c/xampp/htdocs/sanskrit-lexicon/pwk/pwkissues/issue105/
cd /c/xampp/htdocs/sanskrit-lexicon/pwk/pwkissues/issue105

----------------------------------------------------------
Save a copy of the metalines of pw that have <e>
grep -E '<e>' temp_pw_0.txt > pw_e_metalines.txt

wc -l pw_e_metalines.txt
# 135764 pw_e_metalines.txt

----------------------------------------------------------
temp_pw_1.txt : remove <e>N
python remove_e.py temp_pw_0.txt temp_pw_1.txt
764479 lines read from temp_pw_0.txt
764479 lines written to temp_pw_1.txt

Note: In <e>N,  the code N is of form ddd  (3 digits)
--------
# test displays for pwk
 
cp temp_pw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pw  ../../pw
sh xmlchk_xampp.sh pw
# ok  


-------------------------------------------------------
install temp_pw_1 into csl-orig.
---
First, locally.
cd /c/xampp/htdocs/sanskrit-lexicon/pwk/pwkissues/issue105
cp temp_pw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt

--- pull csl-orig, to get latest repository
cd /c/xampp/htdocs/cologne/csl-orig/v02/
git pull # in cas

cd /c/xampp/htdocs/sanskrit-lexicon/pwk/pwkissues/issue105
cp temp_pw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt

# sync to github
cd /c/xampp/htdocs/cologne/csl-orig/v02/
git pull #
git add .
git commit -m "PW: remove <e>N codes from metaline.
Ref: https://github.com/sanskrit-lexicon/PWK/issues/105"
git push


---------------------
sync cologne from github for csl-orig repository
--- regenerate displays at Cologne
# login to cologne server
cd csl-pywork/v02, etc.
---------------------
Sync this repo to github
cd /c/xampp/htdocs/sanskrit-lexicon/pwk/pwkissues/issue105
git add .
git commit -m "PW: remove <e>N codes from metaline.
Ref: https://github.com/sanskrit-lexicon/PWK/issues/105"
---------------------

Done with this issue.
