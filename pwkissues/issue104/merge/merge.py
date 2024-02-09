# coding=utf-8
""" merge.py
"""
from __future__ import print_function
import sys, re,codecs
#import digentry  

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def meta_iline(lines):
 d = {}
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   if line in d:
    print('meta error duplicate',line)
   d[line] = iline
 return d

def write_lines(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for out in lines:
   f.write(out+'\n')  
 print(len(lines),"lines written to",fileout)

def renum_pwkvn_helper(Lold,base):
 # Lold is string
 # base is int
 if re.search(r'^[0-9]+$', Lold):
  nold = int(Lold)
  nnew = base + nold
  Lnew = '%s' % nnew # string
  return Lnew
 # Lold is 'fractional', e.g. 725.1. There are only 4 of these
 m = re.search(r'^([0-9]+)[.]([1-9]+)$', Lold)
 if m == None:
  # error condition
  print('renum_pwkvn_helper ERROR:',Lold)
  exit(1)
 a = m.group(1) # e.g. '725'
 b = m.group(2) # e.g. '1'
 a1 = int(a)
 newa1 = base + a1
 newa2 = '%s' % newa1  # string
 Lnew = newa2 + '.' + b
 return Lnew

def renum_pwkvn(lines):
 newlines = []
 L0 = 200000
 for line in lines:
  if not line.startswith('<L>'):
   # not a metaline.
   newlines.append(line)
   continue
  m = re.search(r'^<L>(.*?)<pc>',line)
  if m == None:
   print('renum_pwkvn: bad metaline:',line)
   exit(1)
  L_old = m.group(1)
  L_new = renum_pwkvn_helper(L_old,L0)
  newline = line.replace('<L>%s<pc>' % L_old, '<L>%s<pc>' % L_new)
  newlines.append(newline)
 return newlines

def supnote_pwkvn(lines):
 # add '<info n="sup_v"/>' to (last) line of body of entry
 newlines = []
 inentry = False
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   inentry = True
   metaline = line  # for use below
   newlines.append(line) # metaline
   continue
  if not inentry:
   # outside of entry
   newlines.append(line) # metaline
   continue   
  if line.startswith('<LEND>'):
   newlines.append(line) # metaline
   inentry = False
   continue
  # in an entry.
  # is next line <LEND>
  nextline = lines[iline + 1]
  if not nextline.startswith('<LEND>'):
   # line is not the last line of entry
   newlines.append(line) # metaline
   continue
  # line is last line of entry. get v from metaline
  m = re.search(r'<pc>([1-7])-',metaline)
  if m == None:
   print('supnote_pwkvn ERROR', metaline)
   exit(1)
  v = m.group(1) # volume
  note = '<info n="sup_%s"/>' % v
  newline = line + note
  newlines.append(newline)
 return newlines

if __name__=="__main__":
 filein1 = sys.argv[1]  # initial cdsl version pw.txt
 filein2 = sys.argv[2]  # initial cdsl version pwkvn.txt
 fileout = sys.argv[3]  # merged version of pw.txt

 lines1 = read_lines(filein1)
 print(len(lines1),"lines read from",filein1)
 lines2 = read_lines(filein2)
 print(len(lines2),"lines read from",filein2)
 lines2a = renum_pwkvn(lines2)
 lines2b = supnote_pwkvn(lines2a)
 newlines = lines1 + lines2b  # concatenate
 write_lines(fileout,newlines)
 
# (+ 674019 90460) == 764479
