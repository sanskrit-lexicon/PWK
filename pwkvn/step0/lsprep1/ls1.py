#-*- coding:utf-8 -*-
"""ls1.py
 
"""
import sys,re,codecs

sys.stdout.reconfigure(encoding='utf-8')

change_lsnames_text = """
AK. OPP.
ALA1M3KA1RAS.
ALAM3KARAS.
ALAM3KARAT.
ALAM3KARAV.
ANTYKSHT2IK.
APA1ST.
AS4V. S4R.
AV. ANUER.
AV. PARI1S4.
BHADRAR.
BHAVAPR.
BR2H. AR.
CAN2DI1S4.
DAMAYANTI1C.
DAS4A K.
DAS4A KARM.
DECI1N.
DES4IN.
DHATUP.
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
  # resolve line-breaks. By removing '-²' or '²'
  line = line.replace('-²','')  # THIS IS VERY TRICKY
  line = line.replace('²','')
  line = re.sub(r'[- ]\[Page.*?\]','',line)
  parts = re.split(r'(<ls>)',line)
  prev = None
  for ipart,part in enumerate(parts):
   if part == '<ls>':
    prev = part
    continue
   if prev == None:
    continue
   # part is the string following some <ls>
   lsparts = part.split(' ')
   lsheads = []
   for lspart in lsparts:
    #if re.search(r'^[A-Z][A-Z0-9Ü-]*[.,]?$',lspart):
    if re.search(r"^[A-Z][A-Z0-9Ü-]*[.,]*('S)?$",lspart):
     lsheads.append(lspart)
    else:
     break
   lsname = ' '.join(lsheads)
   if lsname == '':
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
                    
                    ]
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
   if lsname == '':
    #fdbg.write('%05d %s\n' %(iline+1,part))
    exceptions.append(part)
    """      
    print('dbg: ',line)
    print('parts=',parts)
    print('part=',part)
    print('lsparts=',lsparts)
    print('lsheads=',lsheads)
    exit(1)
    """
    continue
   if lsname.endswith(','):
    # remove the ending comma
    lsname = lsname[0:-1]
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

if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] # extended ascii
 filedbg = sys.argv[3]
 filechg = sys.argv[4]
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 print(len(lines),'lines read from',filein)
 #plines = [line for line in lines if line.startswith('<p>')]
 #print(len(plines),'lines start with <p>')
 lscountd,exceptions,changes = count_ls1(lines)
 write_ls(fileout,lscountd)
 write_exceptions(filedbg,exceptions)
 write_changes(filechg,changes)
 
