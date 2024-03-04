# coding=utf-8
""" make_change_bbmulti.py
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

class Rec:
 def __init__(self,line):
  # line of bbmulti_NN.txt
  lnumstr,col2,data = line.split('\t')
  self.line = line
  self.lnum = int(lnumstr) # line number in pw.txt
  self.col2 = col2
  m = re.search('^([0-9]+)(√?)$',col2)
  self.bbk2num = int(m.group(1))
  self.root = m.group(2)
  self.data = data
  self.check(line)
  self.groups = self.parsedata(data)
 def parsedata(self,data):
  parts = data.split()
  groups = []
  h = None
  for part in parts:
   m1 = re.search(r'^<hom>([0-9])</hom>$',part)
   if m1 == None:
    m2 = re.search(r'^([*]?){#(.*?)#}$',part)
    assert m2 != None
    flag = m2.group(1)
    if flag == '':
     flag = None
    k2text = m2.group(2)
    group = (h,flag,k2text)
    groups.append(group)
    h = None
   else:
    h = m1.group(1)
  return groups
 def check(self,line):
  hws = re.findall('{#[^#]*#}',self.data)
  nhws = len(hws)
  if nhws != self.bbk2num:
   print('Rec_init_WARNING:')
   print('nhws = %s, bbk2num=%s' %(nhws,self.bbk2num))
   print(line)
     
def init_recs(lines):
 # bbmulti_00a.txt and similar
 recs = []
 for iline,line in enumerate(lines):
  rec = Rec(line)
  recs.append(rec)
 return recs

class Change:
 def __init__(self,metaline,meta_lnum,k2old,k2new,metaline_new,bbline):
  self.metaline = metaline
  self.meta_lnum = meta_lnum
  self.k2old = k2old
  self.k2new = k2new
  self.metaline_new = metaline_new
  self.bbline = bbline
  
def make_changes_01(lines,recs):
 changes = []
 skips = []  # rec.line when rec is skipped
 for rec in recs:
  skip = False
  k2s = []
  for group in rec.groups:
    hom,flag,hw = group
    if '°' in hw:
     skip = True
     break
    k2 = ''
    if hom != None:
     k2 = '%s. ' % hom
    if flag == '*':
     k2 = k2 + flag
    k2 = k2 + hw
    k2s.append(k2)
  if skip:
   skips.append(rec.line)
   continue
  # ready to make a metaline change to k2 field
  lnum = rec.lnum  # line number in pw.txt of bbline
  iline = lnum - 1
  bbline = lines[iline]
  meta_iline = iline - 1
  metaline = lines[meta_iline]
  meta_lnum = meta_iline + 1
  m = re.search(r'^(<L>.*?)<k2>(.*)$',metaline)
  assert m != None
  meta_pfx = m.group(1)
  k2old = m.group(2)
  k2new = ', '.join(k2s)
  metaline_new = meta_pfx + '<k2>' + k2new
  change = Change(metaline,meta_lnum,k2old,k2new,metaline_new,bbline)
  changes.append(change)
 return changes,skips

def make_changes_02(lines,recs):
 # matches '°#}'
 changes = []
 skips = []  # rec.line when rec is skipped
 for rec in recs:
  if '°#}' not in rec.data:
   skips.append(rec.line)
   continue
  k2s = []
  skip = False
  for group in rec.groups:
    hom,flag,hw = group
    k2 = ''
    if hom != None:
     k2 = '%s. ' % hom
    if flag == '*':
     k2 = k2 + flag
    k2 = k2 + hw
    k2s.append(k2)
  # ready to make a metaline change to k2 field
  lnum = rec.lnum  # line number in pw.txt of bbline
  iline = lnum - 1
  bbline = lines[iline]
  meta_iline = iline - 1
  metaline = lines[meta_iline]
  meta_lnum = meta_iline + 1
  m = re.search(r'^(<L>.*?)<k2>(.*)$',metaline)
  assert m != None
  meta_pfx = m.group(1)
  k2old = m.group(2)
  k2new = ', '.join(k2s)
  metaline_new = meta_pfx + '<k2>' + k2new
  change = Change(metaline,meta_lnum,k2old,k2new,metaline_new,bbline)
  changes.append(change)
 return changes,skips

def make_changes_03(lines,recs):
 # '{#°ka#}' occurs and no other °
 changes = []
 skips = []  # rec.line when rec is skipped
 for rec in recs:
  # {#°ka#} occurs
  if '{#°ka#}' not in rec.data:
   skips.append(rec.line)
   continue
  # no other °
  a_ = re.findall(r'°',rec.data)
  if len(a_) != 1:
   skips.append(rec.line)
   continue
                  
  k2s = []
  skip = False
  prevhw = None
  for igroup,group in enumerate(rec.groups):
    hom,flag,hw = group
    k2 = ''
    if hom != None:
     k2 = '%s. ' % hom
    if flag == '*':
     k2 = k2 + flag
    if (igroup == 0) and hw.startswith('°'):
     skip = True
     break
    if hw == '°ka':
     hom0,flag0,hw0 = rec.groups[igroup-1] # previous group
     # require last character of previous headword to be a vowel
     hwlast = hw0[-1]
     if hwlast not in 'aAiIuUfFeEoO':
      skip = True
      break
     hw = hw0 + 'ka'
     k2 = k2 + hw
     k2s.append(k2)
    else:
     k2 = k2 + hw
     k2s.append(k2)
  if skip:
   skips.append(rec.line)
   continue
  # ready to make a metaline change to k2 field
  lnum = rec.lnum  # line number in pw.txt of bbline
  iline = lnum - 1
  bbline = lines[iline]
  meta_iline = iline - 1
  metaline = lines[meta_iline]
  meta_lnum = meta_iline + 1
  m = re.search(r'^(<L>.*?)<k2>(.*)$',metaline)
  assert m != None
  meta_pfx = m.group(1)
  k2old = m.group(2)
  k2new = ', '.join(k2s)
  metaline_new = meta_pfx + '<k2>' + k2new
  change = Change(metaline,meta_lnum,k2old,k2new,metaline_new,bbline)
  changes.append(change)
 return changes,skips

def make_changes_04(lines,recs):
 # '{#°[mAInsg]#}' 
 changes = []
 skips = []  # rec.line when rec is skipped
 for rec in recs:
  # {#°.#} occurs
  a_ = re.findall(r'{#°[mAInsg]#}',rec.data)
  if len(a_) == 0:
   skips.append(rec.line)
   continue
  # g °
  a_ = re.findall(r'°',rec.data)
  ndot = len(a_)
  #if len(a_) != 1:
  # skips.append(rec.line)
  # continue
  # get k2s and skip                
  k2s = []
  skip = False
  for igroup,group in enumerate(rec.groups):
    hom,flag,hw = group
    k2 = ''
    if hom != None:
     k2 = '%s. ' % hom
    if flag == '*':
     k2 = k2 + flag
    if ndot != 1:
     if hw.startswith('°'):
      k2 = k2 + '?' + hw
     else:
      k2 = k2 + hw
     k2s.append(k2)
     continue
    # now ndot == 1
    if (igroup == 0) and hw.startswith('°'):
     skip = True
     break
    if not hw.startswith('°'):
     k2 = k2 + hw
     k2s.append(k2)
     continue
    c = hw[1]
    assert hw == '°' + c
    assert c in 'mAInsg'
    hom0,flag0,hw0 = rec.groups[igroup-1] # previous group
    hw0last = hw0[-1]
    if c in 'AI':
     if hw0last not in 'aAiIuUfFeEoO':
      skip = True
      break
     # replace last char in hw0 with c
     hw = hw0[0:-1] + c
     k2 = k2 + hw
     k2s.append(k2)
     continue
    if c in 'mns':
     if hw0last not in 'aAiIuUfFeEoO':
      skip = True
      break
     # append c to hw0
     hw = hw0 + c
     k2 = k2 + hw
     k2s.append(k2)
     continue
    if c in 'g': # just one case
     if hw0last not in 'k':
      skip = True
      break
     # replace last char in hw0 with c
     hw = hw0[0:-1] + c
     k2 = k2 + hw
     k2s.append(k2)
     continue
    assert True == False  # should never reach this line!
  if skip:
   skips.append(rec.line)
   continue
  # ready to make a metaline change to k2 field
  lnum = rec.lnum  # line number in pw.txt of bbline
  iline = lnum - 1
  bbline = lines[iline]
  meta_iline = iline - 1
  metaline = lines[meta_iline]
  meta_lnum = meta_iline + 1
  m = re.search(r'^(<L>.*?)<k2>(.*)$',metaline)
  assert m != None
  meta_pfx = m.group(1)
  k2old = m.group(2)
  k2new = ', '.join(k2s)
  metaline_new = meta_pfx + '<k2>' + k2new
  change = Change(metaline,meta_lnum,k2old,k2new,metaline_new,bbline)
  changes.append(change)
 return changes,skips

def make_changes_05(lines,recs):
 # {#Xca#} {#°cA#}  {#XcA#}  c a single character
 # also Xci
 changes = []
 skips = []  # rec.line when rec is skipped
 for rec in recs:
  #  occurs
  a_ = re.findall(r'°',rec.data)
  ndot = len(a_)
  groups = rec.groups
  if len(groups) != 2:
   skips.append(rec.line)
   continue
  group0,group = groups
  hom0,flag0,hw0 = group0
  hom,flag,hw = group
  m0 = re.search(r'^(.*)(.)(.)$',hw0)
  m  = re.search(r'^°(.)(.)$',hw)
  if (m0 == None) or (m == None):
   skips.append(rec.line)
   continue
  x0 = m0.group(1)
  c0 = m0.group(2)
  v0 = m0.group(3)
  c  = m.group(1)
  v  = m.group(2)
  if (c0 != c) or (v != v0.upper()):
   skips.append(rec.line)
   continue
  k2s = []
  k2 = ''
  if hom0 != None:
   k2 = '%s. ' % hom0
  if flag0 == '*':
   k2 = k2 + flag0
  k2 = k2 + hw0
  k2s.append(k2)
  #
  k2 = ''
  if hom != None:
   k2 = '%s. ' % hom
  if flag == '*':
   k2 = k2 + flag
  hw_new = x0 + c + v
  k2 = k2 + hw_new
  k2s.append(k2)
  # ready to make a metaline change to k2 field
  lnum = rec.lnum  # line number in pw.txt of bbline
  iline = lnum - 1
  bbline = lines[iline]
  meta_iline = iline - 1
  metaline = lines[meta_iline]
  meta_lnum = meta_iline + 1
  m = re.search(r'^(<L>.*?)<k2>(.*)$',metaline)
  assert m != None
  meta_pfx = m.group(1)
  k2old = m.group(2)
  k2new = ', '.join(k2s)
  metaline_new = meta_pfx + '<k2>' + k2new
  change = Change(metaline,meta_lnum,k2old,k2new,metaline_new,bbline)
  changes.append(change)
 return changes,skips

def make_changes_06(lines,recs):
 changes = []
 skips = []  # rec.line when rec is skipped
 for rec in recs:
  m = re.search(r'[/^\\]#}',rec.data)
  if m == None:
   skips.append(rec.line)
   continue
  k2s = []
  groups = rec.groups
  for group in groups:
   hom,flag,hw = group
   k2 = ''
   if hom != None:
    k2 = '%s. ' % hom
   if flag == '*':
    k2 = k2 + flag
   k2 = k2 + hw
   k2s.append(k2)
  # ready to make a metaline change to k2 field
  lnum = rec.lnum  # line number in pw.txt of bbline
  iline = lnum - 1
  bbline = lines[iline]
  meta_iline = iline - 1
  metaline = lines[meta_iline]
  meta_lnum = meta_iline + 1
  m = re.search(r'^(<L>.*?)<k2>(.*)$',metaline)
  assert m != None
  meta_pfx = m.group(1)
  k2old = m.group(2)
  k2new = ', '.join(k2s)
  metaline_new = meta_pfx + '<k2>' + k2new
  change = Change(metaline,meta_lnum,k2old,k2new,metaline_new,bbline)
  changes.append(change)
 return changes,skips

def make_changes_07(lines,recs):
 changes = []
 skips = []  # rec.line when rec is skipped
 for rec in recs:
  m = re.search(r'[^<][/^\\]',rec.data)
  if m == None:
   skips.append(rec.line)
   continue
  k2s = []
  groups = rec.groups
  for group in groups:
   hom,flag,hw = group
   k2 = ''
   if hom != None:
    k2 = '%s. ' % hom
   if flag == '*':
    k2 = k2 + flag
   k2 = k2 + hw
   k2s.append(k2)
  # ready to make a metaline change to k2 field
  lnum = rec.lnum  # line number in pw.txt of bbline
  iline = lnum - 1
  bbline = lines[iline]
  meta_iline = iline - 1
  metaline = lines[meta_iline]
  meta_lnum = meta_iline + 1
  m = re.search(r'^(<L>.*?)<k2>(.*)$',metaline)
  assert m != None
  meta_pfx = m.group(1)
  k2old = m.group(2)
  k2new = ', '.join(k2s)
  metaline_new = meta_pfx + '<k2>' + k2new
  change = Change(metaline,meta_lnum,k2old,k2new,metaline_new,bbline)
  changes.append(change)
 return changes,skips

def make_changes_08(lines,recs):
 changes = []
 skips = []  # rec.line when rec is skipped
 for rec in recs:
  m1 = re.search(r'<hom>',rec.data)
  m2 = re.search(r'^{#°',rec.data)
  if (m1 == None) and (m2 == None):
   skips.append(rec.line)
   continue
  k2s = []
  groups = rec.groups
  for group in groups:
   hom,flag,hw = group
   k2 = ''
   if hom != None:
    k2 = '%s. ' % hom
   if flag == '*':
    k2 = k2 + flag
   k2 = k2 + hw
   k2s.append(k2)
  # ready to make a metaline change to k2 field
  lnum = rec.lnum  # line number in pw.txt of bbline
  iline = lnum - 1
  bbline = lines[iline]
  meta_iline = iline - 1
  metaline = lines[meta_iline]
  meta_lnum = meta_iline + 1
  m = re.search(r'^(<L>.*?)<k2>(.*)$',metaline)
  assert m != None
  meta_pfx = m.group(1)
  k2old = m.group(2)
  k2new = ', '.join(k2s)
  metaline_new = meta_pfx + '<k2>' + k2new
  change = Change(metaline,meta_lnum,k2old,k2new,metaline_new,bbline)
  changes.append(change)
 return changes,skips

def make_changes_09(lines,recs):
 changes = []
 skips = []  # rec.line when rec is skipped
 for rec in recs:
  k2s = []
  groups = rec.groups
  if False and (len(groups)!= 2):
   skips.append(rec.line)
   continue
  skip = False
  hom0,flag0,hw0 = groups[0]
  assert not hw0.startswith('°')
  dbg = rec.data == '{#akaqama#} {#°cakra#}'
  dbg = False
  for igroup,group in enumerate(groups):
   hom,flag,hw = group
   if dbg: print('chk 1:',igroup,group)
   k2 = ''
   assert hom == None
   if hom != None:
    k2 = '%s. ' % hom
   if flag == '*':
    k2 = k2 + flag
   if igroup == 0:
    k2 = k2 + hw
    k2s.append(k2)
    continue
   # further filtering to revise 'hw' for groups 1,2...
   # as a concatenation with hw0
   if hw[0] != '°':
    skip = True
    continue
   hw = hw[1:]  # drop initial °
   c = hw[0] #  first character
   if c in hw0:
    skip = True
    continue
   # must be a composition with hw0
   k2 = k2 + hw0 + hw
   k2s.append(k2)
  if skip:
   skips.append(rec.line)
   continue
  # ready to make a metaline change to k2 field
  lnum = rec.lnum  # line number in pw.txt of bbline
  iline = lnum - 1
  bbline = lines[iline]
  meta_iline = iline - 1
  metaline = lines[meta_iline]
  meta_lnum = meta_iline + 1
  m = re.search(r'^(<L>.*?)<k2>(.*)$',metaline)
  assert m != None
  meta_pfx = m.group(1)
  k2old = m.group(2)
  k2new = ', '.join(k2s)
  metaline_new = meta_pfx + '<k2>' + k2new
  change = Change(metaline,meta_lnum,k2old,k2new,metaline_new,bbline)
  changes.append(change)
 return changes,skips

def make_changes_10(lines,recs):
 changes = []
 skips = []  # rec.line when rec is skipped
 for rec in recs:
  k2s = []
  groups = rec.groups
  if False and (len(groups)!= 2):
   skips.append(rec.line)
   continue
  skip = False
  hom0,flag0,hw0 = groups[0]
  assert not hw0.startswith('°')
  dbg = rec.data == '{#akaqama#} {#°cakra#}'
  dbg = False
  for igroup,group in enumerate(groups):
   hom,flag,hw = group
   if dbg: print('chk 1:',igroup,group)
   k2 = ''
   assert hom == None
   if hom != None:
    k2 = '%s. ' % hom
   if flag == '*':
    k2 = k2 + flag
   if igroup == 0:
    k2 = k2 + hw
    k2s.append(k2)
    continue
   # further filtering to revise 'hw' for groups 1,2...
   # as a concatenation with hw0
   if hw[0] != '°':
    skip = True
    continue
   hw = hw[1:]  # drop initial °
   c = hw[0] #  first character
   # c occurs just once in hw0
   regex = r'^([^%s]+)(%s)([^%s]+)$' %(c,c,c)
   m = re.search(regex,hw0)
   if m == None:
    skip = True
    continue
   pfx = m.group(1)
   # must be a composition with pfx
   k2 = k2 + pfx + hw
   k2s.append(k2)
  if skip:
   skips.append(rec.line)
   continue
  # ready to make a metaline change to k2 field
  lnum = rec.lnum  # line number in pw.txt of bbline
  iline = lnum - 1
  bbline = lines[iline]
  meta_iline = iline - 1
  metaline = lines[meta_iline]
  meta_lnum = meta_iline + 1
  m = re.search(r'^(<L>.*?)<k2>(.*)$',metaline)
  assert m != None
  meta_pfx = m.group(1)
  k2old = m.group(2)
  k2new = ', '.join(k2s)
  metaline_new = meta_pfx + '<k2>' + k2new
  change = Change(metaline,meta_lnum,k2old,k2new,metaline_new,bbline)
  changes.append(change)
 return changes,skips

def make_changes_11(lines,recs):
 changes = []
 skips = []  # rec.line when rec is skipped
 for rec in recs:
  k2s = []
  groups = rec.groups
  if False and (len(groups)!= 2):
   skips.append(rec.line)
   continue
  skip = False
  hom0,flag0,hw0 = groups[0]
  assert not hw0.startswith('°')
  dbg = rec.data == '{#akaqama#} {#°cakra#}'
  dbg = False
  for igroup,group in enumerate(groups):
   hom,flag,hw = group
   if dbg: print('chk 1:',igroup,group)
   k2 = ''
   assert hom == None
   if hom != None:
    k2 = '%s. ' % hom
   if flag == '*':
    k2 = k2 + flag
   if igroup == 0:
    k2 = k2 + hw
    k2s.append(k2)
    continue
   # further filtering to revise 'hw' for groups 1,2...
   # as a concatenation with hw0
   if hw[0] != '°':
    skip = True
    continue
   hw = hw[1:]  # drop initial °
   clen = 4
   if len(hw) < clen:
    skip = True
    continue
   c = hw[0:clen] #  first 4 characters
   # c occurs just once in hw0
   hw0_cs = re.findall(c,hw0)
   if len(hw0_cs) != 1:
    skip = True
    continue
   #
   idx = hw0.index(c)
   pfx = hw0[0:idx]  # so hw0 = pfx + --
   # set hw = pfx + hw
   k2 = k2 + pfx + hw
   k2s.append(k2)
  if skip:
   skips.append(rec.line)
   continue
  # ready to make a metaline change to k2 field
  lnum = rec.lnum  # line number in pw.txt of bbline
  iline = lnum - 1
  bbline = lines[iline]
  meta_iline = iline - 1
  metaline = lines[meta_iline]
  meta_lnum = meta_iline + 1
  m = re.search(r'^(<L>.*?)<k2>(.*)$',metaline)
  assert m != None
  meta_pfx = m.group(1)
  k2old = m.group(2)
  k2new = ', '.join(k2s)
  metaline_new = meta_pfx + '<k2>' + k2new
  change = Change(metaline,meta_lnum,k2old,k2new,metaline_new,bbline)
  changes.append(change)
 return changes,skips

def make_changes_12(lines,recs):
 changes = []
 skips = []  # rec.line when rec is skipped
 for rec in recs:
  k2s = []
  groups = rec.groups
  if False and (len(groups)!= 2):
   skips.append(rec.line)
   continue
  skip = False
  hom0,flag0,hw0 = groups[0]
  assert not hw0.startswith('°')
  dbg = rec.data == '{#akaqama#} {#°cakra#}'
  dbg = False
  for igroup,group in enumerate(groups):
   hom,flag,hw = group
   if dbg: print('chk 1:',igroup,group)
   k2 = ''
   assert hom == None
   if hom != None:
    k2 = '%s. ' % hom
   if flag == '*':
    k2 = k2 + flag
   if igroup == 0:
    k2 = k2 + hw
    k2s.append(k2)
    continue
   # further filtering to revise 'hw' for groups 1,2...
   # as a concatenation with hw0
   if hw[0] != '°':
    skip = True
    continue
   hw = hw[1:]  # drop initial °
   clen = 3
   if len(hw) < clen:
    skip = True
    continue
   c = hw[0:clen] #  first 3 characters
   # c occurs just once in hw0
   hw0_cs = re.findall(c,hw0)
   if len(hw0_cs) != 1:
    skip = True
    continue
   #
   idx = hw0.index(c)
   pfx = hw0[0:idx]  # so hw0 = pfx + --
   # set hw = pfx + hw
   k2 = k2 + pfx + hw
   k2s.append(k2)
  if skip:
   skips.append(rec.line)
   continue
  # ready to make a metaline change to k2 field
  lnum = rec.lnum  # line number in pw.txt of bbline
  iline = lnum - 1
  bbline = lines[iline]
  meta_iline = iline - 1
  metaline = lines[meta_iline]
  meta_lnum = meta_iline + 1
  m = re.search(r'^(<L>.*?)<k2>(.*)$',metaline)
  assert m != None
  meta_pfx = m.group(1)
  k2old = m.group(2)
  k2new = ', '.join(k2s)
  metaline_new = meta_pfx + '<k2>' + k2new
  change = Change(metaline,meta_lnum,k2old,k2new,metaline_new,bbline)
  changes.append(change)
 return changes,skips

def make_changes_13(lines,recs):
 changes = []
 skips = []  # rec.line when rec is skipped
 for rec in recs:
  k2s = []
  groups = rec.groups
  if False and (len(groups)!= 2):
   skips.append(rec.line)
   continue
  skip = False
  hom0,flag0,hw0 = groups[0]
  assert not hw0.startswith('°')
  dbg = rec.data == '{#akaqama#} {#°cakra#}'
  dbg = False
  for igroup,group in enumerate(groups):
   hom,flag,hw = group
   if dbg: print('chk 1:',igroup,group)
   k2 = ''
   assert hom == None
   if hom != None:
    k2 = '%s. ' % hom
   if flag == '*':
    k2 = k2 + flag
   if igroup == 0:
    k2 = k2 + hw
    k2s.append(k2)
    continue
   # further filtering to revise 'hw' for groups 1,2...
   # as a concatenation with hw0
   if hw[0] != '°':
    skip = True
    continue
   hw = hw[1:]  # drop initial °
   clen = 2
   if len(hw) < clen:
    skip = True
    continue
   c = hw[0:clen] #  first 2 characters
   # c occurs just once in hw0
   hw0_cs = re.findall(c,hw0)
   if len(hw0_cs) != 1:
    skip = True
    continue
   #
   idx = hw0.index(c)
   pfx = hw0[0:idx]  # so hw0 = pfx + --
   # set hw = pfx + hw
   k2 = k2 + pfx + hw
   k2s.append(k2)
  if skip:
   skips.append(rec.line)
   continue
  # ready to make a metaline change to k2 field
  lnum = rec.lnum  # line number in pw.txt of bbline
  iline = lnum - 1
  bbline = lines[iline]
  meta_iline = iline - 1
  metaline = lines[meta_iline]
  meta_lnum = meta_iline + 1
  m = re.search(r'^(<L>.*?)<k2>(.*)$',metaline)
  assert m != None
  meta_pfx = m.group(1)
  k2old = m.group(2)
  k2new = ', '.join(k2s)
  metaline_new = meta_pfx + '<k2>' + k2new
  change = Change(metaline,meta_lnum,k2old,k2new,metaline_new,bbline)
  changes.append(change)
 return changes,skips

def make_changes_14(lines,recs):
 changes = []
 skips = []  # rec.line when rec is skipped None are skipped in this version
 skip = False
 for rec in recs:
  k2s = []
  groups = rec.groups
  hom0,flag0,hw0 = groups[0]
  assert not hw0.startswith('°')
  for igroup,group in enumerate(groups):
   hom,flag,hw = group
   k2 = ''
   assert hom == None
   if hom != None:
    k2 = '%s. ' % hom
   if flag == '*':
    k2 = k2 + flag
   k2 = k2 + hw
   k2s.append(k2)
  if skip:
   skips.append(rec.line)
   continue
  # ready to make a metaline change to k2 field
  lnum = rec.lnum  # line number in pw.txt of bbline
  iline = lnum - 1
  bbline = lines[iline]
  meta_iline = iline - 1
  metaline = lines[meta_iline]
  meta_lnum = meta_iline + 1
  m = re.search(r'^(<L>.*?)<k2>(.*)$',metaline)
  assert m != None
  meta_pfx = m.group(1)
  k2old = m.group(2)
  k2new = ', '.join(k2s)
  metaline_new = meta_pfx + '<k2>' + k2new
  change = Change(metaline,meta_lnum,k2old,k2new,metaline_new,bbline)
  changes.append(change)
 return changes,skips

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

def write_changes(fileout,changes,option):
 nochange = 0 
 outrecs = []
 outarr = [] # header
 outarr.append('; ******************************************************')
 outarr.append('; %s: %s changes' % (option,len(changes)))
 outarr.append('; ******************************************************')
 outrecs.append(outarr)
 for c in changes:
  outarr = []
  lnum = int(c.meta_lnum)
  #outarr.append('; %s' % c.metaline)
  # change
  before,after = c.bbline.split('¦')
  # outarr.append('; ' + before + '¦')
  outarr.append('; ' + c.bbline)
  if c.metaline == c.metaline_new:
   outarr.append('; %s old %s' %(lnum,c.metaline))
   outarr.append('; No change to metaline')
   nochange = nochange + 1
  else:
   outarr.append('%s old %s' %(lnum,c.metaline))
   # outarr.append(';')
   outarr.append('%s new %s' %(lnum,c.metaline_new))
  outarr.append('; ----------------------------------------------')
  outrecs.append(outarr)
 write_recs(fileout,outrecs,blankflag=False)
 print(nochange,"cases No change to metaline")

if __name__=="__main__":
 option = sys.argv[1]
 filein1 = sys.argv[2]  # pw.txt
 filein2 = sys.argv[3]  # previous bbmulti_NN.txt
 fileout1 = sys.argv[4] # temp_change_3_4_NN.txt
 fileout2 = sys.argv[5] # bbmulti_NN.txt
 
 lines1 = read_lines(filein1)
 lines2 = read_lines(filein2)
 recs2 = init_recs(lines2)
 changeFname = 'make_changes_%s' %option
 changeF = locals()[changeFname]
 changes,skips = changeF(lines1,recs2)
 write_lines(fileout2,skips)
 print(len(changes),'changes')
 write_changes(fileout1,changes,option)
 exit(1)
