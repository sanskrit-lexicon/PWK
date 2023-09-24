# coding=utf-8
""" ab_local_tm_process.py
"""
from __future__ import print_function
import sys, re,codecs
import digentry  

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

class Case(object):
 def __init__(self,caseline):
  self.caseline = caseline
  self.href = None
  self.metaline = None
  self.lend = None
  self.datalines = []

def generate_recs(lines):
 case = None
 for line in lines:
  if line.startswith('; case '):
   case = Case(line) # start new case
   continue
  if line == ';' : # end of case
   yield case
   case = None
  if line.startswith('; https'):
   case.href = line
   continue
  if line.startswith('<L>'):
   case.metaline = line
   continue
  if line.startswith('<LEND>'):
   case.lend = line
   continue
  # otherwise, assume a line in datalines
  if case != None:
   case.datalines.append(line)

def mark_corrections(cases1,cases2):
 # add 'changes' attribute to cases1
 assert len(cases1) == len(cases2)
 n = 0 # number of cases with a change
 nc = 0 # number of lines changed
 for icase,case1 in enumerate(cases1):
  case2 = cases2[icase]
  assert case1.href == case2.href
  assert case1.metaline == case2.metaline
  assert case1.lend == case2.lend
  changes = []
  datalines1 = case1.datalines
  datalines2 = case2.datalines
  assert len(datalines1) == len(datalines2)
  for i,dataline1 in enumerate(datalines1):
   dataline2 = datalines2[i]
   if dataline1 != dataline2:
    changes.append((i,dataline2))
    nc = nc + 1
  case1.changes = changes
  if len(changes)!= 0:
   n = n + 1
 print(nc,'lines to change from',n,'cases')

def get_L_dict(cases):
 d = {}
 for case in cases:
  metaline = case.metaline
  href = case.href
  m = re.search(r'<L>(.*?)<',metaline)
  L = m.group(1)
  if L in d:
   print('get_L_dict: unexpected duplicate',L)
  d[L] = case
 return d

class Change(object):
 def __init__(self,lnum,old,new,comment,href):
  self.lnum = lnum
  self.old = old
  self.new = new
  self.comment = comment
  self.href = href
  
def get_changerecs(entries,d):
 changerecs = []
 for entry in entries:
  metaline = entry.metaline
  m = re.search(r'<L>(.*?)<',metaline)
  L = m.group(1)
  if L not in d:
   continue
  case = d[L]
  if len(case.changes) == 0:
   continue
  linenum1 = entry.linenum1
  meta = re.sub(r'<k2>.*$','',metaline)
  href = case.href
  for i,dataline2 in case.changes:
   lnum = linenum1 + i + 1
   dataline1 = case.datalines[i]
   comment = '%s (%s)' %(meta,case.caseline)
   changerec = Change(lnum,dataline1,dataline2,comment,href)
   changerecs.append(changerec)
 print(len(changerecs),'Change records')
 return changerecs

def prepare_diffs(oldline,newline):
 olds = re.findall(r'<ab .*?</ab>',oldline)
 news = re.findall(r'<ab .*?</ab>',newline)
 diffs = []
 if len(olds) == len(news):
  for i,old in enumerate(olds):
   new = news[i]
   diff = '; %s  ->  %s' %(old,new)
   diffs.append(diff)
 else:
  diffs.append('; OLD local abbrevs:')
  for i,old in enumerate(olds):
   diffs.append(';   %s: %s' %(i+1,old))
  diffs.append('; NEW local abbrevs:')    
  for i,new in enumerate(news):
   diffs.append(';   %s: %s' %(i+1,new))
 if olds == news:
  diffs.append('; NO local AB  differences. Other differences found')
 #assert diffs != []
 return diffs

def prepare(changerecs):
 outrecs = []
 n = 0
 for rec in changerecs:
  n = n + 1
  # generate output
  outarr = []
  outarr.append('; %s' % rec.comment)
  outarr.append(rec.href)
  difflines = prepare_diffs(rec.old,rec.new)
  for temp in difflines:
   outarr.append(temp)
  outarr.append('%s old %s' % (rec.lnum,rec.old))
  outarr.append(';')
  outarr.append('%s new %s' % (rec.lnum,rec.new))
  outarr.append('; ---------------------------------------------------------')
  outarr.append(';')
  outrecs.append(outarr)
 return outrecs

def write_outrecs(fileout,outrecs):
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outrecs),"cases written to",fileout)

if __name__=="__main__":
 filein1 = sys.argv[1] # ab_local_tm_0
 filein2 = sys.argv[2] # ab_local_tm_0_corr
 filein = sys.argv[3] # xxx.txt cdsl
 fileout = sys.argv[4] #
 lines1 = read_lines(filein1)
 lines2 = read_lines(filein2)
 #print(lines1[3])
 #print(lines2[3])
 assert len(lines1) == len(lines2)
 cases1 = list(generate_recs(lines1))
 print(len(cases1),"cases from",filein1)
 cases2 = list(generate_recs(lines2))
 print(len(cases2),"cases from",filein2)
 # mark corrections (add changes attribute too cases1)
 mark_corrections(cases1,cases2)
 # L-dictionary for cases1
 d1 = get_L_dict(cases1)
 entries = digentry.init(filein)
 changerecs = get_changerecs(entries,d1)
 outrecs = prepare(changerecs)
 #print_outrecs(outrecs)
 write_outrecs(fileout,outrecs)

