# coding=utf-8
""" make_index_orig.py for mbhbomb
"""
from __future__ import print_function
import sys, re, codecs
# import json

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"cases written to",fileout)

def drop_pages(lines,drops):
 newlines = []
 for line in lines:
  parts = line.split('\t')
  page = int(parts[1])
  if page in drops:
   pass
  else:
   newlines.append(line)
 return newlines

def alter_missing(lines):
 # vol., page, sarga, from v., to v., ipage, remark(s)
 #  0     1      2*     3*       4*       5      6
 newlines = []
 prev = None
 for line in lines:
  parts = line.split('\t')
  assert len(parts) == 7
  if parts[2] != '---':
   newline = line
  else:
   assert parts[3] == '---'
   assert parts[4] == '---'
   newparts = []
   prevparts = prev.split('\t')
   for ipart,part in enumerate(parts):
    if ipart == 2:
     newpart = prevparts[ipart]
    elif ipart == 3:
     newpart = prevparts[4]
    elif ipart == 4:
     newpart = prevparts[4]
    else:
     newpart = part
    newparts.append(newpart)
   newline = '\t'.join(newparts)
  newlines.append(newline)
  prev = newline
 return newlines

def drop_empty_remarks(lines):
 newlines = []
 nrk = 0 # number of non-empty remarks
 for line in lines:
  parts = line.split('\t')
  if len(parts) == 7:
   # no remark field
   newline = line
  elif len(parts) == 8:
   if parts[-1] == '':
    # empty remark
    newparts = parts[:-1]  # drop last part, remark field
    newline = '\t'.join(newparts)
   else:
    # non-empty remark
    nrk = nrk + 1
    # change to 'remark=' so searchable
    newparts = parts[:-1]
    newremark = 'remark=%s' %  parts[-1]
    newparts.append(newremark)
    newline = '\t'.join(newparts)
  newlines.append(newline)
 print(nrk,"lines with non-empty remark")
 return newlines

def inherit_tov(lines):
 newlines = []
 prev_tov = None
 for line in lines:
  parts = line.split('\t')
  assert len(parts) == 5  # we've already dropped remark
  fromv = parts[2]
  tov = parts[3]
  if fromv != '---':
   assert tov != '---'
   prev_tov = tov
   newlines.append(line)
  else:
   assert tov == '---'
   new_fromv = prev_tov
   new_tov = prev_tov
   parts[2] = new_fromv
   parts[3] = new_tov
   newline = '\t'.join(parts)
   newlines.append(newline)
 return newlines

def unused_adjust_lines(vol,lines):
 ans = []
 for iline,line in enumerate(lines):
  parts = line.split('\t')
  if len(parts) != 8:
   print('vol %s, line# %s has %s parts' % (vol,iline+1,len(parts)))
   print(line)
   #exit(1)
  if parts[7] != '':
   print(line)
  newline = '\t' . join(parts[0:7])
  ans.append(newline)
 return ans

if __name__ == "__main__":
 dirin = sys.argv[1]  # index_orig
 fileout = sys.argv[2]  # index file
 lines_all = []
 for vol in range(1,6+1):
  filein = 'indexes/index%s_orig.txt' % vol
  lines = read_lines(filein)
  if vol != 1:
   lines = lines[1:]  # drop title line
  lines_all = lines_all + lines
  #linesadj = adjust_lines(vol,lines)
  #for lineadj in linesadj:
  # outarr.append(lineadj)
 outarr = drop_empty_remarks(lines_all)
 write_lines(fileout,outarr)

 
 
