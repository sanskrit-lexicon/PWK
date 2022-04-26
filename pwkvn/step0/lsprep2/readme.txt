
Start with version 10 ../../orig/pwk1-7VN_ansi_10.txt
python ../cp1252_utf8.py ../../orig/pwk1-7VN_ansi_10.txt temp_pwkvn_10.txt


========================================================================

python ls2.py temp_pwkvn_10.txt ls2_10.txt 
615 ls counts written to ls2_10.txt

This uncovers a few missed <ls> in version 10.
 diff ../lsprep1/ls1.txt ls2_10.txt | wc -l
27

========================================================================
temp_pwkvn_11.txt  manual changes
python ls2.py temp_pwkvn_11.txt ls2_11.txt 
613 ls counts written to ls2_11.txt

python ../diff_to_changes.py temp_pwkvn_10.txt temp_pwkvn_11.txt change_11.txt
3 changes 
========================================================================
change_ls2.py
Generates a new version: temp_pwkvn_12.txt, with closing </ls> after the
literary source names.  Line breaks and pages breaks are retained.
Also generates a frequency count of ls names
python change_ls2.py temp_pwkvn_11.txt ls2_11a.txt temp_pwkvn_12.txt

ls2_11a.txt is same as ls2_11.txt.
========================================================================
ls3:  Generates list of lsnames based upon <ls>xxx</ls>
python ls3.py temp_pwkvn_12.txt ls3_12.txt
As expected, ls3_12.txt is same as ls2_11.txt.

========================================================================
There are some issues with temp_pwkvn_12.txt
which make ls3 more complicated than desired.

The next version (temp_pwkvn_13.txt) introduces these by manual changes

These are determined by refining ls4.py and ls4.txt
python ls4.py temp_pwkvn_13.txt ls4.txt
610 ls counts written to ls4.txt
HERE are some of the changes made in temp_pwkvn_13.txt.

python ../diff_to_changes.py temp_pwkvn_12.txt temp_pwkvn_13.txt change_13.txt
change_13.txt has the changes.  (303 changes made).
NOTE: German correction material made based on temp_pwkvn_13.txt

Parentheses
(29) '<ls>NI1LAK.)</ls>' -> '<ls>NI1LAK.</ls>)'
(10) '<ls>BÜHLER).</ls>' -> '<ls>BÜHLER</ls>).'
(1) 'MBH.),</ls>' -> 'MBH.</ls>),
[Page...]
(27) ' [PageX]</ls>' -> '</ls> [PageX]'   (regex change)
(1) '<ls>ANARGHAR. S.</ls> 153.' -> '<ls>ANARGHAR.</ls> S. 153.'
    Question.  8 like '<ls>ANARGHAR.</ls> 5, 11.',
    So maybe 'S.' is for 'Seite'? 
Commas
(22) <ls>BÜHLER,</ls> -> <ls>BÜHLER</ls>,
(5)  <ls>BÜH-²LER,</ls> -> <ls>BÜH-²LER</ls>,
     Note: '<ls>BÜHLER,</ls> ²Rep. No. 561.'
      Should it be? '<ls>BÜHLER, ²Rep.</ls> No. 561.'
(1) <ls>MAVR,</ls> -> <ls>MAVR</ls>,
     Question: <ls>MAVR</ls>, <ls>Ind. Erb.</ls> 18. ->?
               <ls>MAVR, Ind. Erb.</ls> 18.
	       Page 1-286c  adhriyamANa
(29) <ls>M. MÜLLER,</ls> -> <ls>M. MÜLLER</ls>,
     Question: <ls>M. MÜLLER,</ls> ²Ren. 299. -> ?
               <ls>M. MÜLLER, ²Ren.</ls> 299.
(7) <ls>M. ²MÜLLER,</ls> -> <ls>M. ²MÜLLER</ls>,
(43) <ls>PISCHEL,</ls> -> <ls>PISCHEL</ls>,
    Question: <ls>PISCHEL</ls>, Vedische ²Studien 77. fgg.
(3) <ls>PI-²SCHEL,</ls> -> <ls>PI-²SCHEL</ls>,
(8) GELDNER,</ls> -> GELDNER</ls>,
    Question: <ls>GELDNER, Vedische Studien</ls> 128. fgg.
(1) BHA1M. V, -> BHA1M. V.  (print change)
(2) <ls>WILSON,</ls> -> <ls>WILSON</ls>,
   Question: <ls>WILSON</ls>, Sel. Works
             <ls>WILSON</ls>, Sel. ²W.
(5) <ls>VAIJAYANTI1,</ls> -> <ls>VAIJAYANTI1</ls>,
(5) BHU1MIK.,</ls> -> BHU1MIK.</ls>,
   Question: <ls>VAIJAYANTI1</ls>, <ls>BHU1MIK.</ls>, <ls>BRA1HMAN2A1DHY.</ls>
(1) <ls>HAUG,</ls> Acc. 59.  -> <ls>HAUG</ls>, Acc. 59.
(1) <ls>EITEL,</ls> Chin. B. -> <ls>EITEL</ls>, Chin. B.
(1) <ls>KA1D. II,</ls> 115, 4. -> <ls>KA1D. II</ls>, 115, 4.
(2) BR.,</ls> -> BR.</ls>,
(1) '<ls>WARD,</ls> a View ²of the History u. s. w. III, S. 11' ->
    '<ls>WARD</ls>, a View ²of the History u. s. w. III, S. 11'
    Question
(1) <ls>RA1M RA1S,</ls> Architecture, S. 4 -> Question
    <ls>RA1M RA1S</ls>, Architecture, S. 4
(5) .,</ls> -> .</ls>,
(2) <ls>LEUMANN,</ls> Aup. Gl. -> Question
    <ls>LEUMANN</ls>, Aup. Gl.
(1) <ls>BEZZENBERGER,</ls> ²Beitr. 3, 261 -> Question
    <ls>BEZZENBERGER</ls>, ²Beitr. 3, 261
(1) '<ls>BURGESS,</ls> Archaeoi. Survey of Southern ²India, No. 3, S. 45. 54.' ->
    '<ls>BURGESS</ls> Archaeoi., Survey of Southern ²India, No. 3, S. 45. 54.'
    Question

========================================================================
temp_pwkvn_14.txt  misc. manual changes
python ../diff_to_changes.py temp_pwkvn_13.txt temp_pwkvn_14.txt change_14.txt
change_14.txt has the changes.  (44 changes made).
========================================================================
========================================================================
ls4.py  Regenerates list of lsnames using the simpler logic.
python ls4.py temp_pwkvn_14.txt ls4.txt
605 ls counts written to ls4.txt
========================================================================
transfer temp_pwkvn_11.txt, 12, 13, 14 to orig in cp1252 encoding
python ../utf8_cp1252.py temp_pwkvn_11.txt ../../orig/pwk1-7VN_ansi_11.txt
python ../utf8_cp1252.py temp_pwkvn_12.txt ../../orig/pwk1-7VN_ansi_12.txt
python ../utf8_cp1252.py temp_pwkvn_13.txt ../../orig/pwk1-7VN_ansi_13.txt
python ../utf8_cp1252.py temp_pwkvn_14.txt ../../orig/pwk1-7VN_ansi_14.txt

========================================================================


========================================================================
========================================================================
========================================================================
