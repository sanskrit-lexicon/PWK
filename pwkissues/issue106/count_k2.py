# coding=utf-8
""" count_k2.py
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 print(len(lines),"from",filein)
 return lines

def count(lines):
 c = {}
 c['main_L'] = 0
 c['vn_L'] = 0
 c['main_k2'] = 0
 c['vn_k2'] = 0
 for i,line in enumerate(lines):
  if not line.startswith('<L>'):
   continue
  m = re.search(r'<L>(.*?)<pc>.*?<k2>(.*)$',line)
  Lstr = m.group(1)
  k2 = m.group(2)
  Lnum = float(Lstr)
  commas = re.findall(',',k2)
  ncommas = len(commas)
  if ncommas == 0:
   # no alternates
   continue
  if Lnum < 200000.0:
   c['main_L'] = c['main_L'] + 1
   c['main_k2'] = c['main_k2'] + ncommas
  else:
   c['vn_L'] = c['vn_L'] + 1
   c['vn_k2'] = c['vn_k2'] + ncommas
 for key in c:
  print(key,c[key])

def countbbroots(lines):
 n1 = 0
 n2 = 0
 for i,line in enumerate(lines):
  if not line.startswith('<L>'):
   continue
  bbline = lines[i+1]
  if '√' not in bbline:
   continue
  before,after = bbline.split('¦')
  ndeva = len(re.findall(r'{#',before))
  if ndeva < 2:
   continue
  n1 = n1 + 1
  n2 = n2 + ndeva
 print('n1=',n1,'n2=',n2)
 
if __name__=="__main__":
 filein = sys.argv[1]  # pw.txt
 lines = read_lines(filein)
 count(lines)
 countbbroots(lines)
 
 

