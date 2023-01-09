# coding=utf-8
""" temp_change_test2.py
  # uses the repl function of test8
"""
from __future__ import print_function
import sys, re,codecs
import digentry

class Change(object):
 def __init__(self,iline,newline):
  self.iline = iline # index into entry.datalines
  # the old line is entry.datalines[iline]
  self.newline = newline # the new line

def change_line_helper(m):
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
 if newtext != text:
  # Put brackets around changed text.  THIS IS FOR DEBUGGING ONLY
  newtext = '[[%s]]' % newtext
 return newtext

def change_line(line):
 pattern = r'{%.*?%}'
 repl = change_line_helper
 newline = re.sub(pattern,repl,line)
 return newline

def make_changes(entries):
 # add 'changes' attribute to each each entry.
 # changes will be a list of Change objects.
 n = 0
 for entry in entries:
  changes = []
  for iline,line in enumerate(entry.datalines):
   if n >= 10: break
   newline = change_line(line)
   if newline == line:
    # Our replacement didn't change the line. Don't generate a change
    continue
   # Our replacement DID change the line. DO generate a Change object
   n = n + 1  # count this change (for debugging)
   
   change = Change(iline,newline)
   # Append change to list of changes for this entry
   changes.append(change)
  # bottom of for iline loop
  # add the 'changes' attribute to the entry
  entry.changes = changes
  
def write_changes(fileout,entries):
 # get total number of lines changed, for documentation
 nchange = 0 # total number of changes
 nechange = 0 # # number of entries with 1 or more changes
 for entry in entries:
  nchange = nchange + len(entry.changes)
  if len(entry.changes) != 0:
   nechange = nechange + 1
 # generate useful print statement
 print('%s  (%s changes in %s entries) ' % (fileout,nchange,nechange))
 # prepare arrays of output 'records'
 # consisting of a  title, and a record for each entry with a change
 outrecs = []  
 # title section
 outarr = []
 # initial comma means this is a 'comment' in a change file.
 outarr.append('; **********************************************************')
 outarr.append('; %s  (%s changes in %s entries) ' % (fileout,nchange,nechange))
 outarr.append('; **********************************************************')
 outrecs.append(outarr)
 # output records for each entry with a change
 for entry in entries:
  # title for this subsection of changes
  changes = entry.changes
  n = len(entry.changes)
  if n == 0:
   continue # no lines changed in this entry
  outarr = []  # lines in change file for changes in this entry.
  # subtitle for the change(s) in this entry
  outarr.append('; ----------------------------------------------------------')
  # shorten the metaline
  meta = re.sub(r'<k2>.*$','',entry.metaline)
  outarr.append('; (%s) %s' % (n,meta)) 
  outarr.append('; ----------------------------------------------------------')
  # section for each change
  for ichange,change in enumerate(changes):
   if ichange != 0:
    # a separator from previous change
    outarr.append('; ..................................')
   # now for the change
   # unpack the attributes for this change
   iline = change.iline
   newline = change.newline
   # get the line number of the line in the digitization file
   # linenum1 is the line number of the metaline in the file.
   lnum = entry.linenum1 + iline + 1
   # the old line
   oldline = entry.datalines[iline]
   # now prepare for output of the transaction
   outarr.append('%s old %s' %(lnum,oldline))
   outarr.append('%s new %s' %(lnum,newline))
  # append the lines for changes in this entry as another 'record' of output
  outrecs.append(outarr)
 # --- now we send all lines of all outrecs to our output file
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 
if __name__=="__main__":
 filein = sys.argv[1] # (old) digitization
 fileout = sys.argv[2] # change file
 # get list of Entry records from digitization
 # For structure of an entry record,
 # see __init__ of Entry class in digentry.py
 entries = digentry.init(filein)
 # add a 'changes' attribute to each entry
 make_changes(entries)
 # generate output
 write_changes(fileout,entries)
 
