#-*- coding:utf-8 -*-
"""change5.py  Remove {##} in first line
 
"""
import sys,re,codecs
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
  if iline != (ilinemeta + 1):
   continue
  m = re.search(r'^{#(.*?)#} +',line)
  k1dup = m.group(1)
  if k1dup != k1:
   print(line)
   print(k1dup,'!=',k1)
   exit(1)
  assert k1dup == k1
  newline = re.sub(r'^{#(.*?)#} +','',line)
  if newline == line:
   print('unexpected')
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
