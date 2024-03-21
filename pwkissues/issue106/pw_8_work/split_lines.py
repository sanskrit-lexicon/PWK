# coding=utf-8
""" split_lines.py for pw_8_work
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

class AB_change:
 def __init__(self,lines):
  self.lines = lines
  assert re.search(r'^[0-9]+$',lines[0])
  lnum = int(lines[0])
  self.lnum = lnum
  m = re.search(r'^\(CDSL\): (.*)$',lines[1])
  self.cdsl = m.group(1)
  self.abs = []
  # array of replacement lines
  for line in lines[2:-1]:
   m = re.search(r'^\(AB\): (.*)$',line)
   self.abs.append(m.group(1))

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

def split_lines(lines,groups):
 newlines = []
 meta = None
 dgroups = group_lnum_map(groups) 
 for iline,line in enumerate(lines):
  lnum = iline + 1
  if lnum not in dgroups:
   newlines.append(line)
   continue
  group = dgroups[lnum]
  if line != group.cdsl:
   print('split_lines error:',lnum)
   print('cdsl file: ',line)
   print('cdsl group:',group.cdsl)
   newlines.append(line)
   continue
  # normal replacement
  for x in group.abs:
   newlines.append(x)
 return newlines

def group_lnum_map(groups):
 d = {}
 for g in groups:
  lnum = int(g.lnum)
  if lnum in d:
   print('group_lnum_map: duplicate',lnum)
  d[lnum] = g
 return d

if __name__=="__main__":
 filein = sys.argv[1]   # old pw file
 fileinab = sys.argv[2] # AB's diff file
 fileout = sys.argv[3]  # new pw file
 lines = read_lines(filein)
 lines1 = read_lines(fileinab)
 groups = init_ab_groups(lines1)
 print(len(groups),"groups found")
 newlines = split_lines(lines,groups)
 write_lines(fileout,newlines)
 
