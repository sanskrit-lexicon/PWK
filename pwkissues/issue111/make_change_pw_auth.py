#-*- coding:utf-8 -*-
"""make_change_pw_auth.py
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def read_linesdbg(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = []
  for i,x in enumerate(f):
   if i > 10:
    print('debug i=',i)
   try:
    line = x.rstrip('\r\n')
    lines.append(line)
   except:
    lnum = i + 1
    print('read_linesdbg: Problem at line#',lnum)
    exit(1)
 return lines

def write_lines(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for line in lines:
   f.write(line+'\n')  
 print(len(lines),"written to",fileout)

def write_recs(fileout,outrecs):
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for line in outarr:
    f.write(line+'\n')  
 print(len(outrecs),"change records written to",fileout)

class Change:
 def __init__(self,metaline,lnum,line,newline,comments):
  self.metaline = metaline
  self.lnum = lnum
  self.line = line
  self.newline = newline
  self.comments = comments

def make_changes_line(line,d,option):
 botelts = re.findall(r'<bot>.*?</bot>',line)
 eltchgs = []
 newline = line
 if botelts == []:
  return newline,[]
 for botelt in botelts:
  m = re.search(r'<bot>([^ ]+) ([^ ]+) (.*?)</bot>',botelt)
  if m == None:
   continue # no auth
  auth = m.group(3)
  if auth in d:
   # auth presumed ok. no change
   continue
  # option requires either auth to start with upper case or lower case
  c = auth[0]
  clo = c.lower()
  loflag = (c == clo)
  if (option == 'lo'):
   if not loflag:
    continue
  elif (option == 'up'):
   if loflag:
    continue
   else:
    print('unknown option',option)
    exit(1)
  newelt = botelt.replace('<bot>','<botx>')
  newline = newline.replace(botelt,newelt)
  
  # We have a change.
  eltchg = 'Unknown auth'
  eltchgs.append(eltchg)
  eltchgs.append('change type = unknown auth %s' % auth)
 return newline,eltchgs

def make_changes(lines,d,option):
 changes = []
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   metaline = line
   continue
  lnum = iline + 1
  newline,eltchgs = make_changes_line(line,d,option)
  if eltchgs == []:
   continue
  comments = eltchgs
  change = Change(metaline,lnum,line,newline,comments)
  changes.append(change)
 print(len(changes),"Change records returned by make_changes")
 return changes

def write_changes(fileout,changes):
 outrecs = []
 for c in changes:
  outarr = []
  # '*' for org-mode
  #outarr.append('* TODO ; %s' % c.metaline)
  outarr.append('; %s' % c.metaline)
  for comment in c.comments:
   # outarr.append('; ' + comment)
   outarr.append('; %s ' % comment)
  outarr.append('%s old %s' % (c.lnum,c.line))
  outarr.append(';')
  outarr.append('%s new %s' % (c.lnum,c.newline))
  outarr.append('; --------------------------------------------------')
  outrecs.append(outarr)
 write_recs(fileout,outrecs)

def init_known_authd(lines):
 d = {}
 for line in lines:
  try:
   auth,count = line.split('\t')
  except:
   print('ERROR in initi_unknown_authd')
   print(line)
   exit(1)
  d[auth] = True
 return d

if __name__=="__main__":
 option = sys.argv[1] # lo, up
 filein = sys.argv[2] #  xxx.txt
 filein1 = sys.argv[3] # pw_botauth_unknown.txt
 
 fileout = sys.argv[4] # 
 lines = read_lines(filein)
 print(len(lines),"lines read from",filein)
 lines1 = read_lines(filein1)
 print(len(lines1),"lines read from",filein1)
 d = init_known_authd(lines1)
 
 changes = make_changes(lines,d,option)
 write_changes(fileout,changes)

