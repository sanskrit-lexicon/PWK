pwkissues/issue104/readme.txt
https://github.com/sanskrit-lexicon/PWK/issues/104
Begin 02-08-2024

Merge pwkvn.txt into pw.txt.
Remove <e>N from pw metalines 
Modify k2 for alternate headwords

local directory of this readme
cd /c/xampp/htdocs/sanskrit-lexicon/pwk/pwkissues/issue104
----------------------------------------------------------
initialize temp_pw_0.txt from csl-origing at commit on date 02-08-2024
 commit 4494759f16eb74534a52c2509f13377a6842c701 
cd /c/xampp/htdocs/cologne/csl-orig/v02/pw
git show 4494759:v02/pw/pw.txt > temp_pw_0.txt
mv temp_pw_0.txt /c/xampp/htdocs/sanskrit-lexicon/pwk/pwkissues/issue104/

---
initialize temp_pwkvn_0.txt from csl-origing at commit on date 02-08-2024
 commit 4494759f16eb74534a52c2509f13377a6842c701 
cd /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn
git show 4494759:v02/pwkvn/pwkvn.txt > temp_pwkvn_0.txt
mv temp_pwkvn_0.txt /c/xampp/htdocs/sanskrit-lexicon/pwk/pwkissues/issue104/

----------------------------------------------------------
temp_pw_1.txt : initial merger 
mkdir merge: 
# consult merge/readme.txt
1. pwkvn_Lnew = 200000 + pwkvn_Lold
2. <info n="sup_v"/> appended to the text of pwkvn entries
  v = 1-7 the volume, per 'pc'
  For easy identification to generate display message

revise /c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php
  From <info n="sup_1"/> display [supplement volume 1]
--------
test displays for pwkvn
# 
cp ../temp_pw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pw  ../../pw
# revert csl-orig - pw.txt
cd /c/xampp/htdocs/cologne/csl-orig/v02/
git restore pw.txt
# back home
cd /c/xampp/htdocs/sanskrit-lexicon/pwk/pwkissues/issue104


-------------------------------------------------------
go ahead and install temp_pw_1 into csl-orig.
---
First, locally.
--- pull csl-orig, to get latest repository
cd /c/xampp/htdocs/cologne/csl-orig/v02/
git pull # in cas

cd /c/xampp/htdocs/sanskrit-lexicon/pwk/pwkissues/issue104
cp temp_pw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt

# sync to github
git add .
git commit -m "Append PWKVN to PW.
Ref: https://github.com/sanskrit-lexicon/PWK/issues/104"
git push
--- sync csl-websanlexicon to github
 cd /c/xampp/htdocs/cologne/csl-websanlexicon/

git pull
git status
# modified:   v02/makotemplates/web/webtc/basicadjust.php
git add .
git commit -m "pwk display for '<info n="sup_N"/>'.
Ref: https://github.com/sanskrit-lexicon/PWK/issues/104"
git push
---------------------
NOTE: we now have more headwords in PW,
so will need to revise hwnorm1 and then csl-apidev.
However,  we will al
# pw.txt now has all the headwords of pwk
cd /c/xampp/htdocs/cologne/hwnorm1/sanhw1
sh redo.sh
# example difference in hwnorm1c.txt
-aMSagrAhin:aMSagrAhin:PD,PWKVN,SCH
+aMSagrAhin:aMSagrAhin:PD,PW,PWKVN,SCH
-- move to csl-apidev
mv hwnorm1c.sqlite ../../csl-apidev/simple-search/hwnorm1/
# sync hwnorm1 to github
git add .
git commit -m "Append pwkvn to pk.
Ref: https://github.com/sanskrit-lexicon/PWK/issues/104"
git push

--- revise csl-apidev for basic adjust and hwnorm1c.sqlite
cd /c/xampp/htdocs/cologne/csl-websanlexicon/v02
# copy basicadjust.php and basicdisplay.php to local csl-apidev repo
sh apidev_copy.sh
--- sync csl-apidev repo to github

cd /c/xampp/htdocs/cologne/csl-apidev
git add .
git commit -m "Append pwkvn to pk.
Ref: https://github.com/sanskrit-lexicon/PWK/issues/104"
git push


---------------------
sync cologne from github
 for csl-orig, csl-websanlexicon, csl-apidev repositories
--- regenerate displays at Cologne
# login to cologne server
cd csl-pywork/v02
---------------------
Sync this repo to github

Done with this issue.
