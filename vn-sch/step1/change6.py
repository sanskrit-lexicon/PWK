#-*- coding:utf-8 -*-
"""change1a.py  Find places where the IAST of k2 disagrees with k1
 
"""
import sys,re,codecs
from parseheadline import parseheadline
import transcoder
transcoder.transcoder_set_dir('transcoder')
sys.stdout.reconfigure(encoding='utf-8') 
class Change(object):
 def __init__(self,metaline,page,iline,old,new,reason,iline1,line1,new1):
  self.metaline = metaline
  self.page = page
  self.iline = iline
  self.old = old
  self.new = new
  self.reason = reason
  self.iline1 = iline1
  self.line1 = line1
  self.new1 = new1

def change_out(change,ichange):
 outarr = []
 case = ichange + 1
 # change for iline
 lnum = change.iline + 1
 line = change.old
 new = change.new
 outarr.append('%s old %s' % (lnum,line))
 outarr.append('%s new %s' % (lnum,new))
 outarr.append(';')
 # change for iline1
 lnum = change.iline1 + 1
 line = change.line1
 new = change.new1
 outarr.append('%s old %s' % (lnum,line))
 outarr.append('%s new %s' % (lnum,new))
 outarr.append(';---------------------------------------------------------')
 
 return outarr

def write_changes(fileout,changes):
 with codecs.open(fileout,"w","utf-8") as f:
   for ichange,change in enumerate(changes):
    outarr = change_out(change,ichange)
    for out in outarr:
     f.write(out+'\n')
 print(len(changes),"possible changes written to",fileout)

def k2_to_k1(k2new):
 k1chk = k2new
 k1chk = k1chk.replace(r'\\','')
 k1chk = k1chk.replace('/','')
 k1chk = k1chk.replace('^','')
 k1chk = k1chk.replace('(','')
 k1chk = k1chk.replace(')','')
 k1chk = k1chk.replace('[','')
 k1chk = k1chk.replace(']','') 
 k1chk = k1chk.replace('°','')
 k1chk = k1chk.replace('-','')
 k1chk = k1chk.replace("'",'')
 return k1chk

def init_changes(lines):
 changes = [] # array of Change objects
 metaline = None
 nabbrev = 0  # number of abbreviations marked
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   metaline = line
   m = re.search(r'<L>(.*?)<k1>(.*?)<k2>([^<]+)$',metaline)
   L = m.group(1)
   k1 = m.group(2)
   k2 = m.group(3)
   ilinemeta = iline   
  if line.startswith('<LEND>'):
   metaline = None
   continue
  if line.startswith('[Page'):
   page = line
   continue
  if metaline == None:
   continue
  if metaline != line:
   # we are changing only
   continue
  k2lo = k2.lower()
  k2new = transcoder.transcoder_processString(k2lo,'roman1','slp1')
  k1chk = k2_to_k1(k2new)
  if k1chk == k1:
   continue
  # there is some problem with k1 or k2
  newline = line  # dummy new line
  # generate a Change instance
  # next line probably needs change also
  iline1 = iline + 1
  line1 = lines[iline1]
  newline1 = line1
  reason = None
  change = Change(metaline,page,iline,line,newline,reason,iline1,line1,newline1)  
  changes.append(change)
 return changes

if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] # change transactions
 
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 # lines = lines  # for later comparison
 changes = init_changes(lines)
 write_changes(fileout,changes)
