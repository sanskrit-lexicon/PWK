# coding=utf-8
""" make_4a.py
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


def merge(oldlines,pwkvnlines):
 newlines = []
 for i,line in enumerate(oldlines):
  if i == 674019:
   break
  newlines.append(line)
 for pwkvnline in pwkvnlines:
  newlines.append(pwkvnline)
 return newlines

if __name__=="__main__":
 filein = sys.argv[1]  # pw.txt
 filein1 = sys.argv[2] # AB's pwkvn revision with '<div n="p">'
 fileout = sys.argv[3]  # 

 lines = read_lines(filein)
 lines1 = read_lines(filein1)
 newlines = merge(lines,lines1)
 write_lines(fileout,newlines)

 
