
Start with temporary copies of pw.txt and sch.txt.
  temp_pw.txt
  temp_sch.txt  (the latest version constructed in step1)
  
Filter sch for type=EMPTY-STRING.

 --------------------------------------------------------
Several displays/extracts based on temp_sch.txt

# --------------------------------------------------------
 
python extract1.py temp_sch.txt temp_extract1.txt
  This filters only records with type=EMPTY-STRING (the PW-VN cases, we think).
  
Format:  L=N HOM. TYPE {%Y%}¦ TEXT
HOM. is optional; If present, it is the PW homonymn number (a digit),
  followed by period.
TYPE is optional:  ° * + are possible values
   Since this report filters on type=EMPTY-STRING, this field never present.
Y is IAST (with accents, and sometimes other characters)

# -------------------------------------------------------------
# extract2 generates a PW form  in a transcoding
# first arg is the transcoding output name.  IAST in {%X%} transcoded to {%Y%}
python extract2.py slp1 temp_sch.txt temp_extract2_slp1.txt   

# -------------------------------------------------------------
python extract2.py deva1 temp_sch.txt temp_extract2_deva.txt   
# Recover temp_extract2_slp1.txt from temp_extract2_deva.txt   
python extract2_invert_deva.py temp_extract2_deva.txt temp_extract2_deva_slp1.txt   
# validate invertibility
diff temp_extract2_slp1.txt temp_extract2_deva_slp1.txt | wc -l
0  [files are identical]
# remove unneeded file:
rm temp_extract2_deva_slp1.txt

# -------------------------------------------------------------
# recover temp_extract1.txt from temp_extract2_slp1.txt
# This is currently impossible, since temp_extract1.txt has capitalized IAST characters,
# but slp1 transcoding does not recognize the capitalization.
# However, we should get identity except for this aspect.

python extract2_invert_slp1.py temp_extract2_slp1.txt temp_extract2_slp1_roman1.txt

diff temp_extract1.txt temp_extract2_slp1_roman1.txt | wc -l
6112 lines in diff (about 1500 lines are different)

 These differences are due to capitalization of IAST in {%X%}, present in
 temp_extract1.txt but not in extract2_slp1_roman1.txt.
 A program confirms the nature of differences.
python compare_roman1.py temp_extract1.txt temp_extract2_slp1_roman1.txt temp_compare_roman1.txt
0 unexplained.
NOTE: compare Nth lines from the two files,
  after adjusting the line from temp_extract1.txt by changing {%X%} to
  {%x%}  (i.e., lower-casing X).


-------------------------------------

VN estimation (via first letter of headword)
These are the volumes of PWK
1  a to O
2  k to Q
3  t to n
4  p to B
5  m to l
6  v to S
7  s to h

python pwinfo.py temp_sch.txt temp_pw.txt pwinfo.txt
output contains:
L  the Schmidt Cologne record id
V The volume of PW containing the headword, in Arabic numerals or '0' if
   headword not found in PW
VN If headword in PW, then same as V.  Else, estimate 1-7 by above table.

