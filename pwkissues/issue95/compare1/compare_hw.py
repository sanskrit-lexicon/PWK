# coding=utf-8
""" compare_hw.py
"""
from __future__ import print_function
import sys, re,codecs

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

def write_diffs(fileout,diffs):
 #exit(1)
 outrecs = []
 for idiff,diff in enumerate(diffs):
  cdsl_meta,ab_meta = diff
  outarr = []
  L = get_metafield('L',cdsl_meta)
  L1 = get_metafield('L',ab_meta)
  assert L == L1
  pc_cdsl = get_metafield('pc',cdsl_meta)
  pc_ab   = get_metafield('pc',ab_meta)
  assert pc_cdsl == pc_ab
  k1_cdsl = get_metafield('k1',cdsl_meta)
  k1_ab   = get_metafield('k1',ab_meta)
  assert k1_cdsl == k1_ab
  k2_cdsl = get_metafield('k2',cdsl_meta)
  k2_ab   = get_metafield('k2',ab_meta)
  assert k2_cdsl != k2_ab
  
  outarr.append('; %03d: L=%s' %(idiff+1,L))
  outarr.append('cdsl: %s' % cdsl_meta)
  outarr.append('  ab: %s' % ab_meta)
  outarr.append(';  ------------------------------')
  outrecs.append(outarr)
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(diffs),"differences written to",fileout)
def hwdiffs(lines0,lines1):
 metas0 = [line for line in lines0 if line.startswith('<L>')]
 metas1 = [line for line in lines1 if line.startswith('<L>')]
 print('ab0 has %s entries' % len(metas0))
 print('ab1 has %s entries' % len(metas1))
 a = set(metas0)
 b = set(metas1)
 c = a.intersection(b)
 print('%s metalines are identical' % len(c))
 d = a.difference(b)
 outarr = []
 print('%s metalines are in ab0 only' % len(d))
 d1 = b.difference(a)
 print('%s metalines are in ab1 only' % len(d1))
 
 for meta in metas0:
  if meta not in b:
   print('only ab0: %s ' % meta)
 print()
 for meta in metas1:
  if meta not in a:
   print('only ab1: %s ' % meta)
 
 print('exiting in hwdiffs')
 return
 assert len(metas0) == len(metas1)
 diffs = []
 for iline,line in enumerate(metas0):
  line1 = metas1[iline]
  if line != line1:
   diff = (line,line1)
   diffs.append(diff)
 print(len(diffs),"differences in metalines")
 return diffs

if __name__=="__main__":
 filein = sys.argv[1] # bhs.txt cdsl
 filein1 = sys.argv[2] # bhs.txt AB
 fileout = sys.argv[3] # 
 lines = read_lines(filein)
 lines1 = read_lines(filein1)
 hwdiffs(lines,lines1) #count comparison
 #diffs = hwdiffs_L(lines,lines1)
 #write_diffs(fileout,diffs)
 
