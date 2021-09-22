#-*- coding:utf-8 -*-
"""transcodeprep.py
 
 
"""
from __future__ import print_function
import sys, re,codecs
import transcoder
transcoder.transcoder_set_dir('transcoder')

class EntrySch(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  m = re.search(r'^L=([0-9.]+) {#(.*?)#} {%(.*?)%}¦ (.*)$',line)
  if not m:
   print('EntrySch problem:',line)
  self.L = m.group(1)
  self.slp1 = m.group(2)
  self.iast = m.group(3)
  self.text = m.group(4)
  self.iastadj = None
  self.slp1adj = None
  
def init_entries_sch(filein):
 entries = []
 with codecs.open(filein,"r","utf-8") as f:
  for line in f:
   if line.strip() != '':
    entry = EntrySch(line)
    entries.append(entry)
 print(len(entries),"entries read from",filein)
 return entries

def adjust_iast(x):
 x = x.replace('°','')
 x = x.lower()
 x = re.sub(r'[\[\]]','',x)
 x = re.sub(r'[()]','',x)
 x = re.sub(r'^-','',x)
 return x

def adjust(entry):
 iastadj = adjust_iast(entry.iast)
 tranin = 'roman1'  # customized iast
 tranout = 'slp1'
 slp1adj = transcoder.transcoder_processString(iastadj,tranin,tranout)
 entry.iastadj = iastadj
 entry.slp1adj = slp1adj
 entry.slp1adjna = re.sub(r"[\/^']",'',slp1adj)  # remove accents and avagraha

def test():
 outarr = []
 slp1s = ['A/','I/','U/']
 for x in slp1s:
  y = transcoder.transcoder_processString(x,'slp1','roman1')
  z = y.upper()
  outarr.append('%s -> %s AND %s' %(x,y,z))
 return outarr

def write(entries,fileout):
 nok = 0
 nprob = 0
 outrecs = []
 tests = test()
 outrecs = outrecs + tests
 for entry in entries:
  if entry.slp1 == entry.slp1adjna:
   nok = nok + 1
   continue
  nprob = nprob + 1
  out = 'L=%s slp1 = %s, slp1adj = %s, iast = %s, iastadj = %s' % (
      entry.L,entry.slp1, entry.slp1adjna, entry.iast, entry.iastadj)
  outrecs.append(out)
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outrecs:
   f.write(out + '\n')
   f.write('\n')
 print(nok,"iast-slp1 conversions successful")
 print(nprob,"iast-slp1 conversions problematic")
 
if __name__=="__main__":
 filein = sys.argv[1] #  temp_sch1.txt
 fileout = sys.argv[2] # 
 entries = init_entries_sch(filein)
 for entry in entries:
  adjust(entry)
 write(entries,fileout)
 
