#-*- coding:utf-8 -*-
"""change_althws.py
 
"""
from __future__ import print_function
import sys,re,codecs
import digentry  

class Change(object):
 def __init__(self,metaline,lnum,line,newline,lnum1,line1,newline1):
  self.metaline = metaline
  self.lnum = lnum
  self.line = line
  self.newline = newline
  self.lnum1 = lnum1
  self.line1 = line1
  self.newline1 = newline1
  
def replace_2nd_hw(line):
 parts = re.split(r'(<hw>.*?</hw>)',line)
 newparts = []
 ihw = 0
 for part in parts:
  if not part.startswith('<hw>'):
   newpart = part
  elif ihw == 0:
   newpart = part
   ihw = ihw + 1
  else:
   newpart = re.sub(r'</?hw>','',part)
   ihw = ihw + 1
  newparts.append(newpart)
 newline = ''.join(newparts)
 return newline

def make_changes(entries,noaltsd):
 changes = []
 for ientry,entry in enumerate(entries):
  L = entry.metad['L']
  if L not in noaltsd:
   continue
  # first line contains althws: remove it
  if len(entry.datalines) != 2:
   print('make_changes anomaly at L=',L)
   continue
  iline = 0
  line = entry.datalines[iline]
  lnum = entry.linenum1 + iline + 1
  newline = ''
  iline1 = 1
  lnum1 = entry.linenum1 + iline1 + 1
  line1 = entry.datalines[iline1]
  newline1 = replace_2nd_hw(line1)
  metaline = entry.metaline
  change = Change(metaline,lnum,line,newline,lnum1,line1,newline1)
  changes.append(change)
 print(len(changes),'Change transactions found')
 return changes

def write_changes(fileout,changes):
 outrecs=[]
 for change in changes:
  outarr=[]
  metaline = change.metaline
  metaline = re.sub(r'<k2>.*$','',metaline)
  outarr.append('; %s' % metaline)
  lnum = change.lnum
  line = change.line
  newline = change.newline
  outarr.append('%s old %s' %(lnum,line))
  outarr.append('%s new %s' %(lnum,newline))
  outarr.append(';')
  lnum = change.lnum1
  line = change.line1
  newline = change.newline1
  outarr.append('%s old %s' %(lnum,line))
  outarr.append('%s new %s' %(lnum,newline))  
  outarr.append('; ---------------------------')
  outrecs.append(outarr)
  
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
    for out in outarr:
     f.write(out+'\n')
 print(len(changes),"changes written to",fileout)

def unused_write(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for iline,line in enumerate(lines):
   f.write(line+'\n')
 print(len(lines),"records written to",fileout)

def init_noalts(filein):
 d = {}
 with codecs.open(filein,"r","utf-8") as f:
  recs = []
  for iline,line in enumerate(f):
   line = line.rstrip('\r\n')
   if line.startswith(';'):
    continue
   m = re.search(r'^<L>([0-9]+)',line)
   L = m.group(1)
   if L in d:
    print('duplicate L at line',iline+1)
    continue
   d[L] = True
   recs.append(L)
 print(len(recs),"L numbers read from",filein)
 return d

if __name__=="__main__":
 filein = sys.argv[1] # pwkvn.txt
 filein1 = sys.argv[2] # noalt lines
 fileout = sys.argv[3] # change.txt

 entries = digentry.init(filein)
 noaltsd = init_noalts(filein1)
 changes = make_changes(entries,noaltsd)
 write_changes(fileout,changes)

 
