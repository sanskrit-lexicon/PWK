# coding=utf-8
""" diff_to_changes_dict2.py
  
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def get_link(metaline):
 m = re.search(r'<L>(.*?)<pc>(.*?)<k1>',metaline)
 page = m.group(2)
 link = 'https://www.sanskrit-lexicon.uni-koeln.de/scans/csl-apidev/servepdf.php?dict=pw&page=%s' % page
 return link

def char_name(c):
 if c == '\t':
  return 'TAB'
 elif c == ' ':
  return 'SPACE'
 elif c == None:
  return 'NONE'
 else:
  return c

def get_firstdiff(line1,line2):
 n1 = len(line1)
 n2 = len(line2)
 n = max(n1,n2)
 j = None
 for i,c1 in enumerate(line1):
  if i <n2:
   c2 = line2[i]
   if c1 != c2:
    j = i
    break
   else:
    c2 = None
    j = i
 c1a = char_name(c1)
 c2a = char_name(c2)
 note1 = 'at char # %s,  %s != %s)' % (j+1,c1a,c2a)
 note2 = '-'*(j+1)
 return note1,note2
 
class Change(object):
 def __init__(self,iline,line1,line2,metaline1):
  self.iline = iline
  self.line1 = line1
  self.line2 = line2
  self.lnum = iline+1
  self.metaline1 = metaline1 
  a = []
  # output for emacs org mode
  a.append('* %s' %metaline1)
  link = get_link(metaline1)
  a.append(link)
  note1,note2 = get_firstdiff(line1,line2)
  a.append('; %s' % note1)
  #a.append('; %s     %s' %(self.lnum,self.note2))
  a.append('%s old %s' %(self.lnum,self.line1))
  #a.append(';')
  a.append('%s     %s' %(self.lnum,note2))
  a.append('%s new %s' %(self.lnum,self.line2))
  a.append(';---------------------------------------------------')
  self.changeout = a
  
def write_changes(fileout,changes):
 outarr = []
 for change in changes:
  for x in change.changeout:
   outarr.append(x)
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out+'\n')
 print(len(changes),"changes written to",fileout)

def change_1(iline,line1,line2,metaline):
 ans = None
 n1 = len(line1)
 n2 = len(line2)
 if n1 == n2:
  return ans
 # lines are different
 ans = Change(iline,line1,line2,metaline)
 return ans

def write_xtra(fileout,lines,changes):
 """ copy of lines, with markup related to changes
   Purpose to facilitate corrections
 """
 e = {} # dictionary of iline
 for change in changes:
  e[change.iline] = True
 newlines = []
 for iline,line in enumerate(lines):
  if iline not in e:
   newlines.append(line)
  else:
   dash = '---------0'
   dash100 = dash*10
   newlines.append('* ' + dash100)
   newlines.append(line)
   newlines.append('* ' + dash100)
 # write newlines
 with codecs.open(fileout,"w","utf-8") as f:
  for out in newlines:
   f.write(out+'\n')  
 print('write_extra ',len(newlines),"lines written to",fileout)
 
if __name__=="__main__":
 option = sys.argv[1]
 f_option_name = 'change_%s' % option
 f_option = locals()[f_option_name]
 filein1 = sys.argv[2] # old.txt
 filein2 = sys.argv[3] # new.txt
 fileout = sys.argv[4] # changes.txt
 if len(sys.argv) == 7:
  # optional output
  fileout_xtra = sys.argv[5]
  fileout1_xtra = sys.argv[6]
  xtraflag = True
 else:
  xtraflag = False
 # -------------------------------
 lines1 = read_lines(filein1)
 lines2 = read_lines(filein2)
 n = len(lines1)
 if n != len(lines2):
  print('ERROR: files have different number of lines')
  exit(1)
 changes = []
 metaline1 = None
 metaline2 = None
 for iline,line1 in enumerate(lines1):
  line2 = lines2[iline]
  if line1.startswith('<L>'):
   metaline1 = line1
  if line1 == line2:
   continue
  change = f_option(iline,line1,line2,metaline1)
  # change is either None, or a Change object
  if change != None:
   changes.append(change)
 #
 write_changes(fileout,changes)
 if xtraflag:
  write_xtra(fileout_xtra,lines1,changes)
  write_xtra(fileout1_xtra,lines2,changes)
 
