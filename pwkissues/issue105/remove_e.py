# coding=utf-8
""" remove_e.py
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

def write_lines(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for out in lines:
   f.write(out+'\n')  
 print(len(lines),"lines written to",fileout)

def remove_e(lines):
 newlines = []
 for line in lines:
  if not line.startswith('<L>'):
   # not a metaline.
   newlines.append(line)
   continue
  m = re.search(r'<e>(.*)$',line)
  if m == None:
   # some lines (those from pwkvn merger) have no <e>N
   newlines.append(line)
   continue
  code = m.group(1)  #
  # check only digits
  m1 = re.search(r'^[0-9][0-9][0-9]$',code)
  if m1 == None:
   print('Unexpected code %s\nmetaline=%s' %(code,line))
   exit(1)
  # remove <e>N
  old = '<e>' + code
  new = ''
  newline = line.replace(old,new)
  newlines.append(newline)

 return newlines


if __name__=="__main__":
 filein = sys.argv[1]  # initial cdsl version pw.txt
 fileout = sys.argv[2]  # version of pw.txt with <e>N removed

 lines = read_lines(filein)
 print(len(lines),"lines read from",filein)

 newlines = remove_e(lines)

 write_lines(fileout,newlines)
