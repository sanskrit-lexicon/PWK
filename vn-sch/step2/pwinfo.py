#-*- coding:utf-8 -*-
"""pwinfo.py
"""
from __future__ import print_function
import sys, re,codecs
from parseheadline import parseheadline
sys.path.append('../')
import transcoder
transcoder.transcoder_set_dir('../transcoder')

class Entry(object):
 Ldict = {}
 def __init__(self,lines,linenum1,linenum2):
  self.metaline = lines[0]
  self.lend = lines[-1]  # the <LEND> line
  self.datalines = lines[1:-1]  # the non-meta lines
  # parse the meta line into a dictionary
  #self.meta = Hwmeta(self.metaline)
  self.metad = parseheadline(self.metaline)
  self.linenum1 = linenum1
  self.linenum2 = linenum2
  #L = self.meta.L
  L = self.metad['L']
  if L in self.Ldict:
   print("Entry init error: duplicate L",L,linenum1)
   exit(1)
  self.Ldict[L] = self
  #  extra attributes
  self.marked = False # True if type parameter is empty string
  
def init_entries(filein):
 # slurp lines
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [line.rstrip('\r\n') for line in f]
 recs=[]  # list of Entry objects
 inentry = False  
 idx1 = None
 idx2 = None
 for idx,line in enumerate(lines):
  if inentry:
   if line.startswith('<LEND>'):
    idx2 = idx
    entrylines = lines[idx1:idx2+1]
    linenum1 = idx1 + 1
    linenum2 = idx2 + 1
    entry = Entry(entrylines,linenum1,linenum2)
    recs.append(entry)
    # prepare for next entry
    idx1 = None
    idx2 = None
    inentry = False
   elif line.startswith('<L>'):  # error
    print('init_entries Error 1. Not expecting <L>')
    print("line # ",idx+1)
    print(line.encode('utf-8'))
    exit(1)
   else: 
    # keep looking for <LEND>
    continue
  else:
   # inentry = False. Looking for '<L>'
   if line.startswith('<L>'):
    idx1 = idx
    inentry = True
   elif line.startswith('<LEND>'): # error
    print('init_entries Error 2. Not expecting <LEND>')
    print("line # ",idx+1)
    print(line.encode('utf-8'))
    exit(1)
   else: 
    # keep looking for <L>
    continue
 # when all lines are read, we should have inentry = False
 if inentry:
  print('init_entries Error 3. Last entry not closed')
  print('Open entry starts at line',idx1+1)
  exit(1)

 print(len(lines),"lines read from",filein)
 print(len(recs),"entries found")
 return recs

def mark_entries(entries):
 nmark = 0
 n3 = 0
 for entry in entries:
  nlines = len(entry.datalines)
  if nlines != 1:  # the usual
   if nlines == 3: # 2nd most common -- due to page break
    n3 = n3 + 1
   else:
    print(entry.metaline,'has',nlines,'datalines')
   #exit(1)
  found = False  # find {part=...}
  for iline,line in enumerate(entry.datalines):
   m = re.search(r'{part=.*?}',line)
   if m != None:
    temp = m.group(0)
    found = True
    break
  assert found
  m = re.search(r'type=(.*?),',temp)
  assert m != None
  stype = m.group(1)
  entry.marked = (stype == '')
  if entry.marked:
   nmark = nmark + 1
 print(nmark,"entries marked with default type")
 print(n3,"entries have 3 lines")

def entry_out(lines,schhw):
 nlines = len(lines)
 if nlines == 3:
  lines1 = [x for x in lines if not x.startswith('[Page')]
 else:
  lines1 = lines
 text = ' '.join(lines1)
 text = re.sub(r'{part=.*?}','',text)
 #m = re.search(r'^{#(.*?)#} ([0-9.]+ )?( [° * +])?{%(.*?)%}¦',text)
 m = re.search(r'^([0-9.]+ )?( [° * +])?{%(.*?)%}¦',text)
 if not m:
  print('ERROR WARNING',text)
  exit(1)

 hom = ''
 thetype = ''
 if m.group(1) != None:
  hom = m.group(1).strip()
 if m.group(2) != None:
  thetype = m.group(2).strip()
 iasthw = m.group(3)
 return hom,thetype,iasthw

def out_transcode(line,tranout):
 def fslp(m):
  tranin = 'slp1'
  x = m.group(1)
  y = transcoder.transcoder_processString(x,tranin,tranout)
  z = '{#%s#}' %y
  return z

 def fiast(m):
  tranin = 'roman1'
  x = m.group(1)
  # must low-case first
  x1 = x.lower()
  y1 = transcoder.transcoder_processString(x1,tranin,'slp1')
  y = transcoder.transcoder_processString(y1,'slp1',tranout)
  z = '{#%s#}' %y
  return z

 tranin = 'roman1'
 out1 = re.sub(r'{#(.*?)#}',fslp,line)
 out2 = re.sub(r'{%(.*?)%}',fiast,out1)
 return out2

def vnestimate(c):
 vols = ['aAiIuUfFxXeEoO',
         'kKgGNcCjJYwWqQR',
         'tTdDn',
         'pPbB',
         'myrl',
         'vzS',
         'sh']
 for ivol,vol in enumerate(vols):
  if c in vol:
   return ivol+1  # 1-7
 print('vnestimate fails',c)
 exit(1)

def getpwmeta(k1,pwmeta):
 if k1 in pwmeta:
  pw = int(pwmeta[k1])  # volume
  vn = pw  # Estimate VN in same volume
 else:
  pw = 0  # not a pw headword
  vn = vnestimate(k1[0])  # estimate by first character
 return pw,vn

def write(fileout,entries,pwmeta):
 n = 0
 npw = 0  # number of headwords found in pw
 roman = {0:'_', 1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII'}
 with codecs.open(fileout,"w","utf-8") as f:
  for entry in entries:
   if not entry.marked:
    continue
   schhw = entry.metad['k1']
   hom,thetype,iasthw = entry_out([entry.datalines[0]],schhw)
   n = n + 1
   L = entry.metad['L']
   k1 = entry.metad['k1']
   assert k1 == schhw
   assert thetype == ''
   # convert iasthw to Devanagari
   tmp = transcoder.transcoder_processString(iasthw,'roman1','slp1')
   devahw = transcoder.transcoder_processString(tmp,'slp1','deva1')
   pw,vn = getpwmeta(k1,pwmeta)
   if pw != 0:
    npw = npw + 1
   outarr = []
   if hom != '':
    outarr.append(hom + ' ' + devahw)
   else:
    outarr.append(devahw)
   pwroman = roman[pw]
   outarr.append(pwroman)
   outarr.append('%s' %vn)
   field2 = ' '.join(outarr)
   out = '%s\t%s' %(L,field2)
   #out = 'L=%s, k1=%s, pw=%s, vn=%s' %(L,k1,pw,vn)
   f.write(out+'\n')
   
 print(n,"records written to",fileout)
 print(npw,"headwords found in pw")
 
def init_pwmeta(filein):
 # slurp lines
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [line.rstrip('\r\n') for line in f]
 d = {} # for k1, provide volume
 for idx,line in enumerate(lines):
  if not line.startswith('<L>'):
   continue
  m = re.search(r'<L>(.*?)<pc>(.*?)<k1>(.*?)<k2>',line)
  if m == None:
   print('init_pwmeta ERROR:',line)
   exit(1)
  L = m.group(1)
  pc = m.group(2)
  # pc = 7130-2, 1001-1, etc. First character is the volume
  vol = pc[0]  # 
  k1 = m.group(3)
  # there are duplicates, we skip -- only interested in volume
  if k1 not in d:
   d[k1] = vol
 return d
  
if __name__=="__main__":
 filein = sys.argv[1] #  sch.txt (path to digitization of Schmidt)
 filein1 = sys.argv[2] # pw.txt (path to digitization of PW)
 fileout = sys.argv[3] # 
 entries = init_entries(filein)
 pwmeta = init_pwmeta(filein1)
 mark_entries(entries)
 write(fileout,entries,pwmeta)
