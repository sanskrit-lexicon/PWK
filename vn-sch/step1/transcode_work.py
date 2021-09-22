#-*- coding:utf-8 -*-
"""transcode_work.py
 
 
"""
from __future__ import print_function
import sys, re,codecs
import transcoder
transcoder.transcoder_set_dir('transcoder')
import unicodedata

def test():
 outarr = []
 vowels = 'aAiIuUfFxXeEoO'
 accents = '/\\^'
 for vowel in vowels:
  for accent in accents:
   x = vowel + accent
   d = transcoder.transcoder_processString(x,'slp1','deva1')  # pwg, pwk convention
   y = transcoder.transcoder_processString(x,'slp1','roman1')   
   z = y.upper()
   w1a = []
   w2a = []
   for tmp in y:
    w1a.append('\\u%04x' %ord(tmp))
    w2a.append(unicodedata.name(tmp))
   w1 = ''.join(w1a)
   w2 = ','.join(w2a)
   w = '%s %s' %(w1,w2)
   outarr.append('%s %s-> %s AND %s %s' %(x,d,y,z,w))
 # L and |
 outarr.append('-------------------------------------------')
 for x in ['L','|']:
   d = transcoder.transcoder_processString(x,'slp1','deva1')  # pwg, pwk convention
   y = transcoder.transcoder_processString(x,'slp1','roman1')   
   z = y.upper()
   w1a = []
   w2a = []
   for tmp in y:
    w1a.append('\\u%04x' %ord(tmp))
    w2a.append(unicodedata.name(tmp))
   w1 = ''.join(w1a)
   w2 = ','.join(w2a)
   w = '%s %s' %(w1,w2)
   outarr.append('%s %s-> %s AND %s %s' %(x,d,y,z,w))
  
 return outarr

def test1():
 outarr = []
 x = 'Denu/H.'
 y = transcoder.transcoder_processString(x,'slp1','deva1')
 z = transcoder.transcoder_processString(y,'deva1','slp1')
 outarr.append('%s -> %s -> %s' %(x,y,z))
 for tmp in y:
  outarr.append('\\u%04x  %s' % (ord(tmp),unicodedata.name(tmp)))
 return outarr

def test2():
 outarr = []
 x = 'arcatri/a'
 y = transcoder.transcoder_processString(x,'slp1','deva1')
 z = transcoder.transcoder_processString(y,'deva1','slp1')
 outarr.append('%s -> %s -> %s' %(x,y,z))
 for tmp in y:
  outarr.append('\\u%04x  %s' % (ord(tmp),unicodedata.name(tmp)))
 return outarr

if __name__=="__main__":
 fileout = sys.argv[1] # 
 #outrecs = test()
 outrecs = test2()
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outrecs:
   f.write(out + '\n')
 print('results printed to',fileout)
