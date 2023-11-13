#-*- coding:utf-8 -*-
"""bot_freq.py
"""
import sys,re,codecs
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec cannot encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def adjust_1(lines):
 # remove blank lines within entry
 # lines starting with <LEND> must = <LEND>
 newlines = []  # returned
 metaline = None
 for iline,line in enumerate(lines):
  if iline == 0: # include first line
   newlines.append(line)
  elif line.startswith('<L>'):
   metaline = line
   newlines.append(line)
  elif line.startswith('<LEND>'):
   metaline = None
   newline = '<LEND>'
   newlines.append(newline)
  elif metaline == None:
   newlines.append(line) # not in an entry
  else:
   # line within entry.
   # skip if blank
   newline = line.strip() # remove initial or trailing spaces
   if newline == '':
    pass  # skip blank line in entry
   else:
    newlines.append(newline)
 print('1: # lines %s -> %s' %(len(lines),len(newlines)))
 return newlines

def adjust_2_helper(line0):
 line = line0.strip()
 divs = re.findall(r'<div [^>]*>',line)
 if len(divs) == 0:
  return [line]
 if (len(divs) == 1) and line.startswith('<div '):
  return [line]                          
 # multiple divs
 parts = re.split(r'(<div [^>]*>)',line)
 prevdiv = ''
 ans = []
 dbg = False
 # dbg = line.startswith('{#iNk#}¦ = {#iNg#}. <div n="p">')
 for ipart,part in enumerate(parts):
  if dbg: print('part[%s]: %s' % (ipart,part))
  if part == '':
   continue
  if part.startswith('<div '):
   prevdiv = part
  else:
   newline = prevdiv + part
   newline = newline.strip()
   ans.append(newline)
   prevdiv = ''
 if dbg: # dbg
  print('old:',line)
  for x in ans:
   print('new:',x)
  exit(1)
 return ans

def adjust_2(lines):
 # insert new line at a div
 newlines = []  # returned
 metaline = None
 for iline,line in enumerate(lines):
  if iline == 0: # include first line
   newlines.append(line)
  elif line.startswith('<L>'):
   metaline = line
   newlines.append(line)
  elif line == '<LEND>':
   metaline = None
   newlines.append(line)
  elif metaline == None:
   newlines.append(line) # not in an entry
  else:
   # line within entry.
   # if the line has a <div> in the middle, make extra line(s)
   news = adjust_2_helper(line)
   for newline in news:
    newlines.append(newline)
 print('2: # lines %s -> %s' %(len(lines),len(newlines)))
 return newlines


def adjust_3(lines):
 # at most one blank line between entries
 newlines = []  # returned
 metaline = False  
 nblank = 0
 for iline,line in enumerate(lines):
  line = line.strip() # remove spaces at beginning and end
  if iline == 0: # include first line
   newlines.append(line)
  elif line.startswith('<L>'):
   metaline = line
   newlines.append(line)
  elif line == '<LEND>':
   metaline = None
   newlines.append(line)
   nblank = 0
  elif metaline == False:
   newlines.append(line) # line precedes first entry
  elif metaline == None:
   # line is between entries (<LEND> prev entry, and <L> next entry)
   if line == '':
    nblank = nblank + 1
    if nblank == 1:
     newlines.append(line)
    else:  # exclude extra blanks
     pass
   else:
    # non-blank line between entries
    newlines.append(line)
  else:
   # line within entry.
   newlines.append(line)
 print('3: # lines %s -> %s' %(len(lines),len(newlines)))
 return newlines

def adjust_4(lines):
 # at least one blank line between entries
 newlines = []  # returned
 metaline = False  
 nlines = len(lines)
 for iline,line in enumerate(lines):
  line = line.strip() # remove spaces at beginning and end
  if iline == 0: # include first line
   newlines.append(line)
  elif line.startswith('<L>'):
   metaline = line
   newlines.append(line)
  elif line == '<LEND>':
   metaline = None
   newlines.append(line)
   iline1 = iline+1
   if iline1 < nlines:
    nextline = lines[iline1]
    if nextline.startswith('<L>'):
     # insert blank line
     newlines.append('')
  elif metaline == False:
   newlines.append(line) # line precedes first entry
  elif metaline == None:
   newlines.append(line)
  else:
   # line within entry.
   newlines.append(line)
 print('4: # lines %s -> %s' %(len(lines),len(newlines)))
 return newlines

def adjust_5_helper(line,metaline):
 news = []
 if metaline.startswith(('<L>22839<','<L>29651<')):
  news = ['xxx']
 return news

def adjust_5(lines):
 # temporary line inserts to force agreement with AB
 # these will undergo further adjustment
 newlines = []  # returned
 metaline = None
 for iline,line in enumerate(lines):
  if iline == 0: # include first line
   newlines.append(line)
  elif line.startswith('<L>'):
   metaline = line
   newlines.append(line)
  elif line == '<LEND>':
   news = adjust_5_helper(line,metaline)
   for new in news:  # may be empty
    newlines.append(new)
   metaline = None
   newlines.append(line)
  elif metaline == None:
   newlines.append(line) # not in an entry
  else:
   # line within entry.
   newlines.append(line)
 print('5: # lines %s -> %s' %(len(lines),len(newlines)))
 return newlines

def write(fileout,d):
 keys = sorted(d.keys(), key = lambda x: x.lower())
 outarr = []
 for key in keys:
  count = d[key]
  out = '%s %s' %(key,count)
  outarr.append(out)
  
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out + '\n')
 print(len(keys),"written to",fileout)

def bot_tag_count(lines):
 d = {}
 n = 0 # total number of bot tags
 for line in lines:
  bots = re.findall(r'<bot>.*?</bot>',line)
  for bot in bots:
   n = n + 1
   if bot not in d:
    d[bot] = 0
   d[bot] = d[bot] + 1
 print(n,"bot tags")
 print(len(d.keys()),"distinct bot tags")
 return d

if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] # revised xxx.txt
 lines = read_lines(filein)
 d = bot_tag_count(lines)

 write(fileout,d)
 #check_hom_recs()
 
