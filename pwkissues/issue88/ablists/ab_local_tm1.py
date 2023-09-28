# coding=utf-8
""" ab_local_tm1.py
 same as ab_local_tm.py EXCEPT
 only the 'u.' abbreviation
"""
from __future__ import print_function
import sys, re,codecs
import digentry  
 
def write_outrecs(fileout,outrecs):
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outrecs),"cases written to",fileout)

def mark_local(entries):
  # only <ab n="X">u.</ab>
 n = 0
 for entry in entries:
  text = ' '.join(entry.datalines)
  #if '<ab ' in text:
  if '>u.</ab>' in text:
   entry.localflag = True
   n = n + 1
  else:
   entry.localflag = False
 print(n,'entries contain a local abbreviation')

def prepare(entries):
 url = 'https://sanskrit-lexicon.uni-koeln.de/work/pwk_tm/web/webtc/indexcaller.php'
 parms = 'dict=pw&input=slp1&output=deva&key='
 href0 = '%s?%s' % (url,parms)
 outrecs = []
 n = 0
 for entry in entries:
  if not entry.localflag:
   continue
  n = n + 1
  # generate output
  outarr = []
  key = entry.metad['k1']
  link = href0 + key
  outarr.append('; case %s' % n)
  outarr.append('; %s' % link)
  outarr.append(entry.metaline)
  for line in entry.datalines:
   outarr.append(line)
  outarr.append(entry.lend)
  outarr.append(';')
  outrecs.append(outarr)
 return outrecs

if __name__=="__main__":
 filein = sys.argv[1] # xxx.txt cdsl
 fileout = sys.argv[2] #
 entries = digentry.init(filein)
 mark_local(entries)
 outrecs = prepare(entries)
 #print_outrecs(outrecs)
 write_outrecs(fileout,outrecs)

