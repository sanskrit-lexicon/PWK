
Start with version 27: ../../orig/pwk1-7VN_ansi_27.txt
python ../cp1252_utf8.py ../../orig/pwk1-7VN_ansi_27.txt temp_pwkvn_27_hk.txt

cp temp_pwkvn_27_hk.txt temp_pwkvn_28_hk.txt
we allow manual changes in temp_pwkvn_28_hk.txt.
For instance, added <as1>X</as1> markup.

python ../diff_to_changes.py temp_pwkvn_27_hk.txt temp_pwkvn_28_hk.txt changes_28.txt
82 changes written to changes_28.txt


sh install.sh 28
filein=temp_pwkvn_28_hk.txt
92049 lines read from ../lsnum/temp_pwkvn_28_hk.txt
92049 records written to ../lsnum/temp_pwkvn_28_slp1.txt
check_as found 0 problems
checking...
92049 lines read from ../lsnum/temp_pwkvn_28_slp1.txt
92049 records written to ../lsnum/temp.txt
next should show '0'
0

convert to ansi and save in orig
python ../utf8_cp1252.py temp_pwkvn_28_hk.txt ../../orig/pwk1-7VN_ansi_28.txt


========================================================================
python lsnum.py temp_pwkvn_28_hk.txt temp_pwkvn_29_hk.txt.

python ../diff_to_changes.py temp_pwkvn_28_hk.txt temp_pwkvn_29_hk.txt temp_changes_29.txt
11708 changes written to temp_changes_29.txt

sh install.sh 29
filein=temp_pwkvn_29_hk.txt
92049 lines read from ../lsnum/temp_pwkvn_29_hk.txt
92049 records written to ../lsnum/temp_pwkvn_29_slp1.txt
check_as found 0 problems
checking...
92049 lines read from ../lsnum/temp_pwkvn_29_slp1.txt
92049 records written to ../lsnum/temp.txt
next should show '0'
0

cp temp_pwkvn_29_slp1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwkvn  ../../pwkvn
sh xmlchk_xampp.sh pwkvn
python3 ../../xmlvalidate.py ../../pwkvn/pywork/pwkvn.xml ../../pwkvn/pywork/pwkvn.dtd
ok
========================================================================
temp_pwkvn_30_hk.txt  copy of temp_pwkvn_29_hk.txt.
Manually edited.
First for 700 patterns like </ls> [0-9]

</ls> <ls n=""></ls>

@ = </ls>

fgg.
fg.
a. a. O.
v. l.
v. u.
v. a.

sh install.sh 30
cp temp_pwkvn_30_slp1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt

========================================================================
summary
compare to /c/xampp/htdocs/sanskrit-lexicon/PWK/pw_ls/summary/lsextract_all.py

cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pwkvn/pywork/pwkvnauth/pwkvnbib_input.txt temp_pwkvn_tooltip.txt

python lsextract_all.py temp_pwkvn_29_slp1.txt temp_pwkvn_tooltip.txt lsextract_pwkvn.txt

========================================================================
