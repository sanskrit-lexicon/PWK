# coding=utf-8
""" word_change_page.py
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

class Linkrec:
 def __init__(self,metaline,L,pc,k1,href):
  self.metaline = metaline
  self.L = L
  self.pc = pc
  self.k1 = k1
  self.href = href
  
def init_words_page(filein):
 lines = read_lines(filein)
 href0 = 'https://www.sanskrit-lexicon.uni-koeln.de/scans/csl-apidev/servepdf.php?dict=pw&page='
 d = {}
 linkrec = None
 for line in lines:
  if line.strip() == '':
   continue
  m = re.search(r'<L>(.*?)<pc>(.*?)<k1>(.*?)<k2>',line)
  if m != None:
   metaline = line
   L = m.group(1)
   pc = m.group(2)
   k1 = m.group(3)
   href = href0 + pc
   linkrec = Linkrec(metaline,L,pc,k1,href)
   continue
  m = re.search(r'^([0-9]+): (.*)$',line)
  if m != None:
   lnum = m.group(1)
   text = m.group(2) # space separated list of words
   words = text.split()
   for word in words:
    if word not in d:
     d[word] = []
    d[word].append(linkrec)
 return d
if __name__=="__main__":
 filein = sys.argv[1] # word_freq.txt words_change.txt
 filein1 = sys.argv[2] # words.txt
 fileout = sys.argv[3] # frequency count of words, with DE
 recs = init_freq(filein)
 word_links_d = init_words_page(filein1)
 wordkeys = word_links_d.keys()
 print(len(wordkeys),"wordkeys")
 exit(1)
 update_recs(recs,words_page)
 write_freq_recs(fileout,recs)

