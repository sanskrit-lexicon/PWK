#-*- coding:utf-8 -*-
"""first_L_diff.py
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

def get_L_nums(lines):
 ans = []
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   metaline = line
   lnum = iline + 1
   # meta = re.sub(r'<k2>.*$','',metaline)
   rec = (lnum,metaline)
   ans.append(rec)
 return ans

def first_diff(recs1,recs2):
 # assume same number of records (entries)
 assert len(recs1) == len(recs2)
 for i,rec1 in enumerate(recs1):
  rec2 = recs2[i]
  if rec1 != rec2:
   print(' %s != %s' %(rec1,rec2))
   exit(1)
   
if __name__=="__main__":
 filein1 = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 filein2 = sys.argv[2] # 
 lines1 = read_lines(filein1)
 lines2 = read_lines(filein2)
 recs1 = get_L_nums(lines1)
 recs2 = get_L_nums(lines2)
 first_diff(recs1,recs2)
 if recs1 == recs2:
  print('All metalines are the same, and occur at the same line-number')
 
