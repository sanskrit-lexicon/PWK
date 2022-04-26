#-*- coding:utf-8 -*-
"""gtext1.py
 
"""
import sys,re,codecs

sys.stdout.reconfigure(encoding='utf-8')

skipwords = {'', ' ',  ',' ,  '-', '.',
             '?', ', --' , '(-', '-- ,' , '. --', ';',
             '!', "'", '(', ')', ')  --', ').', '*', '*(',
             ',  --',  ', -',  '-,',  '--',  '-- , --',  '--,',
             '.)',  '.',  '.,',  ':', '; --',  '”.',
             '{|', '|}', # '', '', '', 
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

class Change(object):
 def __init__(self,lnum,line,words,page):
  self.lnum = lnum
  self.line = line
  self.words = words
  self.page = page

def examine(lines,gwordset):
 dbg = False
 page = '1-282-a'
 changes = []
 for iline,line0 in enumerate(lines):
  #if iline == 100: break
  line = line0
  m = re.search(r'\[Page(.*?)\]',line)
  newpage = page
  if m != None:
   newpage = m.group(1)
  checks = [] # words in this line 
  for m in re.finditer(r'{%(.*?)%}',line):
   part = m.group(1)
   if len(part) == 1:
    # {%a%} etc. not german!
    continue
   words = part_to_words(part,dbg=dbg)
   for w in words:
    if w in gwordset:
     checks.append(w)
  if checks != []:
   # generate change for this line
   lnum = iline+1
   change = Change(lnum,line,checks,page)
   changes.append(change)
  # update page
  page = newpage
 return changes

def write_changes(fileout,changes):
 outrecs=[]
 for change in changes:
  outarr=[]
  lnum = change.lnum
  line = change.line
  page = change.page
  words = change.words  # suspicious words
  wordstr = ', '.join(words)
  outarr.append('; Page %s. ? %s' % (page,wordstr))
  outarr.append('%s old %s' %(lnum,line))
  outarr.append(';')
  outarr.append('%s new %s' %(lnum,line))
  outarr.append('; ---------------------------')
  outrecs.append(outarr)
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
    for out in outarr:
     f.write(out+'\n')
 print(len(changes),"changes written to",fileout)

def init_gwords_tocheck(filein):
 """ put words into a Python set 
 """
 with codecs.open(filein,"r","utf-8") as f:
  words = []
  n = 0
  for iline,line in enumerate(f):
   line = line.rstrip('\r\n')
   n = n + 1
   try:
    countx,word = re.split(r' +',line)
   except:
    print("Problem with line %s: '%s'" %(iline+1,line))
    continue
   if countx.startswith('x'):
    words.append(word)
 s = set(words)
 print('%s lines read from %s' %(n,filein))
 print('%s words selected' % len(words))
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
 filein1 = sys.argv[2] # pwkvn_german_unknown.txt
 fileout = sys.argv[3] # gtext2
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 print(len(lines),'lines read from',filein)
 gwordset = init_gwords_tocheck(filein1)
 changes = examine(lines,gwordset)
 write_changes(fileout,changes)

