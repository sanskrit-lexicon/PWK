# coding=utf-8
""" renum1.py
"""
from __future__ import print_function
import sys, re,codecs
import digentry  

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"cases written to",fileout)

def write_recs_helper(rec):
 # rec is a change_rec object
 outarr = []
 outarr.append(rec.first)
 for line in rec.comments:
  outarr.append(line)
 lnum1 = rec.lnum_new
 outarr.append('%s old %s' % (lnum1,rec.old))
 outarr.append(rec.semicolon)
 outarr.append('%s new %s' % (lnum1,rec.new))
 outarr.append(rec.last)
 return outarr

def write_recs(fileout,recs):
 outrecs = []
 for rec in recs:
  outarr = write_recs_helper(rec)
  outrecs.append(outarr)
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:          
    f.write(out+'\n')  
 print(len(recs),"cases written to",fileout)
 
class ChangeRec:
 def __init__(self,reclines):
  self.reclines = reclines
  regex_old = '^([0-9]+) old (.*)$'
  regex_new = '^([0-9]+) new (.*)$'
  self.comments = []
  for iline,line in enumerate(reclines):
   if line.startswith('; <L>'):
    m = re.search(r'<L>(.*?)<',line)
    self.L = m.group(1)
    self.first = line
   elif re.search(regex_old,line):
    m = re.search(regex_old,line)
    self.lnum = m.group(1)
    self.old = m.group(2)
   elif re.search(regex_new,line):
    m = re.search(regex_new,line)
    lnum_new = m.group(1)
    assert lnum_new == self.lnum
    self.new = m.group(2)
   elif line == ';':
    self.semicolon = line
   elif line == '; --------------------------------------------------':
    self.last = line
   elif line.startswith('; '):
    self.comments.append(line)
   else:
    print('ChangeRec error')  
  # 
  self.lnum_new = None
  
def generate_recs(lines):
 for line in lines:
  if line.startswith('; <L>'):
   reclines = []
   reclines.append(line)
  elif line.startswith('; --------------------------------------------------'):
   reclines.append(line)
   yield reclines
   reclines = []
  else:
   reclines.append(line)
   
def init_change(filein):
 lines = read_lines(filein)
 reclines = list(generate_recs(lines))
 print(len(reclines),"generated")
 recs = []
 for group in reclines:
  rec = ChangeRec(group)
  recs.append(rec)
 return recs

def renum(entries,changes):
 Ldict = digentry.Entry.Ldict
 notfound = 0
 nfs = []
 for change in changes:
  L = change.L
  if L not in Ldict:
   print('change.L = ',L,'Not found')
   exit(1)
  entry = Ldict[L]
  lnum1 = None
  for iline,line in enumerate(entry.datalines):
   if line == change.old:
    lnum1 = entry.linenum1 + iline + 1
    break
  if lnum1 == None:
   notfound = notfound + 1
   print('notfound#%s (%s) %s' % (notfound,change.lnum,change.first))
  else:
   change.lnum_new = lnum1
 print('notfound = ',notfound)

def merge_changes(a):
 if len(a) == 1:
  # normal case - no duplicates
  return a[0]
 newchange = a[0]
 reclines = [c.reclines for c in a]
 flag = True
 for change in a[1:] :
  if newchange.new != change.old:
   flag = False
   break
  newchange.new = change.new
  newchange.comments = newchange.comments + change.comments
 if not flag:
  for line in reclines:
   print(line)
  exit(1)
 return newchange

def merge_duplicate_lnum(changes):
 d = {}
 for change in changes:
  lnum = change.lnum
  if lnum not in d:
   d[lnum] = []
  d[lnum].append(change)
 lnumarr = sorted(d.keys())
 lnumdup = {}
 for lnum in lnumarr:
  n = len(d[lnum])
  if n not in lnumdup:
   lnumdup[n] = 0
  lnumdup[n] = lnumdup[n] + 1
 print(lnumdup)
 print([lnum for lnum in d if len(d[lnum]) > 1])

 # 
 changes1 = []
 for lnum in lnumarr:
  a = d[lnum]  # array of changes
  change1 = merge_changes(a)
  changes1.append(change1)
 return changes1
if __name__=="__main__":
 filein = sys.argv[1]  # xxx.txt
 filein1 = sys.argv[2] # a standard change file
 fileout = sys.argv[3] # 
 entries = digentry.init(filein)
 changes = init_change(filein1)
 changes1 = merge_duplicate_lnum(changes)
 renum(entries,changes1)  # lnum_new set in change records
 # sort changes by lnum_new
 changes2 = sorted(changes1,key = lambda change: change.lnum_new)
 write_recs(fileout,changes2)
