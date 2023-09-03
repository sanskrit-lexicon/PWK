# coding=utf-8
""" addlink.py
"""
from __future__ import print_function
import sys, re,codecs
import digentry  

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def adjust(filein):
 lines = read_lines(filein)
 print(len(lines),"read from",filein)
 newlines = []
 for line in lines:
  newlines.append(line)
  m = re.search(r'<L>(.*?)<pc>(.*?)<k1>',line)
  if m != None:
   page = m.group(2)
   newline = 'https://www.sanskrit-lexicon.uni-koeln.de/scans/csl-apidev/servepdf.php?dict=pw&page=%s' % page
   newlines.append(newline)
 return newlines

def marklines(lines,d):
 newlines = []
 for line in lines:
  m = re.search(r'<L>(.*?)<pc>',line)
  if m == None:
   newline = line
  else:
   L = m.group(1)
   if L in d:
    newline = '* ' + line
   else:
    newline = line
  newlines.append(newline)
 return newlines

def write(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"lines written to",fileout)

 
if __name__=="__main__":
 filein = sys.argv[1] # File with <L>
 fileout = sys.argv[2] #
 newlines = adjust(filein)
 write(fileout,newlines)
 

