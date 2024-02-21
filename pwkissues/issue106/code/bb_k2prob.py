# coding=utf-8
""" bb_k2prob.py
"""
from __future__ import print_function
import sys, re,codecs
from bb import regexmap

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

class BBrec:
 def __init__(self,metaline,bbdata,bbcode):
  self.metaline = metaline
  self.bbdata = bbdata
  self.bbcode = bbcode# filled in later

#bbregexes = get_bbregexes()

def write_bbrecs(dirout,bbrecs):
 bbcodes = [bbcode for bbcode,bbregex in bbregexes]
 for bbcode in bbcodes:
  fileout = '%s/bb_%s.txt' %(dirout,bbcode)
  outrecs = []
  for bbrec in bbrecs:
   if bbrec.bbcode != bbcode:
    continue
   outarr = []
   fields = (bbrec.metaline,bbrec.bbdata)
   out = '\t'.join(fields)
   outarr.append(out)
   outrecs.append(outarr)
  write_recs(fileout,outrecs)

def bbrecs_init(filein,sfx):
 bbcode = sfx
 lines = read_lines(filein)
 # print(len(lines),"lines read from",filein)
 recs = []
 for line in lines:
  if not line.startswith('<L>'):
   continue
  parts = line.split('\t')
  assert len(parts) == 2
  metaline,bbdata = parts
  rec = BBrec(metaline,bbdata,bbcode)
  recs.append(rec)
 print(len(recs),"bbrecs found in",filein)
 return recs

def get_k2_from_meta(metaline):
 m = re.search(r'<k2>([^<]+)$',metaline)
 if m == None:
  print('get_k2_from_meta ERROR:',metaline)
  exit(1)
 k2 = m.group(1)
 return k2

def get_k2_from_bb(bbrec):
 bbcode = bbrec.bbcode
 regex,regexraw = regexmap[bbcode]
 bbdata = bbrec.bbdata
 # cf. get_bbregexes function in bb.py

 k2 = '?'
 m = re.search(regex,bbdata)
 if bbcode in ('01','01c'):
  k2 = m.group(1)
 elif bbcode in ('01a','01b'):
  k2 = '*' + m.group(1)
 elif bbcode == '01d':
  k2 =  m.group(1) + '*'
 elif bbcode in ('02','02c'):
  hom = m.group(1)
  hw = m.group(2)
  k2 = '%s. %s' % (hom,hw)
 elif bbcode in ('02a','02b'):
  hom = m.group(1)
  hw = '*' + m.group(2)
  k2 = '%s. %s' % (hom,hw)
 elif bbcode == '03':
  k2 = '°' + m.group(1)
 elif bbcode == '03a':
  k2 =  m.group(1) + '°'
 elif bbcode == '03b':
  hom = m.group(1)
  hw = '°' + m.group(2)
  k2 = '%s. %s' % (hom,hw)
 elif bbcode == '03c':
  hom = m.group(1)
  hw =  m.group(2) + '°'
  k2 = '%s. %s' % (hom,hw)
 elif bbcode == '04':
  k2 = '(' + m.group(1) + ')'
 elif bbcode == '04a':
  hom = m.group(1)
  hw =  m.group(2) 
  k2 = '%s. (%s)' % (hom,hw)
 else:
  print('get_k2_from_bb problem')
  exit(1)
 return k2

def check_k2(recs,bbcode):
 probrecs = []
 regex = regexmap[bbcode]
 for rec in recs:
  metaline = rec.metaline
  bbdata = rec.bbdata
  assert bbcode == rec.bbcode
  # get k2 from metaline
  k2_meta = get_k2_from_meta(metaline)
  k2_bb = get_k2_from_bb(rec)
  if k2_meta != k2_bb:
   rec.k2_bb = k2_bb
   rec.k2_meta = k2_meta
   probrecs.append(rec)
 #print("check_k2: ",len(probrecs),"problems")
 return probrecs

def write_problems(fileout,bbrecs):
 with codecs.open(fileout,"w","utf-8") as f:
  for bbrec in bbrecs:
   outarr = []
   outarr.append('%s\t%s' % (bbrec.metaline,bbrec.bbdata))
   outarr.append(' k2_meta = %s, k2_bb = %s' %(bbrec.k2_meta, bbrec.k2_bb))
   outarr.append('')
   for out in outarr:
    f.write(out+'\n')
 print(len(bbrecs),"records written to",fileout)
 
if __name__=="__main__":
 bbcode = sys.argv[1]
 dirin = sys.argv[2]  # directory for input
 fileout = sys.argv[3] #  output
 filein = '%s/bb_%s.txt' %(dirin,bbcode)
 bbrecs = bbrecs_init(filein,bbcode)

 bbrecs1 = check_k2(bbrecs,bbcode)  # return problem records
 
 write_problems(fileout,bbrecs1)
 
 #write_recs(fileout,outrecs)
 
