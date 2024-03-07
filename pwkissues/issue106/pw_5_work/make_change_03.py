# coding=utf-8
""" make_change_03.py
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
matchkeydbg = '<hom>3.</hom> √{#kar#}¦ mit {#aBipra#} 6.'

def get_matchkey(x):
 key = re.sub(r'— Mit.*$','',x)
 key = key[0:45]
 key = re.sub(r' *$','',key)
 return key
class AB_change:
 def __init__(self,lines):
  self.lines = lines
  try:
   a,b,c,d = lines
  except:
   print('AB_change ERROR:',len(lines))
   for line in lines:
    print(line)
   exit(1)
  m = re.search(r'^[0-9]+$',a)
  assert m != None
  self.a = a
  m = re.search(r'\(CDSL\): (.*)$',b)
  self.cdsl = m.group(1)
  m = re.search(r'\(AB\): (.*)$',c)
  self.ab = m.group(1)
  m = re.search(r'^-+$',d)
  assert m != None
  self.cdslkey = get_matchkey(self.cdsl) 
  if False:
   if a == '62989':
    print('AB_change: a=%s, cdslkey="%s"' %(a,self.cdslkey))
    print('matchkeydbg="%s"' % matchkeydbg)
def split_list(a, k):
    """
    Splits a list 'a' into 'k' equal-sized chunks.
    """
    n = len(a) // k  # Calculate the size of each chunk
    return [a[i * n: (i + 1) * n] for i in range(k)]

def test_split_list():
 print('test_split_list')
 a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
 k = len(a) // 3
 groups = split_list(a,k)
 print('a=',a)
 for group in groups:
  print(group)
 exit(1)
# test_split_list()

def init_ab_changes(lines):
 # groups of 4 lines
 q,r = divmod(len(lines),4)
 assert r == 0
 grouplist = split_list(lines,q)
 groups = [AB_change(grouplines) for grouplines in grouplist]
 print('init_ab_changes: %s groups found' % len(groups))
 d = {}
 for group in groups:
  cdslkey = group.cdslkey
  #if cdslkey == matchkeydbg:
  # print('init_ab_changes. found %s' % matchkeydbg)
  if cdslkey in d:
   print('init_ab_changes: dup:',cdslkey)
  d[cdslkey] = group.ab
 changemap = d
 return changemap

def get_changes(lines,changemap):
 changes = []
 used = {}
 for key in changemap:
  used[key] = 0
 
 for iline,line in enumerate(lines):
  matchkey = get_matchkey(line)
  #dbg = matchkey == matchkeydbg
  #if dbg: print('"%s" in changemap = %s' % (matchkey,matchkey in changemap))
  if matchkey not in changemap:
   continue
  ab1 = changemap[matchkey]
  # line is a bbline
  ilinemeta = iline-1
  metaline = lines[ilinemeta]
  # only consider pwkvn elements where L > 200000
  m = re.search(r'<L>(.*?)<',metaline)
  Lfloat = float(m.group(1))
  if Lfloat < 200000.0:
   continue
  lnum = iline + 1
  old = line
  new = ab1
  m = re.search(r'(<info n="sup_."/>)',old)
  if m != None:
   sup = m.group(1)
   new = ab1 + sup
   metaline = '%s (chk SUP: %s)' % (metaline,sup)
  change = Change(metaline,lnum,old,new)
  changes.append(change)
  #group.used = group.used + 1
  used[matchkey] = used[matchkey] + 1
 for key in changemap:
  if used[key] == 0:
   print('UNUSED:',key)
 return changes

def write_unused_groups(fileout,groups):
 # check for unused changemap
 lines = []
 for group in groups:
  if group.used != 1:
   for x in group.lines:
    lines.append(x)
 write_lines(fileout,lines)
 
if __name__=="__main__":
 filein = sys.argv[1]  # pw.txt
 filein1 = sys.argv[2] # AB's pwkvn_4.differences-X.txt
 fileout = sys.argv[3]  # 
 lines = read_lines(filein)
 lines1 = read_lines(filein1)
 changemap = init_ab_changes(lines1)
 changes = get_changes(lines,changemap)
 write_changes(fileout,changes,'xx')
 
 
