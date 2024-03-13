# coding=utf-8
""" ls_instances1.py
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

all_cats = ('A1','A2','A3','A4','X1','X2')
class LS_rec:
 # kind: 'A' <ls>X</ls>
 # 'B' <ls n="A">B</ls>
 def __init__(self,instance,kind,data1,data2):
  self.instance = instance
  self.kind = kind
  self.count = 0  # updated later
  self.data1 = data1
  self.data2 = data2
  #if instance == '<ls n="Chr. 163,">13</ls>':
  # print('%s :: %s :: %s :: %s' %(kind,instance,data1,data2))
  if self.data2 == None:
   assert kind == 'A'
   if re.search(r'^( [0-9]+,[0-9]+)$',data1):
    # <ls>Chr. a,b</ls>
    cat = 'A1'
   else:
    # <ls>Chr. ?</ls>
    cat = 'X1'
  else:
   if (data1 == '') and re.search(r'^([0-9]+,[0-9]+)$',data2):
    cat = 'A2'
   elif (data1 == '') and re.search(r'^([0-9]+,[0-9]+\. fgg?\.)$',data2):
    cat = 'A3'
   elif re.search(r'^ [0-9]+,$',data1) and re.search(r'^([0-9]+)$',data2):
    cat = 'A4'
   else:
    cat = 'X2'
  self.cat = cat
  assert cat in all_cats
def get_instances1(lines,lscode):
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

def write_instances1(fileout,instances,lscode):
 outarr = []
 #instances1 = sorted(instances,key = lambda x: x.instance)
 instances1 = sorted(instances,key = lambda x: x.cat + x.instance)
 for instance in instances1:
  out = '%s\t%s\t%s' %(instance.cat,instance.instance,instance.count)
  outarr.append(out)
 write_lines(fileout,outarr)

def print_cat_counts(instances):
 ntot = 0
 for cat in all_cats:
  arr = [x for x in instances if x.cat == cat]
  n = len(arr)
  print('%s %4d' %(cat,n))
  ntot = ntot + n
 assert ntot == len(instances)
if __name__=="__main__":
 lscode = sys.argv[1]
 filein = sys.argv[2]  # pw.txt
 fileout = sys.argv[3]  # instances of ls codes
 lines = read_lines(filein)
 instances1 = get_instances1(lines,lscode)
 write_instances1(fileout,instances1,lscode)
 print_cat_counts(instances1)
 
 
