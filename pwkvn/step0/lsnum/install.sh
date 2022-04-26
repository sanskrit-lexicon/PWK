ver=$1
filein="temp_pwkvn_${ver}_hk.txt"
fileout="temp_pwkvn_${ver}_slp1.txt"
echo "filein=$filein"
cd ../final
python final.py hk,slp1 ../lsnum/$filein ../lsnum/$fileout
echo "checking..."
python final.py slp1,hk ../lsnum/$fileout ../lsnum/temp.txt
echo "next should show '0'"
diff ../lsnum/$filein ../lsnum/temp.txt | wc -l
