echo "Create pwbib1.txt from pwbib0.txt"
python pwbib1.py pwbib0.txt pwbib1.txt
echo "match pwbib1.txt to sortedcrefs.txt"
python crefmatch.py pwbib1.txt ../pw_dhaval/abbrvwork/abbrvoutput/sortedcrefs.txt  crefmatch.txt pwbib_new.txt > crefmatch_log.txt

