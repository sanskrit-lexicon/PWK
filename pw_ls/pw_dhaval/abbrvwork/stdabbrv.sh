# Creates the correction submission files in standard format. See https://github.com/sanskrit-lexicon/CORRECTIONS/issues/146#issuecomment-163463468 for standard format.

echo 'Creating cref minus bib file'
python stdabbrv.py ../../pwbib/crefminusbib.txt abbrvoutput/sortedcrefs.txt > ../../pwbib/diffstudy/correctionsubmission/cmbsub.txt
echo 'Creating cref bib intersect file'
python stdabbrv.py ../../pwbib/crefbibintersect.txt abbrvoutput/sortedcrefs.txt > ../../pwbib/diffstudy/correctionsubmission/cbisub.txt

echo 'Creating cref minus bib HTML file'
php displayhtml.php ../../pwbib/diffstudy/correctionsubmission/cmbsub.txt ../../pwbib/diffstudy/correctionsubmission/cmbsub.html 2
echo 'Creating cref bib intersect HTML file'
php displayhtml.php ../../pwbib/diffstudy/correctionsubmission/cbisub.txt ../../pwbib/diffstudy/correctionsubmission/cbisub.html 2

