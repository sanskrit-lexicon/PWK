# coding=utf-8
""" ls_expand.py
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

class LS_rec:
 def __init__(self,line):
  parts = line.split('\t')
  self.cat,self.instance,self.count = parts[0:3]
  self.expansions = parts[3:]  # previous expansions, if any
  self.expand = None
  assert re.search(r'^[AXB][1-9]$',self.cat)

def get_instances(lines,lscode):
 a = []  # list of instances returned
 for line in lines:
  instance = LS_rec(line)
  a.append(instance)
 return a
  
def unused_get_instances1(lines,lscode):
 instances = []  # list of LS_rec objects. returned
 d = {}
 regex1raw = '<ls>%s([^<]*)</ls>' % lscode
 regex2raw = '<ls n="%s([^"]*)">([^<]*)</ls>' % lscode
 regex1 = re.compile(regex1raw)
 regex2 = re.compile(regex2raw)
 regexes = (regex1,regex2)
 kinds = ('A','B')
 ntot = 0
 for line in lines:
  for iregex,regex in enumerate(regexes):
   kind = kinds[iregex]
   for m in re.finditer(regex,line):
    x = m.group(0)
    if x not in d:
     if iregex == 0:
      instance = LS_rec(x,kind,m.group(1),None)
     else:
      instance = LS_rec(x,kind,m.group(1),m.group(2))      
     instances.append(instance)
     d[x] = instance
    instance = d[x]
    instance.count = instance.count + 1 # update count of instances
    ntot = ntot + 1
 print(len(instances),"distinct instances")
 print(ntot,"total instances")
 return instances

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

def check_instance(instance,lscode):
 regexes = get_standard_regexes(lscode)
 for iregex,regex in enumerate(regexes):
  try:
   m =  re.search(regex,instance.instance)
  except:
   print('check_instance ERROR. regex=\n%s' % regex)
   exit(1)
  if m != None:
    return iregex
 # instance does not match a standard form
 return None 


def expand_instance_1(instance,lscode,head,body,tail):
 assert head in ('<ls>%s ' % lscode, '<ls n="%s">' % lscode)
 parts = body.split('. ')
 expansions = []
 nparts = len(parts)
 prev1 = None
 status = True
 for ipart,part in enumerate(parts):
  # case 1
  m = re.search(r'^([0-9]+),([0-9]+)$',part)
  if m != None:
   prev1 = m.group(1)
   if ipart == 0:
    # expansion = '<ls>%s %s</ls>' % (lscode,part)
    expansion = '%s%s</ls>' % (head,part)
   else:
    expansion = '<ls n="%s">%s</ls>' % (lscode,part)
   expansions.append(expansion)
   continue
  # case 2
  m = re.search(r'^([0-9]+)$',part)
  if (m != None) and (prev1 != None):
   # note since prev1 != None, also ipart != 0
   expansion = '<ls n="%s %s,">%s</ls>' % (lscode,prev1,part)
   expansions.append(expansion)
   continue
  # case 3
  m = re.search(r'^fgg?\.$',part)
  if (m != None) and (ipart == (nparts - 1)) and (len(expansions) != 0):
   # add part to last expansion
   old = expansions.pop()
   new = re.sub('</ls>$', '. %s</ls>' % part,old)
   expansions.append(new)
   continue
  status = False
  break
 if status:  # len(parts) == len(expansions):
  # update instance object
  instance.expansions = expansions
  instance.expand = '. '.join(expansions)
  cat = instance.cat
  # assume cat is Xn. new cat is Bn
  if cat[0] != 'X':
   print('cat ERROR:',cat)
   print(instance.instance)
   print(instance.expand)
   exit(1)
  cat = 'B' + cat[1:]
  instance.cat = cat

def expand_instance_2(instance,lscode,head,body,tail):
 return

def expand_instance(instance,lscode):
 # two cases
 regex = r'^(<ls>%s )([^<]*)(</ls>)$' % lscode
 m = re.search(regex,instance.instance)
 if m != None:
  return expand_instance_1(instance,lscode,m.group(1),m.group(2),m.group(3))
 # 2nd case
 regex = r'^(<ls n="%s">)([^<]*)(</ls>)$' % lscode
 m = re.search(regex,instance.instance)
 if m != None:
  return expand_instance_1(instance,lscode,m.group(1),m.group(2),m.group(3))
 return None

def expand(instances,lscode):
 # modify instance objects
 dbgstr = 'never will match'
 for i,x in enumerate(instances):
  dbg = (x.instance == dbgstr)
  if dbg:print('expand.',dbgstr)
  #if i == 3565:print(i,x.instance)
  check = check_instance(x,lscode)
  if dbg:print('check=',check)
  if check != None:
   pass
  else:
   expand_instance(x,lscode)
  
def write_instances(fileout,instances,lscode):
 outarr = []
 for x in instances:
  if len(x.expansions) == 0:
   out = '%s\t%s\t%s' %(x.cat,x.instance,x.count)
  else:
   #a = [x.cat,x.instance,x.count] + x.expansions
   #out = '\t'.join(a)
   out = '%s\t%s\t%s\t%s' %(x.cat,x.instance,x.count,x.expand)
  outarr.append(out)
 write_lines(fileout,outarr)

def print_cat_counts(instances):
 ntot = 0
 d = {}
 all_cats = []
 for instance in instances:
  cat = instance.cat
  if cat not in d:
   d[cat] = 0
   all_cats.append(cat)
  d[cat] = d[cat] + 1

 for cat in all_cats:
  n = d[cat]
  print('%s %4d' %(cat,n))
  ntot = ntot + n
 assert ntot == len(instances)
if __name__=="__main__":
 lscode = sys.argv[1]
 filein = sys.argv[2]  # ls_instances1
 fileout = sys.argv[3]  # ls_expand
 lines = read_lines(filein)
 instances = get_instances(lines,lscode)
 expand(instances,lscode)
 write_instances(fileout,instances,lscode)
 print_cat_counts(instances)
 
 
