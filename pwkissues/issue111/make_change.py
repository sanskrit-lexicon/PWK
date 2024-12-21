#-*- coding:utf-8 -*-
"""make_change.py
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
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

def make_changes_line_species(line,dbg):
 # re.findall('<bot>[a-z].*?</bot>',line)
 botelts = re.findall(r'<bot>.*?</bot>',line)
 eltchgs = []
 newline = line
 defaultans = newline,[]
 if botelts == []:
  return defaultans
 probs = []
 for botelt in botelts:
  if dbg: print('botelt=',botelt)
  m = re.search(r'<bot>(.*?)</bot>',botelt)
  wordstr = m.group(1)
  words = wordstr.split(' ')
  if len(words) < 2:
   continue
  word2 = words[1] # 2nd word - species
  word2a = word2.lower()
  if dbg: print('word2=%s, word2a=%s' %(word2,word2a))
  if word2a == word2:
   # no problem. Go to next botelt
   continue
  # We have a change.
  # First, make new bot element
  words[1] = word2a
  wordstrnew = ' '.join(words)
  boteltnew = '<bot>%s</bot>' % wordstrnew
  eltchg = '%s -> %s' % (botelt,boteltnew)
  eltchgs.append(eltchg)
  # Second, update newline
  newline = newline.replace(botelt,boteltnew)
 return newline,eltchgs

def make_changes_line_genus(line,dbg):
 botelts = re.findall(r'<bot>.*?</bot>',line)
 eltchgs = []
 newline = line
 defaultans = newline,[]
 if botelts == []:
  return defaultans
 probs = []
 for botelt in botelts:
  if dbg: print('botelt=',botelt)
  m = re.search(r'<bot>(.*?)</bot>',botelt)
  wordstr = m.group(1)
  words = wordstr.split(' ')
  if len(words) != 2:
   continue
  word1 = words[0] # 1st word - genus
  word2 = words[1] # 2nd word - species
  word1a = word1.capitalize()
  if word1a == word1:
   # no problem. Go to next botelt
   continue
  # We have a change.
  # First, make new bot element
  words[0] = word1a
  wordstrnew = ' '.join(words)
  boteltnew = '<bot>%s</bot>' % wordstrnew
  eltchg = '%s -> %s' % (botelt,boteltnew)
  eltchgs.append(eltchg)
  # Second, update newline
  newline = newline.replace(botelt,boteltnew)
 return newline,eltchgs

def make_changes_line_paren(line,dbg):
 botelts = re.findall(r'<bot>.*?</bot>',line)
 eltchgs = []
 newline = line
 defaultans = newline,[]
 if botelts == []:
  return defaultans
 probs = []
 for botelt in botelts:
  if dbg: print('botelt=',botelt)
  m = re.search(r'<bot>(.*?)</bot>',botelt)
  wordstr = m.group(1)
  m = re.search(r'^([^ ]+) \((.*?)\) (.*)$',wordstr)
  if m == None:
   continue
  word1 = m.group(1)
  word2 = m.group(2)
  word3 = m.group(3)
  word1a = word1.capitalize() # genus
  word2a = word2.capitalize() # alternate genus
  word3a = word3.lower() # species
  # We have a change.
  # First, make 1st bot element
  botelt1 = '<bot>%s %s</bot>' % (word1a,word3a)
  botelt2 = '<bot>%s %s</bot>' % (word2a,word3a)
  boteltnew = '%s (%s)' %(botelt1, botelt2)
  eltchg = '%s -> %s' % (botelt,boteltnew)
  eltchgs.append(eltchg)
  # Second, update newline
  newline = newline.replace(botelt,boteltnew)
 return newline,eltchgs

def make_changes_line_single(line,dbg):
 botelts = re.findall(r'<bot>.*?</bot>',line)
 eltchgs = []
 newline = line
 defaultans = newline,[]
 if botelts == []:
  return defaultans
 probs = []
 for botelt in botelts:
  if dbg: print('botelt=',botelt)
  m = re.search(r'<bot>(.*?)</bot>',botelt)
  wordstr = m.group(1)
  if ' ' in wordstr:
   continue
  # make a formal change, although unchanged
  # use 'botx' to facilitate editing
  # most of these are different species for prior genus-species
  m = re.search(r'<bot>([^ <]+) ([^ <]+)</bot>%} oder {%' + botelt,line)
  if m != None:
   genus = m.group(1).capitalize()
   species1 = m.group(2)
   species = wordstr.lower()
   boteltnew = '<boty>%s %s</bot>' %(genus,species)
  else:
   boteltnew = '<botx>%s</bot>' % wordstr
  eltchg = '%s -> %s' % (botelt,boteltnew)
  eltchgs.append(eltchg)
  # Second, update newline
  newline = newline.replace(botelt,boteltnew)
 return newline,eltchgs

def make_changes(lines,option):
 changes = []
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   metaline = line
   continue
  lnum = iline + 1
  #dbg = (lnum == 223579)
  dbg = False
  if option == 'species':
   newline,eltchgs = make_changes_line_species(line,dbg)
  elif option == 'genus':
   newline,eltchgs = make_changes_line_genus(line,dbg)
  elif option == 'paren':
   newline,eltchgs = make_changes_line_paren(line,dbg)
  elif option == 'single':
   newline,eltchgs = make_changes_line_single(line,dbg)
  else:
   print('unknown option',option)
   exit(1)
  if True and dbg:
   print(line)
   print(newline)
   print(eltchgs)
   exit(1)
  if newline == line:
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

if __name__=="__main__":
 option = sys.argv[1]
 filein = sys.argv[2] #  xxx.txt 
 fileout = sys.argv[3] #
 lines = read_lines(filein)
 print(len(lines),"lines read from",filein)
 changes = make_changes(lines,option)
 write_changes(fileout,changes)

