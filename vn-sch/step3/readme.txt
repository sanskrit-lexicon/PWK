
Start with
  temp_sch.txt  (the latest version constructed in step1)
  pwk_page256-265_ansi.txt : digitization of 10 pages from VN of volume 3
    of PWK.
    
# --------------------------------------------------------
extract3 display.
# extract3 is similar to step2/extract2, but 
#  does NOT filter on type = EMPTY-STRING (i.e. output contains all
#  entries in schmidt.
python extract3.py slp1 temp_sch.txt extract3_slp1.txt   
SAMPLE:
L=4 {#aMSagrAhin#}¦ Adj. ein Erbteil empfangend, Viṣṇus. 15, 39.

# --------------------------------------------------------
# work with pwk3-VN extract
# --------------------------------------------------------
# 1) pwk3vn_utf8.txt
python cp1252_utf8.py ../pwk_page256-265_ansi.txt pwk3vn_utf8.txt
# check invertibility
python utf8_cp1252.py pwk3vn_utf8.txt temp_pwk3vn_utf8_cp1252.txt
diff ../pwk_page256-265_ansi.txt temp_pwk3vn_utf8_cp1252.txt
[no difference]
rm temp_pwk3vn_utf8_cp1252.txt
# --------------------------------------------------------
# examine extended ascii character usage
python ea.py pwk3vn_utf8.txt pwk3vn_eascii.txt
  8 extended ascii characters
£  (\u00a3)    97 := POUND SIGN   used in {#X#} to represent udAtta accent
·  (\u00b7)   509 := MIDDLE DOT   indicates line break
º  (\u00ba)    72 := MASCULINE ORDINAL INDICATOR  change to DEGREE SIGN °
×  (\u00d7)     1 := MULTIPLICATION SIGN einen Zeitraum von 3×24 Mi-·nuten ausfüllend
# --------------------------------------------------------
# 2) change1.txt preliminary changes
a) Move period character outside {#X#}.
   39 instances, all at end: {#X.#}   These assumed punctuation,
   rather than danda.  There are no '|' {#X#}.
b) MASCULINE ORDINAL INDICATOR -> DEGREE SIGN.
c) £ -> /   [udAtta accent]
d) _ -> ^  in {#X#}  svarita accent example {#iraNya_#} [page 256-2]
e) '{#*' -> '*{#' AND '{%*' -> '*{%'
python change1.py pwk3vn_utf8.txt temp_change1.txt
 manually edit as change1.txt
 Also correct systematic typing error in pwk:  jJ -> j
 python change1a.py pwk3vn_1.txt temp_change1a.txt
    and add to change1.txt
 python updateByLine.py pwk3vn_utf8.txt change1.txt pwk3vn_1.txt
 219 lines changed
# --------------------------------------------------------
# 3) convert {#X#} from HK to SLP1
NOTE: all lines (except first line) are blank lines 
OR start with '<p>{#X#}' 
OR start with '<p>N. {#X#}'
This X is the headword.
There may also be {#X#} text after the headword.
Here X is HK, except for accents, which have £ character for udAtta
   (PWK superscript 3).
Use hk_slp1.xml and slp1_hk.xml transcoding files in ../transcoder/ directory
  These copied from websanlexicon.
python pwk_transcode.py  slp1 pwk3vn_1.txt pwk3vn_2.txt

# --------------------------------------------------------
# 4) compare pwk3vn_2 and schmidt (extract3_slp1)
Sanskrit in output can be slp1 or Devanagari
python compare_pwkvn_sch.py slp1 pwk3vn_2.txt extract3_slp1.txt compare_pwkvn_sch.txt


# ===============================================================
  BELOW ARE OLD notes from step2.
  
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

