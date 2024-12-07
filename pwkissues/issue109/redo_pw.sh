version=$1
echo "version $version"
cp temp_pw_$version.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pw  ../../pw
sh xmlchk_xampp.sh pw
# ok  No problems noticed
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue109
