pw_5_work
continue alternate headword (k2) work.
03-05-2024 begin
Begin with Andhrabharati corrections comparing temp_pw_4.txt to his own work.
AB's issue comments begin at
 https://github.com/sanskrit-lexicon/PWK/issues/106#issuecomment-1978548962

AB's supporting files:

pwkvn_4.differences-1.metalines.and.header.lines.txt  (22)
pwkvn_4.differences-2.dhAtu.and.denominative.verbs.txt (93)

674022 L>200002
678906 L>201221 arD
(- 678906 674022) 4884
4888  This is the number in AB file
   
pwkvn_4.differences-3.splits.and.miscellaneous.txt  (75)
  {#X, Y#} -> {#X#}, {#Y#}


temp_pwkvn_4.CDSL.-prefix.splits.txt

-----------------------------------------------------
cp ../temp_pw_4.txt temp_pwkvn-4.cdsl.txt
# manually edit temp_pwkvn-4.cdsl.txt
  delete lines 1-674019  (the 'main' pw)
 90460 temp_pwkvn-4.cdsl.txt
 90893 temp_pwkvn_4.CDSL.-prefix.splits.txt  AB has added 433 lines

-----------
Metalines are the same in number 22611
comparision by count of <L>
grep '<L>' temp_pwkvn_4.CDSL.-prefix.splits.txt | wc -l
22611
grep '<L>' temp_pwkvn-4.cdsl.txt | wc -l
22611
----------
Metalines are in fact identical
# extract all the matalines in the two versions
grep '<L>' temp_pwkvn-4.cdsl.txt > temp_pwkvn-4.cdsl_L.txt
grep '<L>' temp_pwkvn_4.CDSL.-prefix.splits.txt > temp_pwkvn_4.CDSL.-prefix.splits_L.txt
# compare the metalines:
diff temp_pwkvn-4.cdsl_L.txt temp_pwkvn_4.CDSL.-prefix.splits_L.txt | wc -l
0  # no difference.
-------------------------
# simple diff of the two versions

diff temp_pwkvn-4.cdsl.txt temp_pwkvn_4.CDSL.-prefix.splits.txt > temp_diff_pwkvn_4_cdsl_ab.txt
wc -l temp_diff_pwkvn_4_cdsl_ab.txt
1261 temp_diff_pwkvn_4_cdsl_ab.txt

# The diffs are new records with <div n="p">
433 matches for "<div n="p"" in buffer: temp_pwkvn_4.CDSL.-prefix.splits.txt
# No <div n="p"> in pwkvn-4.cdsl
grep -E '<div n="p">' temp_pwkvn-4.cdsl.txt | wc -l
# 0

Note the 433 matches - This accounts for all the new lines!
-------------------------------
Let's see what other differences are present.
201221
cp temp_pwkvn_4.CDSL.-prefix.splits.txt temp_pwkvn_4.CDSL_nodiv.txt
Emacs regex-change: '\n<div n="p"> →  '
and save.

diff temp_pwkvn-4.cdsl.txt temp_pwkvn_4.CDSL_nodiv.txt > diff_pwkvn-4.cdsl_nodiv.txt
wc -l diff_pwkvn-4.cdsl_nodiv.txt
0 diff_pwkvn-4.cdsl_nodiv.txt
This accounts for all the differences.

------------------------------------------------------------------------
temp_pw_4a.txt
A concatenation of
a. the body part from temp_pw_4.txt and
b. temp_pwkvn_4.CDSL.-prefix.splits.txt

cp ../temp_pw_4.txt ../temp_pw_4a.txt
python make_4a.py ../temp_pw_4.txt temp_pwkvn_4.CDSL.-prefix.splits.txt ../temp_pw_4a.txt
# check line counts
wc -l ../temp_pw_4.txt ../temp_pw_4a.txt
  764479 ../temp_pw_4.txt
  764912 ../temp_pw_4a.txt
 (- 764912 764479) = 433 (As expected)
------------------------------------------------------------------------
temp_pw_5.txt
Constructed from ../temp_pw_4a.txt in 3 steps.

-- 01
cp ../temp_pw_4a.txt  ../temp_pw_4a1.txt
manual edit of temp_pw_4a1.txt.
Apply Changes per pwkvn_4.differences-1.metalines.and.header.lines.txt  (22)

# construct change file
python ../diff_to_changes_dict.py ../temp_pw_4a.txt  ../temp_pw_4a1.txt temp_change_4_5_01.txt

touch ../change_4a_5.txt
# manual insert temp_change_4_5_01.txt into change_4a_5.txt

# recompute temp_pw_5.txt from temp_pw_4a.txt
cd ../
python updateByLine.py temp_pw_4a.txt change_4a_5.txt temp_pw_5.txt
34 change transactions from change_4a_5.txt

-- 02
 Changes per pwkvn_4.differences-2.dhAtu.and.denominative.verbs.txt

# this is complicated for various reasons.
# the 'temp_unused_groups_02.txt have (about 30) have to be done manually
python make_change_01.py ../temp_pw_5.txt pwkvn_4.differences-2.dhAtu.and.denominative.verbs.txt temp_change_4_5_02.txt 
764912 from ../temp_pw_5.txt
372 from pwkvn_4.differences-2.dhAtu.and.denominative.verbs.txt
102 records written to temp_change_4_5_02.txt

# manual edit of temp_change_4_5_02.txt
 compare with pwkvn_4.differences-2
 a) remove a few in temp_change_4_5_02.txt
 b) accept 5 more ('i' see below)
# manual insert temp_change_4_5_02.txt into change_4a_5.txt

# recompute temp_pw_5.txt from temp_pw_4a.txt
cd ../
python updateByLine.py temp_pw_4a.txt change_4a_5.txt temp_pw_5.txt
132 change transactions from change_4a_5.txt

AB missed these
<L>204132<pc>3-256-b<k1>i<k2>3. i ?
<L>205418<pc>4-296-b<k1>i<k2>3. i ?
<L>206831<pc>5-249-c<k1>i<k2>3. i ?
<L>208655<pc>6-298-b<k1>i<k2>3. i  ?
<L>214506<pc>7-320-d<k1>i<k2>3. i  ?

-- 03
 Changes per pwkvn_4.differences-3.splits.and.miscellaneous.txt

# this is complicated for various reasons.
# the 'temp_unused_groups_02.txt have (about 30) have to be done manually
python make_change_03.py ../temp_pw_5.txt pwkvn_4.differences-3.splits.and.miscellaneous.txt temp_change_4_5_03.txt 
nit_ab_changes: 75 groups found
76 records written to temp_change_4_5_03.txt

# manual edit of temp_change_4_5_03.txt
 compare with pwkvn_4.differences-3
 many manual changes required due to <div n="p"/>
# manual insert temp_change_4_5_03.txt into change_4a_5.txt

# recompute temp_pw_5.txt from temp_pw_4a.txt
cd ../
python updateByLine.py temp_pw_4a.txt change_4a_5.txt temp_pw_5.txt
218 change transactions from change_4a_5.txt

Note: <L>222590<pc>7-389-d<k1>riktI
  Question !√{#riktI#}.  cf. <L>94190<pc>5-189-b<k1>riktI

