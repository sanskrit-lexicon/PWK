# coding=utf-8
""" make_change.py
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

def init_bb_iline_dict(lines):
 d = {}
 for iline,line in enumerate(lines):
  if not '¦' in line:
   continue
  if line in d:
   print('Warning - duplicate',iline,line)
   d[line] = -1  # later code takes this into account
  else: 
   d[line] = iline
 return d

def init_bb_iline_dict1(lines1a,iline_d):
 d1 = {}
 for line in lines1a:
  if line in iline_d:
   d1[line] = iline_d[line]
  else:
   print('init_bb_iline_dict1 NOT FOUND',line)
   exit(1)
 return d1

def adjust_lines2a(lines2a, lines1a):
 lines2b = []
 nsame = 0
 ndiff = 0
 for i,line2a in enumerate(lines2a):
  line1a = lines1a[i]
  assert line2a != line1a
  # specialized difference
  m = re.search(r'^(.*)(<info n="sup_[1-7]"/>)$',line1a)
  assert m != None
  info = m.group(2)
  line2b = line2a + info
  lines2b.append(line2b)
  if line2b == line1a:
   nsame = nsame + 1
  else:
   ndiff = ndiff + 1
 print('adjust_lines2a: nsame=%s, ndiff=%s' %(nsame,ndiff))
 return lines2b

def make_changes_01(lines1a,lines2b,iline_d1,lines,option):
 changes = []
 new_lines1a = []
 for i,line1a in enumerate(lines1a):
  line2b = lines2b[i]
  if line1a == line2b:
   # no change
   new_lines1a.append(line1a)
   continue
  # option 01
  test2b = line2b.replace('!√','')
  if line1a != test2b:
   new_lines1a.append(line1a)
   continue
  iline = iline_d1[line1a]
  if iline == -1:  # a duplicate 
   print('changes_01 WARNING:',line1a)
   new_lines1a.append(line1a)
   continue
  bbline = lines[iline]
  assert bbline == line1a
  ilinemeta = iline - 1
  metaline = lines[ilinemeta]
  assert metaline.startswith('<L>')
  lnum = iline + 1
  change = Change(metaline,lnum,bbline,line2b)
  changes.append(change)
  new_lines1a.append(line2b)
 print(len(changes),"changes")
 return changes,new_lines1a

def make_changes_02(lines1a,lines2b,iline_d1,lines,option):
 changes = []
 new_lines1a = []
 for i,line1a in enumerate(lines1a):
  line2b = lines2b[i]
  if line1a == line2b:
   # no change
   new_lines1a.append(line1a)
   continue
  # option 02
  test2b = line2b.replace('√','')
  if line1a != test2b:
   new_lines1a.append(line1a)
   continue
  iline = iline_d1[line1a]
  if iline == -1:  # a duplicate 
   print('changes_02 WARNING:',line1a)
   new_lines1a.append(line1a)
   continue
  bbline = lines[iline]
  assert bbline == line1a
  ilinemeta = iline - 1
  metaline = lines[ilinemeta]
  assert metaline.startswith('<L>')
  lnum = iline + 1
  change = Change(metaline,lnum,bbline,line2b)
  changes.append(change)
  new_lines1a.append(line2b)
 print(len(changes),"changes")
 return changes,new_lines1a

def make_changes_03(lines1a,lines2b,iline_d1,lines,option):
 changes = []
 new_lines1a = []
 for i,line1a in enumerate(lines1a):
  line2b = lines2b[i]
  if line1a == line2b:
   # no change
   new_lines1a.append(line1a)
   continue
  # option 03
  test2b = line2b.replace('¦','')
  test1a = line1a.replace('¦','')
  if test1a != test2b:
   new_lines1a.append(line1a)
   continue
  iline = iline_d1[line1a]
  if iline == -1:  # a duplicate 
   print('changes_03 WARNING:',line1a)
   new_lines1a.append(line1a)
   continue
  bbline = lines[iline]
  assert bbline == line1a
  ilinemeta = iline - 1
  metaline = lines[ilinemeta]
  assert metaline.startswith('<L>')
  lnum = iline + 1
  change = Change(metaline,lnum,bbline,line2b)
  changes.append(change)
  new_lines1a.append(line2b)
 print(len(changes),"changes")
 return changes,new_lines1a

def make_changes_04(lines1a,lines2b,iline_d1,lines,option):
 changes = []
 new_lines1a = []
 for i,line1a in enumerate(lines1a):
  line2b = lines2b[i]
  if line1a == line2b:
   # no change
   new_lines1a.append(line1a)
   continue
  # option 04
  # remaining lines are different.  Generate a change
  # manually examine
  iline = iline_d1[line1a]
  if iline == -1:  # a duplicate 
   print('changes_03 WARNING:',line1a)
   new_lines1a.append(line1a)
   continue
  bbline = lines[iline]
  assert bbline == line1a
  ilinemeta = iline - 1
  metaline = lines[ilinemeta]
  assert metaline.startswith('<L>')
  lnum = iline + 1
  change = Change(metaline,lnum,bbline,line2b)
  changes.append(change)
  new_lines1a.append(line2b)
 print(len(changes),"changes")
 return changes,new_lines1a

if __name__=="__main__":
 option = sys.argv[1]
 filein = sys.argv[2]  # pw.txt
 filein1 = sys.argv[3] # cdsl-extract from AB
 filein2 = sys.argv[4] # ab-version  
 fileout = sys.argv[5]  # change file 
 fileout1 = sys.argv[6] # new version of filein1
 lines = read_lines(filein)
 lines1 = read_lines(filein1) # cdsl
 lines1a = [x for x in lines1 if '¦' in x]  
 lines2 = read_lines(filein2) # ab
 lines2a = [x for x in lines2 if '¦' in x]
 print(len(lines1a),len(lines2a))
 assert len(lines1a) == len(lines2a)
 # lines1a and lines2a are 'parallel'; i.e.
 # arrays have same length and 
 # lines1a[i] is comparable to lines2a[i]
 lines2b = adjust_lines2a(lines2a, lines1a)
 
 iline_d = init_bb_iline_dict(lines)
 iline_d1 = init_bb_iline_dict1(lines1a,iline_d)
 changeFname = 'make_changes_%s' %option
 changeF = locals()[changeFname]
 changes,new_lines1a = changeF(lines1a,lines2b,iline_d1,lines,option)
 write_changes(fileout,changes,option)
 write_lines(fileout1,new_lines1a)
 

