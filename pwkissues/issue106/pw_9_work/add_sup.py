# coding=utf-8
""" add_sup.py for pw_9_work
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

def check_sup_cdsl(lines):
 meta = False
 nprob = 0
 vnflag = None
 supsfound = []
 nvns = 0 # number of vn entries
 nsups = 0 # number of lines with re.search(r'<info n="sup_[0-9]"/>$',line)
 for iline,line in enumerate(lines):
  if re.search(r'<info n="sup_[0-9]"/>$',line):
   nsups = nsups + 1
  if line.startswith('<L>'):
   meta = line
   m = re.search(r'^<L>(.*?)<pc>',meta)
   L = float(m.group(1))
   vnflag = (L >= 200000.0)
   supsfound = []
   if vnflag:
    nvns = nvns + 1
   #if meta.startswith('<L>200002<pc>'):
   # print('checkmeta: vnflag=%s meta=%s' %(vnflag,meta))
  elif line.startswith('<LEND>'):
   if (vnflag == True) and (len(supsfound) != 1):
    print('problem 1 with',meta)
    print('vnflag=%s, # sups=%s' %(vnflag,len(supsfound)))
    exit(1)
   elif (vnflag == False) and (len(supsfound) != 0):
    print('problem 2 with',meta)
    print('vnflag=%s, # sups=%s' %(vnflag,len(supsfound)))
    exit(1)
   meta = None
   vnflag = None
   supsfound = []
  elif meta == False:
   # before first entry
   pass
  elif (meta != None):
   # in an entry
   if (vnflag == True):
    # in an entry in the vn section 
    m = re.search(r'<info n="sup_[0-9]"/>$',line)
    if m != None:
     supsfound.append(line)
    # if meta.startswith('<L>200002<pc>'): print('dbg: m=%s\nline=%s' %(m,line))
 print('nvns=%s, nsups=%s' %(nvns,nsups))
 return # None

def add_sup(lines,lines1):
 # lines from AB
 # lines1 from temp_pw_9
 newlines = [] # revision of lines
 meta = None
 nchg = 0 
 for iline,line in enumerate(lines):
  line1 = lines1[iline]
  if line.startswith('<L>'):
   meta = line
   assert line1.startswith('<L>')
   # check for comparable meta lines
   m = re.search(r'^<L>(.*?)<pc>',line)
   L = m.group(1)
   m1 = re.search(r'^<L>(.*?)<pc>',line1)
   L1 = m1.group(1)
   assert L == L1
   newlines.append(line)
  elif line.startswith('<LEND>'):
   assert line1.startswith('<LEND>')
   newlines.append(line)
  elif meta == None:
   newlines.append(line)
  else:
   # meta != None. in an entry
   m1 = re.search(r'(<info n="sup_[0-9]"/>)$',line1)
   if m1 == None:
    newlines.append(line)
   else:
    sup = m1.group(1)
    newline = line + sup
    newlines.append(newline)
    nchg = nchg + 1
 assert len(newlines) == len(lines)
 print('add_sup changes %s lines' % nchg)
 return newlines
if __name__=="__main__":
 filein = sys.argv[1]   # AB cdsl file (one of two)
 filein1 = sys.argv[2] # ../temp_pw_9
 fileout = sys.argv[3]  # new version of AB cdsl file
 lines = read_lines(filein)
 lines1 = read_lines(filein1)
 check_sup_cdsl(lines1)
 assert len(lines) == len(lines1)
 newlines = add_sup(lines,lines1)
 write_lines(fileout,newlines)
 
