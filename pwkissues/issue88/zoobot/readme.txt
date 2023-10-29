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
#*************************************************************************
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
9f Part 1
10-20-2023 Additional zoo and bot tags
additional zoo tags
python zoo_add.py ../temp_pw_9e.txt ../temp_pw_9e_work.txt

Acheriris Kokor Zibha 1 1  
Antilope cervicapra 1 2  (1 AB, 2 CDSL)
Ardea Argala 1 1
Ardea nivea 20 21
Ardea sibirica 27 27
Coluber Naga 8 8
Lacerta Godica 1 3
Noctua indica 1 1
Tantalus flacinellus 1 1
Unguis odoratus 1 24

python zoo_add.py ../temp_pw_ab_9.txt ../temp_pw_ab_9_work.txt
[same counts as for temp_pw_9e.txt]

----------------------------------------
additional bot tags for pw_ab_9
temp_Addl.bot.tags.in.pw_ab_9.lines.txt 
  Ref: https://github.com/sanskrit-lexicon/PWK/files/13056552/Addl.bot.tags.in.pw_ab_9.lines.txt
   
python bot_add_ab_9.py ../temp_pw_ab_9_work.txt temp_Addl.bot.tags.in.pw_ab_9.lines.txt ../temp_pw_ab_9_work1.txt

(520535): <bot>Piper longum</bot>  add italics
544350  italics

Generate changes and revise pw_ab_9
python diff_to_changes_dict.py temp_pw_ab_9.txt temp_pw_ab_9_work1.txt zoobot/temp_change_pw_ab_9_11.txt
281 changes written to zoobot/temp_change_pw_ab_9_11.txt

# manual insert zoobot/temp_change_pw_ab_9_11.txt into change_pw_ab_9.txt
# generate temp_pw_ab_9.txt
python updateByLine.py temp_pw_ab_8.txt change_pw_ab_9.txt temp_pw_ab_9.txt
443 change transactions from change_pw_ab_9.txt
# check
diff temp_pw_ab_9.txt temp_pw_ab_9_work1.txt | wc -l
# 0 as expected

----------------------------------------

zoo tags for pw_9f
cp temp_pw_9e.txt temp_pw_9f.txt
cp temp_pw_9f.txt temp_pw_9f_work.txt

python ../ablists/regex_compare_texts_count1.py '<bot>.*?</bot>' ../temp_pw_9f_work.txt ../temp_pw_ab_9.txt temp1.org ../temp_pw_9f_work1.txt ../temp_pw_ab_9_work1.txt
254 cases

# Manual edit temp_pw_9f_work1.txt and  temp_pw_ab_9_work1.txt to resolve cases
# Remove temp markup ('* <L>' -> '<L>') of temp_pw_9f_work1.txt and
#  save as temp_pw_9f_work.txt
# Remove temp markup ('* <L>' -> '<L>') of temp_pw_ab_9_work1.txt and
#  save as temp_pw_ab_9_work.txt

# Redo bot count to see if further changes required.
# revise temp_pw_9f_work.txt and temp_pw_ab_9_work.txt
python ../ablists/regex_compare_texts_count1.py '<bot>.*?</bot>' ../temp_pw_9f_work.txt ../temp_pw_ab_9_work.txt temp1.org ../temp_pw_9f_work1.txt ../temp_pw_ab_9_work1.txt
0 cases 

# do similar analysis with zoo tag,

python ../ablists/regex_compare_texts_count1.py '<zoo>.*?</zoo>' ../temp_pw_9f_work.txt ../temp_pw_ab_9_work.txt temp1.org ../temp_pw_9f_work1.txt ../temp_pw_ab_9_work1.txt
22 cases
# revise temp_pw_9f_work.txt and temp_pw_ab_9_work.txt

Now temp_pw_9f_work.txt and temp_pw_ab_9_work.txt agree in counts of
  bot/zoo elements
Further, require that the bot/zoo elements are identical

python ../ablists/regex_compare_texts1.py '<zoo>.*?</zoo>' ../temp_pw_9f_work.txt ../temp_pw_ab_9_work.txt temp1.org ../temp_pw_9f_work1.txt ../temp_pw_ab_9_work1.txt
# 0 cases

python ../ablists/regex_compare_texts1.py '<bot>.*?</bot>' ../temp_pw_9f_work.txt ../temp_pw_ab_9_work.txt temp1.org ../temp_pw_9f_work1.txt ../temp_pw_ab_9_work1.txt
# 3 cases
# these corrected.

### now temp_pw_9f_work.txt and temp_pw_ab_9_work.txt agree in text
#  of zoo and bot.

### See if any differences in counts of {%X%} (since zoo, bot normally
# occur as italic text

python ../ablists/regex_compare_texts_count1.py '{%.*?%}' ../temp_pw_9f_work.txt ../temp_pw_ab_9_work.txt temp1.org ../temp_pw_9f_work1.txt ../temp_pw_ab_9_work1.txt
21 cases.
Most of these are due to intraline [Page...] in ab_9.
Resolved.
The '•' character used in ab_9 when merging at page breaks (21 cases)
Resolve these in temp_pw_9f_work1.txt


# remove temp markup (* <L> -> <L>) in temp_pw_9f_work1.txt, and save as temp_pw_9f_work.txt.
python diff_to_changes_dict.py temp_pw_9f.txt temp_pw_9f_work.txt zoobot/temp_change_pw_9f_1.txt
283 changes written to zoobot/temp_change_pw_9f_1.txt

touch change_pw_9f.txt
# manual insert zoobot/temp_change_pw_9f_1.txt into change_pw_9f.txt
# generate temp_pw_9f.txt
python updateByLine.py temp_pw_9e.txt change_pw_9f.txt temp_pw_9f.txt
# 283 lines changed
# check
diff temp_pw_9f.txt temp_pw_9f_work.txt | wc -l
# 0 as expected

-------------------------
# Generate change transactions for temp_pw_ab_9
# remove temp markup (* <L> -> <L>) in temp_pw_ab_9_work1.txt, and save as temp_pw_ab_9_work.txt.
python diff_to_changes_dict.py temp_pw_ab_9.txt temp_pw_ab_9_work.txt zoobot/temp_change_pw_ab_9_12.txt
6 changes written to zoobot/temp_change_pw_ab_9_12.txt

# manual insert zoobot/temp_change_pw_ab_9_12.txt into change_pw_ab_9.txt
# generate temp_pw_ab_9.txt
python updateByLine.py temp_pw_ab_8.txt change_pw_ab_9.txt temp_pw_ab_9.txt
# 449 lines changed
# check
diff temp_pw_ab_9.txt temp_pw_ab_9_work.txt | wc -l
# 0 as expected

------------------------------------------------------
9f Part 2
Some misc. changes to pw_9f noticed during work above.

cp temp_pw_9f.txt temp_pw_9f_work.txt
manual edit temp_pw_9f_work.txt, temp_pw_ab_9_work.txt

' —,%}' -> '%} —,'  45
"{%[^%]*_"  (15)  Remove variously. Uncover some missed 'bot' tags.

## generate changes
python diff_to_changes_dict.py temp_pw_9f.txt temp_pw_9f_work.txt zoobot/temp_change_pw_9f_2.txt
59 changes written to zoobot/temp_change_pw_9f_2.txt

touch change_pw_9f.txt
# manual insert zoobot/temp_change_pw_9f_2.txt into change_pw_9f.txt
# regenerate temp_pw_9f.txt
python updateByLine.py temp_pw_9e.txt change_pw_9f.txt temp_pw_9f.txt
# 342 lines changed
# check
diff temp_pw_9f.txt temp_pw_9f_work.txt | wc -l
# 0 as expected

-------------------------
# Generate change transactions for temp_pw_ab_9

python diff_to_changes_dict.py temp_pw_ab_9.txt temp_pw_ab_9_work.txt zoobot/temp_change_pw_ab_9_13.txt
9 changes written to zoobot/temp_change_pw_ab_9_13.txt

# manual insert zoobot/temp_change_pw_ab_9_13.txt into change_pw_ab_9.txt
# generate temp_pw_ab_9.txt
python updateByLine.py temp_pw_ab_8.txt change_pw_ab_9.txt temp_pw_ab_9.txt
# 458 lines changed
# check
diff temp_pw_ab_9.txt temp_pw_ab_9_work.txt | wc -l
# 0 as expected

------------------------------------------------------
9f Part 3
Miscellaneous changes
- and — in italic text

python ../ablists/regex_compare_texts_count1.py '{%[^%]*-.*?%}' ../temp_pw_9f_work.txt ../temp_pw_ab_9_work.txt temp1.org ../temp_pw_9f_work1.txt ../temp_pw_ab_9_work1.txt

------------------------------------------------------
TODO ' —,%}' -> '%} —,'  45
<bot>Os Sepiae</bot>  -> <zoo>Os sepiae</zoo> (4) neither plant nor animal
<zoo>Unguis adoratus</zoo> (1) neither plant nor animal
•[Page61
17 matches for "{%[^%]*_"  (15)

Asa foetida
Andropogon muricatus


--------------------------------
python ../ablists/regex_compare_texts_count1.py '{%[^%]*-.*?%}' ../temp_pw_9f_work.txt ../temp_pw_ab_9_work.txt temp1.org ../temp_pw_9f_work1.txt ../temp_pw_ab_9_work1.txt
62 cases written to temp1.org

# Manual changes to temp_pw_9f_work.txt and temp_pw_ab_9_work.txt to resolve.

# Additional changes to temp_pw_9f_work.txt
1.  Change'{% ' as appropriate 29 temp_pw_9f_work.txt
2. ' {%— ' -> ' — {%'  119
3. '^{%— ' -> '— {%'    20  [regex replace] 
4. ' {%—, ' -> ' —, {%'  5
5. ' —%} ' -> '%} — '  40
Italic text with —  (count resolve)
python ../ablists/regex_compare_texts_count1.py '{%[^%]*—.*?%}' ../temp_pw_9f_work.txt ../temp_pw_ab_9_work.txt temp1.org ../temp_pw_9f_work1.txt ../temp_pw_ab_9_work1.txt
33 cases written to temp1.org

#manual resolve by edit of temp_pw_9f_work1.txt temp_pw_ab_9_work1.txt

78 matches in 40 lines for "•" in buffer temp_pw_9f_work.txt
  These are deleted to end of line

python ../ablists/regex_compare_texts_count1.py '{%.*?%}' ../temp_pw_9f_work.txt ../temp_pw_ab_9_work.txt temp1.org ../temp_pw_9f_work1.txt ../temp_pw_ab_9_work1.txt
3 cases .
manual changes to temp_pw_9f_work.txt

' {%; ' -> '; {%'  10 changes
' {%, ' -> ', {%'  63 changes
'%}:' -> ':%}'  49 changes
'.,%}$' -> '%}.'  17  (regex change)
'.;%}' 4 changes

------------------------
Install 9f, etc. for Part 3
# generate changes
python diff_to_changes_dict.py temp_pw_9f.txt temp_pw_9f_work.txt zoobot/temp_change_pw_9f_3.txt
493 changes written to zoobot/temp_change_pw_9f_3.txt
# manual insert zoobot/temp_change_pw_9f_3.txt into change_pw_9f.txt

# regenerate temp_pw_9f.txt
python updateByLine.py temp_pw_9e.txt change_pw_9f.txt temp_pw_9f.txt
# 835 lines changed
# check
diff temp_pw_9f.txt temp_pw_9f_work.txt | wc -l
# 0 as expected

-------------------------
# Generate change transactions for temp_pw_ab_9

python diff_to_changes_dict.py temp_pw_ab_9.txt temp_pw_ab_9_work.txt zoobot/temp_change_pw_ab_9_14.txt
4 changes written to zoobot/temp_change_pw_ab_9_14.txt

# manual insert zoobot/temp_change_pw_ab_9_14.txt into change_pw_ab_9.txt
# generate temp_pw_ab_9.txt
python updateByLine.py temp_pw_ab_8.txt change_pw_ab_9.txt temp_pw_ab_9.txt
# 462 lines changed
# check
diff temp_pw_ab_9.txt temp_pw_ab_9_work.txt | wc -l
# 0 as expected

------------------------------------------
Install revised temp_pw_9f.txt in csl-orig, etc.
-----------------------
# do local install
cp temp_pw_9f.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt

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
git commit -m "PW: Revise pw.txt based on revised temp_pw_9f.txt
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
git commit -m "temp_pw_9f, temp_pw_ab_9. #88"
git push

*************************************************************************
10-26-2023  resolve differences in CDSL/AB versions for
  all italic and Sanskrit text strings.
*************************************************************************
#  This will be version 10
cp temp_pw_9f.txt temp_pw_10.txt
cp temp_pw_10.txt temp_pw_10_work.txt
touch change_pw_10.txt

cp temp_pw_ab_9.txt temp_pw_ab_10.txt
cp temp_pw_ab_10.txt temp_pw_ab_10_work.txt
touch change_pw_ab_10.txt


----------------------------
Part 1
python ../ablists/regex_compare_texts1.py '{%.*?%}' ../temp_pw_10_work.txt ../temp_pw_ab_10_work.txt temp1.org ../temp_pw_10_work1.txt ../temp_pw_ab_10_work1.txt
579 cases written to temp1.org

manual changes to temp_pw_10_work1.txt
1. a few misc.
2. \([0-9]\)x\([0-9]\) -> \1×\2  17
3. <lang n="greek">\(.\)</lang> -> \1 88

# remove temp markup (* <L> -> <L>) in  temp_pw_10_work1.txt, and
  save as  temp_pw_10_work.txt
# generate changes
python diff_to_changes_dict.py temp_pw_10.txt temp_pw_10_work.txt zoobot/temp_change_pw_10_1.txt
106 changes written to zoobot/temp_change_pw_10_1.txt
# manual insert zoobot/temp_change_pw_10_1.txt into change_pw_10.txt

# regenerate temp_pw_10.txt
python updateByLine.py temp_pw_9f.txt change_pw_10.txt temp_pw_10.txt
# 106 change transactions
# check
diff temp_pw_10.txt temp_pw_10_work.txt | wc -l
# 0 as expected

# remove temp markup (* <L> -> <L>) in  temp_pw_ab_10_work1.txt, and
  save as  temp_pw_ab_10_work.txt
# generate changes
python diff_to_changes_dict.py temp_pw_ab_10.txt temp_pw_ab_10_work.txt zoobot/temp_change_pw_ab_10_1.txt
1 changes written to zoobot/temp_change_pw_ab_10_1.txt
# manual insert zoobot/temp_change_pw_ab_10_1.txt into change_pw_ab_10.txt

# regenerate temp_pw_ab_10.txt
python updateByLine.py temp_pw_ab_9.txt change_pw_ab_10.txt temp_pw_ab_10.txt
# 1 change transactions
# check
diff temp_pw_ab_10.txt temp_pw_ab_10_work.txt | wc -l
# 0 as expected

----------------------------
Part 2
python ../ablists/regex_compare_texts1.py '{%.*?%}' ../temp_pw_10_work.txt ../temp_pw_ab_10_work.txt temp1.org ../temp_pw_10_work1.txt ../temp_pw_ab_10_work1.txt
552 cases written to temp1.org
18 matches for "({%[^%)]*)" in buffer: temp_pw_10_work1.txt
 ({%\([^%)]*\))  -> {%(\1)

76 matches for "[0-9]〉 {%[^%]*,%}$" in buffer: temp_pw_ab_10_work1.txt
   Generally, these should end as %}.
manual changes to temp_pw_10_work1.txt
48 matches for "{%[0-9])" in buffer: temp_pw_10_work1.txt
 '{%\([0-9]\)) ' -> '\1) {%'   22
 '{%\([0-9])[a-z]\)) ' -> '\1 {%'

552 Manual cases.

# remove temp markup (* <L> -> <L>) in  temp_pw_10_work1.txt, and
  save as  temp_pw_10_work.txt
# generate changes
python diff_to_changes_dict.py temp_pw_10.txt temp_pw_10_work.txt zoobot/temp_change_pw_10_2.txt
531 changes written to zoobot/temp_change_pw_10_2.txt
# manual insert zoobot/temp_change_pw_10_2.txt into change_pw_10.txt

# regenerate temp_pw_10.txt
python updateByLine.py temp_pw_9f.txt change_pw_10.txt temp_pw_10.txt
# 637 change transactions
# check
diff temp_pw_10.txt temp_pw_10_work.txt | wc -l
# 0 as expected

# remove temp markup (* <L> -> <L>) in  temp_pw_ab_10_work1.txt, and
  save as  temp_pw_ab_10_work.txt
# generate changes
python diff_to_changes_dict.py temp_pw_ab_10.txt temp_pw_ab_10_work.txt zoobot/temp_change_pw_ab_10_2.txt
81 changes written to zoobot/temp_change_pw_ab_10_2.txt
# manual insert zoobot/temp_change_pw_ab_10_2.txt into change_pw_ab_10.txt

# regenerate temp_pw_ab_10.txt
python updateByLine.py temp_pw_ab_9.txt change_pw_ab_10.txt temp_pw_ab_10.txt
# 82 change transactions
# check
diff temp_pw_ab_10.txt temp_pw_ab_10_work.txt | wc -l
# 0 as expected

------------------------------
Part 3  any more italic text differences?
python ../ablists/regex_compare_texts1.py '{%.*?%}' ../temp_pw_10_work.txt ../temp_pw_ab_10_work.txt temp1.org ../temp_pw_10_work1.txt ../temp_pw_ab_10_work1.txt
21 cases written to temp1.org
# manual corrections to temp_pw_10_work1.txt temp_pw_ab_10_work1.txt
# These are cases where my correction in Part 2 was faulty.

# remove temp markup (* <L> -> <L>) in  temp_pw_10_work1.txt, and
  save as  temp_pw_10_work.txt
# generate changes
python diff_to_changes_dict.py temp_pw_10.txt temp_pw_10_work.txt zoobot/temp_change_pw_10_3.txt
14 changes written to zoobot/temp_change_pw_10_3.txt
# manual insert zoobot/temp_change_pw_10_3.txt into change_pw_10.txt

# regenerate temp_pw_10.txt
python updateByLine.py temp_pw_9f.txt change_pw_10.txt temp_pw_10.txt
# 651 change transactions
# check
diff temp_pw_10.txt temp_pw_10_work.txt | wc -l
# 0 as expected

# remove temp markup (* <L> -> <L>) in  temp_pw_ab_10_work1.txt, and
  save as  temp_pw_ab_10_work.txt
# generate changes
python diff_to_changes_dict.py temp_pw_ab_10.txt temp_pw_ab_10_work.txt zoobot/temp_change_pw_ab_10_3.txt
4 changes written to zoobot/temp_change_pw_ab_10_3.txt
# manual insert zoobot/temp_change_pw_ab_10_3.txt into change_pw_ab_10.txt

# regenerate temp_pw_ab_10.txt
python updateByLine.py temp_pw_ab_9.txt change_pw_ab_10.txt temp_pw_ab_10.txt
# 86 change transactions
# check
diff temp_pw_ab_10.txt temp_pw_ab_10_work.txt | wc -l
# 0 as expected

python ../ablists/regex_compare_texts1.py '{%.*?%}' ../temp_pw_10_work.txt ../temp_pw_ab_10_work.txt temp1.org ../temp_pw_10_work1.txt ../temp_pw_ab_10_work1.txt
3 cases show difference, but this is not material.
Example under <L>42565<pc>2264-1<k1>jApaka
cdsl {%zu 1)a) in Beziehung stehend%}
ab   {%zu 1〉a〉 in Beziehung stehend%}
The other two similar cases are under
<L>43020<pc>2270-3<k1>jIvanIya and
<L>77910<pc>4237-1<k1>brahman


_____________________________________________________________
Part 4:
AB uses some special unicode for fractions.
Do the same for cdsl.

python ../ablists/regex_compare_texts1.py '[0-9]/[0-9]' ../temp_pw_10_work.txt ../temp_pw_ab_10_work.txt temp1.org ../temp_pw_10_work1.txt ../temp_pw_ab_10_work1.txt
32 cases written to temp1.org
⁰¹⁴⁵⁶⁷⁸⁹⁄₀₁₂₃₄₅₆₇₈₉ 
python ../ablists/regex_compare_texts1.py '[⁰¹⁴⁵⁶⁷⁸⁹⁄₀₁₂₃₄₅₆₇₈₉]+' ../temp_pw_10_work.txt ../temp_pw_ab_10_work.txt temp1.org ../temp_pw_10_work1.txt ../temp_pw_ab_10_work1.txt
32 cases written to temp1.org
# manual changes to temp_pw_10_work1.txt temp_pw_ab_10_work1.txt

#install changes

# remove temp markup (* <L> -> <L>) in  temp_pw_10_work1.txt, and
  save as  temp_pw_10_work.txt
# generate changes
python diff_to_changes_dict.py temp_pw_10.txt temp_pw_10_work.txt zoobot/temp_change_pw_10_4.txt
34 changes written to zoobot/temp_change_pw_10_4.txt
# manual insert zoobot/temp_change_pw_10_4.txt into change_pw_10.txt

# regenerate temp_pw_10.txt
python updateByLine.py temp_pw_9f.txt change_pw_10.txt temp_pw_10.txt
# 685 change transactions
# check
diff temp_pw_10.txt temp_pw_10_work.txt | wc -l
# 0 as expected

# remove temp markup (* <L> -> <L>) in  temp_pw_ab_10_work1.txt, and
  save as  temp_pw_ab_10_work.txt
# generate changes
python diff_to_changes_dict.py temp_pw_ab_10.txt temp_pw_ab_10_work.txt zoobot/temp_change_pw_ab_10_4.txt
2 changes written to zoobot/temp_change_pw_ab_10_4.txt
# manual insert zoobot/temp_change_pw_ab_10_4.txt into change_pw_ab_10.txt

# regenerate temp_pw_ab_10.txt
python updateByLine.py temp_pw_ab_9.txt change_pw_ab_10.txt temp_pw_ab_10.txt
# 88 change transactions
# check
diff temp_pw_ab_10.txt temp_pw_ab_10_work.txt | wc -l
# 0 as expected
--------
--------------------------------------------------------------
Part 5:  resolve differences in Devanagari text
python ../ablists/regex_compare_texts1.py '{#.*?#}' ../temp_pw_10_work.txt ../temp_pw_ab_10_work.txt temp1.org ../temp_pw_10_work1.txt ../temp_pw_ab_10_work1.txt
241 cases written to temp1.org

# manual changes to temp_pw_10_work1.txt temp_pw_ab_10_work1.txt

#install changes

# remove temp markup (* <L> -> <L>) in  temp_pw_10_work1.txt, and
  save as  temp_pw_10_work.txt
# generate changes
python diff_to_changes_dict.py temp_pw_10.txt temp_pw_10_work.txt zoobot/temp_change_pw_10_5.txt
265 changes written to zoobot/temp_change_pw_10_5.txt
# manual insert zoobot/temp_change_pw_10_5.txt into change_pw_10.txt

# regenerate temp_pw_10.txt
python updateByLine.py temp_pw_9f.txt change_pw_10.txt temp_pw_10.txt
# 950 change transactions
# check
diff temp_pw_10.txt temp_pw_10_work.txt | wc -l
# 0 as expected

# remove temp markup (* <L> -> <L>) in  temp_pw_ab_10_work1.txt, and
  save as  temp_pw_ab_10_work.txt
# generate changes
python diff_to_changes_dict.py temp_pw_ab_10.txt temp_pw_ab_10_work.txt zoobot/temp_change_pw_ab_10_5.txt
11 changes written to zoobot/temp_change_pw_ab_10_5.txt
# manual insert zoobot/temp_change_pw_ab_10_5.txt into change_pw_ab_10.txt

# regenerate temp_pw_ab_10.txt
python updateByLine.py temp_pw_ab_9.txt change_pw_ab_10.txt temp_pw_ab_10.txt
# 99 change transactions
# check
diff temp_pw_ab_10.txt temp_pw_ab_10_work.txt | wc -l
# 0 as expected
--------

--------------------------------------------------------------
Part 6:  resolve differences in [.,][.,]

74 matches in 70 lines for "[.,][.,]" in buffer: temp_pw_10_work.txt
41 matches in 37 lines for "[.,][.,]" in buffer: temp_pw_ab_10_work.txt

python ../ablists/regex_compare_texts1.py '[.,][.,]' ../temp_pw_10_work.txt ../temp_pw_ab_10_work.txt temp1.org ../temp_pw_10_work1.txt ../temp_pw_ab_10_work1.txt
55 cases written to temp1.org

# resolve differences by manual edits
#install changes

# remove temp markup (* <L> -> <L>) in  temp_pw_10_work1.txt, and
  save as  temp_pw_10_work.txt
# generate changes
python diff_to_changes_dict.py temp_pw_10.txt temp_pw_10_work.txt zoobot/temp_change_pw_10_6.txt
55 changes written to zoobot/temp_change_pw_10_6.txt
# manual insert zoobot/temp_change_pw_10_6.txt into change_pw_10.txt

# regenerate temp_pw_10.txt
python updateByLine.py temp_pw_9f.txt change_pw_10.txt temp_pw_10.txt
# 1005 change transactions
# check
diff temp_pw_10.txt temp_pw_10_work.txt | wc -l
# 0 as expected

# remove temp markup (* <L> -> <L>) in  temp_pw_ab_10_work1.txt, and
  save as  temp_pw_ab_10_work.txt
# generate changes
python diff_to_changes_dict.py temp_pw_ab_10.txt temp_pw_ab_10_work.txt zoobot/temp_change_pw_ab_10_6.txt
5 changes written to zoobot/temp_change_pw_ab_10_6.txt
# manual insert zoobot/temp_change_pw_ab_10_6.txt into change_pw_ab_10.txt

# regenerate temp_pw_ab_10.txt
python updateByLine.py temp_pw_ab_9.txt change_pw_ab_10.txt temp_pw_ab_10.txt
# 104 change transactions
# check
diff temp_pw_ab_10.txt temp_pw_ab_10_work.txt | wc -l
# 0 as expected
--------

--------------------------------------------------------------
Part 7:  <lang> tag

198 matches in 196 lines for "<lang>.*?</lang>" in buffer: temp_pw_ab_10_work.txt
150 matches for "<lang>.*?</lang>" in buffer: temp_pw_10_work.txt

128 matches for "<lang>Prākrit</lang>" in buffer: temp_pw_ab_10_work.txt
128 matches for "<lang>Prākrit</lang>" in buffer: temp_pw_10_work.txt

50 matches in 48 lines for "<lang>ved\.</lang>" in buffer: temp_pw_ab_10_work.txt
9 matches for "<lang>ved\.</lang>" in buffer: temp_pw_10_work.txt


python ../ablists/regex_compare_texts1.py '<lang>.*?</lang>' ../temp_pw_10_work.txt ../temp_pw_ab_10_work.txt temp1.org ../temp_pw_10_work1.txt ../temp_pw_ab_10_work1.txt
45 cases written to temp1.org
change ' ved. ' to ' <lang>ved.</lang> '  (38)

python ../ablists/regex_compare_texts1.py '<lang>.*?</lang>' ../temp_pw_10_work.txt ../temp_pw_ab_10_work.txt temp1.org ../temp_pw_10_work1.txt ../temp_pw_ab_10_work1.txt
10 cases written to temp1.org

# resolved these 10 manually.

#install changes

# remove temp markup (* <L> -> <L>) in  temp_pw_10_work1.txt, and
  save as  temp_pw_10_work.txt
# generate changes
python diff_to_changes_dict.py temp_pw_10.txt temp_pw_10_work.txt zoobot/temp_change_pw_10_7.txt
46 changes written to zoobot/temp_change_pw_10_7.txt
# manual insert zoobot/temp_change_pw_10_7.txt into change_pw_10.txt

# regenerate temp_pw_10.txt
python updateByLine.py temp_pw_9f.txt change_pw_10.txt temp_pw_10.txt
# 1051 change transactions
# check
diff temp_pw_10.txt temp_pw_10_work.txt | wc -l
# 0 as expected

There are no changes for pw_ab_10

------------------------------------------------------------
Part 8:
 Resolve differences spaces in following
 19 matches in 13 lines for "[0-9], [0-9]" in buffer: temp_pw_ab_10_work1.txt
265 matches in 216 lines for "[0-9], [0-9]" in buffer: temp_pw_10_work1.txt

First, make a blanket changed in temp_pw_10_work.txt:
 "\([0-9]\), \([0-9]\)"  -> "\1,\2"   269 changes in 198 lines

# Now compare with AB to resolved diffs
python ../ablists/regex_compare_texts1.py '[0-9], [0-9]' ../temp_pw_10_work.txt ../temp_pw_ab_10_work.txt temp1.org ../temp_pw_10_work1.txt ../temp_pw_ab_10_work1.txt
13 cases written to temp1.org

# Resolve these differences manually.

#install changes

# remove temp markup (* <L> -> <L>) in  temp_pw_10_work1.txt, and
  save as  temp_pw_10_work.txt
# generate changes
python diff_to_changes_dict.py temp_pw_10.txt temp_pw_10_work.txt zoobot/temp_change_pw_10_8.txt
191 changes written to zoobot/temp_change_pw_10_8.txt
# manual insert zoobot/temp_change_pw_10_8.txt into change_pw_10.txt

# regenerate temp_pw_10.txt
python updateByLine.py temp_pw_9f.txt change_pw_10.txt temp_pw_10.txt
# 1242 change transactions
# check
diff temp_pw_10.txt temp_pw_10_work.txt | wc -l
# 0 as expected

There are no changes for pw_ab_10


#*************************************************************************
10-29-2023
That's enough for now for pw_10.
Ready to install in csl-orig, etc.
*************************************************************************

-------------------------------------
Install temp_pw_10.txt in csl-orig repository, and update displays
cd ../  # issue88

-----------------------
# do local install
cp temp_pw_10.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
xxx
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
git commit -m "PW: Revise pw.txt based on temp_pw_10.txt
  Ref: https://github.com/sanskrit-lexicon/PWK/issues/88"
git push

--------------------------------------------
update cologne displays
login to cologne
---- csl-orig
git pull
# 1225 lines changed
---- csl-pywork
cd v02
sh generate_dict.sh pw  ../../PWScan/2020/

--------------------------------------------
sync this repository to Github
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue88

git add .
git commit -m "temp_pw_10, temp_pw_ab_10. #88"
git push

***************************************************************
TODO
59089 matches in 51082 lines for "[0-9]\.</ls>" in buffer: temp_pw_10_work.txt
5 matches for "[0-9]\.</ls>" in buffer: temp_pw_ab_10_work.txt

I'll resolve these differences later, as part of <ls> resolution.  See readme/ls

------------------------------------------------------------
23 matches in 21 lines for "{%\([^%]*\) oder%}" in buffer: temp_pw_ab_10_work1.txt
27 matches in 25 lines for "{%\([^%]*\) oder%}" in buffer: temp_pw_10_work1.txt

------
German idiom with dashes.  Maybe some long-dashes should be WITHIN italics
Consult Thomas
Example: <L>74469<pc>4188-3<k1>prAya
old:  {%meistens —, zum grössten Theil%} —
new?: {%meistens —, zum grössten Theil —%}
------
------
1294 matches in 1291 lines for "!√" in buffer: temp_pw_ab_10_work1.txt
------
--------------------------------------------------------------
Part x:  paren-groups
python ../ablists/regex_compare_texts1.py '\([^[]*?\)' ../temp_pw_10_work.txt ../temp_pw_ab_10_work.txt temp1.org ../temp_pw_10_work1.txt ../temp_pw_ab_10_work1.txt
The exclusion of '['  is to exclude the [Pagexxx] markup, which AB and CDSL mark differently, and which I
  do not choose to use AB markup, at least for now.
  
1515 cases written to temp1.org  Too big a list to resolve manually.

python ../ablists/regex_compare_texts1.py '\(.*?\)' ../temp_pw_10_work.txt ../temp_pw_ab_10_work.txt temp1.org ../temp_pw_10_work1.txt ../temp_pw_ab_10_work1.txt

