#-*- coding:utf-8 -*-
"""bb.py
"""
from __future__ import print_function
import sys,re,codecs
import digentry  

## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec cannot encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

class Change(object):
 def __init__(self,metaline,lnum,line,newline):
  self.metaline = metaline
  self.lnum = lnum
  self.line = line
  self.newline = newline

def compare_changes_1(e1,e2):
 """  work with first line
  check for equality up through broken bar
 """
 ans = [] # return array of change objects
 iline = 0
 line1 = e1.datalines[iline]
 line2 = e2.datalines[iline]
 if line1 == line2:
  return ans  # nothing to do
 if '¦' not in line1:
  return ans
 if '¦' not in line2:
  return ans
 line1a1 = line1.replace('¦','')
 line2a1 = line2.replace('¦','')  
 if line1a1 != line2a1:
  # there is some other difference 
  return ans
 # Yes, there is a difference in first part
 # generate new line
 newline1 = line2
 # generate change transaction
 lnum = e1.linenum1 + iline + 1
 change = Change(e1.metaline,lnum,line1,newline1)
 ans = [change]  # return as singleton array.
 return ans

def compare(entries1,entries2):
 ans = []  # array of Change objects
 #print('# entries1=',len(entries1))
 #print('# entries2=',len(entries2))
 for ientry,e1 in enumerate(entries1):
  e2 = entries2[ientry]
  changes = compare_changes_1(e1,e2)
  for change in changes:
   ans.append(change)
 #print('compare: # changes=',len(ans))
 return ans

def write_changes(fileout,changes):
 outrecs=[]
 for change in changes:
  outarr=[]
  metaline = change.metaline
  metaline = re.sub(r'<k2>.*$','',metaline)
  outarr.append('; %s' % metaline)
  # change info: 
  outarr.append('; change location of broken bar')
  lnum = change.lnum
  line = change.line
  newline = change.newline
  outarr.append('%s old %s' %(lnum,line))
  outarr.append(';')
  outarr.append('%s new %s' %(lnum,newline))
  outarr.append('; ------------------------------------------------------')
  outrecs.append(outarr)
  
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
    for out in outarr:
     f.write(out+'\n')
 print(len(changes),"changes written to",fileout)

def write(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for line in lines:
   f.write(line + '\n')
 print(len(lines),"written to",fileout)
 
if __name__=="__main__":
 filein = sys.argv[1] #  xxx. digitization v2
 filein1 = sys.argv[2] # v2
 fileout = sys.argv[3] # change file
 entries_v1 = digentry.init(filein)
 # reset Ldict
 digentry.Entry.Ldict = {}
 entries_v2 = digentry.init(filein1)

 changes = compare(entries_v1,entries_v2)

 write_changes(fileout,changes)
