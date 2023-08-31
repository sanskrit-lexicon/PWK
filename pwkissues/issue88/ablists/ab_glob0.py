""" ab_glob0.py
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
 regexraw = r'<ab>(.*?)</ab>'
 regex = re.compile(regexraw)
 for line in lines:
  n = n + 1
  tags = re.findall(regex,line)
  for c in tags:
   if c not in asdict:
    asdict[c] = 0
   asdict[c] = asdict[c] + 1
 return asdict

class Tip(object):
 def __init__(self,line):
  self.line = line
  m = re.search(r'^(.*?)\t(.*)$',line)
  self.abbrev = m.group(1)
  self.data = m.group(2)
  m1 = re.search(r'<id>(.*?)</id> *<disp>(.*?)</disp>',self.data)
  ident = m1.group(1)
  if ident != self.abbrev:
   print('Tip error:',line)
   exit(1)
  assert ident == self.abbrev
  self.tooltip = m1.group(2)
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
 for abbrev in dabbrev:
  count = dabbrev[abbrev]
  if abbrev not in dtips:
   line = '%s\t<id>%s</id> <disp>%s</disp>' %(abbrev,abbrev,'?')
   rec = Tip(line)
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
 return tips,dtips

def make_outarr(tips0):
 recs = sorted(tips0,key = lambda rec: rec.abbrev.lower())
 outarr = []
 for rec in recs:
  out = '%s\t%s,%s\t%s' %(rec.abbrev,rec.usedcd,rec.usedab,rec.tooltip)
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
#-----------------------------------------------------
if __name__=="__main__":
 filein = sys.argv[1]  # cdsl pw.txt
 filein1 = sys.argv[2] # AB pw.txt
 filein2 = sys.argv[3] # pwab_input
 fileout = sys.argv[4] # result file
 
 lines = read_lines(filein)
 d = count_ab(lines)
 print(len(d),"distinct <ab>X</ab> from",filein)
 #
 lines1 = read_lines(filein1)
 d1 = count_ab(lines1)
 print(len(d1),"distinct <ab>X</ab> from",filein1)
 # tips
 tips,dtips = init_tips(filein2)
 # extend tips, dtips for d
 tips,dtips = update_tips(tips,dtips,'cdsl',d)
 # extend tips,dtips for d1
 tips,dtips = update_tips(tips,dtips,'ab',d1)
 outarr = make_outarr(tips) 
 write_outarr(fileout,outarr)
 # 
 check_space(tips,dtips)
 
