""" ab_local1.py
"""
import re,sys
import codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def count_ab(lines):
 asdict = {}
 n = 0
 regexraw = r'<ab (.*?)>(.*?)</ab>'
 regex = re.compile(regexraw)
 for line in lines:
  n = n + 1
  tags = re.findall(regex,line)
  for c in tags:
   #print("count_ab:",c)
   #exit(1)
   # ('n="Noth"', 'N.')  
   if c not in asdict:
    asdict[c] = 0
   asdict[c] = asdict[c] + 1
 return asdict

class Tip(object):
 def __init__(self,abbrevtuple):
  # abbrevtuple = # ('n="Noth"', 'N.')  
  attrib_string,abbrev_string = abbrevtuple
  m = re.search(r'^n="([^"]*)"$',attrib_string)
  if m == None:
   print('Tip: bad tuple',abbrevtuple)
   exit(1)
  self.tip = m.group(1)
  self.abbrev_string = abbrev_string
  self.abbrev = "%s=%s" % (self.abbrev_string,self.tip)
  self.usedcd = 0 # number of usages in cdsl pw
  self.usedab = 0 # number of usages in ab pw
  
def init_tips(filein):
 lines = read_lines(filein)
 recs = []
 d = {}
 for line in lines:
  if line.startswith(';'):
   # skip comment lines
   continue
  rec = Tip(line)
  recs.append(rec)
  abbrev = rec.abbrev
  if abbrev in d:
   print('WARNING: init_tips duplicate',line)
  d[abbrev] = rec
 print(len(recs),"read from",filein)
 return recs,d

def update_tips(tips,dtips,src,dabbrev):
 # src is ab or cdsl
 # modify tips and dtips
 for abbrev in dabbrev:
  count = dabbrev[abbrev]
  if abbrev not in dtips:
   line = '%s\t<id>%s</id> <disp>%s</disp>' %(abbrev,abbrev,'?')
   rec = Tip(abbrev)
   tips.append(rec)
   dtips[abbrev] = rec
  rec = dtips[abbrev]
  if src == 'cdsl':
   rec.usedcd = count
  elif src == 'ab':
   rec.usedab = count
  else:
   print('update_tips: invalid src',src)
   exit(1)
 # return revised data
 # return tips,dtips

def make_outarr(tips0):
 recs = sorted(tips0,key = lambda rec: rec.abbrev.lower())
 outarr = []
 for rec in recs:
  #out = '%s\t%s,%s\t%s' %(rec.abbrev,rec.usedcd,rec.usedab,rec.tooltip)
  out = '%s,%s\t%s' %(rec.usedcd,rec.usedab,rec.abbrev)
  outarr.append(out)
 return outarr


def write_outarr(fileout,outarr):
 fout = codecs.open(fileout,'w','utf-8')
 for out in outarr:
  fout.write("%s\n" % out)
 fout.close()
 print(len(outarr),"lines written to",fileout)

def check_space(tips,dtips):
 for rec in tips:
  abbrev = rec.abbrev
  if ' ' in abbrev:
   abbrev1 = abbrev.replace(' ','') # remove spaces
   if abbrev1 in dtips:
    rec1 = dtips[abbrev1]
    print(rec.line)
    print(rec1.line)
    print()

def count_diff(tips):
 n = 0
 for rec in tips:
  if rec.usedcd != rec.usedab:
   n = n + 1
 print(n,'differences in local abbreviations')
 # group
 d = {}
 for rec in tips:
  a = rec.abbrev_string
  if a not in d:
   d[a] = 0
  d[a] = d[a] + 1
 keys = d.keys()
 keys = sorted(keys,key = lambda x: x.lower())
 for key in keys:
  #print(key,d[key])
  pass
 print(len(keys),'distinct abbreviations')
 
#-----------------------------------------------------
if __name__=="__main__":
 filein = sys.argv[1]  # cdsl pw.txt
 filein1 = sys.argv[2] # AB pw.txt
 #filein2 = sys.argv[3] # pwab_input
 fileout = sys.argv[3] # result file
 
 lines = read_lines(filein)
 d = count_ab(lines)
 print(len(d),"distinct <ab []>X</ab> from",filein)
 #
 lines1 = read_lines(filein1)
 d1 = count_ab(lines1)
 print(len(d1),"distinct <ab []>X</ab> from",filein1)
 
 # tips
 #tips,dtips = init_tips(filein2)
 tips = []
 dtips = {}
 # extend tips, dtips for d
 update_tips(tips,dtips,'cdsl',d)
 # extend tips,dtips for d1
 update_tips(tips,dtips,'ab',d1)
 outarr = make_outarr(tips) 
 write_outarr(fileout,outarr)
 count_diff(tips)
 
