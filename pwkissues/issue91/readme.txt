Refer https://github.com/sanskrit-lexicon/PWK/issues/91

Implementation steps

---------------------------------------------------------
temp_pw_0.txt
This will be the latest version of csl-orig/v02/pw/pwtxt.
It's name starts with 'temp';
  By ./gitignore of this repository, files whose names start with 'temp'
  are not tracked by git.
Make 'pwk/pwissues/issue91/temp_pw_0.txt' to be a copy of
 'csl-orig/v02/pw/pw.txt'.  Do this however convenient.
Jim's method
cd /c/xampp/htdocs/sanskrit-lexicon/pwk/pwkissues/issue91
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw_0.txt
---------------------------------------------------------
Sample program to create a 'change' file.
This is for changing 'Pron.' to 'Pronoun'.
We don't really want to do this, it's just an example.
python change_sample.py temp_pw_0.txt change_sample.txt
# apply changes
python updateByLine.py temp_pw_0.txt change_sample.txt temp_pw_sample.txt
