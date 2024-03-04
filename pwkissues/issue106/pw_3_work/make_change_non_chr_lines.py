# coding=utf-8
""" make_change_non_chr_lines.py
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 print(len(lines),"from",filein)
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
 def __init__(self,metaline,lnum,old,new,status):
  self.metaline = metaline
  self.lnum = lnum
  self.old = old
  self.new = new
  self.status = status

def write_changes_helper(changes,option,status):
 status_msgs = {
  1: '√{#X#}¦',
  2: '*√{#X#}¦',
  3: '<hom>Y</hom> √{#X#}¦',
  4: '<hom>Y</hom> *√{#X#}¦',
  5: 'other - may require metaline change'
  }
 outrecs = []
 outarr = [] # header
 outarr.append('; ******************************************************')
 outarr.append('; %s.%s: %s changes %s' % (option,status,len(changes),status_msgs[status]))
 outarr.append('; ******************************************************')
 outrecs.append(outarr)
 for c in changes:
  outarr = []
  outarr.append('; %s' % c.metaline)
  lnum = int(c.lnum)
  if status == 5:
   # possible metaline change
   outarr.append('; ALSO METALINE CHANGE')
   lnum_meta = lnum - 1
   outarr.append('%s old %s' %(lnum_meta,c.metaline))
   outarr.append('%s new %s' %(lnum_meta,c.metaline))
   outarr.append(';')
  # change 
  outarr.append('%s old %s' %(lnum,c.old))
  outarr.append(';')
  outarr.append('%s new %s' %(lnum,c.new))
  outarr.append('; ----------------------------------------------')
  outrecs.append(outarr)
 return outrecs

def write_changes(fileout,changes,option):
 outrecs_all = []
 for status in [1,2,3,4,5]:
  changes1 = [c for c in changes if c.status == status]
  outrecs1 = write_changes_helper(changes1,option,status)
  for out in outrecs1:
   outrecs_all.append(out)
 write_recs(fileout,outrecs_all,blankflag=False)

def make_change_helper(old,bbdata):
 before,after = old.split('¦')
 assert bbdata.endswith('¦')
 before_new = bbdata[0:-1] # remove ¦
 # 1 √{#X#}¦
 m = re.search(r'^√{#[^#]*#}$',before_new)
 if (m != None) and (before_new.replace('√','') == before):
  status = 1
  new = before_new + '¦' + after
  return (new,status)
 # 2 *√{#X#}¦  
 m = re.search(r'^\*√{#[^#]*#}$',before_new)
 if (m != None) and (before_new.replace('√','') == before):
  status = 2
  new = before_new + '¦' + after
  return (new,status)
 # 3 <hom>Y</hom> √{#X#}¦
 m = re.search(r'^<hom>[^<]*</hom> √{#[^#]*#}$',before_new)
 if (m != None) and (before_new.replace('√','') == before):
  status = 3
  new = before_new + '¦' + after
  return (new,status)
 # 4 <hom>Y</hom> *√{#X#}¦
 m = re.search(r'^<hom>[^<]*</hom> \*√{#[^#]*#}$',before_new)
 if (m != None) and (before_new.replace('√','') == before):
  status = 4
  new = before_new + '¦' + after
  return (new,status)
 # 5 other
 status = 5
 new = before_new + '¦' + after
 return (new,status)

def get_previous_metaline(lines,iline):
 while iline > 0:
  iline = iline - 1
  prevline = lines[iline]
  if prevline.startswith('<L>'):
   return prevline
 return None

def make_changes(lines,recs,nonchrs):
 # recs list of Citation_lines
 changes = []
 #statuses = [0,0,0,0,0]  # count of status from make_change_helper
 statuses = [0]  # status not really needed
 for rec in recs:
  lnum = rec.lnum  # line number of bbline
  cdsl = rec.cdsl
  ab   = rec.ab
  iline = lnum - 1
  old = lines[iline]  # old bb-line
  assert cdsl == old
  new = ab
  metaline = get_previous_metaline(lines,iline)
  assert metaline.startswith('<L>')
  status = 1  # superfluous
  change = Change(metaline,lnum,old,new,status)
  statuses[status-1] = statuses[status-1] + 1
  changes.append(change)
 print(len(changes),"changes")
 print('statuses = ',statuses)
 return changes

class Citation_lines:
 def __init__(self,group):
  # group is a list of 4 strings
  (a,b,c,d) = group
  self.lnum = int(a)
  self.cdsl = re.sub(r'\(CDSL\): *','',b)
  self.ab   = re.sub(r'\(AB\): *','',c)
  d1 = d.replace('-','')
  if d1 != '':
   print('WARNING citationlines',group)

def citation_line_groups(a,k):
 # a is a list or tuple
 assert k > 0
 n = len(a) # any list
 assert n > 0
 q,r = divmod(n,k)
 assert r == 0
 # q is the number of groups of size k
 # range(q) = {0,...,q-1}
 groups = [a[i*k : (i+1)*k] for i in range(q)]
 if True:
  print('n=%s, k=%s, q=%s, len(groups)=%s' %(n,k,q,len(groups)))
 return groups

def init_citation_lines(filein):
 lines = read_lines(filein)
 groups = citation_line_groups(lines,4)
 recs = []
 for group in groups:
  rec = Citation_lines(group)
  recs.append(rec)
 print(len(recs),"records initialized from",filein)
 return recs 

if __name__=="__main__":
 filein = sys.argv[1]  # pw.txt
 filein1 = sys.argv[2] #  non-Chr.citation.lines.txt (from AB)
 filein2 = sys.argv[3] # non-Chr.citations.txt
 fileout = sys.argv[4]  # change file 

 lines = read_lines(filein)
 recs = init_citation_lines(filein1)
 nonchrs = read_lines(filein2)
 changes = make_changes(lines,recs,nonchrs)
 write_changes(fileout,changes,'06')
