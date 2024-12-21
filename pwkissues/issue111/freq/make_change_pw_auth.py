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

def make_changes_line(line,dbg,d):
 botelts = re.findall(r'<bot>.*?</bot>',line)
 eltchgs = []
 newline = line
 if dbg: print(line)
 if dbg: print('botelts=',botelts)
 if botelts == []:
  return newline,[]
 for botelt in botelts:
  if dbg: print('botelt=',botelt)
  if botelt not in d:
   if dbg: print('bot not in d' )
   continue
  rec = d[botelt]
  if dbg: print('rec.newelt = %s' % rec.newelt)
                 
  if rec.newelt != None:
   newline = newline.replace(rec.botelt,rec.newelt)
  
  # We have a change.
  eltchg = rec.line
  eltchgs.append(eltchg)
  eltchgs.append('change type = %s' % rec.type)
 return newline,eltchgs

def make_changes(lines,d):
 changes = []
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   metaline = line
   continue
  lnum = iline + 1
  dbg = False
  # dbg = (iline == 31585)
  newline,eltchgs = make_changes_line(line,dbg,d)
  if False and dbg:
   print(line)
   print(newline)
   print(eltchgs)
   exit(1)
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

class Rec:
 def __init__(self,line):
  self.line = line
  m = re.search(r'^<bot>(.*?)</bot>$',line)
  self.bot = m.group(1)
  self.botelt = '<bot>%s</bot>' % self.bot
  self.count = 0
  self.gsinfo = None
  self.rest = None
  self.used = False
  self.newelt = None
  self.type = 'manual'
def init_recs(lines):
 recs = [Rec(line) for line in lines]
 d = {}
 for rec in recs:
  d[rec.botelt] = rec
 return recs,d

if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt
 filein1 = sys.argv[2] # bot_freq_pw_2_gs_00.txt 
 fileout = sys.argv[3] # .org
 lines = read_lines(filein)
 print(len(lines),"lines read from",filein)
 lines1 = read_lines(filein1)
 print(len(lines1),"lines read from",filein1)
 recs,d = init_recs(lines1)
 
 changes = make_changes(lines,d)
 write_changes(fileout,changes)

