sfx="$1"
if [ ! $1 ] ; then
    echo usage "sh redo.sh N"
    exit 1
fi    
 
file=temp_pw_ab_$sfx.txt
# filex=pw_hwextra.txt
origdir=/c/xampp/htdocs/cologne/csl-orig/v02/pw
orig=$origdir/pw.txt
#origx=$origdir/$filex
echo "Copy $file to $orig"
cp $file $orig
#echo "Copy $filex to $origx"
#cp $filex $origx
echo
devdir=/c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue95/dev$sfx
echo "BEGIN Generate display in $devdir"
echo "-------------------------------------------------"
cd /c/xampp/htdocs/cologne/csl-pywork/v02/
root=dev_$sfx
echo
pwd
sh generate_dict.sh pw $devdir
echo
echo "END generate display in $devdir"
echo "-------------------------------------------------"

cd $origdir
echo "restoring $orig"
git restore pw.txt
#echo "restoring $origx"
#git restore $filex

