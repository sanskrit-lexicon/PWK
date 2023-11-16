#-*- coding:utf-8 -*-
"""step234.py
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

def adjust_blob_2(blob,dbg=False):
 # Step-2: merging consecutive <ls n="Chr.
 # </ls>. <ls n="Chr.(.*?)"> -> '. '
 newblob = re.sub(r'</ls>[.] <ls n="Chr[.](.*?)">',
                  r'. ',blob)
 
 lines = blob_to_lines(blob)
 newlines = blob_to_lines(newblob)
 assert len(lines) == len(newlines)
 n = 0 
 for i,line in enumerate(lines):
  newline = newlines[i]
  if newline != line:
   n = n + 1
 print(n,'differences via adjust_blob_2')
 if dbg:
  fileout = 'temp_blob_2.txt'
  write_lines(fileout,newlines)
 return newblob

def adjust_blob_3(blob,dbg=False):
 # Step-3: removing the italic terminations around [Pagexxx]
 # %} \[Page(.*?)\] {% -> ' [Page\1] '
 newblob = re.sub(r'%} \[Page(.*?)\] {%',
                  r' [Page\1] ',blob)
 
 lines = blob_to_lines(blob)
 newlines = blob_to_lines(newblob)
 assert len(lines) == len(newlines)
 n = 0 
 for i,line in enumerate(lines):
  newline = newlines[i]
  if newline != line:
   n = n + 1
 print(n,'differences via adjust_blob_3')
 if dbg:
  fileout = 'temp_blob_3.txt'
  write_lines(fileout,newlines)
 return newblob

def adjust_blob_4(blob,dbg=False):
 # Step-4 After <pc> and [Page
 # a insert '-' after the first (volume) digit
 newblob = re.sub(r'(<pc>.)', r'\1-',blob)
 newblob = re.sub(r'(\[Page.)',r'\1-',newblob)
 # b) Change the ending (column) digit -[123] to a letter -[abc] resp.
 def f_4b1(m):
  d = {'1':'a', '2':'b', '3':'c'}
  a = m.group(1)
  b = m.group(2)
  b1 = d[b]
  ans = '%s-%s<' %(a,b1)
  return ans
 newblob = re.sub(r'(<pc>.*?)-(.)<',f_4b1,newblob)
 
 def f_4b2(m):
  d = {'1':'a', '2':'b', '3':'c'}
  a = m.group(1)
  b = m.group(2)
  b1 = d[b]
  ans = '%s-%s]' %(a,b1)
  return ans
 newblob = re.sub(r'(\[Page.*?)-(.)\]',f_4b2,newblob)
 
 lines = blob_to_lines(blob)
 newlines = blob_to_lines(newblob)
 assert len(lines) == len(newlines)
 n = 0 
 for i,line in enumerate(lines):
  newline = newlines[i]
  if newline != line:
   n = n + 1
 print(n,'differences via adjust_blob_4')
 if dbg:
  fileout = 'temp_blob_4.txt'
  write_lines(fileout,newlines)
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
 blob_2 = adjust_blob_2(blob,dbg=True)
 blob_3 = adjust_blob_3(blob_2,dbg=True)
 blob_4 = adjust_blob_4(blob_3,dbg=True)
 newblob = blob_4
 newlines = blob_to_lines(newblob)
 write_lines(fileout,newlines)
