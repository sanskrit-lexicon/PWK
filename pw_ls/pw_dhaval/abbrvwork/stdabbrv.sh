# Creates the correction submission files in standard format. See https://github.com/sanskrit-lexicon/CORRECTIONS/issues/146#issuecomment-163463468 for standard format.

echo 'Creating pwbib/diffstudy/correctionsubmission/cmb.txt (cref minus pwbib0)'
python stdabbrv.py ../../pwbib/crefminusbib.txt abbrvoutput/sortedcrefs.txt ../../pwbib/pwbib1.txt > ../../pwbib/diffstudy/correctionsubmission/cmbsub.txt
echo 'Creating pwbib/diffstudy/correctionsubmission/cbi.txt (cref pwbib0 intersection)'
python stdabbrv.py ../../pwbib/crefbibintersect.txt abbrvoutput/sortedcrefs.txt ../../pwbib/pwbib1.txt > ../../pwbib/diffstudy/correctionsubmission/cbisub.txt

echo 'Creating pwbib/diffstudy/correctionsubmission/cmb.html (cref minus pwbib0)'
php displayhtml.php ../../pwbib/diffstudy/correctionsubmission/cmbsub.txt ../../pwbib/diffstudy/correctionsubmission/cmbsub.html 2
echo 'Creating pwbib/diffstudy/correctionsubmission/cbi.html (cref pwbib0 intersect)'
php displayhtml.php ../../pwbib/diffstudy/correctionsubmission/cbisub.txt ../../pwbib/diffstudy/correctionsubmission/cbisub.html 2

