#-*- coding:utf-8 -*-
"""change1.py  IAST Spelling changes in sch.txt
 
"""
import sys,re,codecs
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec cannot encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 
class Change(object):
 def __init__(self,metaline,page,iline,old,new,reason,iline1,line1,new1):
  self.metaline = metaline
  self.page = page
  self.iline = iline
  self.old = old
  self.new = new
  self.reason = reason
  self.iline1 = iline1
  self.line1 = line1
  self.new1 = new1
def change1(line):
 reason = 'marked'
 if '</ls>' not in line:
  return reason,line
 newline = re.sub(r'</ls>(-[0-9]+)',r'\1</ls>',line)
 newline = re.sub(r'</ls>-(-[0-9]+)',r'\1</ls>',newline)
 return reason,newline

def old_init_changes(lines,tooltips0):
 known_abbrevs = ['P.']
 tooltips1 = [tip for tip in tooltips0 if tip.abbrev in known_abbrevs]
 tooltips = sorted(tooltips1,key = lambda tip: len(tip.abbrev),reverse=True)
 for tip in tooltips[0:10]:print(tip.abbrev)
 
 changes = [] # array of Change objects
 metaline = None
 imetaline1 = None
 page = None
 regex_split = re.compile(r'({#.*?#})|(<ls>.*?</ls>)')
 regex_replacenew = r'<ls>\1</ls>' # re.compile(r'<ls>\1<ls>')
 # regex for Panini (P.)
 regex_replaceold_P = re.compile(r'(P[.] +[IV]+[.] +[0-9]+[.] +[0-9]+[.]?)')
 #regex_replaceold_P = re.compile(r'(P[.] +[IV]+[.] +[0-9]+[.] +[0-9]+[.]? [0-9VI .;?]+)')
 for iline,line in enumerate(lines):
  #if iline == 260: print('dbgstart:',line)
  if iline == 0: # %***This File is E:\\APTE.ALL, Last update 11.09.06 
   continue  # 
  line = line.rstrip('\r\n')
  if line == '':
   continue
  if line.startswith('<L>'):
   metaline = line
   imetaline1 = iline+1
   continue
  if line == '<LEND>':
   metaline = None
   imetaline = None
   continue
  if line.startswith('[Page'):
   page = line
   continue
  #if imetaline1 == iline:
  #assert '¦' in line  # check
  #continue
  if line.startswith('[Page'):
   continue
  if '.' not in line:
   # all tooltip abbreviations contain a period.
   continue
  #newline = line.rstrip()  # remove trailing spaces
  #if iline == 260: print('dbg:oldline:',line)
  newline = line
  found = False
  for tip in tooltips:
   ab = tip.abbrev
   parts = re.split(regex_split,newline)
   newparts = []
   if ab != 'P.':
    continue
   else:
    regex_replaceold = regex_replaceold_P
   for part in parts:
    newpart = part
    if part == None:
     newpart = ''
    elif part.startswith('{#'):
     pass
    elif part.startswith('<ls>'):
     pass
    elif ab not in part:
     pass
    else:  
     newpart = re.sub(regex_replaceold,regex_replacenew,part)
    newparts.append(newpart)
   newline = ''.join(newparts) # end of tooltips loop
  #if iline == 260: print('dbg:newline=',line)
  if newline == line:
   continue
  # generate a change
  iline1 = None
  line1 = None
  newline1 = None
  reason = ''
  change = Change(metaline,page,iline,line,newline,reason,iline1,line1,newline1)

  changes.append(change)
 print(len(changes),'potential changes found')
 return changes

def change_out(change,ichange):
 outarr = []
 case = ichange + 1
 #outarr.append('; TODO Case %s: (reason = %s)' % (case,change.reason))
 try:
  ident = '%s  (reason = %s)' %(change.metaline,change.reason)
 except:
  print('ERROR:',change.iline,change.old)
  exit(1)
 if ident == None:
  ident = change.page
 outarr.append('; ' + ident)
 # change for iline
 lnum = change.iline + 1
 line = change.old
 new = change.new
 outarr.append('%s old %s' % (lnum,line))
 outarr.append('%s new %s' % (lnum,new))
 outarr.append(';')
 #change for iline1
 if False:
  lnum = change.iline1 + 1
  line = change.line1
  new = change.new1
  outarr.append('%s old %s' % (lnum,line))
  outarr.append('%s new %s' % (lnum,new))
  outarr.append(';')

 # dummy next line
 return outarr

def write_changes(fileout,changes):
 with codecs.open(fileout,"w","utf-8") as f:
   for ichange,change in enumerate(changes):
    outarr = change_out(change,ichange)
    for out in outarr:
     f.write(out+'\n')
 print(len(changes),"possible changes written to",fileout)

def write_changes(fileout,changes):
 # aggregate via reason
 aggs = {}
 for change in changes:
  reason = change.reason
  if reason not in aggs:
   aggs[reason] = []
  aggs[reason].append(change)
 
 with codecs.open(fileout,"w","utf-8") as f:
  reasons = aggs.keys()
  nchanges = 0
  for reason in reasons:
   changes1 = aggs[reason]
   f.write('; --------------------------------------------------------------\n')
   #f.write(';  iast = %s, %s instances\n' %(reason,len(changes1)))
   f.write(';  iast = %s\n' % reason)
   f.write('; --------------------------------------------------------------\n')
   for ichange,change in enumerate(changes1):
    outarr = change_out(change,ichange)
    for out in outarr:
     f.write(out+'\n')
   nchanges = nchanges + len(changes1)
 print(nchanges,"possible changes written to",fileout)

class Tooltip(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  parts = re.split(r' += ',line)
  if len(parts) != 2:
   print('problem parsing tooltip')
   print(line)
   print(parts)
   exit(1)
  self.abbrev,self.tip = parts
  self.nabbrev = 0
  
def init_tooltip(filein):
 with codecs.open(filein,"r","utf-8") as f:
  ans = [Tooltip(x) for x in f]
 print(len(ans),'tooltips from',filein)
 return ans

def init_changes(lines,Lcases):
 changes = [] # array of Change objects
 metaline = None
 nabbrev = 0  # number of abbreviations marked
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   metaline = line
   m = re.search(r'<L>(.*?)<',metaline)
   L = m.group(1)
   continue
  if line.startswith('<LEND>'):
   metaline = None
   continue
  if line.startswith('[Page'):
   page = line
   continue
  if metaline == None:
   continue
  if L not in Lcases:
   continue
  iast = Lcases[L]
  if iast not in line:
   print('Warning: ',iast,'NOT IN',line)
   continue
  # generate a Change instance
  # remove hyphen phrase in line
  newline = line
  # insert the hyphen in next line
  iline1 = None #iline + 1
  line1 = None #lines[iline1]
  newline1 = None
  reason = iast
  change = Change(metaline,page,iline,line,newline,reason,iline1,line1,newline1)  
  changes.append(change)
 return changes

def init_L_cases():
 textlines = """
L=1562 iast = aduḥspṛṣta
L=2295 iast = anākāṅksya
L=3302 iast = apadāñta
L=3332 iast = ápapivāms
L=3775 iast = ápratiṣthāyuka
L=4155 iast = abhiruḍgatā
L=4223 iast = abhíhotavái
L=4531 iast = amṇās
L=5057 iast = alaksmīka
L=5317 iast = avapṛṣthī
L=5714 iast = avṛṣtikāma
L=6274 iast = asiyasṭi
L=7048 iast = Ā̀́pāṣṭhi
L=7150 iast = Ā̀́mitraśocani
L=7155 iast = āmūṛdhāntam
L=7218.1 iast = ā̀̀ra
L=7636 iast = inḍindirā
L=7686 iast = indranīlamaṇimaya=indranīlamaya
L=7774 iast = Íṣvāśanī
L=8239 iast = udakya=udaśyāmāka
L=11923 iast = Kkuḍula
L=12492 iast = goḷikā
L=13803 iast = jáḷhu
L=15048 iast = dakṣiṇata-upacāra
L=15071 iast = daksiṇottara
L=15549 iast = durvyavahṛṣti
L=17152 iast = niṣpūtigaṇdhika
L=19737 iast = prāṇmukhāñcana
L=22941 iast = luñcālunca
L=23490 iast = vāpan;
L=24175 iast = viśvadrśvan
L=24295.1 iast = vihaṅgikā
L=24969 iast = śā(ate)
L=27766 iast = adhvmukha
""".splitlines()
 d = {}
 for line in textlines:
  line = line.rstrip('\r\n')
  line = line.strip()
  if line == '':
   continue
  m = re.search(r'^L=(.*?) iast = (.*)$',line)
  L = m.group(1)
  iast = m.group(2)
  if L in d:
   print('Unexpected duplicate L',line)
  d[L] = iast
 return d
  
if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] # possible change transactions
 Lcases = init_L_cases()
 
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 # lines = lines  # for later comparison
 changes = init_changes(lines,Lcases)
 write_changes(fileout,changes)
