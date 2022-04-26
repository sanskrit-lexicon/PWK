
for file in gtext1_known.txt gtext1_unknown.txt gtext3.txt \
            pwkvn_german_unknown.txt readme.txt unknown_merge.txt \
            unknown_x.txt unknown_x_eng.txt unknown_x_num.txt
do
    echo $file
    python ../../utf8_cp1252.py utf8/$file cp1252/$file
done
