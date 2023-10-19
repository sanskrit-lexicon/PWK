# coding=utf-8
""" regex_compare_texts1.py
  optionally write copy of xxx.txt with
  additional '* <L>' markup for entries flagged as different
"""
from __future__ import print_function
import sys, re,codecs
import digentry  

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines
 
def get_metafield(f,meta):
 if f == 'k2':
  if '<h>' in meta:
   regex = r'<%s>(.*?)<' % f
  else:
   regex = r'<%s>(.*?)$' % f
 else:
  regex = r'<%s>(.*?)<' % f
 m = re.search(regex,meta)
 value = m.group(1)
 return value


def hwdiffs(cdsl_lines,ab_lines):
 cdsl_metas = [line for line in cdsl_lines if line.startswith('<L>')]
 ab_metas = [line for line in ab_lines if line.startswith('<L>')]
 print('cdsl has %s entries' % len(cdsl_metas))
 print('ab   has %s entries' % len(ab_metas))
 assert len(cdsl_metas) == len(ab_metas)
 diffs = []
 for iline,line in enumerate(cdsl_metas):
  line1 = ab_metas[iline]
  if line != line1:
   diff = (line,line1)
   diffs.append(diff)
 print(len(diffs),"differences in metalines")
 return diffs


def write_difftext(fileout,e1s,e2s):
 outrecs = []
 n = 0
 no = 0
 for i,e1 in enumerate(e1s):
  e2 = e2s[i]
  if e1.text == e2.text:
   n = n + 1
  else:
   no = no + 1
   if no < 5:
    print(e1.metaline)
    print('cdsl text\n',e1.text)
    print()
    print('ab text\n',e2.text)
   
 print(n,'entries have same text')
 
def get_link(metaline):
 m = re.search(r'<L>(.*?)<pc>(.*?)<k1>',metaline)
 page = m.group(2)
 link = 'https://www.sanskrit-lexicon.uni-koeln.de/scans/csl-apidev/servepdf.php?dict=pw&page=%s' % page
 return link

def previous_compare_tags(text1,text2,metaline,regex):
 # first difference
 a1 = re.findall(regex,text1)
 a2 = re.findall(regex,text2)
 ans = []
 if a1 == a2:
  return ans 
 # diff
 n1 = len(a1)
 n2 = len(a2)
 n = max(n1,n2)
 tok = ''
 for i in range(0,n):
  if i < n1:
   x1 = a1[i]
  else:
   x1 = 'None'
   a1.append(x1)
  if i < n2:
   x2 = a2[i]
  else:
   x2 = 'None'
   a2.append(x2)
  if x1 != x2:
   meta = re.sub(r'<k2>.*$','',metaline)
   link = get_link(meta)
   outarr = []
   outarr.append('--------')
   outarr.append('* ' + meta)  
   outarr.append(link)
   i1 = max(i - 5,0)
   for j in range(i1,i):
    outarr.append('%s %s' %(j+1,a1[j]))
   outarr.append('%s: %s  !=  %s' %(i+1,x1,x2))
   ans = outarr
   return ans
 # ever executed?
 return ans

def compare_tags(text1,text2,metaline,regex):
 dbg = False
 a1 = re.findall(regex,text1)
 a2 = re.findall(regex,text2)
 ans = []
 if a1 == a2:
  return ans
 n1 = len(a1)
 n2 = len(a2)
 n = max(n1,n2)
 # get a1, a2 with same number of elments. Missing = 'None' (string)
 b1 = []
 b2 = []
 for i in range(0,n):
  if i < n1:
   x1 = a1[i]
  else:
   x1 = 'Nonex'
   a1.append(x1)
   if dbg: print('x1 none i=',i)
  b1.append(x1)
  if i < n2:
   x2 = a2[i]
  else:
   x2 = 'Nonex'
   a2.append(x2)
   if dbg: print('x2 none i=',i)
  b2.append(x2)
 #
 m1 = len(b1)
 m2 = len(b2)
 m = max(m1,m2)
 if dbg: print(metaline,n1,n2,n,m)
 assert m1 == m2
 
 # construct outarr
 outarr = []  # aka ans. returned
 meta = re.sub(r'<k2>.*$','',metaline)
 link = get_link(meta)
 outarr.append('--------')
 outarr.append('* ' + meta)  
 outarr.append(link)
 for i in range(0,m):
  x1 = b1[i]
  x2 = b2[i]
  if dbg: print('%s\nx1=%s\nx2=%s' %(i,x1,x2))
  if x1 == x2: #not almost_equal(x1,x2):
   out = '%s: %s ==' %(i+1,x1)
  else:
   out = '%s: %s  !=  %s' %(i+1,x1,x2)
  outarr.append(out)
  if dbg: print('chk',out)
 for idx,out in enumerate(outarr):
  if dbg: print('dbg: ',out)
 return outarr

def compare(entries1,entries2,maxdiff,regex):
 nd = 0
 ntag = 0
 tagtype = None
 tag = 'ls'
 #tagtype='n'
 outrecs = []
 for ientry,e1 in enumerate(entries1):
  e2 = entries2[ientry]
  text1 = ' '.join(e1.datalines)
  text2 = ' '.join(e2.datalines)
  # next exits on diff
  ans = compare_tags(text1,text2,e1.metaline,regex)
  if ans != []:
   outrecs.append(ans)
   if maxdiff != None:
    if len(outrecs) > maxdiff:
     break
 return outrecs

def write_outrecs(fileout,outrecs):
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outrecs),"cases written to",fileout)
 
def print_outrecs(outrecs):
 for outarr in outrecs:
  for out in outarr:
   print(out)

def compare_hws(entries1,entries2):
 nd = 0
 ntag = 0
 tagtype = None
 tag = 'ls'
 #tagtype='n'
 for ientry,e1 in enumerate(entries1):
  e2 = entries2[ientry]
  if e1.metaline == e2.metaline:
   continue
  print('metaline diff:')
  print('#1: %s' %(e1.metaline))
  print('#2: %s' %(e2.metaline))
  exit(1)

def write_xtra(fileout,filein,outrecs):
 """ copy of filein, with markup related to outrecs.
   Purpose to facilitate corrections
 """
 # harvest metaline L from outrecs
 d = {}
 for outarr in outrecs:
  # look for <L>X<pc> (in metaline)
  for out in outarr:
   m = re.search(r'<L>(.*?)<pc>',out)
   if m:
    L = m.group(1)
    if L in d:
     print('Unexpected duplicate L')
    d[L] = True
    break
 # get the original lines
 lines = read_lines(filein)
 # modify each metaline
 newlines = []
 for line in lines:
  m = re.search(r'^<L>(.*?)<pc>',line)
  if m == None:
   newline = line
  else:
   L = m.group(1)
   if L in d:
    newline = '* ' + line
   else:
    newline = line
  newlines.append(newline)
 # write newlines
 with codecs.open(fileout,"w","utf-8") as f:
  for out in newlines:
   f.write(out+'\n')  
 print('write_extra ',len(newlines),"lines written to",fileout)

if __name__=="__main__":
 regex = sys.argv[1]
 filein = sys.argv[2] # xxx.txt cdsl
 filein1 = sys.argv[3] # xxx.txt AB
 fileout = sys.argv[4] #
 if len(sys.argv) == 7:
  # optional output
  fileout_xtra = sys.argv[5]
  fileout1_xtra = sys.argv[6]
  xtraflag = True
 else:
  xtraflag = False
 entries_cdsl = digentry.init(filein)
 # reset Ldict
 digentry.Entry.Ldict = {}
 entries_ab = digentry.init(filein1)
 # compare_hws(entries_cdsl,entries_ab)
 maxdiff = None
 outrecs = compare(entries_cdsl,entries_ab,maxdiff,regex)
 #print_outrecs(outrecs)
 write_outrecs(fileout,outrecs)
 if xtraflag:
  write_xtra(fileout_xtra,filein,outrecs)
  write_xtra(fileout1_xtra,filein1,outrecs)
