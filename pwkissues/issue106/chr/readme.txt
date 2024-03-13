chr
expand ls markup for Chr. (Bohtlingk Chrestomathie)
03-12-2024 begin

Plan:
step 1: generate all current Chr. instances
  two forms: <ls>Chr. X</ls> and <ls n="Chr.X">Y</ls>

step 2: transform 'incomplete' instances to complete instances.

step 3: Generate change transactions for pw using the complete instances

The choice of input digitization may need to change, depending on
when this is run.
At this moment (03-12-2024), we use ../temp_pw_6.txt
--------------------------------------------------------------------
step1
python ls_instances.py 'Chr.' ../temp_pw_6.txt chr_instances.txt
764912 from ../temp_pw_6.txt
4547 distinct instances
5706 total instances
4547 lines written to chr_instances.txt

--------------------------------------------------------------------
step1 review
 two numbers (digit sequences)
<ls>Chr. x,y</ls>
<ls n="Chr.">x,y</ls>
<ls n="Chr. x,">y</ls>

<ls>Chr. 35. fg.</ls>	1
<ls n="Chr.">240,27 fgg.</ls>	1
<ls n="Chr.">29,15. fgg.</ls>	1
3 matches for "[0-9] " in buffer: chr_instances.txt
  -- <ls n="Chr.">34,10 ff.</ls>
    'ff.' -> 'fgg.'  typo 
   -- <ls n="Chr.">240,29 fg.</ls>
    '240,29 fg.' -> '240,29. fg.'  typo
   -- <ls n="Chr.">240,27 fgg.</ls>
    '240,27 fgg.' -> '240,27. fgg.'  typo
45 matches for "<ls>Chr. .*? " 
956 matches for '<ls n="Chr.">.*? '
  <ls n="Chr.">59,3. 7</ls>

26 matches for "\.<"
   ff.</ls> (1)
   fg.</ls> (6)
   fgg.</ls> (19)  (+ 19 6 1) = 26


Transformation examples:
---
old: <ls n="Chr.">27,24. 28,3</ls>
new: <ls n="Chr.">27,24</ls>. <ls n="Chr.">28,3</ls>
---
old: <ls n="Chr.">271,14. 21</ls>
new: <ls n="Chr.">271,14</ls>. <ls n="Chr. 271,">21</ls>
---
old: <ls>Chr. 35. fg.</ls>
new: ?
---
old: <ls n="Chr.">259,15. 272,13. 285,17. 288,16</ls>
new: <ls n="Chr.">259,15</ls>. <ls n="Chr.'272,13. 285,17. 288,16</ls>
--------------------------------------------------------------------
preliminary changes to pw
cp ../temp_pw_6.txt temp_pw_6a_edit.txt
manual edit of temp_pw_6a_edit.txt

---
<ls n="Chr.">34,10 ff.</ls>
<ls n="Chr.">34,10. fgg.</ls>

---
<ls n="Chr.">240,29 fg.</ls>
<ls n="Chr.">240,29. fg.</ls>
---
<ls n="Chr.">240,27 fgg.</ls>
<ls n="Chr.">240,27. fgg.</ls>

03-13-2024  5 more changes.  See change_6_6a.txt
---
# generate change file
python ../diff_to_changes_dict.py ../temp_pw_6.txt temp_pw_6a_edit.txt change_6_6a.txt
python ../updateByLine.py  ../temp_pw_6.txt change_6_6a.txt temp_pw_6a.txt
diff temp_pw_6a.txt temp_pw_6a_edit.txt  | wc -l
# 0 as expected
# remove unneeded temp_pw_6a_edit.txt
rm temp_pw_6a_edit.txt
--------------------------------------------------------------------
step1a
use temp_pw_6a.txt for input
Provide more 'classification' analysis particular to Chr.
python ls_instances1.py 'Chr.' temp_pw_6a.txt chr_instances1.txt
764912 from temp_pw_6a.txt
4546 distinct instances
5706 total instances
4546 lines written to chr_instances1.txt

x and y digit sequences
A1  242  <ls>Chr. x,y</ls>
A2 3296  <ls n="Chr.">x,y</ls> 
A3   22  <ls n="Chr.">x,y. F</ls>  F = fg. or fgg.
A4    8  <ls n="Chr. x">y</ls>
X1   45  <ls>Chr. Z</ls>  Z not specified
X2  933  <ls n="Chr.Z">W</ls> Z, W not specified

Our task is to 'expand' X types to a sequence of A types
--------------------------------------------------------------------

step2  expand the Xes into Bes
python ls_expand.py 'Chr.' chr_instances1.txt chr_expand.txt

4546 from chr_instances1.txt
4546 lines written to chr_expand.txt
A1  242
A2 3296
A3   22
A4    8
B1   44
X1    1   This is <ls>Chr. 351. fg.</ls> under kar. p. 351 is appendix
B2  933

https://babel.hathitrust.org/cgi/pt?id=hvd.32044086565637&seq=705
This 1877 version, correlates well with pw references.
Many scribbled 'extra' pages.

--------------------------------------------------------------------
step3
 # apply the expansions of chr_expand.txt to make changes to pw.txt
python ls_expand_make_change.py 'Chr.' chr_expand.txt temp_pw_6a.txt change_pw_6a_6b.txt

4546 from chr_expand.txt
764912 from temp_pw_6a.txt
943 lines changed
944 records written to change_pw_6a_6b.txt
check: len(a) = 5995 number of Chr. ls instances after change.
check fails: <ls>Chr. 351. fg.</ls>
check_instance_strings finds 1 non-standard strings

----
To apply these changes:
python ../updateByLine.py temp_pw_6a.txt change_pw_6a_6b.txt temp_pw_6b.txt
764912 lines read from temp_pw_6a.txt
764912 records written to temp_pw_6b.txt
943 change transactions from change_pw_6a_6b.txt

----------------------------
rerun instances1 on revised pw

python ls_instances1.py 'Chr.' temp_pw_6b.txt chr_instances1_revised.txt
764912 from temp_pw_6b.txt
4998 distinct instances
7168 total instances
4998 lines written to chr_instances1_revised.txt
A1  285
A2 4366
A3   25
A4  320
X1    1
X2    1

Note The X
764912 from temp_pw_6b.txt
4998 distinct instances
7168 total instances
4998 lines written to chr_instances1_revised.txt
A1  285
A2 4366
A3   25
A4  320
X1    1
X2    1

The two X items are in fact ok.
X1	<ls>Chr. 351. fg.</ls>	1
X2	<ls n="Chr. 241,">16. fgg.</ls>	1

We probably also want to mark <ab>fg.</ab> and <ab>fgg.</ab>.
This could be done globally (some are so marked, some are not).
