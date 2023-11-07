#-*- coding:utf-8 -*-
"""root_add.py
"""
from __future__ import print_function
import sys,re,codecs
import digentry  

## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec cannot encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

class Change(object):
 def __init__(self,metaline,lnum,line,newline,old,new):
  self.metaline = metaline
  self.lnum = lnum
  self.line = line
  self.newline = newline
  self.old = old
  self.new = new

def unused_compare_changes_1(e1,e2):
 """  work with first line
 """
 ans = [] # return array of change objects
 iline = 0
 line1 = e1.datalines[iline]
 line2 = e2.datalines[iline]
 m = re.search(r'({#[^#]*#})(.*?)¦',line1)
 if m == None:
  return ans
 root1 = m.group(1)
 root2 = '!√' + root1

 if root2 not in line2:
  return ans
 newline1 = line1.replace(root1,root2,1)
 # generate change transaction
 lnum = e1.linenum1 + iline + 1
 change = Change(e1.metaline,lnum,line1,newline1,root1,root2)
 ans = [change]  # return as singleton array.
 return ans

def compare_changes_1(e1,e2):
 """  work with first line
 """
 ans = [] # return array of change objects
 iline = 0
 line1 = e1.datalines[iline]
 line2 = e2.datalines[iline]
 m = re.search(r'({#[^#]*#})(.*?)¦',line1)
 if m == None:
  return ans
 root1 = m.group(1)
 root2 = '√' + root1
 root3 = '!' + root2

 if root3 in line2:
  newline1 = line1.replace(root1,root3,1)
  newroot1 = root3
 elif root2 in line2:
  newline1 = line1.replace(root1,root2,1)
  newroot1 = root2
 else:
  # not found
  return ans
 # generate change transaction
 lnum = e1.linenum1 + iline + 1
 change = Change(e1.metaline,lnum,line1,newline1,root1,newroot1)
 ans = [change]  # return as singleton array.
 return ans

def compare(entries1,entries2,option):
 ans = []  # array of Change objects
 #print('# entries1=',len(entries1))
 #print('# entries2=',len(entries2))
 for ientry,e1 in enumerate(entries1):
  e2 = entries2[ientry]
  changes = compare_changes_1(e1,e2)
  for change in changes:
   ans.append(change)
 #print('compare: # changes=',len(ans))
 return ans

def write_changes(fileout,changes):
 outrecs=[]
 for change in changes:
  outarr=[]
  metaline = change.metaline
  metaline = re.sub(r'<k2>.*$','',metaline)
  outarr.append('; %s' % metaline)
  # change info: old and new
  outarr.append('; "%s"  --> "%s"' % (change.old,change.new))
  outarr.append('; --------------------')
  lnum = change.lnum
  line = change.line
  newline = change.newline
  outarr.append('%s old %s' %(lnum,line))
  outarr.append(';')
  outarr.append('%s new %s' %(lnum,newline))
  outarr.append('; ------------------------------------------------------')
  outrecs.append(outarr)
  
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
    for out in outarr:
     f.write(out+'\n')
 print(len(changes),"changes written to",fileout)

def write(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for line in lines:
   f.write(line + '\n')
 print(len(lines),"written to",fileout)
 
if __name__=="__main__":
 option = sys.argv[1]
 assert option in ['1','2']
 
 filein = sys.argv[2] #  temp_pw_X.txt (path to digitization of xxx)
 filein1 = sys.argv[3] # temp_pw_ab_X.txt
 fileout = sys.argv[4] # change file
 entries_cdsl = digentry.init(filein)
 # reset Ldict
 digentry.Entry.Ldict = {}
 entries_ab = digentry.init(filein1)

 changes = compare(entries_cdsl,entries_ab,option)

 write_changes(fileout,changes)
