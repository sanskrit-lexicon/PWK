# coding=utf-8
""" init_bbmulti.py
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 print(len(lines),"from",filein)
 return lines

def write_lines(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for out in lines:
   f.write(out+'\n')  
 print(len(lines),"lines written to",fileout)

class Rec:
 def __init__(self,lnum,ndeva,beforea,before,root):
  self.lnum = lnum
  self.ndeva = ndeva
  self.beforea = beforea
  self.before = before # not used
  self.root = root  # boolean
  
def write_recs(fileout,recs):
 outarr = [] # header
 for rec in recs:
  lnum1 = str(rec.lnum)
  ndeva1 = str(rec.ndeva)
  if rec.root:
   ndeva1 = ndeva1 + '√'
  #out = '\t'.join((lnum1,ndeva1,rec.beforea,rec.before))
  out = '\t'.join((lnum1,ndeva1,rec.beforea))
  outarr.append(out)
 write_lines(fileout,outarr)

def before_simplify(x):
 x = re.sub(r'\([^#]*\)', ' ',x)
 x = x.replace('ʼs','')
 x = re.sub(r'\[Page.*?\]', ' ', x)
 x = re.sub(r'{%[^%#]*%}', ' ', x)
 x = re.sub(r'<ab>[^<]*</ab>',' ',x)
 x = re.sub(r'<ls>[^<]*</ls>',' ',x)
 x = re.sub(r'<ls n=".*?">[^<]*</ls>',' ',x)
 x = re.sub(r'<ab n=".*?">[^<]*</ab>',' ',x)
 x = re.sub(r'<lex>[^<]*</lex>',' ',x)
 x = re.sub(r'<is>[^<]*</is>',' ',x)
 x = re.sub(r'<arab>[^<]*</arab>',' ',x)
 x = re.sub(r'<lang>[^<]*</lang>',' ',x)
 x = re.sub(r' und ',' ',x)
 x = re.sub(r' oder ',' ',x)
 x = re.sub(r'[!√,.?=;]','',x)
 # x = re.sub(r'\(wohl *\', r'(',x
 x = re.sub(r'  +',' ',x)
 x = x.replace('( ','(')
 x = x.replace(' )',')')
 x = re.sub(r'\(({#[^#]*#})\)',r'\1',x)
 x = re.sub(r'  +',' ',x)
 #x = x.replace('( *)',' ')
 x = re.sub(r'\( *\)',' ',x)
 x = re.sub(r'  +',' ',x)
 x = re.sub(r'#}[^#]*$','#}',x)
 words = ['(stark ', '(oder ', '(wohl ', '(in ', '(zu ',
              '(eine ', '(auch ', '(schwach ', '(richtig ', '(lies ',
              '(von ', '(nicht ', '(für ', '(wo ', '(mit der ',
              '(metrisch für ', '(so Index statt ', '(Am Ende eines ',
              '(defectiv ',
              '(nur in der ältesten Sprache nur in den Formen ',
              ' in der) ',
              ]
 for word in words:
   x = x.replace(word,'')
 x = re.sub(r'[()]','',x)
 x = re.sub(r'  +',' ',x) 
 return x

def init_recs(lines):
 errfile = 'temp_bbmulti_errors.txt'
 outerr = []
 recs = []
 n = 0 # sum of ndevas before broken bar
 nroots = 0
 for iline,line in enumerate(lines):
  if '¦' not in line:
   continue
  try:
   before,after = line.split('¦')
  except:
   lnum = iline + 1
   metaline = lines[iline-1]
   outerr.append('; %s' % metaline)
   outerr.append('%s old %s' %(lnum,line))
   outerr.append('%s new %s' %(lnum,line))
   outerr.append(';')
   continue
  devas = re.findall('{#',before)
  ndevas = len(devas)
  if ndevas < 2:
   continue
  lnum = iline + 1
  beforea = before_simplify(before)
  root = ('√' in before)
  if root:
   nroots = nroots + 1
  rec = Rec(lnum,ndevas,beforea,before,root)
  n = n + ndevas
  recs.append(rec)
 if len(outerr) != 0:
  write_lines(errfile,outerr)
 print(n,"count of all {#X#} before ¦")
 print(nroots,'records marked as √')
 return recs

def check_recs(recs):
 for rec in recs:
  pass
 
if __name__=="__main__":
 filein = sys.argv[1]  # pw.txt
 fileout = sys.argv[2]  # change file 

 lines = read_lines(filein)
 recs = init_recs(lines)
 write_recs(fileout,recs)
 check_recs(recs)
 
