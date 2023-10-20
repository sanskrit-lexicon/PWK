zoobot

10-12-2023 begin.

-----------------------
Part 1
remove spurious '_' in <bot>X</bot>

  This is an unwanted residue from previous work.
cp ../temp_pw_8.txt ../temp_pw_9.txt
cp ../temp_pw_ab_8.txt ../temp_pw_ab_9.txt

touch ../change_pw_9.txt

edit temp_pw_9.txt in Emacs
<bot\([^<]*\)_ → <bot\1  [replace _ by space]
278 changes in 262 lines.
---- generate change file
python ../diff_to_changes_dict.py ../temp_pw_8.txt ../temp_pw_9.txt temp_change_pw_9_1.txt
262 changes written to temp_change_pw_9_1.txt

# manual insert temp_change_pw_9_1.txt into change_pw_9.txt
# check
python updateByLine.py temp_pw_8.txt change_pw_9.txt temp.txt
diff temp_pw_9.txt temp.txt | wc -l
# 0 expected
-----------------------
Resolve differences in count of '<bot*?</bot> between temp_pw_9.txt and temp_pw_ab_9.txt
Note: forms <bot>X</bot> and <bot n="T">Y</bot>

Part 2: counts of bot tags
Revise so both temp_pw_9 and temp_pw_ab_9 have same count of 'bot' tags.

temporary copies:
cp temp_pw_9.txt temp_pw_9_work.txt
cp temp_pw_ab_9.txt temp_pw_ab_9_work.txt

python ../ablists/regex_compare_texts_count1.py '<bot>.*?</bot>' ../temp_pw_9_work.txt ../temp_pw_ab_9_work.txt temp.org
# 18 cases written to temp.org

# manual edit ../temp_pw_9_work.txt, ../temp_pw_ab_9_work.txt to resolve differences.

---- Now handle the <bot n="T">X</bot> cases
python ../ablists/regex_compare_texts_count1.py '<bot.*?</bot>' ../temp_pw_9_work.txt ../temp_pw_ab_9_work.txt temp1.org
manual edit ../temp_pw_9_work.txt, ../temp_pw_ab_9_work.txt to resolve differences

../
python diff_to_changes_dict.py temp_pw_9.txt temp_pw_9_work.txt zoobot/temp_change_pw_9_2.txt
# 61 lines changed
# manual insert zoobot/temp_change_pw_9_2.txt into change_pw_9.txt

python updateByLine.py temp_pw_8.txt change_pw_9.txt temp_pw_9.txt
# 323 lines changed
# check
diff temp_pw_9.txt temp_pw_9_work.txt | wc -l
# 0, as expected.

-----------------------
zoo tag.
Only 2 instances.
Same in temp_pw_9.txt as in temp_pw_ab_9.txt
No work required.
-----------------------
resolve textual differences in <bot> tags.
Part 3: intervening 'oder'
bot tags ALWAYS occur within italic text.
There are numerous cases of form '<bot>X y oder z</bot>.
In these, the 'oder' text is NOT italic  (conclusion based on sample of instances).
These are recoded to change the italic text markup
Example:
old: {%<bot>Sida cordifolia oder rhombifolia</bot>%}
new: {%<bot>Sida cordifolia</bot>%} oder {%<bot>rhombifolia</bot>%}

cp temp_pw_9.txt temp_pw_9_work.txt
cp temp_pw_ab_9.txt temp_pw_ab_9_work.txt

These changes are made to both temp_pw_9_work.txt and temp_pw_ab_9_work.txt.
Changes made manually in emacs:
<bot>\([^<%]*\) oder  → <bot>\1%} oder {%<bot>
temp_pw_9_work.txt: 30
temp_pw_ab_9_work.txt: 147

Generate change files and revise temp_pw_9 and temp_pw_ab_9

python diff_to_changes_dict.py temp_pw_9.txt temp_pw_9_work.txt zoobot/temp_change_pw_9_3.txt
30 changes 
# manual insert temp_change_pw_9_3.txt into change_pw_9.txt
# regen temp_pw_9.txt
python updateByLine.py temp_pw_8.txt change_pw_9.txt temp_pw_9.txt
# 353 lines changed
# check
diff temp_pw_9.txt temp_pw_9_work.txt | wc -l
# 0, as expected

python diff_to_changes_dict.py temp_pw_ab_9.txt temp_pw_ab_9_work.txt zoobot/temp_change_pw_ab_9_3.txt
# manual insert temp_change_pw_ab_9_3.txt into change_pw_ab_9.txt
# regen temp_pw_ab_9.txt
python updateByLine.py temp_pw_ab_8.txt change_pw_ab_9.txt temp_pw_ab_9.txt
# 148 lines changed
# check
diff temp_pw_ab_9.txt temp_pw_ab_9_work.txt | wc -l
# 0, as expected
-----------------------------------------------------
Part 4
Now, we have to re-align the counts.

# for convenience, also make work1 versions with temporary'* <L>' markup for the cases that differ.

python ../ablists/regex_compare_texts_count1.py '<bot>.*?</bot>' ../temp_pw_9.txt ../temp_pw_ab_9.txt temp.org ../temp_pw_9_work1.txt ../temp_pw_ab_9_work1.txt

113 cases written to temp.org
write_extra  682608 lines written to ../temp_pw_9_work1.txt
write_extra  674189 lines written to ../temp_pw_ab_9_work1.txt

# manual changes to ./temp_pw_9_work1.txt ../temp_pw_ab_9_work1.txt
# 
# with help from temp.org
# remove temporary markup ('* <L>' -> <L>)
# Count again: did we get all of them?
python ../ablists/regex_compare_texts_count1.py '<bot>.*?</bot>' ../temp_pw_9_work1.txt ../temp_pw_ab_9_work1.txt temp2.org
# 0 cases  -- we have them all!

Generate change files for part 4
 and revise temp_pw_9 and temp_pw_ab_9

python diff_to_changes_dict.py temp_pw_9.txt temp_pw_9_work1.txt zoobot/temp_change_pw_9_4.txt118 changes 
# manual insert temp_change_pw_9_4.txt into change_pw_9.txt
# regen temp_pw_9.txt
python updateByLine.py temp_pw_8.txt change_pw_9.txt temp_pw_9.txt
# 471 lines changed
# check
diff temp_pw_9.txt temp_pw_9_work1.txt | wc -l
# 0, as expected

python diff_to_changes_dict.py temp_pw_ab_9.txt temp_pw_ab_9_work1.txt zoobot/temp_change_pw_ab_9_4.txt
1 change
# manual insert temp_change_pw_ab_9_4.txt into change_pw_ab_9.txt
# regen temp_pw_ab_9.txt
python updateByLine.py temp_pw_ab_8.txt change_pw_ab_9.txt temp_pw_ab_9.txt
# 149 lines changed
# check
diff temp_pw_ab_9.txt temp_pw_ab_9_work1.txt | wc -l
# 0, as expected
-----------------------------------------------------

-------------------------------------------------------------
Part 5:  align text contents for bot tags

Look for differences in bot tags, write optional work1 files
 to facilitate comparisons.
python ../ablists/regex_compare_texts1.py '<bot.*?</bot>' ../temp_pw_9_work.txt ../temp_pw_ab_9_work.txt temp.org ../temp_pw_9_work1.txt ../temp_pw_ab_9_work1.txt
238 cases written to temp.org
write_extra  682608 lines written to ../temp_pw_9_work1.txt
write_extra  674189 lines written to ../temp_pw_ab_9_work1.txt

Manual changes.

Remove temporary markup in work1, save as work
# any differences remain?
python ../ablists/regex_compare_texts1.py '<bot.*?</bot>' ../temp_pw_9_work.txt ../temp_pw_ab_9_work.txt temp.org 

7 cases remain, per temp.org
Correct the work file.
Rerun
python ../ablists/regex_compare_texts1.py '<bot.*?</bot>' ../temp_pw_9_work.txt ../temp_pw_ab_9_work.txt temp.org
0 cases written to temp.org
Done!

#
# Make change file(s) for part 5 for pw_9 

python diff_to_changes_dict.py temp_pw_9.txt temp_pw_9_work.txt zoobot/temp_change_pw_9_5.txt
# manual insert temp_change_pw_9_5.txt into change_pw_9.txt
# regen temp_pw_9.txt
python updateByLine.py temp_pw_8.txt change_pw_9.txt temp_pw_9.txt
# 726 lines changed.
# check
diff temp_pw_9.txt temp_pw_9_work.txt | wc -l
# 0, as expected

#
# Make change file(s) for part 5 for pw_ab_9 

python diff_to_changes_dict.py temp_pw_ab_9.txt temp_pw_ab_9_work.txt zoobot/temp_change_pw_ab_9_5.txt
1 change
# manual insert temp_change_pw_ab_9_5.txt into change_pw_ab_9.txt
# regen temp_pw_ab_9.txt
python updateByLine.py temp_pw_ab_8.txt change_pw_ab_9.txt temp_pw_ab_9.txt
# 150 lines changed
# check
diff temp_pw_ab_9.txt temp_pw_ab_9_work.txt | wc -l
# 0, as expected
--------------------------------------------------

Part 6:
Asterisk to precede {% and {#  (beginning of italic text or Devanagari text.
This is the rule for AB version.
---
grep -E '[*]{%' temp_pw_ab_9.txt | wc -l
8612 cases
grep -E '{%[*]' temp_pw_ab_9.txt | wc -l
1 case   ---- probably an oversight. -- will change
grep -E '[*]{#' temp_pw_ab_9.txt | wc -l
28493
grep -E '{#[*]' temp_pw_ab_9.txt | wc -l
0
---
But cdsl normally has such asterisks 'inside'
grep -E '[*]{%' temp_pw_9.txt | wc -l
50
grep -E '{%[*]' temp_pw_9.txt | wc -l
8558
grep -E '[*]{#' temp_pw_9.txt | wc -l
11
grep -E '{#[*]' temp_pw_9.txt | wc -l
29681

cp temp_pw_9.txt temp_pw_9a.txt
Make changes to temp_pw_9a
In emacs, edit temp_pw_9a.txt:
 - '{%*' -> '*{%'
 - '{#*' -> '*{#'
Now,
grep -E '[*]{%' temp_pw_9a.txt | wc -l
8608
grep -E '{%[*]' temp_pw_9a.txt | wc -l
0
grep -E '[*]{#' temp_pw_9a.txt | wc -l
29691
grep -E '{#[*]' temp_pw_9a.txt | wc -l
0

----

Handle the 1 case in temp_pw_ab_9.txt
cp temp_pw_ab_9.txt temp_pw_ab_9_work.txt
Edit manually temp_pw_ab_9_work.txt
Change one case '{%*'

python diff_to_changes_dict.py temp_pw_ab_9.txt temp_pw_ab_9_work.txt zoobot/temp_change_pw_ab_9_6.txt
1 change
# manual insert temp_change_pw_ab_9_6.txt into change_pw_ab_9.txt
# regen temp_pw_ab_9.txt
python updateByLine.py temp_pw_ab_8.txt change_pw_ab_9.txt temp_pw_ab_9.txt
# 151 lines changed
# check
diff temp_pw_ab_9.txt temp_pw_ab_9_work.txt | wc -l
# 0, as expected

--------------------------
grep -E '[*]{#' temp_pw_ab_9.txt | wc -l
28493
grep -E '[*]{#' temp_pw_9a.txt | wc -l
29691
grep -E '[*]{%' temp_pw_ab_9.txt | wc -l
8613
grep -E '[*]{%' temp_pw_9a.txt | wc -l
8608

Resolve the '*{%' differences

cp temp_pw_9a.txt temp_pw_9a_work.txt
cp temp_pw_ab_9.txt temp_pw_ab_9_work.txt

python ../ablists/regex_compare_texts_count1.py '[*]{%' ../temp_pw_9a_work.txt ../temp_pw_ab_9_work.txt temp2.org
9 cases written to temp2.org
# manual edit of ../temp_pw_9a_work.txt and ../temp_pw_ab_9_work.txt to resolve differences.

python ../ablists/regex_compare_texts_count1.py '{%[^%]*{#' ../temp_pw_9a_work.txt ../temp_pw_ab_9_work.txt temp2.org

No changes to temp_pw_ab_9_work.txt

cp temp_pw_9a_work.txt temp_pw_9b.txt
# changes from 9a to 9b
touch change_pw_9b.txt

python diff_to_changes_dict.py temp_pw_9a.txt temp_pw_9a_work.txt zoobot/temp_change_pw_9b_1.txt
15 changes

# manual insert zoobot/temp_change_pw_9b_1.txt into change_pw_9b.txt
# generate temp_pw_9b.txt
python updateByLine.py temp_pw_9a.txt change_pw_9b.txt temp_pw_9b.txt
# 16 lines changed
# check
diff temp_pw_9b.txt temp_pw_9a_work.txt
# 0 as expected
-----------------------------
Preliminary look at the '{#X#}' differences

# first, the count differences
cp temp_pw_9b.txt temp_pw_9b_work.txt
cp temp_pw_ab_9.txt temp_pw_ab_9_work.txt

python ../ablists/regex_compare_texts_count1.py '{#.*?#}' ../temp_pw_9b_work.txt ../temp_pw_ab_9_work.txt temp2.org ../temp_pw_9b_work1.txt  ../temp_pw_ab_9_work1.txt
596 cases written to temp2.org
These differences seem to be mainly coding of the first line of entries with
 multiple headwords.
Example:
<L>863<pc>1010-3<k1>aGnya
cdsl: {#a/Gnya#}¦ und {#a/Gnia, aGnya/#} und {#agnia/#} <lex>m.</lex> {%Stier;%} <lex>f.</lex> {#A#} {%Kuh%}.

ab:   {#a/Gnya#} und {#a/Gnia#}, {#aGnya/#} und {#agnia/#}¦ <lex>m.</lex> {%Stier;%} <lex>f.</lex> {#A#} {%Kuh%}.


python ../ablists/regex_compare_texts_count2.py '{#.*?#}' '¦' ../temp_pw_9b_work.txt ../temp_pw_ab_9_work.txt temp2.org ../temp_pw_9b_work1.txt  ../temp_pw_ab_9_work1.txt
624 cases
----
This presentation could be used to make corrections manually.
This seems wasteful.
Better to simply copy such AB lines to CDSL
----
Part 1 for {#X#} resolution

python change_multiple_headwords.py ../temp_pw_9b.txt ../temp_pw_ab_9.txt temp_change_pw_9c_1.txt
5478 changes written to temp_change_pw_9c_1.txt

touch change_pw_9c.txt

# manually insert zoobot/temp_change_pw_9c_1.txt into change_pw_9c.txt
# initialize temp_pw_9c.txt
python updateByLine.py temp_pw_9b.txt change_pw_9c.txt temp_pw_9c.txt
# 5478 lines changed.

---------------------------------
continue the comparison of number of {#X#} fragments
cp temp_pw_9c.txt temp_pw_9c_work.txt
cp temp_pw_ab_9.txt temp_pw_ab_9_work.txt

python ../ablists/regex_compare_texts_count1.py '{#.*?#}' ../temp_pw_9c_work.txt ../temp_pw_ab_9_work.txt temp1.org ../temp_pw_9c_work1.txt  ../temp_pw_ab_9_work1.txt
# 532 cases written to temp1.org

Try to identify subcase patterns that can be resolved en-masse

---------------------------------
Part 2:
Eliminate = character within {#X#}
edit temp_pw_9c_work.txt
manual change: {#X = Y#} -> {#X#} = {#Y#}
{#\([^ #]+\) = \([^ #]+\)#} -> {#\1#} = {#\2#}

Generate change transactions:
python diff_to_changes_dict.py temp_pw_9c.txt temp_pw_9c_work.txt zoobot/temp_change_pw_9c_2.txt
50 changes written to zoobot/temp_change_pw_9c_2.txt

# manual insert zoobot/temp_change_pw_9c_2.txt into change_pw_9c.txt
# generate temp_pw_9c.txt
python updateByLine.py temp_pw_9b.txt change_pw_9c.txt temp_pw_9c.txt
# 5528 lines changed
# check
diff temp_pw_9c.txt temp_pw_9c_work.txt
# 0 as expected
--------------------------------
Part 3:
 {#X; Y#} -> {#X}; {#Y#}  
edit temp_pw_9c_work.txt
Manual change: {#\([^ #]+\); \([^ #]+\)#} -> {#\1#}; {#\2#}

python ../ablists/regex_compare_texts_count1.py '{#.*?#}' ../temp_pw_9c_work.txt ../temp_pw_ab_9_work.txt temp1.org ../temp_pw_9c_work1.txt  ../temp_pw_ab_9_work1.txt

Generate change transactions:
python diff_to_changes_dict.py temp_pw_9c.txt temp_pw_9c_work.txt zoobot/temp_change_pw_9c_3.txt
9 changes written to zoobot/temp_change_pw_9c_3.txt

# manual insert zoobot/temp_change_pw_9c_3.txt into change_pw_9c.txt
# generate temp_pw_9c.txt
python updateByLine.py temp_pw_9b.txt change_pw_9c.txt temp_pw_9c.txt
# 5537 lines changed
# check
diff temp_pw_9c.txt temp_pw_9c_work.txt
# 0 as expected

--------------------------------
Part 4:
 #} - {# -> —
 #} — {#  -> —
 
manual edit temp_pw_9c_work.txt

python ../ablists/regex_compare_texts_count1.py '{#.*?#}' ../temp_pw_9c_work.txt ../temp_pw_ab_9_work.txt temp1.org ../temp_pw_9c_work1.txt  ../temp_pw_ab_9_work1.txt
# cases written to temp1.org

# Generate change transactions:
python diff_to_changes_dict.py temp_pw_9c.txt temp_pw_9c_work.txt zoobot/temp_change_pw_9c_4.txt
63 changes written to zoobot/temp_change_pw_9c_4.txt

# manual insert zoobot/temp_change_pw_9c_4.txt into change_pw_9c.txt
# generate temp_pw_9c.txt
python updateByLine.py temp_pw_9b.txt change_pw_9c.txt temp_pw_9c.txt
# 5600 lines changed
# check
diff temp_pw_9c.txt temp_pw_9c_work.txt
# 0 as expected

# 1 case for ab_9
manual edit temp_pw_ab_9_work

# Generate change transactions:
python diff_to_changes_dict.py temp_pw_ab_9.txt temp_pw_ab_9_work.txt zoobot/temp_change_pw_ab_9_7.txt
1 changes written to zoobot/temp_change_pw_ab_9_7.txt

# manual insert zoobot/temp_change_pw_ab_9_7.txt into change_pw_ab_9.txt

# generate temp_pw_ab_9.txt
python updateByLine.py temp_pw_ab_8.txt change_pw_ab_9.txt temp_pw_ab_9.txt
# 152 lines changed
# check
diff temp_pw_ab_9.txt temp_pw_ab_9_work.txt
# 0 as expected

---------------------------------------------
Part 5:

python ../ablists/regex_compare_texts_count1.py '{#.*?#}' ../temp_pw_9c_work.txt ../temp_pw_ab_9_work.txt temp1.org ../temp_pw_9c_work1.txt  ../temp_pw_ab_9_work1.txt
# 471 cases written to temp1.org

{#X, *Y#} -> {#X}, *{#Y#}
manual edit temp_pw_ab_9_work.txt
Change:
{#\([^# ,]*\), [*]\([^# ,]*\)#} -> {#\1#}, *{#\2#}

# Generate change transactions:
python diff_to_changes_dict.py temp_pw_9c.txt temp_pw_9c_work.txt zoobot/temp_change_pw_9c_5.txt
60 changes written to zoobot/temp_change_pw_9c_5.txt

# manual insert zoobot/temp_change_pw_9c_5.txt into change_pw_9c.txt
# generate temp_pw_9c.txt
python updateByLine.py temp_pw_9b.txt change_pw_9c.txt temp_pw_9c.txt
# 5660 lines changed
# check
diff temp_pw_9c.txt temp_pw_9c_work.txt
# 0 as expected
---------------------------------------------
Part 6: {#X; Y#} -> {#X#}; {#Y#}

edit temp_pw_9c_work.txt
Manual changes:
{#\([^#;]*\); \([^#]*\)#} -> {#\1#}; {#\2#}

python ../ablists/regex_compare_texts_count1.py '{#.*?#}' ../temp_pw_9c_work.txt ../temp_pw_ab_9_work.txt temp1.org ../temp_pw_9c_work1.txt  ../temp_pw_ab_9_work1.txt
# 421 cases written to temp1.org

{#X (Y)#}
11 matches in 10 lines for "{#\([^ #]*\) (\([^ #]*)\)#}" in buffer: temp_pw_ab_9_work1.txt
oversight?
138 matches in 136 lines for "{#\([^ #]*\) (\([^ #]*)\)#}" in buffer: temp_pw_9c_work1.txt

# manual changes of temp_pw_9c_work1.txt
{#X (Y)#} -> {#X#} ({#Y#})   
{#\([^ #]*\) (\([^ #]*)\)#}  -> {#\1#} ({#\2#})   138 changes
# manual correction back for the 11 {#X (Y)#} of pw_ab_9   
# remove temp markup (* <L> -> <L>) in temp_pw_9c_work1.txt, and save as temp_pw_9c_work.txt.

# Generate change transactions:
python diff_to_changes_dict.py temp_pw_9c.txt temp_pw_9c_work.txt zoobot/temp_change_pw_9c_6.txt
143 changes written to zoobot/temp_change_pw_9c_6.txt

# manual insert zoobot/temp_change_pw_9c_6.txt into change_pw_9c.txt
# generate temp_pw_9c.txt
python updateByLine.py temp_pw_9b.txt change_pw_9c.txt temp_pw_9c.txt
# 5803 lines changed
# check
diff temp_pw_9c.txt temp_pw_9c_work.txt
# 0 as expected

---------------------------------------------------------------
Part 7: 

python ../ablists/regex_compare_texts_count1.py '{#.*?#}' ../temp_pw_9c_work.txt ../temp_pw_ab_9_work.txt temp1.org ../temp_pw_9c_work1.txt  ../temp_pw_ab_9_work1.txt
# 309 cases written to temp1.org

edit temp_pw_9c_work.txt

Remove semicolon within {#X#}  8

Also, '#}.{# ' -> '#}. {#'  78
)) -> )  19
)#}) → #})  120+
---------
TODO:
---
print change at <L>13620<pc>1161-1<k1>Agantuka
---
L>48240<pc>3059-2<k1>tvat  <div> on new line
---
ya  many {#X#} {#Y#}  why all separately marked? (why not {#X y#} ?)
---------
ODD:
<L>27428<pc>2060-1<k1>kAlIvidyA<k2>kAlIvidyA<e>107
{#kAlIvidyA#}¦ {#svacCandasaMgrahaH#} <ab>desgl.</ab>
---
<L>42819<pc>2267-3<k1>jinamantraSAstra<k2>jinamantraSAstra<e>100
{#jinamantraSAstrastotrAdi#}¦
---
<L>71380<pc>4144-2<k1>pratiyogijYAnasya<k2>pratiyogijYAnasya<e>107
{#pratiyogijYAnasya_hetutvaKaRqanam#}¦
---
<L>71382<pc>4144-2<k1>pratiyogyanaDikaraRe<k2>pratiyogyanaDikaraRe<e>107
{#pratiyogyanaDikaraRe_nASasyotpattinirAsaH#}¦
---
<L>113197<pc>6245-3<k1>SukamahimnaH<k2>SukamahimnaH<e>107
{#SukamahimnaH_stavaH#}¦
---
----------------

# Generate change transactions for temp_pw_9c
# remove temp markup (* <L> -> <L>) in temp_pw_9c_work1.txt, and save as temp_pw_9c_work.txt.
python diff_to_changes_dict.py temp_pw_9c.txt temp_pw_9c_work.txt zoobot/temp_change_pw_9c_7.txt
566 changes written to zoobot/temp_change_pw_9c_7.txt

# manual insert zoobot/temp_change_pw_9c_7.txt into change_pw_9c.txt
# generate temp_pw_9c.txt
python updateByLine.py temp_pw_9b.txt change_pw_9c.txt temp_pw_9c.txt
# 6369 lines changed
# check
diff temp_pw_9c.txt temp_pw_9c_work.txt
# 0 as expected

# Generate change transactions for temp_pw_ab_9
# remove temp markup (* <L> -> <L>) in temp_pw_ab_9_work1.txt, and save as temp_pw_ab_9_work.txt.
python diff_to_changes_dict.py temp_pw_ab_9.txt temp_pw_ab_9_work.txt zoobot/temp_change_pw_ab_9_8.txt
2 changes written to zoobot/temp_change_pw_ab_9_8.txt

# manual insert zoobot/temp_change_pw_ab_9_8.txt into change_pw_ab_9.txt
# generate temp_pw_ab_9.txt
python updateByLine.py temp_pw_ab_8.txt change_pw_ab_9.txt temp_pw_ab_9.txt
# 154 lines changed
# check
diff temp_pw_ab_9.txt temp_pw_ab_9_work.txt | wc -l
# 0 as expected

--------------------------------------------------------------------
Part 8
Let's see what remains to resolve count differences

python ../ablists/regex_compare_texts_count1.py '{#.*?#}' ../temp_pw_9c_work.txt ../temp_pw_ab_9_work.txt temp2.org ../temp_pw_9c_work1.txt  ../temp_pw_ab_9_work1.txt
15 cases written to temp2.org

# manual edit of temp_pw_9c_work1.txt

# Generate change transactions for temp_pw_9c
# remove temp markup (* <L> -> <L>) in temp_pw_9c_work1.txt, and save as temp_pw_9c_work.txt.
python diff_to_changes_dict.py temp_pw_9c.txt temp_pw_9c_work.txt zoobot/temp_change_pw_9c_8.txt
18 changes written to zoobot/temp_change_pw_9c_8.txt

# manual insert zoobot/temp_change_pw_9c_.txt into change_pw_9c.txt
# generate temp_pw_9c.txt
python updateByLine.py temp_pw_9b.txt change_pw_9c.txt temp_pw_9c.txt
# 6387 lines changed
# check
diff temp_pw_9c.txt temp_pw_9c_work.txt
# 0 as expected

Are there more?

python ../ablists/regex_compare_texts_count1.py '{#.*?#}' ../temp_pw_9c_work.txt ../temp_pw_ab_9_work.txt temp3.org
4 cases
# manual edit temp_pw_9c_work.txt
python diff_to_changes_dict.py temp_pw_9c.txt temp_pw_9c_work.txt zoobot/temp_change_pw_9c_9.txt
6 changes written to zoobot/temp_change_pw_9c_9.txt

# manual insert zoobot/temp_change_pw_9c_9.txt into change_pw_9c.txt
# generate temp_pw_9c.txt
python updateByLine.py temp_pw_9b.txt change_pw_9c.txt temp_pw_9c.txt
# 6393 lines changed
# check
diff temp_pw_9c.txt temp_pw_9c_work.txt
# 0 as expected

python ../ablists/regex_compare_texts_count1.py '{#.*?#}' ../temp_pw_9c_work.txt ../temp_pw_ab_9_work.txt temp3.org
0 changes !

----------------------------------------------
Part 10:  parentheses within devanagari text
{#[^ #]*[()][^#]*#}

python ../ablists/regex_compare_texts_count1.py '{#[^ #]*[()][^#]*#}' ../temp_pw_9c_work.txt ../temp_pw_ab_9_work.txt temp1.org ../temp_pw_9c_work1.txt  ../temp_pw_ab_9_work1.txt
124 cases written to temp1.org

# Generate change transactions for temp_pw_9c
# remove temp markup (* <L> -> <L>) in temp_pw_9c_work1.txt, and save as temp_pw_9c_work.txt.
python diff_to_changes_dict.py temp_pw_9c.txt temp_pw_9c_work.txt zoobot/temp_change_pw_9c_10.txt
145 changes written to zoobot/temp_change_pw_9c_10.txt

# manual insert zoobot/temp_change_pw_9c_10.txt into change_pw_9c.txt
# generate temp_pw_9c.txt
python updateByLine.py temp_pw_9b.txt change_pw_9c.txt temp_pw_9c.txt
# 6538 lines changed
# check
diff temp_pw_9c.txt temp_pw_9c_work.txt
# 0 as expected

# Generate change transactions for temp_pw_ab_9
# remove temp markup (* <L> -> <L>) in temp_pw_ab_9_work1.txt, and save as temp_pw_ab_9_work.txt.
python diff_to_changes_dict.py temp_pw_ab_9.txt temp_pw_ab_9_work.txt zoobot/temp_change_pw_ab_9_9.txt
1 changes written to zoobot/temp_change_pw_ab_9_9.txt

# manual insert zoobot/temp_change_pw_ab_9_9.txt into change_pw_ab_9.txt
# generate temp_pw_ab_9.txt
python updateByLine.py temp_pw_ab_8.txt change_pw_ab_9.txt temp_pw_ab_9.txt
# 155 lines changed
# check
diff temp_pw_ab_9.txt temp_pw_ab_9_work.txt | wc -l
# 0 as expected
---------------------------------------------------------------
Change ' to ʼ in Non-Devanagari text.
temp_pw_9d.txt

7329 matches in 6732 lines for "ʼ" in buffer: temp_pw_ab_9.txt
1254 matches in 1207 lines for "ʼ" in buffer: temp_pw_9c.txt

cd zoobot
python punct3.py ../temp_pw_9c.txt ../temp_pw_9d.txt
5588 lines changed

7314 matches in 6721 lines for "ʼ" in buffer: temp_pw_9d.txt

Resolve differences between 9d and ab_9
cp temp_pw_9d.txt temp_pw_9e.txt
cp temp_pw_9e.txt temp_pw_9e_work.txt

python ../ablists/regex_compare_texts_count1.py 'ʼ' ../temp_pw_9e_work.txt ../temp_pw_ab_9.txt temp1.org ../temp_pw_9e_work1.txt ../temp_pw_ab_9_work1.txt
50 cases

resolve differences in temp1.org by editing 9e_work1 and ab_9_work1

# Generate change transactions for temp_pw_9e
# remove temp markup (* <L> -> <L>) in temp_pw_9e_work1.txt, and save as temp_pw_9e_work.txt.
python diff_to_changes_dict.py temp_pw_9e.txt temp_pw_9e_work.txt zoobot/temp_change_pw_9e_1.txt
44 changes written to zoobot/temp_change_pw_9e_1.txt

touch change_pw_9e.txt
# manual insert zoobot/temp_change_pw_9e_1.txt into change_pw_9e.txt
# generate temp_pw_9e.txt
python updateByLine.py temp_pw_9d.txt change_pw_9e.txt temp_pw_9e.txt
# 44 lines changed
# check
diff temp_pw_9e.txt temp_pw_9e_work.txt | wc -l
# 0 as expected

# Generate change transactions for temp_pw_ab_9
# remove temp markup (* <L> -> <L>) in temp_pw_ab_9_work1.txt, and save as temp_pw_ab_9_work.txt.
python diff_to_changes_dict.py temp_pw_ab_9.txt temp_pw_ab_9_work.txt zoobot/temp_change_pw_ab_9_10.txt
7 changes written to zoobot/temp_change_pw_ab_9_10.txt

# manual insert zoobot/temp_change_pw_ab_9_10.txt into change_pw_ab_9.txt
# generate temp_pw_ab_9.txt
python updateByLine.py temp_pw_ab_8.txt change_pw_ab_9.txt temp_pw_ab_9.txt
# 162 lines changed
# check
diff temp_pw_ab_9.txt temp_pw_ab_9_work.txt | wc -l
# 0 as expected

--------------
Any differences still there?

python ../ablists/regex_compare_texts_count1.py 'ʼ' ../temp_pw_9e_work.txt ../temp_pw_ab_9.txt temp1.org ../temp_pw_9e_work1.txt ../temp_pw_ab_9_work1.txt
0 cases -- all done

# Peek at differences in apostrophe

python ../ablists/regex_compare_texts_count1.py "'" ../temp_pw_9e_work.txt ../temp_pw_ab_9.txt temp1.org ../temp_pw_9e_work1.txt ../temp_pw_ab_9_work1.tx
0 cases

409 matches in 363 lines for "'" in buffer: temp_pw_ab_9_work.txt
409 matches in 366 lines for "'" in buffer: temp_pw_9e_work.txt
Same! Great.

7334 matches in 6736 lines for "ʼ" in buffer: temp_pw_ab_9_work.txt
7334 matches in 6741 lines for "ʼ" in buffer: temp_pw_9e_work.txt

Most "ʼ" occur as "ʼs".  
7269 matches in 6683 lines for "ʼs" in buffer: temp_pw_9e_work.txt
7279 matches in 6688 lines for "ʼs" in buffer: temp_pw_ab_9_work.txt
Oops! Resolve these differences

python ../ablists/regex_compare_texts_count1.py "ʼs" ../temp_pw_9e_work.txt ../temp_pw_ab_9.txt temp1.org ../temp_pw_9e_work1.txt ../temp_pw_ab_9_work1.txt
16 cases written to temp1.org

# manual edit 9e_work1.txt and ab_9_work1.txt to resolve differences

# Generate change transactions for temp_pw_9e
# remove temp markup (* <L> -> <L>) in temp_pw_9e_work1.txt, and save as temp_pw_9e_work.txt.
python diff_to_changes_dict.py temp_pw_9e.txt temp_pw_9e_work.txt zoobot/temp_change_pw_9e_2.txt
16 changes written to zoobot/temp_change_pw_9e_2.txt

# manual insert zoobot/temp_change_pw_9e_2.txt into change_pw_9e.txt
# generate temp_pw_9e.txt
python updateByLine.py temp_pw_9d.txt change_pw_9e.txt temp_pw_9e.txt
# 60 lines changed
# check
diff temp_pw_9e.txt temp_pw_9e_work.txt
# 0 as expected

No changes made to ab_9_work1.
-------------------------------
*************************************************************************
10-18-2023
That's enough for now.
Ready to install in csl-orig, etc.
*************************************************************************

-------------------------------------
Install temp_pw_9e.txt in csl-orig repository, and update displays
cd ../  # issue88

-----------------------
# do local install
cp temp_pw_9e.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt

# check local installation
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pw  ../../pw
sh xmlchk_xampp.sh pw
# ok
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue88

# push repositories to GitHub
----- csl-orig
cd /c/xampp/htdocs/cologne/csl-orig
git pull # check for other revisions. 
git status  # v02/pw/pw.txt
git add .
git commit -m "PW: Revise pw.txt based on temp_pw_9e.txt
  Ref: https://github.com/sanskrit-lexicon/PWK/issues/88"
git push

--------------------------------------------
update cologne displays
login to cologne
---- csl-orig
git pull
---- csl-pywork
cd v02
sh generate_dict.sh pw  ../../PWScan/2020/

--------------------------------------------
sync this repository to Github
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue88

git add .
git commit -m "temp_pw_9e, temp_pw_ab_9. #88"
git push
*********************************************************

  Ref: https://github.com/sanskrit-lexicon/PWK/issues/88#issuecomment-1770337758
# Correct by revision to temp_pw_9e.txt
cp temp_pw_9e.txt temp_pw_9e_work.txt
Manual edit temp_pw_9e_work.txt
1. ' ,'  -> ','  (6 cases)
2q. comma at beginning of line  (92 cases)
   move to previous line (but most have a [PageX] as previous line,
     so for these move to end of line preceding the [PageX] line
2b. semicolon at beginning of line (2 cases)
2c. period at beginning of line  (1 case)
2d. remove space at end of line (36 cases)
3. -- no changes at present time.
4a. missing bot markup when compared with the revised pw.AB.v1.txt
   This will require different activity. Defer for now
4b. Dass. => <ab>Dass.</ab> (3 cases)

Revise temp_pw_9e.txt
# Generate change transactions for temp_pw_9e
python diff_to_changes_dict.py temp_pw_9e.txt temp_pw_9e_work.txt zoobot/temp_change_pw_9e_3.txt
235 changes written to zoobot/temp_change_pw_9e_3.txt

# manual insert zoobot/temp_change_pw_9e_1.txt into change_pw_9e.txt
python updateByLine.py temp_pw_9d.txt change_pw_9e.txt temp_pw_9e.txt
295 lines changed
#check
diff temp_pw_9e.txt temp_pw_9e_work.txt | wc -l
# 0 as expected
------------------------------------------
Install revised temp_pw_9e.txt in csl-orig, etc.
-----------------------
# do local install
cp temp_pw_9e.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt

# check local installation
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pw  ../../pw
sh xmlchk_xampp.sh pw
# ok
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue88

# push repositories to GitHub
----- csl-orig
cd /c/xampp/htdocs/cologne/csl-orig
git pull # check for other revisions. 
git status  # v02/pw/pw.txt
git add .
git commit -m "PW: Revise pw.txt based on revised temp_pw_9e.txt
  Ref: https://github.com/sanskrit-lexicon/PWK/issues/88"
git push

--------------------------------------------
update cologne displays
login to cologne
---- csl-orig
git pull
---- csl-pywork
cd v02
sh generate_dict.sh pw  ../../PWScan/2020/

--------------------------------------------
sync this repository to Github
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue88

git add .
git commit -m "temp_pw_9e, temp_pw_ab_9. #88"
git push


*********************************************************
