version=$1
cp temp_pw_${version}.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pw  ../../pw
sh xmlchk_xampp.sh pw
cd /c/xampp/htdocs/cologne/csl-orig/v02/pw/
git restore pw.txt
cd /c/xampp/htdocs/sanskrit-lexicon/pwk/pwkissues/issue106
