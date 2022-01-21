#-*- coding:utf-8 -*-
"""listls_abnormal.py
"""
from __future__ import print_function
import sys, re,codecs
from parseheadline import parseheadline

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
  self.lsarr = []
  
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


class LSinstance(object):
 def __init__(self,entry,ls,lstype=None):
  self.entry = entry
  self.ls = ls
  self.type = lstype  # type of 
  
def find_abnormals_spr(lspfx,entries):
 tmp = lspfx.replace('.','[.]')
 regex1 = r'<ls>%s.*?</ls>'%tmp
 regex2 = r'<ls n="%s">.*?</ls>' % tmp
 regex = '(%s)|(%s)' %(regex1,regex2)
 #regexnorm = re.compile(r'^<ls>%s ([0-9]+)[.]</ls>$'%tmp)
 # ending '.' optional
 regexnorm = re.compile(r'^<ls>%s ([0-9]+[.]?)( fg+[.])?</ls>$'%tmp)
 regex1a = r'<ls>%s ([0-9]+[.]?)</ls>'%tmp
 regex1b = r'<ls>%s ([0-9]+[.]?) fgg?[.]</ls>' % tmp
 regex2a = r'<ls n="%s">([0-9]+[.]?)</ls>' % tmp
 regex2b = r'<ls n="%s">([0-9]+[.]?) fgg?[.]</ls>' % tmp
 abnormals = []
 normals = []
 for entry in entries:
  text = '\n'.join(entry.datalines)
  lsarr = re.findall(regex1,text,flags=re.DOTALL)
  for ls in lsarr:
   if re.search(regex1a,ls):
    normal = LSinstance(entry,ls,'1a')
    normals.append(normal)
   elif re.search(regex1b,ls):
    normal = LSinstance(entry,ls,'1b')
    normals.append(normal)
   else:
    abnormal = LSinstance(entry,ls)
    abnormals.append(abnormal)
  lsarr = re.findall(regex2,text,flags=re.DOTALL)
  for ls in lsarr:
   if re.search(regex2a,ls):
    normal = LSinstance(entry,ls,'2a')
    normals.append(normal)
   elif re.search(regex2b,ls):
    normal = LSinstance(entry,ls,'2b')
    normals.append(normal)
   else:
    abnormal = LSinstance(entry,ls)
    abnormals.append(abnormal)
 return abnormals,normals

def normals_summary(normals):
 d = {} 
 for lsinstance in normals:
  t = lsinstance.type
  if t not in d:
   d[t] = 0
  d[t] = d[t] + 1
 types = sorted(d.keys())
 for t in types:
  print(d[t],"ls instances of type",t)
  
def write_abnormals(fileout,abnormals):
 with codecs.open(fileout,"w","utf-8") as f:
  for x in abnormals:
   entry = x.entry
   ls = x.ls
   L = entry.metad['L']
   k1 = entry.metad['k1']
   out = '%s %s %s' %(ls,k1,L)
   f.write(out+'\n')
 print(len(abnormals),'abnormal ls written to',fileout)
 #exit(1) 
if __name__=="__main__":
 lspfx = sys.argv[1]
 filein = sys.argv[2] #  xxx.txt (path to digitization of xxx)
 #filebib = sys.argv[2]  # pwbib_input.txt
 fileout = sys.argv[3] #
 entries = init_entries(filein)
 if lspfx == 'Spr.':
  abnormals,normals = find_abnormals_spr(lspfx,entries)
  write_abnormals(fileout,abnormals)
  normals_summary(normals)
  exit(1)
 print('Not implemented for lspfx = %s' %lspfx)
