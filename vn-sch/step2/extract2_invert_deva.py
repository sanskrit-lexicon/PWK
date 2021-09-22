#-*- coding:utf-8 -*-
"""extract2.py
"""
from __future__ import print_function
import sys, re,codecs
sys.path.append('../')
import transcoder
transcoder.transcoder_set_dir('../transcoder')

class EntrySch(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  m = re.search(r'^L=([0-9.]+) (.*)$',line)
  if not m:
   print('EntrySch problem:',line)
  self.L = m.group(1)
  self.text = m.group(2)
  
def init_entries_sch(filein):
 entries = []
 with codecs.open(filein,"r","utf-8") as f:
  for line in f:
   if line.strip() != '':
    entry = EntrySch(line)
    entries.append(entry)
 print(len(entries),"entries read from",filein)
 return entries

def out_transcode(line,tranout):
 def fdeva(m):
  tranin = 'deva1'
  x = m.group(1)
  y = transcoder.transcoder_processString(x,tranin,tranout)
  z = '{#%s#}' %y
  return z
 out1 = re.sub(r'{#(.*?)#}',fdeva,line)
 return out1

def write(fileout,entries,tranout):
 n = 0
 with codecs.open(fileout,"w","utf-8") as f:
  for entry in entries:
   n = n + 1
   L = entry.L
   text = entry.text
   out = out_transcode(text,tranout)
   outarr = []
   outarr.append('L=%s %s'%(L,out))
   outarr.append('')
   for out in outarr:
    f.write(out + '\n')
   if False:
    print('DEBUG. first record -- then exit')
    print('L=%s, text=%s' %(L,text))
    print('out=',outarr[0])
    print('tranout=',tranout)
    exit(1)
 print(n,"records written to",fileout)

if __name__=="__main__":
 # convert from Devanagari to slp1
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx
 fileout = sys.argv[2] # 
 entries = init_entries_sch(filein)
 tranout = 'slp1'
 write(fileout,entries,tranout)
