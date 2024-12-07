12-07-2024. 

Ref: https://github.com/sanskrit-lexicon/PWK/issues/110
   BHĀGAVATAPURĀṆA link target

   standardization of pwkvn links for 'Bhāg. P.'


This directory:
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue110

----
Start with pw.txt from csl-orig at latest commit
  0c75b1638ac483a88277f9ede301a55e6ac55ee1

cd /c/xampp/htdocs/cologne/csl-orig
git show 0c75b1638a:v02/pwkvn/pwkvn.txt > /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue110/temp_pwkvn_0.txt

-----------------------------------------------
baseline: all links
python link_prelim2.py temp_pwkvn_0.txt link_prelim2_0.txt
  198 <ls>BHĀG. P..*?</ls>
   13 <ls n="BHĀG. P..*?</ls>
  211 Total


python link_expand.py link_prelim2_0.txt link_expand_0.txt link_change_0_todo.txt
00211 ALL
00203 STANDARD
00008 CANTDO
00000 OK
00211 TOTAL

Note: there are NO links to expand!

python check_bur.py link_prelim2_0.txt Burnouf.BhP.index.txt temp_check_bur.txt
1 links incompatible with index
1 lines written to temp_check_bur.txt

6319	apravizwa	20555	<ls n="BHĀG. P.">7,49,4</ls>
  This also appears in pw.txt (see ../issue109/readme.txt)
  AB's solution: 2,9,34 (other places: 7,12,15 & 10,3,14)  print change

-----------------------------------------------
cp temp_pwkvn_0.txt temp_pwkvn_1.txt

#Manual edit temp_pwkvn_1.txt for the apravizwa change, and one other.

# make change_1.txt
python diff_to_changes_dict.py temp_pwkvn_0.txt temp_pwkvn_1.txt change_1.txt
2 changes written to change_1.txt

python link_prelim2.py temp_pwkvn_1.txt link_prelim2_1.txt
  198 <ls>BHĀG. P..*?</ls>
   13 <ls n="BHĀG. P..*?</ls>
  211 Total

python check_bur.py link_prelim2_1.txt Burnouf.BhP.index.txt temp_check_bur.txt
0 links incompatible with index  # good!

-----------------------------------------
# summary by book order
python summary.py 1 temp_pwkvn_1.txt bhagp_standard_1.txt bhagp_nonstandard_1.txt
211 instances of ls
204 cases written to bhagp_standard_2.txt
7 cases written to bhagp_nonstandard_2.txt

# summary by skandha, adhyaya, verse  # only standard
python summary.py 2 temp_pwkvn_1.txt bhagp_verse_2.txt
211 instances of ls
196 cases written to bhagp_verse_2.txt

--------------------------------------------
Installation version 1
--------------------------------------------
# local installation
sh redo_pwkvn.sh 1
-----------------------------------
sync csl-orig to Github
cd /c/xampp/htdocs/cologne/csl-orig

git add . # pwkvn.txt
git commit -m "PWKVN: standardization of links for 'Bhāg. P.'
Ref: https://github.com/sanskrit-lexicon/PWK/issues/110"
#  2 lines changed.
git push

-----------------------------------
sync csl-corrections to Github
  Note: there is no 'pwkvn' dictionary in csl-corrections.
        Make a comment in pw_printchange.txt at 12-07-2024 apravizwa
cd /c/xampp/htdocs/cologne/csl-corrections/
git add . # dictionaries/pw/pw_printchange.txt
git commit -m "PWKVN: print changes
Ref: https://github.com/sanskrit-lexicon/PWK/issues/110"
# 1 line changed.
git push

-----------------------------------
Sync Cologne server to github
1. csl-orig repo
2. csl-pywork/v02  pw  make displays
3. csl-corrections

-----------------------------------
sync this PW repo to github.
============================================================
