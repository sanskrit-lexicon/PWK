#-*- coding:utf-8 -*-
"""addnum.py
 
"""
import sys,re,codecs

def addnum(lines):
 recs = []
 n0 = 172000
 for iline,line in enumerate(lines):
  num = n0 + iline + 1
  ident = '%07d' %num
  newline = re.sub('<p pc=','<p n="%s" pc=' %ident,line)
  recs.append(newline)
 return recs

def write(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for line in lines:
   f.write(line+'\n')
 print(len(lines),"records written to",fileout)

if __name__=="__main__":
 filein = sys.argv[1] #  pwkvn
 fileout = sys.argv[2] # 
 
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
  print(len(lines),"lines read from",filein)
 newlines = addnum(lines)
 write(fileout,newlines)
 
 
 
