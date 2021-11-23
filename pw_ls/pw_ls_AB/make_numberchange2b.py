#-*- coding:utf-8 -*-
"""make_numberchange2b.py
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

def decompress(a):
 """
  a is a sequence of sequences of integers, with compression
  Return d,flag  where d is the decompression of a, and flag is
  True only when the decompression is successful.
  When the flag is False, d will be returned incomplete
  We try to decompress each element of a. 
  When flag is True,
   d will have the same length as a.
  d[0] = a[0]  (assume first element is decompressed
  If n0 is the length of the first element of a,
    then len(d[k]) == n0 for all k
  We construct d[k+1] from d[k] and a[k+1]
 """
 d = []
 if a == []:
  return d,True
 n0 = len(a[0])
 for ix,x in enumerate(a):
  if ix == 0:
   y = x
   d.append(y)
  else:
   # construct y from d[ix-1] and x
   z = d[ix-1] # we know len(z) == n0
   nx = len(x)
   if nx == n0:
    y = x
    d.append(y)
   elif nx > n0:
    # cannot finish decompression
    return d,False
   else: # nx < n0.
    # If z is a,b,c  and x is d,e,  then y = a,d,e
    y = z[0:n0 - nx]+x
    if not (len(y) == n0):
     print('decompress error:')
     exit(1)
    d.append(y)
 # since we are here, the first step of the decompression is done.
 # 'd' is computed.
 
 # Now we validate that 'd' is an 'increasing' sequence.
 # This is done by lexicograpical ordering
 d_lexord = sorted(d)  # this seems to be done by Python 
 flag = (d == d_lexord)
 return d,flag
 """ home-grown lexicographical sorting. Not quite right
 if len(a) == 1:
  # no ordering check to do.
  return d,True
 flag = True 
 for i,y in enumerate(d):
  if i == 0:
   x = y
  else:
   # check that x<=y  (don't require 'strictly increasing')
   # each of x,y is a sequence of integers length n0.
   # require that x[j] <= y[j]
   cmp = True
   for j,u in enumerate(x):
    v = y[j]
    if u <= v:
     pass
    else:
     # not x<y
     cmp = False
     break
   if not cmp:
    flag = False
    break
 return d,flag
 """

def lsnumstr_to_intseq(lsnums):
 """
  a : a sequence of strings, each of which is a sequence of 
   'proper' digit strings,
  We return  the corresponding sequence of integer-sequences

 """
 # 'lsnums' is a certain kind of sequence
 # return True when it can be interpreted as an integer sequence
 # return False when we think n
 new = lsnums
 if not re.search('^[0-9,. ]+$',new):
  # sequence contains wrong kind of characters
  return [],False
 parts = new.split(' ')
 subparts = [part.split(',') for part in parts]
 flag = True  # are subparts correctly formed?
 intsubparts = []
 nparts = len(parts) # same as len(subparts)
 for isubpart,subpart in enumerate(subparts):
  # subpart is a list.
  # confirm that each element of subpart ends with a period,
  # with possible exception of last element of subpart
  if subpart[-1].endswith('.'):
   subpart[-1] = subpart[-1][0:-1] # drop ending period
  else:
   # only the last subpart is allowed NOT to end with a period
   if isubpart != (nparts - 1):
    flag = False  
    break
  # now, try to convert each element of subpart to an integer
  # the int() type will do the conversion, if possible
  try:
   intsubpart = [int(i) for i in subpart]
  except:
   flag = False
   break
  intsubparts.append(intsubpart)
 return intsubparts,flag

def lookat_check(lsnumstr):
 intsubparts,success = lsnumstr_to_intseq(lsnumstr)
 if success:
  decompressed,success = decompress(intsubparts)
 return success
 
def changeline2b(line,abbrs1):
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
  if not re.search('^[0-9,. ]+$',lsnum):
   # consider only cases with numbers
   flag = True
  else:
   flag = lookat_check(lsnum)
  if not flag:
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

def test():
 pass
if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx
 filebib = sys.argv[2]  # pwbib_input
 fileout = sys.argv[3] # change_X
 
 entries = init_entries(filein)

 abbrs = init_pwbib(filebib)

 abbrs1 = sorted(abbrs , key = lambda x : len(x.abbr),reverse=True)
 changes = []  # list of change records
 #nlook = 0
 first = False
 first = True
 for entry in entries:
  if not first:
   L = entry.metad['L']
   if L == '57128':
    first= True
   else:
    continue
  for iline,line in enumerate(entry.datalines):
   newline = changeline2b(line,abbrs1)
   if newline != line:
    lnum = entry.linenum1+iline+1
    metaline = re.sub(r'<k2>.*$','',entry.metaline)
    change = Change(metaline,lnum,line,newline)
    changes.append(change)

 write_changes(fileout,changes)
 
