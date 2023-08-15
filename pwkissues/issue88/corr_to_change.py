# coding=utf-8
""" change3.py

"""
from __future__ import print_function
import sys, re,codecs

class Change(object):
 def __init__(self,lnum,line,newline,meta,foundrecs):
  self.lnum = lnum
  self.line = line
  self.newline = newline
  self.meta = meta
  self.foundrecs = foundrecs
  
def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_changes(fileout,changes):
 outrecs = []
 for change in changes:
  outarr = []
  outarr.append('; %s' % change.meta)
  line = change.line  # old line
  newline = change.newline
  for rec in change.foundrecs:
   outarr.append('; old: %s' % rec.old)
   outarr.append('; new: %s' % rec.new)
   outarr.append('; -----')
  lnum = change.lnum
  outarr.append('%s old %s' %(lnum,line))
  outarr.append(';')
  outarr.append('%s new %s' %(lnum,newline))
  outarr.append('; --------------------------------------------------------')
  outrecs.append(outarr)
 # write outrecs
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(outrecs),"changes written to",fileout)

class Rec(object):
 def __init__(self,old,new):
  self.old = old
  self.new = new
  self.used = 0
  
def make_changes(lines,recs):
 drec = {}
 for rec in recs:
  drec[rec.old] = rec
 #
 nfound = 0
 nfoundlines = 0
 #regexraw = r'{%(.*?)%}' 
 #regex = re.compile(regexraw)
 #langstart = ('<ger>','<fr>','<tib>','<lat>')
 changes = [] # list of Change objects
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   meta = line
   #continue
  if line.startswith('<LEND>'):
   meta = None
   #continue
  newline = line
  foundrecs = []
  for rec in recs:
   newline1 = newline.replace(rec.old,rec.new)
   if newline1 != newline:
    foundrecs.append(rec)
    rec.used = rec.used + 1
   newline = newline1
  # prepare change, if needed
  if newline != line:
   nfoundlines = nfoundlines + 1
   lnum = iline + 1
   change = Change(lnum,line,newline,meta,foundrecs)
   changes.append(change)
 #print('nfound=',nfound)
 print(len(changes),"lines to change")
 # find number of corrections used
 unusedrecs = [rec for rec in recs if rec.used == 0]
 n = len(unusedrecs)
 print(n,"corrections not used")
 if n != 0:
  for rec in unusedrecs:
   print(rec.old)
 return changes

def init_prec(filein):
 lines = read_lines(filein)
 old = None
 for line in lines:
  m = re.search(r'^(old|new): (.*)$',line)
  if m == None:
   continue
  ltype = m.group(1)
  data = m.group(2)
  if ltype == 'old':
   old = data
  elif ltype == 'new':
   new = data
   yield Rec(old,new)
   old = None
  else:
   print('ERROR: line=',line)
   
if __name__=="__main__":
 filein = sys.argv[1] # bhs.txt
 filein1 = sys.argv[2]  # check3a_edit.txt
 fileout = sys.argv[3] # unmarked italic
 lines = read_lines(filein)
 recs = list(init_prec(filein1))  # prechange
 print(len(recs),"read from",filein1)
 changes = make_changes(lines,recs)
 # write_changes(fileout,changes)
 write_changes(fileout,changes)
 
