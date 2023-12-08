# coding=utf-8
""" make_change_regular.py
"""
from __future__ import print_function
import sys, re,codecs
import digentry  

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

word_regex_raw = '[A-Za-z0-9äöüÄÖÜ]+'
word_regex = re.compile(word_regex_raw)

def exclude_words(words):
 ans = []
 for word in words:
  if len(word) == 1:
   continue
  if re.search(r'^[0-9]+$',word):
   continue
  ans.append(word)
 return ans

def get_words_line(line0,iline=None):
 # return array of words
 # various filters
 line = line0
 line = re.sub(r'{%.*?%}', ' ',line)
 line = re.sub(r'{#.*?#}', ' ',line)
 line = re.sub(r'<([^ ]*?)(.*?)>.*?</\1>',' ',line)
 line = re.sub(r'¦',' ',line)
 line = re.sub(r'<div.*?>',' ',line)
 line = line.strip()
 words0 = re.findall(word_regex,line)
 words = exclude_words(words0)
 dbg = False
 if dbg:
  print('line0: ',line0)
  print('line : "%s"' % line)
  print('words:',', '.join(words))
  print()
 return words

def get_words(entries):
 # create entry.dataline_words array
 dbg = False
 for ientry,e in enumerate(entries):
  e.dataline_words = []
  for iline,line in enumerate(e.datalines):
   words_line = get_words_line(line)
   e.dataline_words.append(words_line)

 print("exit get_words")
 
def write_outrecs(fileout,outrecs):
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outrecs),"cases written to",fileout)

def write_recs(fileout,recs):
 outrecs = []
 for irec,rec in enumerate(recs):
  if rec.lnum == None:
   print('write_recs problem:',rec.linein)
  outarr = []
  outarr.append('; %s' %rec.metaline)
  outarr.append('; %s -> %s' %(rec.oldword,rec.newword))
  outarr.append('%s old %s' % (rec.lnum,rec.line))
  outarr.append(';')
  outarr.append('%s new %s' % (rec.lnum,rec.newline))
  outrecs.append(outarr)
 write_outrecs(fileout,outrecs)

def write_outrecs(fileout,outrecs):
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outrecs),"cases written to",fileout)

def write_outarr(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"cases written to",fileout)

def get_freq(entries):
 d = {}
 for ientry,entry in enumerate(entries):
  for iline,words_line in enumerate(entry.dataline_words):
   for w in words_line:
    if w not in d:
     d[w] = 0
    d[w] = d[w] + 1
 return d

def write_freq(fileout,entries):
 freqsd = get_freq(entries)
 uwords = freqsd.keys()  # unique words
 uwords1 = sorted(uwords, key = lambda w: w.lower())
 outarr = []
 for w in uwords1:
  count = freqsd[w]
  out = '%s %s' % (w,count)
  outarr.append(out)
 write_outarr(fileout,outarr)

class Change:
 def __init__(self,line):
  # 13tn 1 -DE IT 0 : CHG : JF : -> 13ten
  self.linein = line
  parts = line.split(':')
  if len(parts) != 4:
   print ('Change Parse Error 1',line)
   exit(1)
  a = parts[0].split(' ')
  if len(a) != 6:
   print ('Change Parse Error 2',line)
   print('a=',a)
   exit(1)
  self.oldword = a[0]
  # check that a[1] is '1'  (one instance of the word)
  if a[1].strip() != '1':
   print('Warning: Change Parse 2a:',line)
   
  m = re.search(r'^ *-> +(.*$)',parts[3]) # : -> 13ten
  if m == None:
   print ('Change Parse Error 3',line)
   exit(1)
  self.newword = m.group(1).strip()
  # some other fields needed
  self.metaline = None
  self.lnum = None
  self.line = None
  self.newline = None
  
def init_change_regular(filein):
 lines = read_lines(filein)
 recs = [Change(line) for line in lines]
 print(len(recs),"records read from",filein)
 return recs

# regexsplitraw = r'<(?P<tag>[^ ])*?.*?>.*</(?P=tag)>|({%.*?%})|({#.*?#})|(<div.*?>)|(¦)|([A-Za-z0-9äöüÄÖÜ]+)'
#regexsplitraw = r'|({%.*?%})|({#.*?#})|(<div.*?>)|(¦)|([A-Za-z0-9äöüÄÖÜ]+)'
regexsplitraw = r'(<(?P<tag>[^ >]+).*?>.*?</(?P=tag)>)|({%.*?%})|({#.*?#})|(<div.*?>)|(¦)|([A-Za-z0-9äöüÄÖÜ]+)'

regexsplit = re.compile(regexsplitraw)

word_regex_raw = '[A-Za-z0-9äöüÄÖÜ]+'
word_regex = re.compile(word_regex_raw)
tagnames = {'ab','lex','ls','hom','lang','gk','mong','arab','rus','is','bot','zoo','iw'}
def get_newline(line,drec):
 dbg = False
 if dbg: print(line)
 parts = re.split(regexsplit,line)
 # if dbg: print(parts)
 newparts = []
 chgrecs = []
 for part in parts:
  if part == None:
   pass
  elif part == '':
   pass
  elif part == '¦':
   newparts.append(part)
  elif part.startswith(('{','<',' ')):
   newparts.append(part)
  elif part in tagnames:
   #newparts.append(part)
   pass  # a weakness since no non-capturing named groups
  elif re.search(word_regex,part):
   #print('word:',part)
   if part in drec:
    rec = drec[part]
    newpart = rec.newword
    newparts.append(newpart)
    chgrecs.append(rec)
   else:
    newparts.append(part)
  else:
   #print('other part="%s"' % part)
   newparts.append(part)
 if chgrecs != []:
  newline = ''.join(newparts)
 else:
  newline = line
 return newline,chgrecs
def update_recs(entries,recs):
 drec = {}
 for rec in recs:
  w = rec.oldword
  if w in drec:
   print('update_recs error 1',line)
   exit(1)
  drec[w] = rec
 #
 for ientry,e in enumerate(entries):
  for iline,line in enumerate(e.datalines):
   newline,chgrecs = get_newline(line,drec)
   if newline == line:
    continue
   if len(chgrecs) != 1:
    print('PROBLEM: chgrecs has length',len(chgrecs))
    #print('   line=',line)
    #print()
    #print('newline=',newline)
    for rec in chgrecs:
     print(rec.line)
    continue
   if False:
    print('   line=',line)
    print()
    print('newline=',newline)
    print(chgrecs)
   rec = chgrecs[0]
   rec.metaline = e.metaline
   rec.lnum = e.linenum1 + iline + 1
   rec.line = line
   rec.newline = newline
def test():
 import re
 example = "<hom>1.</hom> {#a#}¦ <lex>Pron.</lex> der 3ten Person"
 pattern = r'(<[^>]+>)|(\{#\w+#\})|(¦)'
 print(pattern)
 result = re.split(pattern, example)
 # Remove empty strings from the result
 result = [s for s in result if s]
 print('test :',result)
 #exit()
"""
r'(<[^>]+>)|(\{#\w+#\})|(¦)' instead of
r'(<[^>]+>)|(\{#\w+#\})|( [.] *)'
"""
def test1():
 import re
 example = "<hom>1.</hom> {#a#}¦ <lex>Pron.</lex> der 3ten Person"
 #pattern = r'(<[^>]+>)|(\{#\w+#\})|(¦)'
 pattern = r'(<[^>]+>)|(\{#\w+#\})|( [.] *)'
 print(pattern)
 result = re.split(pattern, example)
 # Remove empty strings from the result
 result = [s for s in result if s]
 print('test1:',result)
 exit()
 
def test2():
 import re
 example = '<hom>1.</hom> {#a#}¦ <lex n="dummy">Pron.</lex> der 3ten Person'
 print(example)
 print()
 pattern = r'(<(?P<tag>[^ >]+)[^>]+>.*?</?P=tag>)|(\{#\w+#\})|(¦)|( +)'
 pattern = r'(<(?P<tag>[^>]+)[^>]+>.*?</?P=tag>)'
 pattern = r'(<.*?>)'
 pattern = r'(<(?P<tag>[^ >]+).*?>.*?</(?P=tag)>)'
 pattern = r'(<(?P<tag>[^ >]+).*?>.*?</(?P=tag)>)|({%.*?%})|({#.*?#})|(<div.*?>)|(¦)|([A-Za-z0-9äöüÄÖÜ]+)'
 print(pattern)
 result = re.split(pattern, example)
 print('result=',result)
 # Remove empty strings from the result
 result = [s for s in result if s]
 for r in result:
  print(r)
 exit()

 
if __name__=="__main__":
 #test2()
 #test()
 #test1()
 #exit(1)
 filein = sys.argv[1]  # pre_change1_regular
 filein1 = sys.argv[2] # xxx.txt cdsl
 fileout = sys.argv[3] # change_word_regular.txt change transactions
 recs = init_change_regular(filein)
 entries = digentry.init(filein1)

 update_recs(entries,recs)
 write_recs(fileout,recs)
 #get_words(entries) # entry.dataline_words
 # now we have to correlate the lists of entry.dataline_words
 # with recs
 # This logic requires that we are changing words which only appear once
 
 exit(1)
 write_words(fileout,entries)
 write_freq(fileout1,entries)

 
