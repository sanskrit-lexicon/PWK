# coding=utf-8
""" bb_after.py
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for out in lines:
   f.write(out+'\n')  
 print(len(lines),"lines written to",fileout)

def write_recs(fileout,outrecs,printflag=True,blankflag=True):
 # outrecs is array of array of lines
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
   if blankflag:
    out = ''  # blank line separates recs
    f.write(out+'\n')
 if printflag:
  print(len(outrecs),"records written to",fileout)

class Change:
 def __init__(self,metaline,lnum,old,new):
  self.metaline = metaline
  self.lnum = lnum
  self.old = old
  self.new = new


def get_AB_candidates():
 # AB mentions these entries as implying alt headwords
 Lints =  (
  16678, 22390, 23281, 26293, 28410,
  30597, 34090, 34556, 36315, 37930,
  39355, 39831, 39852, 43702, 43761,
  44078, 44931, 46971, 55339, 55378,
  56092, 59172, 61689, 61801, 74511,
  77163, 80864, 87626, 88417, 89051,
  94286, 97985, 100189, 102651, 103657,
  110117, 110192, 112382, 113429, 115433,
  125488, 130735, 133969,
  200221, 203121, 203284, 203898, 204099, 
  204416, 204577, 205639, 206832, 207055, 
  207313, 209005, 209263, 213195, 213697,
  200048, 200334, 201819, 206328, 208193,
  209653, 214672, 221290
  )
 Lstrs = ["%s" % x for x in Lints]
 print(len(Lstrs),"identified by AB")
 d = {x:0 for x in Lstrs}
 return d

def get_JF_candidates():
 Lints = [21217, 21803, 22760, 24412,74318,
          94162, 124106, 200027, 200069, 200935,
          201924, 202368, 204118, 204195, 204440,
          206886, 207889, 207904, 214939, 215265,
          215302, 215307, 216046, 216515, 216995,
          222058, 
          ]
 Lstrs = ["%s" % x for x in Lints]
 print(len(Lstrs),"identified by JF")
 d = {x:0 for x in Lstrs}
 return d
 
AB_candidates_dict = get_AB_candidates()
JF_candidates_dict = get_JF_candidates()

class Outpart:
 def __init__(self,metaline,bbline,bblnum,after_word_n):
  self.metaline = metaline
  self.bbline = bbline
  self.bblnum = bblnum # int
  self.after_word_n = after_word_n #int
  m = re.search(r'<L>(.*?)<pc>',metaline)
  L = m.group(1)
  self.L = L
  if L in AB_candidates_dict:
   AB_candidates_dict[L] = AB_candidates_dict[L] + 1
   src = 'AB'
   srcnum = 1
  elif L in JF_candidates_dict:
   JF_candidates_dict[L] = JF_candidates_dict[L] + 1
   src = 'JF'
   srcnum = 2
  else:
   src = '_'
   srcnum = 9 # unknown
  self.src = src
  self.srcnum = srcnum
   
def analyze_lines(lines):
 outlines = []
 outparts = []
 nmeta = 0
 for iline,line in enumerate(lines):
  m = re.search(r'(<L>.*)$',line)
  if not line.startswith('<L>'):
   continue
  nmeta = nmeta + 1
  metaline = line
  iline1 = iline + 1
  bbline = lines[iline1] # broken-bar line
  bblnum = iline1 + 1
  before,after = bbline.split('¦')
  # require {# in after
  m = re.search(r'{#',after)
  if m == None:
   continue # skip
  after_word_n = m.start()
  if '√' in before:
   continue # skip roots
  # require only 1 {# in before
  before_words = re.findall(r'{#',before)
  before_word_n = len(before_words)
  assert before_word_n != 0
  if before_word_n > 1:
   continue # skip
  # we now have a candidate.
  
  outpart = Outpart(metaline,bbline,bblnum,after_word_n)
  outparts.append(outpart)
 print(len(outparts),'candidates.',nmeta,'metalines')
 return outparts

def write_outparts(fileout,outparts):
 outparts_sorted = sorted(outparts,key = lambda x: (x.srcnum,x.after_word_n))
   
 outrecs = []
 outarr = [] # header
 outarr.append('; ******************************************************')
 outarr.append('; %s records :' % len(outparts))
 outarr.append('; ******************************************************')
 outrecs.append(outarr)
 for c in outparts_sorted:
  outarr = []
  # experience shows after_word_n <= 607, so only 3 digits needed.
  nout = '%03d' % c.after_word_n
  lnum = c.bblnum
  lnumstr = '%s' % lnum
  bbline = c.bbline
  metaline = c.metaline
  src = c.src
  a = (nout+src,bbline,metaline,lnumstr)
  out = '\t'.join(a)
  outarr.append(out)
  outrecs.append(outarr)
 print(len(outrecs),"outrecs")
 write_recs(fileout,outrecs,blankflag=True)
def check_src_unused():
 n = 0
 for L in AB_candidates_dict:
  val = AB_candidates_dict[L]
  if val == 0:
   print('AB missed '+L)
   n = n + 1
 n = 0
 for L in JF_candidates_dict:
  val = JF_candidates_dict[L]
  if val == 0:
   print('JF missed '+L)
   n = n + 1
   
def write_changes(fileout,outparts):
   
 outrecs = []
 outarr = [] # header
 outarr.append('; ******************************************************')
 outarr.append('; %s records :' % len(outparts))
 outarr.append('; ******************************************************')
 outrecs.append(outarr)
 for c in outparts:
  if c.srcnum == 9:
   continue
  src = c.src
  assert src in ('JF','AB')
  
  lnum = c.bblnum
  lnumstr = '%s' % lnum
  bbline = c.bbline
  metaline = c.metaline
  lnum_meta = lnum - 1
  
  outarr = []
  srcd = {'JF':'Jim', 'AB':'Andhrabharati'}
  outarr.append('; src = %s' % srcd[src])
  outarr.append('%s old %s' %(lnum_meta,metaline))
  outarr.append('%s new %s' %(lnum_meta,metaline))  # to change manually
  outarr.append(';')
  outarr.append('%s old %s' %(lnum,bbline))
  outarr.append('%s new %s' %(lnum,bbline))
  outarr.append('; -------------------------------------------------------')
  outrecs.append(outarr)
 print(len(outrecs),"outrecs")
 write_recs(fileout,outrecs,blankflag=False)
 
if __name__=="__main__":
 filein = sys.argv[1]  # pw.txt
 fileout = sys.argv[2]  # candidate file
 fileout1 = sys.argv[3] # change file
 lines = read_lines(filein)
 outparts = analyze_lines(lines)
 write_outparts(fileout,outparts)
 write_changes(fileout1,outparts)
 check_src_unused()
 
