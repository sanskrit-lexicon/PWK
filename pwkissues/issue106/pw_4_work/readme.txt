pw_4_work
Revise k2 based on {#X#} in bbline
02-27-2024 begin

touch change_3_4.txt
cp temp_pw_3.txt temp_pw_4.txt

1636 matches for "<k2>.*?," in buffer: temp_pw_4.txt
8570 matches for "{#.*?{#.*¦" in buffer: temp_pw_4.txt

Thus, there will be about 7000 changes to metaline k2.

-----------------------------------------------------------------------
# informal counts
1607 matches for "^{#[^#°]*#} und {#[^#°]*#}¦" in buffer: temp_pw_4.txt
91 matches for "^\*{#[^#°]*#} und {#[^#°]*#}¦" in buffer: temp_pw_4.txt
39 matches for "^{#[^#°]*#} und \*{#[^#°]*#}¦" in buffer: temp_pw_4.txt
407 matches for "^\*{#[^#°]*#} und \*{#[^#°]*#}¦" in buffer: temp_pw_4.txt
53 matches for "^<hom>[^<]*</hom> {#[^#°]*#} und {#[^#°]*#}¦" in buffer: temp_pw_4.txt
815 matches for "^{#[^#°]*#} und {#°[^#]*#}¦" in buffer: temp_pw_4.
4777 matches for "^\*?{#[^#]*#}[^{]* \*?{#[^#]*#}¦" in buffer: temp_pw_4.txt

-----------------------------------------------------------------------
temp_bbmulti_00.txt
format of temp_bbmulti_xx.txt:
3 tab-delimited fields
- lnum  line number within temp_pw_4.txt, 1,2,...
- ndeva count of {# in 'before' field
- beforeadj text before ¦ with adjustments 

python init_bbmulti.py ../temp_pw_4.txt temp_bbmulti_00.txt
764479 from ../temp_pw_4.txt
8569 lines written to temp_bbmulti_00.txt
103 records marked as √
NOTES:
761612	2	<hom>1</hom> {#sic#} {#siYca/ti#}

cp temp_bbmulti_00.txt bbmulti_00.txt

-----------------------------------------------------------------------
cp bbmulti_00.txt bbmulti_00a.txt
touch change_bbmulti_00a.txt

# manual edit of bbmulti_00a.txt
-----------------
01:  changes to root lines
python ../diff_to_changes_dict.py temp_bbmulti_00.txt bbmulti_00a.txt temp_change_bbmulti_00a_01.txt
18 changes written to temp_change_bbmulti_00a_01.txt
-----------------
02: 46 (a)misplaced '*'; (b) {#X Y#} -> {#X} {#Y}; drop alternate
cp bbmulti_00a.txt tempwork_bbmulti_00a.txt
# manual edit of tempwork_bbmulti_00a.txt
python ../diff_to_changes_dict.py bbmulti_00a.txt tempwork_bbmulti_00a.txt tempchange.txt
46 changes written to tempchange.txt

# insert tempchange.txt into change_bbmulti_00a.txt

# recalculate bbmulti_00a.txt

python ../updateByLine.py bbmulti_00.txt change_bbmulti_00a.txt bbmulti_00a.txt

NOTE: there are 6 cases with no altheadwords <TAB>1<TAB>
-----------------
03: 54 text between '#} and {#'
54 matches in 49 lines for "#} [^{*]" in buffer: bbmulti_00a.txt
cp bbmulti_00a.txt tempwork_bbmulti_00a.txt
# manual edit of tempwork_bbmulti_00a.txt
python ../diff_to_changes_dict.py bbmulti_00a.txt tempwork_bbmulti_00a.txt tempchange.txt
39 changes written to tempchange.txt

# insert tempchange.txt into change_bbmulti_00a.txt

# recalculate bbmulti_00a.txt

python ../updateByLine.py bbmulti_00.txt change_bbmulti_00a.txt bbmulti_00a.txt
103 change transactions from change_bbmulti_00a.txt

-----------------
04: {#A#} -> {#°A#} (55),
    {#I#} -> {#°I#} (30)
85 matches in 72 lines for "{#[IA]#}" in buffer: bbmulti_00a.txt

cp bbmulti_00a.txt tempwork_bbmulti_00a.txt
# manual edit of tempwork_bbmulti_00a.txt
python ../diff_to_changes_dict.py bbmulti_00a.txt tempwork_bbmulti_00a.txt tempchange.txt
72 changes written to tempchange.txt

# insert tempchange.txt into change_bbmulti_00a.txt

# recalculate bbmulti_00a.txt

python ../updateByLine.py bbmulti_00.txt change_bbmulti_00a.txt bbmulti_00a.txt
175 change transactions from change_bbmulti_00a.txt

------------------------------------------------------------
01: No °
Modify temp_pw_4.txt and change_3_4.txt in stages.
Also, construct helpers change_bbmulti_NN.txt

python make_change_bbk2.py 01 ../temp_pw_4.txt bbmulti_00a.txt temp_change_3_4_01.txt bbmulti_01.txt

764479 from ../temp_pw_4.txt
8569 from bbmulti_00a.txt
3453 lines written to bbmulti_01.txt
5116 changes
5117 records written to temp_change_3_4_01.txt
1221 cases No change to metaline
manually insert temp_change_3_4_01.txt into change_3_4.txt

# revise temp_pw_4.txt
python ../updateByLine.py ../temp_pw_3.txt ../change_3_4.txt ../temp_pw_4.txt
3895 change transactions from ../change_3_4.txt

------------------------------------------------------------
02: ° at end {#X°#}  131  This sometimes corresponds to MW 'ibc'

python make_change_bbk2.py 02 ../temp_pw_4.txt bbmulti_01.txt temp_change_3_4_02.txt bbmulti_02.txt

764479 from ../temp_pw_4.txt
3453 from bbmulti_01.txt
3322 lines written to bbmulti_02.txt
131 changes
132 records written to temp_change_3_4_02.txt
2 cases No change to metaline

# manually edit temp_change_3_4_02.txt
# manually insert temp_change_3_4_02.txt into change_3_4.txt
# A few bb-lines changed also
# revise temp_pw_4.txt
python ../updateByLine.py ../temp_pw_3.txt ../change_3_4.txt ../temp_pw_4.txt
4030 change transactions from ../change_3_4.txt

------------------------------------------------------------
03:  {#°ka#} 
462 matches in 458 lines for "{#°ka#}" in buffer: bbmulti_02.txt
Exclude cases with two (or more) °, then 418 cases of {#°ka#}

python make_change_bbk2.py 03 ../temp_pw_4.txt bbmulti_02.txt temp_change_3_4_03.txt bbmulti_03.txt
764479 from ../temp_pw_4.txt
3322 from bbmulti_02.txt
2904 lines written to bbmulti_03.txt
418 changes
419 records written to temp_change_3_4_03.txt
26 cases No change to metaline


# manually examine temp_change_3_4_03.txt -- seems ok
# manually insert temp_change_3_4_03.txt into change_3_4.txt

# revise temp_pw_4.txt
python ../updateByLine.py ../temp_pw_3.txt ../change_3_4.txt ../temp_pw_4.txt
4422 change transactions from ../change_3_4.txt

------------------------------------------------------------
04:  
162 matches in 149 lines for "{#°.#}" in buffer: bbmulti_03.txt
162 matches in 149 lines for "{#°[mAInsg]#}" in buffer: bbmulti_03.txt

python make_change_bbk2.py 04 ../temp_pw_4.txt bbmulti_03.txt temp_change_3_4_04.txt bbmulti_04.txt

764479 from ../temp_pw_4.txt
2904 from bbmulti_03.txt
2794 lines written to bbmulti_04.txt
110 changes
111 records written to temp_change_3_4_04.txt
16 cases No change to metaline

# manually edit temp_change_3_4_04.txt
#   finish corrections for those marked ?°
# manually insert temp_change_3_4_04.txt into change_3_4.txt

# revise temp_pw_4.txt
python ../updateByLine.py ../temp_pw_3.txt ../change_3_4.txt ../temp_pw_4.txt
4551 change transactions from ../change_3_4.txt


------------------------------------------------------------
05:
76 matches for "\(.\)a#} {#°\1A#}" in buffer: bbmulti_04.txt
50 matches in 49 lines for "\(.\)i#} {#°\1I#}" in buffer: bbmulti_04.txt

{#Xca#} {#°cA#}  {#XcA#}  c a single character

python make_change_bbk2.py 05 ../temp_pw_4.txt bbmulti_04.txt temp_change_3_4_05.txt bbmulti_05.txt
764479 from ../temp_pw_4.txt
2759 from bbmulti_04.txt
2622 lines written to bbmulti_05.txt
137 changes
138 records written to temp_change_3_4_05.txt
16 cases No change to metaline

# manually examine temp_change_3_4_05.txt.  Looks ok
# manually insert temp_change_3_4_05.txt into change_3_4.txt

# revise temp_pw_4.txt
python ../updateByLine.py ../temp_pw_3.txt ../change_3_4.txt ../temp_pw_4.txt
4672 change transactions from ../change_3_4.txt

------------------------------------------------------------
06: ends in accent
160 matches in 123 lines for "[/^\]#}" in buffer: bbmulti_05.txt

python make_change_bbk2.py 06 ../temp_pw_4.txt bbmulti_05.txt temp_change_3_4_06.txt bbmulti_06.txt
764479 from ../temp_pw_4.txt
2622 from bbmulti_05.txt
2499 lines written to bbmulti_06.txt
123 changes
124 records written to temp_change_3_4_06.txt

# manually edit temp_change_3_4_06.txt.
#  all require correction
# manually insert temp_change_3_4_06.txt into change_3_4.txt

# revise temp_pw_4.txt
python ../updateByLine.py ../temp_pw_3.txt ../change_3_4.txt ../temp_pw_4.txt
4795 change transactions from ../change_3_4.txt

------------------------------------------------------------
07: other accents  200+

python make_change_bbk2.py 07 ../temp_pw_4.txt bbmulti_06.txt temp_change_3_4_07.txt bbmulti_07.txt
764479 from ../temp_pw_4.txt
2499 from bbmulti_06.txt
2363 lines written to bbmulti_07.txt
136 changes
137 records written to temp_change_3_4_07.txt

# manually edit temp_change_3_4_07.txt.
#  all require correction
# manually insert temp_change_3_4_07.txt into change_3_4.txt

# revise temp_pw_4.txt
python ../updateByLine.py ../temp_pw_3.txt ../change_3_4.txt ../temp_pw_4.txt
4944 change transactions from ../change_3_4.txt

------------------------------------------------------------
08: remaining <hom> OR initial ° (ifc - at end of compound)
20 matches for "<hom>" in buffer: bbmulti_07.txt
12 matches for "	{#°" in buffer: bbmulti_07.txt

python make_change_bbk2.py 08 ../temp_pw_4.txt bbmulti_07.txt temp_change_3_4_08.txt bbmulti_08.txt

764479 from ../temp_pw_4.txt
2363 from bbmulti_07.txt
2331 lines written to bbmulti_08.txt
32 changes
33 records written to temp_change_3_4_08.txt
0
# manually edit temp_change_3_4_08.txt.
#  all require correction
# manually insert temp_change_3_4_08.txt into change_3_4.txt

# revise temp_pw_4.txt
python ../updateByLine.py ../temp_pw_3.txt ../change_3_4.txt ../temp_pw_4.txt
4977 change transactions from ../change_3_4.txt

------------------------------------------------------------
09: concatenation with first hw

python make_change_bbk2.py 09 ../temp_pw_4.txt bbmulti_08.txt temp_change_3_4_09.txt bbmulti_09.txt

764479 from ../temp_pw_4.txt
2331 from bbmulti_08.txt
2044 lines written to bbmulti_09.txt
287 changes
288 records written to temp_change_3_4_09.txt
43 cases No change to metaline

# manually edit temp_change_3_4_09.txt.
#  no changes required - spot check looks ok
# manually insert temp_change_3_4_09.txt into change_3_4.txt

# revise temp_pw_4.txt
python ../updateByLine.py ../temp_pw_3.txt ../change_3_4.txt ../temp_pw_4.txt
5222 change transactions from ../change_3_4.txt

------------------------------------------------------------
10: hw0 = XcY and hw = °cZ (which c is not in X or Y.
    hw -> XcZ
    This is usually right, but must be manually examined.

python make_change_bbk2.py 10 ../temp_pw_4.txt bbmulti_09.txt temp_change_3_4_10.txt bbmulti_10.txt
764479 from ../temp_pw_4.txt
2044 from bbmulti_09.txt
736 lines written to bbmulti_10.txt
1308 changes
1309 records written to temp_change_3_4_10.txt
92 cases No change to metaline


# manually edit temp_change_3_4_10.txt.
#  about 100 lines changed, including
#  a. typos
#  b. algorithm gives wrong answer
# manually insert temp_change_3_4_10.txt into change_3_4.txt

# revise temp_pw_4.txt
python ../updateByLine.py ../temp_pw_3.txt ../change_3_4.txt ../temp_pw_4.txt
6471 change transactions from ../change_3_4.txt


?
{#avyaktagaRita#} und {#°vIja#}¦
{#vEdyanATadIkzitIya#} <lex>n.</lex> und {#°nATaBew#}  BEw ? (cf. acc, mw)

------------------------------------------------------------
11: like 10, but instead of first char of hw, take first 4 characters

python make_change_bbk2.py 11 ../temp_pw_4.txt bbmulti_10.txt temp_change_3_4_11.txt bbmulti_11.txt

764479 from ../temp_pw_4.txt
736 from bbmulti_10.txt
533 lines written to bbmulti_11.txt
203 changes
204 records written to temp_change_3_4_11.txt
17 cases No change to metaline

# manually edit temp_change_3_4_11.txt.
#  examine all.  A few changes
# manually insert temp_change_3_4_11.txt into change_3_4.txt

# revise temp_pw_4.txt
python ../updateByLine.py ../temp_pw_3.txt ../change_3_4.txt ../temp_pw_4.txt
6664 change transactions from ../change_3_4.txt

------------------------------------------------------------
12: like 10, but instead of first char of hw, take first 3 characters

python make_change_bbk2.py 12 ../temp_pw_4.txt bbmulti_11.txt temp_change_3_4_12.txt bbmulti_12.txt
764479 from ../temp_pw_4.txt
533 from bbmulti_11.txt
466 lines written to bbmulti_12.txt
67 changes
68 records written to temp_change_3_4_12.txt
5 cases No change to metaline


# manually edit temp_change_3_4_12.txt.
#  examine all.  A few changes
# manually insert temp_change_3_4_12.txt into change_3_4.txt

# revise temp_pw_4.txt
python ../updateByLine.py ../temp_pw_3.txt ../change_3_4.txt ../temp_pw_4.txt
6730 change transactions from ../change_3_4.txt

------------------------------------------------------------
13: like 10, but instead of first char of hw, take first 2 characters

python make_change_bbk2.py 13 ../temp_pw_4.txt bbmulti_12.txt temp_change_3_4_13.txt bbmulti_13.txt

764479 from ../temp_pw_4.txt
466 from bbmulti_12.txt
441 lines written to bbmulti_13.txt
25 changes
26 records written to temp_change_3_4_13.txt
0 cases No change to metaline

# manually edit temp_change_3_4_13.txt.
#  examine all.  A few changes
# manually insert temp_change_3_4_13.txt into change_3_4.txt

# revise temp_pw_4.txt
python ../updateByLine.py ../temp_pw_3.txt ../change_3_4.txt ../temp_pw_4.txt
6760 change transactions from ../change_3_4.txt

------------------------------------------------------------
14: all the rest in bbmulti_13

python make_change_bbk2.py 14 ../temp_pw_4.txt bbmulti_13.txt temp_change_3_4_14.txt bbmulti_14.txt
764479 from ../temp_pw_4.txt
441 from bbmulti_13.txt
0 lines written to bbmulti_14.txt
441 changes
442 records written to temp_change_3_4_14.txt
1 cases No change to metaline

# manually edit temp_change_3_4_14.txt.
#  examine all.
# manually insert temp_change_3_4_14.txt into change_3_4.txt

# revise temp_pw_4.txt
python ../updateByLine.py ../temp_pw_3.txt ../change_3_4.txt ../temp_pw_4.txt
7254 change transactions from ../change_3_4.txt

THIS FINISHES THE bbline -> k2 work

---------------------------------------------------------
TODO:
5 matches for "a/i" in buffer: temp_pw_4.txt
25 matches for "a/u" in buffer: temp_pw_4.txt
a/i  -> E/
a/u  -> O/
example: 42272 new <L>9297<pc>1-108-c<k1>arkASvameDa<k2>arkASvameDa, °Da/u
 (corrected in 07 group)
---
print change: done
<L>117618<pc>7-019-b<k1>saMgItakOmudI
saMgInArAyaRa -> saMgItanArAyaRa
