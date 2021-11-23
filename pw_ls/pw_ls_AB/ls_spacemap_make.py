#-*- coding:utf-8 -*-
""" ls_spacemap_make.py
"""
from __future__ import print_function
import sys, re,codecs

def ls_addspace(ls):
 ndot = len(re.findall(r'[.]',ls))
 lsnew = ls
 #if ndot == 0:
 # return lsnew
 if ls == 'VP.²':
  return lsnew
 # add a space after each comma
 lsnew = lsnew.replace(',' ,', ')
 # add a space after each period
 lsnew = lsnew.replace('.','. ')
 # add a space before each left-paren
 lsnew = lsnew.replace('(',' (')
 # remove spaces at end
 lsnew = re.sub(r' +$','',lsnew)
 # 1) remove multiple spaces
 lsnew = re.sub(r'  +',' ',lsnew)
 # 2) before )
 lsnew = lsnew.replace(' )',')')
 # 3) before ]
 lsnew = lsnew.replace(' ]',']')
 # special cases
 lsnew = lsnew.replace(' delab',' de la b')
 lsnew = lsnew.replace(' zu',' zu ')
 lsnew = lsnew.replace(' zu .',' zu.')
 lsnew = lsnew.replace(' deGr.',' de Gr.')
 return lsnew

class PWLS(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  m = re.search(r'^(.*) ([0-9]+)$',line)
  self.ls = m.group(1)
  self.count = m.group(2)
  self.lsnew = None
  ls = self.ls
  self.lsnew = ls_addspace(ls)
def init_pwls(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  recs = [PWLS(line) for line in f]
 return recs

def write_nochange(recs,fileout):
 with codecs.open(fileout,"w","utf-8") as f:
  for rec in recs:
   out = rec.ls
   f.write(out+'\n')
 print(len(recs),"written to",fileout)

def write_change(recs,fileout):
 with codecs.open(fileout,"w","utf-8") as f:
  for rec in recs:
   out = "%s : %s" %(rec.ls,rec.lsnew)
   assert ':' not in rec.ls
   f.write(out+'\n')
 print(len(recs),"written to",fileout)

def write_check(recs,fileout):
 with codecs.open(fileout,"w","utf-8") as f:
  for rec in recs:
   out = "%s %s" %(rec.lsnew,rec.count)
   f.write(out+'\n')
 print(len(recs),"written to",fileout)

if __name__=="__main__":
 filein = sys.argv[1] #  listls1_pw_06.txt
 fileout = sys.argv[2] # ls_spacemap
 fileout1 = sys.argv[3] # ls_nochange
 recs = init_pwls(filein)
 recs = sorted(recs,key = lambda x : x.lsnew)
 recs_change = [rec for rec in recs if rec.ls != rec.lsnew]
 write_change(recs_change,fileout)
 recs_nochange = [rec for rec in recs if rec.ls == rec.lsnew]
 write_nochange(recs_nochange,fileout1)
 if True:
  filename = "temp_spacemap_check.txt"
  write_check(recs,filename)
