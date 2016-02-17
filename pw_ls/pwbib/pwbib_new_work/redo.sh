
python mergebibnew.py ../pwbib1.txt ../pwbib_new.txt mergebibnew.txt

python properrefs1.py mergebibnew.txt ../../pw_dhaval/abbrvwork/abbrvoutput/properrefs.txt properrefs1.txt 

python bibnew_disp1.py mergebibnew.txt properrefs1.txt bibnew_disp1.txt

python bibnew_disp2.py mergebibnew.txt properrefs1.txt tab_table.txt bibnew_disp2.txt
