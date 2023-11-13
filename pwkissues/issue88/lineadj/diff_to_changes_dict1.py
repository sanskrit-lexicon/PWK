# coding=utf-8
""" diff_to_changes_dict1.py
   Generate change transactions from an 'old' and 'new' file
   The two files should have same number of lines
   ASSUME input file is a dictionary as in csl-orig/v02, e.g. mw.txt.
     This structure identifies the metaline for each change;
     and this is the only difference from diff_to_changes.py,
     which ignores this structure, and is thus available for 
     generating changes for any two text files with same number of lines.
  python diff_to_changes_dict.py old.txt new.txt changes.txt
  Now:
  python updateByLine.py old.txt changes.txt new1.txt
  then new1.txt is same as new.txt.
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

class Change(object):
 def __init__(self,iline,line1,line2,metaline1):
  self.iline = iline
  self.line1 = line1
  self.line2 = line2
  self.lnum = iline+1
  self.metaline1 = metaline1 
  a = []
  a.append('; %s' %metaline1)
  a.append('%s old %s' %(self.lnum,self.line1))
  a.append(';')
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
 dbg = False
 if dbg:print('line1=%s\nline2=%s\n\n' %(line1,line2))
 ans = None
 n1 = len(line1)
 n2 = len(line2)
 if n1 == n2:
  return ans
 # lines have different lengths
 if n1 != (n2+1):
  return ans
 # line1 has 1 additional character
 for i,c1 in enumerate(line1):
  if (i == n2) and (c1 == '.'):
   # last character of line1 is first unmatched, and is a period 
   newline1 = line1[0:i] + line1[i+1:]
   if newline1 != line2:
    return ans
   ans = Change(iline,line1,line2,metaline)
   return ans
  if i == n2:
   return ans
  c2 = line2[i]
  if c1 == c2:
   continue
  # first difference
  if dbg: print('i=%s, c1=%s, c2=%s' %(i,c1,c2))
  if c1 != '.':
   return ans
  # first difference is at a period in line1
  # solution is to drop that period
  newline1 = line1[0:i] + line1[i+1:]
  if dbg: print('newline1=',newline1)
  if newline1 != line2:
   return ans
  ans = Change(iline,line1,line2,metaline)
  return ans

def change_2(iline,line1,line2,metaline):
 # X<ab -> X <ab resolves the diff
 dbg = False
 if dbg:print('line1=%s\nline2=%s\n\n' %(line1,line2))
 ans = None
 newline1 = re.sub(r'([^ ])<ab', r'\1 <ab',line1,1) # first instance only
 if newline1 == line2:
  ans = Change(iline,line1,line2,metaline)
 return ans

def change_3(iline,line1,line2,metaline):
 # line1 missing period at end of line
 ans = None
 newline1 = line1 + '.'
 if newline1 == line2:
  ans = Change(iline,line1,line2,metaline)
 return ans

def change_4(iline,line1,line2,metaline):
 # similar to change_1, except there is an extra comma
 dbg = False
 if dbg:print('line1=%s\nline2=%s\n\n' %(line1,line2))
 ans = None
 n1 = len(line1)
 n2 = len(line2)
 if n1 == n2:
  return ans
 # lines have different lengths
 if n1 != (n2+1):
  return ans
 # line1 has 1 additional character
 for i,c1 in enumerate(line1):
  if (i == n2) and (c1 == ','):
   # last character of line1 is first unmatched, and is a period 
   newline1 = line1[0:i] + line1[i+1:]
   if newline1 != line2:
    return ans
   ans = Change(iline,line1,line2,metaline)
   return ans
  if i == n2:
   return ans
  c2 = line2[i]
  if c1 == c2:
   continue
  # first difference
  if dbg: print('i=%s, c1=%s, c2=%s' %(i,c1,c2))
  if c1 != ',':
   return ans
  # first difference is at a period in line1
  # solution is to drop that period
  newline1 = line1[0:i] + line1[i+1:]
  if dbg: print('newline1=',newline1)
  if newline1 != line2:
   return ans
  ans = Change(iline,line1,line2,metaline)
  return ans

def change_5(iline,line1,line2,metaline):
 # </ab>X -> </ab> X  (similar to change_2)
 dbg = False
 if dbg:print('line1=%s\nline2=%s\n\n' %(line1,line2))
 ans = None
 newline1 = re.sub(r'</ab>([^ ])', r'</ab> \1',line1,1) # first instance only
 if newline1 == line2:
  ans = Change(iline,line1,line2,metaline)
 return ans

def change_6(iline,line1,line2,metaline):
 # These will be changed manually
 ans = None
 n1 = len(line1)
 n2 = len(line2)
 if (abs(n1 - n2) == 1) and (n1 <= 200):
  ans = Change(iline,line1,line2,metaline)
 return ans

def char_name(c):
 if c == '\t':
  return 'TAB'
 elif c == ' ':
  return 'SPACE'
 else:
  return c
 
def change_7_note(line1,line2):
 n1 = len(line1)
 n2 = len(line2)
 assert n1 == n2
 j = None
 for i,c1 in enumerate(line1):
  c2 = line2[i]
  if c1 != c2:
   j = i
   break
 # check that this is the ONLY difference
 line1a = line1[0:j] + c2 + line1[j+1:]
 if line1a != line2:
  return None
 c1a = char_name(c1)
 c2a = char_name(c2)
 note = '  (first diff at char # %s,  %s != %s)' % (j+1,c1a,c2a)
 return note

def change_7(iline,line1,line2,metaline):
 # 
 ans = None
 n1 = len(line1)
 n2 = len(line2)
 if (n1 == n2) and (line1 != line2):
  # Generate a note
  note = change_7_note(line1,line2)
  if note != None:
   ans = Change(iline,line1,line2,metaline + note)
 return ans

def change_8_note(line1,line2):
 n1 = len(line1)
 n2 = len(line2)
 assert n1 == n2
 j = None
 for i,c1 in enumerate(line1):
  c2 = line2[i]
  if c1 != c2:
   j = i
   break
 c1a = char_name(c1)
 c2a = char_name(c2)
 note = '  (first diff at char # %s,  %s != %s)' % (j+1,c1a,c2a)
 return note

def change_8(iline,line1,line2,metaline):
 # 
 ans = None
 n1 = len(line1)
 n2 = len(line2)
 if (n1 == n2) and (line1 != line2):
  # Generate a note
  note = change_8_note(line1,line2)
  ans = Change(iline,line1,line2,metaline + note)
 return ans

if __name__=="__main__":
 option = sys.argv[1]
 f_option_name = 'change_%s' % option
 f_option = locals()[f_option_name]
 filein1 = sys.argv[2] # old.txt
 filein2 = sys.argv[3] # new.txt
 fileout = sys.argv[4] # changes.txt
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
 
