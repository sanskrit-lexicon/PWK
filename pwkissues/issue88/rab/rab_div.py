#-*- coding:utf-8 -*-
"""rab_div.py  
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
old: <div n="1">— 2) fingirter Mannsname.
new: <div n="1">— 2〉 fingirter Mannsname.
〉 = Unicode RIGHT ANGLE BRACKET
 """
 newline = re.sub(r'(— [0-9a-zα-ωΑ-Ω]+)\)',r'\1〉',line)
 return newline

def adjust_2_helper(line):
 """ Example:
old: {#garuqa#} 1) a) <ls>SUPARṆ. 1,3</ls>.
new: {#garuqa#} 1〉 a〉 <ls>SUPARṆ. 1,3</ls>.
〉 = Unicode RIGHT ANGLE BRACKET
 """
 newline = re.sub(r'( [0-9a-zα-ωΑ-Ω][0-9a-zα-ωΑ-Ω]?)\)',r'\1〉',line)
 return newline

def adjust_3_helper(line):
 """ Example:
old: {#agnigarBa#} 2〉c).
new: {#agnigarBa#} 2〉c〉.
 """
 newline = re.sub(r'(〉[0-9a-zα-ωΑ-Ω])\)',r'\1〉',line)
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
   if option == '1':  # div
    newline = adjust_1_helper(line)
   elif option == '2':
    newline = line
    newline = re.sub(r' ([0-9]+)\)([a-z])\)([α-ωΑ-Ω])\)',
                     r' \1〉\2〉\3〉',newline)    # no space
    newline = re.sub(r' ([0-9]+)\)([0-9])\)([0-9])\)',
                     r' \1〉 \2〉 \3〉',newline)  # space
    
    newline = re.sub(r' ([0-9]+)\)([a-z])\)',  r' \1〉\2〉',newline)
    newline = re.sub(r' ([0-9]+)\) ([a-z])\)', r' \1〉\2〉',newline)
    newline = re.sub(r' ([0-9]+)\) ([a-z])\.', r' \1〉\2〉.',newline)

    newline = re.sub(r' ([0-9]+)\)([0-9])\)',  r' \1〉 \2〉',newline)
   elif option == '3':
    newline = re.sub(r'( [*]?[0-9a-zα-ωΑ-Ω])\)', r'\1〉',line)
    newline = re.sub(r'( [0-9]+)\)\.', r'\1〉.',newline)
   else:
    print('option ERROR:"%s"' %option)
    exit(1)
  #if iline == 20:print('check2:\nold:%s\nnew:%s' %(line,newline))
  
  if newline != line:
   nchg = nchg + 1
   # get rid of extra spaces
   # newline = re.sub(r'  +',' ',newline)
  newlines.append(newline)
 print(nchg,"lines changed for option",option)
 return newlines

def write(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for line in lines:
   f.write(line + '\n')
 print(len(lines),"written to",fileout)
 
if __name__=="__main__":
 options = ['1','2','3']
 #options = ['1','2a']
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] # revised xxx.txt
 lines = read_lines(filein)
 newlines = lines
 for option in options:
  newlines = adjust(newlines,option)

 write(fileout,newlines)
 #check_hom_recs()
 
