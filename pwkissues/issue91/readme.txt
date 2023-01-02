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
---------------------------------------------------------
# test1.py usage 
# The input file 'test1.txt' is constructed manually
# The program does something to each line of test1.txt,
# and writes the (new) lines to result1.txt
python test1.py test1.txt result1.txt
---------------------------------------------------------
# test2.py usage
# A minor refactoring  (rearrangement) of test1.py.
# test2.py actually does the same thing as test1.py,
#  but separates out the 'tricky' part into change_one_line function
# The input test2.txt is identical to test1.txt
# test2.txt was construted by:  cp test1.txt test2.txt
# The program constructs result2.txt
python test2.py test2.txt result2.txt
# Since the input files test1.txt and test2.txt are identical,
# and since test2.py only refactored the part of test1.py that
# changes one line, we expect that result2.txt will be identical to result1.txt
# We can check this by using the 'diff' utility:
diff result1.txt result2.txt
# This will print only differences to the terminal.
# If (as in this case) there are NO differences between
# result1.txt and result2.txt, then NOTHING will be printed to terminal!
---------------------------------------------------------
---------------------------------------------------------
---------------------------------------------------------
# change_1.py usage:
python change_1.py temp_pw_0.txt change_1.txt
