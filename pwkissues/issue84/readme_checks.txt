# readme_checks.txt

----------------------------------------
# get temporary local copy of dictionaries for checking
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temp_pwkvn.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt temp_sch.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw.txt


=====================================================

PRELIMINARY MANUAL CHECKs for pw

python generate_random.py 5 pw3 temp_pw.txt index.txt check_pw3_man.txt
regex_raw = <ls>MBH. ([0-9]+),([0-9]+),([0-9]+)
found 3474 instances in kosha

5 written to check_pw3_man.txt

4/5 checked.
 One is partially ok
 Suggest print changes for pw
202140 : anaritra : MBH. 5,63,8 : MBH. 5,63,7 :  v.l. ataritra,  pw_printchg
201983 : ataritra : MBH. 5,63,8 : MBH. 5,63,7 : pw_printchg
39232 : car : MBH. 18,3,45 : MBH. 18,3,15  : pw typo

=====  another check for each parvan
vol  parvans
1    1,2
2    3
3    4,5,6
4    7,8,9
5    10,11,12
6    13,14,15,16,17,18

parvan  1 483 instances in pw
1379 : ajIvita : MBH. 1,158,33 : 1-381 : ok  (vol 1, epage 381
parvan  2 194 instances in pw
48026 : trEbali : MBH. 2,4,13  : 1-519 : ok
parvan  3 645 instances in pw
8973<pc>1-105-a<k1>araRyavAsin : MBH. 3,267,17 : 2-538 : ok
parvan  4 132 instances in pw
202323<pc>2-290-c<k1>aprArTanIyA : MBH. 4,14,36 : 3-34 : ok
parvan  5 266 instances in pw
74613<pc>4-190-c<k1>prAvrAjya : MBH. 5,175,41 : 3-457 : ok
parvan  6 202 instances in pw
106006<pc>6-144-b<k1>vIrakarA : MBH. 6,9,26 : 3-522 : ok
parvan  7 238 instances in pw
202722<pc>2-295-a<k1>utkocin  : MBH. 7,73,32 : 4-129
parvan  8 159 instances in pw
72689<pc>4-163-a<k1>pramaRqala : MBH. 8,16,15 : 4-474 : ok
parvan  9 62 instances in pw
69498<pc>4-118-a<k1>pfTudaMzwra : MBH. 9,45,102 : 4-784 : ok
parvan 10 16 instances in pw
125736<pc>7-139-c<k1>sukrUra : MBH. 10,8,137 : 5-32 : ok [variant numbering]
parvan 11 14 instances in pw
3512<pc>1-041-c<k1>anapeta : MBH. 11,23,32 : 5-86 : ok
parvan 12 484 instances in pw
4237<pc>1-049-c<k1>anIrzu : MBH. 12,230,13 : 5-609 : ok
parvan 13 429 instances in pw
116183<pc>6-289-a<k1>zawsahasraSata : MBH. 13,155,14 : 6-397 : ok
parvan 14 111 instances in pw
208273<pc>6-293-c<k1>atisparDin : MBH. 14,5,5 : 6-436 : ok
parvan 15 25 instances in pw
40817<pc>2-239-c<k1>cyu : >MBH. 15,16,22 : 6-612 : ok : cyavitum
parvan 16 6 instances in pw
17429<pc>1-211-a<k1>Ikz : MBH. 16,6,13 : 6-655 : ok : aByupekzita
parvan 17 3 instances in pw
222102<pc>7-385-a<k1>atiBukta : MBH. 17,2,25 : 6-671 : ok
parvan 18 3 instances in pw
39232 : car : MBH. 18,3,15 : 6-684 : ok : upacIrRa

=====================================================

PRELIMINARY MANUAL CHECKs for mw

python generate_random.py 5 mw3 temp_mw.txt index.txt check_mw3_man.txt
regex_raw = <ls>MBh. ([vix]+), *([0-9]+), *([0-9]+)
found 232 instances in kosha

5 written to check_mw3_man.txt
All checks ok

=====================================================

PRELIMINARY MANUAL CHECKs for pwkvn

python generate_random.py 5 pwkvn3 temp_pwkvn.txt index.txt check_pwkvn3_man.txt
regex_raw = <ls>MBH. ([0-9]+),([0-9]+),([0-9]+)
found 777 instances in kosha

5 written to check_pwkvn3_man.txt
All checks ok

=====================================================

PRELIMINARY MANUAL CHECKs for sch

python generate_random.py 5 sch3 temp_sch.txt index.txt check_sch3_man.txt
regex_raw = <ls>MBh. ([0-9]+),([0-9]+),([0-9]+)
found 772 instances in kosha

5 written to check_sch3_man.txt
4/5 check ok.  The other one is a commentary variant: NÄ«lak. zu MBh.

=====================================================

PRELIMINARY MANUAL CHECKs for pwg

python generate_random.py 5 pwg3 temp_pwg.txt index.txt check_pwg3_man.txt
regex_raw = <ls>MBH. ([0-9]+),([0-9]+),([0-9]+)
found 1 instances in kosha

1 written to check_pwg3_man.txt
NOT FOUND.  low print quality. NÄ«lak. zu MBH.


=====================================================
pw generate all

python generate_random.py ALL pw3 temp_pw.txt index.txt check_all_pw3_0.txt check_all_pw3_0_nopagerec.txt

regex_raw = <ls>MBH. ([0-9]+),([0-9]+),([0-9]+)
found 3474 instances in kosha
get_examples: 68 pagerecs not found

# examine the 68 pagerecs not found
# check the pw scans for all 68 case, confirming the key from the ls
# mark each as either:
1. (48)  pwrefok   the ls reference matches the scan
2. (19) key -> newkey  when the key (ls ref) is a typo

cp pw.txt pw1.txt
# make manual changes to pw1.txt for the 19.
97934 : vanajapattrAkza : (1,17,43)   : (1,171,43)
105868 : vihewaka       : (1,20,76)   : (1,3076)
72767 : pramARAyAmatas  : (1,22,31)   : (1,222,31)
72767 : pramARAyAmatas  : (1,22,31)   : (1,222,31)
79806 : Bid             : (2,24,83)   : (2,2483)
24001 : kanapa          : (2,30,34)   : (3,20,34)
20257 : upahvara        : (2,165,5)   : (3,165,5)
99469 : vasuDArA        : (3,2000,41) : (3,200,41)
20071 : upaSruti        : (5,14,26)   : (5,13,26)
117928 : saYj           : (5,45,72)   : (6,45,72)
44998 : talanizpeza     : (5,448,52)  : (5,48,52)
28461 : kuRqala         : (6,6,63)    : (6,9,63)
64793 : paryAya         : (6,37,45)   : (6,3745)
92561 : raTayoDa        : (8,117,55)  : (6,117,55)
90760 : yAdavIputra     : (12,96,71)  : (12,69,71)
55351 : DAv             : (12,380,45) : (12,280,45) 
106757 : vfzalayAjaka   : (13,200,6)  : (13,200,7)
117746 : sacakropaskara : (14,79,156) : (14,79,15)
39232  : car            : (18,3,45)   : (18,3,15)

# change file pw -> pw1
python diff_to_changes_dict.py temp_pw.txt temp_pw1.txt change_pw_pw1.txt
19 changes written to change_pw_pw1.txt
NOTE: These are all typos


# rerun, using temp_pw1.txt

python generate_random.py ALL pw3 temp_pw1.txt index.txt check_all_pw3_1.txt check_all_pw3_1_nopagerec.txt


All in this random sample checked.

=====================================================
pw generate all using MBH. ed. Bomb.

python generate_random.py ALL pw3a temp_pw.txt index.txt check_all_pw3a_0.txt check_all_pw3a_0_nopagerec.txt

regex_raw = <ls>MBH. ed. Bomb. ([0-9]+),([0-9]+),([0-9]+)
found 9 instances in kosha
found 9 distinct in kosha
write_examples: 9 written to check_all_pw3a_0.txt
write_examples: 1 written to check_all_pw3a_0_nopagerec.txt

One pagerec not found: 6,21,21 dASat
Others ok (but some are indirect) 

=====================================================
 changes from AB
 Ref: https://github.com/sanskrit-lexicon/PWK/issues/84#issuecomment-2945143071
L-27585 : kASyapadvIpa:  <ls>MBH. 6,6</ls> : <ls>MBH. 6,6,55</ls> ;;print_change
L-114323 : SESupAli : <ls>MBH. 254,6</ls> : <ls>MBH. 3,254,16</ls> ;;print_change
L-123397 : sAMsa : <ls>MBH. 6,6</ls> : <ls>MBH. 6,64</ls> ;;print_change
  (also fehlerhaft für {#sAMsa#} : fehlerhaft für {#mAMsa#} ;; typo
L-130874 : sTA : <ls>MBH. 6,9</ls> : <ls>MBH. 6,93</ls> ;;print_change

L-220999 : vas : <ls>MBH. 13,4</ls>. <ls n="MBH. 13,">10</ls> : <ls>MBH. 13,4,10</ls> ;;typo

cp temp_pw1.txt temp_pw2.txt

python diff_to_changes_dict.py temp_pw1.txt temp_pw2.txt change_pw1_pw2.txt
5 changes written to change_pw1_pw2.txt


-------------
install temp_pw2.txt
cp temp_pw2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
cd /c/xampp/htdocs/cologne/csl-orig/v02
git add .
git commit -m "PW: misc changes re mbhbomb.
Ref: https://github.com/sanskrit-lexicon/PWK/issues/84"
git push

# Also update csl-corrections/dictionaries/pw/pw_printchange.txt

# return to this directory
cd /c/xampp/htdocs/sanskrit-lexicon/pwk/pwkissues/issue84
=====================================================
index_AB.txt  see readme.txt  A revision of index_orig.txt by AB.

=====================================================
temp_pw3.txt

cp temp_pw2.txt temp_pw3.txt
# apply changes to temp_pw3.txt from check_all_pw3_1_nopagerec.resolved.txt

Jim's work in check_all_pw3_1_nopagerec.resolved_notes.txt

# make change file
python diff_to_changes_dict.py temp_pw2.txt temp_pw3.txt change_pw2_pw3.txt
37 changes written to change_pw2_pw3.txt

-----------------------------------------
install temp_pw3.txt
cp temp_pw3.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
cd /c/xampp/htdocs/cologne/csl-orig/v02
git add .
git commit -m "PW: misc changes re mbhbomb 'pagerec not found'
Ref: https://github.com/sanskrit-lexicon/PWK/issues/84"
git push

# Also update csl-corrections/dictionaries/pw/pw_printchange.txt

# return to this directory
cd /c/xampp/htdocs/sanskrit-lexicon/pwk/pwkissues/issue84

----------------------------------------
generate all with temp_pw3.txt and index_AB.txt

python generate_random.py ALL pw3 temp_pw3.txt index_AB.txt check_all_pw3_2.txt check_all_pw3_2_nopagerec.txt

regex_raw = <ls>MBH. ([0-9]+),([0-9]+),([0-9]+)
found 3474 instances in kosha
found 3052 distinct in kosha
write_examples: 3472 written to check_all_pw3_2.txt
write_examples: 4 written to check_all_pw3_2_nopagerec.txt

=====================================================
mw generate all

python generate_random.py ALL mw3 temp_mw.txt index.txt check_all_mw3_0.txt check_all_mw3_0_nopagerec.txt
regex_raw = <ls>MBh. ([vix]+), *([0-9]+), *([0-9]+)
found 232 instances in kosha
found 219 distinct in kosha
write_examples: 232 written to check_all_mw3_0.txt
write_examples: 15 written to check_all_mw3_0_nopagerec.txt


---------------------------------
All (almost) checks favorable.
Ready to install:
 csl-websanlexicon
 csl-apidev



