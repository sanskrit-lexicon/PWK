# coding=utf-8
""" alter_diff_02.py for pw_8_work
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
 def __init__(self,lnum_meta,metaline,metaline_new,lnum_old,old,new,cat):
  self.metaline = metaline
  self.metaline_new = metaline_new
  self.lnum_meta = lnum_meta
  self.lnum_old = lnum_old
  self.old = old
  self.new = new
  self.cat = cat
  assert cat in ['meta','other','metabb']

def get_outarr_helper(c):
 # change to metaline.  Need to check bbline
 outarr = []
 outarr.append('; %s cat=%s' % (c.metaline,c.cat))
 # change to metaline
 outarr.append('%s old %s' %(c.lnum_meta,c.metaline))
 outarr.append('%s new %s' %(c.lnum_meta,c.metaline_new))
 outarr.append('; ---- bbline')
 # comment out bbline change show only 'old
 outarr.append(';%s old %s' %(c.lnum_old,c.old))
 #outarr.append(';')
 #outarr.append(';%s new %s' %(c.lnum_old,c.new))
 outarr.append('; ----------------------------------------------')
 return outarr

def write_groups(fileout,groups):
 outarr = []
 for group in groups:
  for line in group:
   outarr.append(line)
 write_lines(fileout,outarr)
 return

class AB_change:
 def __init__(self,lines):
  self.lines = lines
  n0 = len(lines)
  assert n0 == 4
  parts = lines[0].split(',')  # lnums
  try:
   lnums = [int(part) for part in parts]
  except:
   print('AB_change error: lines=',lines)
   exit(1)
  m = re.search(r'^\(CDSL\): (.*)$',lines[1])
  self.cdsl = m.group(1)
  m = re.search(r'^\(AB\): (.*)$',lines[2])
  self.ab = m.group(1)

def get_groups(lines):
 group = []
 for iline,line in enumerate(lines):
  group.append(line)
  if line.startswith('-'):
   yield group
   group = []

def get_newgroups(group):
 # group is array of lines
 parts = group[0].split(',')
 lnums0 = [int(x) for x in parts]
 assert len(parts) == 2
 l1 = lnums0[0]
 l2 = lnums0[1]
 lnums = list(range(l1,l2+1))
 if lnums[-1] != l2:
  print(lnums0)
  print(lnums)
  exit(1)
 n = len(lnums)
 assert len(group) == (2 + (2 * n))
 newgroups = []
 for i,lnum in enumerate(lnums):
  line0 = '%s' % lnums[i]
  line1 = group[1+i]
  try:
   line2 = group[1+i+n]
  except:
   print('error n=%s, i=%s' %(n,i))
   print(lnums)
   for ig,g in enumerate(group):
    print('%s:%s' %(ig,g))
   exit(1)
         
  line3 = group[-1]  # ----
  m = re.search(r'^\(CDSL\): <L>(.*)<pc>', line1)
  Lcdsl = m.group(1)
  m = re.search(r'^\(AB\): <L>(.*)<pc>',line2)
  Lab = m.group(1)
  assert Lcdsl == Lab
  newgroup = [line0,line1,line2,line3]
  newgroups.append(newgroup)
 return newgroups

def init_ab_groups(lines):
 # groups
 groups0 = list(get_groups(lines))
 print(len(groups0),"groups found")
 # normalize so each group has 4 lines
 groups1 = []
 for group in groups0:
  if len(group) == 4:
   # no change
   groups1.append(group)
  elif len(group) in [6,8]:
   newgroups = get_newgroups(group)
   for g in newgroups:
    groups1.append(g)
  else:
   print('init_ab_groups unexpected: %s' % group[0])
 print(len(groups1),"normalized groups")
 return groups1

def init_pwchanges(lines,dgroups):
 changes = []
 Ldbg = '215472'
 for iline,line in enumerate(lines):
  # match by L
  m = re.search(r'^<L>(.*?)<pc>',line)
  if m == None:
   continue
  L = m.group(1)
  if L == Ldbg:print('init_pwchanges  chk 1')
  if L not in dgroups:
   continue
  if L == Ldbg:print('init_pwchanges  chk 2')
  
  group = dgroups[L]
  lnum_meta = iline + 1
  metaline = line
  assert metaline == group.cdsl
  metaline_new =   group.ab
  # also bbline
  lnum_old = lnum_meta + 1
  bbline = lines[iline + 1] # line after metaline
  # usually there is no change needed in bbline.
  old = bbline
  new = bbline
  # most diffs are just in () in ab but not in cdsl
  if re.sub(r'[()]','',metaline_new) == metaline:
   cat = 'meta'
  else:
   cat = 'other'  # some other change
  change = Change(lnum_meta,metaline,metaline_new,lnum_old,old,new,cat)
  changes.append(change)
 return changes

if __name__=="__main__":
 filein = sys.argv[1] # AB's diff file
 fileout = sys.argv[2]  # revised diff file
 lines = read_lines(filein)
 groups = init_ab_groups(lines)
 print(len(groups),"groups found")
 write_groups(fileout,groups)
