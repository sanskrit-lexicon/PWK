#-*- coding:utf-8 -*-
"""lsnum.py
 
"""
from __future__ import print_function
import sys,re,codecs

def lsnum1a(line):
 if '</ls>' not in line:
  return line 
 newline = re.sub(r'</ls> (²?[0-9]+, ²?[0-9]+, ²?[0-9]+, ²?[0-9]+[.])',r'@ \1</ls4>',line)
 newline = re.sub(r'</ls> (²?[0-9]+, ²?[0-9]+, ²?[0-9]+[.])',r'@ \1</ls3>',newline)
 newline = re.sub(r'</ls> (²?[0-9]+, ²?[0-9]+[.])',r'@ \1</ls2>',newline)
 newline = re.sub(r'</ls> (²?[0-9]+[.])',r'@ \1</ls1>',newline)
 return newline

def lsnum1b(line):
 if '</ls>' not in line:
  return line 
 newline = re.sub(r'</ls> (²?[0-9]+, ²?[0-9]+, ²?[0-9]+, ²?[0-9]+)[ ]',r'@ \1</ls4> ',line)
 newline = re.sub(r'</ls> (²?[0-9]+, ²?[0-9]+, ²?[0-9]+)[ ]',r'@ \1</ls3> ',newline)
 newline = re.sub(r'</ls> (²?[0-9]+, ²?[0-9]+)[ ]',r'@ \1</ls2> ',newline)
 return newline

def lsnum2a(line):
 #if '</ls>' not in line:
 # return line 
 newline = re.sub(
  r'<ls>([^<]+?@) ([^<]+)</ls4> (²?[0-9]+, ²?[0-9]+, ²?[0-9]+, ²?[0-9]+[.])',
  r'<ls>\1 \2</ls4> <ls n="\1">\3</ls4>',line)

 newline = re.sub(
  r'<ls>([^<]+?@) ([^<]+)</ls3> (²?[0-9]+, ²?[0-9]+, ²?[0-9]+[.])',
  r'<ls>\1 \2</ls3> <ls n="\1">\3</ls3>',newline)

 newline = re.sub(
  r'<ls>([^<]+?@) ([^<]+)</ls2> (²?[0-9]+, ²?[0-9]+[.])',
  r'<ls>\1 \2</ls2> <ls n="\1">\3</ls2>',newline)

 newline = re.sub(
  r'<ls>([^<]+?@) ([^<]+)</ls> (²?[0-9]+[.])',
  r'<ls>\1 \2</ls> <ls n="\1">\3</ls>',newline)

 return newline

def lsnum2b(line):
 newline = re.sub(r'(<ls n="[^"]*?@">)([^<]+)</ls4> (²?[0-9]+, ²?[0-9]+, ²?[0-9]+, ²?[0-9]+[.])',r'\1 \2</ls4> \1\3</ls4>',line)

 newline = re.sub(r'(<ls n="[^"]*?@">)([^<]+)</ls3> (²?[0-9]+, ²?[0-9]+, ²?[0-9]+[.])',r'\1 \2</ls3> \1\3</ls3>',newline)
 
 newline = re.sub(r'(<ls n="[^"]*?@">)([^<]+)</ls2> (²?[0-9]+, ²?[0-9]+[.])',r'\1 \2</ls2> \1\3</ls2>',newline)

 newline = re.sub(r'(<ls n="[^"]*?@">)([^<]+)</ls1> (²?[0-9]+[.])',r'\1 \2</ls1> \1\3</ls1>',newline)

 return newline

def lsnum3a(line,iline):  #<ls>X@ N, N, N, N.</ls4> N.   etc. 
 #if '</ls>' not in line:
 # return line
 iopt = 4
 newline = line
 if iopt == 0:
  return newline
 
 newline = re.sub(
  r'<ls>([^<]+?@) (²?[0-9]+, ²?[0-9]+, ²?[0-9]+,) (²?[0-9]+[.])</ls4> (²?[0-9]+[.])',
  r'<ls>\1 \2 \3</ls4> <ls n="\1 \2">\4</ls4>',newline)
 if iopt == 1:
  return newline
 # 
 newline = re.sub(
  r'<ls>([^<]+?@) (²?[0-9]+, ²?[0-9]+,) (²?[0-9]+[.])</ls3> (²?[0-9]+[.])',
  r'<ls>\1 \2 \3</ls3> <ls n="\1 \2">\4</ls3>',newline)
 if iopt == 2:
  return newline
 
 newline = re.sub(
  r'<ls>([^<]+?@) (²?[0-9]+,) (²?[0-9]+[.])</ls2> (²?[0-9]+[.])',
  r'<ls>\1 \2 \3</ls2> <ls n="\1 \2">\4</ls2>',newline)
 if iopt == 3:
  return newline

 newline = re.sub(
  r'<ls>([^<]+?@) (²?[0-9]+[.])</ls1> (²?[0-9]+[.])',
  r'<ls>\1 \2</ls1> <ls n="\1">\3</ls1>',newline)

 return newline

def remove_temp_code(line):
 newline = line.replace('@','')
 newline = re.sub(r'</ls.>','</ls>',newline)
 # not sure why an extra space is sometimes present
 newline = re.sub(r'(<ls n="[^"]+">) ',r'\1',newline)
 return newline

def lsnum1_misc(newline,iline):
 
 newline = re.sub(
  r'<ls>P[.]</ls> (²?[0-9]+, ²?[0-9]+, ²?[0-9]+), <ab>Sch[.]</ab>',
  r'<ls>P. \1</ls>, <ab>Sch.</ab>',newline)

 newline = re.sub(
  r'<ls>P[.]</ls> (²?[0-9]+, ²?[0-9]+, ²?[0-9]+),',
  r'<ls>P. \1</ls>,',newline)

 newline = re.sub(
  r'<ls>HEMA1DRI</ls> (²?[0-9]+, ²?{%[ab]%}, ²?[0-9]+, ²?[0-9]+[.]?)',
  r'<ls>HEMA1DRI \1</ls>',newline)

 newline = re.sub(
  r'<ls>VR2SHABH.</ls> (²?[0-9]+, ²?{%[ab]%}, ²?[0-9]+[.]?)',
  r'<ls>VR2SHABH. \1</ls>',newline)

 newline = re.sub(
  r'<ls>MAHA1BH.</ls> (²?[0-9]+, ²?[0-9]+, ²?{%[ab]%}[.]?)',
  r'<ls>MAHA1BH. \1</ls>',newline)

 newline = re.sub(
  r'<ls>ALAM3KA1RAV.</ls> (²?[0-9]+, ²?{%[ab]%}.)',
  r'<ls>ALAM3KA1RAV. \1</ls>',newline)

 newline = re.sub(
  r'<ls>MAHA1VY.</ls> (²?[0-9]+)',
  r'<ls>MAHA1VY. \1</ls>',newline)

 return newline

def lsnum1(line,iline):
 if line.strip() == '':
  return line
 if line.startswith(('<L>','<LEND>','<H>')):
  return line
 if '<ls>' not in line:
  return line
 newline = lsnum1a(line)
 newline = lsnum1b(newline)

 newline = lsnum1_misc(newline,iline)

 #newline = remove_temp_code(newline)
 #return newline
 #print('lsnum1: returning early')
 newline = lsnum2a(newline)
 #newline = remove_temp_code(newline)
 #return newline

 while True:
  newline1 = lsnum2b(newline)
  if newline1 == newline:
   break
  newline = newline1

 newline = lsnum3a(newline,iline)

 newline = remove_temp_code(newline)
  
 return newline


def lsnum(lines):
 newlines = []
 nchg = 0
 for iline,line in enumerate(lines):
  newline = lsnum1(line,iline)
  if newline != line:
   nchg = nchg + 1
  newlines.append(newline)
 print(nchg,'lines changed')
 return newlines

def write(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for iline,line in enumerate(lines):
   f.write(line+'\n')
 print(len(lines),"records written to",fileout)

if __name__=="__main__":
 filein = sys.argv[1] # pwkvn
 fileout = sys.argv[2] # pwkvn
 
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
  print(len(lines),"lines read from",filein)

 newlines = lsnum(lines)
 
 write(fileout,newlines)

 
