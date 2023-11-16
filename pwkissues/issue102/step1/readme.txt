step1/readme.txt

Duplicate AB's conversion from temp_pw_17a.txt to temp_pw_ab_17a.txt
'merging separate [Pagexxx] lines into other lines'

python step1.py ../temp_pw_17a.txt temp_pw_ab_17a_step1.txt


python step234.py temp_pw_ab_17a_step1.txt temp_pw_ab_17a_234.txt
674062 lines read from temp_pw_ab_17a_step1.txt
895 differences via adjust_blob_2
757 differences via adjust_blob_3
141513 differences via adjust_blob_4
674062 written to temp_pw_ab_17a_234.txt

-------------
diff temp_pw_ab_17a_234.txt ../temp_pw_ab_17a.txt | wc -l
84
# 0 expected.

diff temp_pw_ab_17a_234.txt ../temp_pw_ab_17a.txt > diff_4.txt
First difference:
373c373
< <LEND> [1002-1]
---
> <LEND> [Page1-002-a]

Resolve these by a change file
python ../diff_to_changes_dict.py temp_pw_ab_17a_234.txt ../temp_pw_ab_17a.txt change_diff_4.txt
# 21 changes written to change_diff_4.txt
python ../updateByLine.py temp_pw_ab_17a_234.txt change_diff_4.txt temp_pw_ab_17a_final.txt
21 change transactions from change_diff_4.txt

diff temp_pw_ab_17a_final.txt ../temp_pw_ab_17a.txt | wc -l
# 0, as expected

