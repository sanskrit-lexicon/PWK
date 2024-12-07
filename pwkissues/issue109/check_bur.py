# coding=utf-8
""" check_bur.py for bhagp_bur
"""
from __future__ import print_function
import sys, re,codecs
import json

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines_simple(fileout,outarr,printFlag=True):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    #if out == None:
    # out = '?'
    f.write(out+'\n')
 if printFlag:
  print(len(outarr),"lines written to",fileout)

class Pagerec(object):
 """
Format of Burnouf.BhP.index.txt
volume	page	sk.	adhy.	from v.	to v.				
I	1	(I)	1	1	2ab
""" 
 def __init__(self,line,iline):
  line = line.rstrip('\r\n')
  parts = line.split('\t')
  assert len(parts) == 6
  self.line = line
  self.iline = iline
  partsnum = []
  flagnum = True
  vol_raw = parts[0]  #I,II,III
  page_raw = parts[1] # internal to volume. digits
  kanda_raw = parts[2] # skandha (I,II,...,IX)
  sarga_raw = parts[3] # adhy
  verse1_raw = parts[4] 
  verse2_raw = parts[5]
  droman_int = {'I':1, 'II':2, 'III':3, 'IV':4,
                'V':5, 'VI':6, 'VII':7, 'VIII':8, 'IX':9}
  self.vol = droman_int[vol_raw]  # 1,2,3
  assert self.vol in (1,2,3)
  self.page = int(page_raw)
  kanda_raw_noparen = kanda_raw[1:-1]
  assert kanda_raw == '(' + kanda_raw_noparen + ')'
  self.kanda = droman_int[kanda_raw_noparen]  # 1,...,9
  self.sarga = int(sarga_raw)
  try:
   m = re.search(r'^([0-9]+)([abcd]*)$',verse1_raw)
   self.verse1 = int(m.group(1))
   self.verse1x = m.group(2)
  except:
   print('problem with verse1 (iline = %s):' % iline)
   print(line)
   print('verse1_raw="%s"' % (verse1_raw))
   exit(1)
  m = re.search(r'^([0-9]+)([abcd]*)$',verse2_raw)
  self.verse2 = int(m.group(1))
  self.verse2x = m.group(2)
  self.flagnum = True  # used?
  ###  vol 1, page1 : 1193.pdf
  #    vol 2, page1 : 2031.pdf
  #    vol 3, page1 : 3121.pdf
  dvolpage0 = {1:193-1, 2:31-1, 3:121-1} 
  page_offset = dvolpage0[self.vol]
  extpage = self.page + page_offset # int
  vpstr = '%s%03d' %(self.vol,extpage)
  self.vp = vpstr
 def todict(self):
  e = {
   'v':self.vol, 'page':int(self.page), 'k':int(self.kanda),
   's':int(self.sarga),
   'v1':int(self.verse1), 'v2':int(self.verse2),
   'x1':self.verse1x, 'x2':self.verse2x, 'vp':self.vp
  }
  return e
def init_pagerecs(filein):
 """ filein is a csv file, with tab-delimiter and with first line as fieldnames
 """
 recs = []
 with codecs.open(filein,"r","utf-8") as f:
  for iline,line in enumerate(f):
   if (iline == 0):
    assert line.startswith('volume') # skip column-title line
    continue
   pagerec = Pagerec(line,iline)
   if pagerec.flagnum:
    # skip some records
    recs.append(pagerec)
 print(len(recs),'Page records read from',filein)
 return recs

def init_check_dict(pagerecs):
 d = {}
 for rec in pagerecs:
  # key = "%s.%s" %(rec.kanda,rec.sarga)
  k = int(rec.kanda)
  s = int(rec.sarga)
  v1 = int(rec.verse1)
  v2 = int(rec.verse2)
  for v in range(v1,v2+1):
   key = (k,s,v)
   d[key] = rec
 return d

def init_kandadict(pagerecs):
 d = {}
 kold = None
 for rec in pagerecs:
  k = rec.kanda;
  s = rec.sarga
  key = "%s.%s" %(rec.kanda,rec.sarga)
  if k not in d:
   d[k] = {}
  if s not in d[k]:
   d[k][s] = []
  recobj = rec.todict()
  d[k][s].append(recobj)
 return d

def write_kanda(fileout,d):
 # d is a dictionary of kandas,
 # and each value is a dictionary
 # Generate a javascript file setting value of a global indexdata
 outarr = []
 outarr.append('indexdata = {')
 for k in d:
  # key has form k  (1 to 9)  
  outarr.append(' %s: {' % k)
  sd = d[k] # dictionary of sargas
  for s in sd:
   outarr.append('  %s: [' % s)
   pagerecs = sd[s]  # array of dictionaries
   for pagerec in pagerecs:
    # pagerec is a dict
    jsonstring = json.dumps(pagerec)
    outarr.append('    %s,' % jsonstring)
   outarr.append(' ], ') # end of pagerecs
  outarr.append(' },') # end of sarga dictionary
 outarr.append('};') # end of kanda dictionary
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out + '\n')
 print(len(outarr),'lines written to',fileout)

def write_kandasarga(fileout,d):
 # d is a dictionary, and each value is an array of dictionaries
 # Generate a javascript file setting value of a global indexdata
 outarr = []
 outarr.append('indexdata = {')
 for key in d:
  # key has form k.s  (kanda,sarga)
  arr = d[key] # an array
  outarr.append(' "%s": [' % key)
  for a in arr:
   # a is a dict
   jsonstring = json.dumps(a)
   outarr.append('  %s,' % jsonstring)
  outarr.append(' ], ') # end of array arr
 outarr.append('};') 
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out + '\n')
 print(len(outarr),'lines written to',fileout)

# ------------------------------------------
# code from link_expand.py
# ------------------------------------------
def check_standarda(ls,sregs):
 used = []
 for ireg,sreg in enumerate(sregs):
  m = re.search(sreg,ls)
  if m:
   used.append((m,ireg))
 flag = (len(used) == 1)
 if flag:
  m,ireg = used[0]
 else:
  m,ireg = None,-1
 return flag,m,ireg

def get_standard_regexes(X):
 d1 = "([0-9]+)"
 d2 = "([0-9]+)"
 d3 = "([0-9]+)"
 # r"X (ABC|DEF)?"  syntax for optional matches
 # optional . OR optional fg. OR optional fgg.
 Y = "(\.| fg\.| fgg\.|\. fg\.|\. fgg\.)?"
 regexraws = [
  r'<ls>%s</ls>' % X,
  r'<ls>%s %s,%s,%s%s</ls>' %(X,d1,d2,d3,Y),
  r'<ls n="%s">%s,%s,%s%s</ls>' %(X,d1,d2,d3,Y),
  r'<ls n="%s %s,">%s,%s%s</ls>' %(X,d1,d2,d3,Y),
  r'<ls n="%s %s,%s,">%s%s</ls>' %(X,d1,d2,d3,Y),
 ]
 regexes = list(map(re.compile,regexraws))
 return regexes,regexraws

class Inrec:
 def __init__(self,line):
  self.line = line
  parts = line.split('\t')
  self.parts = parts
  self.L = parts[0]
  self.k1 = parts[1]
  self.lnum = parts[2] # string,
  self.ilnum = int(self.lnum)
  self.ls = parts[3]
  ##
  self.m = None
  self.ireg = None
  ##
  self.status = 'TODO'
  self.indexchk = False
  #self.d1 = None
  #self.d2 = None
  #self.d3 = None
  
def init_inrecs(filein):
 lines = read_lines(filein)
 recs = []
 for line in lines:
  recs.append(Inrec(line))
 print(len(recs),"read from",filein)
 return recs

#def check_bur(d1,d2,d3,dcheck):
# pass

def process(filein,fileout,pagerecs):
 recs_all = init_inrecs(filein)
 sregs, sregraws = get_standard_regexes(X)
 dcheck = init_check_dict(pagerecs)
 n = 0
 for irec,rec in enumerate(recs_all):
  flag,m,ireg = check_standarda(rec.ls,sregs)
  if not flag:
   assert rec.status == 'TODO'
   continue
  # rec is standard
  rec.status = 'STANDARD'
  rec.m = m
  rec.ireg = ireg
  # When ireg = 0, 
  if ireg == 0:
   # there are no d1,d2,d3, so nothing to check
   continue 
  d1 = int(m.group(1))
  d2 = int(m.group(2))
  d3 = int(m.group(3))
  key = d1,d2,d3
  # Burnouf has only skandhas 1-9 (d1)
  if (d1 not in (1,2,3,4,5,6,7,8,9)):
   rec.status = 'BOMBAY'
   continue
  rec.indexchk = (key in dcheck)
  if rec.indexchk == False:
   n = n + 1
 print(n,"links incompatible with index")
 outarr = []
 for rec in recs_all:
  if rec.ireg == 0:
   continue
  if rec.status != 'STANDARD':
   continue
  if rec.indexchk == False:
   outarr.append(rec.line)
 write_lines_simple(fileout,outarr)
 
if __name__ == "__main__":
 filein = sys.argv[1] # prelim2 file
 filein1 = sys.argv[2]  # tab-delimited index file
 fileout = sys.argv[3]
 pagerecs = init_pagerecs(filein1)  # from index
 X = r'BHĀG\. P\.' # global variable
 process(filein,fileout,pagerecs)
 exit(1)
 #kandasargadict = init_kandasargadict(pagerecs)
 #write_kandasarga(fileout,kandasargadict)
 kandadict = init_kandadict(pagerecs)
 write_kanda(fileout,kandadict)
 
