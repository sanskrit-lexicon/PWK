# coding=utf-8
""" metaline.py
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
  line1 = e1.metaline
  line2 = e2.metaline
  if line1 == line2:
   continue
  lnum = e1.linenum1
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

def write_changes(fileout,changes):
 outrecs=[]
 for change in changes:
  outarr=[]
  metaline = change.metaline
  metaline = re.sub(r'<k2>.*$','',metaline)
  outarr.append('; %s' % metaline)
  # change info: 
  outarr.append('; metalines differ')
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

if __name__=="__main__":
 filein = sys.argv[1] # xxx.txt cdsl
 filein1 = sys.argv[2] # xxx.txt AB
 fileout = sys.argv[3] #
 entries_cdsl = digentry.init(filein)
 # reset Ldict
 digentry.Entry.Ldict = {}
 entries_ab = digentry.init(filein1)
 # compare_hws(entries_cdsl,entries_ab)
 maxdiff = None
 changes = compare(entries_cdsl,entries_ab,maxdiff)
 write_changes(fileout,changes)
