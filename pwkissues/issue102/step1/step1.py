#-*- coding:utf-8 -*-
"""step1.py
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
 print(len(lines),"lines read from",filein)
 return lines

def read_blob(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  blob = f.read()
 return blob
 
def write_lines(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for line in lines:
   f.write(line + '\n')
 print(len(lines),"written to",fileout)

def adjust_blob_a(blob,dbg=False):
 # (a) <LEND>\n[ -> <LEND> [ ;; 682113 -> 679088 (-3025)
 newblob = blob.replace('<LEND>\n[','<LEND> [')
 # info
 lines = blob_to_lines(newblob)
 print('blob_a has',len(lines),'lines')
 return newblob

def adjust_blob_b(blob,dbg=False):
 # (b) \[Page(.*?)\]\n<LEND> -> <LEND> \[Page\1\] ;; 679088 -> 679068 (-20)
 newblob = re.sub('\[Page(.*?)\]\n<LEND>',
                  r'<LEND> [\1]',blob)
 # info
 lines = blob_to_lines(newblob)
 print('blob_b has',len(lines),'lines')
 if dbg:
  fileout = 'temp_blob_b.txt'
  write_lines(fileout,lines)
 return newblob

def adjust_blob_c(blob,dbg=False):
 # (c) ([^\n])\n\[Page(.*?)\]\n -> \1 \[Page\2\] ;; 679068 -> 673636 (-5432)
 newblob = re.sub('([^\n])\n\[Page(.*?)\]\n',
                  r'\1 [Page\2] ',blob)
 # info
 lines = blob_to_lines(newblob)
 print('blob_c has',len(lines),'lines')
 if dbg:
  fileout = 'temp_blob_c.txt'
  write_lines(fileout,lines)
 return newblob

def adjust_blob_d(blob,dbg=False):
 # (d) ] <div n= -> ]\n<div n= ;; 673636 -> 674062 (426)
 newblob = blob.replace('] <div n=',
                        ']\n<div n=')
 # info
 lines = blob_to_lines(newblob)
 print('blob_d has',len(lines),'lines')
 if dbg:
  fileout = 'temp_blob_d.txt'
  write_lines(fileout,lines)
 return newblob

def blob_to_lines(blob,dbg=False):
 lines = blob.split('\n')
 # remove empty line at end
 if lines[-1] == '':
  del lines[-1]
 return lines

def check_blob(lines,blob):
 newlines = blob_to_lines(blob)
 assert newlines == lines

if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] # modified xxx.txt
 lines = read_lines(filein)
 blob = read_blob(filein)
 check_blob(lines,blob)  
 blob_a = adjust_blob_a(blob,dbg=True)
 blob_b = adjust_blob_b(blob_a,dbg=True)
 blob_c = adjust_blob_c(blob_b,dbg=True)
 blob_d = adjust_blob_d(blob_c,dbg=True)
 newblob = blob_d
 newlines = blob_to_lines(newblob)
 write_lines(fileout,newlines)
