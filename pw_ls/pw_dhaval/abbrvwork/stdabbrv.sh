# Creates the correction submission files in standard format. See https://github.com/sanskrit-lexicon/CORRECTIONS/issues/146#issuecomment-163463468 for standard format.

python stdabbrv.py ../../pwbib/crefminusbib.txt abbrvoutput/sortedcrefs.txt > ../../pwbib/diffstudy/correctionsubmission/cmbsub.txt
python stdabbrv.py ../../pwbib/bibminuscref.txt abbrvoutput/sortedcrefs.txt > ../../pwbib/diffstudy/correctionsubmission/bmcsub.txt
python stdabbrv.py ../../pwbib/crefbibintersect.txt abbrvoutput/sortedcrefs.txt > ../../pwbib/diffstudy/correctionsubmission/cbisub.txt

