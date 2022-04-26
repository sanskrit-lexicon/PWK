#-*- coding:utf-8 -*-
"""ls2.py
 
"""
import sys,re,codecs

sys.stdout.reconfigure(encoding='utf-8')

otherlsnames = ['Ind. St.','Verz. d. B. H.','Verz. d. Oxf. H.',
                    'Wiener Z. f. d. K. d.','Wiener Zeitschr. f. d. K. d.',
                    'Mon. d. B. A.','Monatsb. d. B. A.',
                    'NÖLDEKE','VP.^2^', 'PA1N2INI^2^','LA^1^.',
                    'Procc. A. O. S.',
                    'phil.-hist. Kl. der Wiener Ak.',
                    'phil.-hist. Klasse der Wiener Ak.',
                    'phil.-hist. Kl. d. Wiener Ak.',
                    'Ind. Antiq.','Ind. Erb.','Ind. Str.', 
                     'Ind. Ind.', #?
                     'PAIPP.-Rec.','VALLABHI1-Gr.',
                    'S4A1RADA1-Hdschrr.).',
                    'MAITR. S.)'
                    ]
otherlsnames_parts = [re.split(r'()',x) for x in otherlsnames]

change_lsnames_text = """
"""

def get_change_lsnames():
 lines = change_lsnames_text.splitlines()
 d = {}
 for line in lines:
  line = line.rstrip('\r\n')
  if line.strip() == '':
   continue
  d[line] = True
 return d

class Change(object):
 def __init__(self,lnum,line,lsname,page):
  self.lnum = lnum
  self.line = line
  self.lsname = lsname
  self.page = page

def part_to_lsname(part):
 # part is the string following some <ls>
 # resolve line-breaks. By removing '-²' or '²'
 part = part.replace('-²','')  # THIS IS VERY TRICKY
 part = part.replace('²','')
 part = re.sub(r'[- ]\[Page.*?\]','',part) 
 lsparts = part.split(' ')
 lsheads = []
 for lspart in lsparts:
  if re.search(r"^[A-Z][A-Z0-9Ü-]*[.,]*('S)?$",lspart):
   lsheads.append(lspart)
  else:
   break
 lsname = ' '.join(lsheads)
 if lsname == '':
  for otherlsname in otherlsnames:
   if part.startswith(otherlsname):
    lsname = otherlsname
    break
 if lsname == '':
  if (0 < len(lsparts)):
   lspart = lsparts[0]
   if lspart.endswith(')'):
    # remove paren at end of lsparts[0] e.g., NI1LAK.) -> NI1LAK.
    lsname = lspart[0:-1]
   elif lspart.endswith((').' ,'),')):                          
    lsname = lspart[0:-2] 
 if lsname.endswith(','):
  # remove the ending comma
  lsname = lsname[0:-1]
 return lsname

def gen_fraglens_a(texttypes,dbg=False):
 # return list of initial
 #A(X*BX*)A  where A is lspart with itype = 1
 # convert lsheads into a string
 sparts = []
 for i,texttype in enumerate(texttypes):
  itype,text = texttype
  if itype == 1:
   sparts.append('a')
  elif itype == 0:
   sparts.append('b') # space
  else:
   sparts.append('x') # text to skip
 s = ''.join(sparts)
 if dbg:
  print("gen_fraglens_a: fragstring s=\n'%s'" % s)
 # use regexes to get sequence of initial fragments
 ans = []
 n = 0
 for n in range(0,len(s)):
  m = re.search(r'^(ax*a*)(x*bx*ax*a*){%s}'%n,s)
  if m == None:
   continue
  t = m.group(0)
  ans.append(len(t))
  if dbg:
   print('gen_fraglens_a: n=%s, t=%s' %(n,t))
 return ans

def gen_fraglens_b(texttypes,dbg=False):
 # return list of initial
 #A(X*BX*)A  where A is lspart with itype>0
 # convert lsheads into a string
 sparts = []
 for i,texttype in enumerate(texttypes):
  itype,text = texttype
  if itype > 0:
   sparts.append('a')
  elif itype == 0:
   sparts.append('b') # space
  else:
   sparts.append('x') # text to skip
 s = ''.join(sparts)
 if dbg:
  print("gen_fraglens_b: fragstring s=\n'%s'" % s)
 # use regexes to get sequence of initial fragments
 ans = []
 n = 0
 for n in range(0,len(s)):
  #m = re.search(r'^a(x*bx*a){%s}'%n,s)
  m = re.search(r'^(ax*a*)(x*bx*ax*a*){%s}'%n,s)
  if m == None:
   continue
  t = m.group(0)
  ans.append(len(t))
  if dbg:
   print('gen_fraglens_b: n=%s, t=%s' %(n,t))
 return ans
  
def lsparts_to_lsheads(lsparts,dbg=False):
 """ lshead = [(type,text) for text in lsparts
  type = -1  Do not use text in determination of lsname
  type =  0  Space, possibly use between parts of lsname
  type =  1  text matches particular regex
  type =  2  text is otherwise 
 """
 lstype_parts = []
 for i,lspart in enumerate(lsparts):
  if lspart in ['-²','²']:
   lstype_parts.append((-1,lspart))
   continue
  if lspart.startswith(('-[Page',' [Page')):
   lstype_parts.append((-1,lspart))
   continue
  if lspart == ' ':
   lstype_parts.append((0,lspart))
   continue
  if re.search(r"^[A-Z][A-Z0-9Ü-]*[.,)]*('S)?$",lspart):
   lstype_parts.append((1,lspart))
  else:
   lstype_parts.append((2,lspart))
 # Try longest match with otherlsnames
 fraglens = gen_fraglens_b(lstype_parts,dbg=dbg)
 for fraglen in reversed(fraglens):  # go from longest to shortest
  lsheads = lstype_parts[0:fraglen]
  lsnameparts = [lspart for itype,lspart in lsheads if itype >= 0]
  lsname = ''.join(lsnameparts)
  if lsname in otherlsnames:
   return lsheads,lsname
 # Try 'normal'
 fraglens = gen_fraglens_a(lstype_parts,dbg=dbg)
 if fraglens != []:
  # Use longest fraglen
  fraglen = fraglens[-1]
  lsheads = lstype_parts[0:fraglen]
  lsnameparts = [lspart for itype,lspart in lsheads if itype >= 0]
  lsname = ''.join(lsnameparts)
  return lsheads,lsname
  
 return lstype_parts,''

def part_to_lsname1(part0,dbg=False):
 # part is the string following some <ls>
 part = part0
 lsparts = re.split(r'(-²)|(²)|(-\[Page.*?\])|( \[Page.*?\])|( )',part)
 lsparts1 = [x for x in lsparts if x not in [None,'']]
 part1 = ''.join(lsparts1)
 if part1 != part:
  print("WARNING:\npart = '%s'\npart1= '%s'" %(part,part1))
  for ix,x in enumerate(lsparts1):
   print("lspart1[%s]='%s'" %(ix,lsparts1[ix]))
  exit(1)
 lsheads,lsname = lsparts_to_lsheads(lsparts1,dbg=dbg)
  
 if dbg:
  for ix,x in enumerate(lsparts1):
   if x != None:
    print("lspart[%s]='%s'" %(ix,lsparts1[ix]))
  print()
  for ix,x in enumerate(lsheads):
   print("lshead[%s]='%s'" %(ix,lsheads[ix]))
  print('lsname=',lsname)
  exit(1)
 # some tidying up of lsname
 if lsname.endswith(')'):
  lsname = lsname[0:-1]
 elif lsname.endswith((').' ,'),')):                          
  lsname = lsname[0:-2] 
 elif lsname.endswith(','):
  # remove the ending comma
  lsname = lsname[0:-1]  
 return lsname

def count_ls1(lines):
 change_lsnamed = get_change_lsnames()
 changes = []
 lsnamed = {}
 exceptions = []
 page = None
 for iline,line0 in enumerate(lines):
  line = line0
  if not line.startswith('<p>'):
   continue
  m = re.search(r'\[Page(.*?)\]',line)
  if m:
   page = m.group(1)
  parts = re.split(r'(<ls>)',line)
  prev = None
  for ipart,part in enumerate(parts):
   if part == '<ls>':
    prev = part
    continue
   if prev == None:
    continue
   # part is the string following some <ls>
   ## begin computation of lsname from part
   lsname = part_to_lsname(part)
   lsname1 = part_to_lsname1(part)
   if lsname != lsname1:
    print("line %s\npart= '%s' \nlsname = '%s'\nlsname1 = '%s'\n" %(iline+1,part,lsname,lsname1))
    part_to_lsname1(part) #,dbg=True)
    #exit(1)
    lsname = lsname1
   ## end of computation of lsname for this part
   if lsname == '':
    exceptions.append(part)
    continue
   # update lsnamed
   if lsname not in lsnamed:
    lsnamed[lsname] = 0
   lsnamed[lsname] = lsnamed[lsname] + 1
   if lsname in change_lsnamed:
    change = Change(iline+1,line0,lsname,page)
    changes.append(change)
 # reduce dictionary by merging, for example,
 # 0008 BLOOMFIELD and 0002 BLOOMFIELD. to
 #  0010 BLOOMFIELD
 lsnamed = lsname_reduce(lsnamed)
 return lsnamed,exceptions,changes

def unused_lsname_reduce(d):
 e = {} # new merged dictionary
 keys = sorted(d.keys())
 prev = '-----' # some non-key
 for key in keys:
  if not key.endswith('.'):
   e[key] = d[key]
  elif key == (prev+'.'):
   e[prev] = e[prev] + d[key]
  else:
   e[key] = d[key]
  prev = key
 ekeys = e.keys()
 print('lsname_reduce %s -> %s' %(len(keys),len(ekeys)))
 return e

def lsname_reduce(d):
 e = {} # new merged dictionary
 keys = sorted(d.keys())
 prev = '-----' # some non-key
 for key in keys:
  if key.endswith('.'):
   key1 = key[0:-1]
   if key1 in e:
    e[key1] = e[key1] + d[key]
   else:
    e[key] = d[key]
  else: # key does not end in '.'
   e[key] = d[key]
 ekeys = e.keys()
 print('lsname_reduce %s -> %s' %(len(keys),len(ekeys)))
 return e

def removenum(s):
 s1 = re.sub(r'[0-9-]','',s)
 return s1

def write_ls(fileout,lsdict):
 recs = [[k,lsdict[k],removenum(k)] for k in lsdict]
 recs1 = sorted(recs,key = lambda rec: rec[2])
 with codecs.open(fileout,"w","utf-8") as f:
   for key,n,key1 in recs1:
    n = lsdict[key]
    out = '%04d %s' %(n,key)
    f.write(out+'\n')
 print(len(recs),"ls counts written to",fileout)

def write_exceptions(fileout,exceptions):
 exceptions1 = sorted(exceptions)
 with codecs.open(fileout,"w","utf-8") as f:
   for x in exceptions1:
    out = x
    f.write(out+'\n')
 print(len(exceptions),"exceptions written to",fileout)

def write_changes(fileout,changes):
 #changes1 = sorted(changes,key = lambda x: x.lsname)
 changes1 = changes
 with codecs.open(fileout,"w","utf-8") as f:
   for change in changes1:
    outarr = []
    lsname = change.lsname
    lnum = change.lnum
    line = change.line
    page = change.page
    outarr.append('; %s Page %s' % (lsname,page))
    outarr.append('%s old %s' %(lnum,line))
    outarr.append(';')
    for out in outarr:
     f.write(out+'\n')
 print(len(changes),"changes written to",fileout)

def test1():
 part = 'DA-²S4AK. 51, 7. -- 8) {%Nenner eines Bruchs.%} '
 lsname = part_to_lsname1(part,dbg=True)
 print('test1: lsname=',lsname)
 exit(1)
if __name__=="__main__":
 #test1()
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] # extended ascii
 #filedbg = sys.argv[3]
 #filechg = sys.argv[4]
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 print(len(lines),'lines read from',filein)
 #plines = [line for line in lines if line.startswith('<p>')]
 #print(len(plines),'lines start with <p>')
 lscountd,exceptions,changes = count_ls1(lines)
 write_ls(fileout,lscountd)
 #write_exceptions(filedbg,exceptions)
 #write_changes(filechg,changes)
 
