#-*- coding:utf-8 -*-
"""bot_freq.py
"""
import sys,re,codecs
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec cannot encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write(fileout,d):
 keys = sorted(d.keys(), key = lambda x: x.lower())
 outarr = []
 for key in keys:
  count = d[key]
  out = '%s %s' %(key,count)
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

if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] # bot frequences
 lines = read_lines(filein)
 d = bot_tag_count(lines)

 write(fileout,d)
 #check_hom_recs()
 
