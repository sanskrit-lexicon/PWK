# coding=utf-8
""" morealt.py
"""
from __future__ import print_function
import sys, re,codecs
#import digentry  

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for out in lines:
   f.write(out+'\n')  
 print(len(lines),"lines written to",fileout)

def write_recs(fileout,outrecs,printflag=True):
 # outrecs is array of array of lines
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
   out = ''  # blank line separates recs
   f.write(out+'\n')
 if printflag:
  print(len(outrecs),"records written to",fileout)

class CAND:
 def __init__(self,instance):
  metaline,nextline,nextlnum = instance
  self.metaline = metaline
  self.nextline = nextline
  self.nextlnum = nextlnum

def init_regexA():
 regexes = [
  r'^ <lex>Adj.</lex> \(<lex>f.</lex> {#[^#]*#}[^#]*$',
  r'^ <lex>Adj.</lex> von {#[^#]*#}[^#]*$',
  r'^ <lex>[^<]*</lex> = {#[^#]*#}[^#]*$',
  r'fehlerhaft',
  r'Fehlerhaft',
  r'^ <is>gaṇa</is> {#[^#]*#}[^#]',
  r'^ <lex>Adv.</lex> mit {#',
  r'^ <lex>[^<]*</lex> <ab>Nom. abstr.</ab> zu {#',
  r'^ <lex>[^<]*</lex> <ab>Nom. abstr.</ab> von {#',
  r'^ <ab>s.</ab> {#',
  r'^ <lex>Adj.</lex> in {#',
  r'^[^#]+<ab>Vgl.</ab> {#[^#]*#}[^#]*$',
  r'schlechte Schreibart für',
  r'{%eine <ab>best.</ab> Pflanze,%} = {#',
  r'Hypocoristicon of',
  r'^ in [*]?{#',
  r'^ <ab>Partic.</ab> von',
  r'^ <lex>[^<]*</lex> in {#',
  r'^ <ab>s. u.</ab> {#[^#]*#}[^#]*$',
  r'^ <ab>s. u.</ab> <hom>[^<]*</hom> {#[^#]*#}[^#]*$',
  r'^ <lex>Pron.</lex>',
 ]
 regexA = {}
 for i,regex in enumerate(regexes):
  iregex = i+1
  code = '%02d' % iregex  # assume < 100 regexes
  regexA[code] = regex
 return regexA

def init_regexB():
 regexes = [
  r'<ab>v. l.</ab> für {#',
  r'<ab>Patron.</ab> von {#',
  r'= {#',
  r'<ab>s\.</ab> {#',
  r'#} <ab>v\. l\.</ab>', 
  r'<ab>v\. l\.</ab> zu {#', 
  r'<ab>v\. l\.</ab> {#', 
  r'<is>gaṇa</is> {#', 
  r'<lex>f.</lex> zu {#', 
  r'<ab>Demin.</ab> von {#', 
  r'= {#', 
  r'= <hom>[^<]*</hom> {#', 
  r'<lex>Adj.</lex> zu {#', 
  r'<ab>Absol.</ab> mit {#',
  r'Richtig {#',
  r' in {#',
  r' [vV]on {#',
  r' Richtig[.]? (wohl|wäre) [*]?{#',
  r' Richtiger [*]?{#',
  r'#} {%enthaltend%}',
  r'von <hom>[^<]*</hom>',
  r'<ab>Nom.</ab> {#',
  r'<ab>[vV]gl.</ab> {#',
  r'<ab>[vV]gl.</ab> <ab n="unter">u.</ab> {#',
  r'<ab>(Superl.|Compar.|Pl.|Inf.)</ab> zu {#',
  r' [mM]it folgendem {#',
  r'{#[^#]+ ',
  r' anzunehmen für {#',
  r'<ab>[vV]gl.</ab> <hom>[^<]+</hom> {#',
  r'<lex>[^<]*</lex> mit {#',
  r'<ab>[^<]*</ab> mit {#',
  r' in Verbindung mit {#',
  r'^ mit {#',
  r' {%das Wort%} {#',
  r'^ .\. .\. {#',
  r' für {#',
  r'<ab>s.</ab> <hom>[^<]*</hom> {#',
  r'<ab>s. u.</ab> {#',
  r'<ab>Infin.</ab> zu <hom>[^<]*</hom> {#',
  r' nur {#',
  r' zu {#',
  r' <ab>s\. u\.</ab>',
  r'{%der Ausruf%} {#',
  r'{%mit dem Ausruf%} {#',
  r'mit%} {#',
  r'^ <lex>[^<]*</lex> {#',
  r'</ab> zu <hom>[^<]*</hom> {#',
  r'Laut%} {#',
  r'<ab>Nom. abstr.</ab> zu <hom>[^<]*</hom> {#',
 ]
 regexB = {}
 for i,regex in enumerate(regexes):
  iregex = i+1
  code = '%02d' % iregex  # assume < 100 regexes
  regexB[code] = regex
 return regexB

regexA = init_regexA()

regexB = init_regexB()

class CASES:
 def __init__(self,code,regex):
  self.code = code
  self.regex = regex
  self.instances = []  # (metaline,bbline,bblnum)

def init_cases(regexX):
 cases = []
 for code in regexX:
  case = CASES(code,regexX[code])
  cases.append(case)
 return cases

def match_cases(after,cases):
 for case in cases:
  code = case.code
  regex = case.regex
  if re.search(regex,after):
   return case
 return None

def morealt(lines):
 cands1 = []  # 
 cands2 = []
 casesA = init_cases(regexA)
 casesB = init_cases(regexB)
 for iline,line in enumerate(lines):
  if not line.startswith('<L>'):
   # line not a metaline.
   # newlines.append(line)
   continue
  # line is metaline
  # check for consistency with next line 
  iline1 = iline + 1
  line1 = lines[iline1]
  lnum1 = iline1 + 1 # line number of bbline (iline1)
  before,after = line1.split('¦')
  # skip if more than one {#X#} in before
  bwords = re.findall(r'{#[^#]*#}',before)
  if len(bwords) > 1:
   continue
  # skip if no {#X##} after
  awords = re.findall(r'{#[^#]*#}',after)
  nawords = len(awords)
  if nawords == 0:
   continue
  # skip if before marked as root
  if '√' in before:
   continue

  lnum1 = iline1 + 1
  instance = (line,line1,lnum1)
  caseA = match_cases(after,casesA)
  if caseA != None:
   caseA.instances.append(instance)
   continue
  
  caseB = match_cases(after,casesB)
  if (nawords == 1) and (caseB != None):
   caseB.instances.append(instance)
   continue
  # instance is a candidate for alternate headwords
  cand = CAND(instance)
  if nawords == 1:
   cands1.append(cand)
  else:
   cands2.append(cand)

 #print(len(cands),"candidates found")
 return cands1,cands2,casesA,casesB

def write_cases(fileout,cases,precond='None'):
 outrecs = []
 ntot = 0
 for case in cases:
  ntot = ntot + len(case.instances)
  
 for icase,case in enumerate(cases):
  outarr = []
  code = case.code
  regex = case.regex
  instances = case.instances
  ninstances = len(instances)
  if icase == 0:
   print('%d records written to %s' % (ntot,fileout))
   out = '; %d total instances written to %s' % (ntot,fileout)
   outarr.append(out)
  outarr.append('; ***************************************')
  outarr.append('; pre-condition: %s' % precond)
  outarr.append("; %5s NOALT regex[%s] = '%s'" % (ninstances,code,regex))
  outarr.append('; ***************************************')
  for instance in instances:
   metaline,bbline,bblnum = instance
   meta1 = re.sub(r'<k2>.*$','',metaline)
   outarr.append('; %s' % meta1)
   outarr.append('%s %s' % (bblnum,bbline))
   outarr.append(';')
  outrecs.append(outarr)
 write_recs(fileout,outrecs,printflag=False)
  
def write_candidates(fileout,cands):
 outrecs = []
 for c in cands:
  outarr = []
  outarr.append('; ' + c.metaline)
  outarr.append('%s %s' %(c.nextlnum,c.nextline))
  outarr.append(' ')
  outrecs.append(outarr)
 write_recs(fileout,outrecs)

if __name__=="__main__":
 filein = sys.argv[1]  # initial cdsl version pw.txt
 fileout1 = sys.argv[2]  # candidates1
 fileout2 = sys.argv[3]  # candidates1
 fileoutA = sys.argv[4]
 fileoutB = sys.argv[5]
 lines = read_lines(filein)
 print(len(lines),"lines read from",filein)

 # casesA - NOT an alt headword based on regex matching of ¦AFTER 
 # casesB - similarly, with the precondition that only one {#X#} in AFTER
 
 candidates1,candidates2,casesA,casesB = morealt(lines)
 write_candidates(fileout1,candidates1)
 write_candidates(fileout2,candidates2)
 write_cases(fileoutA,casesA)
 write_cases(fileoutB,casesB,precond='Exactly 1 Sanskrit after broken-bar')
