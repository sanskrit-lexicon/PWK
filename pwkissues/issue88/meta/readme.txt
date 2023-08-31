pwkissues/issue88/meta/readme.txt
adapted from /c/xampp/htdocs/sanskrit-lexicon/BHS/meta

This directory for general update of the csl-orig/v02/pw/meta2.txt file.
It is adapted from the issues/issue1/meta directory.

The main task is to run programs to generate counts of
- extended ascii characters
- tags - mainly xml tags.

Main logic is:
- copy latest versions from csl-orig of
  - digitization (xxx.txt) and
  - meta2  (xxx-meta2.txt)
- run programs to generate statistics from xxx.txt
- manually adapt xxx-meta2.txt from these statistics
- copy revised xxx-meta2 back to csl-orig and update csl-orig.

-----------------------------------------------
cp  /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw-meta2.txt pw-meta2.txt


-----------------------------------------------
# extended ascii codes with counts
--- for temp_pw_0
python check_ea1.py ../temp_pw_0.txt check_ea1_pw_0.txt
682608 lines in ../temp_pw_0.txt
144 extended ascii codes found in ../temp_pw_0.txt

--- for temp_pw_ab_1
python check_ea1.py ../temp_pw_ab_1.txt check_ea1_pw_ab_1.txt
674189 lines in ../temp_pw_ab_1.txt
171 extended ascii codes found in ../temp_pw_ab_1.txt


-----------------------------------------------
# tag summary 08-24-2023
--- for temp_pw_0
python check_tags.py ../temp_pw_0.txt check_tags_pw_0.txt check_tags_local_pw_0.txt
13 lines written to check_tags_pw_0.txt
357 lines written to check_tags_local_pw_0.txt

--- for temp_pw_ab_1
python check_tags.py ../temp_pw_ab_1.txt check_tags_pw_ab_1.txt check_tags_local_pw_ab_1.txt

17 lines written to check_tags_pw_ab_1.txt
1030 lines written to check_tags_local_pw_ab_1.txt

--------------------------------------------------------------------
