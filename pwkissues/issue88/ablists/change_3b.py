#-*- coding:utf-8 -*-
"""change_3b.py
 
"""
from __future__ import print_function
import sys,re,codecs
import digentry  


def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def count_ab(lines):
 asdict = {}
 n = 0
 regexraw = r'<ab (.*?)>(.*?)</ab>'
 regex = re.compile(regexraw)
 for line in lines:
  n = n + 1
  tags = re.findall(regex,line)
  for c in tags:
   #print("count_ab:",c)
   #exit(1)
   # ('n="Noth"', 'N.')  
   if c not in asdict:
    asdict[c] = 0
   asdict[c] = asdict[c] + 1
 return asdict

#def get_local_abbrev_dict(lines):
# # key for d is like: ('n="Noth"', 'N.')
# d = count_ab(lines)
# return d

def make_changes_1(entries1,entries2):
 # returns list of changes for entries1
 regexraw = r'<ab (.*?)>(.*?)</ab>'
 regex = re.compile(regexraw)
 changes = []
 for ientry,e1 in enumerate(entries1):
  e2 = entries2[ientry]
  #  key for d2 is like: ('n="Noth"', 'N.')
  d2 = count_ab(e2.datalines)
  for iline1,line1 in enumerate(e1.datalines):
   line1_new = line1
   line1_olds = []
   line1_news = []
   for key in d2:
    count2 = d2[key]
    if count2 != 1:
     continue
    newchanges = [] # list of changes to this line for this key
    (attrib,abbrev) = key
    # look for ' <abbrev> '
    s1 = ' %s ' % abbrev
    regex1 = s1.replace('.','[.]')
    instances = re.findall(regex1,line1_new)
    if len(instances) != 1:
     line1_new = line1  # so no change will be generated
     continue
    metaline = e1.metaline
    lnum = e1.linenum1 + iline1 + 1
    ablocal = '**<ab %s>%s</ab>**' % key   # asterisks for checking
    line1_new = line1_new.replace(s1,' ' + ablocal + ' ')
    line1_olds.append(s1)
    line1_news.append(ablocal)
   if line1_new == line1:
    continue
   change = Change(metaline,lnum,line1,line1_new,line1_olds,line1_news)
   changes.append(change)
 return changes

class Change(object):
 def __init__(self,metaline,lnum,line,newline,old,new):
  self.metaline = metaline
  self.lnum = lnum
  self.line = line
  self.newline = newline
  self.old = old
  self.new = new

class Tip(object):
 def __init__(self,abbrevtuple):
  # abbrevtuple = # ('n="Noth"', 'N.')  
  attrib_string,abbrev_string = abbrevtuple
  m = re.search(r'^n="([^"]*)"$',attrib_string)
  if m == None:
   print('Tip: bad tuple',abbrevtuple)
   exit(1)
  self.tip = m.group(1)
  self.abbrev_string = abbrev_string
  self.abbrev = "%s=%s" % (self.abbrev_string,self.tip)
  self.usedcd = 0 # number of usages in cdsl pw
  self.usedab = 0 # number of usages in ab pw
  
def write_changes(fileout,changes):
 outrecs=[]
 for change in changes:
  outarr=[]
  metaline = change.metaline
  metaline = re.sub(r'<k2>.*$','',metaline)
  outarr.append('; %s' % metaline)
  # change info: old and new
  # change.old is an array
  for i,old in enumerate(change.old):
   new = change.new[i]
   outarr.append('; "%s"  --> "%s"' % (old,new))
  outarr.append('; --------------------')
  lnum = change.lnum
  line = change.line
  newline = change.newline
  outarr.append('%s old %s' %(lnum,line))
  outarr.append(';')
  outarr.append('%s new %s' %(lnum,newline))
  outarr.append('; ------------------------------------------------------')
  outrecs.append(outarr)
  
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
    for out in outarr:
     f.write(out+'\n')
 print(len(changes),"changes written to",fileout)

def unused_write(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for iline,line in enumerate(lines):
   f.write(line+'\n')
 print(len(lines),"records written to",fileout)

def init_noalts(filein):
 d = {}
 with codecs.open(filein,"r","utf-8") as f:
  recs = []
  for iline,line in enumerate(f):
   line = line.rstrip('\r\n')
   if line.startswith(';'):
    continue
   m = re.search(r'^<L>([0-9]+)',line)
   L = m.group(1)
   if L in d:
    print('duplicate L at line',iline+1)
    continue
   d[L] = True
   recs.append(L)
 print(len(recs),"L numbers read from",filein)
 return d

if __name__=="__main__":
 filein = sys.argv[1] # xxx.txt cdsl
 filein1 = sys.argv[2]  # xxx.txt AB
 fileout = sys.argv[3] # change.txt
 entries_cdsl = digentry.init(filein)
 # reset Ldict
 digentry.Entry.Ldict = {}
 entries_ab = digentry.init(filein1)
 #
 # lines1 = read_lines(filein1)
 # d1 = count_ab(lines1)
 # print(len(d1),"distinct <ab []>X</ab> from",filein1)
 changes = make_changes_1(entries_cdsl,entries_ab)
 write_changes(fileout,changes)
 exit(1)
 # tips = []
 # dtips = {}
 # extend tips,dtips for d1
 update_tips(tips,dtips,'ab',d1)
 exit(1)
 changes = make_changes(entries_cdsl,dtips)
 write_changes(fileout,changes)

 
