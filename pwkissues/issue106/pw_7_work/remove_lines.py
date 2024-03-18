# coding=utf-8
""" remove_lines
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
 def __init__(self,lines,pwlines):
  self.lines = lines
  n0 = len(lines)
  parts = lines[0].split(',')  # lnums
  try:
   lnums = [int(part) for part in parts]
  except:
   print('AB_change error: lines=',lines)
   exit(1)
  cdsls = []
  cdsl_ilinespw = []
  for i,lnumpw in enumerate(lnums):
   ilinepw = lnumpw - 1
   cdsl = pwlines[ilinepw]
   iline = i + 1
   line1 = lines[iline]
   chkline1 = '(CDSL): ' + cdsl
   if chkline1 != line1:
    print('AB_change problem 1: %s' % lines[0])
    exit(1)
   cdsls.append(cdsl)
   cdsl_ilinespw.append(ilinepw)
  abs = []
  i0 = len(lnums) + 1
  for iline,line in enumerate(lines):
   if iline < i0:
    # cdsl line
    continue
   if (iline+1) == n0:
    # last line ----
    continue
   # should be an AB line
   m = re.search(r'^\(AB\): (.*)$',line)
   if m != None:
    ab = m.group(1)
    abs.append(ab)
   else:
    print('AB_change problem 2: %s' % lines[0])
    print('# cdsls = ',len(cdsls))
    print(line)
    exit(1)
  if True and (lnums == [76890]): # debug
   print('check: %s  # abs = %s' % (lnums,len(abs)))
   #exit(1)
  self.lnums = lnums
  self.cdsls = cdsls
  self.cdsl_ilinespw = cdsl_ilinespw
  self.abs = abs

def get_groups(lines):
 group = []
 for iline,line in enumerate(lines):
  group.append(line)
  if line.startswith('-'):
   yield group
   group = []
   
def init_ab_changes(lines,pwlines):
 # groups
 groups0 = list(get_groups(lines))
 print(len(groups0),"groups found")
 #
 groups = []
 for group0 in groups0:
  groups.append(AB_change(group0,pwlines))
 return groups

def change_lines(groups,lines):
 # check group -- list lines is modified
 for igroup,group in enumerate(groups):
  ilines = group.cdsl_ilinespw
  nilines = len(ilines)
  assert nilines in (1,2)
  if nilines == 2:
   assert ilines[0]+1 == ilines[1]
  if igroup != 0:
   group0 = groups[igroup - 1] # prev group
   ilines0 = group0.cdsl_ilinespw
   assert ilines0[-1] < ilines[0]
 print('group check ok')
 groupsa = groups.copy()
 groupsa.reverse() # in reverse order
 for group in groupsa:
  ilines = group.cdsl_ilinespw
  cdsls = group.cdsls
  abs = group.abs
  if True and (group.lnums == [76890]): # debug
   print('change_line: %s, %s' %(group.lnums,len(abs)))
  iline0 = ilines[0]
  # remove the cdsls from lines
  for cdsl in cdsls:
   cdsl_prev = lines.pop(iline0)
   assert cdsl == cdsl_prev
  # insert the ab's
  lines[iline0:iline0] = abs
 #
 ncdsls = sum(len(g.cdsls) for g in groups)
 nabs = sum(len(g.abs) for g in groups)
 print('delete %s lines, insert %s lines' %(ncdsls,nabs))
 # 

def remove_lnums(lines,lnumstr):
 if lnumstr == '':
  ilines = []
 else:
  lnums = lnumstr.split(',')
  ilines = [int(lnum) for lnum in lnums]
 newlines = []
 for iline,line in enumerate(lines):
  if iline in ilines:
   lnum = iline + 1
   print('remove_lnums: line # ',lnum)
  else:
   newlines.append(line)
 return newlines

def remove_extra_in(lines):
 # remove empty lines within entry
 newlines = []
 nskip = 0 # number of lines skipped
 meta = None
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   newlines.append(line)
   meta = line
  elif line.startswith('<LEND>'):
   newlines.append(line)
   meta = None
  elif meta != None:
   if line.strip() == '':
    # skip blank line
    nskip = nskip + 1
    print('drop blank line at lnum = ',iline + 1)
   else:
    newlines.append(line)
  else:
   # meta is None - keep lines not in entry
   newlines.append(line)
 print('remove_extra_in: %s lines dropped' % nskip)
 print('remove_extra_in: %s lines returned' % len(newlines))
 return newlines

def remove_extra_out(lines):
 # remove extra empty lines outside of entry
 # so there is just 1 empty line between <LEND> and <L>...
 newlines = []
 nskip = 0 # number of lines skipped
 meta = False
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   newlines.append(line)
   meta = line
  elif line.startswith('<LEND>'):
   newlines.append(line)
   meta = None
   nempty = 0
  elif meta == False:
   # before first entry
   newlines.append(line)   
  elif meta != None:
   # keep line within entry
   newlines.append(line)
  elif meta == None:
   empty = (line.strip() == '')
   if empty:
    nempty = nempty + 1
    if nempty == 1:
     # keep this empty line
     newlines.append(line)
    else:
     # drop this empty line
     nskip = nskip + 1
   else:
    # non-empty line between entries.
    # for 'PW',  '<H>' lines are acceptable
    if line.startswith('<H>'):
     newlines.append(line)
    else:
     print('unexpected line between entries. current lnum=',iline + 1)
     print(line)
     print('---')
     newlines.append(line)
  else:
   print('remove_extra_out error',iline+1)
   print('line=',line)
   exit(1)
 print('remove_extra_out: %s lines dropped' % nskip)
 print('remove_extra_out: %s lines returned' % len(newlines))
 return newlines

if __name__=="__main__":
 lnumstr = sys.argv[1]  # remove these lnums
 filein = sys.argv[2]  # pw.txt
 fileout = sys.argv[3]  # work version of pw.txt
 lines = read_lines(filein)
 # newlines = lines.copy()
 newlines = remove_lnums(lines,lnumstr)
 newlines1 = remove_extra_in(newlines)
 newlines2 = remove_extra_out(newlines1)
 write_lines(fileout,newlines2)
 # only one empty line between entries
