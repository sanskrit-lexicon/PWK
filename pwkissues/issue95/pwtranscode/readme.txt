July 17, 2023

temp_pw_orig.txt
  Local copy of /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt 
   at commit 734c5856af12a51863947e808723111b2aab7a6f

----------------
../change_0.txt
conversion uncovered 19 errors in Devanagari text.
change_0  provides corrections.

temp_pw_0.txt
python ../updateByLine.py temp_pw_orig.txt ../change_0.txt temp_pw_0.txt

-----------------------------------------------
devanagari conversion
-----------------------
python pw_transcode.py slp1 deva temp_pw_0.txt temp_pw_0_deva.txt
# check invertibility
python pw_transcode.py deva slp1 temp_pw_0_deva.txt temp_pw_0_deva_slp1.txt
diff temp_pw_0.txt temp_pw_0_deva_slp1.txt
# NO diff - invertibility confirmed.

-----------------------------------------------
iast conversion
-----------------------

python pw_transcode.py slp1 roman temp_pw_0.txt temp_pw_0_iast.txt

# confirm invertibility:
python pw_transcode.py roman slp1 temp_pw_0_iast.txt temp_pw_0_iast_slp1.txt
diff temp_pw_0.txt temp_pw_0_iast_slp1.txt
# (no difference)

--------???
# NOTE:  pw_transcode program changed to
  manually adjust three lines in the roman-slp1 transcoding.


-----------------------------------------------------------------------


Currently (Jan 3, 2021), pw.txt agrees with version in csl-orig at
commit# 67bfbda32328317ab45f69432f58204595227609).

Folder to create versions of the base digitization of pw  (pw.txt)
where the slp1 text is transcoded.
We also check for invertibility of this transcoding.

The current transcoding results are:
 pw_iast.txt and pw_deva.txt.

These are reconstructed by:

python pw_transcode.py slp1 roman pw.txt pw_iast.txt
and
python pw_transcode.py slp1 deva pw.txt pw_deva.txt

Discussion of pw_iast.txt
-------------------------

The transcoding details are contained in transcoder/slp1_roman.xml.

python pw_transcode.py slp1 roman pw.txt pw_iast.txt

We do the inverse transcoding, from iast back to slp1.
The inverse transcoding is governed by transcoder/roman_slp1.xml.

python pw_transcode.py roman slp1 pw_iast.txt temp_pw_slp1.txt
diff pw.txt temp_pw_slp1.txt > temp.txt

The diff shows that there are 3 cases where the transcoding is NOT invertible.
Note: temp_pw_slp1.txt should == pw.txt
  only differs in 3 words:
slp1  <L>116525.7<pc>588,2<k1>paramahaMsopanizadhfdaya<k2>parama/—haMsopanizad-hfdaya<e>4
iast  <L>116525.7<pc>588,2<k1>paramahaṃsopaniṣadhṛdaya<k2>paramá—haṃsopaniṣad-hṛdaya<e>4
slp1a <L>116525.7<pc>588,2<k1>paramahaMsopanizaDfdaya<k2>parama/—haMsopanizad-hfdaya<e>4

slp1  <L>139372<pc>704,3<k1>prAghAra<k2>prAg—hAra<e>3
iast  <L>139372<pc>704,3<k1>prāghāra<k2>prāg—hāra<e>3
<L>139372<pc>704,3<k1>prAGAra<k2>prAg—hAra<e>3

slp1  <L>139373<pc>704,3<k1>prAghoma<k2>prAg—homa<e>3
iast  <L>139373<pc>704,3<k1>prāghoma<k2>prāg—homa<e>3
slp1a <L>139373<pc>704,3<k1>prAGoma<k2>prAg—homa<e>3


Discussion of pw_deva.txt
-------------------------
NOTE: This uses the 'MW' transcoding rules:"  slp1_deva.xml and deva_slp1.xml

This is how we can transcode pw.txt to Devanagari.

python pw_transcode.py slp1 deva pw.txt pw_deva.txt 

python pw_transcode.py deva slp1 pw_deva.txt temp_pw_slp1.txt

Now, pw.txt and temp_pw_slp1.txt should be the same
diff pw.txt temp_pw_slp1.txt 
The files are the same!

Discussion of 
-------------------------
NOTE: This uses the 'PW' transcoding rules:"  slp1_deva1.xml and deva1_slp1.xml
(taken from csl-websanlexicon).

This is how we can transcode pw.txt to Devanagari.

python pw_transcode.py slp1 deva1 temp_pw_0.txt temp_pw_0_deva1.txt 

python pw_transcode.py deva1 slp1 temp_pw_0_deva1.txt temp_pw_0_deva1_slp1.txt

Now, temp_pw_0.txt and temp_pw_0_deva1_slp1.txt should be the same
diff temp_pw_0.txt temp_pw_0_deva1_slp1.txt 
The files are the same!
--------------------------------------------------
11-09-2023
HK transcoding requested by @maltenth
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue95/pwtranscode
cp /c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/utilities/transcoder/*hk*.xml transcoder/


# get latest copy of pw.txt
  (this is at commit 5fd4222ad497c894ed5d602fa652e4a2ec68c3cd of csl-orig)
mkdir temphk
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temphk/pw.txt

python pw_transcode.py slp1 hk temphk/pw.txt temphk/pw_hk.txt

# confirm invertibility:
python pw_transcode.py hk slp1 temphk/pw_hk.txt temphk/pw_hk_slp1.txt
diff temphk/pw.txt temphk/pw_hk_slp1.txt | wc -l
# 0 expected
# got 148!  Mostly these involve hiatus
   (two vowels, 'ai', 'au'  in slp1  become ') --
Example:
slp1: aDaupAsana
hk  : adhaupAsana
slp1: aDOpAsana   Note this is different from original slp1!

--------------------------------------------------
11-13-2023
HK transcoding requested by @maltenth, using revised csl-orig/v02/pw/pw.txt
csl-orig at commit d847fe33dd4e2626ebf8869325e0bca452a5f20d

cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temphk/pw.txt
python pw_transcode.py slp1 hk temphk/pw.txt temphk/pw_hk.txt
# confirm invertibility:
python pw_transcode.py hk slp1 temphk/pw_hk.txt temphk/pw_hk_slp1.txt
diff temphk/pw.txt temphk/pw_hk_slp1.txt | wc -l
# 0 expected
# got 148!  Mostly these involve hiatus. See above.

cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue95/pwtranscode
--------------------------------------------------
11-15-2023
transcoding of pwkvn
mkdir temppwkvn
Andhrabharati reports problem  with transcoding for pwkvn dictionary.
  Ref: https://github.com/sanskrit-lexicon/PWK/issues/102#issuecomment-181166452


cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt tempvn/pwkvn.txt
python pw_transcode.py slp1 deva tempvn/pwkvn.txt tempvn/pwkvn_deva.txt
# confirm invertibility:
python pw_transcode.py deva slp1 tempvn/pwkvn_deva.txt tempvn/pwkvn_deva_slp1.txt
diff tempvn/pwkvn.txt tempvn/pwkvn_deva_slp1.txt | wc -l
# 0 expected
# got 148!  Mostly these involve hiatus. See above.

cd /c/xampp/htdocs/sanskrit-lexicon/PWKVNK/pwkvnkissues/issue95/pwkvntranscode
-
--------------------------------------------------
11-15-2023
transcoding of pwkvn_AB_v.1.txt

cp ~/Downloads/andhrabharati/pwkvn/pwkvn_AB_v.1.txt temp_vn_ab/

python pw_transcode.py slp1 deva temp_vn_ab/pwkvn_AB_v.1.txt temp_vn_ab/pwkvn_AB_v.1_deva.txt

check invertibility:
python pw_transcode.py deva slp1 temp_vn_ab/pwkvn_AB_v.1_deva.txt temp_vn_ab/pwkvn_AB_v.1_deva_slp1.txt

diff temp_vn_ab/pwkvn_AB_v.1.txt temp_vn_ab/pwkvn_AB_v.1_deva_slp1.txt | wc -l
# 0   invertibility is fine.
--------------------------------------------------
11-21-2023
HK transcoding of pwg requested by @maltenth
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue95/pwtranscode

# get latest copy of pwg.txt
  (this is at commit ae6e6988ee586cd190b982ebcf32a0c684bdbb81 of csl-orig)
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temphk/pwg.txt

python pw_transcode.py slp1 hk temphk/pwg.txt temphk/pwg_hk.txt

# confirm invertibility:
python pw_transcode.py hk slp1 temphk/pwg_hk.txt temphk/pwg_hk_slp1.txt
diff temphk/pwg.txt temphk/pwg_hk_slp1.txt | wc -l
# 0 expected
# got 92!  These involve hiatus, as with 'pwk'
   (two vowels, 'ai', 'au'  in slp1  become ') --
-------------------------------------------------
--------------------------------------------------
11-21-2023
HK transcoding of pwkvn: possible interest to  @maltenth
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue95/pwtranscode


# get latest copy of pwkvn.txt
  (this is at commit ae6e6988ee586cd190b982ebcf32a0c684bdbb81 of csl-orig)
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temphk/pwkvn.txt

python pw_transcode.py slp1 hk temphk/pwkvn.txt temphk/pwkvn_hk.txt

# confirm invertibility:
python pw_transcode.py hk slp1 temphk/pwkvn_hk.txt temphk/pwkvn_hk_slp1.txt
diff temphk/pwkvn.txt temphk/pwkvn_hk_slp1.txt | wc -l
# 0 expected
