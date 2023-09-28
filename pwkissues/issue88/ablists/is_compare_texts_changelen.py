# coding=utf-8
""" is_compare_texts_changelen.py
"""
from __future__ import print_function
import sys, re,codecs
import digentry  

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

class Change(object):
 def __init__(self,a1,a2):
  self.a1 = a1  # array
  self.a2 = a2
  self.metaline = None # set later
  assert len(a1) == len(a2)

def get_metafield(f,meta):
 if f == 'k2':
  if '<h>' in meta:
   regex = r'<%s>(.*?)<' % f
  else:
   regex = r'<%s>(.*?)$' % f
 else:
  regex = r'<%s>(.*?)<' % f
 m = re.search(regex,meta)
 value = m.group(1)
 return value

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

def write_difftext(fileout,e1s,e2s):
 outrecs = []
 n = 0
 no = 0
 for i,e1 in enumerate(e1s):
  e2 = e2s[i]
  if e1.text == e2.text:
   n = n + 1
  else:
   no = no + 1
   if no < 5:
    print(e1.metaline)
    print('cdsl text\n',e1.text)
    print()
    print('ab text\n',e2.text)
   
 print(n,'entries have same text')
 
def get_link(metaline):
 m = re.search(r'<L>(.*?)<pc>(.*?)<k1>',metaline)
 page = m.group(2)
 link = 'https://www.sanskrit-lexicon.uni-koeln.de/scans/csl-apidev/servepdf.php?dict=pw&page=%s' % page
 return link


def tags_with_ilines(lines):
 """
  text is tab-delimited list of lines
  Find all, and in which line
 """
 a = []
 ilines = []
 for iline,line in enumerate(lines):
  for m in re.finditer('<is[^<]*>.*?<?is>',line):
   tag = m.group(0)
   a.append(tag)
   ilines.append(iline)
 return a,ilines

def compare_tags(lines1,lines2):
 a1,ilines1 = tags_with_ilines(lines1)
 a2,ilines2 = tags_with_ilines(lines2)
 change = None
 if a1 == a2:
  return change
 # diff
 n1 = len(a1)
 n2 = len(a2)
 if n1 == n2:
  return change
 ##
 n = max(n1,n2)
 for i in range(0,n):
  if i < n1:
   x1 = a1[i]
  else:
   x1 = None
   a1.append(x1)
  if i < n2:
   x2 = a2[i]
  else:
   x2 = None
   a2.append(x2)
 # generate this change and return
 change = Change(a1,a2)
 return change

def compare(entries1,entries2,maxdiff):
 # first changes
 changes = []
 for ientry,e1 in enumerate(entries1):
  e2 = entries2[ientry]
  lines1 = e1.datalines
  lines2 = e2.datalines
  # next exits on diff
  change = compare_tags(lines1,lines2)
  if change != None:
   # fill in metaline and lnum
   change.metaline = e1.metaline
   changes.append(change)
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

def get_changenote(old,new):
 old1 = re.sub(r'</?is>','',old)
 new1 = re.sub(r'</?is>','',new)
 if old1[0].lower() != new1[0].lower(): 
   return ' Please check'
 if abs(len(old1) - len(new1)) > 2:
   return ' Please check'
 return ''
def change_to_outarr(change):
 outarr = []
 outarr.append('; ------------------------------------------------------')
 outarr.append('; %s' % change.metaline)
 a1 = change.a1
 a2 = change.a2
 for i,x1 in enumerate(a1):
  x2 = a2[i]
  outarr.append('%s cdsl=%s ab=%s' %(i+1,x1,x2))
 #changenote = get_changenote(change.old,change.new)
 #outarr.append('; %s -> %s%s' %(change.old,change.new,changenote))
 return outarr

def write_changes(fileout,changes):
 outrecs = [change_to_outarr(c) for c in changes]
 write_outrecs(fileout,outrecs)

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
  exit(1)


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
 print(len(changes),"changes found")
 write_changes(fileout,changes)
 

