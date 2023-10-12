#-*- coding:utf-8 -*-
"""punct1.py 
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

space_replacements = [
 (' .', '.'), # remove space before period
 (' ,', ','), # remove space before comma
 (' ;', ';'), # remove space before semicolon
 (' )', ')'), # remove space before right-paren
 (' ]', ']'), # remove space before right-bracket
 ('( ', '('), # remove space after left-paren
 ('[ ', '['), # remove space after left-bracket
 ]

space_replacements_deva = space_replacements[1:]  # all but period
def adjust_helper(line):
 newline = line
 parts = re.split('({#.*?#})',line)
 newparts = []
 for part in parts:
  if part.startswith('{#'):
   newpart = part
   for old,new in space_replacements_deva:
    newpart = newpart.replace(old,new)   
  else:
   newpart = part
   for old,new in space_replacements:
    newpart = newpart.replace(old,new)
  newparts.append(newpart)
 newline = ''.join(newparts)
 return newline
  
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
  else: # one of the 'datalines' of entry
   newline = adjust_helper(line)
  newlines.append(newline)
  if newline != line:
   nchg = nchg + 1
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
  
