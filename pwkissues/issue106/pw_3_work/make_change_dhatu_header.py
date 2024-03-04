# coding=utf-8
""" make_change_dhatu_header.py
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

def make_changes(lines,recs):
 changes = []
 statuses = [0,0,0,0,0]  # count of status from make_change_helper
 for rec in recs:
  lnum = rec.lnum  # line number of bbline
  bbdata = rec.bbdata
  iline = lnum - 1
  old = lines[iline]  # old bb-line
  metaline = lines[iline-1]
  assert metaline.startswith('<L>')
  new,status = make_change_helper(old,bbdata)
  change = Change(metaline,lnum,old,new,status)
  statuses[status-1] = statuses[status-1] + 1
  changes.append(change)
 print(len(changes),"changes")
 print('statuses = ',statuses)
 return changes

class Dhatu_header:
 def __init__(self,lnum,bbdata):
  self.lnum = int(lnum)
  self.bbdata = bbdata
  
def init_dhatu_header(filein):
 lines = read_lines(filein)
 recs = []
 for line in lines:
  (lnum,bbdata) = line.split('\t')
  rec = Dhatu_header(lnum,bbdata)
  recs.append(rec)
 return recs

if __name__=="__main__":
 filein = sys.argv[1]  # pw.txt
 filein1 = sys.argv[2] # dhAtu.header.lines.txt (from AB)
 fileout = sys.argv[3]  # change file 

 lines = read_lines(filein)
 recs = init_dhatu_header(filein1)
 changes = make_changes(lines,recs)
 write_changes(fileout,changes,'05')
 """
 exit(1)
 lines1a = [x for x in lines1 if '¦' in x]  
 lines2 = read_lines(filein2) # ab
 lines2a = [x for x in lines2 if '¦' in x]
 print(len(lines1a),len(lines2a))
 assert len(lines1a) == len(lines2a)
 # lines1a and lines2a are 'parallel'; i.e.
 # arrays have same length and 
 # lines1a[i] is comparable to lines2a[i]
 lines2b = adjust_lines2a(lines2a, lines1a)
 
 iline_d = init_bb_iline_dict(lines)
 iline_d1 = init_bb_iline_dict1(lines1a,iline_d)
 changeFname = 'make_changes_%s' %option
 changeF = locals()[changeFname]
 changes,new_lines1a = changeF(lines1a,lines2b,iline_d1,lines,option)
 write_changes(fileout,changes,option)
 write_lines(fileout1,new_lines1a)
  """


