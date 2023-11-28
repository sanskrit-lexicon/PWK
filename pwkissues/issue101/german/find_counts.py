# coding=utf-8
""" italic_word_change.py
"""
from __future__ import print_function
import sys, re,codecs
import digentry  

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines
 
class Input:
 def __init__(self,old,new,inputcount):
  self.old = old
  self.new = new
  self.inputcount = inputcount
  self.anycount = 0  # filled in by compare function
  
def init_correction_input(filein):
 lines = read_lines(filein)
 d = {}
 recs = []
 for iline,line in enumerate(lines):  
  m = re.search(r'^([0-9]+) (.*)$',line)
  inputcount = int(m.group(1))
  rest = m.group(2)
  (old,new) = rest.split('->')
  old = old.strip()
  new = new.strip()
  if old in d:
   print('unexpected duplicate:',old)
  rec = Input(old,new,inputcount)
  d[old] = rec
  recs.append(rec)
 print("init_correction_input:",len(lines),"read from",filein)
 return d,recs

class Change(object):
 def __init__(self,metaline,lnum,line,newline,inputs):
  self.metaline = metaline
  self.lnum = lnum
  self.line = line
  self.newline = newline
  self.inputs_applied = inputs

def italic_changes(text,d):
 parts = re.split(r'(\w+)',text)
 newparts = []
 inputs = []  
 for part in parts:
  if part in d:
   rec = d[part]
   old = part
   new = rec.new
   rec.changecount = rec.changecount + 1
   inputs.append(rec)
   newparts.append(new)
  else:
   newparts.append(part)
 newtext = ''.join(newparts)
 return newtext,inputs

def line_changes(line,dinput):
 ans = [] # array of changes
 # restrict to italic text
 inputs_applied = []
 parts = re.split(r'({%.*?%})',line)
 newparts = []
 changes = []
 for part in parts:
  if part.startswith('{%'):
   newpart,partinputs = italic_changes(part,dinput)
   for input in partinputs:
    inputs_applied.append(input)
  else:
   newpart = part
  newparts.append(newpart)
 newline = ''.join(newparts)
 return newline,inputs_applied

def find_all(a_str, sub):
  result = []
  start = 0
  while True:
    start = a_str.find(sub, start)
    if start == -1: 
      return result
    result.append(start)
    start += len(sub) # use start += 1 to find overlapping matches

def findany_line(line,inputs):
 for input in inputs:
  indexes = find_all(line,input.old)
  n = len(indexes)
  input.anycount = input.anycount + n
  
def findany(entries,inputs):
 dbg = False
 changes = []
 for ientry,e in enumerate(entries):
  for iline,line in enumerate(e.datalines):
    findany_line(line,inputs) # updates input recs
 return changes

def write_outrecs(fileout,outrecs):
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outrecs),"cases written to",fileout)
 
def print_outrecs(outrecs):
 for outarr in outrecs:
  for out in outarr:
   print(out)


def write_outrecs(fileout,outrecs):
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outrecs),"cases written to",fileout)
 
def print_outrecs(outrecs):
 for outarr in outrecs:
  for out in outarr:
   print(out)


def write_changes(fileout,changes,dinput):
 outrecs=[]
 for change in changes:
  outarr=[]
  metaline = change.metaline
  inputs_applied = change.inputs_applied
  metaline = re.sub(r'<k2>.*$','',metaline)
  outarr.append('; %s' % metaline)
  # change info: 
  outarr.append('; broken bar position with other non-minor change(s)')
  lnum = change.lnum
  line = change.line
  newline = change.newline
  outarr.append('%s old %s' %(lnum,line))
  for input in inputs_applied:
   outarr.append('; %s -> %s' %(input.old,input.new))
  outarr.append(';')

  outarr.append('%s new %s' %(lnum,newline))
  outarr.append('; ------------------------------------------------------')
  outrecs.append(outarr)
  
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
    for out in outarr:
     f.write(out+'\n')
 print(len(changes),"changes written to",fileout)

def write_newinputs(fileout,inputrecs):
 outarr = []
 for rec in inputrecs:
  out = '%s %s %s -> %s' %(rec.inputcount, rec.anycount,rec.old,rec.new)
  outarr.append(out)
  
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out+'\n')
 print(len(inputrecs),"records written to",fileout)


if __name__=="__main__":
 filein = sys.argv[1] # xxx.txt cdsl
 filein1 = sys.argv[2] # correction input
 fileout = sys.argv[3] # inputs with observed counts
 dinput,inputrecs = init_correction_input(filein1)
 entries_cdsl = digentry.init(filein)
 findany(entries_cdsl,inputrecs)
 write_newinputs(fileout,inputrecs)
 
