# coding=utf-8
""" nohomchk.py
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

def write_recs(fileout,outrecs):
 # outrecs is array of array of lines
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
   out = ''  # blank line separates recs
   f.write(out+'\n')
 print(len(outrecs),"records written to",fileout)

def nohomchk(lines):
 outrecs = []
 nprob = 0 # metaline and ¦ line inconsistent
 nok = 0 # metaline and ¦ line consistent.
 for iline,line in enumerate(lines):
  if not line.startswith('<L>'):
   # line not a metaline.
   # newlines.append(line)
   continue
  m = re.search(r'<k2>([^<]*)$',line) # no <h> after <k2>
  if m == None:
   # skip if <h> present
   # newlines.append(line)
   continue
  k2 = m.group(1)
  # for the entries from pwkvn
  #  may contain multiple items, comma-separated
  k2 = re.sub(r',.*$','',k2)
  # This k2 may contain 'N. ' (homonym)
  if re.search(r'^[0-9]',k2):
   # skip
   continue
  # check for consistency with next line 
  iline1 = iline + 1
  line1 = lines[iline1]
  m = re.search(r'^([^(]*?){#(.*?)#}.*?¦',line1)
  if m != None:
   flag = m.group(1)
   k2a = m.group(2)
   if '*' in flag:
    k2a = '*' + k2a
  if m == None:
   # for some (approx 2700), the form is ({#X#}) rather than {#X#}, and
   m = re.search(r'^\((.*?){#(.*?)#}\).*?¦',line1)
   if m != None:
    flag = m.group(1)
    assert '*' not in flag
    k2a = '(' + m.group(2) + ')'
  if m == None:
   # unexpected
   nprob = nprob + 1
   outarr = []
   outarr.append(line + ' TYPE 1') # metaline
   outarr.append(line1) # ¦ line
   outrecs.append(outarr)
   continue
  if (k2 == k2a):
   nok = nok + 1
  else:
   nprob = nprob + 1
   outarr = []
   outarr.append(line + ' TYPE k2a=%s' % k2a) # metaline
   outarr.append(line1) # ¦ line
   outrecs.append(outarr)
 print('nohomchk: %s ok, %s questionable' %(nok, nprob))
 return outrecs

if __name__=="__main__":
 filein = sys.argv[1]  # initial cdsl version pw.txt
 fileout = sys.argv[2]  # version of pw.txt with <e>N removed
 
 lines = read_lines(filein)
 print(len(lines),"lines read from",filein)

 outrecs = nohomchk(lines)
 write_recs(fileout,outrecs)
 
