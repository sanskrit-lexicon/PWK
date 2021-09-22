# extraction with native (i.e. IAST italic) Schmidt coding of Sanskrit.
python extract1.py temp_sch.txt temp_extract1.txt

# slp1 coding
python extract2.py slp1 temp_sch.txt temp_extract2_slp1.txt   

# devanagari coding
python extract2.py deva1 temp_sch.txt temp_extract2_deva.txt   
# Recover temp_extract2_slp1.txt from temp_extract2_deva.txt   
python extract2_invert_deva.py temp_extract2_deva.txt temp_extract2_deva_slp1.txt   
diff temp_extract2_slp1.txt temp_extract2_deva_slp1.txt | wc -l

python extract2_invert_slp1.py temp_extract2_slp1.txt temp_extract2_slp1_roman1.txt
diff temp_extract1.txt temp_extract2_slp1_roman1.txt | wc -l

python compare_roman1.py temp_extract1.txt temp_extract2_slp1_roman1.txt temp_compare_roman1.txt

python pwinfo.py temp_sch.txt temp_pw.txt pwinfo.txt
