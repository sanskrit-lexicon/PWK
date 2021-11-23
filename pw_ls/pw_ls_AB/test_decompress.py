#-*- coding:utf-8 -*-
"""make_numberchange2b.py
"""
from __future__ import print_function
import sys, re,codecs
from make_numberchange2b import lsnumstr_to_intseq, decompress

if __name__=="__main__":
 x = sys.argv[1]
 seq,flag = lsnumstr_to_intseq(x)
 print(flag,seq)
 if flag:
  d,flag1 = decompress(seq)
  print(flag1,d)
