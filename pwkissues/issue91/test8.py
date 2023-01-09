# coding=utf-8
"""test8.py  see readme.txt for usage
   
"""
from __future__ import print_function
import sys,re,codecs

# def f(x,y,z):  that's the way Python function definitions start
def read_lines(filein):
 # Notice the indentation
 # there's a lot packed into the next line.
 # We could say:
 #  open file named filein for reading. The file is encoded as utf-8.
 #  Use the variable 'f' for reading from the file. 'f' could be
 #  called the 'file handle'.
 with codecs.open(filein,"r","utf-8") as f:
  # Notice the further indentation
  # Read every line in the file, and strip from the end of each
  # line the line-ending characters '\r\n'
  # And, add each stripped line into the Python list named 'lines'
  lines = [line.rstrip('\r\n') for line in f]
 # Notice we have gone back to 1 character of indentation (same as 'with')
 # print to the 'console' a message indicating how many lines were read
 print(len(lines),"lines read from",filein)
 # the function returns the list of lines
 return lines

def FUNCTION_new_pattern(m):
 # This function is passed as the 'repl' argument of re.sub in change_one_line
 # 'm' is a 'Match' object which matches the 'pattern' of
 #   the re.sub in change_one_line.
 #  m.group(0) is the text matching pattern of change_one_line's re.sub
 # i.e., in this case, m.group(0) = {%...%}
 text = m.group(0)  # {%...%}
 # within text, we can change all ' {#...#} ' to '%} {#...#} {#'
 pattern = ' {#([^#]*)#} '
 repl = r'%} {#\1#} {%'
 newtext = re.sub(pattern,repl,text)
 # return newtext.  It will replace the string matched
 # by re.sub in change_one_line
 #NOTE: This logic does not completely handle cases
 # with two Devanagari sections within italics
 # Thus we write a warning note
 if False:
  devas = re.findall(r'{#.*?#}',text)
  if len(devas) > 1:
   print('TWO-DEVA WARNING: ',text)
 return newtext

def FUNCTION_new_pattern(m):
 # This function is passed as the 'repl' argument of re.sub in change_one_line
 # 'm' is a 'Match' object which matches the 'pattern' of
 #   the re.sub in change_one_line.
 #  m.group(0) is the text matching pattern of change_one_line's re.sub
 # i.e., in this case, m.group(0) = {%...%}
 text = m.group(0)  # {%...%}
 # within text, we can change all ' {#...#} ' to '%} {#...#} {#'
 pattern = ' {#([^#]*)#} '
 repl = r'%} {#\1#} {%'
 newtext = re.sub(pattern,repl,text)
 # return newtext.  It will replace the string matched
 # by re.sub in change_one_line
 return newtext

def change_one_line(line):
 pattern = r'{%.*?%}'
 newline =  re.sub(pattern, FUNCTION_new_pattern, line)
 return newline
 
def change_lines(lines):
 newlines = []  # start with an empty list, in which the new lines will be put
 # adjust each line in a python 'for loop'
 for line in lines:
  # All the work required to get newline is now done in change_one_line
  # This refactoring means that further refinement of how we get
  # newline can be accomplished by modifying change_one_line function
  newline = change_one_line(line)
  newlines.append(newline)
 return newlines
 
def write_lines(fileout,oldlines,newlines):
 # Note we call this function as 'write_lines(fileout,lines,newlines)'.
 # In this function, the function parameter 'oldlines' will, when
 # called, have the value lines.
 # open the file, but this time for 'writing'
 with codecs.open(fileout,"w","utf-8") as f:
  # write each line using a for loop
  # use enumerate to coordinate between the two 'parallel' arrays,
  #  oldlines and newlines
  for iline,oldline in enumerate(oldlines):
   # iline is the index into oldlines.  The first value of iline is 0
   # then 1, 2, ....  The last value of iline is len(oldlines)-1
   # oldline is the same as oldlines[iline]
   # Similarly, the newline corresponding to oldlines is newlines[iline]
   newline = newlines[iline]
   # We will format a 'transaction' for this particular oldline,newline pair
   # The transaction will generate several lines of output, with the
   # aim of making visual comparison easy.
   # The lines of transaction will be in an array 'outarr' of strings.
   outarr = []  # starts out as empty array (or list)
   # -----------------------------------------------
   # first line of transaction will show
   # a) the transaction number, based on iline
   itran = iline + 1  # itran will be 1 for first transaction, 2 for 2nd
   # b) the 'status' based on whether newline == oldline or newline != oldline
   if newline == oldline:
    status = 'SAME'  # newline and oldline are the same
   else:
    status = 'DIFFERENT' # newline is changed from oldline
   # Construct an easy to read message from itran and status
   # start with semicolon to indicate 'comment'
   out = '; line %s: newline and oldline are %s' %(itran,status)
   # Add this line to outarr list
   outarr.append(out)
   # -----------------------------------------------
   # second line will show oldline, identified as OLDLINE
   out = 'OLDLINE %s' % oldline
   outarr.append(out)
   # -----------------------------------------------
   # next line will show newline, identified as NEWLINE
   out = 'NEWLINE %s' % newline
   outarr.append(out)
   # ------------------------------------------------
   # last line will be a 'separator between this transaction
   # and next transaction
   outarr.append('; -----------------------------------------------------')
   # -------------------------------------------------------
   # now write all the transaction lines
   for out in outarr:
    # add the 'newline' line break character at the end of the line
    f.write(out+'\n')
   # this is the last line of the 'for iline,oldline ' loop.
  # This is the first statement AFTER the 'for iline,oldline ' loop.
  # note it is indented the same as the 'for iline' loop statement
  # The program now goes back up to the top of the loop, giving
  # us the next iline, oldline in the enumeration of oldlines
  # When there are no more oldlines, the program contines with the
  # In our program, this is also the last line of the 'with' block.
 # This is first statement AFTER the 'with' block
 # Note it is indented the same as the 'with ..' statement
 print(len(oldlines),"old/new transactions written to",fileout)
 # This function doesn't explicitly return anything.
 # Since there is no 'return', it implicitly returns the special value None
if __name__=="__main__":
 # First input argument: path to input text file
 filein = sys.argv[1]
 # Second input argument: path to output text file
 fileout = sys.argv[2] # word frequency
 # Call function read_lines to get all the input lines into
 #  a python list 'lines'
 lines = read_lines(filein)
 # Call function adjustlines to do something to each line
 # Result is the list newlines
 newlines = change_lines(lines)
 # write both lines and newlines to fileout
 write_lines(fileout,lines,newlines)
 # That's all this little program does

 
