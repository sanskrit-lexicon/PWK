# coding=utf-8
""" make_change_03.py for pw_8_work
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
 def __init__(self,metaline,lnum,old,new,cat):
  self.metaline = metaline
  self.lnum = lnum
  self.old = old
  self.new = new
  self.cat = cat
  #assert cat in ['meta','other','metabb']

def write_changes_helper(c):
 outarr = []
 outarr.append('; %s cat=%s' % (c.metaline,c.cat))
 outarr.append('%s old %s' %(c.lnum,c.old))
 outarr.append(';')
 outarr.append('%s new %s' %(c.lnum,c.new))
 outarr.append('; ----------------------------------------------')
 return outarr

def write_changes(fileout,changes,option):
 outrecs = []
 cats = []
 for c in changes:
  if c.cat not in cats:
   cats.append(c.cat)
 for cat0 in cats:
  changes1 = [c for c in changes if c.cat == cat0]
  outarr = [] # header
  outarr.append('; ******************************************************')
  outarr.append('; cat=%s: %s changes' % (cat0,len(changes1)))
  print('; cat=%s: %s changes' % (cat0,len(changes1)))
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
  assert len(lnums) == 1
  self.lnum = lnums[0]
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

def init_ab_groups(lines):
 # groups
 groups0 = list(get_groups(lines))
 print(len(groups0),"groups found")
 # normalize so each group has 4 lines
 groups1 = []
 for group in groups0:
  groups1.append(AB_change(group))
 return groups1

def get_cat_0(old,new,cat0):
 old1 = old.replace('¦','')
 new1 = new.replace('¦','')
 old2 = old1.replace('.)',').')
 new2 = new1.replace('.)',').')
 if '¦' in old:
  if old1 == new1:
   cat = cat0 + ':¦'
  elif old2 == new2:
   cat = cat0 + ':¦).'
  else:
   cat = cat0 + ':¦other'
 else: # not '¦' in old:
  if old2 == new2:
   cat = cat0 + ':).'
  else:
   cat = cat0 + ':other'
 return cat

def get_cat_1(old,new,cat0):
 if new == old + '.':
  return cat0 + ':end.'
 old1 = old.replace('√','') 
 new1 = new.replace('√','') 
 if old1 == new1:
  return cat0 + ':√'
 old2 = old1.replace('#}?', '#} ?')
 new2 = new1
 if old2 == new2:
  return cat0 + ':#}?'
 old3 = re.sub(r'[!√]','',old)
 new3 = re.sub(r'[!√]','',new)
 if old3 == new3:
  return cat0 + ':!√'
 old4 = re.sub(r'[ ¦.,°]','',old)
 new4 = re.sub(r'[ ¦.,°]','',new)
 if False:
  print('old4=',old4)
  print('new4=',new4)
  print('old4 == new4 is',old4 == new4)
 if old4 == new4:
  return cat0 + ':punct'
 return cat0 + ':other'

def get_cat_2(old,new,cat0):
 old1 = re.sub(r'[ ¦.,°!√]','',old)
 new1 = re.sub(r'[ ¦.,°!√]','',new)
 if old1 == new1:
  return cat0 + ':punct'
 replacements = (('{%',''), ('%}',''))
 old2 = old1
 new2 = new1
 for a,b in replacements:
  old2 = old2.replace(a,b)
  new2 = new2.replace(a,b)
 if old2 == new2:
  return cat0 + ':italic'

 replacements = (('{#',''), ('#}',''))
 old3 = old2
 new3 = new2
 for a,b in replacements:
  old3 = old3.replace(a,b)
  new3 = new3.replace(a,b)
 if old3 == new3:
  return cat0 + ':deva'
 if '〔' in old:
  return cat0 + ':ls〔'
 return cat0 + ':other'


def init_pwchanges(lines,dgroups,cat0):
 changes = []
 meta = None
 Fname = 'get_cat_%s' %cat0
 catF = globals()[Fname]

 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   meta = line
  # match by lnum
  lnum = iline + 1
  if lnum not in dgroups:
   continue
  group = dgroups[lnum]
  cdsl = group.cdsl
  ab   = group.ab
  if cdsl != line:
   print('init_pwchanges error, lnum=',lnum)
   print('  cdsl:',line)
   print('g.cdsl:',cdsl)
   exit(1)
  metaline = meta
  old = cdsl
  new = ab
  cat = catF(old,new,cat0)
  change = Change(metaline,lnum,old,new,cat)
  changes.append(change)
 return changes

def group_lnum_map(groups):
 d = {}
 for g in groups:
  lnum = int(g.lnum)
  if lnum in d:
   print('group_lnum_map: duplicate',lnum)
  d[lnum] = g
 return d

def make_changes_0(lines,groups):
 groups1 = [g for g in groups if (len(g.ab) - len(g.cdsl)) == 0]
 d1 = group_lnum_map(groups1)
 cat = '0'
 changes = init_pwchanges_0(lines,d1,cat)
 return changes

def make_changes_1(lines,groups):
 groups1 = [g for g in groups if (len(g.ab) - len(g.cdsl)) == 1]
 d1 = group_lnum_map(groups1)
 cat = '1'
 changes = init_pwchanges(lines,d1,cat)
 return changes

def make_changes_2(lines,groups):
 groups1 = []
 for g in groups:
  n = len(g.ab) - len(g.cdsl)
  if (n > 1) or (n < 0):
   groups1.append(g)
 #groups1 = [g for g in groups if () == 1]
 d1 = group_lnum_map(groups1)
 cat = '2'
 changes = init_pwchanges(lines,d1,cat)
 return changes

if __name__=="__main__":
 option = sys.argv[1]
 filein = sys.argv[2]   # pw file
 fileinab = sys.argv[3] # AB's diff file
 fileout = sys.argv[4]  # ?
 lines = read_lines(filein)
 lines1 = read_lines(fileinab)
 groups = init_ab_groups(lines1)
 print(len(groups),"groups found")
 Fname = 'make_changes_%s' %option
 changeF = locals()[Fname]
 changes = changeF(lines,groups)
 write_changes(fileout,changes,option)
