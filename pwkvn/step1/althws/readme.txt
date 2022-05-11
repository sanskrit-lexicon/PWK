
Revise the althws (and hw) markup.

Ref: https://github.com/sanskrit-lexicon/PWK/issues/86

non-althws.entries.Vol.1-6.txt taken from above issue.
temp_pwkvn.txt  take from csl-orig

cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temp_pwkvn_0.txt
(commit f6a5171f05ba543b6e34c50bd9332c56673026f0)

non-althws-simple.txt
The 'simple cases from non-althws.entries.Vol.1-6.txt
 Note: Lines starting with ';' are skipped.  These to be handled separately
 L=9355 commented out:  no <althws>

====================================================================
non-althws-simple_special.txt
 items with notes from AB and Jim
temp_pwkvn_1.txt   These changes implemented.
install: csl-orig/v02/pwkvn/pwkvn.txt
cp temp_pwkvn_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt
cd /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/update
# check xml validity
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwkvn  ../../pwkvn
sh xmlchk_xampp.sh pwkvn

# remake mergehw in display
cd /c/xampp/htdocs/cologne/csl-apidev/pwkvn/mergehw
sh redo.sh
# commit csl-apidev

# commit csl-orig
cd /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/
Ref: 
# come back here in git bash
cd /c/xampp/htdocs/sanskrit-lexicon/pwk/pwkvn/step1/althws

====================================================================


python change_althws.py temp_pwkvn_0.txt non-althws-simple.txt change_1.txt
133 L numbers read from non-althws-simple.txt
Items to exclude 
L =
 488,  882, 1086, 1180, 1539, 1629, 1683, 2008, 2064,
2249, 2810, 2883, 2885, 2893, 2924, 2991, 3129, 3280, 3365,
3446, 3511, 3538, 3542, 3551, 3615, 3813, 3883, 4034, 4094,
4098, 4345, 4366, 4595, 4826, 4839, 4867, 4927, 4946, 5504,
5646, 5828, 5888, 6102, 6244, 6251, 6255, 6270, 6376, 6425,
6441, 6691, 6746, 6747, 6759, 6814, 7024, 7052, 7071, 7110,
7164, 7168, 7178, 7287, 7402, 7438, 7594, 7713, 7717, 7749,
7950, 8156, 8220, 8247, 8347, 8376, 8437, 8508, 8626, 8675,
8757, 8776, 8971, 9027, 9139, 9321, 9381, 9387, 9402,

88 non-althws-simple_488.txt
 The items in the list above
45 non-althws-simple_not488.txt

python change_althws.py temp_pwkvn_1.txt non-althws-simple_488.txt change_1_488.txt
92052 lines read from temp_pwkvn_1.txt
22609 entries found
88 L numbers read from non-althws-simple_488.txt
88 Change transactions found
88 changes written to change_1_488.txt

python change_althws.py temp_pwkvn_1.txt non-althws-simple_not488.txt change_1_not488.txt
92052 lines read from temp_pwkvn_1.txt
22609 entries found
45 L numbers read from non-althws-simple_not488.txt
45 Change transactions found
45 changes written to change_1_not488.txt
====================================================================
Apply change_1_not488.txt
python updateByLine.py temp_pwkvn_1.txt change_1_not488.txt temp_pwkvn_2.txt
90 lines changed.
====================================================================
temp_pwkvn_3.txt   (Manual changes)

1. remove the blank lines introduced in change_1_not488.txt
2. 16168  kuRW shld be althw headword

(material from non-althws-simple_special.txt from AB and Jim)

3. 246  should have "</hw> und <hw>" in place of "</hw> u. <hw>".
4. <L>725 ; however, this internally has two more new entries to be split as <L>725.1 "1. अनुत्तर" and <L>725.2 "2. अनुत्तर"<L>725 ; however, this internally has two more new entries to be split as <L>725.1 "1. अनुत्तर" and <L>725.2 "2. अनुत्तर"
5. <L>2654 ; आवश्यकसूत्र is not an althw, but a sub-hw internal in the body.
   True.  No change required.  It needs to be althw since Volume 7 refers to
   AvaSyakasUtra.
6. <L>2727 ; is a continuation of <L>2726, and not a new entry & both are to be merged.
7. <L>3429 ; althw should be अदूरेबान्धव
   L=10461.  Similarly correct althw from adUre to adUrebAnDava
8. <L>7164 (Jim)  mark only garut as alt headword  (cf L=16817 vol 7)
9. <L>8508 (Jim)  only aSocyatA as althws (not aSocyatva, aSocyaM)
  cf. L=13380 in vol 7.
10. no change ;<L>8746 ; mentions repositioning of two entries (कटुकविटप & कटुतुम्बी); how to treat this entry? probably like at <L>8844, may have just these two words as althws.  

  confer vol 7: 15641 and 15644 

====================================================================
(Jim) Observations where Volume 7 has overlooked some headwords
of earlier volumes
1. <L>7168 gAQavarcas, gAQavarcastva.  
   Vol. 7 has only <L>16837 gAQavarcastva   possible error in vol 7?
2. <L>8776 karuRavedin, karuRaveditA
   vol 7 has only karuRaveditA cf. <L>15780
3. <L>8971 triHzamfdDa, triHzamfdDatva
   Vol 7 has only triHzamfdDatva  cf. <L>17989
====================================================================
installation of temp_pwkvn_3.txt

install: csl-orig/v02/pwkvn/pwkvn.txt
cp temp_pwkvn_3.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt
# next is extra step for pwkvn - do before pywork/v02
cd /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/update
sh redo.sh

# check xml validity
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwkvn  ../../pwkvn
sh xmlchk_xampp.sh pwkvn
 # ok 
# commit/push to csl-orig
cd /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn
# return home
cd /c/xampp/htdocs/sanskrit-lexicon/pwk/pwkvn/step1/althws
========================================================
regenerate the headwords in the pwkvn application of csl-apidev
cd /c/xampp/htdocs/cologne/csl-apidev/pwkvn/mergehw
sh redo.sh
# return home
cd /c/xampp/htdocs/sanskrit-lexicon/pwk/pwkvn/step1/althws
