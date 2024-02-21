# coding=utf-8
""" possible_roots1.py
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for out in lines:
   f.write(out+'\n')  
 print(len(lines),"lines written to",fileout)

def write_recs(fileout,outrecs,printflag=True,blankflag=True):
 # outrecs is array of array of lines
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
   if blankflag:
    out = ''  # blank line separates recs
    f.write(out+'\n')
 if printflag:
  print(len(outrecs),"records written to",fileout)

class Change:
 def __init__(self,metaline,lnum,old,new):
  self.metaline = metaline
  self.lnum = lnum
  self.old = old
  self.new = new

def make_changes(lines):
 #regex1 = r'^[*]?{#[kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh|][aAiIuUfFxXeEoOMH][kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh|]#}¦'
 #regex2 = r'^<hom>[^<]*</hom> [*]?{#[kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh|][aAiIuUfFxXeEoOMH][kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh|]#}¦'
 # ends in consonantconsonant
 # regex1 
 regex1 = r'[*]?{#[^#]*[kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh|]#}¦ [*]?{#[^#]*at[ie]#}'
 regex2 = r'[*]?{#[^#]*[kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh|]#}¦,? [*]?{#[^#]*at[ie]#}'
 regex3 = r'[*]?{#[^#]*[kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh|]#}¦,? [*]?{#[^#]*ita#}'
 regex4 = r'[*]?{#[^#]*[kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh|]#}¦,? [*]?{#[^#]*am#}'
 regex5 = r'[*]?{#[^#]*[kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh|]#}¦,? [*]?{#[^#]*mA[nR]a#}'

 changes = [] # match regex1 or regex2

 for iline,line in enumerate(lines):
  m = re.search(r'(<L>.*)$',line)
  if not line.startswith('<L>'):
   continue
  metaline = line
  iline1 = iline + 1
  old = lines[iline1] # broken-bar line
  lnum = iline1 + 1
  new = None
  before,after = old.split('¦')
  if '√' in before:
   continue # already marked as a root
  if re.search(regex1,old):
   change = Change(metaline,lnum,old,new)
   changes.append(change)
  elif re.search(regex2,old):
   change = Change(metaline,lnum,old,new)
   changes.append(change)
  elif re.search(regex3,old):
   change = Change(metaline,lnum,old,new)
   changes.append(change)
  elif re.search(regex4,old):
   change = Change(metaline,lnum,old,new)
   changes.append(change)
  elif re.search(regex5,old):
   change = Change(metaline,lnum,old,new)
   changes.append(change)
 return changes

def write_changes(fileout,changes):
 outrecs = []
 outarr = [] # header
 outarr.append('; ******************************************************')
 outarr.append('; %s possible roots :' % len(changes))
 outarr.append('; ******************************************************')
 outrecs.append(outarr)
 for c in changes:
  outarr = []
  outarr.append('%s\t%s' % (c.old,c.metaline))
  #lnum = int(c.lnum)
  # change 
  #outarr.append(c.old)
  outrecs.append(outarr)
 write_recs(fileout,outrecs,blankflag=True)

if __name__=="__main__":
 filein = sys.argv[1]  # pw.txt
 fileout = sys.argv[2]  # 

 lines = read_lines(filein)
 changes = make_changes(lines)
 write_changes(fileout,changes)

