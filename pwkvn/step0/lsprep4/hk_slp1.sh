pathhk=$1
pathslp1=$2
#filein="temp_pwkvn_${ver}_hk.txt"
#fileout="temp_pwkvn_${ver}_slp1.txt"
#echo "filein=$filein"
cd ../final
python final.py hk,slp1 $pathhk $pathslp1
echo "checking..."
python final.py slp1,hk $pathslp1 temp.txt
echo "next should show '0'"
diff $pathhk temp.txt | wc -l
