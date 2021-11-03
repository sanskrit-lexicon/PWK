#-*- coding:utf-8 -*-
"""diffls4a.py  
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

L_assert_ok =[
"1192" ,"4919" ,"5783" ,"5784" ,"18875" ,
"21063" ,"21524" ,"22308" ,"23792" ,"27986" ,
"28511" ,"31882" ,"39320" ,"41631" ,"45079" ,
"47235" ,"54778" ,"55732" ,"61671" ,"63230" ,
"69108" ,"69474" ,"72438" ,"83546" ,"91142" ,
"92045" ,"94635" ,"104556" ,"106503" ,"116498" ,
"120998" ,"121214",
# and a few more
 "6919","96906", "123891",
 "44487", "112945","131519", "134797",
# more from diffls4
 "2514", "2711", "3347", "3486",  "5444",
 "5635", "6478", "7434", "7859", "8624", 
 "9946", "10039", "10854", "17476", "20341", 
 "20386", "20885", "23118", "23902", "24728", 
 "24737", "28004", "28343", "29500", "31095", 
 "31948", "32272", "34418", "37314", "37842", 
 "40817", "40981", "41215", "42736", "45037", 
 "47065", "49511", "50420", "50491", "51552", 
 "52136", "53447", "54574", "55874", "", 
 "", "", "", "", "", 
 "", "", "", "", "", 
 "", "", "", "", "", 
 "", "", "", "", "", 
 "", "", "", "", "", 
 "", "", "", "", "", 
 "", "", "", "", "", 
 
 ]

def lseqF(x,y):
 return (not surely_different(x,y))

def write_diff_any_N(fileout,entries1,entries2):
 # change transaction lines for cases where no ls refs in pw (entries1)
 nok = 0 # number that are OK by virtue of L_assert_ok
 dont_print_ok = True
 if dont_print_ok:
  print("WARNING: Not printing 'OK' records")
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
  if False:  # we include ALL differences
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
  if L in L_assert_ok:
   out = out + ' OK'
   nok = nok + 1
   if dont_print_ok:
    continue
  outarr.append(out)
  if True:
   ndiff = ndiff + 1
   outarr = []
   outarr.append('; <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
   outarr.append(out)
   #outarr.append('; pw: %s' % lsarr1[0])
   #nlsmax = max(n1,n2)
   matches,pwnonmatches,abnonmatches = merge(lsarr1,lsarr2,lseqF)
   """
   for ls in lsarr1:
    outarr.append('; pw: %s' % ls)
   for ls in lsarr2:
    outarr.append('; ab: %s' % ls)
   """
   for ls1,ls2 in matches:
    outarr.append('; pw: %s  ~= ab: %s' %(ls1,ls2))
   outarr.append('; NON-matches')
   for ls1 in pwnonmatches:
    outarr.append('; pw: %s' % ls1)
   for ls2 in abnonmatches:
    outarr.append('; ab: %s' % ls2)
   # now the pw entries
   for iline,line in enumerate(entry1.datalines):
    lnum = entry1.linenum1 + iline + 1
    #line = entry1.datalines[iline]
    outarr.append('%s old %s' %(lnum,line))
    outarr.append('%s new %s' %(lnum,line))
    outarr.append(';')
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
 print(ndiff,'different ls cases')
 print(nok,'of these are ok by assertion')
 print('leaving',ndiff-nok,'differences to re-investigate')

def match_helper_v0(a,b,a_used,b_used):
 a_match = []
 for i,x in enumerate(a):
  b_avail = [j for j in range(len(b)) if (not b_used[j]) and (x == b[j])]
  if b_avail == []:
   # x not matched
   a_match.append(None)
  else:
   # use first match
   j = b_avail[0]
   a_match.append(j)
   a_used[i] = j
   b_used[j] = i
 return a_match

def merge_v0(a,b):
 """ a,b are lists
 Return a list of pairs 
 Example:
  a = [1,5]  b = [2,1]  
   ans = [[None,2],[1,1],[5,None]]
  a[0] == b[1], a[1] not in b,  b[0] not in a
  
  c = [[0,1] , [1,None]]  
  d = [[0,
 """
 ans = []
 #na = len(a)
 #nb = len(b)
 a_used = [None for x in a] # subscripts of a that match
 b_used = [None for x in b]
 #a_match = [None for x in a]
 a_match = match_helper_v0(a,b,a_used,b_used)
 b_match = match_helper_v0(b,a,b_used,a_used)
 if True:
  print('a=',a)
  print('b=',b)
  print('a_match=',a_match)
  print('b_match=',b_match)
  print('a_used=',a_used)
  print('b_used=',b_used)

def match_helper(a,b,a_used,b_used,eqF):
 #a_match = []
 for i,x in enumerate(a):
  b_avail = [j for j in range(len(b)) if (not b_used[j]) and eqF(x,b[j])]
  if b_avail == []:
   # x not matched
   #a_match.append(None)
   pass
  else:
   # use first match
   j = b_avail[0]
   #a_match.append(j)
   a_used[i] = j
   b_used[j] = i
 return #a_match

def merge(a,b,eqF):
 """ a,b are lists
 Return 3 lists:
  matches:  list of 2-tuples (x,y) from a,b with eqF(x,y) == True
 anonmatches: list of x in 'a' with no matches in 'b'
 bnonmatches: list of y in 'b' with no matches in 'a'
 """
 ans = []
 a_used = [None for x in a] # subscripts of a that match
 b_used = [None for x in b]
 match_helper(a,b,a_used,b_used,eqF)
 match_helper(b,a,b_used,a_used,eqF)
 matches = []
 for i,j in enumerate(a_used):
  if j != None:
   matches.append((a[i],b[j]))
 anonmatches = []
 for i,j in enumerate(a_used):
  if j == None:
   anonmatches.append(a[i])
 #nonmatches.append(('XX','YY'))
 bnonmatches = []
 for j,i in enumerate(b_used):
  if i == None:
   bnonmatches.append(b[j])
 return (matches,anonmatches,bnonmatches)
  
def test():
 # a1: [[0,1],[1,False],[2,2],[3,False]
 # b1: [[0,False],[1,0],[2,3]]
 # a[0],b[1]
 # a[3],b[2]
 # --
 # a[1]
 # a[2]
 # b[0]
 a = ['x','w','u','y']
 b = ['z','x','y']
 #merge_v0(a,b)
 def eqF(x,y):
  return (x == y)
 matches,anonmatches,bnonmatches = merge(a,b,eqF)
 if True:
  print('a=',a)
  print('b=',b)
  #print('a_used=',a_used)
  #print('b_used=',b_used)
  print('matches')
  for c,d in matches:
   print(c,d)
  print('non-matches')
  for c in anonmatches:
   print(c,'--')
  for d in bnonmatches:
   print('--',d)
 exit(1)
              
if __name__=="__main__":
 #test()
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
 write_diff_any_N(fileout,entries1,entries2)

