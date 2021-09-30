#-*- coding:utf-8 -*-
"""pwk_transcode.py
"""

from __future__ import print_function
import sys, re,codecs
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
  #entry.marked = (stype == '')
  entry.marked = True   #  ALL entries are marked!
  if entry.marked:
   nmark = nmark + 1
 print(nmark,"all entries marked ")
 print(n3,"entries have 3 lines")

def entry_out(lines):
 nlines = len(lines)
 if nlines == 3:
  lines1 = [x for x in lines if not x.startswith('[Page')]
 else:
  lines1 = lines
 text = ' '.join(lines1)
 text = re.sub(r'{part=.*?}','',text)
 #if not re.search(r'^{#.*?#} ([0-9.]+ )?( [° * +])?{%.*?%}¦',text):
 #if not re.search(r'^([0-9.]+ )?( [° * +])?{%.*?%}¦',text):
 if not re.search(r'^([0-9.]+ )?( *[°*†]+)?{%.*?%}¦',text):
  print('WARNING',text)
 return text

def out_transcode(line,tranout):
 def fslp(m):
  tranin = 'hk'
  x = m.group(1)
  y = transcoder.transcoder_processString(x,tranin,tranout)
  z = '{#%s#}' %y
  return z

 def unused_fiast(m):
  tranin = 'roman1'
  x = m.group(1)
  # must low-case first
  x1 = x.lower()
  y1 = transcoder.transcoder_processString(x1,tranin,'slp1')
  y = transcoder.transcoder_processString(y1,'slp1',tranout)
  z = '{#%s#}' %y
  return z

 #tranin = 'roman1'
 out1 = re.sub(r'{#(.*?)#}',fslp,line)
 #out2 = re.sub(r'{%(.*?)%}',fiast,out1)
 return out1

def write(fileout,lines,tranout):
 n = 0
 with codecs.open(fileout,"w","utf-8") as f:
  for line in lines:
   n = n + 1
   out = out_transcode(line,tranout)
   outarr = []
   outarr.append('L=%s %s'%(n,out))
   #outarr.append('')
   for out in outarr:
    f.write(out + '\n')
 print(n,"records written to",fileout)

if __name__=="__main__":
 tranout = sys.argv[1]
 tranouts = ['slp1']
 if tranout not in tranouts:
  print('tranout must be one of %s' ','.join(tranouts))
  exit(1)
 filein = sys.argv[2] #  pwk with {#X#} ans X in HK 
 fileout = sys.argv[3] # 
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [line.rstrip('\r\n') for line in f if line.startswith('<p>')]

 write(fileout,lines,tranout)
