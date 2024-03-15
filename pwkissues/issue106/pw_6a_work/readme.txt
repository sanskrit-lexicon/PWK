pw_6a_work
continue alternate headword (k2) work.
03-14-2024 begin

AB's supporting file:

readme.AB.remarks.txt
  comments by AB on items in ../pw_6_work/readme.txt


cp readme.AB.remarks.txt temp_readme.AB.remarks.txt
cp ../change_5_6.txt temp_change_5_6.txt
Review and edit  temp_readme.AB.remarks.txt
touch temp_change_6_6a.org
  Pre-changes based on remarks
cp ../temp_pw_6.txt temp_pw_6_work.txt
  Make changes manually to temp_pw_work.txt as noted in temp_change_6_6a.org

# generate ../change_6_6a.txt
python ../diff_to_changes_dict.py ../temp_pw_6.txt temp_pw_6_work.txt temp_change_6_6a.txt
7 changes written to temp_change_6_6a.txt
# insert into ../change_6_6a.txt

# generate ../temp_pw_6a.txt
764912 lines read from temp_pw_6.txt
764912 records written to temp_pw_6a.txt
7 change transactions from change_6_6a.txt

# remove pw_6a_work/temp_pw_6_work.txt (it is same as ../temp_pw_6a.txt)
NOTES to AB
---
;; And do we revert the few places where the sequence is recently changed to put the items in order?
JIM: NO, do not make print change to restore alph. order
---
<L>124385<pc>7-121-b<k1>sAradIya
 {#nAmamAlA#} -> {#°nAmamAlA#} in bbline  (the ° is needed, but missing in print
---
 <L>124169<pc>7-118-a<k1>sAmAnyABAvagranTa<k2>sAmAnyABAvagranTa, ⁅#sAmAnyA⁆°BAvawippanI, ⁅#sAmAnyA⁆°BAvarahasya
jim: The '#' is not needed in metaline

-----------------------------------------------------
TODO:
---
make mw print change
<L>124654<pc>7-124-c<k1>sAvairisole<k2>sAva_irisole
  sAva_irisole -> sAvairisole  slp1 does not need _ for hiatus
  Note: mw:   sAvaisirole  MW print change?
;; AB note: MW has erred!!
---
