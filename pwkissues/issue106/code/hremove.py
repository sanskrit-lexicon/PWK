# coding=utf-8
""" hremove.py
"""
from __future__ import print_function
import sys, re,codecs
#import digentry  

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for out in lines:
   f.write(out+'\n')  
 print(len(lines),"lines written to",fileout)

def write_recs(fileout,outrecs):
 # outrecs is array of array of lines
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
   out = ''  # blank line separates recs
   f.write(out+'\n')
 print(len(outrecs),"records written to",fileout)

def hremove(lines):
 newlines = []
 n = 0 # number of lines changes
 for iline,line in enumerate(lines):
  if not line.startswith('<L>'):
   # not a metaline.
   newlines.append(line)
   continue
  # metaline remove <h>N at end
  newline = re.sub(r'<k2>(.*?)<h>([0-9]+)$',r'<k2>\2. \1',line)
  if newline != line:
   n = n + 1
  newlines.append(newline)
 print(n,'lines changed')
 return newlines

if __name__=="__main__":
 filein = sys.argv[1]  # initial cdsl version pw.txt
 fileout = sys.argv[2]  # version of pw.txt with <e>N removed
 
 lines = read_lines(filein)
 print(len(lines),"lines read from",filein)

 newlines = hremove(lines)
 write_lines(fileout,newlines)
 
