sfx="$1"
if [ ! $1 ] ; then
    echo usage "sh redo_dev.sh N"
    exit 1
fi    

file=temp_pwkvn_$sfx.txt
origdir=/c/xampp/htdocs/cologne/csl-orig/v02/pwkvn
orig=$origdir/pwkvn.txt

echo "Copy $file to $orig"
cp $file $orig
#echo "Copy $filex to $origx"
#cp $filex $origx
echo
devdir=/c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue103/dev$sfx
echo "BEGIN Generate display in $devdir"
echo "-------------------------------------------------"
cd /c/xampp/htdocs/cologne/csl-pywork/v02/
root=dev_$sfx
echo
pwd
sh generate_dict.sh pwkvn $devdir
echo
echo "END generate display in $devdir"
echo "-------------------------------------------------"

cd $origdir
echo "restoring $orig"
git restore pwkvn.txt
#echo "restoring $origx"
#git restore $filex

echo "check xmlvalidity"
cd $devdir
python /c/xampp/htdocs/cologne/xmlvalidate.py pywork/pwkvn.xml pywork/pwkvn.dtd
