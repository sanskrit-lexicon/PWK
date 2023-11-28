# coding=utf-8
""" corrections_count.py
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines
 

class Input:
 def __init__(self,old,new,inputcount):
  self.old = old
  self.new = new
  self.inputcount = inputcount
  
def init_correction_input(filein):
 mandups = {
  "Title" : 5,
  "freudlich": 5,
  "freudliche": 3,
  "nacht": 2,
  "paederia": 2,
  "ven": 2,
  }
 lines = read_lines(filein)
 d = {}
 recs = []
 for iline,line in enumerate(lines):
  (old,new) = line.split('->')
  old = old.strip()
  new = new.strip()
  if old not in d:
   rec = Input(old,new,0)
   d[old] = rec
   recs.append(rec)
  rec = d[old]
  if old in mandups:
   inputcount = mandups[old]
   rec.inputcount = inputcount
  else:
   rec.inputcount = rec.inputcount + 1
 print("init_correction_input:",len(lines),"read from",filein)
 duprecs = [rec for rec in recs if rec.inputcount > 1]
 print(len(duprecs),"duplicate inputs found")
 return recs

def write_recs(fileout,recs):
 with codecs.open(fileout,"w","utf-8") as f:
  for rec in recs:
   out = '%s %s -> %s' %(rec.inputcount,rec.old,rec.new) 
   f.write(out+'\n')  
 print(len(recs),"records written to",fileout)
 
if __name__=="__main__":
 filein = sys.argv[1] # correction input
 fileout = sys.argv[2] # correction input with counts
 recs = init_correction_input(filein)
 write_recs(fileout,recs)
 
