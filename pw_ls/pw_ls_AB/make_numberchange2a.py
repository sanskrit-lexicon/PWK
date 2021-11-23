#-*- coding:utf-8 -*-
"""make_numberchange2a.py
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

class Change(object):
 def __init__(self,metaline,lnum,old,new):
  self.metaline = metaline
  self.lnum = lnum
  self.old = old
  self.new = new
  
class PWBIB(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.line = line
  p = line.split('\t')
  assert len(p)== 4
  self.ident,self.abbr,self.lslow,self.tooltip = p
  self.count = 0

def init_pwbib(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  recs = [PWBIB(line) for line in f]
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
 return None

def lookat_check(new):
 parts = new.split(' ')
 subparts = [part.split(',') for part in parts]
 lens = set([len(subpart) for subpart in subparts])
 if len(lens) == 1:
  return False
 # i,j. k. is ok
 m = re.search(r'^[0-9]+,[0-9]+[.] [0-9]+[.]?$',new)
 if m != None:
  return False
 # a,b,c. d. is ok
 m = re.search(r'^[0-9]+,[0-9]+,[0-9]+[.] [0-9]+[.]?$',new)
 if m != None:
  return False  
 # a,b,c,d. e. is ok
 m = re.search(r'^[0-9]+,[0-9]+,[0-9]+,[0-9]+[.] [0-9]+[.]?$',new)
 if m != None:
  return False  
 return True  # cannot confirm form of new.

def changeline2a(line,abbrs1):
 def f(m):
  ans = m.group(0)
  ls = m.group(1)
  rec = find_abbr(ls,abbrs1)
  if rec == None:
   # for 'number' type ls entries  e.g. <ls>1,2,3</ls>
   return ans
  # 
  lsname = rec.abbr
  assert ls.startswith(lsname)
  # If there are no additional characters in ls following lsname, nothing to do
  if ls == lsname:
   return ans
  # now ls has additional characters
  # if character after lsname is ' ', no change
  n = len(lsname)
  # if there is only one additional character, which is a period, then no change
  if ls == (lsname + '.'):
   return ans
  # next character should be a space
  assert ls[n] == ' '
  lsnum = ls[n+1:]
  # revise lsnum
  # replace period-digit with period-space-digit
  #lsnum1 = re.sub(r'[.]([0-9])',r'. \1',lsnum)
  # replace nonspace-leftparen with nonspace-space-leftparen
  #lsnum1 = re.sub(r'([^ ])\(',r'\1 (',lsnum1)
  # reconstruct lsnew
  if lookat_check(lsnum):
   lsnew = '[%s]' %ls
  else:
   lsnew = ls
  ans = '<ls>%s</ls>'%lsnew
  return ans
 #
 newline = re.sub(r'<ls>(.*?)</ls>',f,line)
 return newline

def write_changes(fileout,changes):
 outrecs = []
 for change in changes:
  outarr = []
  outarr.append('; -------------------------------------')
  outarr.append('; ' + change.metaline)
  outarr.append('%s old %s' %(change.lnum,change.old))
  outarr.append('; ')
  outarr.append('%s new %s' %(change.lnum,change.new))
  outrecs.append(outarr)
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(outrecs),"records written to",fileout)

if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx
 filebib = sys.argv[2]  # pwbib_input
 fileout = sys.argv[3] # change_X
 
 entries = init_entries(filein)

 abbrs = init_pwbib(filebib)

 abbrs1 = sorted(abbrs , key = lambda x : len(x.abbr),reverse=True)
 changes = []  # list of change records
 #nlook = 0
 for entry in entries:
  for iline,line in enumerate(entry.datalines):
   newline = changeline2a(line,abbrs1)
   if newline != line:
    lnum = entry.linenum1+iline+1
    #newline1 = newline
    #for lookat in lookats:
    # newline1 = newline1.replace(lookat,'[%s]'%lookat)
    metaline = re.sub(r'<k2>.*$','',entry.metaline)
    change = Change(metaline,lnum,line,newline)
    changes.append(change)

 write_changes(fileout,changes)
 
