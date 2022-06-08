#-*- coding:utf-8 -*-
"""unmarked_ab_italic.py
 
"""
from __future__ import print_function
import sys, re,codecs
import digentry


class Change(object):
 def __init__(self,metaline,lnum,old,new,newabs):
  self.metaline = metaline
  self.lnum = lnum
  self.old = old
  self.new = new
  self.newabs = newabs

def write_newabs_summary(fileout,changes):
 d = {}
 for change in changes:
  for newab in change.newabs:
   ab = newab.abbrev
   if ab not in d:
    d[ab] = 0
   d[ab] = d[ab] + 1
 #
 keys = sorted(d.keys(), key = lambda x: x.lower())
 ntot = 0
 for key in keys:
  print(key,d[key])
  ntot = ntot + d[key]
 print(ntot,"abbreviations marked")
 
def write_changes(fileout,changes):
 outrecs = []
 prevmeta = None
 for change in changes:
  outarr = []
  outarr.append('; ===============================================')
  metaline = change.metaline
  if metaline == prevmeta:
   outarr.append('; -----------------------')
  else:
   meta = re.sub(r'<k2>.*$','',metaline)
   outarr.append('; %s' % meta)
   prevmeta = metaline
  a = [x.abbrev for x in change.newabs]
  a1 = ', '.join(a)
  outarr.append('; newabs = %s'%a1)
  outarr.append('%s old %s' %(change.lnum,change.old))
  outarr.append(';')
  outarr.append('%s new %s' %(change.lnum,change.new))
  outrecs.append(outarr)
 # now, write outrecs
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print('change records written to',fileout)
  
def unmarked_abbrev(part,abbrev):
 newpart = part
 newabs = []
 if True:
  ab = abbrev.abbrev
  ab1 = ab.replace('.','[.]')
  newpart1 = re.sub(r'\b%s' % ab1,r'<ab>%s</ab>' % ab,newpart)
  if newpart1 != newpart:
   # The above changes apostrophe s. incorrectly
   if ab == 's.':
    newpart1 = newpart1.replace("'<ab>s.</ab>","'s.")
   if newpart1 != newpart:
    newabs.append(abbrev)
    newpart = newpart1
 return newpart,newabs

# applies only to italic text
regexsplitraw = r'({%[^%]*%})|(<ab>[^<]*</ab>)|(<lex>[^<]*</lex>)|(<ls.*?>[^<]*</ls>)|(<lang.*?>[^<]*</lang>)|({#[^#]*#})'
regexsplit = re.compile(regexsplitraw)

def change_unmarked_line(line,abbrevs):
 newline = line
 newabs = [] # abbreviations to be marked
 prevsplitline = None
 for iabbrev,abbrev in enumerate(abbrevs):
  oldline = newline
  ab = abbrev.abbrev
  ab1 = ab.replace('.','[.]')
  newline = re.sub(r'^%s' % ab1,r'<ab>%s</ab>' % ab,oldline)
  if newline != oldline:
   # Assume abbrevs sorted in reverse order by length.
   newabs.append(abbrev)
  if prevsplitline != newline:
   parts = re.split(regexsplit,newline)
   prevsplitline = newline
  newparts = []
  for part in parts:
   if part == None:
    continue
   elif part.startswith(('<ab>','<lex>','<ls','<lang','{#')):
    newpart = part
   else:
    newpart,newpartabbrevs = unmarked_abbrev(part,abbrev)
    for x in newpartabbrevs:
     newabs.append(x)
   newparts.append(newpart)
  newline = ''.join(newparts)
 return newline,newabs

def change_unmarked(entries,abbrevs):
 abbrevs1 = sorted(abbrevs,key = lambda x: len(x.abbrev),reverse = True)
 # <ab>X</ab> OR <lex>X</lex>
 changes = []
 for entry in entries:
  for iline,line in enumerate(entry.datalines):
   # look for abbreviations in {%X%} segments within line
   if '{%' not in line:
    continue
   parts = re.split(r'({%[^%]*%})',line)
   newparts = []
   newabs = []
   for part in parts:
    if part.startswith('{%'):
     part1 = part[2:-2] # drop initial {% and final %}
     newpart1,newabs_part = change_unmarked_line(part1,abbrevs1)
     if newpart1 != part1:
      for newab in newabs_part:
       newabs.append(newab)
      newpart = '{%'+newpart1+'%}' # reattach the percent markup
     else:
      newpart = part
    elif part == None:
     print('UNEXPECTED')
     newpart = ''
    else:
     newpart = part      
    newparts.append(newpart)
   newline = ''.join(newparts)
   if newline == line:
    continue
   # construct change
   metaline = entry.metaline
   lnum = entry.linenum1 + iline + 1
   change = Change(metaline,lnum,line,newline,newabs)
   changes.append(change)
 print(len(changes),"lines changed")
 return changes

class Abbrev:
 def __init__(self,line):
  m = re.search(r'^([^\t]+)\t<id>(.*?)</id> *<disp>(.*?)</disp>',line)
  if m == None:
   print('Abbrev error:',line)
   exit(1)
  self.abbrev = m.group(1)
  temp = m.group(2)
  self.tip = m.group(3)
  if self.abbrev != temp:
   print('Abbrev warning: %s != %s' %(self.abbrev, temp))
  self.used = False
  # Example: Abl.  
  # re.sub(r'\bAbl\.','<ab>Abl.</ab>',line)
  # re.sub(r'^Abl\.','<ab>Abl.</ab>,line)
  self.abbrevregex = re.compile(self.abbrev.replace('.','[.]'))
   
def init_abbrev(filein):
 # slurp lines
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [line.rstrip('\r\n') for line in f if not line.startswith(';')]
 recs=[Abbrev(line) for line in lines]
 # check for dups, and get dictionary
 d = {}
 for rec in recs:
  key = rec.abbrev
  if key in d:
   print('init_abbrev: duplicate abbreviation',key)
  d[key] = rec
  
 print(len(recs),"abbreviations read from",filein)
 return recs,d


if __name__=="__main__":
 filein = sys.argv[1] #  digitization consisten with option
 filein1 = sys.argv[2] # tooltip file for abbreviations
 fileout = sys.argv[3] # changes for filein
 entries = digentry.init(filein)
 abbrevs,dabbrevs= init_abbrev(filein1)
 #abbrevs = [x for x in abbrevs if x.abbrev == 'vgl.']
 #print(len(abbrevs),' dbg')
 #entries = entries[0:1000]
 changes = change_unmarked(entries,abbrevs)
 write_changes(fileout,changes)
 write_newabs_summary(None,changes)
 
