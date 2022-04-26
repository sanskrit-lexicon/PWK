
Installation of a new cologne dictionary based on pwkvn.

========================================================================
update steps starting with a latest version from csl-orig

========================================================================
Update steps starting from an ansi version
Choose a latest version of ansi version of digitization in ../orig directory

As example, we take the current latest version (as of 4-20-2022)
../orig/pwk1-7VN_ansi_27.txt

convert this to the slp1/utf8 form needed by csl-orig:
python ../step0/cp1252_utf8.py ../orig/pwk1-7VN_ansi_27.txt temp_pwkvn_utf8.txt
cd ../step0/final
python final.py hk,slp1 ../../install/temp_pwkvn_utf8.txt ../../install/temp_pwkvn_utf8_slp1.txt
cd ../../install
cp temp_pwkvn_utf8_slp1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt

Now proceed normally with the cologne installation from csl-pywork/v02
cd /c/xampp/htdocs/cologne/csl-pywork/v02/
sh generate_dict.sh pwkvn  ../../pwkvn
# check pwkvn.xml validity
sh xmlchk_xampp.sh pwkvn
# ok

========================================================================
Preparation  of csl-orig, etc.
========================================================================
mkdir /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn
cp temp_pwkvn_28.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt
python hwextra.py temp_pwkvn_28.txt pwkvn_hwextra.txt
cp pwkvn_hwextra.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/
cp pwkvn-meta2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/

touch /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvnheader.xml


========================================================================
/c/xampp/htdocs/cologne/csl-pywork/v02:
 DONE: edit dictparms.py
 DONE: edit redo_xampp_all.sh
 DONE: edit redo_cologne_all.sh
 TODO?: inventory.txt
 DONE: edit makotemplates/pywork/make_xml.py
 
/c/xampp/htdocs/cologne/csl-websanlexicon/v02:
 DONE: edit dictparms.py
   
 cd distinctfiles
 cp -r pw pwkvn
 edit distinctfiles/pwkvn/web/webtc/pdffiles.txt
  
 edit makotemplates/web/webtc/dictinfo.php
  insert line: (use PW images for PWKVN)
      "PWKVN"=>"//www.sanskrit-lexicon.uni-koeln.de/scans/PWScan/2014/web/pdfpages" ,
  use jpg images 
  pages pw3-257N.jpg through pw3-265N.jpg are copied from
   https://www.sanskrit-lexicon.uni-koeln.de/scans/PWScan/PWScanjpg/ into
   In ssh session:
     cd /nfs/projekt/sanskrit-lexicon/http/docs/scans/PWScan
     cp PWScanjpg/pw3-257N.jpg 2014/web/pdfpages/
     cp PWScanjpg/pw3-258N.jpg 2014/web/pdfpages/
     cp PWScanjpg/pw3-259N.jpg 2014/web/pdfpages/
cp PWScanjpg/pw3-260N.jpg 2014/web/pdfpages/
cp PWScanjpg/pw3-261N.jpg 2014/web/pdfpages/
cp PWScanjpg/pw3-262N.jpg 2014/web/pdfpages/
cp PWScanjpg/pw3-263N.jpg 2014/web/pdfpages/
cp PWScanjpg/pw3-264N.jpg 2014/web/pdfpages/
cp PWScanjpg/pw3-265N.jpg 2014/web/pdfpages/

 edit makotemplates/web/webtc/servpdfClass.php

========================================================================
 
csl-pywork/v02/distinctfiles/pwkvn/pywork/pwkvnauth/
csl-pywork/v02/distinctfiles/pwkvn/pywork/pwkvnab/
 #initially, copy from pw
 cd csl-pywork/v02/distinctfiles/
 cp -r pw pwkvn

Manually adjust files in pwkvnauth (DONE)
Manually adjust files in pwkvnab (DONE)
  Manually adjust inventory.txt, and redo_postxml.sh
TODO: add ab markup to pwkvn.txt
 NOTE: This done partially manually.

TODO: pwkvnheader.xml  currently empty.

 modify csl-pywork/v02/inventory.txt
 modify makotemplates/redo_postxml.sh for 'literary source'
 in csl-websanlexicon/v02, modify basicadjust.php and dal.php

csl-apidev editing
 servepdfClass.php
 basicadjust.php  

========================================================================
Abbreviation tooltips.
  
csl-pywork/v02/distinctfiles/pwkvn/pywork/pwkvnab/
 #initially, copy from pw
 START HERE
 modify csl-pywork/v02/inventory.txt
 modify makotemplates/redo_postxml.sh for 'literary source'
 in csl-websanlexicon/v02, modify basicadjust.php and dal.php

csl-apidev editing
 servepdfClass.php
 basicadjust.php  
 
========================================================================
========================================================================

1. /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvnheader.xml
========================================================================
