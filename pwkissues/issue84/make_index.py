# coding=utf-8
""" make_index.py for mbhbomb
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
 # vol., page, parvan, adhy   fromv, tov., ipage, remark(s)
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

def alter_missing1(lines):
 newlines = []
 prev = None
 for iline,line in enumerate(lines):
  parts = line.split('\t')
  adhy = parts[3]
  fromv = parts[4]
  tov = parts[5]
  if adhy != '':
   newline = line
   prev = parts[3:6]
  else: # adhy == ''
   assert fromv == ''
   assert tov == ''
   newparts = parts
   newparts[3:6] = prev
   newline = '\t'.join(newparts)
   prev = newparts[3:6]
  newlines.append(newline)
 return newlines

def alter_missing2(lines):
 newlines = []
 prev = None
 for iline,line in enumerate(lines):
  parts = line.split('\t')
  parvan = parts[2]
  adhy = parts[3]
  fromv = parts[4]
  tov = parts[5]
  ipage = parts[6]
  if parvan == '---':  # will handle this later
   newline = line
   prev = parts[2:7]
   
  if ipage != '---':
   newline = line
   prev = parts[2:7]
  else: # ipage == '---'
   assert adhy == '---'
   assert fromv == '---'
   assert tov == '---'
   newparts = parts
   newparts[2:7] = prev
   newline = '\t'.join(newparts)
   prev = newparts[2:7]
  newlines.append(newline)
 return newlines

def alter_missing3(lines):
 # ipage not missing AND parvan not missing
 # AND adhy,fromv,tov missing
 newlines = []
 prev = None
 for iline,line in enumerate(lines):
  parts = line.split('\t')
  parvan = parts[2]
  adhy = parts[3]
  fromv = parts[4]
  tov = parts[5]
  ipage = parts[6]
  if (ipage != '---') and (parvan != '---') and (adhy == '---'):
   assert fromv == '---'
   assert tov == '---'
   newparts = parts
   newparts[3:6] = prev
   newline = '\t'.join(newparts)
   prev = newparts[3:6]
  else:
   newline = line
   prev = parts[3:6]
  newlines.append(newline)
 return newlines

def alter_missing4(lines):
 # all but vol, page are missing
 newlines = []
 prev = None
 x = ['---','---','---','---','---']
 for iline,line in enumerate(lines):
  parts = line.split('\t')
  y = parts[2:7]
  if y == x:
   newparts = parts
   newparts[2:7] = prev
   newline = '\t'.join(newparts)
  else:
   prev = y
   newline = line
  newlines.append(newline)
 return newlines

def alter_missing5(lines):
 # all but vol, page are missing
 newlines = []
 prevline = None
 for iline,line in enumerate(lines):
  parts = line.split('\t')
  if parts[2:6] == ['---','---','---','---']:
   prevparts = prevline.split('\t')
   newparts = parts
   newparts[2:6] = prevparts[2:6]
   newline = '\t'.join(newparts)
  elif parts[4:6] == ['---','---']:
   prevparts = prevline.split('\t')
   newparts = parts
   newparts[4:6] = prevparts[4:6]
   newline = '\t'.join(newparts)
  else:
   newline = line
  newlines.append(newline)
  prevline = newline
 return newlines

correction_lines = (
 (
  '2	67	3	25	1	14	28b',
  '2	67	3	26	1	14	28b'
  ),
 
 )

def correct_line(line):
 for old,new in correction_lines:
  if old == line:
   return new
 return line

def corrections(lines):
 n = 0
 newlines = []
 for line in lines:
  newline = correct_line(line)
  newlines.append(newline)
  if newline != line:
   n = n + 1
 print(n,'lines corrected by corrections function')
 return newlines

if __name__ == "__main__":
 filein = sys.argv[1]  # index_orig
 fileout = sys.argv[2]  # index file
 # Currently, just a copy
 lines = read_lines(filein)
 lines1 = alter_missing1(lines)
 lines2 = alter_missing2(lines1)  # no ipage
 lines3 = alter_missing3(lines2)
 lines4 = alter_missing4(lines3)
 lines5 = alter_missing5(lines4)
 lines6 = corrections(lines5)
 outarr = lines6
 write_lines(fileout,outarr)

 
