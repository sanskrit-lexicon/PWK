#-*- coding:utf-8 -*-
"""make_numberchange2.py
"""
from __future__ import print_function
import sys, re,codecs
from parseheadline import parseheadline

class Entry(object):
 Ldict = {}
 def __init__(self,lines,linenum1,linenum2):
  # linenum1,2 are int
  self.metaline = lines[0]
  self.lend = lines[-1]  # the <LEND> line
  self.datalines = lines[1:-1]  # the non-meta lines
  # parse the meta line into a dictionary
  #self.meta = Hwmeta(self.metaline)
  self.metad = parseheadline(self.metaline)
  self.linenum1 = linenum1
  self.linenum2 = linenum2
  #L = self.meta.L
  L = self.metad['L']
  if L in self.Ldict:
   print("Entry init error: duplicate L",L,linenum1)
   exit(1)
  self.Ldict[L] = self
  self.lsarr = []
  
def init_entries(filein):
 # slurp lines
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [line.rstrip('\r\n') for line in f]
 recs=[]  # list of Entry objects
 inentry = False  
 idx1 = None
 idx2 = None
 for idx,line in enumerate(lines):
  if inentry:
   if line.startswith('<LEND>'):
    idx2 = idx
    entrylines = lines[idx1:idx2+1]
    linenum1 = idx1 + 1
    linenum2 = idx2 + 1
    entry = Entry(entrylines,linenum1,linenum2)
    recs.append(entry)
    # prepare for next entry
    idx1 = None
    idx2 = None
    inentry = False
   elif line.startswith('<L>'):  # error
    print('init_entries Error 1. Not expecting <L>')
    print("line # ",idx+1)
    print(line.encode('utf-8'))
    exit(1)
   else: 
    # keep looking for <LEND>
    continue
  else:
   # inentry = False. Looking for '<L>'
   if line.startswith('<L>'):
    idx1 = idx
    inentry = True
   elif line.startswith('<LEND>'): # error
    print('init_entries Error 2. Not expecting <LEND>')
    print("line # ",idx+1)
    print(line.encode('utf-8'))
    exit(1)
   else: 
    # keep looking for <L>
    continue
 # when all lines are read, we should have inentry = False
 if inentry:
  print('init_entries Error 3. Last entry not closed')
  print('Open entry starts at line',idx1+1)
  exit(1)

 print(len(lines),"lines read from",filein)
 print(len(recs),"entries found")
 return recs

class Change(object):
 def __init__(self,metaline,lnum,old,new):
  self.metaline = metaline
  self.lnum = lnum
  self.old = old
  self.new = new

def lookat_check(new,old):
 if new == old:
  return False
 parts = new.split(' ')
 subparts = [part.split(',') for part in parts]
 lens = set([len(subpart) for subpart in subparts])
 if len(lens) == 1:
  return False
 m = re.search(r'^[0-9]+,[0-9]+[.] [0-9]+[.]?$',new)
 if m != None:
  return False  
 return True  # cannot confirm form of new.

def changeline2(line):
 lookats = []
 def f(m):
  ans = m.group(0)
  ls = m.group(1)
  lsnum = m.group(1)  
  # revise lsnum
  # replace period-digit with period-space-digit
  lsnum1 = re.sub(r'[.]([0-9])',r'. \1',lsnum)
  # replace nonspace-leftparen with nonspace-space-leftparen
  lsnum1 = re.sub(r'([^ ])\(',r'\1 (',lsnum1)
  # reconstruct lsnew
  lsnew = lsnum1
  if lookat_check(lsnum1,lsnum):
   lookats.append(lsnum1)
   
  ans = '<ls>%s</ls>'%lsnew
  return ans
 #
 # ls cases that start with a number
 newline = re.sub(r'<ls>([0-9].*?)</ls>',f,line)
 return newline,lookats

def write_changes(fileout,changes):
 outrecs = []
 for change in changes:
  outarr = []
  outarr.append('; -------------------------------------')
  outarr.append('; ' + change.metaline)
  outarr.append('%s old %s' %(change.lnum,change.old))
  outarr.append('; ')
  outarr.append('%s new %s' %(change.lnum,change.new))
  outrecs.append(outarr)
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(outrecs),"records written to",fileout)

if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx
 fileout = sys.argv[2] # change_X
 
 entries = init_entries(filein)

 changes = []  # list of change records
 nlook = 0
 for entry in entries:
  for iline,line in enumerate(entry.datalines):
   newline,lookats = changeline2(line)
   if newline != line:
    lnum = entry.linenum1+iline+1
    newline1 = newline
    for lookat in lookats:
     newline1 = newline1.replace(lookat,'[%s]'%lookat)
    metaline = re.sub(r'<k2>.*$','',entry.metaline)
    change = Change(metaline,lnum,line,newline1)
    changes.append(change)
    if lookats != []:
     #print(metaline,lookats)
     nlook = nlook + 1
 write_changes(fileout,changes)
 print(nlook,'to look at')
 
