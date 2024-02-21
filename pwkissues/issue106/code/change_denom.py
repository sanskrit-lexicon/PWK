# coding=utf-8
""" change_denom.py
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for out in lines:
   f.write(out+'\n')  
 print(len(lines),"lines written to",fileout)

def write_recs(fileout,outrecs,printflag=True,blankflag=True):
 # outrecs is array of array of lines
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
   if blankflag:
    out = ''  # blank line separates recs
    f.write(out+'\n')
 if printflag:
  print(len(outrecs),"records written to",fileout)

class Change:
 def __init__(self,metaline,lnum,old,new):
  self.metaline = metaline
  self.lnum = lnum
  self.old = old
  self.new = new

def make_changes(lines):
 changes = []
 for iline,line in enumerate(lines):
  m = re.search(r'(<L>.*)$',line)
  if not line.startswith('<L>'):
   continue
  metaline = line
  iline1 = iline + 1
  old = lines[iline1]
  lnum = iline1 + 1
  new = re.sub(r'^({#[^#]*y#}¦, {#°yat[ie]#})',r'!√\1',old)
  if new == old:
   continue
  change = Change(metaline,lnum,old,new)
  changes.append(change)
 return changes

def write_changes(fileout,changes):
 outrecs = []
 outarr = [] # header
 outarr.append('; ******************************************************')
 outarr.append('; %s changes:' % len(changes))
 outarr.append('; ******************************************************')
 outrecs.append(outarr)
 for c in changes:
  outarr = []
  outarr.append('; %s' % c.metaline)
  lnum = int(c.lnum)
  # change 
  outarr.append('%s old %s' %(lnum,c.old))
  outarr.append(';')
  outarr.append('%s new %s' %(lnum,c.new))
  outarr.append('; ----------------------------------------------')
  outrecs.append(outarr)
 write_recs(fileout,outrecs,blankflag=False)

if __name__=="__main__":
 filein = sys.argv[1]  # pw.txt
 fileout = sys.argv[2]  # change file 

 lines = read_lines(filein)
 changes = make_changes(lines)
 write_changes(fileout,changes)

