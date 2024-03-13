# coding=utf-8
""" ls_expand_make_change.py
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
 def __init__(self,metaline,lnum,old,new,linechanges):
  self.metaline = metaline
  self.lnum = lnum
  self.old = old
  self.new = new
  self.linechanges = linechanges
  
class LS_rec:
 def __init__(self,line):
  parts = line.split('\t')
  self.cat,self.instance,self.count = parts[0:3]
  if len(parts) == 3:
   self.expand = None
  elif len(parts) == 4:
   self.expand = parts[3]
  else:
   print('LS_rec error.\n%s' % line)
   exit(1)
  self.status = None  # will be revised by check_instances
  
def get_instances(lines,lscode):
 a = []  # list of instances returned
 for line in lines:
  instance = LS_rec(line)
  a.append(instance)
 return a
  
def get_standard_regexes(lscode):
 regexes = [
  r'<ls>%s ([0-9]+,[0-9]+)</ls>' % lscode,
  r'<ls>%s ([0-9]+,[0-9]+)\. fgg?\.</ls>' % lscode,
  
  r'<ls n="%s">([0-9]+,[0-9]+)</ls>' % lscode,
  r'<ls n="%s">([0-9]+,[0-9]+)\. fgg?\.</ls>' % lscode,
  
  r'<ls n="%s [0-9]+,">([0-9]+)</ls>' % lscode,
  r'<ls n="%s [0-9]+,">([0-9]+)\. fgg?\.</ls>' % lscode,
  ]
 return regexes

def check_instance_string(s,regexes):
 for iregex,regex in enumerate(regexes):
  try:
   m =  re.search(regex,s)
  except:
   print('check_instance_string ERROR. regex=\n%s' % regex)
   exit(1)
  if m != None:
    return iregex
 # instance does not match a standard form
 return None 

def check_instance_strings(a,lscode):
 # a is array of strings
 regexes = get_standard_regexes(lscode)
 n = 0 # count of problems
 for x in a:
  status = check_instance_string(x,regexes)
  if status == None:
   print('check fails:',x)
   n = n + 1
 print('check_instance_strings finds %s non-standard strings' % n)

def check(instances,lscode):
 a = [] # array of strings to check
 for x in instances:
  if x.expand == None:
   a.append(x.instance)
   continue
  b = re.findall(r'<ls.*?</ls>',x.expand)
  for y in b:
   a.append(y)
 print('check: len(a) = %s' % len(a))
 check_instance_strings(a,lscode)
 
def make_changes(lines,instances):
 changes = []
 d = {}
 for x in instances:
  if x.expand == None:
   continue
  old = x.instance
  new = x.expand
  if old in d:
   print('make_changes Error duplicate',old)
  d[old] = x
 # ------
 meta = None
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   meta = line
   continue
  newline = line
  oldnews = []
  for m in re.finditer(r'<ls.*?</ls>',line):
   oldls = m.group(0)
   if oldls not in d:
    continue
   instance = d[oldls]
   newls = instance.expand
   assert newls != None
   newline = newline.replace(oldls,newls)
   oldnews.append((oldls,newls))
  if newline == line:
   continue
  # generate change of line
  lnum = iline + 1
  change = Change(meta,lnum,line,newline,oldnews)
  changes.append(change)
 return changes

def get_outarr(c):
 outarr = []
 outarr.append('; %s : %s changes' % (c.metaline,len(c.linechanges)))
 for i,a in enumerate(c.linechanges):
  old,new = a
  outarr.append('; %d: old: %s' % (i+1,old))
  outarr.append(';    new: %s' % new)
  #outarr.append('; %s: %s -> %s' %(i+1,old,new))
 outarr.append('%s old %s' %(c.lnum,c.old))
 outarr.append(';')
 outarr.append('%s new %s' %(c.lnum,c.new))
 outarr.append('; ----------------------------------------------')
 return outarr

def write_changes(fileout,changes):
 outrecs = []
 outarr = [] # header
 outarr.append('; ******************************************************')
 outarr.append('; %s lines changed' % len(changes))
 outarr.append('; ******************************************************')
 outrecs.append(outarr)
 
 for c in changes:
  outarr = get_outarr(c)
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

if __name__=="__main__":
 lscode = sys.argv[1]
 filein = sys.argv[2]  # ls_expand
 filein1 = sys.argv[3] # a version of pw.txt
 fileout = sys.argv[4]  # change file
 lines = read_lines(filein)
 
 instances = get_instances(lines,lscode)
 lines1 = read_lines(filein1)
 changes = make_changes(lines1,instances)
 print(len(changes),'lines changed')
 write_changes(fileout,changes)
 check(instances,lscode)
 
 
 
