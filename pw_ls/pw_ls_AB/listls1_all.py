#-*- coding:utf-8 -*-
"""listls1_all.py
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
  L = self.metad['L']
  if L in self.Ldict:
   print("Entry init error: duplicate L",L,linenum1)
   exit(1)
  self.Ldict[L] = self
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
 text = ' '.join(entry.datalines)
 if option == 'pw':
  lsarr = get_ls_pw(text)
 else:
  lsarr = get_ls_ab(text,option)
 if False: # dbg
  L = entry.metad['L']
  if L == '2':
   print('chk',L,'\n'.join(lsarr))
 entry.lsarr = lsarr

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

class PWBIB(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  p = line.split('\t')
  assert len(p)== 4
  self.ident,self.abbr,self.lslow,self.tooltip = p
  self.instances = []

def init_pwbib(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  recs = [PWBIB(line) for line in f]
 print(len(recs),"pwbib read from",filein)
 # check for duplicate idents
 d = {}
 for irec,rec in enumerate(recs):
  if rec.ident in d:
   print("ERROR: duplicate ident",rec.ident)
  d[rec.ident] = True
 return recs

def find_abbr(lsbody,abbrs):
 """ abbrs assumed sorted by descending length of abbreviation. 
  Find the longest abbreviation that starts lsbody.
  This is the FIRST abbreviation that starts lsbody
 """
 for abbr in abbrs:
  if lsbody.startswith(abbr.abbr):
   return abbr
 #print('find_abbr error. lsbody=',lsbody)
 return None

def update_abbrs(line,abbrs1):
 for m in re.finditer(r'<ls>([^0-9].*?)</ls>',line):
  ls = m.group(1)
  if ls.startswith('II,'): #Similar to numeric
   continue
  if ls.startswith('S. '): #Similar to numeric (Seite = page)
   if not ls.startswith('S. S. S.'):
    continue
  pwbibrec = find_abbr(ls,abbrs1)
  if pwbibrec != None:
   pwbibrec.instances.append(ls)
   continue
  else:
   print('Unknown ls:',ls)
   
def write_abbrs(fileout,abbrs):
 outarr = []
 for abbr in abbrs:
  count = len(abbr.instances)
  outarr.append('; ------------------------------------')
  outarr.append("; %s %s" %(abbr.abbr,count))
  outarr.append('; ------------------------------------')
  instances = sorted(abbr.instances)
  for x in instances:
   outarr.append(x)
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out+'\n')
 print(len(outarr),"records written to",fileout)

def write_pwbib(fileout,recs):
 outarr = []
 for rec in recs:
  out = '\t'.join([rec.ident,rec.abbr,rec.lslow,rec.tooltip])
  outarr.append(out) 
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out+'\n')
 print(len(outarr),"records written to",fileout)


if __name__=="__main__":
 #test_make_ls()
 option = 'pw'
 assert option in ['pw','ab','ab1']  # Cologne or Andhrabharti version
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx
 filebib = sys.argv[2]  # pwbib_input.txt
 fileout = sys.argv[3] #
 entries = init_entries(filein)

 abbrs = init_pwbib(filebib)

 abbrs1 = sorted(abbrs , key = lambda x : len(x.abbr),reverse=True)
 
 for entry in entries:
  for line in entry.datalines:
   update_abbrs(line,abbrs1)
 # sort abbreviations for printing
 abbrs_sort = sorted(abbrs,key = lambda x : x.abbr)
 write_abbrs(fileout,abbrs_sort)
