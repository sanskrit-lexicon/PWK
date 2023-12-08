# coding=utf-8
""" itwords.py
"""
from __future__ import print_function
import sys, re,codecs
import digentry  

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

word_regex_raw = '[A-Za-z0-9äöüÄÖÜ]+'
word_regex = re.compile(word_regex_raw)

def exclude_words(words):
 ans = []
 for word in words:
  if len(word) == 1:
   continue
  if re.search(r'^[0-9]+$',word):
   continue
  ans.append(word)
 return ans

def get_words_line(line0):
 # return array of words
 # various filters
 line = line0
 #line = re.sub(r'{%.*?%}', ' ',line)
 line = re.sub(r'{#.*?#}', ' ',line)
 line = re.sub(r'<([^ ]*?)(.*?)>.*?</\1>',' ',line)
 line = re.sub(r'¦',' ',line)
 line = re.sub(r'<div.*?>',' ',line)
 line = line.strip()
 words0 = re.findall(word_regex,line)
 words = exclude_words(words0)
 dbg = False
 if dbg:
  print('line0: ',line0)
  print('line : "%s"' % line)
  print('words:',', '.join(words))
  print()
 return words

def get_itwords_line(line):
 italics = re.findall(r'{%.*?%}',line)
 itwords = []
 for italic in italics:
  text = italic[2:-2] # remove {% and %}
  words = get_words_line(text)
  for w in words:
   itwords.append(w)
 return itwords

def get_words(entries):
 # create entry.dataline_words array
 dbg = False
 for ientry,e in enumerate(entries):
  e.dataline_words = []
  for iline,line in enumerate(e.datalines):
   words_line = get_itwords_line(line)
   e.dataline_words.append(words_line)

 print("exit get_words")
 
def write_outrecs(fileout,outrecs):
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outrecs),"cases written to",fileout)

def write_words(fileout,entries):
 outrecs = []
 for ientry,entry in enumerate(entries):
  #if ientry > 100:
  # print('write_words exits')
  # break
  outarr = []
  outarr.append(entry.metaline)
  for iline,words_line in enumerate(entry.dataline_words):
   out = ' '.join(words_line)
   if out != '':
    lnum = entry.linenum1 + iline + 1
    outarr.append('%s: %s' % (lnum,out))
  if len(outarr) > 1:
   outarr.append('')
   outrecs.append(outarr)
 write_outrecs(fileout,outrecs)

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

def get_freq(entries):
 d = {}
 for ientry,entry in enumerate(entries):
  for iline,words_line in enumerate(entry.dataline_words):
   for w in words_line:
    if w not in d:
     d[w] = 0
    d[w] = d[w] + 1
 return d

def write_freq(fileout,entries):
 freqsd = get_freq(entries)
 uwords = freqsd.keys()  # unique words
 uwords1 = sorted(uwords, key = lambda w: w.lower())
 outarr = []
 for w in uwords1:
  count = freqsd[w]
  out = '%s %s' % (w,count)
  outarr.append(out)
 write_outarr(fileout,outarr)
 
if __name__=="__main__":
 filein = sys.argv[1] # xxx.txt cdsl
 fileout = sys.argv[2] # words in entries
 fileout1 = sys.argv[3] # frequency count of words
 entries = digentry.init(filein)
 get_words(entries) # entry.dataline_words
 write_words(fileout,entries)
 write_freq(fileout1,entries)

 
