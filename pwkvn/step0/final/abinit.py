#-*- coding:utf-8 -*-
"""abinit.py
 
"""
from __future__ import print_function
import sys,re,codecs

class AB:
 def __init__(self,line):
  self.ab,self.abdata = line.split('\t')
  
def init_abdata(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = [AB(x.rstrip('\r\n')) for x in f if not x.startswith(';')]
  print(len(recs),"abbreviations read from",filein)
 return recs

def unused_abinit1(line,abdata):
 if line.strip() == '':
  return line
 if line.startswith(('<L>','<LEND>','<H>')):
  return line
 for rec in abdata:
  line = re.sub(rec.regex,rec.replace,line)
 return line

def abinit1(line,abdata):
 if line.strip() == '':
  return line
 if line.startswith(('<L>','<LEND>','<H>')):
  return line
 for rec in abdata:
  parts = re.split('(<ab>.*?</ab>)|(<ls>.*?</ls>)',line)
  newparts = []
  for part in parts:
   if part == None:
    continue
   if part.startswith(('<ab>','<ls>')):
    newpart = part
   else:
    newpart = re.sub(rec.regex,rec.replace,part)
   newparts.append(newpart)
  line = ''.join(newparts)
 return line

def abdata_prepare(abdata):
 abdata1 = sorted(abdata,key = lambda x: len(x.ab),reverse=True)
 # add changes attribute
 for rec in abdata1:
  ab = rec.ab
  ab1 = ab.replace('.','[.]')
  regexraw = r'([ (*]|<lb/>)(%s)([ ,)])' % ab1
  rec.regex = re.compile(regexraw)
  rec.replace = r'\1<ab>\2</ab>\3'
 return abdata1

def abinit(lines,abdata):
 newlines = []
 abdata1 = abdata_prepare(abdata)
 nchg = 0
 for iline,line in enumerate(lines):
  newline = abinit1(line,abdata1)
  if newline != line:
   nchg = nchg + 1
  newlines.append(newline)
 print(nchg,'lines changed')
 return newlines

def write(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for iline,line in enumerate(lines):
   f.write(line+'\n')
 print(len(lines),"records written to",fileout)

if __name__=="__main__":
 filein = sys.argv[1] # pwkvn
 filein1 = sys.argv[2] # pwkvnab_input.txt
 fileout = sys.argv[3] # pwkvn
 
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
  print(len(lines),"lines read from",filein)

 abdata = init_abdata(filein1)

 newlines = abinit(lines,abdata)
 
 write(fileout,newlines)

 
