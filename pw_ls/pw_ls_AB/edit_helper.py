#-*- coding:utf-8 -*-
"""edit_helper.py
"""
from __future__ import print_function
import sys, re,codecs

class REC(object):
 def __init__(self,lines):
  self.lines = lines
  self.changed = False

def generate_recs(lines):
 iline = 0
 nlines = len(lines)
 while (iline < nlines):
  if not lines[iline].startswith('; ------------'):
   print('Problem at line',iline+1)
   print(lines[iline])
   exit(1)
  yield REC(lines[iline:iline+5])
  iline = iline + 5

  
def mark_changed(rec):
 old = rec.lines[2]
 new = rec.lines[4]
 new = new.replace('<ls>[','<ls>')
 new = new.replace(']</ls>','</ls>')
 old1 = re.sub(r'^([0-9]+) new ',r'\1 old ',new)
 if old1 != old:
  # replace rec.lines[4]
  rec.lines[4] = new
  # mark rec as changed
  rec.changed = True

def write_changed(fileout,recs):
 with codecs.open(fileout,encoding='utf-8',mode='w') as f:
  n = 0
  for rec in recs:
   if rec.changed:
    n = n + 1
    for out in rec.lines:
     f.write(out + '\n')
 print(n,"changed records written to",fileout)
 
def write_unchanged(fileout,recs):
 with codecs.open(fileout,encoding='utf-8',mode='w') as f:
  n = 0
  for rec in recs:
   if not rec.changed:
    n = n + 1
    for out in rec.lines:
     f.write(out + '\n')
 print(n,"unchanged records written to",fileout)
  
if __name__=="__main__":
 filein = sys.argv[1]
 fileout = sys.argv[2] # changed records
 fileout1 = sys.argv[3] # unchanged_records (can be same as filein)
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [line.rstrip('\r\n') for line in f]
 recs = list(generate_recs(lines))
 print(len(recs),"records from",filein)
 for rec in recs:
  mark_changed(rec)
 write_changed(fileout,recs)
 write_unchanged(fileout1,recs)
 # write
 
 
