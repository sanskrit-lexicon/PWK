# coding=utf-8
""" is_compare_texts_change.py
"""
from __future__ import print_function
import sys, re,codecs
import digentry  

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

class Change(object):
 def __init__(self,iline,oldline,newline,chgtags):
  self.metaline = None # filled in later
  self.lnum = None
  self.iline = iline
  self.oldline = oldline
  self.newline = newline
  self.chgtags = chgtags # array of (oldtag,newtag)

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
  for m in re.finditer('<is.*?>.*?</is>',line):
   tag = m.group(0)
   a.append(tag)
   ilines.append(iline)
 return a,ilines

def compare_tags(lines1,lines2):
 a1,ilines1 = tags_with_ilines(lines1)
 a2,ilines2 = tags_with_ilines(lines2)
 changes = []
 if a1 == a2:
  return changes
 n1 = len(a1)
 n2 = len(a2)
 # we require same number of tags from both sources
 if n1 != n2:
  return changes
 n = max(n1,n2)
 linegroups = {}
 for i in range(0,n):
  iline = ilines1[i]
  if iline not in linegroups:
   linegroups[iline] = []
  linegroups[iline].append(i)
 linegroupkeys = sorted(linegroups.keys())
 i = -1
 for iline in linegroupkeys:
  linegroup = linegroups[iline]
  oldline = lines1[iline]
  if False:
   print('dbg: iline=%s, linegroup=%s' %(iline,linegroup))
   print('oldline=',oldline)
  # compute newline and chgtags
  parts = re.split('(<is.*?>.*?</is>)',oldline)
  newparts = []
  chgtags = []
  for ipart,part in enumerate(parts):
   if part.startswith('<is'):
    i = i + 1
    x1 = a1[i]
    x2 = a2[i]
    if x1 != part:
     print('ERROR: oldline=',oldline)
     print('x1 = %s, part = %s' % (x1,part))
     exit(1)
    newpart = x2
    if x1 != x2:
     chgtags.append((x1,x2))
   else:
    newpart = part
   newparts.append(newpart)
  newline = ''.join(newparts)
  if newline == oldline:
   continue
  # generate a change for this line
  change = Change(iline,oldline,newline,chgtags)
  changes.append(change)
 return changes # None

def mark_changes(entries1,entries2,maxdiff):
 # add changes attribute to each entry of entries1
 for ientry,e1 in enumerate(entries1):
  e2 = entries2[ientry]
  lines1 = e1.datalines
  lines2 = e2.datalines
  # next exits on diff
  #print('dbg: begin',e1.metaline)
  changes = compare_tags(lines1,lines2) # from this entry
  if len(changes) != 0:
   #print('dbg: %s (%s)' % (e1.metaline,len(changes)))
   pass
  for change in changes:
   # fill in metaline and lnum
   change.metaline = e1.metaline
   change.lnum = e1.linenum1 + change.iline + 1
  # add to entry
  e1.changes = changes

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
 if abs(len(old1) -len(new1)) > 2:
   return ' Please check'
 return ''

def change_to_outarr(changes):
 outarr = []
 for ichange,change in enumerate(changes):
  nchanges = len(changes)
  # header material for changes to this entry
  outarr.append('; ------------------------------------------------------')
  outarr.append('; %s (%s)' % (change.metaline,nchanges))
  for oldtag,newtag in change.chgtags:
   changenote = get_changenote(oldtag,newtag)
   outarr.append('; CHANGE: %s -> %s%s' %(oldtag,newtag,changenote))
  outarr.append('; ------------------------------------------------------')
  # details of the change to this line
  outarr.append('%s old %s' %(change.lnum,change.oldline))
  outarr.append(';')
  outarr.append('%s new %s' %(change.lnum,change.newline))
  outarr.append('; ------------------------')
 return outarr

def write_changes(fileout,entries):
 outrecs = []
 for entry in entries:
  if entry.changes != []:
   outrec = change_to_outarr(entry.changes)
   outrecs.append(outrec)
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
 mark_changes(entries_cdsl,entries_ab,maxdiff)
 write_changes(fileout,entries_cdsl)
 

