# coding=utf-8
""" summary.py for bot
"""
from __future__ import print_function
import sys, re,codecs
import digentry  

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines_simple(fileout,outarr,printFlag=True):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    #if out == None:
    # out = '?'
    f.write(out+'\n')
 if printFlag:
  print(len(outarr),"lines written to",fileout)

def write_recs_1_standard(fileout,recs):
 # recs is list of Inrec objects
 outarr = []
 for rec in recs:
  if rec.status != 'STANDARD':
   continue
  ireg = rec.ireg
  m = rec.m
  #parms = (rec.genus,rec.species,rec.auth)
  #parmstr = '(%s,%s,%s)' % parms
  rec1 = (rec.L,rec.k1,rec.lnum,rec.bot)
  out = '\t'.join(rec1)
  outarr.append(out)
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"cases written to",fileout)

def write_recs_1_nonstandard(fileout,recs):
 # recs is list of Inrec objects
 outarr = []
 for rec in recs:
  if rec.status != 'TODO':
   continue
  rec1 = (rec.L,rec.k1,rec.lnum,rec.bot)
  out = '\t'.join(rec1)
  outarr.append(out)
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"cases written to",fileout)

def write_recs_2(fileout,recs):
 # recs is list of Inrec objects
 outarr = []
 recs1 = [rec for rec in recs if rec.status == 'STANDARD']
 # establish
 d = {}
 for rec in recs1:
  ireg = rec.ireg
  if ireg == 0:
   key = (0,0,0)
  else:
   key = (rec.d1,rec.d2,rec.d3)
  if key not in d:
   d[key] = []
  d[key].append(rec)
 keys = d.keys()
 keys1 = sorted(keys)
 for key in keys1:
  n = len(d[key])
  parmstr = '(%s,%s,%s)' % key
  out = '%s\t%s' %(parmstr,n)
  outarr.append(out)
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"cases written to",fileout)

def write_recs_3(fileout,recs):
 # recs is list of Inrec objects
 # aggregate on auth
 outarr = []
 #recs1 = [rec for rec in recs if rec.status == 'STANDARD']
 recs1 = recs
 #
 d = {}
 for rec in recs1:
  key = rec.auth
  if key == None:
   key = '_None'
  if key not in d:
   d[key] = []
  d[key].append(rec)
 keys = d.keys()
 keys1 = sorted(keys,key = lambda x: x.lower())
 for key in keys1:
  n = len(d[key])
  parmstr = key
  out = '%s\t%s' %(parmstr,n)
  outarr.append(out)
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"cases written to",fileout)

def write_recs_3a(fileout,recs,showknown):
 # recs is list of Inrec objects
 outarr = []
 # only records with an auth field
 recs1 = [rec for rec in recs if rec.auth != None]
 # sort by (rec.auth, rec.ilnum)
 recs2 = sorted(recs1, key = lambda rec: (rec.auth, rec.ilnum))
 for rec in recs2:
  if rec.auth == None:
   # no author. skip
   continue
  # record has an author
  if showknown and (not rec.auth_known):
   continue
  if (not showknown) and rec.auth_known:
   continue
  rec1 = (rec.L,rec.k1,rec.lnum,rec.bot)
  out = '\t'.join(rec1)
  outarr.append(out)
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"cases written to",fileout)


def check_standarda(bot,sregs):
 used = []
 for ireg,sreg in enumerate(sregs):
  m = re.search(sreg,bot)
  if m:
   used.append((m,ireg))
 flag = (len(used) == 1)
 if flag:
  m,ireg = used[0]
 else:
  m,ireg = None,-1
 return flag,m,ireg


def get_all_regexes():
 regexraws = [
  r'<bot.*?</bot>'
 ]
 regexes = list(map(re.compile,regexraws))
 return regexes,regexraws

def findall_bot_entries(entries,regexes):
 nregex = len(regexes)
 recs = []
 counts = {}
 for i in range(nregex):
  counts[i] = 0
 dups = [] # lines with duplicate bot
 for ientry,entry in enumerate(entries):
  #text = ' '.join(entry.datalines)
  L = entry.metad['L'] # the entry id
  k1 = entry.metad['k1'] # the entry id
  linenum1 = entry.linenum1
  for idx,line in enumerate(entry.datalines):
   lnum = linenum1 + idx + 1
   d = {}
   vals = []
   dupflag = False
   counts_line = {}
   for iregex,regex in enumerate(regexes):
    a = re.findall(regex,line)
    for x in a:
     val = (L,k1,lnum,x)
     vals.append(val)
     if iregex not in counts_line:
      counts_line[iregex] = 0
     counts_line[iregex] = counts_line[iregex] + 1
     if val in d:
      dupflag = True
      break
     d[val] = True
    if dupflag:
     dups.append((lnum,val))
     continue
   for val in vals:
    (L,k1,lnum,x) = val
    rec = Inrec(L,k1,str(lnum),x)
    recs.append(rec)
   for iregex in counts_line:
    counts[iregex] = counts[iregex] + counts_line[iregex]
 print('%s instances of bot' % len(recs))
 print('findall_bot_entries: number of lines with duplicates=',len(dups))
 for dup in dups:
  lnum,val = dup
  (L,k1,lnum1,x) = val
  assert lnum == lnum1
  print('duplicate: L=%s, k1=%s, lnum=%s, bot=%s' %(L,k1,lnum,x))
 return recs,counts 

def get_standard_regexes():
 # not 'auth' can be several 'words'
 regexraws = [
  r'<bot>([A-Z][^ ]+) ([a-z][^ ]+)</bot>', # Genus species
  r'<bot>([A-Z][^ ]+) ([a-z][^ ]+) (.*?)</bot>', # Genus species auth
 ]
 regexes = list(map(re.compile,regexraws))
 return regexes,regexraws

class Inrec:
 def __init__(self,L,k1,lnum,bot):
  #self.line = line
  #parts = line.split('\t')
  #self.parts = parts
  self.L = L
  self.k1 = k1
  self.lnum = lnum # string,
  self.ilnum = int(self.lnum)
  self.bot = bot
  self.status = 'TODO'
  self.m = None
  self.ireg = None
  self.genus = None
  self.species = None
  self.auth = None
  self.auth_known = False

def classify(allrecs):
 sregs, sregraws = get_standard_regexes()
 for irec,rec in enumerate(allrecs):
  flag,m,ireg = check_standarda(rec.bot,sregs)
  if not flag:
   assert rec.status == 'TODO'
   continue
  # rec is standard
  rec.status = 'STANDARD'
  rec.m = m
  rec.ireg = ireg
  if ireg == 0:
   rec.genus,rec.species = m.group(1),m.group(2)
   rec.auth = None
  elif ireg == 1:
   rec.genus,rec.species,rec.auth = m.group(1),m.group(2),m.group(3)

def init_known_auths(filein):
 lines = read_lines(filein)
 d = {}
 for line in lines:
  # line is 'auth,count'
  try:
   auth,count = line.split(',')
  except:
   continue # line not used
  if auth in d:
   print('init_known_auths duplicate:',auth)
  d[auth] = count
 return d

def mark_known(recs,dknown):
 n = 0
 for rec in recs:
  if rec.auth == None:
   continue # no auth
  rec.auth_known = (rec.auth in dknown)
  if rec.auth_known:
   n = n + 1
 print('mark_known finds %s records with known author' % n)
 
if __name__ == "__main__":
 option = sys.argv[1]
 filein = sys.argv[2] # xxx.txt
 entries = digentry.init(filein)
 allregs,allregsraw = get_all_regexes()
 # allrecs is list of Inrec objects
 allrecs,allcounts = findall_bot_entries(entries,allregs)
 classify(allrecs)
 if option == '1':
  fileout = sys.argv[3]
  fileout1 = sys.argv[4]
  write_recs_1_standard(fileout,allrecs)
  write_recs_1_nonstandard(fileout1,allrecs)
 elif option == '2':
  fileout = sys.argv[3]
  write_recs_2(fileout,allrecs)
 elif option == '3':
  fileout = sys.argv[3]
  write_recs_3(fileout,allrecs)
 elif option == '3a':
  filein1 = sys.argv[3]  # wcvp/temp_wcvp_auth.txt
  fileout = sys.argv[4]
  fileout1 = sys.argv[5]
  d = init_known_auths(filein1)
  print(len(d),"records kept from",filein1)
  mark_known(allrecs,d)

  write_recs_3a(fileout,allrecs,True) # all records with a known auth
  write_recs_3a(fileout1,allrecs,False) # all records with an unknown auth
 else:
  print('unknown option',option)

