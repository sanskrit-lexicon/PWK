# coding=utf-8
""" add_althws.py
"""
from __future__ import print_function
import sys, re,codecs
#import digentry  

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def meta_iline(lines):
 d = {}
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   if line in d:
    print('meta error duplicate',line)
   d[line] = iline
 return d

def update(lines,dmeta,lines1):
 newlines = []
 for line in lines:  # old ab 
  newlines.append(line)
  if line.startswith('<L>'):
   meta = line
   if meta not in dmeta:
    print('update error',meta1)
    exit(1)
   iline1 = dmeta[meta]
   nextline1 = lines1[iline1+1]
   if nextline1.startswith('<althws>'):
    newlines.append(nextline1)
 return newlines

def write_lines(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for out in lines:
   f.write(out+'\n')  
 print(len(lines),"lines written to",fileout)

if __name__=="__main__":
 filein = sys.argv[1]  # initial ab version
 filein1 = sys.argv[2] # initial cdsl version (with <althws>X</althws>)
 fileout = sys.argv[3] # revised ab version with althws

 lines = read_lines(filein)
 lines1 = read_lines(filein1)

 dmeta = meta_iline(lines1)
 newlines = update(lines,dmeta,lines1)
 write_lines(fileout,newlines)
 
