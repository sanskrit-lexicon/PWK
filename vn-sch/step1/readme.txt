
Start with temporary copies of sch.txt.
  temp_sch.txt  from csl-orig/v02/sch/sch.txt at
   commit 1c933ccd4184d49ee651244cf73f6829077f426c
   
Filter sch for type=EMPTY-STRING.

python change1.py temp_sch.txt temp_change1.txt
 Edit copy change1.txt as changes to apply to temp_sch.txt
Inconsistent accents with diphthongs:
 ái  (1),  aí (14) instances
 áu  (0),  aú (9)
Does not use preformed accents


# ------------------------------
# transcode_work.txt
# generate listing of the relevant transcoding, slp1, roman1, deva1
# deva1  uses pwg, pwk convention for accents
# roman1 uses also shows accents
As usual, exceedingly tricky and complex for basically no information.
The bane of existence in this field.
python transcode_work.py transcode_work.txt
# -----------------------------

python updateByLine.py temp_sch.txt change1.txt temp_sch1.txt

# --------------------------------------------------------
# reposition the homonymns. originally the format in TEXT is
 {#X#} {%Y%}¦ {!N!} TEXT1
 CHANGE to
 {#X#} N. {%Y%}¦ TEXT1
 
python change2.py temp_sch1.txt change2.txt
python updateByLine.py temp_sch1.txt change2.txt temp_sch2.txt

# --------------------------------------------------------
# change3:  several minor improvements
#  '.%}' -> '%}.'   Italic text is IAST Sanskrit. Similarly for comma, semicolon
# Remove space before ','
# Remove multiple spaces
# change 'º' (MASCULINE ORDINAL INDICATOR) to '°' (DEGREE SIGN)
# change '°=' to '° ='
python change3.py temp_sch2.txt temp_change3.txt
 # 29191 changes
python updateByLine.py temp_sch2.txt temp_change3.txt temp_sch3.txt

# --------------------------------------------------------
# change4:  Insert 'type' character : e.g. {%*X%}
python change4.py temp_sch3.txt temp_change4.txt
 #  changes
python updateByLine.py temp_sch3.txt temp_change4.txt temp_sch4.txt

# --------------------------------------------------------
# change5:  Remove the {#X#} in first line of text
Reasons: (a) Duplicates k1 of metaline, (b) Devanagari not present in Schmidt
 print.
python change5.py temp_sch4.txt temp_change5.txt
 #  changes
python updateByLine.py temp_sch4.txt temp_change5.txt temp_sch5.txt

# --------------------------------------------------------
# change6:  Correct errors in k2 iast coding. Preparation for change7

python change6.py temp_sch5.txt temp_change6.txt
 # change6.txt constructed manually from temp_change6.txt
 # also changed ā̀̀ (usually to ā́  (with a couple of exceptions)
 # python change6a.py temp_sch6.txt temp_change6a.txt
 #  Cases reviewed and added manually to change6.txt.
 #    about 80 cases {%X%} where X has a period (the periods at end were
 #    previously relocated in change3)
 
python updateByLine.py temp_sch5.txt change6.txt temp_sch6.txt

# --------------------------------------------------------
# change7:  convert k2 from iast to slp1.  It is convention that
#  both k1 and k2 are in slp1.

python change7.py temp_sch6.txt temp_change7.txt
 #  changes
python updateByLine.py temp_sch6.txt temp_change7.txt temp_sch7.txt

# --------------------------------------------------------
Install temp_sch7.txt as new version in csl-orig
cp temp_sch7.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt             
# Recreate with csl-pywork/v02 and check validity.
# This version should also be run with new version of make_xml.py in csl-pywork/v02

# --------------------------------------------------------
Several displays/extracts based on temp_sch7.txt

