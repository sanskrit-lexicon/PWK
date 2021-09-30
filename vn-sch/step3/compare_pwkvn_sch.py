#-*- coding:utf-8 -*-
"""compare_pwkvn_sch.py
"""

from __future__ import print_function
import sys, re,codecs
sys.path.append('../')
import transcoder
transcoder.transcoder_set_dir('../transcoder')

class Pentry(object):
 Ldict = {}
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.line = line
  self.status = False
  m = re.search(r'^L=(.*?) <p>(.*)$',line)
  if not m:
   return
  self.L = m.group(1)
  self.text = m.group(2)
  m = re.search(r'^(.*?){#(.*?)#}',self.text)
  if not m:
   print('Pentry Error 1',line)
   return
  head = m.group(1)
  self.k2 = m.group(2)
  # remove accents
  k1 = self.k2.replace('/','')
  k1 = k1.replace('^','')
  k1 = re.sub(r',.*$','',k1)
  k1 = re.sub(r' .*$','',k1)
  k1 = re.sub(r'\(.*$','',k1)  # duHkhasparza(m)
  self.k1 = k1
  if head == '':
   self.hom = ''
   self.marker = ''
  elif ' ' in head:
   # homonym and optional marker
   parts = head.split(' ')
   hompart = parts[0]
   marker = parts[1]
   m = re.search(r'^([1-9])[.]$',hompart)
   if not m:
    print('Pentry Error 2',line)
    return
   self.hom = m.group(1)
   self.marker = marker  # Empty string if there is no marker
   if marker not in ['*','','°']:
    print('Unknown marker =',self.marker,'   ',line)
  else:
   # No homonym, but a marker
   self.hom = ''
   self.marker = head
   if self.marker not in ['*','°']:
    print('Unknown marker =',self.marker,'   ',line)
  self.status = True
  # homk1 should be unique
  homk1 = self.hom + self.k1
  if homk1 in Pentry.Ldict:
   print('Pentry Warning homk1 not unique:',homk1,line)
  Pentry.Ldict[homk1] = self
  self.homk1 = homk1
  
def init_pentries(filein):
 # slurp lines
 recs = []
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  for iline,line in enumerate(f):
   rec = Pentry(line)
   if rec.status:
    recs.append(rec)
 print('Pentry:',len(recs),"records read from",filein)
 return recs

class Sentry(object):
 Ldict = {}
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.line = line
  self.status = False
  m = re.search(r'^L=(.*?) (.*)$',line)
  if not m:
   return
  self.L = m.group(1)
  self.text = m.group(2)
  m = re.search(r'^(.*?){#(.*?)#}',self.text)
  if not m:
   print('Pentry Error 1',line)
   return
  head = m.group(1)
  self.k2 = m.group(2)
  # remove accents
  k1 = self.k2.replace('/','')
  k1 = k1.replace('^','')
  k1 = k1.replace('[','')
  k1 = k1.replace(']','')
  k1 = k1.replace('-','')
  k1 = re.sub(r'\(.*$','',k1)  # special for Schmidt - also PWK!
  self.k1 = k1
  
  if head == '':
   self.hom = ''
   self.marker = ''
  elif ' ' in head:
   # homonym and optional marker
   parts = head.split(' ')
   hompart = parts[0]
   marker = parts[1]
   m = re.search(r'^([1-9])[.]$',hompart)
   if not m:
    print('Pentry Error 2',line)
    return
   self.hom = m.group(1)
   self.marker = marker  # Empty string if there is no marker
   if marker not in ['*','','°','†','†°','†*']:
    print('Unknown marker =',self.marker,'   ',line)
  else:
   # No homonym, but a marker
   self.hom = ''
   self.marker = head
   if self.marker not in ['*','','°','†','†°','†*']:
    print('Unknown marker =',self.marker,'   ',line)
  self.status = True
  # homk1 should be unique
  homk1 = self.hom + self.k1
  if homk1 in Sentry.Ldict:
   # There are several duplicates in Schmidt. Probably his own VN?
   #print('Sentry Warning homk1 not unique: "%s"'%homk1,line)
   pass
  else:
   Sentry.Ldict[homk1] = []
  Sentry.Ldict[homk1].append(self)
  self.homk1 = homk1
  
def init_sentries(filein):
 recs = []
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  for iline,line in enumerate(f):
   if line.strip() == '':
    # assume file has some blank lines, which we skip
    continue
   rec = Sentry(line)
   if rec.status:
    recs.append(rec)
 print('Sentry:',len(recs),"records read from",filein)
 return recs
 

def mark_entries(entries):
 nmark = 0
 n3 = 0
 for entry in entries:
  nlines = len(entry.datalines)
  if nlines != 1:  # the usual
   if nlines == 3: # 2nd most common -- due to page break
    n3 = n3 + 1
   else:
    print(entry.metaline,'has',nlines,'datalines')
   #exit(1)
  found = False  # find {part=...}
  for iline,line in enumerate(entry.datalines):
   m = re.search(r'{part=.*?}',line)
   if m != None:
    temp = m.group(0)
    found = True
    break
  assert found
  m = re.search(r'type=(.*?),',temp)
  assert m != None
  stype = m.group(1)
  #entry.marked = (stype == '')
  entry.marked = True   #  ALL entries are marked!
  if entry.marked:
   nmark = nmark + 1
 print(nmark,"all entries marked ")
 print(n3,"entries have 3 lines")

def entry_out(lines):
 nlines = len(lines)
 if nlines == 3:
  lines1 = [x for x in lines if not x.startswith('[Page')]
 else:
  lines1 = lines
 text = ' '.join(lines1)
 text = re.sub(r'{part=.*?}','',text)
 #if not re.search(r'^{#.*?#} ([0-9.]+ )?( [° * +])?{%.*?%}¦',text):
 #if not re.search(r'^([0-9.]+ )?( [° * +])?{%.*?%}¦',text):
 if not re.search(r'^([0-9.]+ )?( *[°*†]+)?{%.*?%}¦',text):
  print('WARNING',text)
 return text

def out_transcode(line,tranout):
 def fslp(m):
  tranin = 'slp1'
  x = m.group(1)
  y = transcoder.transcoder_processString(x,tranin,tranout)
  z = '{#%s#}' %y
  return z

 def unused_fiast(m):
  tranin = 'roman1'
  x = m.group(1)
  # must low-case first
  x1 = x.lower()
  y1 = transcoder.transcoder_processString(x1,tranin,'slp1')
  y = transcoder.transcoder_processString(y1,'slp1',tranout)
  z = '{#%s#}' %y
  return z

 #tranin = 'roman1'
 out1 = re.sub(r'{#(.*?)#}',fslp,line)
 #out2 = re.sub(r'{%(.*?)%}',fiast,out1)
 return out1

pwschforce = {
  #"AmikzApayasya" : "Amikzapayasya",
  #"AyujY" : "Ayuj",
  #"AvasaTIya" : "AvasaTiya",
  #"upasaMbihIrzu" : "upasaMjihIrzu",
  #"ekonapaYcASadDA" : "ekonapaYcASaDA",
  #"evaMvAdin" : "evaMvAdiR",
  #"kAmarUpin" : "kAmarupin",
  #"kAmaGarza" : "kAmavarza",
  #"gukAra" : "guMkAra",
  # homonym difference betwee pwkvn and schmidt
  "1karz" : "karz",
  "kuw" : "4kuw",
  "1kup" : "kup",
  "Guz" : "1Guz",
  "tap" : "1tap",
  "tar" : "1tar",
  "1Dar" : "Dar",
  # homonym difference, and also vowel length difference
  "2ta" : "tA",
}

def write(fileout,pentries,sentries,tranout):
 filelog = 'compare_log.txt'
 flog = codecs.open(filelog,"w","utf-8")
 n = 0
 nmulti = 0  # number of cases with multiple schmidt matches
 nzero = 0   # number of cases with NO schmidt matches
 with codecs.open(fileout,"w","utf-8") as f:
  for pentry in pentries:   
   outarr = []
   n = n + 1
   # one line for PWKVN
   ptext = out_transcode(pentry.text,tranout)
   outarr.append('(pvn  %s) %s' %(pentry.L.rjust(5),ptext))
   # one (or more) lines for matching Schmidt
   key = pentry.homk1
   key1 = key
   sentries = []
   keyflag = ''
   if key in Sentry.Ldict:
    sentries = Sentry.Ldict[key]
   elif key in pwschforce:
    key1 = pwschforce[key] # force pw 'key' to match sch 'key1'
    if key1 in Sentry.Ldict:
     sentries = Sentry.Ldict[key1]
     keyflag = '!'
   if sentries != []:
    if len(sentries) != 1:
     nmulti = nmulti + 1
     flag = '+'
    else:
     flag = ''
    for sentry in sentries:
     # remove ¦ from text
     stext = sentry.text.replace('¦','')
     stext = out_transcode(stext,tranout)
     if keyflag == '':
      outarr.append('(%ssch  %s) %s' %(flag,sentry.L.rjust(5),stext))
     else:
      outarr.append('(%ssch%s %s) %s' %(flag,keyflag,sentry.L.rjust(5),stext))
   else:
    # no schmidt matches
    nzero = nzero + 1
    outarr.append('(?sch )')
    flog.write('  "%s" : "%s",\n' %(key,key1))
   outarr.append('') # readabilty blank line
   #outarr.append('L=%s %s'%(n,out))
   #outarr.append('')
   for out in outarr:
    f.write(out + '\n')
 print(n,"records written to",fileout)
 print(nmulti,"pwk entries have multiple Schmidt matches")
 print(nzero,"pwk entries have NO Schmidt matches. See",filelog)
 flog.close()

if __name__=="__main__":
 # tranin is slp1
 tranout = sys.argv[1]
 tranouts = ['slp1','deva1']
 if tranout not in tranouts:
  print('tranout must be one of %s' ','.join(tranouts))
  exit(1)
 filein = sys.argv[2] #  pwk3vn_2
 filein1 = sys.argv[3] # extract3_slp1.txt schmidt
 fileout = sys.argv[4] #
 pentries = init_pentries(filein)
 
 sentries = init_sentries(filein1)
 
 write(fileout,pentries,sentries,tranout)
