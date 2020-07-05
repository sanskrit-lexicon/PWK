#-*- coding:utf-8 -*-
"""pw_verb_filter.py
 
 
"""
from __future__ import print_function
import sys, re,codecs
from parseheadline import parseheadline
#import transcoder
#transcoder.transcoder_set_dir('transcoder')

class Entry(object):
 Ldict = {}
 def __init__(self,lines,linenum1,linenum2):
  # linenum1,2 are int
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
  self.marked = False # from a filter of markup associated with verbs
  self.markcode = None
  self.markline = None

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

def mark_entries_verb(entries,exclusions,inclusions):
 """ pw verbs: <ls>DHĀTUP """
 #nonverbs = ['aDvayant','jmAyant','tvAyant','rayIyant']
 for entry in entries:
  # first exclude known non-verbs
  if entry.metaline in exclusions:
   exclusions[entry.metaline] = True  # so we know exclusion has been used
   continue 
  if entry.metaline in inclusions:
   entry.markcode = 'X'
   continue
  k1 = entry.metad['k1']
  L  = entry.metad['L']
  code = None
  linenum1 = entry.linenum1  # integer line number of metaline
  datalines = entry.datalines
  # patterns in additional lines
  patterns = [u'¦[ ,]*{#[^#]*t[ie]#}','<ab>[dD]enom[.]</ab>','Sautra',u'<div n="p">— Mit {#([a-zA-Z]+)#}']
  codes = [None,None,None,None,None]
  pattern_codes = ['3','N','S','U','ZZ']
  lex=False
  for iline,line in enumerate(datalines):
   if (iline < 2) and ('<lex>' in line):
    codes = [None,None,None,None,None]
    break
   if (iline == 0) and ('<ab>Adv.</ab>' in line):
    # example zaqguRI, which also has <div n="p">— Mit {#kar#}
    codes = [None,None,None,None,None]
    break
   if (iline == 0) and re.search(u'¦ *<ab>Partic[.]</ab>',line ):
    # example #virUQa#}¦ <ab>Partic.</ab> <ab>s.u.</ab>  ^1. {#ruh#}
    codes = [None,None,None,None,None]
    break
   for ipattern,pattern in enumerate(patterns):
    if re.search(pattern,line):
     codes[ipattern] = pattern_codes[ipattern]
   #if (iline == 0) and re.search(r'<lex>',line):
   # if L != '54387':  # 54387 ,BA is verb entry, but has <lex> in start
   #  lex=True
  codes_used = [c for c in codes if c != None]
  if len(codes_used) != 0:
   code = ''.join(codes_used)
  if (code != None) and lex:
   print('exclude lex',code,entry.metaline)
   code=None
  if code != None:
    entry.markcode = code
    #entry.markline = line
    #entry.marklinenum=entry.linenum1 + (iline+1)
    #break # for iline,line
 for x in exclusions:
  if not exclusions[x]:
   print('Unused exclusion:',x)

def write_verbs(fileout,entries):
 n = 0
 coded = {}
 with codecs.open(fileout,"w","utf-8") as f:
  for ientry,entry in enumerate(entries):
   code = entry.markcode
   if not code:
    continue
   if code not in coded:
    coded[code] = 0
   coded[code] = coded[code] + 1
   n = n + 1
   outarr = []
   k1 = entry.metad['k1']  
   L =  entry.metad['L']
   k2 = entry.metad['k2']
   outarr.append(';; Case %04d: L=%s, k1=%s, k2=%s, code=%s' %(n,L,k1,k2,code))
   #linenum = entry.marklinenum
   #line = entry.markline
   #outarr.append('%6s: %s'%(linenum,line))
   #outarr.append(';')
   for out in outarr:
    f.write(out+'\n')
 code_keys = sorted(coded.keys())
 for code in code_keys:
  print('%04d %s' %(coded[code],code))
 print('%04d' %n,"verbs written to",fileout)

def init_exclusions(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = [x.rstrip() for x in f if not x.startswith(';')]
 d = {}
 for rec in recs:
  d[rec] = False
 print(len(recs),"records read from",filein)
 return d

def init_inclusions(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = [x.rstrip() for x in f if not x.startswith(';')]
 d = {}
 for rec in recs:
  d[rec] = False
 print(len(recs),"records read from",filein)
 return d

if __name__=="__main__": 
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx
 filein1 = sys.argv[2] # pw_verb_exclude.txt
 filein2 = sys.argv[3] # pw_verb_include.txt
 fileout = sys.argv[4] # 
 entries = init_entries(filein)
 exclusions = init_exclusions(filein1)
 inclusions = init_inclusions(filein2)
 mark_entries_verb(entries,exclusions,inclusions)
 write_verbs(fileout,entries)
