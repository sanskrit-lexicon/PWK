
Start with version 14: ../../orig/pwk1-7VN_ansi_14.txt
python ../cp1252_utf8.py ../../orig/pwk1-7VN_ansi_14.txt temp_pwkvn_14.txt


========================================================================
python ls4.py temp_pwkvn_14.txt ls4_14.txt 
22569 lines read from temp_pwkvn_14.txt
605 ls counts written to ls4_14.txt

cp /c/xampp/htdocs/cologne/csl-pywork/v02/makotemplates
========================================================================
transcoder.py transcoder module for python
from github repository funderburkjim/sanskrit-transcoding
cp /c/xampp/htdocs/funderburkjim/sanskrit-transcoding/transcoder.py .

========================================================================
programs adapted from repository  sanskrit-lexicon/PWG
in folder pwg_ls/pwgbib/digitization

as_roman.xml  transcoder file
roman_as.xml  transcoder file
as_roman.py   model of transcoder application


========================================================================
traninvert.py  
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls/pwgbib/digitization/traninvert.py .

adapt as_roman.xml to current needs.
python traninvert.py as_roman.xml roman_as.xml
But then modify roman_as.xml to NOT convert umlauts
  (since Ü, Ö appear in pwkvn rather than U7, O7)
========================================================================
First, convert the ls names in ls4_14.txt to iast.
python as_roman.py as,roman ls4_14.txt temp_ls4_14_iast.txt

# check invertibility
python as_roman.py roman,as temp_ls4_14_iast.txt temp.txt
diff ls4_14.txt  temp.txt
 ## no difference, as expected
 rm temp.txt
========================================================================
Compare ls4_iast with pwbib
The results of the compare.py program are used to correlate the literary
source abbreviations appearing in pwkvn to the literary source abbreviations
used in pw.txt.  

The source for the pw abbreviations is
temp_pwls.txt: summary of pwk ls markup
cp /c/xampp/htdocs/sanskrit-lexicon/PWK/pw_ls/summary/lsextract_pw.txt temp_pwls.txt

First, generate the initial comparisons, based on version 14 of pwkvn:
python compare.py temp_ls4_14_iast.txt temp_pwls.txt compare_14.txt compare_14_pwunused.txt
605 Vnls records read from temp_ls4_14_iast.txt
847 Pwls records read from temp_pwls.txt
  skipping ALL, NUMBER, UNKNOWN
316 matches found, 289 unmatched
605 records written to compare_14.txt
528 unmatched pwbib records written to compare_14_pwunused.txt

========================================================================
Iterative analysis leads to manual changes in the next version of pwkvn:
temp_pwkvn_15.txt (starts as a copy of temp_pwkvn_14.txt).
notes_15.txt contains notes made during this comparison process.

python ls4.py temp_pwkvn_15.txt ls4_15.txt 
python as_roman.py as,roman ls4_15.txt temp_ls4_15_iast.txt
python compare.py temp_ls4_15_iast.txt temp_pwls.txt compare_15.txt compare_15_pwunused.txt

The final results of compare.py:
585 Vnls records read from temp_ls4_15_iast.txt
847 Pwls records read from temp_pwls.txt
  skipping ALL, NUMBER, UNKNOWN
326 matches found, 259 unmatched
585 records written to compare_15.txt
518 unmatched pwbib records written to compare_15_pwunused.txt

========================================================================
prepare change_15.txt for all the changes from version 14 to version 15
python ../diff_to_changes.py temp_pwkvn_14.txt temp_pwkvn_15.txt change_15.txt
645 changes written to change_15.txt

========================================================================
transfer temp_pwkvn_15.txt to orig in cp1252 encoding
python ../utf8_cp1252.py temp_pwkvn_15.txt ../../orig/pwk1-7VN_ansi_15.txt

========================================================================


