
10-15-2025 begun ejf
fix references t Ramayana Gorresio edition

sanskrit-lexicon-scans/

Ref: https://github.com/sanskrit-lexicon/PWK/tree/master/pwkissues/issue83fix
this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue83fix

-------------------------------------
# get temporary local copy of koshas
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temp_pwkvn_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt temp_sch_0.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw_0.txt

--------------------------------------
link target sample: https://sanskrit-lexicon-scans.github.io/ramayanagorr/?N,N,N


--------------------------------------
For mw, changes made previously in work on Bombay Ramayana
See 
https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issue75fix
this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue75fix

-------------------------------------------------
We use lsfix2.py, with parmfile lsfix2_parm.py
to examine splitting

For each kosha, try to resolve non-standard references by
splitting multiple references into sequences of standard references,
and making manual changes to the kosha.

See the readme files for these koshas:

readme_pwg.txt 18 links added.  temp_pwg_2.txt
  Revisions to
    pwgbib_input.txt  (csl-pywork)
  
readme_pw.txt  0 additional links.  No change to pw.txt
     Revise pwbib_input.txt  (pywork repo)
     
readme_pwkvn.txt 0 additional links. No changes to pwkvn.txt 
   
     
readme_sch.txt  1 additional link.  temp_sch_1.txt
 
 
readme_mw.txt  no changes (See above comment)

================================================
INSTALLATION
sync to github:

------------------
# csl-orig 
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue83fix
diff temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt | wc -l
#diff temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt | wc -l
#diff temp_pwkvn_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt | wc -l
diff temp_sch_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt | wc -l
#diff temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt | wc -l
#0  as expected

cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "issue83fix  splitting 'Ramayana Gorresio' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue83fix


# csl-pywork
cd /c/xampp/htdocs/cologne/csl-pywork
git pull
git add .
git commit -m "issue83fix  splitting 'Ramayana Gorresio' refs
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue83fix

---------------------------------------------------
# sync to Cologne,
pull changed repos,
redo displays for  pwg, pw, pwkvnsch, mw

---------------
csl-orig #pull
csl-websanlexicon #pull
csl-apidev #pull
csl-corrections #pull
csl-pywork #pull
---------------
# update displays for pwg sch
cd csl-pywork/v02
sh generate_dict.sh pwg  ../../PWGScan/2020/
#sh generate_dict.sh pw  ../../PWScan/2020/
#sh generate_dict.sh pwkvn  ../../PWKVNScan/2020/
sh generate_dict.sh sch  ../../SCHScan/2020/ 
#sh generate_dict.sh mw  ../../MWScan/2020/

-----------------------------------------------------
# sync issue83fix to github.
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue83fix
git pull
git add .
git commit -m "issue83fix 'Ramayana Gorresio' link splitting
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push

------------------------------------------------------------
THE END
