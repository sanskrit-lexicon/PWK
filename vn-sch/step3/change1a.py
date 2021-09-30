#-*- coding:utf-8 -*-
"""change1a.py for pwkvn
 
"""
import sys,re,codecs
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec cannot encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 
class Change(object):
 def __init__(self,metaline,page,iline,old,new,reason,iline1,line1,new1):
  self.metaline = metaline
  self.page = page
  self.iline = iline
  self.old = old
  self.new = new
  self.reason = reason
  self.iline1 = iline1
  self.line1 = line1
  self.new1 = new1
def change1(line):
 reason = 'marked'
 if '</ls>' not in line:
  return reason,line
 newline = re.sub(r'</ls>(-[0-9]+)',r'\1</ls>',line)
 newline = re.sub(r'</ls>-(-[0-9]+)',r'\1</ls>',newline)
 return reason,newline

def change_out(change,ichange):
 outarr = []
 case = ichange + 1
 #outarr.append('; TODO Case %s: (reason = %s)' % (case,change.reason))
 try:
  ident = '%s  (reason = %s)' %(change.metaline,change.reason)
 except:
  print('ERROR:',change.iline,change.old)
  exit(1)
 if ident == None:
  ident = change.page
 outarr.append('; ' + ident)
 # change for iline
 lnum = change.iline + 1
 line = change.old
 new = change.new
 outarr.append('%s old %s' % (lnum,line))
 outarr.append('%s new %s' % (lnum,new))
 outarr.append(';')
 #change for iline1
 if True:
  lnum = change.iline1 + 1
  line = change.line1
  new = change.new1
  outarr.append('%s old %s' % (lnum,line))
  outarr.append('%s new %s' % (lnum,new))
  outarr.append(';')

 # dummy next line
 return outarr

def change_out_simple(change,ichange):
 outarr = []
 # change for iline
 lnum = change.iline + 1
 line = change.old
 new = change.new
 if change.metaline == None:
  outarr.append('; not entry')
 outarr.append('%s old %s' % (lnum,line))
 outarr.append(';')
 outarr.append('%s new %s' % (lnum,new))
 outarr.append('; ----')

 # dummy next line
 return outarr

def write_changes(fileout,changes):
 with codecs.open(fileout,"w","utf-8") as f:
   for ichange,change in enumerate(changes):
    outarr = change_out_simple(change,ichange)
    for out in outarr:
     f.write(out+'\n')
 print(len(changes),"change transactions written to",fileout)

def change_helper(x):
 # kOjJa -> kOja    (A systematic typing error)
 x = re.sub(r'({#[^#]*)jJ',r'\1j',x) # pwk svarita
 return x
def init_changes(lines):
 changes = [] # array of Change objects
 metaline = None
 for iline,line in enumerate(lines):
  n1 = len(re.findall('{#',line))
  n2 = len(re.findall('#}',line))
  if n1 != n2:
   print(iline,'unbalanced {##}')
   continue
  newline = change_helper(line)
  if newline == line:
   continue
  iline1 = None #iline + 1
  line1 = None # lines[iline1]
  newline1 = None
  reason = None
  page = None
  change = Change(metaline,page,iline,line,newline,reason,iline1,line1,newline1)  
  changes.append(change)
 print(len(changes),"changes init_changes")
 return changes

if __name__=="__main__":
 filein = sys.argv[1] #  pwkvn
 fileout = sys.argv[2] # possible change transactions
 #hyphens = init_hyphens()
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 # lines = lines  # for later comparison
 changes = init_changes(lines)
 write_changes(fileout,changes)
