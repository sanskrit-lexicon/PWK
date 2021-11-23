#-*- coding:utf-8 -*-
"""L_iline_diff.py
"""
from __future__ import print_function
import sys, re,codecs

if __name__=="__main__":
 filein1 = sys.argv[1]
 filein2 = sys.argv[2]
 with codecs.open(filein1,encoding='utf-8',mode='r') as f:
  lines1 = [line.rstrip('\r\n') for line in f]
 with codecs.open(filein2,encoding='utf-8',mode='r') as f:
  lines2 = [line.rstrip('\r\n') for line in f]
 for iline,line1 in enumerate(lines1):
  if line1.startswith('<L>'):
   line2 = lines2[iline]
   if line1 != line2:
    print('first metaline diff at iline=',iline+1)
    exit(1)
 print('metalines and their line numbers agree')
 
