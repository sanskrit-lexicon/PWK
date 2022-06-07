#-*- coding:utf-8 -*-
"""freq_ab.py
 
"""
from __future__ import print_function
import sys, re,codecs
import digentry

def write_freq(fileout,freq,abbrevd):
 keys = sorted(freq.keys(), key = lambda x: x.lower())
 outarr = []
 notips = []
 for key in keys:
  if key not in abbrevd:
   notips.append(key)
   tip = '[unknown]'
  else:
   rec = abbrevd[key]
   tip = rec.tip
   rec.used = True
  out = '%s %s %s' % (key,freq[key],tip)
  outarr.append(out)
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')
 print(len(keys),"records written to",fileout)
 print(len(notips),"abbreviations without tooltip" )
 for key in notips:
  print('   %s %s unknown' %(key,freq[key]))
 
def find_freq(entries):
 # <ab>X</ab> OR <lex>X</lex>
 d = {}
 for entry in entries:
  for line in entry.datalines:
   for m in re.finditer(r'<ab>([^<]*)</ab>',line):
    g = m.group(1)
    if g not in d:
     d[g] = 0
    d[g] = d[g] + 1
   for m in re.finditer(r'<lex>([^<]*)</lex>',line):
    g = m.group(1)
    if g not in d:
     d[g] = 0
    d[g] = d[g] + 1
 print(len(d.keys()),'different greek strings')
 return d

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

def check_used(abbrevs):
 unused = [rec for rec in abbrevs if rec.used == False]
 print(len(unused),"abbreviation tips unused:")
 for rec in unused:
  print('   %s %s' %(rec.abbrev,rec.tip))
if __name__=="__main__":
 filein = sys.argv[1] #  digitization consisten with option
 filein1 = sys.argv[2] # tooltip file for abbreviations
 fileout = sys.argv[3] # changes for filein
 entries = digentry.init(filein)
 abbrevs,dabbrevs= init_abbrev(filein1)
 
 d = find_freq(entries)
 write_freq(fileout,d,dabbrevs) # also modifies abbrev used field
 check_used(abbrevs)
 
 
