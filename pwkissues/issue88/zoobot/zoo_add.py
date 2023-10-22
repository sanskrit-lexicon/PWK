#-*- coding:utf-8 -*-
"""zoo_add.py Additional zoo tags
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

class Zoo:
 def __init__(self,line):
  m = re.search(r'^(.*?) \(([0-9]+)\)$',line)
  if m == None:
   self.status = False
   return
  self.status = True
  self.name = m.group(1)
  self.newcount = int(m.group(2))
  self.count = 0  # number changed
  name = self.name
  self.replacements = [
    ('{%' + name + '%}' , '{%<zoo>' + name + '</zoo>%}') ,
    (' ' + name   , ' <zoo>' + name + '</zoo>'),
    ('<bot>' + name + '</bot>', '<zoo>' + name + '</zoo>'),
  ]
  if False: # dbg
   for x in self.replacements:
    print(x)
    
def init_zoo_recs():
 zoo_tag_data = """
Acheriris Kokor Zibha (1)
Antilope cervicapra (1)
Ardea Argala (1)
Ardea nivea (20)
Ardea sibirica (27)
Coluber Naga (8)
Lacerta Godica (1)
Noctua indica (1)
Tantalus flacinellus (1)
Unguis odoratus (1)
"""
 lines = zoo_tag_data.splitlines()
 recs = []
 for line in lines:
  rec = Zoo(line)
  if rec.status:
   recs.append(rec)
 nrecs = len(recs)
 assert nrecs == 10
 return recs

zoo_recs = init_zoo_recs()

def check_zoo_recs():
 for rec in zoo_recs:
  print(rec.name, rec.newcount, rec.count)
  
def adjust_helper(line):
 newline = line
 parts = re.split('({%.*?%})',line)  # assume in italics
 newparts = []
 for part in parts:
  if part.startswith('{%'):
   newpart = part
   for rec in zoo_recs:
    replacements = rec.replacements
    for old,new in replacements:
     newpart1 = newpart.replace(old,new)
     if newpart1 != newpart:
      rec.count = rec.count + 1
     newpart = newpart1
  else:
   newpart = part
  newparts.append(newpart)
 newline = ''.join(newparts)
 return newline
  
def adjust(lines):
 newlines = []  # returned
 metaline = None
 nchg = 0
 for iline,line in enumerate(lines):
  if iline == 0: 
   newline = line
  elif line == '':
   newline = line
  elif line.startswith('<L>'):
   metaline = line
   newline = line
  elif line == '<LEND>':
   metaline = None
   newline = line
  elif metaline == None:
   newline = line # not in an entry
  else: # one of the 'datalines' of entry
   newline = adjust_helper(line)
  newlines.append(newline)
  if newline != line:
   nchg = nchg + 1
 print(nchg,"lines changed")
 return newlines

def write(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for line in lines:
   f.write(line + '\n')
 print(len(lines),"written to",fileout)
 
if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] # revised xxx.txt
 lines = read_lines(filein)
 newlines = adjust(lines)

 write(fileout,newlines)
 check_zoo_recs()
 
