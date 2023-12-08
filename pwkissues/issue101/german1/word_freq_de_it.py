# coding=utf-8
""" word_freq_de_it.py
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
  de = rec.de
  itcount = rec.itcount
  w = rec.word
  count = rec.count
  out = '%s %s %s IT %s' % (w,count,de,itcount)
  outarr.append(out)
 write_outarr(fileout,outarr)

class Freq:
 def __init__(self,line):
  try:
   self.word,self.count,self.de = line.split()
  except:
   parts = line.split()
   print('ERROR: %s parts' % len(parts))
   print(parts)
   exit(1)
  self.itcount = 0  # count of this word in italics

def init_freq(filein):
 lines = read_lines(filein)
 recs = [Freq(line) for line in lines]
 return recs

class ItFreq:
 def __init__(self,line):
  try:
   self.word,self.count = line.split()
  except:
   parts = line.split()
   print('ItFreq error:',len(parts))
   print(parts)
   exit(1)

def init_itfreq(filein):
 lines = read_lines(filein)
 recs = [ItFreq(line) for line in lines]
 d = {}
 for rec in recs:
  d[rec.word] = rec.count
 return recs,d

def update_recs(recs,itdict):
 for rec in recs:
  if rec.word in itdict:
   rec.itcount = itdict[rec.word]
  else:
   rec.it = 0
   
if __name__=="__main__":
 filein = sys.argv[1] # word_freq_de.txt
 filein1 = sys.argv[2] # itwords_freq
 fileout = sys.argv[3] # frequency count of words, with DE and itfreq
 recs = init_freq(filein)  # freq_de
 itrecs,itdict = init_itfreq(filein1)
 update_recs(recs,itdict)
 write_freq_recs(fileout,recs)

