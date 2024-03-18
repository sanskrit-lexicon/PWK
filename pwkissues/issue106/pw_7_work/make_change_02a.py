# coding=utf-8
""" make_change_02a.py for pw_7_work
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

def get_outarr_meta(c):
 # change to metaline.  Need to check bbline
 outarr = []
 outarr.append('; %s cat=%s' % (c.metaline,c.cat))
 # change to metaline
 outarr.append('%s old %s' %(c.lnum_meta,c.metaline))
 outarr.append('%s new %s' %(c.lnum_meta,c.metaline_new))
 outarr.append('; ---- change to bbline ?')
 outarr.append('%s old %s' %(c.lnum_old,c.old))
 outarr.append(';')
 outarr.append('%s new %s' %(c.lnum_old,c.new))
 outarr.append('; ----------------------------------------------')
 return outarr

def get_outarr_other(c):
 # change to some other line.
 outarr = []
 outarr.append('; %s cat=%s' % (c.metaline,c.cat))
 # change to some other line, probably not bbline
 #if ('¦' in c.old) or ('<L>' in c.old):
 # print('get_outarr_other: %s\nold=%s' %(c.lnum_old,c.old))
 outarr.append('%s old %s' %(c.lnum_old,c.old))
 outarr.append(';')
 outarr.append('%s new %s' %(c.lnum_old,c.new))
 outarr.append('; ----------------------------------------------')
 return outarr

def get_outarr_metabb(c):
 # changes to both metaline and bbline
 outarr = []
 outarr.append('; %s cat=%s' % (c.metaline,c.cat))
 # change to metaline
 outarr.append('%s old %s' %(c.lnum_meta,c.metaline))
 outarr.append('%s new %s' %(c.lnum_meta,c.metaline_new))
 outarr.append('; ---- ')
 outarr.append('%s old %s' %(c.lnum_old,c.old))
 outarr.append(';')
 outarr.append('%s new %s' %(c.lnum_old,c.new))
 outarr.append('; ----------------------------------------------')
 return outarr

def write_changes(fileout,changes,option):
 outrecs = []
 outarr = [] # header
 outarr.append('; ******************************************************')
 outarr.append('; %s: %s changes' % (option,len(changes)))
 outarr.append('; ******************************************************')
 outrecs.append(outarr)
 
 for c in changes:
  if c.cat == 'meta':
   outarr = get_outarr_meta(c)
  elif c.cat == 'other':
   outarr = get_outarr_other(c)
  elif c.cat == 'metabb':
   outarr = get_outarr_metabb(c)
  else:
   print('write_changes_error. unknown cat=',c.cat)
   exit(1)
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
  parts = lines[0].split(',')  # lnums
  try:
   lnums = [int(part) for part in parts]
  except:
   print('AB_change error: lines=',lines)
  numlnums = len(lnums)
  assert numlnums in (1,2)
  self.lnums = lnums
  self.cdsls = []
  self.abs = []
  if (numlnums == 1) and (n0 == 4):
   a,b,c,d = lines
   m = re.search(r'\(CDSL\): (.*)$',b)
   self.cdsls.append(m.group(1))
   m = re.search(r'\(AB\): (.*)$',c)
   self.abs.append(m.group(1))
  elif (numlnums == 2) and (n0 == 6):
   assert lnums[1] == (lnums[0] + 1)
   a,b,c,d,e,f = lines
   m = re.search(r'\(CDSL\): (.*)$',b)
   self.cdsls.append(m.group(1))
   m = re.search(r'\(CDSL\): (.*)$',c)
   self.cdsls.append(m.group(1))
   m = re.search(r'\(AB\): (.*)$',d)
   self.abs.append(m.group(1))
   m = re.search(r'\(AB\): (.*)$',e)
   self.abs.append(m.group(1))
  else:
   print('unexpected:',n0,lnums)
   print('AB_change ERROR:',len(lines))
   for line in lines:
    print(line)
   exit(1)

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
 return groups

def get_prev_meta_iline(lines,ilinemeta):
 found = False
 while ilinemeta > 0:
  ilinemeta = ilinemeta - 1
  if lines[ilinemeta].startswith('<L>'):
   found = True
   break
 if not found:
  print('get_changes_2 ERROR 2',lnum)
  exit(1)
 return ilinemeta

def get_changes_1(lines,group):
 glnum = group.lnums[0]
 cdsl  = group.cdsls[0]
 ab = group.abs[0]
 giline = glnum - 1
 pwline = lines[giline]
 if cdsl != pwline:
  print('get_changes_1:',glnum)
  print('cdsl=',cdsl)
  print('pwline=',pwline)
 if cdsl.startswith('<L>'):
  metaline = cdsl
  lnum_meta = glnum
  metaline_new = ab
  iline_old = giline + 1
  old = lines[iline_old]
  lnum_old = iline_old + 1
  new = old  # must be examined
  cat = 'meta'
  change = Change(lnum_meta,metaline,metaline_new,lnum_old,old,new,cat)
 else:
  # look backwards in lines for preceding metaline
  ilinemeta = get_prev_meta_iline(lines,giline)
  metaline = lines[ilinemeta]
  metaline_new = metaline
  lnum_meta = ilinemeta + 1
  iline_old = giline
  old = lines[iline_old]
  lnum_old = iline_old + 1
  new = ab
  cat = 'other'
  change = Change(lnum_meta,metaline,metaline_new,lnum_old,old,new,cat)
 return change

def get_changes_2(lines,group):
 # [0] is change in metaline
 # [1] is change in bbline
 glnum = group.lnums[0]
 cdsl  = group.cdsls[0]
 ab = group.abs[0]
 giline = glnum - 1
 pwline = lines[giline]
 cs = []
 if cdsl.startswith('<L>'):
  lnum_meta = glnum
  metaline = cdsl
  metaline_new = ab
  iline_old = giline + 1
  lnum_old = iline_old + 1
  assert lnum_old == group.lnums[1]
  old = lines[iline_old]
  assert old == group.cdsls[1]
  new = group.abs[1]
  cat = 'metabb'
  change = Change(lnum_meta,metaline,metaline_new,lnum_old,old,new,cat)
  cs.append(change)
 else:
  #print('get_changes_2 problem',glnum)
  #change = None
  ilinemeta = get_prev_meta_iline(lines,giline)
  metaline = lines[ilinemeta]
  metaline_new = metaline
  lnum_meta = ilinemeta + 1
  # two separate changes
  cs = []
  for i,lnum_old in enumerate(group.lnums):
   old = group.cdsls[i]
   new = group.abs[i]
   cat = 'other'
   change = Change(lnum_meta,metaline,metaline_new,lnum_old,old,new,cat)
   cs.append(change)
 return cs

def get_changes(lines,groups):
 changes = []
 for group in groups:
  if len(group.lnums) == 1:
   change = get_changes_1(lines,group)
   changes.append(change)
  elif len(group.lnums) == 2:
   cs = get_changes_2(lines,group)
   for change in cs:
    changes.append(change)
  else:
   print('get_changes ERROR',group.lnums)
   exit(1)
 return changes

if __name__=="__main__":
 filein = sys.argv[1]  # pw.txt
 filein1 = sys.argv[2] # AB's pw_5.differences.latest.txt
 fileout = sys.argv[3]  # 
 lines = read_lines(filein)
 lines1 = read_lines(filein1)
 groups = init_ab_changes(lines1) # list of AB_change records
 changes = get_changes(lines,groups)
 write_changes(fileout,changes,'02')
 
 
