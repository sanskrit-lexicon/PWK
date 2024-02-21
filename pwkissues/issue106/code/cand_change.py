# coding=utf-8
""" cand_change.py
"""
from __future__ import print_function
import sys, re,codecs
#import digentry  

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for out in lines:
   f.write(out+'\n')  
 print(len(lines),"lines written to",fileout)

def write_recs(fileout,outrecs,printflag=True,blankflag=True):
 # outrecs is array of array of lines
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
   if blankflag:
    out = ''  # blank line separates recs
    f.write(out+'\n')
 if printflag:
  print(len(outrecs),"records written to",fileout)

class CAND:
 def __init__(self,instance):
  metaline,nextline,nextlnum = instance
  self.metaline = metaline
  self.nextline = nextline
  self.nextlnum = nextlnum
  self.metaline1 = None
  self.nextline1 = None

def write_candidates(fileout,cands):
 outrecs = []
 for c in cands:
  outarr = []
  outarr.append('; ' + c.metaline)
  outarr.append('%s %s' %(c.nextlnum,c.nextline))
  outarr.append(' ')
  outrecs.append(outarr)
 write_recs(fileout,outrecs)

def init_cands(filein):
 lines = read_lines(filein)
 cands = []
 for iline,line in enumerate(lines):
  m = re.search(r'; (<L>.*)$',line)
  if m == None:
   continue
  metaline = m.group(1)
  iline1 = iline + 1
  temp = lines[iline1]
  m = re.search(r'^(.*?) (.*)$',temp)
  nextlnum = m.group(1)
  nextline = m.group(2)
  instance = (metaline,nextline,nextlnum)
  cand = CAND(instance)
  cands.append(cand)
 return cands

def change_01(cands):
 # modify cand objects
 for cand in cands:
  metaline = cand.metaline
  nextline = cand.nextline # bbline
  lnum     = cand.nextlnum # line number of bbline in temp_pw_X.txt
  before,after = nextline.split('¦')
  sanparts = re.findall(r'{#[^#]*#}',after)
  n = len(sanparts)
  if n != 1:
   continue # cannot handle this candidate
  sanpart = sanparts[0] # {#X#}
  sanword = sanpart[2:-2] # remove {# and #}
  if sanword not in ('°tA','°tva'):
   continue  # cannot handle this candidate
  # move the broken bar to be after this instance
  after1 = after.replace(sanpart,sanpart + '¦')
  nextline1 = before + '¦' + after1
  # add term to metaline k2
  # assume <k2> is the last field of metaline
  m = re.search(r'<k1>([^<]*?)<k2>([^<]*)$',metaline)
  if m == None:
   print('change_01 metaline ERROR:',metaline)
   exit(1)
  k1 = m.group(1)
  k2old = m.group(2)
  sfx = sanword[1:]  # tA or tva
  k2a = k1 + sfx
  k2new = '<k2>' + k2old + ', ' + k2a
  metaline1 = metaline.replace('<k2>%s' % k2old, '<k2>%s' % k2new)
  cand.metaline1 = metaline1
  cand.nextline1 = nextline1
 return

def change_02(cands):
 
 for cand in cands:
  metaline = cand.metaline
  nextline = cand.nextline # bbline
  lnum     = cand.nextlnum # line number of bbline in temp_pw_X.txt
  before,after = nextline.split('¦')
  sanparts = re.findall(r'{#[^#]*#}',after)
  n = len(sanparts)
  if n != 1:
   continue # cannot handle this candidate
  sanpart = sanparts[0] # {#X#}
  sanword = sanpart[2:-2] # remove {# and #}
  if sanword not in ('°tA','°tva'):
   continue  # cannot handle this candidate
  # move the broken bar to be after this instance
  after1 = after.replace(sanpart,sanpart + '¦')
  nextline1 = before + '¦' + after1
  # add term to metaline k2
  # assume <k2> is the last field of metaline
  m = re.search(r'<k1>([^<]*?)<k2>([^<]*)$',metaline)
  if m == None:
   print('change_01 metaline ERROR:',metaline)
   exit(1)
  k1 = m.group(1)
  k2old = m.group(2)
  sfx = sanword[1:]  # tA or tva
  k2a = k1 + sfx
  k2new = '<k2>' + k2old + ', ' + k2a
  metaline1 = metaline.replace('<k2>%s' % k2old, '<k2>%s' % k2new)
  cand.metaline1 = metaline1
  cand.nextline1 = nextline1
 return

def write_cands_todo(fileout,cands):
 cands_todo = [cand for cand in cands if cand.metaline1 == None]
 write_candidates(fileout,cands_todo)

def write_cands_change(fileout,cands):
 cands_change = [cand for cand in cands if cand.metaline1 != None]
 outrecs = []
 for c in cands_change:
  outarr = []
  outarr.append('; %s' % c.metaline)
  lnum = int(c.nextlnum)
  lnum_meta = lnum - 1
  # change for metaline
  outarr.append('%s old %s' %(lnum_meta,c.metaline))
  outarr.append('%s new %s' %(lnum_meta,c.metaline1))
  outarr.append('; --')
  # change for bbline (nextline)
  outarr.append('%s old %s' %(lnum,c.nextline))
  outarr.append(';')
  outarr.append('%s new %s' %(lnum,c.nextline1))
  outarr.append('; ----------------------------------------------')
  outrecs.append(outarr)
 write_recs(fileout,outrecs,blankflag=False)

if __name__=="__main__":
 option = sys.argv[1]
 filein = sys.argv[2]  # candidate file
 fileout1 = sys.argv[3]  # change file to temp_pw_2.txt for this option
 fileout2 = sys.argv[4]  # remaining candidates
 
 cands = init_cands(filein)
 print(len(cands),"candidates read from",filein)

 fname = 'change_%s' % option
 changeF = locals().get(fname)
 if changeF == None:
  print('function %s not found' % fname)
  exit(1)
 changeF(cands)
 write_cands_change(fileout1,cands)
 write_cands_todo(fileout2,cands)
