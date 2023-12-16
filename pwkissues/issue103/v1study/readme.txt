pwkissues/issue103/v1study/readme.txt

Begin 12-11-2023
Compare Andhrabharati's version1 of pwkvn to latest cdsl version.

# this directory
cd /c/xampp/htdocs/sanskrit-lexicon/pwk/pwkissues/issue103

# issue 103 link
 https://github.com/sanskrit-lexicon/PWK/issues/103

# cdsl version start with temp_pwpvn_0.txt as copy of
  csl-orig/v02/pwkvn/pwkvn.txt at commit 9c178657efabe2462601baf05a4a3ec6f18a32ae
 cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temp_pwkvn_0.txt

# Version from Andhrabharati

AB version https://github.com/sanskrit-lexicon/PWK/issues/102#issuecomment-1811667633
renamed temp_pwkvn_ab_0.txt

# compare number of lines
wc -l temp_pwkvn*
  92007 temp_pwkvn_0.txt
  90461 temp_pwkvn_ab_0.txt
(+ 90461 1553) - 
# make displays 
sh redo_dev.sh 0

-----------------
sh redo_dev.sh ab_0
# Correct 5 xml errors in cdsl version.
cp temp_pwkvn_ab_0.txt temp_pwkvn_ab_0a.txt

sh redo_dev.sh ab_0a

----------------------------------------------------------
entry comparisons

grep -E "^<L>" temp_pwkvn_0.txt | wc -l
22609

grep -E "^<L>" temp_pwkvn_ab_0a.txt | wc -l
22611

-----
grep -E "^<L>" temp_pwkvn_0.txt > temp_pwkvn_0_meta.txt
grep -E "^<L>" temp_pwkvn_ab_0a.txt > temp_pwkvn_ab_0a_meta.txt

diff temp_pwkvn_0_meta.txt temp_pwkvn_ab_0a_meta.txt | wc -l
16

$ diff temp_pwkvn_0_meta.txt temp_pwkvn_ab_0a_meta.txt > tempdiff_meta.txt

cp temp_pwkvn_0.txt temp_pwkvn_0a.txt
1.  add <h>
  <L>1729<pc>1-299-a<k1>upamAtar<k2>upamAtar<h>2
  <L>1754<pc>1-299-c<k1>Uh<k2>Uh<h>1
  <L>1764<pc>1-299-c<k1>ekavarRa<k2>ekavarRa<h>2
2. Two additional entries  (this changes number of lines)
   <L>8024.1<pc>5-262-c<k1>ma<k2>ma<h>2
   <L>20250.1<pc>7-366-1<k1>ma<k2>ma<h>2
3. Remove blank line at end of temp_pwkvn_0a.txt


# check
grep -E "^<L>" temp_pwkvn_0a.txt > temp_pwkvn_0a_meta.txt

diff  temp_pwkvn_0a_meta.txt temp_pwkvn_ab_0a_meta.txt
# files are the same.  0a and ab_0a agree in metalines.

-------------------------------------------------------------
   92014 temp_pwkvn_0a.txt
   90461 temp_pwkvn_ab_0a.txt
1553 matches for "<althws>" in buffer: temp_pwkvn_0a.txt
(+ 90461 1553) 92014

python add_althws.py temp_pwkvn_ab_0a.txt temp_pwkvn_0a.txt temp_pwkvn_ab_0b.txt
92014 lines written to temp_pwkvn_ab_0b.txt

Note: Now temp_pwkvn_0a.txt and temp_pwkvn_ab_0b.txt have same number of
  lines, and temp_pwkvn_ab_0b.txt has the <althws>X</althws> lines.

However, As #103 mentions,  Andhrabharati prefers to use the 'gra'
method of representing 'alternate headwords' in pwkvn.

-------------------------------------------------------------
Systematic adjustments to cdsl version to bring into line with AB version

python compare_lines.py temp_pwkvn_0a.txt temp_pwkvn_ab_0b.txt
92014 read from temp_pwkvn_0a.txt
92014 read from temp_pwkvn_ab_0b.txt
69396 lines are the same


python cdsl_adj1.py temp_pwkvn_0a.txt temp_pwkvn_0b.txt
92014 read from temp_pwkvn_0a.txt
92014 read from temp_pwkvn_ab_0b.txt
69396 lines are the same


python compare_lines.py temp_pwkvn_0b.txt temp_pwkvn_ab_0b.tx
92014 read from temp_pwkvn_0b.txt
92014 read from temp_pwkvn_ab_0b.txt
89126 lines are the same

Conclusion: all but 3000 lines are explained by various
'simple' alterations to the cdsl version.


-------------------------------------------------------------
At this point, I stop the comparison.
And agree to accept the AB version.

The AB version (with my insertion of the 'althws' lines)
is temp_pwkvn_ab_0b.txt , and its zip temp_pwkvn_ab_0b.zip is
uploaded and mentioned in the comment
https://github.com/sanskrit-lexicon/PWK/issues/103#issuecomment-1851223255
-------------------------------------------------------------
