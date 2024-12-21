#-*- coding:utf-8 -*-
"""bot_freq_withmw.py
"""
import sys,re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write(fileout,d,dmw):
 keys = sorted(d.keys(), key = lambda x: x.lower())
 outarr = []
 outarr.append(fileout)
 for ikey,key in enumerate(keys):
  count = d[key]
  if key in dmw:
   mwcount = dmw[key]
  else:
   mwcount = 0
  lnum = ikey + 1
  #m = re.search(r'<bot>(.*?)</bot>',key)
  bot0 = key
  out = '%04d %s %s MW %s -> %s' %(lnum,key,count,mwcount,bot0)
  outarr.append(out)
  
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out + '\n')
 print(len(keys),"written to",fileout)

def bot_tag_count(lines):
 d = {}
 n = 0 # total number of bot tags
 for line in lines:
  bots = re.findall(r'<bot>.*?</bot>',line)
  for bot in bots:
   n = n + 1
   if bot not in d:
    d[bot] = 0
   d[bot] = d[bot] + 1
 print(n,"bot tags")
 print(len(d.keys()),"distinct bot tags")
 return d

def init_mw_freq(filein):
 lines = read_lines(filein1)
 d = {}
 for line in lines:
  m = re.search(r'(<bot>.*?</bot>) (.*)$',line)
  key = m.group(1)
  count = m.group(2)
  d[key] = int(count)
 return d
  
if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 filein1 = sys.argv[2] # mw bot tags
 fileout = sys.argv[3] #  frequency
 lines = read_lines(filein)
 d = bot_tag_count(lines)
 dmw = init_mw_freq(filein1)
 write(fileout,d,dmw)
 
