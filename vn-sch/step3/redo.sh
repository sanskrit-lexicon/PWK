echo "extract3_slp1"
python extract3.py slp1 temp_sch.txt extract3_slp1.txt   
echo "pwk3vn_1"
python updateByLine.py pwk3vn_utf8.txt change1.txt pwk3vn_1.txt
echo "pwk3vn_2.txt"
python pwk_transcode.py  slp1 pwk3vn_1.txt pwk3vn_2.txt
echo "compare_pwkvn_sch"
python compare_pwkvn_sch.py slp1 pwk3vn_2.txt extract3_slp1.txt compare_pwkvn_sch.txt
python compare_pwkvn_sch.py deva1 pwk3vn_2.txt extract3_slp1.txt compare_pwkvn_sch_deva.txt
