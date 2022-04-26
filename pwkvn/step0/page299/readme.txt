
Start with ../orig/pwkvn_vol1_page299_ansi.txt
# convert to utf8
python ../cp1252_utf8.py ../../orig/pwkvn_vol1_page299_ansi.txt temp_299_01.txt

Objectives:
1. Add markup to this page analogous to that in pwkvn1-7VN_ansi_21.txt
2. Insert result into pwkvn1-7VN_ansi_22.txt

===========================================================
local copy temp_pwkvn_21.txt
python ../cp1252_utf8.py ../../orig/pwkvn1-7VN_ansi_21.txt temp_pwkvn_21.txt
===========================================================
temp_299_02.txt Apply <ls>X</ls> markup
 Manual
 use lsprep3/compare_15.txt  for known <ls>X</ls>
 
===========================================================
temp_299_03.txt Apply <hw>X</hw> markup
 Also apply <hom>N.</hom> markup  (1)
 Also {%a,%} -> {%a%}, (5)
===========================================================
temp_299_04.txt add pc markup
<p> -> <p pc="1-299-a">  (or -b or -c)

===========================================================
Add n="" markup.
temp_299_05.txt
The 50 entries in page1-299 goes after n=01719 of temp_pwkvn_21.txt
<p n="01719" pc="1-298-c"><hw>{#unnati#}</hw> 1) {%erectio%} (penis) <ls>KAUTUKAR.</ls> 68. [Page2-285-a] 
<H>Nachträge und Verbesserungen. [2] 
<p n="01721" pc="2-285-a"><hw>{#aMzumadbhedasaMgraha#}</hw> m. Titel eines Werkes Opp. Cat. 1. 

For some reason, n="01720" is absent in pwkvn_21, so
I will use it.
I'll add two digits f
the numbers in page299 will be n="0172001"  to n="0172050"
python addnum.py temp_299_04.txt temp_299_05.txt
===========================================================
temp_pwkvn_22.txt
insert temp_299_05.txt after n="01719"
Also, correct the [Page2-285-a] to [Page1-299-a] in n="01719"

===========================================================
repeat the analysis in ../meta, using temp_pwkvn_22.txt.
python ../meta/meta2.py temp_pwkvn_22.txt ../meta/meta1_edit.txt temp_pwkvn_22a.txt

python ../meta/meta2_analyze1.py temp_pwkvn_22a.txt ../meta/analyze1_problems.txt temp_analyze1_22.txt

===========================================================
Transfer version 22 to orig

transfer temp_pwkvn_22.txt to orig in cp1252 encoding
python ../utf8_cp1252.py temp_pwkvn_22.txt ../../orig/pwk1-7VN_ansi_22.txt

check invertibility
 python ../cp1252_utf8.py ../../orig/pwk1-7VN_ansi_22.txt temp.txt
 diff temp_pwkvn_22.txt temp.txt
 # no difference expected.

===========================================================
===========================================================
===========================================================
