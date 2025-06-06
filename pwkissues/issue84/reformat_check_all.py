# coding=utf-8
""" reformat_check_all.py
"""
from __future__ import print_function
import sys, re, codecs
# import json

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_recs(fileout,outrecs):
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outrecs),"cases written to",fileout)
   
def write_lines(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"cases written to",fileout)

def generate_groups(lines):
 """  sample group of 6 lines
048
TODO key (13,200,7): pagerec not found
L= 106757, hw= vfzalayAjaka, pc=6-154-a
check: ?
AB: (3,200,7) ;;Jim's corrrection to be reverted and corrected
----------------------------------------------
"""
 group = []  
 for iline,line in enumerate(lines):
  group.append(line)
  if line.startswith('---'): # last line of group
   yield group
   group = []

class Group():
 def __init__(self,glines,num,p0,a0,v0,p1,a1,v1,L,hw,pc,comment):
  self.glines = glines
  self.case = num
  self.p0 = p0
  self.a0 = a0
  self.v0 = v0
  self.p1 = p1
  self.a1 = a1
  self.v1 = v1
  self.L = L
  self.hw = hw
  self.pc = pc
  self.comment = comment
  
def init_groups(lines):
 grouplines = list(generate_groups(lines))
 print(len(grouplines),"groups found")
 groups = []
 for glines in grouplines:
  num = glines[0]
  m = re.search('^TODO key \(([0-9]+),([0-9]+),([0-9]+)\): pagerec not found$',glines[1])
  if m == None:
   print('problem with group %s, line %s' % (num,1))
   print(glines[1])
   exit(1)
  p0 = int(m.group(1))
  a0  = int(m.group(2))
  v0  = int(m.group(3))
  
  gline = glines[2]
  m = re.search(r'^L= (.*?), hw= (.*?), pc=(.*)$',gline)
  if m == None:
   print('problem with group %s, line %s' % (num,2))
   print(gline)
   exit(1)
  L = m.group(1)
  hw = m.group(2)
  pc = m.group(3)
  gline = glines[3]
  if gline != 'check: ?':
   print('problem with group %s, line %s' % (num,3))
   print(gline)
   exit(1)
  gline = glines[4]
  m = re.search(r'^AB: \(([0-9]+),([0-9]+),([0-9]+)\) +;;(.*)$',gline)
  if m == None:
   print('problem with group %s, line %s' % (num,3))
   print(gline)
   exit(1)
  p1 = int(m.group(1))
  a1  = int(m.group(2))
  v1  = int(m.group(3))
  comment = m.group(4)
  group = Group(glines,num,p0,a0,v0,p1,a1,v1,L,hw,pc,comment)
  groups.append(group)
 return groups

def outgroup(group):
 glines = group.glines
 L = group.L
 hw = group.hw
 p0 = group.p0
 a0 = group.a0
 v0 = group.v0
 p1 = group.p1
 a1 = group.a1
 v1 = group.v1
 old = 'MBH. %s,%s,%s' %(p0,a0,v0)
 new = 'MBH. %s,%s,%s' %(p1,a1,v1)
 newline = '%s : %s : %s : %s : pc' %(L,hw,old,new)
 orgmode = '* TODO %s' % glines[0]
 outarr = [orgmode] + glines[1:5] + [newline,glines[5]]
 #print(outarr)
 #exit(1)
 return outarr

if __name__ == "__main__":
 filein = sys.argv[1]  # 
 fileout = sys.argv[2]  # 
 lines = read_lines(filein)
 groups = init_groups(lines)
 outrecs = [outgroup(group) for group in groups]
 write_recs(fileout,outrecs)

 
 
