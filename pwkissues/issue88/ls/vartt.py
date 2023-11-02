#-*- coding:utf-8 -*-
"""vartt.py  
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

def adjust(lines):
 newlines = []  # returned
 metaline = None
 nchg = 0
 for iline,line in enumerate(lines):
  if iline == 0: 
   newline = line
  elif line == '':
   newline = line
  elif line.startswith('<L>'):
   metaline = line
   newline = line
  elif line == '<LEND>':
   metaline = None
   newline = line
  elif metaline == None:
   newline = line # not in an entry
  else:
   newline = re.sub(r'</ls>[,.] <ls>Vārtt\.' ,
                    ', Vārtt.',
                    line)
  if newline != line:
   nchg = nchg + 1 
  newlines.append(newline)
 print(nchg,"lines changed")
 return newlines

def write(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for line in lines:
   f.write(line + '\n')
 print(len(lines),"written to",fileout)
 
if __name__=="__main__": 
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] # revised xxx.txt
 lines = read_lines(filein)
 newlines = adjust(lines)

 write(fileout,newlines)
 
