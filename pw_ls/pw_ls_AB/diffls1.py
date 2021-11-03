#-*- coding:utf-8 -*-
"""diffls1.py
"""
from __future__ import print_function
import sys, re,codecs
from parseheadline import parseheadline

class Entry(object):
 Ldict = {}
 def __init__(self,lines,linenum1,linenum2):
  # linenum1,2 are int
  self.metaline = lines[0]
  self.lend = lines[-1]  # the <LEND> line
  self.datalines = lines[1:-1]  # the non-meta lines
  # parse the meta line into a dictionary
  #self.meta = Hwmeta(self.metaline)
  self.metad = parseheadline(self.metaline)
  self.linenum1 = linenum1
  self.linenum2 = linenum2
  #L = self.meta.L
  """
  L = self.metad['L']
  if L in self.Ldict:
   print("Entry init error: duplicate L",L,linenum1)
   exit(1)
  self.Ldict[L] = self
  """
  self.lsarr = []
   
def init_entries(filein):
 # slurp lines
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [line.rstrip('\r\n') for line in f]
 recs=[]  # list of Entry objects
 inentry = False  
 idx1 = None
 idx2 = None
 for idx,line in enumerate(lines):
  if inentry:
   if line.startswith('<LEND>'):
    idx2 = idx
    entrylines = lines[idx1:idx2+1]
    linenum1 = idx1 + 1
    linenum2 = idx2 + 1
    entry = Entry(entrylines,linenum1,linenum2)
    recs.append(entry)
    # prepare for next entry
    idx1 = None
    idx2 = None
    inentry = False
   elif line.startswith('<L>'):  # error
    print('init_entries Error 1. Not expecting <L>')
    print("line # ",idx+1)
    print(line.encode('utf-8'))
    exit(1)
   else: 
    # keep looking for <LEND>
    continue
  else:
   # inentry = False. Looking for '<L>'
   if line.startswith('<L>'):
    idx1 = idx
    inentry = True
   elif line.startswith('<LEND>'): # error
    print('init_entries Error 2. Not expecting <LEND>')
    print("line # ",idx+1)
    print(line.encode('utf-8'))
    exit(1)
   else: 
    # keep looking for <L>
    continue
 # when all lines are read, we should have inentry = False
 if inentry:
  print('init_entries Error 3. Last entry not closed')
  print('Open entry starts at line',idx1+1)
  exit(1)

 print(len(lines),"lines read from",filein)
 print(len(recs),"entries found")
 return recs

def get_ls_pw(text):
 "All <ls>X</ls>"
 lsarr = re.findall(r'<ls>.*?</ls>',text)
 return lsarr

def generate_ab_ls(lsarr):
 """ combine <ls> and following <ln>
 """
 val = None # previous <ls>x</ls>
 for idx,item in enumerate(lsarr):
  if idx == 0:
   if item.startswith('<ln>'):
    yield item
   else:  # it is <ls>
    val = item
  elif item.startswith('<ls>'):
   if val != None:
    yield val
   val = item
  else: # item = '<ln>'
   if val != None:
    newval = val + item
    yield newval
    val = None
   else:
    yield item
    val = None
 if val != None:
  yield val  # last one

def lsab1_merge(lsarr):
 """ assume each item x in the lsarr list has one of three forms:
  <ls>X</ls><ln>Y</ln>  -> <ls>ZY</ls>
  <ls>X</ls> or -> <ls>Z</ls>
  <ln>Y</ln> or -> <ls>Y</ls>
  where Z is X with the spaces removed
  for ab
 """
 ans = []
 if False:
  n = len(lsarr)
  if n != 0:
   print('lsab1_merge',n)
   for a in lsarr:
    print(a)
   print('quitting') 
   #exit(1)
 for a in lsarr:
  #if a.startswith('<ls>VĀMANA</ls>'): print('a=',a)
  m = re.search(r'^<ls>VĀMANA</ls><ln>(.*?)</ln>$',a)
  if m != None:
   ln = m.group(1)
   d = '<ls>VĀMANA %s</ls>' %ln
   if False:
    print("ab1_merge: '%s' -> '%s'" %(a,d))
   ans.append(d)
   continue
  # 'Usual' case
  b = a.replace(' ','')
  c = b.replace('ln>','ls>')
  # is VĀMANA handled right?  It should have no period in PW.
  d = c.replace('</ls><ls>','')
  ans.append(d)
 return ans

def get_ls_ab(text,option):
 """ remove a lot of stuff that is in the way of ls identification
 """
 text = re.sub(r'<ab>.*?</ab>',' ',text)
 text = re.sub(r'<lex>.*?</lex>',' ',text)
 text = re.sub(r'<bot>.*?</bot>',' ',text)
 text = re.sub(r'<is>.*?</is>',' ',text)
 text = re.sub(r'{%.*?%}',' ',text)
 text = re.sub(r'{#.*?#}',' ',text)
 # replace <x> with <ln>x</ln> when x starts with  a digit
 # 10-26-2021 This change made in temp_pw_AB_02.txt
 #text = re.sub(r'<([1-9].*?)>',r'<ln>\1</ln>',text)
 lsarr0 = re.findall(r'<l[sn]>.*?</l[sn]>',text)
 lsarr1 = list(generate_ab_ls(lsarr0))
 if option == 'ab':
  lsarr = lsarr1
 else:  # ab1
  lsarr = lsab1_merge(lsarr1)
 return lsarr

def markls(entry,option): 
 if option != 'pw':
  text = ' '.join(entry.datalines)
  entry.lsarr = get_ls_ab(text,option)
  entry.lsilines = []
  return
 lsall = []
 ilinesall = []  # parallel to lsall.
 for iline,text in enumerate(entry.datalines):
  lsarr = get_ls_pw(text)
  for ls in lsarr:
   lsall.append(ls)
   ilinesall.append(iline)
 entry.lsarr = lsall
 entry.lsilines = ilinesall

def write_ls(fileout,entries):
 with codecs.open(fileout,"w","utf-8") as f:
  nentry = 0 # number of entries with an ls
  nls = 0 # total number of ls entries
  for entry in entries:
   lsarr = entry.lsarr
   n = len(lsarr)
   if n == 0:
    continue
   nentry = nentry + 1
   nls = nls + n
   outarr = []
   L = entry.metad['L']
   k1 = entry.metad['k1']
   outarr.append('; %s %s (%s)' % (L,k1,n))
   for ls in lsarr:
    outarr.append(ls)
   outarr.append('; --------------------')
   for out in outarr:
    f.write(out+'\n')
 print(nentry,'entries have ls markup')
 print(nls,'Total ls markup instances')

def surely_different(x,y):
 x1 = re.sub(r'[.,]</ls>','</ls>',x)
 y1 = re.sub(r'[.,]</ls>','</ls>',y)
 if x1 == y1:
  return False
 x2 = x1.replace(' ','')
 y2 = y1.replace(' ','')
 if x2 == y2:
  return False
 return True # x and y are different

def almost_equal(a,b):
 """ arrays (lsarr1, 2)
 """
 n = len(a)
 if n != len(b):
  return False
 for i,x in enumerate(a):
  y = b[i]
  if surely_different(x,y):
   return False
 return True

def write_diff(fileout,entries1,entries2):
 # how many differences?
 ndiff = 0
 n1tot = 0
 n2tot = 0
 num_ls_entries1 = 0
 num_ls_entries2 = 0
 outrecs = []
 for ientry,entry1 in enumerate(entries1):
  entry2 = entries2[ientry]
  lsarr1 = entry1.lsarr
  lsarr2 = entry2.lsarr
  n1 = len(lsarr1)
  n2 = len(lsarr2)
  n1tot = n1tot + n1
  n2tot = n2tot + n2
  if n1 != 0:
   num_ls_entries1 = num_ls_entries1 + 1
  if n2 != 0:
   num_ls_entries2 = num_ls_entries2 + 1
  flag = almost_equal(lsarr1,lsarr2)
  if flag:
   continue
  # different   
  outarr = []
  assert entry1.metaline == entry2.metaline
  L = entry1.metad['L']
  k1 = entry1.metad['k1']
  pc = entry1.metad['pc']
  out = '; %s %s %s : (%s %s)' %(L,k1,pc,n1,n2)
  outarr.append(out)
  if (n1,n2) == (1,1):
   ndiff = ndiff + 1
   outarr = []
   outarr.append('; <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
   outarr.append(out)
   outarr.append('; pw: %s' % lsarr1[0])
   outarr.append('; ab: %s' % lsarr2[0])
   for i,ls in enumerate(lsarr1):
    iline = entry1.lsilines[i]
    lnum = entry1.linenum1 + iline + 1
    line = entry1.datalines[iline]
    outarr.append('%s old %s' %(lnum,line))
    outarr.append(';')
    outarr.append('%s new %s' %(lnum,line))
   outarr.append('; >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
  outrecs.append(outarr)
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(outrecs),'entries have different ls')
 print(num_ls_entries1,'entries of cologne version have ls markup')
 print(num_ls_entries2,'entries of AB version have ls markup')
 print(n1tot,'ls instances in cologne version')
 print(n2tot,'ls instances in AB version')
 print(ndiff,'different ls in 1,1 case')

def write_diff_0_N(fileout,entries1,entries2):
 # change transaction lines for cases where no ls refs in pw (entries1)
 ndiff = 0
 n1tot = 0
 n2tot = 0
 num_ls_entries1 = 0
 num_ls_entries2 = 0
 outrecs = []
 for ientry,entry1 in enumerate(entries1):
  entry2 = entries2[ientry]
  lsarr1 = entry1.lsarr
  lsarr2 = entry2.lsarr
  n1 = len(lsarr1)
  n2 = len(lsarr2)
  n1tot = n1tot + n1
  n2tot = n2tot + n2
  if n1 != 0:
   #num_ls_entries1 = num_ls_entries1 + 1
   continue
  if n2 != 0:
   num_ls_entries2 = num_ls_entries2 + 1
  flag = almost_equal(lsarr1,lsarr2)
  if flag:
   continue
  # different   
  outarr = []
  assert entry1.metaline == entry2.metaline
  L = entry1.metad['L']
  k1 = entry1.metad['k1']
  pc = entry1.metad['pc']
  out = '; %s %s %s : (%s %s)' %(L,k1,pc,n1,n2)
  outarr.append(out)
  if True:
   ndiff = ndiff + 1
   outarr = []
   outarr.append('; <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
   outarr.append(out)
   #outarr.append('; pw: %s' % lsarr1[0])
   for ls in lsarr2:
    outarr.append('; ab: %s' % lsarr2[0])
   for iline,line in enumerate(entry1.datalines):
    lnum = entry1.linenum1 + iline + 1
    #line = entry1.datalines[iline]
    outarr.append('%s old %s' %(lnum,line))
    outarr.append(';')
    outarr.append('%s new %s' %(lnum,line))
   outarr.append('; >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
  outrecs.append(outarr)
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(outrecs),'entries have different ls')
 print(num_ls_entries1,'entries of cologne version have ls markup')
 print(num_ls_entries2,'entries of AB version have ls markup')
 print(n1tot,'ls instances in cologne version')
 print(n2tot,'ls instances in AB version')
 print(ndiff,'different ls in 1,1 case')
 
if __name__=="__main__": 
 filein1 = sys.argv[1]  # Cologne pw.txt
 #assert option in ['pw','ab','ab1']  # Cologne or Andhrabharti version
 filein2 = sys.argv[2] #  ab version of pw.txt
 fileout = sys.argv[3] # 
 entries1 = init_entries(filein1)
 for entry in entries1:
  markls(entry,'pw')
 entries2 = init_entries(filein2)
 assert len(entries1) == len(entries2)
 for entry in entries2:
  markls(entry,'ab1')
 write_diff_0_N(fileout,entries1,entries2)

