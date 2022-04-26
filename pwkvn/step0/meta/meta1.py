#-*- coding:utf-8 -*-
"""meta1.py
 
"""
import sys,re,codecs


def check(iline,line):
 if len(re.findall('{#',line)) != len(re.findall('#}',line)):
  print('check %s : %s' %(iline+1,line))

class Rec:
 def __init__(self,rectype,L,pc,vol,hws,body):
  assert rectype in ['H','p']
  self.rectype = rectype
  self.L = L
  self.pc = pc
  self.hws = hws
  self.body = body
  self.vol = vol
  if self.hws == None:
   return
  a = []
  types = []
  regexes = [r"^{#[*º]*[a-zA-Z£_¹']+º?#}$", r"^{#[*]?[a-zA-Z£_¹']+º?#}$"]
  for ihw,hw in enumerate(hws):
   if ihw == 0:
    regex = regexes[0]
   else:
    regex = regexes[1]
   if re.search(regex,hw):
    a.append(hw)
    types.append('ok')
    continue
   x = re.sub(r'\[Page.*?\]','',hw)
   x = re.sub(r'[-²]','',x)
   if (ihw != 0) and x.startswith('{#º'):
    xprev = a[ihw-1]
    xprev1 = xprev[0:-2] # remove ending #}
    x1 = x[3:]  # remove initial {#º
    a.append(xprev1+x1)
    types.append('adj1')
   else:
    a.append(x)
    types.append('adj')
  self.hwscalc = a
  self.types = types
  
def line_to_rec(line):
 # <p n="N" pc="P">X
 m = re.search(r'^<p n="(.*?)" pc="(.*?)">(.*)$',line)
 n = m.group(1)
 pc = m.group(2)
 body = m.group(3)
 hws = []
 for m in re.finditer(r'<hw>(.*?)</hw>',line):
  hw = m.group(1)
  hws.append(hw)
  assert ',' not in hw
 assert hws != []
 m = re.search(r'^([1-7])-([0-9]{3,3})-(1?[a-d])$',pc)
 if m == None:
  print('pc does not parse: "%s"' %pc)
  exit(1)
 vol = m.group(1)  # volume
 L = n # temporary
 rec = Rec('p',L,pc,vol,hws,body)
 return rec

def make_recs(lines):
 recs = []
 for iline,line in enumerate(lines):
  if line.startswith('<H>'):
   rec = Rec('H',None,None,None,None,line)
   recs.append(rec)
   continue
  if '<hw>' not in line:
   # one case
   print('skipping line',line)
   continue
  rec = line_to_rec(line)
  recs.append(rec)
 return recs

def rec_to_lines(rec):
 outarr = []
 if rec.rectype == 'H':
  outarr.append(rec.body)
 else:
  outarr.append('<n>%s<pc>%s' %(rec.L,rec.pc))
  for ihw,hw in enumerate(rec.hws):
   hwcalc = rec.hwscalc[ihw]
   hwtype = rec.types[ihw]
   if hwtype == 'ok':
    assert hwcalc == hw
    outarr.append('hw:%s' % hw)
   elif hwtype == 'adj':
    outarr.append('hw:%s => %s' %(hw,hwcalc))
   elif hwtype == 'adj1':
    outarr.append('hw:%s º> %s' %(hw,hwcalc))    
   else:
    print('rec_to_lines error')                  
  #hwstr = ', '.join(rec.hws)
  #hwline = 'hws=%s' % hwstr
  #outarr.append(hwline)
  outarr.append(rec.body)
  outarr.append('<LEND>')
 return outarr

def write(fileout,recs):
 with codecs.open(fileout,"w","utf-8") as f:
  for rec in recs:
   outarr = rec_to_lines(rec)
   for line in outarr:
    f.write(line+'\n')
   # add blank line
   f.write('\n')
 print(len(recs),"records written to",fileout)

def write_tempchg(fileout,recs):

 outarr = []
 for rec in recs:
  if rec.rectype == 'H':
   continue
  hws = rec.hws
  for ihw,hw in enumerate(hws):
   hwcalc = rec.hwscalc[ihw]
   hwtype = rec.types[ihw]
   if hwtype == 'ok':
    continue
   elif hwtype == 'adj':
    outarr.append('%s %s => %s' %(rec.L,hw,hwcalc))
   elif hwtype == 'adj1':
    hwprev = hws[ihw-1]
    outarr.append('%s %s º> %s <prev>%s</prev>' %(rec.L,hw,hwcalc,hwprev))
   else:
    print('write_tempchg error')
 with codecs.open(fileout,"w","utf-8") as f:
  for line in outarr:
   f.write(line+'\n')
 print(len(outarr),"records written to",fileout)
 
if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] # temporary version of pwkvn
 fileout1 = sys.argv[3] # file of hw changes, updated manually.
 
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
  print(len(lines),"lines read from",filein)
 recs = make_recs(lines)
 write(fileout,recs)
 write_tempchg(fileout1,recs)

 
