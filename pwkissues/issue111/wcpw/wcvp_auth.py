#-*- coding:utf-8 -*-
""" wcvp_auth.py
"""
from __future__ import print_function
import sys, re,codecs
import csv

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for line in lines:
   f.write(line+'\n')  
 print(len(lines),"written to",fileout)

class Freq:
 def __init__(self,line):
  self.line = line
  m = re.search(r'^<bot>(.*?)</bot> ([0-9]+)$',line)
  self.bot = m.group(1)
  self.count = int(m.group(2))
  self.used = False # modified in mark_freqs
  
def init_freqs(filein):
 lines = read_lines(filein)
 freqs = [Freq(line) for line in lines]
 print(len(freqs),"freqs read from",filein)
 d = {}
 for freq in freqs:
  if freq.bot in d:
   print('duplicate bot at',freq.line)
  d[freq.bot] = freq
 return freqs,d

def get_botname(line):
 line1 = re.sub(r'#.*$','',line)
 line1 = line1.replace('€','')
 line1 = line1.replace('_',' ')
 botname = line1.strip()
 return botname

class Bot:
 # file from Thomas
 def __init__(self,line):
  self.line = line
  self.count = 0   # modified in mark_freqs
  self.botname = get_botname(line)
  self.current,self.corrected = self.getcc()
  
 def get_newline(self):
  newline = '%s  <count>%s</count>' %(self.line,self.count)
  return newline

 def getcc(self):
  parts = self.line.split('\t')
  if len(parts) == 2:
   part1,part2 = parts
   part1 = re.sub(r' *# *','',part1)
   part2 = re.sub(r' *# *','',part2)
  else:
   part1 = None
   part2 = None
  return part1,part2
  
def init_botrecs(filein):
 lines = read_lines(filein)
 botrecs = []
 for iline,line in enumerate(lines):
  if iline in [0,1]:
   continue
  botrec = Bot(line)
  botrecs.append(botrec)
 print(len(botrecs),"botrecs read from",filein)
 a = [rec for rec in botrecs if (rec.current == rec.corrected) and
      (rec.current != None)]
 print(len(a),"botrecs have current == corrected")
 return botrecs

def update(botrecs,freqs,freqsd): 
 dbg = False
 for i,botrec in enumerate(botrecs):
  bot = get_bot(line)
  if bot in freqsd:
   freq = freqsd[bot]
   freq.used = freq.used + 1
   bot.found = True
   bot.count = freq.count
   continue
  # generate a new botrec
    
def write_tips(fileout,tips):
 outarr = []
 for tip in tips:
  a = []
  for tag in tip.tagcounts:
   n = tip.tagcounts[tag]
   a.append('%s,%s' %(tag,n))
  b = ' '.join(a)
  out = '%s\t%s <count>%s</count>' %(tip.ab,tip.tip,b)
  outarr.append(out)
 write_lines(fileout,outarr)

def sort_tips(tips):
 tips1 = []
 for tip in tips:
  if 'lang' in tip.tagcounts:
   tips1.append(tip)
 tips1a = sorted(tips1,key = lambda tip: tip.ab.lower())
 tips2 = []
 for tip in tips:
  if 'lang' not in tip.tagcounts:
   tips2.append(tip)
 tips2a = sorted(tips2,key = lambda tip: tip.ab.lower())
 return tips1a + tips2a

def notfound_botrecs_in_freqs(botrecs,freqsd):
 ans = [] # botrecs not found in freqs
 for botrec in botrecs:
  botname = botrec.botname
  if botname not in freqsd:
   ans.append(botrec)
 print(len(ans),"botrecs not found")
 return ans

def write_botrecsnf(fileout,botrecsnf):
 outarr = [botrec.line for botrec in botrecsnf]
 write_lines(fileout,outarr)
 print(len(outarr),"botrecs not found written to",fileout)

def mark_freqs(botrecs,freqsd):
 for botrec in botrecs:
  botname = botrec.botname
  if botname in freqsd:
   freq = freqsd[botname]
   botrec.count = freq.count
   freq.used = True

def write_botrecs(fileout,botrecs):
 outarr = []
 n0 = 0 # number with count = 0
 for botrec in botrecs:
  outarr.append(botrec.get_newline())
  if botrec.count == 0:
   n0 = n0 + 1
 print('%s botrecs have count = 0' %n0)
 write_lines(fileout,outarr)

def write_freqs_unused(fileout,freqs):
 outarr = []
 for freq in freqs:
  if not freq.used:
   outarr.append(freq.line)
 write_lines(fileout,outarr)

def test0(filein,fileout):
 with codecs.open(filein,encoding='utf-8',mode='r') as csvfile:
  # Create a reader object with a comma as the delimiter
  reader = csv.reader(csvfile, delimiter='|')
  # Iterate through each row in the CSV file
  n = 0
  for irow,row in enumerate(reader):
   # Process each row (e.g., print it) row is a list of column values
   if irow == 0:
    print(row)
    print('first row has',len(row),'columns')
    # count # of rows
   n = n + 1
 print(n,"rows read from",filein)
  
def test1(filein,fileout):
 # use a dictreader
 with codecs.open(filein,encoding='utf-8',mode='r') as csvfile:
  # Create a reader object with a comma as the delimiter
  reader = csv.DictReader(csvfile, delimiter='|')
  # Iterate through each row in the CSV file
  n = 0
  for irow,row in enumerate(reader):
   # Process each row
   # row is a dict
   if irow == 0:
    print(row) 
    print('first row has',len(row),'columns')
   # count # of rows
   n = n + 1
 print(n,"rows read from",filein)

def init_auth(filein,colnames):
 # use a dictreader
 #colnames = ['primary_author']
 #colnames = ['taxon_authors']
 d = {}
 with codecs.open(filein,encoding='utf-8',mode='r') as csvfile:
  # Create a reader object with a comma as the delimiter
  reader = csv.DictReader(csvfile, delimiter='|')
  # Iterate through each row in the CSV file
  n = 0
  for irow,row in enumerate(reader):
   # Process each row
   # row is a dict
   vals = [row[colname] for colname in colnames]
   valtup = tuple(vals)
   if valtup not in d:
    n = n + 1
    d[valtup] = 0
   d[valtup] = d[valtup] + 1
 print(n,"distinct values of %s" % colnames)
 return d

def write_auth(fileout,d):
 keys = list(d.keys())
 keys = sorted(keys)
 outarr = []
 for key in keys:  # key = valtup in init_auth
  count = d[key]
  outlist = list(key)  # tuple becomes list
  countstr = str(count)
  outlist.append(countstr)
  out = ','.join(outlist)  # ',' does not occur 
  outarr.append(out)
 write_lines(fileout,outarr) 
   
if __name__=="__main__":
 colname = sys.argv[1] 
 filein = sys.argv[2] #  wcvp_names.csv
 fileout = sys.argv[3] # wcvp_auth.txt  primary author
 colnames = [colname] 
 auth = init_auth(filein,colnames)
 write_auth(fileout,auth)
 
