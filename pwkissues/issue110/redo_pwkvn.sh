version=$1
echo "version $version"
cp temp_pwkvn_$version.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwkvn  ../../pwkvn
sh xmlchk_xampp.sh pwkvn
# ok  No problems noticed
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue110

