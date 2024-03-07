# coding=utf-8
""" make_change_02.py
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 print(len(lines),"from",filein)
 return lines

def write_lines(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for out in lines:
   f.write(out+'\n')  
 print(len(lines),"lines written to",fileout)

class Change:
 def __init__(self,metaline,lnum,old,new):
  self.metaline = metaline
  self.lnum = lnum
  self.old = old
  self.new = new

def write_changes(fileout,changes,option):
 outrecs = []
 outarr = [] # header
 outarr.append('; ******************************************************')
 outarr.append('; %s: %s changes' % (option,len(changes)))
 outarr.append('; ******************************************************')
 outrecs.append(outarr)
 for c in changes:
  outarr = []
  outarr.append('; %s' % c.metaline)
  lnum = int(c.lnum)
  # change 
  outarr.append('%s old %s' %(lnum,c.old))
  outarr.append(';')
  outarr.append('%s new %s' %(lnum,c.new))
  outarr.append('; ----------------------------------------------')
  outrecs.append(outarr)
 write_recs(fileout,outrecs,blankflag=False)

def write_recs(fileout,outrecs,printflag=True,blankflag=True):
 # outrecs is array of array of lines
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
   if blankflag:
    out = ''  # blank line separates recs
    f.write(out+'\n')
 if printflag:
  print(len(outrecs),"records written to",fileout)

class AB_change:
 def __init__(self,lines):
  self.lines = lines
  try:
   a,b,c,d = lines
  except:
   print('AB_change ERROR:',len(lines))
   for line in lines:
    print(line)
   exit(1)
  m = re.search(r'^[0-9]+$',a)
  assert m != None
  self.a = a
  m = re.search(r'\(CDSL\): (.*)$',b)
  self.cdsl = m.group(1)
  m = re.search(r'\(AB\): (.*)$',c)
  self.ab = m.group(1)
  m = re.search(r'^-+$',d)
  assert m != None
  m = re.search(r'^(.*)¦',self.cdsl)
  self.cdsl1 = m.group(1)
  m = re.search(r'^(.*)¦',self.ab)
  self.ab1 = m.group(1)
  # used
  self.used = 0 # will be modified 
  
def split_list(a, k):
    """
    Splits a list 'a' into 'k' equal-sized chunks.
    """
    n = len(a) // k  # Calculate the size of each chunk
    return [a[i * n: (i + 1) * n] for i in range(k)]

def test_split_list():
 print('test_split_list')
 a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
 k = len(a) // 3
 groups = split_list(a,k)
 print('a=',a)
 for group in groups:
  print(group)
 exit(1)
# test_split_list()

def init_ab_changes(lines):
 # groups of 4 lines
 q,r = divmod(len(lines),4)
 assert r == 0
 grouplist = split_list(lines,q)
 groups = [AB_change(grouplines) for grouplines in grouplist]
 d = {}
 for group in groups:
  cdsl1 = group.cdsl1
  if cdsl1 not in d:
   d[cdsl1] = []
  d[cdsl1].append(group)
 # check for ab- consistency
 keys1 = d.keys()
 for cdsl1 in keys1:
  groups1 = d[cdsl1]
  ab1 = groups1[0].ab1
  for g in groups1:
   assert g.ab1 == ab1
 changemap = {}
 for cdsl1 in keys1:
  groups1 = d[cdsl1]
  ab1 = groups1[0].ab1
  changemap[cdsl1] = ab1
 return changemap

def get_changes(lines,changemap):
 changes = []
 for iline,line in enumerate(lines):
  m = re.search(r'^(.*)¦(.*)$',line)
  if m == None:
   continue
  before = m.group(1)
  after  = m.group(2)
  if before not in changemap:
   continue
  cdsl1 = before
  ab1 = changemap[before]
  # line is a bbline
  ilinemeta = iline-1
  metaline = lines[ilinemeta]
  lnum = iline + 1
  old = line
  new = ab1 + '¦' + after
  change = Change(metaline,lnum,old,new)
  changes.append(change)
  #group.used = group.used + 1
 return changes

def unused_get_changes(lines,changemap):
 changes = []
 for iline,line in enumerate(lines):
  # AB file does not have the <info n="sup_N"/>
  m = re.search(r'^(.*)(<info n="sup_."/>)$',line)
  if m == None:
   continue
  gline = m.group(1)
  sup = m.group(2)
  if gline not in changemap:
   continue
  group = changemap[gline]
  cdsl = group.cdsl
  assert cdsl == gline
  ab = group.ab
  ab1 = ab + sup
  # line is a bbline
  ilinemeta = iline-1
  metaline = lines[ilinemeta]
  lnum = iline + 1
  change = Change(metaline,lnum,line,ab1)
  changes.append(change)
  group.used = group.used + 1
 return changes

def write_unused_groups(fileout,groups):
 # check for unused changemap
 lines = []
 for group in groups:
  if group.used != 1:
   for x in group.lines:
    lines.append(x)
 write_lines(fileout,lines)
 
if __name__=="__main__":
 filein = sys.argv[1]  # pw.txt
 filein1 = sys.argv[2] # AB's pwkvn_4.differences-X.txt
 fileout = sys.argv[3]  # 
 lines = read_lines(filein)
 lines1 = read_lines(filein1)
 changemap = init_ab_changes(lines1)
 write_changes(fileout,changes,'xx')
 
 
