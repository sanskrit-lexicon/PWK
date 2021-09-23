# change1.txt manual
python updateByLine.py temp_sch.txt change1.txt temp_sch1.txt
python change2.py temp_sch1.txt change2.txt
python updateByLine.py temp_sch1.txt change2.txt temp_sch2.txt

python change3.py temp_sch2.txt temp_change3.txt
python updateByLine.py temp_sch2.txt temp_change3.txt temp_sch3.txt

python change4.py temp_sch3.txt temp_change4.txt
python updateByLine.py temp_sch3.txt temp_change4.txt temp_sch4.txt

python change5.py temp_sch4.txt temp_change5.txt
python updateByLine.py temp_sch4.txt temp_change5.txt temp_sch5.txt

# change6.txt manual
python updateByLine.py temp_sch5.txt change6.txt temp_sch6.txt

python change7.py temp_sch6.txt temp_change7.txt
python updateByLine.py temp_sch6.txt temp_change7.txt temp_sch7.txt

python change8.py temp_sch7.txt temp_change8.txt

python updateByLine.py temp_sch7.txt temp_change8.txt temp_sch8.txt

echo "final version is temp_sch8.txt"
