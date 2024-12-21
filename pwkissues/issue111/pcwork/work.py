#-*- coding:utf-8 -*-
""" work.py
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for line in lines:
   f.write(line+'\n')  
 print(len(lines),"written to",fileout)

def write_groups(fileout,outrecs):
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for line in outarr:
    f.write(line+'\n')  
 print(len(outrecs),"groups written to",fileout)

def write_grouprecs1(fileout,grouprecs):
 with codecs.open(fileout,"w","utf-8") as f:
  for grec in grouprecs:
   outarr = grec.group
   for line in outarr:
    f.write(line+'\n')  
 print("write_grouprecs1:",len(grouprecs),"groups written to",fileout)

def write_grouprecs2_helper(grec):
 if not grec.pc:
  first = 'pc: None'
 elif grec.pcval == None:
  first = 'pc: noval'
 else:
  first = 'pc: %s' % grec.pcval
 outarr = []
 outarr.append(grec.group[0])
 outarr.append(first)
 for line in grec.group[1:]:
  outarr.append(line)
 return outarr
 

def write_grouprecs2(fileout,grouprecs):
 with codecs.open(fileout,"w","utf-8") as f:
  for grec in grouprecs:
   outarr = write_grouprecs2_helper(grec)
   for line in outarr:
    f.write(line+'\n')  
 print("write_grouprecs2:",len(grouprecs),"groups written to",fileout)

def make_groups(lines):
 group = None
 for iline,line in enumerate(lines):
  if line.startswith('; <L>'):
   group = [line]
  elif line.startswith('; --------------------------'):
   try:
    group.append(line)
   except:
    print('make groups Error: lnum=',iline+1)
    exit(1)
   yield group
   group = None
  else:
   group.append(line)

def check_groups(groups):
 for group in groups:
  if not group[1].startswith('; <bot>'):
   print('chk 1:',group[1])
 n = 0
 for group in groups:
  for line in group[2:-1]:
   if line.startswith('; <bot>'):
    n = n + 1
    print('extra:',line)
 if n != 0:
  print(n,'extra "; <bot>" lines')

class Grouprec:
 def __init__(self,group):
  self.group = group
  key1 = group[1]  # comment line, usu. ' <bot> ...'
  metaline = group[0]
  m = re.search(r'<L>(.*?)<pc>(.*?)<k1>(.*?)<',metaline)
  L = m.group(1)
  pagecol = m.group(2)
  k1 = m.group(3)
  key2 = float(L)
  self.sortkey = (key1,key2)
  self.L = L
  self.pagecol = pagecol
  self.k1 = k1
  self.pc = False #print change
  for line in group:
   if 'print change' in line:
    self.pc = True
    break
  self.pcval = None
def init_grouprecs(groups):
 recs = [Grouprec(group) for group in groups]
 return recs

def check_grouprecs_line1(grouprecs):
 n = 0
 for grec in grouprecs:
  if not grec.group[1].startswith('; <bot>'):
   print('check:',grec.group[1])
   n = n + 1
 print('check_grouprecs_line1 finds %s problems' % n)
 
def mark_extra_bot(grouprecs):
 check_grouprecs_line1(grouprecs)
 n = 0
 for grec in grouprecs:
  for i,line in enumerate(grec.group):
   flag = line.startswith('; <bot>')
   if flag and (i > 1):
    grec.group[i] = grec.group[i].replace('; <bot>','; <botx>')
    n = n + 1
 print(n,'lines noted in mark_extra_bot')

def pc_botsp(grecs):
 for grec in grecs:
  for line in grec.group:
   m = re.search(r'; <bot>(.*?)</bot> .*? bot sp\. +"(.*?)".*?print change',line)
   if m == None:
    continue
   oldbot = m.group(1)
   newbot = m.group(2)
   x = '%s : %s : %s : %s' %(grec.L,grec.k1,oldbot,newbot)
   grec.pcval = x
if __name__=="__main__":
 option = sys.argv[1]
 filein = sys.argv[2] #  xxx.txt 
 fileout = sys.argv[3] #
 lines = read_lines(filein)
 print(len(lines),"lines read from",filein)
 groups = list(make_groups(lines))
 # check_groups(groups)
 grouprecs = init_grouprecs(groups)
 grouprecs1 = sorted(grouprecs,key = lambda grec : grec.sortkey)
 if option == 'sort':
  write_grouprecs1(fileout,grouprecs1)
 elif option == 'extra':
  mark_extra_bot(grouprecs1)
  write_grouprecs1(fileout,grouprecs1)
 elif option =='pcbotsp':
  pc_botsp(grouprecs1)
  write_grouprecs2(fileout,grouprecs1)
 else:
  print('unknown option',option)
  exit(1)



