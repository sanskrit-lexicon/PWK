sfx="$1"
if [ ! $1 ] ; then
    echo usage "sh redo_dev.sh N"
    exit 1
fi    

file=temp_pw_$sfx.txt
origdir=/c/xampp/htdocs/cologne/csl-orig/v02/pw
orig=$origdir/pw.txt

echo "Copy $file to $orig"
cp $file $orig
#echo "Copy $filex to $origx"
#cp $filex $origx
echo
devdir=/c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue88/dev$sfx
echo "BEGIN Generate display in $devdir"
echo "-------------------------------------------------"
cd /c/xampp/htdocs/cologne/csl-pywork/v02/ || exit 1
root=dev_$sfx
echo
pwd
sh generate_dict.sh pw $devdir
echo
echo "END generate display in $devdir"
echo "-------------------------------------------------"

cd $origdir || exit 1
echo "restoring $orig"
git restore pw.txt
#echo "restoring $origx"
#git restore $filex

echo "check xmlvalidity"
cd $devdir || exit 1
python /c/xampp/htdocs/cologne/xmlvalidate.py pywork/pw.xml pywork/pw.dtd
