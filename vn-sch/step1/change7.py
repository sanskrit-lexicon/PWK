#-*- coding:utf-8 -*-
"""change6.py  convert k2 to slp1 (metaline)
 
"""
import sys,re,codecs
from parseheadline import parseheadline
sys.path.append('../')
import transcoder
transcoder.transcoder_set_dir('../transcoder')

## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec cannot encode characters 
## when run in a git bash script.

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
 #outarr.append('; TODO Case %s: (reason = %s)' % (case,change.reason))
 try:
  ident = '%s' %(change.metaline,)
 except:
  print('ERROR:',change.iline,change.old)
  exit(1)
 if ident == None:
  ident = change.page
 outarr.append('; ' + ident)
 # change for iline
 lnum = change.iline + 1
 line = change.old
 new = change.new
 outarr.append('%s old %s' % (lnum,line))
 outarr.append('%s new %s' % (lnum,new))
 outarr.append(';')
 return outarr

def write_changes(fileout,changes):
 with codecs.open(fileout,"w","utf-8") as f:
   for ichange,change in enumerate(changes):
    outarr = change_out(change,ichange)
    for out in outarr:
     f.write(out+'\n')
 print(len(changes),"possible changes written to",fileout)

def init_changes(lines):
 changes = [] # array of Change objects
 metaline = None
 nabbrev = 0  # number of abbreviations marked
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   metaline = line
   m = re.search(r'<L>(.*?)<k1>(.*?)<',metaline)
   L = m.group(1)
   k1 = m.group(2)
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
   # we are changing onl
   continue
  def k2tran(m):
   x = m.group(1)
   x1 = x.lower()  
   y = transcoder.transcoder_processString(x1,'roman1','slp1')
   z = '<k2>' + y
   k1chk = y.replace(r'\\','')
   k1chk = k1chk.replace('/','')
   k1chk = k1chk.replace('^','')
   k1chk = k1chk.replace('(','')
   k1chk = k1chk.replace(')','')
   k1chk = k1chk.replace('[','')
   k1chk = k1chk.replace(']','') 
   k1chk = k1chk.replace('°','')
   k1chk = k1chk.replace('-','')
   k1chk = k1chk.replace("'",'')
   if k1chk != k1:
    print(L,k1,k1chk,y,x)
   return z
  newline = re.sub(r'<k2>([^<]+)$',k2tran,line)
  if False:
   print(line)
   print(newline)
   exit(1)
  if newline == line:
   # sometimes the iast and slp1 spellings are the same.
   # example anudaka
   continue
  # generate a Change instance
  # nothing to do in next line
  iline1 = None #iline + 1
  line1 = None #lines[iline1]
  newline1 = None
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
