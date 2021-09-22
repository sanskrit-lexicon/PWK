#-*- coding:utf-8 -*-
"""compare_roman1.py
"""
from __future__ import print_function
import sys, re,codecs

def adjust(line):
 # lower-case all {%X%}
 def f(m):
  x = m.group(0)
  y = x.lower()
  return y
 lineadj = re.sub(r'{%[^%]+%}',f,line)
 return lineadj

if __name__=="__main__":
 filein = sys.argv[1] #  temp_extract1.txt
 filein1 = sys.argv[2] # temp_extract2_slp1_roman1.txt
 fileout = sys.argv[3] # problems listed
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 with codecs.open(filein1,"r","utf-8") as f:
  lines1 = [x.rstrip('\r\n') for x in f]
 assert len(lines) == len(lines1)
 nprob = 0

 outrecs = []
 for iline,line in enumerate(lines):
  line1 = lines1[iline]
  linea = adjust(line)
  if linea != line1:
   nprob = nprob + 1
   outarr = [line,line1,linea,' ']
   outrecs.append(outarr)
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(nprob,"unexplained differences written to",fileout)
 
