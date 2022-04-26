
Start with version 15: ../../orig/pwk1-7VN_ansi_15.txt
python ../cp1252_utf8.py ../../orig/pwk1-7VN_ansi_15.txt temp_pwkvn_15.txt


========================================================================
list all instances of 'wide' text (taking into account line-break)
python wide.py temp_pwkvn_15.txt wide_15.txt 
22569 lines read from temp_pwkvn_15.txt
589 wide text written to wide_15.txt

New version, start with version 15
cp temp_pwkvn_15.txt temp_pwkvn_16.txt

python wide.py temp_pwkvn_16.txt wide_16.txt 
22569 lines read from temp_pwkvn_16.txt
518 wide text written to wide_16.txt

========================================================================
transcoder.py transcoder module for python
from github repository funderburkjim/sanskrit-transcoding
cp /c/xampp/htdocs/funderburkjim/sanskrit-transcoding/transcoder.py .



========================================================================
Convert the ls names in wide_16.txt to iast.
The transcoder files as_roman.xml and roman_as.xml are slightly different
from those in ../lsprep3  (SH, sh <-> S2, s2; also h2,H2.

python as_roman.py as,roman wide_16.txt temp_wide_16_iast.txt

# check invertibility
python as_roman.py roman,as temp_wide_16_iast.txt temp.txt
diff wide_16.txt  temp.txt
 ## no difference, as expected
 rm temp.txt
========================================================================
prepare change_16.txt for all the changes from version 15 to version 16
python ../diff_to_changes.py temp_pwkvn_15.txt temp_pwkvn_16.txt change_16.txt
153 changes written to change_16.txt

========================================================================
transfer temp_pwkvn_16.txt to orig in cp1252 encoding
python ../utf8_cp1252.py temp_pwkvn_16.txt ../../orig/pwk1-7VN_ansi_16.txt

========================================================================


