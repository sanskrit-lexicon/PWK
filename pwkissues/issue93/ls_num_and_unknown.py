#-*- coding:utf-8 -*-
""" ls_num_and_unknown.py  list the details 
"""
import sys,re,codecs
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec cannot encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 

class LSCase(object):
 def __init__(self,ls,abbrev,metaline,iline,line):
  self.ls = ls
  self.abbrev = abbrev
  self.metaline = metaline
  self.iline = iline
  self.line = line
  self.parmstr = ls[len(abbrev):].strip()
  if self.parmstr == '':
   self.nparms = 0
  else:
   self.nparms = len(self.parmstr.split(' '))
  self.len = len(self.parmstr)
  
def lscase_out(lscase,ilscase):
 outarr = []
 case = ilscase + 1
 #outarr.append('; TODO Case %s: (reason = %s)' % (case,lscase.reason))
 try:
  ident = re.sub(r'<k2>.*$','',lscase.metaline)
 except:
  print('ERROR:',lscase.iline,lscase.old)
  exit(1)
 if ident == None:
  ident = lscase.page
 outarr.append('; %s' % ident)
 outarr.append('; problem with: %s' %lscase.ls)
 lnum = lscase.iline + 1
 line = lscase.line
 new = line
 outarr.append('%s old %s' % (lnum,line))
 outarr.append('; correction: ?')
 outarr.append('%s new %s' % (lnum,new))
 outarr.append(';--------------------------------------------------')
 # dummy next line
 return outarr

def write_lscases(fileout,lscases):
 with codecs.open(fileout,"w","utf-8") as f:
   for idx,lscase in enumerate(lscases):
    outarr = lscase_out(lscase,idx)
    for out in outarr:
     f.write(out+'\n')
 print(len(lscases),"cases written to",fileout)

class Tooltip(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  # pwg has code, abbrevUpper, abbrevLower,tip
  self.code,self.abbrev,self.abbrevlo,self.tip = line.split('\t')
  self.total = 0
  
def init_tooltip(filein):
 with codecs.open(filein,"r","utf-8") as f:
  ans = [Tooltip(x) for x in f]
 print(len(ans),'tooltips from',filein)
 return ans

def dfirstchar(tooltips_sorted):
 d = {}
 for tip in tooltips_sorted:
  c = tip.abbrev[0]
  if c not in d:
   d[c] = []
  d[c].append(tip)
 return d

def findtip(ls,tiplist):
 for tip in tiplist:
  if ls.startswith(tip.abbrev):
   return tip
 return None

def count_tips(lines,tipd,numbertip,unknowntip):
 #
 lscases = []  # return array of LSCase objecct
 metaline = None
 imetaline1 = None
 page = None
 for iline,line in enumerate(lines):
  if iline == 0: # %***This File is E:\\APTE.ALL, Last update 11.09.06 
   continue  # 
  line = line.rstrip('\r\n')
  if line == '':
   continue
  if line.startswith('<L>'):
   metaline = line
   imetaline1 = iline+1
   entry = [] # list of LSCase appearing in this entry
   continue
  if line == '<LEND>':
   if len(entry)>0:
    lsentries.append(entry)
    # 
   metaline = None
   imetaline = None
   continue
  if line.startswith('[Page'):
   page = line
   continue
  for m in re.finditer(r'<ls([^>]*)>([^<]*)</ls>',line):
   attrib = m.group(1)
   elt = m.group(2)
   if len(elt) == 0:
    print('WARNING at line %s %s' % (iline+1,metaline))
    print('ls = ',m.group(0))
    tip = unknowntip
    tip.total = tip.total + 1
    continue
   m1 = re.search(r' +n="(.*?)"',attrib)
   if m1 != None:
    nval = m1.group(1)
    elt = nval + ' ' + elt
   if re.search(r'^[0-9]',elt): # number
    tip = numbertip
   elif elt[0] not in tipd:
    tip = unknowntip
   else:
    tiplist = tipd[elt[0]]
    tip  = findtip(elt,tiplist)
    if tip == None:
     tip = unknowntip
   # found a match
   if not (tip in (unknowntip,numbertip)):
    continue  # only interested in unknown or number tips
   lscase = LSCase(elt,tip.abbrev,metaline,iline,line)
   lscases.append(lscase)
 
 print(len(lscases),'cases found')
 return lscases

if __name__=="__main__":
 
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 filetip = sys.argv[2] # pwgbib_input.txt
 fileout = sys.argv[3] # output summary
 tips0 = init_tooltip(filetip)
 tips = sorted(tips0,key = lambda tip: len(tip.abbrev),reverse=True)
 tipd = dfirstchar(tips)
 # dummy for number
 numbertip = Tooltip("9.1\tNUMBER\tnumber\tls starts with number")
 # dummy for unknown
 unknowntip = Tooltip("9.2\tUNKNOWN\tunknown\tls is unknown")
 
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 lscases = count_tips(lines,tipd,numbertip,unknowntip) 
 write_lscases(fileout,lscases)
 
