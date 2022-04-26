
Start with version 23: ../../orig/pwk1-7VN_ansi_23.txt
python ../cp1252_utf8.py ../../orig/pwk1-7VN_ansi_23.txt temp_pwkvn_23.txt

========================================================================
start with a copy of ../meta/meta1_edit.txt
cp ../meta/meta1_edit.txt .
This is used to complete abbreviated alternate headwords.

========================================================================
temp_pwkvn_24.txt  Precursor to pwkvn.txt (dictionary form).
meta3.py
 A variation of ../meta/meta2.py, which generates alternate headwords.
 
python meta3.py temp_pwkvn_23.txt meta1_edit.txt temp_pwkvn_24.txt

convert to ansi and save in orig
python ../utf8_cp1252.py temp_pwkvn_24.txt temp_pwkvn_24_ansi.txt
cp temp_pwkvn_24_ansi.txt ../../orig/pwk1-7VN_ansi_24.txt

========================================================================
cp ../lsprep3/transcoder.py .
cp ../lsprep3/as_roman.xml .
cp ../lsprep3/roman_as.xml .
cp ../slp/hk_slp1.xml .
cp ../slp/slp1_hk.xml .

========================================================================
temp_pwkvn_25.txt (manual)
  Miscellaneous changes uncovered during final.py


python ../diff_to_changes.py temp_pwkvn_24.txt temp_pwkvn_25.txt change_25.txt
294 changes written to change_25.txt

convert to ansi and save in orig
python ../utf8_cp1252.py temp_pwkvn_25.txt temp_pwkvn_25_ansi.txt
cp temp_pwkvn_25_ansi.txt ../../orig/pwk1-7VN_ansi_25.txt

Note 1: 
In <ls>X</ls>, change SH to S2.
Reason:  Print has 'sh' for the iast spelling of
  cerebral sibilant (HK=S, slp1=z).
  In <ls>X</ls>, this is currently coded as SH.
  in {|X<|}, this is coded as S2 (or s2).

  In conversion to IAST, both S2 and SH will be changed to Ṣ.
  For the IAST conversion to be invertible, we should not have
  instances of both S2 and SH --  either one COULD be chosen.

  Since there are about 600 SH in <ls>X</ls>, and about 150 [Ss]2 in
  {|X|},  I choose to change the latter to SH/sh.
  s2 -> sh  (153 changes in 149 lines)

Note as_roman.xml and roman_as.xml only convert SH and sh.
----------------------------------------------------------
Note 2: 3 greek phrases under headwords. Change from empty string
 to a unique string
 <hw>{#juka#}</hw> : <pc>5-254-c
   <gr></gr> -> <gr>greek1</gr>
   pw: <lang n="greek">ζυγόν</lang>
   
 <hom>5.</hom> <hw>{#pArtha#}</hw> : <pc>5-259-c
   <gr></gr> -> <gr>greek2</gr>
   παρθενος
 <hw>{#zakasthAna#}</hw> : <pc>6-306-c
   <gr></gr> -> <gr>greek3</gr>
   pw: Ζακαστηνη
----------------------------------------------------------
add ls markup to Spr. (140 instances)

========================================================================
temp_pwkvn_25_slp1.txt  Bijective Conversion from prior version
python final.py hk,slp1 temp_pwkvn_25.txt temp_pwkvn_25_slp1.txt
check invertibility:
python final.py slp1,hk temp_pwkvn_25_slp1.txt temp.txt
diff temp_pwkvn_25.txt temp.txt | wc -l
 # 0  as expected

conversions:
 {#X#} hk <-> slp1
   Accents:  [£_¹]  <->  /\^
   Similarly in metaline k1 and k2 values.
 {|X|} <-> <is>Y</is>  [treated as wide in display for pwg]
    AS is converted to IAST
 <ls>X</ls> <-> <ls>Y</is>  AS is converted to IAST
 S4l. <-> Śl.   (AS coding not in <ls>X</ls> or {|X|} -- only 2 instances)
 masc ord indicator º <-> degree °
 ²  <-> <lb>  line break  (cannot use <lb/>, since / has meaning in devanagari)
========================================================================
hwextra
python hwextra.py temp_pwkvn_25_slp1.txt pwkvn_hwextra.txt
 
========================================================================

temp_pwkvn_26_slp1.txt manual changes noticed while adding ab markup

python ../diff_to_changes.py temp_pwkvn_25_slp1.txt temp_pwkvn_26_slp1.txt change_26.txt
52 changes written to change_26.txt

convert to ansi and save in orig
python final.py slp1,hk temp_pwkvn_26_slp1.txt temp_pwkvn_26_hk.txt

python ../utf8_cp1252.py temp_pwkvn_26_hk.txt temp_pwkvn_26_ansi.txt
cp temp_pwkvn_26_ansi.txt ../../orig/pwk1-7VN_ansi_26.txt

========================================================================
version 27 add <ab>X</ab> markup
cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pwkvn/pywork/pwkvnab/pwkvnab_input.txt .
python abinit.py temp_pwkvn_26_slp1.txt pwkvnab_input.txt temp_pwkvn_27_slp1.txt
92049 lines read from temp_pwkvn_26_slp1.txt
71 abbreviations read from pwkvnab_input.txt
11911 lines changed
92049 records written to temp_pwkvn_27_slp1.txt

convert to ansi and save in orig
python final.py slp1,hk temp_pwkvn_27_slp1.txt temp_pwkvn_27_hk.txt
# check invertibility
python final.py hk,slp1 temp_pwkvn_27_hk.txt temp.txt
diff temp_pwkvn_27_slp1.txt temp.txt | wc -l
 # 0 as expected
python ../utf8_cp1252.py temp_pwkvn_27_hk.txt temp_pwkvn_27_ansi.txt
cp temp_pwkvn_27_ansi.txt ../../orig/pwk1-7VN_ansi_27.txt


========================================================================
