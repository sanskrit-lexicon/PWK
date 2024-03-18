# coding=utf-8
""" make_change_03.py for pw_7_work
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
 
if __name__=="__main__":
 filein = sys.argv[1]  # pw.txt
 filein1 = sys.argv[2] # AB's diff file
 fileout = sys.argv[3]  # work version of pw.txt
 lines = read_lines(filein)
 lines1 = read_lines(filein1)
 groups = init_ab_changes(lines1,lines)
 print(len(groups),"groups found")
 newlines = lines.copy()
 change_lines(groups,newlines)
 write_lines(fileout,newlines)
