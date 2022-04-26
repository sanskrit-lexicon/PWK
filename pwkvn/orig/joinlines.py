#-*- coding:utf-8 -*-
"""joinlines.py work with cp1252 encoding files
 
"""
import sys,re,codecs

def join_plines(x):
 """ x is array of strings of length n
  if n = 0 or n=1 return x
  else:
   remove line-endings from x[0],...,x[n-2] (all but last line
  Then join the list of adjusted strings (so return a string)
 """
 n = len(x)
 if n == 0:
  return ''
 if n == 1:
  return x[0]
 y = []
 for i,s in enumerate(x):
  if i != (n-1):
   s1 = s.rstrip('\r\n')
  else:
   s1 = s
  y.append(s1)
 #
 return ''.join(y)

def joinlines(lines):
 """ A generator for array of new lines.
 """
 ans = [] # array of joined lines
 jlines = []

 for iline,line in enumerate(lines):
  #if iline > 10:break
  if line.startswith(('<H>','<p>')):
   if jlines != []:
    newline = join_plines(jlines)
    #print('yield:',iline+1,newline)
    yield newline
   jlines = [line]
  elif jlines == []:
   print("joinlines error at line number",iline+1)
   print('line=',line)
   exit(1)
  else:
   jlines.append(line)
 # last one
 if jlines != []:
  newline = join_plines(jlines)
  yield newline


if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] # extended ascii
 
 with codecs.open(filein,"r","cp1252") as f:
  lines = [x for x in f]  # retain line-ending characters (\r\n)
 print(len(lines),"read from",filein)
 newlines = list(joinlines(lines))
 with codecs.open(fileout,"w","cp1252") as f:
  for line in newlines:
   f.write(line)
 print(len(newlines),"written to",fileout)
 
 
