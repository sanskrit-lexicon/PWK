echo '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE pw SYSTEM "pw.dtd"><bibminuscref>' > diffstudy/bibminuscref.xml
while read -r line
do
	echo '<entry>'$line'</entry>' >> diffstudy/bibminuscref.xml
	grep '<ls>'$line'[0-9. ,]*</ls>' ../../../Cologne_localcopy/pw/pwxml/xml/pw.xml >> diffstudy/bibminuscref.xml
done < bibminuscref.txt
echo '</bibminuscref>' >> diffstudy/bibminuscref.xml

echo '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE pw SYSTEM "pw.dtd"><crefminusbib>' > diffstudy/crefbibintersect.xml
while read -r line
do
	echo '<entry>'$line'</entry>' >> diffstudy/crefbibintersect.xml
	grep '<ls>'$line'[0-9. ,]*</ls>' ../../../Cologne_localcopy/pw/pwxml/xml/pw.xml >> diffstudy/crefbibintersect.xml
done < crefbibintersect.txt
echo '</bibminuscref>' >> diffstudy/crefbibintersect.xml

echo '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE pw SYSTEM "pw.dtd"><crefminusbib>' > diffstudy/crefminusbib.xml
while read -r line
do
	echo '<entry>'$line'</entry>' >> diffstudy/crefminusbib.xml
	grep '<ls>'$line'[0-9. ,]*</ls>' ../../../Cologne_localcopy/pw/pwxml/xml/pw.xml >> diffstudy/crefminusbib.xml
done < crefminusbib.txt
echo '</bibminuscref>' >> diffstudy/crefminusbib.xml
