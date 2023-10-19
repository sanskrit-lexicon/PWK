#-*- coding:utf-8 -*-
"""change_multiple_headwords.py
 
"""
from __future__ import print_function
import sys,re,codecs
import digentry  


def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def count_ab(lines):
 asdict = {}
 n = 0
 regexraw = r'<ab (.*?)>(.*?)</ab>'
 regex = re.compile(regexraw)
 for line in lines:
  n = n + 1
  tags = re.findall(regex,line)
  for c in tags:
   #print("count_ab:",c)
   #exit(1)
   # ('n="Noth"', 'N.')  
   if c not in asdict:
    asdict[c] = 0
   asdict[c] = asdict[c] + 1
 return asdict

#def get_local_abbrev_dict(lines):
# # key for d is like: ('n="Noth"', 'N.')
# d = count_ab(lines)
# return d

def make_changes_1(entries1,entries2):
 # returns list of changes for entries1
 regexraw = r'{#.*?#}'
 regex = re.compile(regexraw)
 changes = []
 for ientry,e1 in enumerate(entries1):
  e2 = entries2[ientry]
  #  key for d2 is like: ('n="Noth"', 'N.')
  d2 = count_ab(e2.datalines)
  for iline1,line1 in enumerate(e1.datalines):
   # differences in number of headwords
   if iline1 != 0:
    # only the FIRST line of entry is relevant
    continue
   line2 = e2.datalines[iline1]
   parts1 = line1.split('¦')
   parts2 = line2.split('¦')
   if not ((len(parts1) == 2) and (len(parts2) == 2)):
    print('unexpected',e1.metaline,len(parts1), len(parts2))
    print(line1)
    print(line2)
    print()
    continue

   # number of 'sanskrit' texts fragments
   nfrag1 = len(re.findall(regex,parts1[0]))
   nfrag2 = len(re.findall(regex,parts2[0]))
   if nfrag1 == nfrag2:
    continue
   # when number of fragments differs, generate change transaction
   metaline = e1.metaline
   line1_new = line2  # take the complete line from second source
   lnum = e1.linenum1 + iline1 + 1
   change = Change(metaline,lnum,line1,line1_new,nfrag1,nfrag2)
   changes.append(change)
 return changes

class Change(object):
 def __init__(self,metaline,lnum,line,newline,nfrag_old,nfrag_new):
  self.metaline = metaline
  self.lnum = lnum
  self.line = line
  self.newline = newline
  self.nfrag_old = nfrag_old
  self.nfrag_new = nfrag_new

def write_changes(fileout,changes):
 outrecs=[]
 for change in changes:
  outarr=[]
  metaline = change.metaline
  metaline = re.sub(r'<k2>.*$','',metaline)
  outarr.append('; %s' % metaline)
  outarr.append('; # headwords: %s -> %s' %(change.nfrag_old,change.nfrag_new))
  outarr.append('; --------------------')
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

def writelines(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for iline,line in enumerate(lines):
   f.write(line+'\n')
 print(len(lines),"records written to",fileout)

if __name__=="__main__":
 filein = sys.argv[1] # xxx.txt cdsl
 filein1 = sys.argv[2]  # xxx.txt AB
 fileout = sys.argv[3] # change.txt
 entries_cdsl = digentry.init(filein)
 # reset Ldict
 digentry.Entry.Ldict = {}
 entries_ab = digentry.init(filein1)
 changes = make_changes_1(entries_cdsl,entries_ab)
 write_changes(fileout,changes)

