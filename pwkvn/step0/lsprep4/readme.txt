lsprep4:  Revise the literary source tooltips for pwkvn.

Start with version 28: ../../orig/pwk1-7VN_ansi_28.txt
python ../cp1252_utf8.py ../../orig/pwk1-7VN_ansi_28.txt temp_pwkvn_28_hk.txt



========================================================================
redo work from /c/xampp/htdocs/sanskrit-lexicon/PWK/pw_ls/summary

Start with a copy of latest pw.txt at 
  cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw.txt

and with a copy of latest pwbib_input.txt
cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pw/pywork/pwauth/pwbib_input.txt temp_pw_tooltip.txt

cp /c/xampp/htdocs/sanskrit-lexicon/PWK/pw_ls/summary/lsextract_all.py lsextract_all1.py
revise all1 to print full information from pw_tooltip.

python lsextract_all1.py temp_pw.txt temp_pw_tooltip.txt temp_pwls.txt

========================================================================
python ls4.py temp_pwkvn_28_hk.txt ls4_28.txt 
92049 lines read from temp_pwkvn_28_hk.txt
589 ls counts written to ls4_28.txt

Make iast version for 'compare' program
python as_roman.py as,roman ls4_28.txt temp_ls4_28_iast.txt

# check invertibility
python as_roman.py roman,as temp_ls4_28_iast.txt temp.txt
diff ls4_28.txt  temp.txt
 ## no difference, as expected
 rm temp.txt

========================================================================
pwkvn
========================================================================
python compare.py temp_ls4_28_iast.txt temp_pwls.txt compare_28.txt compare_28_pwunused.txt

compare_28_edit.txt  Manual editing to fill in missing identifications.
pwkvn_tooltip.txt  from compare_28_edit.txt, removing first 3 tab columns.

python ls4.py temp_pwkvn_28.txt ls4_28.txt 
=======================================================================
Compare ls4_iast with pwbib
The results of the compare.py program are used to correlate the literary
source arbbreviations appearing in pwkvn to the literary source abbreviations
used in pw.txt.  

# convert to slp1  (paths are relative to pwkvn/step0/final)
sh hk_slp1.sh ../lsprep4/temp_pwkvn_28_hk.txt  ../lsprep4/temp_pwkvn_28_slp1.txt

Further, remove '-<lb/>' and '<lb/>' and '[Page...]'

python lsextract_all1.py temp_pwkvn_28_slp1.txt pwkvn_tooltip.txt temp_pwkvnls.txt

========================================================================
cp pwkvn_tooltip.txt /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pwkvn/pywork/pwkvnauth/pwkvnbib_input.txt 

cp temp_pwkvn_28_hk.txt ../lsnum/temp_pwkvn_28_hk.txt
cp ../lsnum/temp_pwkvn_28_hk.txt ../lsnum/tempprev_pwkvn_28_hk.txt
cp temp_pwkvn_28_hk.txt ../lsnum/temp_pwkvn_28_hk.txt

========================================================================
