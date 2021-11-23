#-*- coding:utf-8 -*-
"""listls1_ab_dbg.py
"""
from __future__ import print_function
import sys, re,codecs
from parseheadline import parseheadline

class Entry(object):
 Ldict = {}
 def __init__(self,lines,linenum1,linenum2):
  # linenum1,2 are int
  self.metaline = lines[0]
  self.lend = lines[-1]  # the <LEND> line
  self.datalines = lines[1:-1]  # the non-meta lines
  # parse the meta line into a dictionary
  #self.meta = Hwmeta(self.metaline)
  self.metad = parseheadline(self.metaline)
  self.linenum1 = linenum1
  self.linenum2 = linenum2
  #L = self.meta.L
  L = self.metad['L']
  if L in self.Ldict:
   print("Entry init error: duplicate L",L,linenum1)
   exit(1)
  self.Ldict[L] = self
  self.lsarr = []
  self.dbgcount = 0
  
def init_entries(filein):
 # slurp lines
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [line.rstrip('\r\n') for line in f]
 recs=[]  # list of Entry objects
 inentry = False  
 idx1 = None
 idx2 = None
 for idx,line in enumerate(lines):
  if inentry:
   if line.startswith('<LEND>'):
    idx2 = idx
    entrylines = lines[idx1:idx2+1]
    linenum1 = idx1 + 1
    linenum2 = idx2 + 1
    entry = Entry(entrylines,linenum1,linenum2)
    recs.append(entry)
    # prepare for next entry
    idx1 = None
    idx2 = None
    inentry = False
   elif line.startswith('<L>'):  # error
    print('init_entries Error 1. Not expecting <L>')
    print("line # ",idx+1)
    print(line.encode('utf-8'))
    exit(1)
   else: 
    # keep looking for <LEND>
    continue
  else:
   # inentry = False. Looking for '<L>'
   if line.startswith('<L>'):
    idx1 = idx
    inentry = True
   elif line.startswith('<LEND>'): # error
    print('init_entries Error 2. Not expecting <LEND>')
    print("line # ",idx+1)
    print(line.encode('utf-8'))
    exit(1)
   else: 
    # keep looking for <L>
    continue
 # when all lines are read, we should have inentry = False
 if inentry:
  print('init_entries Error 3. Last entry not closed')
  print('Open entry starts at line',idx1+1)
  exit(1)

 print(len(lines),"lines read from",filein)
 print(len(recs),"entries found")
 return recs

class PWBIB_AB(object):
 ntot = 0
 def __init__(self,line):
  line = line.rstrip('\r\n')
  # <ls>X</ls>
  m = re.search(r'<ls>(.*?)</ls>',line)
  if m != None:
   self.abbr = m.group(1)
  else:
   self.abbr = line.strip()
  PWBIB_AB.ntot = PWBIB_AB.ntot + 1
  self.ident = '%04d' % PWBIB_AB.ntot
  self.lslow = self.abbr.capitalize()
  self.tooltip = 'No tooltip given'
  self.count = 0

def init_pwbib_ab(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  recs = [PWBIB_AB(line) for line in f]
 print(len(recs),"pwbib read from",filein)
 # check for duplicate idents
 d = {}
 for irec,rec in enumerate(recs):
  if rec.ident in d:
   print("ERROR: duplicate ident",rec.ident)
  d[rec.ident] = True
 return recs

def find_abbr(lsbody,abbrs):
 """ abbrs assumed sorted by descending length of abbreviation. 
  Find the longest abbreviation that starts lsbody.
  This is the FIRST abbreviation that starts lsbody
 """
 for abbr in abbrs:
  if lsbody.startswith(abbr.abbr):
   return abbr
 #print('find_abbr error. lsbody=',lsbody)
 return None


def update_dabbrs(line,dabbrs,entry,lsdbg):
 for m in re.finditer(r'<ls>(.*?)</ls>',line):
  ls = m.group(1)
  if ls in dabbrs:
   abbr = dabbrs[ls]
   abbr.count = abbr.count + 1
   lsname = abbr.abbr
   if lsname == lsdbg:
    entry.dbgcount = entry.dbgcount + 1

def write_dbg(fileout,entries,lsdbg):
 outrecs = []
 ntot = 0
 nline = 0
 for entry in entries:
  ndbg = entry.dbgcount
  if ndbg != 0:
   outarr = []
   metaline = re.sub(r'<k2>.*$','',entry.metaline)
   outarr.append('%2d %s' % (ndbg,metaline))
   outrecs.append(outarr)
   ntot = ntot + ndbg
   nline = nline + 1
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(outrecs),"records written to",fileout)
 print(lsdbg,'occurs %s times in %s entries'%(ntot,nline))

if __name__=="__main__":
 lsdbg = sys.argv[1]
 filein = sys.argv[2] #  xxx.txt (path to digitization of xxx
 filebib = sys.argv[3]  # pwbib_input.txt (ab format)
 fileout = sys.argv[4] #

 entries = init_entries(filein)
 abbrs = init_pwbib_ab(filebib)
 dabbrs = {}
 for x in abbrs:
  dabbrs[x.abbr] = x
 unknowns = [] # list of PWBIB records not in abbrs
 for entry in entries:
  for line in entry.datalines:
   update_dabbrs(line,dabbrs,entry,lsdbg)
 write_dbg(fileout,entries,lsdbg)
 
