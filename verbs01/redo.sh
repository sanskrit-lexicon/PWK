#echo "remake mwverbs"
orig="../../../cologne/csl-orig/v02"
mwverbs1="../../MWS/mwverbs/mwverbs1.txt"
#python mwverb.py mw ../../mw/mw.txt mwverbs.txt
#echo "remake mwverbs1"
#python mwverbs1.py mwverbs.txt mwverbs1.txt
echo "remake pw_verb_filter.txt"
python pw_verb_filter.py ${orig}/pw/pw.txt pw_verb_exclude.txt pw_verb_include.txt pw_verb_filter.txt
echo "remake pw_verb_filter_map.txt"
python pw_verb_filter_map.py pw_verb_filter.txt pw_mw_map_edit.txt ${mwverbs1} pw_verb_filter_map.txt
echo "remake pw_preverb1.txt"
python preverb1.py slp1 ${orig}/pw/pw.txt pw_verb_filter_map.txt ${mwverbs1} pw_preverb1.txt
