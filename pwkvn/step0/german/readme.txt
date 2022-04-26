german
 check German spelling in pwkvn

======================================================================
temp_germansave.txt
Source:
https://gist.github.com/MarvinJWendt/2f4f4154b8ae218600eb091a5706b5f4/raw/36b70dd6be330aa61cd4d4cdfda6234dcb0b8784/wordlist-german.txt

1908815 words
======================================================================
pwkvn version 13

python ../cp1252_utf8.py ../../orig/pwk1-7VN_ansi_13.txt temp_pwkvn_13.txt

python gtext1.py temp_pwkvn_13.txt temp_germansave.txt gtext1_known.txt gtext1_unknown.txt
Examine italic text, assumed to be German.

======================================================================

pwkvn_german_unknown.txt
copy of gtext1_unknown.txt analyzed in Google Docs.
The Google Docs Spell check provides visual clue (red jagged underline).
These examined manually and an 'x' inserted as 1st character for underlined word
1093 marked with 'x' out of 2964 (so slightly over 1/3 are marked).

======================================================================
python gtext2.py temp_pwkvn_13.txt pwkvn_german_unknown.txt temp_gtext2.txt
show records of temp_pwkvn_13.txt that have words marked with 'x' in
pwkvn_german_unknown.txt

temp_gtext2.txt superceded by gtext3.txt

======================================================================
unknown_x.txt
 just the lines of pwkvn_german_unknown.txt starting with 'x'
 1093 lines

python unknown_number.py unknown_x.txt unknown_x_num.txt
Replace the frequency count with a sequence number.

Use google translate on unknown_x_num.txt to get unknown_x_eng.txt
5000 char limit, so has to be done in sections.

1-299, 300-589, 590-799,
800-999, 1000-1093

=====================================
Merge unknown_x_num.txt with unknown_x_eng.txt to

python unknown_merge.py unknown_x_num.txt unknown_x_eng.txt unknown_merge.txt


=====================================
python gtext3.py temp_pwkvn_13.txt unknown_merge.txt gtext3.txt
=====================================
gtext3_revised.txt
 Edited by Thomas, received 04-03-2022
 Edited lines marked with greek letter mu: μ
 
 These changes are applied in temp_pwkvn_23.txt
  (see step0/final,  also orig)

