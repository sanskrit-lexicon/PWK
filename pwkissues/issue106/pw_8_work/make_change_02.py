# coding=utf-8
""" make_change_02.py for pw_8_work
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

known_cats = ['paren','°','other']
class Change:
 def __init__(self,lnum_meta,metaline,metaline_new,lnum_old,old,new,cat):
  self.metaline = metaline
  self.metaline_new = metaline_new
  self.lnum_meta = lnum_meta
  self.lnum_old = lnum_old
  self.old = old
  self.new = new
  self.cat = cat
  if not cat in known_cats:
   print('Change: unexpected cat="%s"' % cat)

def write_changes_helper(c):
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

def write_changes(fileout,changes,option):
 outrecs = []
 for cat0 in known_cats:
  changes1 = [c for c in changes if c.cat == cat0]
  outarr = [] # header
  outarr.append('; ******************************************************')
  outarr.append('; cat=%s: %s changes' % (cat0,len(changes1)))
  outarr.append('; ******************************************************')
  outrecs.append(outarr)
  for c in changes1:
   outarr = write_changes_helper(c)
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
   
def init_ab_changes(lines):
 # groups
 groups0 = list(get_groups(lines))
 print(len(groups0),"groups found")
 #
 groups = []
 for group0 in groups0:
  groups.append(AB_change(group0))
 # lookup dictionary based on <L>
 d = {}
 for group in groups:
  m = re.search(r'^<L>(.*?)<pc>',group.cdsl)
  L = m.group(1)
  if L in d:
   print('unexpected duplicate ERROR')
   exit(1)
  else:
   d[L] = group
   # check ab the same L
   m = re.search(r'^<L>(.*?)<pc>',group.ab)
   Lab = m.group(1)
   assert L == Lab
 return groups,d

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
   cat = 'paren'
  elif re.sub(r'[°]','',metaline) == re.sub(r'[°]','',metaline_new):
   cat = '°'
  else:
   cat = 'other'  # some other change
  change = Change(lnum_meta,metaline,metaline_new,lnum_old,old,new,cat)
  changes.append(change)
 return changes

if __name__=="__main__":
 option = '02'
 filein = sys.argv[1]  # pw.txt
 filein1 = sys.argv[2] # AB's diff file
 fileout = sys.argv[3]  # change file
 lines = read_lines(filein)
 lines1 = read_lines(filein1)
 groups,dgroups = init_ab_changes(lines1)
 print(len(groups),"groups found")
 changes = init_pwchanges(lines,dgroups)
 write_changes(fileout,changes,option)
