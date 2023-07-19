#-*- coding:utf-8 -*-
"""pw_transcode.py
"""
from __future__ import print_function
import sys, re,codecs
import transcoder
transcoder.transcoder_set_dir('transcoder')

slp1chars = {}
def update_slp1chars(x,y,tranin,tranout):
 if not ((tranin == 'roman') and (tranout == 'slp1')):
  return
 m = re.search(r"^[a-zA-Z|~/\\^— √°'+.,;=?\[\]\(\)!‘’*_3-]*$",y)
 if m == None:
  print('Unexpected character in line #%s' % (iline+1,))
  print(' x=',x)
  print(' y=',y)
 return
 
def convert(line,tranin,tranout):
 # convert text  in '{#X#}'
 def f(m):
  x = m.group(1)
  y = transcode(x,tranin,tranout)
  return '{#%s#}' %y

 regex = '{#(.*?)#}'
 lineout = re.sub(regex,f,line)
 return lineout

def print_unicode(u):
 """ Sample output:
 """
 import unicodedata
 outarr = []
 for c in u:
  name = unicodedata.name(c)
  icode = ord(c)
  a = f"{icode:04X} | {c} | {name}"
  outarr.append(a)
 return outarr

def transcode(x,tranin,tranout):
 y = transcoder.transcoder_processString(x,tranin,tranout)
 """
 #if True and (('|' in x) or ('Q' in x)):
 if False and ('~' in x):  # for debugging.
  print_unicode(x,y)
 update_slp1chars(x,y,tranin,tranout)
 """
 return y


def test():
 x = sys.argv[1]  # slp1 text
 fileout = "temp_test.txt"
 outarr = []
 outarr.append(x)
 y = transcode(x,'slp1','deva1')
 outarr.append(y)
 for out in print_unicode(y):
  outarr.append('  %s' % out)
 z = transcode(y,'deva1','slp1')
 outarr.append(z)
 for out in print_unicode(z):
  outarr.append('  %s' % out)
 
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out+'\n')
 print('check results in ',fileout)
 exit(1)
 
if __name__=="__main__":
 test()
