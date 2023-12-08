# coding=utf-8
""" word_freq_de.py
"""
from __future__ import print_function
import sys, re,codecs
import digentry  

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_outrecs(fileout,outrecs):
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outrecs),"cases written to",fileout)

def write_outarr(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"cases written to",fileout)

def write_freq_recs(fileout,recs):
 outarr = []
 for rec in recs:
  if rec.de:
   flag = "+DE"
  else:
   flag = "-DE"
  w = rec.word
  count = rec.count
  out = '%s %s %s' % (w,count,flag)
  outarr.append(out)
 write_outarr(fileout,outarr)

def init_gwords(filein):
 """ put words into a Python set 
 """
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
  print(len(lines),"words read from",filein)
  s = set(lines)
  print(len(s),"set length is",len(s))
  return s

class Freq:
 def __init__(self,line):
  self.word,self.count = line.split()
  self.de = False  # assume not in german wordlist

def init_freq(filein):
 lines = read_lines(filein)
 recs = [Freq(line) for line in lines]
 return recs

def update_recs(recs,gwordset):
 for rec in recs:
  if rec.word in gwordset:
   rec.de = True
   
if __name__=="__main__":
 filein = sys.argv[1] # word_freq.txt
 filein1 = sys.argv[2] # german word list
 fileout = sys.argv[3] # frequency count of words, with DE
 recs = init_freq(filein)
 gwordset = init_gwords(filein1)
 update_recs(recs,gwordset)
 write_freq_recs(fileout,recs)

