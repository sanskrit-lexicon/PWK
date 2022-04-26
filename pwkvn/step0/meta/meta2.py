#-*- coding:utf-8 -*-
"""meta2.py
 
"""
import sys,re,codecs

def check(iline,line):
 if len(re.findall('{#',line)) != len(re.findall('#}',line)):
  print('check %s : %s' %(iline+1,line))

class Meta1:
 d = {}
 def __init__(self,line):
  line = line.rstrip('\r\n')
  m = re.search(r'^([0-9]+) ({#[^#]*#}) [º=]> (.*)$',line)
  self.n = m.group(1)
  self.hw = m.group(2) # headword or headword fragment
  rest = m.group(3)
  rest = re.sub(r'<prev>.*?</prev>','',rest)
  rest = rest.rstrip()
  self.adjhws = rest.split(',')  # one or more adjusted headwords
  self.nused = 0
  key = self.n + self.hw
  if key in self.d:
   print('Meta1 unexpected duplicate key',key)
  self.d[key] = self
  self.key = key

def init_meta1(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = [Meta1(x) for x in f]
 print(len(recs),'records read from',filein)
 return recs

class Rec:
 def __init__(self,rectype,L,pc,vol,hws,body):
  assert rectype in ['H','p']
  self.rectype = rectype
  self.L = L
  self.pc = pc
  self.hws = hws
  self.body = body
  self.vol = vol
  
def line_to_rec(line):
 # <p n="N" pc="P">X
 m = re.search(r'^<p n="(.*?)" pc="(.*?)">(.*)$',line)
 n = m.group(1)
 pc = m.group(2)
 body = m.group(3)
 hws = []
 for m in re.finditer(r'<hw>(.*?)</hw>',line):
  hw = m.group(1)
  hws.append(hw)
  assert ',' not in hw
 assert hws != []
 m = re.search(r'^([1-7])-([0-9]{3,3})-(1?[a-d])$',pc)
 if m == None:
  print('pc does not parse: "%s"' %pc)
  exit(1)
 vol = m.group(1)  # volume
 L = n # temporary
 rec = Rec('p',L,pc,vol,hws,body)
 return rec

def make_recs(lines):
 recs = []
 for iline,line in enumerate(lines):
  if line.startswith('<H>'):
   rec = Rec('H',None,None,None,None,line)
   recs.append(rec)
   continue
  if '<hw>' not in line:
   # one case
   print('skipping line',line)
   continue
  rec = line_to_rec(line)
  recs.append(rec)
 return recs

def rec_to_lines(rec):
 meta1d = Meta1.d
 outarr = []
 if rec.rectype == 'H':
  outarr.append(rec.body)
 else:
  outarr.append('<n>%s<pc>%s' %(rec.L,rec.pc))
  for ihw,hw in enumerate(rec.hws):
   key = rec.L + hw
   if key not in meta1d:
    outarr.append('hw:%s' %hw)
   else:
    meta1 = meta1d[key]
    meta1.nused = meta1.nused + 1
    for hw1 in meta1.adjhws:
     outarr.append('hw:%s' %hw1)
  outarr.append(rec.body)
  outarr.append('<LEND>')
 return outarr

def write(fileout,recs):
 with codecs.open(fileout,"w","utf-8") as f:
  for rec in recs:
   outarr = rec_to_lines(rec)
   for line in outarr:
    f.write(line+'\n')
   # add blank line
   f.write('\n')
 print(len(recs),"records written to",fileout)


def check_meta1_used(meta1s):
 unused = [x for x in meta1s if x.nused != 1]
 nprob = len(unused)
 print(nprob,"unused meta1 records")
 for x in unused:
  print("unused:",x.key)
if __name__=="__main__":
 filein = sys.argv[1] #  pwkvn
 filein1 = sys.argv[2] # meta1_edit
 fileout = sys.argv[3] # 
 
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
  print(len(lines),"lines read from",filein)

 meta1_recs = init_meta1(filein1)  # dictionary Meta1.d
 recs = make_recs(lines)
 write(fileout,recs)
 check_meta1_used(meta1_recs)
 
 
 
