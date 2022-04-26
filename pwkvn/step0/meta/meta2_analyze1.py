#-*- coding:utf-8 -*-
"""meta2_analyze1.py
 
"""
import sys,re,codecs
import digentry

def extend_entries(entries):
 """ add attributes 'n', pc, vol, hws, hwadjs
 """
 for entry in entries:
  entry.pc = entry.metad['pc'] # 1-282-a
  entry.vol = entry.pc[0]  # 1
  entry.n = entry.metad['n']  # 'line number' from pwkvn_21
  hws = []
  hwadjs = []
  for line in entry.datalines:
   m = re.search(r'^hw:{#([^#]*?)#}$',line)
   if m == None:
    continue
   hw = m.group(1)
   hwadj = re.sub(r'[º*£_¹]','',hw)
   hws.append(hw)
   hwadjs.append(hwadj)
  entry.hws = hws
  entry.hwadjs = hwadjs
  
def entryhwd(entries):
 d = {} # dictionary of headwords
 for entry in entries:
  hws = entry.hwadjs
  for hw in hws:
   if hw not in d:
    d[hw] = []
   d[hw].append(entry)
 return d

def write1(fileout,entries):
 d = entryhwd(entries)
 keys = d.keys()
 keys = sorted(keys)
 with codecs.open(fileout,"w","utf-8") as f:
  for hw in keys:
   entries = d[hw]
   vols = sorted([entry.vol for entry in entries])
   s = ','.join(vols)
   outarr = []
   out = '%s %s' %(hw,s)
   outarr.append(out)
   for line in outarr:
    f.write(line+'\n')
  print(len(d),"records written to",fileout)

def write2(fileout,entries,problems):
 from itertools import product
 # 
 dproblems = {}
 for problem in problems:
  key = (problem.n,problem.hw,problem.vref)
  assert key not in dproblems
  dproblems[key] = problem
 d = entryhwd(entries)
 # get entries in volume 7 with refs in other volumes
 for entry in entries:
  entry.problems = []
  vol = entry.vol
  if vol != '7':
   # we only want volume 7 entries
   continue
  # parse last line
  line = entry.datalines[-1]
  m = re.search(r'</hw> ([IV]+[.] )?([1-6 .]+)',line)
  if m == None:
   continue
  x = m.group(2).strip()
  vrefs = re.findall(r'[1-6][.]',x)
  vrefs = [x.replace('.','') for x in vrefs] # remove trailing period
  hws = entry.hwadjs
  # for each hw and each vref, look for an entry for the headword
  # whose vol is vref. For any (hw,vref) pair with no such entry,
  # note as a possible error.
  hwvs = list(product(hws,vrefs))
  probs = []
  for hw,vref in hwvs:
   a = d[hw] # entries that have hw as headword
   found = False
   for e in a:
    if e.vol == vref:
     found=True
     break
   if not found:
    probs.append((hw,vref))
  entry.problems = probs
 # generate text for the problems
 outarr = []
 newprob = 0
 for entry in entries:
  if entry.problems == []:
   continue
  n = entry.n
  pc = entry.pc
  probs = entry.problems
  #a = ['%s %s' % (hw,vref) for (hw,vref) in probs]
  #s = ', '.join(a)
  #out = '%s %s %s' %(n,pc,s)
  #outarr.append(out)
  for (hw,vref) in probs:
   s = '%s %s' % (hw,vref)
   if (n,hw,vref) in dproblems:
    out = dproblems[(n,hw,vref)].line
   else:
    reason = 'newprob'
    out = '%s %s %s %s' %(reason,n,pc,s)
    newprob = newprob + 1
   outarr.append(out)
 # write outarr
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out+'\n')
 print(len(outarr),"cases written to",fileout)
 print(newprob,"new problems found (marked as 'newprob')")
 
class Problem:
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.line = line
  parts = re.split(r' +',line)
  self.reason = parts[0]
  self.n = parts[1]
  self.pc = parts[2]
  self.hw = parts[3]
  self.vref = parts[4]
  self.rest = ' '.join(parts[5:])
  
def init_problems(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = [Problem(x) for x in f if not x.startswith(';')]
 print(len(recs),"problems read from",filein)
 return recs

if __name__=="__main__":
 filein = sys.argv[1] #  pwkvn_22
 filein1 = sys.argv[2] # analyze1_problems
 fileout = sys.argv[3] # 
 
 #with codecs.open(filein,"r","utf-8") as f:
 # lines = [x.rstrip('\r\n') for x in f]
 entries = digentry.init(filein)
 problems = init_problems(filein1)
 extend_entries(entries)
 #write1(fileout,entries)
 write2(fileout,entries,problems)
 
 
