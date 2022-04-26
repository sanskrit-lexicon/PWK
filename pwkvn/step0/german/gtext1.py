#-*- coding:utf-8 -*-
"""gtext1.py
 
"""
import sys,re,codecs

sys.stdout.reconfigure(encoding='utf-8')

skipwords = {'', ' ',  ',' ,  '-', '.',
             '?', ', --' , '(-', '-- ,' , '. --', ';',
             '!', "'", '(', ')', ')  --', ').', '*', '*(',
             ',  --',  ', -',  '-,',  '--',  '-- , --',  '--,',
             '.)',  '.',  '.,',  ':', '; --',  ## '',   '', 
             } # a set
print('skipwords=',skipwords)

def part_to_words(part0,dbg=False):
 # part is the string following some <ls>
 part = part0
 part = part.replace('-²','') 
 part = part.replace('²','')
 part = re.sub(r'-?\[Page.*?\]','',part)
 words1 = re.split(r'\b',part)
 words = []
 for w0 in words1:
  w = w0.strip()  # remove spaces at either end
  if w in skipwords:
   continue
  if re.search(r'^[0-9]+$',w):
   continue
  if len(w) == 1: # single character
   continue
  words.append(w)
 if dbg:
  print("part_to_words: '%s'" %part)
  print('words=',words)
 if ',' in words:
  print('ANOMALY: comma is still in words!')
  exit(1)
 return words

def updatedict(d,x):
 if x not in d:
  d[x] = 0
 d[x] = d[x] + 1
 
def examine(lines,gwordset):
 dbg = False
 page = '1-292-b'
 known = {}
 unknown = {}
 for iline,line0 in enumerate(lines):
  #if iline == 1000: break
  line = line0
  m = re.search(r'\[Page(.*?)\]',line)
  if m != None:
   newpage = m.group(1)
  for m in re.finditer(r'{%(.*?)%}',line):
   part = m.group(1)
   if len(part) == 1:
    # {%a%} etc. not german!
    continue
   words = part_to_words(part,dbg=dbg)
   flagwords = []
   for w in words:
    if w in gwordset:
     updatedict(known,w)
    else:
     updatedict(unknown,w)
     if len(w) == 1:
      flagwords.append(w)
   if flagwords != []:
    print('line#%d,unknowns=%s' %(iline+1,flagwords))
    _ = part_to_words(part,dbg=True)
   continue
 return known,unknown

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
 outrecs=[]
 for change in changes:
  outarr=[]
  lnum = change.lnum
  line = change.line
  page = change.page
  newline = change.newline
  outarr.append(';Page %s' % page)
  outarr.append('%s old %s' %(lnum,line))
  outarr.append(';')
  outarr.append('%s new %s' %(lnum,newline))
  outarr.append('; ---------------------------')
  outrecs.append(outarr)
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
    for out in outarr:
     f.write(out+'\n')
 print(len(changes),"changes written to",fileout)

def init_gwords(filein):
 """ put words into a Python set 
 """
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
  print(len(lines),"words read from",filein)
  s = set(lines)
  print(len(s),"set length is",len(s))
  return s

def write_words(fileout,d):
 words = d.keys()
 words = sorted(words,key = lambda w: w.lower())
 ntot = 0
 with codecs.open(fileout,"w","utf-8") as f:
  for w in words:
   n = d[w]
   out = '%04d %s' %(n,w)
   f.write(out+'\n')
   ntot = ntot + n
 print('%s instances of %s words written to %s' % (ntot,len(words),fileout))

if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 filein1 = sys.argv[2] # german word
 fileout1 = sys.argv[3] # known words, with count
 fileout2 = sys.argv[4] # unknown words, with count
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 print(len(lines),'lines read from',filein)
 gwordset = init_gwords(filein1)
 known,unknown = examine(lines,gwordset)
 
 write_words(fileout1,known)
 write_words(fileout2,unknown)
 exit(1)
 #write_exceptions(filedbg,exceptions)
 #write_changes(filechg,changes)
 with codecs.open(filenew,"w","utf-8") as f:
  for out in newlines:
   f.write(out+'\n')
 print(len(newlines),"lines written to",filenew)
 
