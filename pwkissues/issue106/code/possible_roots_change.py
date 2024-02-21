# coding=utf-8
""" possible_roots_change.py
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
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

def make_changes(edits):
 changes = []
 for edit in edits:
  metaline = edit.metaline
  old = edit.bbline  # old
  lnum = edit.bblnum
  before,after = old.split('¦')
  m = re.search(r'^(.*?)([*])?({#.*?#})$',before)
  if m == None:
   print('make_changes ERROR 1')
  hom = m.group(1)
  asterisk = m.group(2) # either None or '*'
  if asterisk == None:
   asterisk = ''
  word = m.group(3)
  assert before == (hom + asterisk + word)
  newbefore = hom + asterisk + '√' + word
  new = newbefore + '¦' + after
  change = Change(metaline,lnum,old,new)
  changes.append(change)
 return changes

def write_changes(fileout,changes):
 outrecs = []
 outarr = [] # header
 outarr.append('; ******************************************************')
 outarr.append('; %s possible roots :' % len(changes))
 outarr.append('; ******************************************************')
 outrecs.append(outarr)
 for c in changes:
  outarr = []
  outarr.append('; ' + c.metaline)
  outarr.append('%s old %s' % (c.lnum,c.old))
  outarr.append(';')
  outarr.append('%s new %s' % (c.lnum,c.new))
  outrecs.append(outarr)
 write_recs(fileout,outrecs,blankflag=False)

class Editroot:
 def __init__(self,line):
  self.line = line
  m = re.search(r'^YES (.*?)\t(.*)$',line)
  self.bbline = m.group(1)
  self.metaline = m.group(2)
  # get L for matching with pw.txt
  m = re.search(r'<L>(.*?)<pc>',self.metaline)
  self.L = m.group(1)
  # filled later
  self.bblnum = None
  self.newbbline = None
  
def init_roots_edit(filein):
 lines = read_lines(filein)
 keep = [line for line in lines if line.startswith('YES ')]
 print(len(keep),"marked YES in",filein)
 editrecs = [Editroot(line) for line in keep]
 return editrecs

def set_lnum(edits,pwlines):
 dedit = {}
 for edit in edits:
  dedit[edit.L] = edit
 #
 for iline,pwline in enumerate(pwlines):
  m = re.search(r'<L>(.*?)<pc>',pwline)
  if m == None:
   continue
  pwL = m.group(1)
  if pwL not in dedit:
   continue
  edit = dedit[pwL]
  iline1 = iline + 1
  lnum = iline1 + 1  # line number of bbline
  edit.bblnum = lnum
  assert edit.metaline == pwline
  assert edit.bbline == pwlines[iline1]
  
if __name__=="__main__":
 filein = sys.argv[1]  # pw.txt
 filein1 = sys.argv[2] # possible_roots_edit.txt
 fileout = sys.argv[3]  #  change transactions

 pwlines = read_lines(filein)
 edits = init_roots_edit(filein1)
 set_lnum(edits,pwlines)
 
 changes = make_changes(edits)
 write_changes(fileout,changes)

