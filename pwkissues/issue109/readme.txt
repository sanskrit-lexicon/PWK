12-06-2024. 

Ref: https://github.com/sanskrit-lexicon/PWK/issues/109
   BHĀGAVATAPURĀṆA link target

   standardization of pw links for 'Bhāg. P.'  (also pwkvn)


This directory:
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue109

----
Start with pw.txt from csl-orig at latest commit
  86f1ed82e4eb935b710d8ba2f4f2ed6bb32027f8


cd /c/xampp/htdocs/cologne/csl-orig
git show 86f1ed82:v02/pw/pw.txt > /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue109/temp_pw_0.txt

-----------------------------------------------
baseline: all links
python link_prelim2.py temp_pw_0.txt link_prelim2_0.txt

  964 <ls>BHĀG. P..*?</ls>
   18 <ls n="BHĀG. P..*?</ls>
  982 Total
982 cases written to link_prelim2_0.txt

python link_expand.py link_prelim2_0.txt link_expand_0.txt link_change_0_todo.txt

00982 ALL
00879 STANDARD
00062 CANTDO
00041 OK
00982 TOTAL
all cases accounted for
41 lines written to link_expand_0.txt
62 lines written to link_change_0_todo.txt

python make_change1.py temp_pw_0.txt link_expand_0.txt change_1.txt
41 cases
python updateByLine.py temp_pw_0.txt change_1.txt temp_pw_1.txt
41 change transactions from change_1.txt

-----------------------------------------------
python link_prelim2.py temp_pw_1.txt link_prelim2_1.txt
  964 <ls>BHĀG. P..*?</ls>
   74 <ls n="BHĀG. P..*?</ls>
 1038 Total
1038 cases written to link_prelim2_1.txt

python summary.py 1 temp_pw_1.txt bhagp_standard_1.txt bhagp_nonstandard_1.txt
1038 instances of ls
975 cases written to bhagp_standard_1.txt
63 cases written to bhagp_nonstandard_1.txt

In nonstandard, 55 instances match 'BHĀG. P. ed.'
The other 9 need adjustment

11884	aSvameDaka	44736	<ls n="BHĀG. P. 9,22,">(39)</ls>	(<ls n="BHĀG. P. 9,22,">39</ls>)
21461	ftaMBara	83278	<ls n="BHĀG. P.">BHĀG. 6,13,17</ls>	<ls n="BHĀG. P.">6,13,17</ls>
26676	kAmASaya	105300	<ls>BHĀG. P. 7</ls>	<ls>BHĀG. P. 7,11,34.</ls>.
39232	car	158594	<ls>BHĀG. P. 7,15</ls>	<ls>BHĀG. P. 7,3,15</ls>
47512	triDAman	194858	<ls>BHĀG. P. 3,8. 31</ls>	<ls>BHĀG. P. 3,8,31</ls>
63492	parAYc	262083	<ls>BHĀG. P. 5,5,3,1</ls>	<ls>BHĀG. P. 5,5,31</ls>
98343	var	409440	<ls>BHĀG. P. 1</ls>	  <ls>BHĀG. P.</ls>
119549	saptaSAlivawI	499464	<ls>BHĀG. P. 6,52</ls>	 <ls>BHĀV. P. 6,52</ls>  (only instance BHĀV. P.)
206433	arTaracana	588520	<ls n="BHĀG. P. 3">23,8</ls>	<ls n="BHĀG. P. 3,">23,8</ls>
                                

cp temp_pw_1.txt temp_pw_2.txt

Manual edit temp_pw_2.txt
  changing as above
sh redo_pw.sh 2

python link_prelim2.py temp_pw_2.txt link_prelim2_2.txt
  963 <ls>BHĀG. P..*?</ls>
   74 <ls n="BHĀG. P..*?</ls>
 1037 Total

python summary.py 1 temp_pw_2.txt bhagp_standard_2.txt bhagp_nonstandard_2.txt
1037 instances of ls
983 cases written to bhagp_standard_2.txt
54 cases written to bhagp_nonstandard_2.txt

Note: The nonstandards all match '<ls>BHĀG. P. ed.'

----
python check_bur.py link_prelim2_2.txt Burnouf.BhP.index.txt temp_check_bur.txt

34382	gataspfha	137484	<ls>BHĀG. P. 7,10,190</ls>   <ls>BHĀG. P. 7,10,19 </ls>

21824	ekapati	84708	<ls>BHĀG. P. 4,26,27</ls>	     27 not found
49440	daSArDa	202888	<ls>BHĀG. P. 5,15,30</ls>	     30 not found
82462	maDumEreya	340902	<ls>BHĀG. P. 6,2,59</ls>     59 not found
84707	mahABogin	350359	<ls>BHĀG. P. 5,24,81</ls>    81 not found
206319	apravizwa	588168	<ls n="BHĀG. P.">7,49,4</ls> 49 not found

Andhrabharati found solutions for these, They are all print changes to pw.txt
21824	ekapati	84708	<ls>BHĀG. P. 4,26,27</ls>	     4,20,27
49440	daSArDa	202888	<ls>BHĀG. P. 5,15,30</ls>	     3,15,30
82462	maDumEreya	340902	<ls>BHĀG. P. 6,2,59</ls>     6,1,59
84707	mahABogin	350359	<ls>BHĀG. P. 5,24,81</ls>    5,24,31
206319	apravizwa	588168	<ls n="BHĀG. P.">7,49,4</ls> 2,9,34 (other places: 7,12,15 & 10,3,14)

Rerun using revised temp_pw_2

sh redo_pw.sh 2

python link_prelim2.py temp_pw_2.txt link_prelim2_2.txt
  963 <ls>BHĀG. P..*?</ls>
   74 <ls n="BHĀG. P..*?</ls>
 1037 Total

python summary.py 1 temp_pw_2.txt bhagp_standard_2.txt bhagp_nonstandard_2.txt
1037 instances of ls
983 cases written to bhagp_standard_2.txt
54 cases written to bhagp_nonstandard_2.txt

python check_bur.py link_prelim2_2.txt Burnouf.BhP.index.txt temp_check_bur.txt
0 links incompatible with index ! good

# summary by skandha, adhyaya, verse  # only standard
python summary.py 2 temp_pw_2.txt bhagp_verse_2.txt
1037 instances of ls
737 cases written to bhagp_verse_2.txt

# generate change_2.txt
python diff_to_changes_dict.py temp_pw_1.txt temp_pw_2.txt change_2.txt
16 changes written to change_2.txt


===============================================
Installation version 2
--------------------------------------------
# local installation
sh redo_pw.sh 2

-----------------------------------
sync csl-orig to Github
cd /c/xampp/htdocs/cologne/csl-orig/v02

git add pw/pw.txt # pw.txt
git commit -m "PW: standardization of links for 'Bhāg. P.', version 2 
Ref: https://github.com/sanskrit-lexicon/PWK/issues/109"
56 insertions(+), 56 deletions(-)
xxx# 19 insertions(+), 19 deletions(-)
git push

-----------------------------------
sync csl-corrections to Github
cd /c/xampp/htdocs/cologne/csl-corrections/
git add . # dictionaries/pw/pw_printchange.txt
git commit -m "PW: print changes
Ref: https://github.com/sanskrit-lexicon/PWK/issues/109"
# 
git push

-----------------------------------
Sync Cologne server to github
1. csl-orig repo  # pull
2. csl-pywork/v02 #  pw  make displays
3. csl-corrections # pull

-----------------------------------
sync this PWK repo to github.

===============================================
