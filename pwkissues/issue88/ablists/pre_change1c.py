# coding=utf-8
""" pre_change1c.py
"""
from __future__ import print_function
import sys, re,codecs
import digentry

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

class Tip(object):
 def __init__(self,line):
  self.line = line
  self.abbrev,self.counts,self.tooltip = line.split('\t')
  self.usedcd = 0 # number of usages in cdsl pw
  self.usedab = 0 # number of usages in ab pw
  a,b = self.counts.split(',')
  self.countcd = int(a)
  self.countab = int(b)
  self.replace = None
  
def init_tips(filein):
 lines = read_lines(filein)
 recs = []
 d = {}
 for line in lines:
  if line.startswith(';'):
   # skip comment lines
   continue
  rec = Tip(line)
  recs.append(rec)
  abbrev = rec.abbrev
  if abbrev in d:
   print('WARNING: init_tips duplicate',line)
  d[abbrev] = rec
 print(len(recs),"read from",filein)
 return recs,d

def howmany(regex,entries):
 n = 0
 for entry in entries:
  for line in entry.datalines:
   matches = re.findall(regex,line)
   n = n + len(matches)
 return n

def check_tips(tips,entries):
 ans = []
 nchk = 0
 for rec in tips:
  if rec.countcd != 0:
   continue
  if rec.countab == 0:
   continue
  nchk = nchk + 1
  #if nchk > 10:
  # break
  abbrev = rec.abbrev
  regexraw = abbrev.replace('.','[.]')
  regex = re.compile(regexraw)
  n = howmany(regex,entries)
  absdiff = abs(n - rec.countab)
  if absdiff < 5:
   old = abbrev
   new = '<ab>%s</ab>' % abbrev
   replace = ('%s' % old, '%s' % new)
   ans.append(replace)
   print(' %s, # %s,%s' %(replace,n,rec.countab))
 return ans

if __name__=="__main__":
 filein = sys.argv[1] # (old) digitization
 filein1 = sys.argv[2] # ab_glob1
 #fileout = sys.argv[3] # 
 # get list of Entry records from digitization
 # For structure of an entry record,
 # see __init__ of Entry class in digentry.py
 entries = digentry.init(filein)
 # tips
 tips,dtips = init_tips(filein1)
 data = check_tips(tips,entries)
