PW=../../../../pwxml/pw.xml
if !([ -e $PW ])
 then
  echo "path to PW does not exist: $PW"
  echo "See pw_dhaval/readme.md for where to get pw.xml"
  exit 1
fi

python abbrv.py $PW
echo "Converting the Anglicized Sanskrit to IAST"
echo 
python transcoder/as_roman.py abbrvoutput/sortedcrefs.txt abbrvoutput/sortedcrefsiast.txt as roman
echo "Preparing dislpay.html for viewing."
php displayhtml.php
