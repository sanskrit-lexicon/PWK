# coding=utf-8
""" alldiffminor.py
"""
from __future__ import print_function
import sys, re,codecs
import digentry  

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines
 
def hwdiffs(cdsl_lines,ab_lines):
 cdsl_metas = [line for line in cdsl_lines if line.startswith('<L>')]
 ab_metas = [line for line in ab_lines if line.startswith('<L>')]
 print('cdsl has %s entries' % len(cdsl_metas))
 print('ab   has %s entries' % len(ab_metas))
 assert len(cdsl_metas) == len(ab_metas)
 diffs = []
 for iline,line in enumerate(cdsl_metas):
  line1 = ab_metas[iline]
  if line != line1:
   diff = (line,line1)
   diffs.append(diff)
 print(len(diffs),"differences in metalines")
 return diffs

def get_link(metaline):
 m = re.search(r'<L>(.*?)<pc>(.*?)<k1>',metaline)
 page = m.group(2)
 link = 'https://www.sanskrit-lexicon.uni-koeln.de/scans/csl-apidev/servepdf.php?dict=pw&page=%s' % page
 return link

class Change(object):
 def __init__(self,metaline,lnum,line,newline):
  self.metaline = metaline
  self.lnum = lnum
  self.line = line
  self.newline = newline

def compare(entries1,entries2,maxdiff):
 dbg = False
 changes = []
 for ientry,e1 in enumerate(entries1):
  e2 = entries2[ientry]
  for iline,line1 in enumerate(e1.datalines):
   line2 = e2.datalines[iline]
   if line1 == line2:
    continue
   line1a = re.sub(r'[ .,;¦]','',line1)
   line2a = re.sub(r'[ .,;¦]','',line2) 
   if line1a == line2a:
     lnum = e1.linenum1 + iline + 1
     metaline = e1.metaline
     oldline = line1
     newline = line2
     change = Change(metaline,lnum,oldline,newline)
     changes.append(change)
 print(len(changes),"changes from compare function")
 return changes

def write_outrecs(fileout,outrecs):
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outrecs),"cases written to",fileout)
 
def print_outrecs(outrecs):
 for outarr in outrecs:
  for out in outarr:
   print(out)

def compare_hws(entries1,entries2):
 nd = 0
 ntag = 0
 tagtype = None
 tag = 'ls'
 #tagtype='n'
 for ientry,e1 in enumerate(entries1):
  e2 = entries2[ientry]
  if e1.metaline == e2.metaline:
   continue
  print('metaline diff:')
  print('#1: %s' %(e1.metaline))
  print('#2: %s' %(e2.metaline))
  print()


def write_xtra(fileout,filein,outrecs):
 """ copy of filein, with markup related to outrecs.
   Purpose to facilitate corrections
 """
 # harvest metaline L from outrecs
 d = {}
 for outarr in outrecs:
  # look for <L>X<pc> (in metaline)
  for out in outarr:
   m = re.search(r'<L>(.*?)<pc>',out)
   if m:
    L = m.group(1)
    if L in d:
     print('Unexpected duplicate L')
    d[L] = True
    break
 # get the original lines
 lines = read_lines(filein)
 # modify each metaline
 newlines = []
 for line in lines:
  m = re.search(r'^<L>(.*?)<pc>',line)
  if m == None:
   newline = line
  else:
   L = m.group(1)
   if L in d:
    newline = '* ' + line
   else:
    newline = line
  newlines.append(newline)
 # write newlines
 with codecs.open(fileout,"w","utf-8") as f:
  for out in newlines:
   f.write(out+'\n')  
 print('write_extra ',len(newlines),"lines written to",fileout)

def write_outrecs(fileout,outrecs):
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outrecs),"cases written to",fileout)
 
def print_outrecs(outrecs):
 for outarr in outrecs:
  for out in outarr:
   print(out)

def compare_hws(entries1,entries2):
 nd = 0
 ntag = 0
 tagtype = None
 tag = 'ls'
 #tagtype='n'
 for ientry,e1 in enumerate(entries1):
  e2 = entries2[ientry]
  if e1.metaline == e2.metaline:
   continue
  print('metaline diff:')
  print('#1: %s' %(e1.metaline))
  print('#2: %s' %(e2.metaline))
  print()


def write_xtra(fileout,filein,outrecs):
 """ copy of filein, with markup related to outrecs.
   Purpose to facilitate corrections
 """
 # harvest metaline L from outrecs
 d = {}
 for outarr in outrecs:
  # look for <L>X<pc> (in metaline)
  for out in outarr:
   m = re.search(r'<L>(.*?)<pc>',out)
   if m:
    L = m.group(1)
    if L in d:
     print('Unexpected duplicate L')
    d[L] = True
    break
 # get the original lines
 lines = read_lines(filein)
 # modify each metaline
 newlines = []
 for line in lines:
  m = re.search(r'^<L>(.*?)<pc>',line)
  if m == None:
   newline = line
  else:
   L = m.group(1)
   if L in d:
    newline = '* ' + line
   else:
    newline = line
  newlines.append(newline)
 # write newlines
 with codecs.open(fileout,"w","utf-8") as f:
  for out in newlines:
   f.write(out+'\n')  
 print('write_extra ',len(newlines),"lines written to",fileout)

def difflist(str1,str2,dbg=False):
 import difflib
 from difflib import Differ
 x1 = str1.split()
 x2 = str2.split()
 d = difflib.Differ()
 diff = d.compare(x1, x2)
 ans1 = []
 for a in diff:
  if a.startswith('  '):
   a1 = (' ',a[2:])
  elif a.startswith('- '):
   a1 = ('-',a[2:])
  elif a.startswith('+ '):
   a1 = ('+',a[2:])
  elif a.startswith('? '):
   a1 = ('?',a[2:])
   continue  # ignore this
  else:
   print('unexpected a="%s"' % a)
  ans1.append(a1)
 if dbg:
  for a1 in ans1:
   print(a1)
 #
 ans2 = []
 for i,a1 in enumerate(ans1):
  code = a1[0]
  s = a1[1]
  if i == 0:
   a2 = code + ' ' + s
   ans2.append(a2)
   prevcode = code
  elif code == prevcode:
   ans2[-1] = ans2[-1] + ' ' + s
  else:
   a2 = code + ' ' + s
   ans2.append(a2)
   prevcode = code
 return ans2

def write_changes(fileout,changes):
 outrecs=[]
 for change in changes:
  outarr=[]
  metaline = change.metaline
  metaline = re.sub(r'<k2>.*$','',metaline)
  outarr.append('; %s' % metaline)
  # change info: 
  #outarr.append('; a')
  lnum = change.lnum
  line = change.line
  newline = change.newline
  outarr.append('%s old %s' %(lnum,line))
  # outarr.append(';')
  indent = ' '*5
  diff = difflist(line,newline)
  outarr.append('; ' + indent + 'DIFF BEGIN')
  for d in diff:
   outarr.append('; ' + indent + d)
  outarr.append('; ' + indent + 'DIFF END')   
  outarr.append('%s new %s' %(lnum,newline))
  outarr.append('; ------------------------------------------------------')
  outrecs.append(outarr)
  
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
    for out in outarr:
     f.write(out+'\n')
 print(len(changes),"changes written to",fileout)

if __name__=="__main__":
 filein = sys.argv[1] # xxx.txt cdsl
 filein1 = sys.argv[2] # xxx.txt AB
 fileout = sys.argv[3] #
 if len(sys.argv) == 6:
  # optional output
  fileout_xtra = sys.argv[4]
  fileout1_xtra = sys.argv[5]
  xtraflag = True
 else:
  xtraflag = False
 entries_cdsl = digentry.init(filein)
 # reset Ldict
 digentry.Entry.Ldict = {}
 entries_ab = digentry.init(filein1)
 compare_hws(entries_cdsl,entries_ab)
 maxdiff = None
 changes = compare(entries_cdsl,entries_ab,maxdiff)
 write_changes(fileout,changes)
 if xtraflag:
  print('skipping write_extra')
  exit(1)
  write_xtra(fileout_xtra,filein,outrecs)
  write_xtra(fileout1_xtra,filein1,outrecs)
  
