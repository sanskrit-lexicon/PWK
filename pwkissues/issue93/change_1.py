# coding=utf-8
""" change_1.py
"""
from __future__ import print_function
import sys, re,codecs
import digentry

class Change(object):
 def __init__(self,iline,newline):
  self.iline = iline # index into entry.datalines
  # the old line is entry.datalines[iline]
  self.newline = newline # the new line

def get_newline(line,option):
 if option == '1':
  newline = re.sub(r'<ls>([0-9]+,[0-9]+)</ls>',
                   r'<ls n="Chr.">\1</ls>',line)
  return newline
 if option == '2':
  newline = re.sub(r'<ls>([0-9]+,[0-9]+[.]?)</ls>',
                   r'<ls n="Chr.">\1</ls>',line)
  return newline
 if option == '3':
  newline = re.sub(r'<ls>([0-9]+),([0-9]+[.]) ([0-9]+[.]?)</ls>',
                   r'<ls n="Chr.">\1,\2</ls> <ls n="Chr. \1,">\3</ls>',line)
  return newline
 if option == '3':
  newline = re.sub(r'<ls>([0-9]+),([0-9]+[.]) ([0-9]+[.]?)</ls>',
                   r'<ls n="Chr.">\1,\2</ls> <ls n="Chr. \1,">\3</ls>',line)
  return newline
 if option == '4':
  newline = re.sub(r'<ls>([0-9]+,[0-9]+[.]) ([0-9]+,[0-9]+[.]?)</ls>',
                   r'<ls n="Chr.">\1</ls> <ls n="Chr.">\2</ls>',line)
  return newline
 if option == '5':
  newline = re.sub(r'<ls>([0-9]+,[0-9]+[.]) ([0-9]+,[0-9]+[.]) ([0-9]+,[0-9]+[.]?)</ls>',
                   r'<ls n="Chr.">\1</ls> <ls n="Chr.">\2</ls> <ls n="Chr.">\3</ls>',line)
  return newline
 if option == '6':
  def f6(m):
   body = m.group(1)
   parts = body.split(' ')
   newparts = []
   nparts = len(parts)
   ok = True  # are all parts of form number,number ?
   for ipart,part in enumerate(parts):
    ok = False
    if (ipart+1) == nparts: # ending period optional 
     if re.search(r'^[0-9]+,[0-9]+[.]?$',part):
      ok = True
    else: # not the last one. ending period required
     if re.search(r'^[0-9]+,[0-9]+[.]$',part):
      ok = True
    if not ok:
     break
    newpart = '<ls n="Chr.">%s</ls>' % part
    newparts.append(newpart)
   if not ok:
    newbody = '<ls>%s</ls>' % body  # no change
   else:
    newbody = ' '.join(newparts)
   return newbody
  newline = re.sub(r'<ls>([0-9][0-9., ]+)</ls>',f6,line)
  return newline
 print('get_newline ERROR: unknown option ',option)
 exit(1)
 
def make_changes(entries,option):
 # add 'changes' attribute to each each entry.
 # changes will be a list of Change objects.
 n = 0
 for entry in entries:
  changes = []
  # metaline = entry.metaline
  # lnummeta = entry.linenum1
  for iline,line in enumerate(entry.datalines):
   newline = get_newline(line,option)
   if newline == line:
    # Our replacement didn't change the line. Don't generate a change
    continue
   # Our replacement DID change the line. DO generate a Change object
   change = Change(iline,newline)
   # Append change to list of changes for this entry
   changes.append(change)
  # bottome of for iline loop
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
 option = sys.argv[1]
 filein = sys.argv[2] # (old) digitization
 fileout = sys.argv[3] # change file
 # get list of Entry records from digitization
 # For structure of an entry record,
 # see __init__ of Entry class in digentry.py
 entries = digentry.init(filein)
 # add a 'changes' attribute to each entry
 make_changes(entries,option)
 # generate output
 write_changes(fileout,entries)
 
