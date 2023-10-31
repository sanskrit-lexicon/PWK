#-*- coding:utf-8 -*-
"""hom_add.py Additional hom tags
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
  
def adjust_1_helper(line):
 """ Example:
old: 1. {#a#}¦
new: <hom>1.</hom> {#a#}¦
 """
 def f(m):
  homdata = m.group(1)
  x = m.group(2)
  new = '<hom>%s</hom>%s' %(homdata,x)
  return new
 newline = re.sub(r'^([0-9]+\.)( .*?¦)',f,line)
 return newline

def adjust_2_helper(line):
 """ Example:
old: ' ^1. '
new: ' <hom>1.</hom> '
 """
 def f(m):
  homdata = m.group(1)
  new = ' <hom>%s</hom> ' % homdata
  return new
 newline = re.sub(r' \^([0-9]+\.) ',f,line)
 return newline
  
def adjust_3_helper(line):
 """ Example:
old: ' 3. {#'
new: ' <hom>3.</hom> {# '
 """
 def f(m):
  homdata = m.group(1)
  new = ' <hom>%s</hom> {#' % homdata
  return new
 newline = re.sub(r' ([0-9]+\.) {#',f,line)
 return newline
  
def adjust(lines,option):
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
   if option == '1':
    newline = adjust_1_helper(line)
   elif option == '2':
    newline = adjust_2_helper(line)
   elif option == '3':
    newline = adjust_3_helper(line)
   else:
    print('option ERROR:',option)
    exit(1)
  if newline != line:
   nchg = nchg + 1
   # get rid of extra spaces
   newline = re.sub(r'  +',' ',newline)
  newlines.append(newline)
 print(nchg,"lines changed")
 return newlines

def write(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for line in lines:
   f.write(line + '\n')
 print(len(lines),"written to",fileout)
 
if __name__=="__main__":
 option = sys.argv[1]
 assert option in ['1','2','3']
 
 filein = sys.argv[2] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[3] # revised xxx.txt
 lines = read_lines(filein)
 newlines = adjust(lines,option)

 write(fileout,newlines)
 #check_hom_recs()
 
