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
# test3.py usage
# A minor refactoring  (rearrangement) of test2.py.
# test3.py actually does the same thing as test2.py,
#  but without surplus function re.findall
# The input test3.txt is identical to test1.txt and to test2.txt
# The program constructs result3.txt
python test3.py test1.txt result3.txt
---------------------------------------------------------
# test4.py usage
# Modify write_lines to show both lines and newlines, for easy comparison
# Change_one_line is the same as in test3.py
# We reuse the input file test1.txt
# The program constructs result4.txt
python test4.py test1.txt result4.txt
---------------------------------------------------------
# test5.py usage
# Use re.search to learn about 'match-groups'
python test5.py "PATTERN" "LINE"
Program executes 'm = re.search(PATTERN,LINE)'
 The value of 'm' is either NONE or a Match object.
 program prints the substring of LINE matching PATTERN,
 and, if there are groups in PATTERN, information about the groups.
 PATTERN has a 'group' if there is a sub-pattern enclosed in parens,
   Example PATTERN = "(dog|cat).*(runs|jumps)"  has two groups
---------------------------------------------------------
# test6.py usage
# A minor refactoring  (rearrangement) of test4.py.
# But now we use more flexible patterns
# This program constructs the 'DIFFERENT' lines by more otimal way
python test6.py test1.txt result6.txt
---------------------------------------------------------
# test7.py usage
# first attempt to use a function as 2nd ('repl') argument of re.sub
# program does not work quite right, mainly because of function
# FUNCTION_new_pattern.
python test7.py test1.txt result7.txt
---------------------------------------------------------
# test8.py usage
# revision of test7, correcting FUNCTION_new_pattern
# FUNCTION_new_pattern.
# also slightly changed the pattern and repl in FUNCTION_new_pattern
python test8.py test8.txt result8.txt
# Also, run test8 with a new test file (test8a.txt)
python test8.py test8a.txt result8a.txt
---------------------------------------------------------
# change_test1.py usage:
# limit number of changes to 10.  Add temporary [[...]] markup to
# changed lines, so we can more easily identify what our patterns
# are finding. 
python change_test1.py temp_pw_0.txt change_test1.txt
---------------------------------------------------------
# change_test3.py usage:
# A minor changing of change_test2.py (modifies change_test1.py, using the ideas of test8)
# Add temporary [[...]] markup to
# changed lines, so we can more easily identify what our patterns
# are finding. 
python change_test3.py temp_pw_0.txt change_test3.txt
---------------------------------------------------------
# change_1.py usage:
# A minor changing of change_test2.py (modifies change_test1.py, using the ideas of test8)
# Removed temporary [[...]] markup to changed lines
python change_1.py temp_pw_0.txt change_1.txt
