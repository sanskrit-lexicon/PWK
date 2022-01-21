#-*- coding:utf-8 -*-
"""make_change_ls.py
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

class Change(object):
 def __init__(self,metaline,lnum,old,new):
  self.metaline = metaline
  self.lnum = lnum
  self.old = old
  self.new = new

def init_strings(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  stringlist = [line.rstrip('\r\n') for line in f]
  stringset = set(stringlist) # handles duplicates, if any
 print(len(stringset),"strings read from",filein)
 return stringset

def change_ls_matching_given(line,stringset):
 def f(m):
  ans = m.group(0)
  ls = m.group(1)
  if ans in stringset:
   ans = '<ls>[%s]</ls>'%ls
  return ans
 newline = re.sub(r'<ls>(.*?)</ls>',f,line)
 return newline

def write_changes(fileout,changes):
 outrecs = []
 for change in changes:
  outarr = []
  outarr.append('; -------------------------------------')
  outarr.append('; ' + change.metaline)
  outarr.append('%s old %s' %(change.lnum,change.old))
  outarr.append('; ')
  outarr.append('%s new %s' %(change.lnum,change.new))
  outrecs.append(outarr)
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(outrecs),"records written to",fileout)

def change_ls_matching_given_1(line):
 m = re.search(r'<ls>Spr.</ls>',line)
 if m == None:
  return False,line
 return True,line

def change_ls_matching_given_2(line):
 newline = re.sub(r'<ls>Spr. ([0-9]+[.]) ([0-9]+[.]?)</ls>',
                r'<ls>Spr. \1</ls> <ls n="Spr.">\2</ls>',line)
 flag = not (newline == line)
 return flag,newline

def change_ls_matching_given_3(line):
 newline = re.sub(r'<ls>Spr. ([0-9]+[.]) ([0-9]+[.]) ([0-9]+[.]?)</ls>',
                r'<ls>Spr. \1</ls> <ls n="Spr.">\2</ls> <ls n="Spr.">\3</ls>',line)
 flag = not (newline == line)
 return flag,newline

data4raw = """
<ls>Spr. 40. fg. 1879. fg.</ls> akftya 200
<ls>Spr. 139. fg. 7722.</ls> atiparicaya 1834
<ls>Spr. 7620,7828.</ls> atri 2346
<ls>Spr. 318. fg. 4059. 4525.</ls> anubanDa 4652
<ls>Spr. 7646 .7732.</ls> antar 5210
<ls>Spr. 7826, N.</ls> anDas 5521
<ls>Spr. 7861,d.</ls> kalADara 25469
<ls>Spr. 7861,b.</ls> kalADara 25469
<ls>Spr. 76,77</ls> pad 62714
<ls>Spr. 3981. fgg. 7718.</ls> paropakAra 64601
<ls>Spr. 78,25.</ls> pratizWa 71584
<ls>Spr. 7750,7770.</ls> yA 90611
"""
def get_data4():
 lines1 = data4raw.splitlines()
 lines = []
 for line in lines1:
  line = line.strip()
  if line == '':
   continue
  line = re.sub('</ls>.*$','</ls>',line)
  lines.append(line)
 return lines

data4list = get_data4()
#for x in data4list:
# print(x)
 
def change_ls_matching_given_4(line):
 #print(len(data4list))
 #exit(1)
 for ls in data4list:
  if ls in line:
   return True,line
 return False,line

if __name__=="__main__":
 option = sys.argv[1]
 filein = sys.argv[2] #  xxx.txt (path to digitization of xxx
 fileout = sys.argv[3] # change_X
 
 entries = init_entries(filein)
 fname = 'change_ls_matching_given_%s' % option
 changef = locals()[fname]
 changes = []  # list of change records
 for entry in entries:
  for iline,line in enumerate(entry.datalines):
   flag,newline = changef(line)
   if flag: #
    lnum = entry.linenum1+iline+1
    metaline = re.sub(r'<k2>.*$','',entry.metaline)
    change = Change(metaline,lnum,line,newline)
    changes.append(change)

 write_changes(fileout,changes)
 
