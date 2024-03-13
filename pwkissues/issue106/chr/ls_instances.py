# coding=utf-8
""" ls_instances.py
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
 # kind: 'A' <ls>X</ls>
 # 'B' <ls n="A">B</ls>
 def __init__(self,instance,kind):
  self.instance = instance
  self.kind = kind
  self.count = 0  # updated later

def get_instances(lines,lscode):
 instances = []  # list of LS_rec objects. returned
 d = {}
 regex1raw = '<ls>%s[^<]*</ls>' % lscode
 regex2raw = '<ls n="%s[^"]*">[^<]*</ls>' % lscode
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
     instance = LS_rec(x,kind)
     instances.append(instance)
     d[x] = instance
    instance = d[x]
    instance.count = instance.count + 1 # update count of instances
    ntot = ntot + 1
 print(len(instances),"distinct instances")
 print(ntot,"total instances")
 return instances

def write_instances(fileout,instances,lscode):
 outarr = []
 #instances1 = sorted(instances,key = lambda x: x.instance)
 instances1 = sorted(instances,key = lambda x: len(x.instance))
 for instance in instances1:
  out = '%s\t%s' %(instance.instance,instance.count)
  outarr.append(out)
 write_lines(fileout,outarr)

if __name__=="__main__":
 lscode = sys.argv[1]
 filein = sys.argv[2]  # pw.txt
 fileout = sys.argv[3]  # instances of ls codes
 lines = read_lines(filein)
 instances = get_instances(lines,lscode)
 write_instances(fileout,instances,lscode)
 
 
