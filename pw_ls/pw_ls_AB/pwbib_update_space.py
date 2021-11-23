#-*- coding:utf-8 -*-
"""pwbib_update_space.py
"""
from __future__ import print_function
import sys, re,codecs
from parseheadline import parseheadline

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

class Change(object):
 def __init__(self,lnum,old,new):
  self.lnum = lnum
  self.old = old
  self.new = new
  
class LSMAP(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  p = line.split(' : ')
  assert len(p)== 2
  self.lsold = p[0]
  self.lsnew = p[1]
  self.count = 0

def init_lsmap(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  recs = [LSMAP(line) for line in f]
 print(len(recs),"read from",filein)
 return recs

def find_abbr(lsbody,abbrs):
 """ abbrs assumed sorted by descending length of abbreviation. 
  Find the longest abbreviation that starts lsbody.
  This is the FIRST abbreviation that starts lsbody
 """
 for abbr in abbrs:
  if lsbody.startswith(abbr.lsold):
   return abbr
 #print('find_abbr error. lsbody=',lsbody)
 return None

def changeline(line,abbrs1):
 def f(m):
  ls = m.group(1)
  rec = find_abbr(ls,abbrs1)
  if rec == None:
   lsnew = ls
  else:
   lsnew = ls.replace(rec.lsold,rec.lsnew)
   # If there are digits following rec.lsnew in ls, then insert a space
   n = len(rec.lsnew)
   if (n < len(lsnew)) and (lsnew[n] in '0123456789'):
    lsnew = lsnew[0:n] + ' ' + lsnew[n:]
  ans = '<ls>%s</ls>'%lsnew
  return ans
 
 newline = re.sub(r'<ls>(.*?)</ls>',f,line)
 return newline

def write_changes(fileout,changes):
 outrecs = []
 for change in changes:
  outarr = []
  outarr.append('; -------------------------------------')
  outarr.append('%s old %s' %(change.lnum,change.old))
  outarr.append('; ')
  outarr.append('%s new %s' %(change.lnum,change.new))
  outrecs.append(outarr)
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(outrecs),"records written to",fileout)

def estimate_lslow(ls):
 parts = re.split(r'\b',ls)
 newparts = []
 for part in parts:
  if re.search(r'[a-z]',part):
   newpart = part
  else:
   newpart = part.capitalize()
  newparts.append(newpart)
 new = ''.join(newparts)
 #print ls,new
 return new

if __name__=="__main__":
 filein = sys.argv[1] #  pwbib_input
 filemap = sys.argv[2]  # ls_spacemap
 fileout = sys.argv[3] # change_X
 
 entries = init_pwbib(filein)

 abbrs = init_lsmap(filemap)

 abbrs1 = sorted(abbrs , key = lambda x : len(x.lsold),reverse=True)
 changes = []  # list of change records
 for iline,rec in enumerate(entries):
   ls = rec.abbr
   newlsmap = find_abbr(ls,abbrs1)
   if newlsmap == None:
    continue
   newls = newlsmap.lsnew
   if ls != newls:
    lnum = iline+1
    line = '\t'.join([rec.ident,rec.abbr,rec.lslow,rec.tooltip])
    assert line == rec.line
    # try to get new low also
    newlslow = estimate_lslow(newls)
    newline = '\t'.join([rec.ident,newls,newlslow,rec.tooltip])
    change = Change(lnum,line,newline)
    changes.append(change)

 write_changes(fileout,changes)
 
