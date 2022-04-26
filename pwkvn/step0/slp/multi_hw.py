#-*- coding:utf-8 -*-
"""multi_hw.py
 
"""
import sys,re,codecs

def fchange(m):
 # m.group(0) = <hw>X</hw>
 r = "[*º]?[A-Za-z£_¹'º]+"
 x0 = m.group(0)
 x = m.group(1)
 # 1) 
 if re.search(r"^{#%s#}$",x):
  return x0
 # 2)
 m = re.search(r"^([0-9. ]+){#(%s)#}$" % r,x)
 if m!=None:
  h=m.group(1)
  hom = re.sub(r'([0-9.]+)',r'<hom>\1</hom>',h)
  y1 = m.group(2)
  ans = "%s<hw>{#%s#}</hw>" %(hom,y1)
  return ans
 # 3)
 m = re.search(r"^{#(%s), (%s)#}$" % (r,r),x)
 if m != None:
  y1 = m.group(1)
  y2 = m.group(2)
  ans = "<hw>{#%s#}</hw>, <hw>{#%s#}</hw>" %(y1,y2)
  return ans
 # 4)
 m = re.search(r"^([0-9. ]+){#(%s), (%s)#}$" % (r,r),x)
 if m!= None:
  h=m.group(1)
  hom = re.sub(r'([0-9.]+)',r'<hom>\1</hom>',h)
  y1 = m.group(2)
  y2 = m.group(3)
  ans = "%s<hw>{#%s#}</hw>, <hw>{#%s#}</hw>" %(hom,y1,y2)
  return ans
 # 5)
 m = re.search(r"^([0-9. ]*){#(%s)#} (²?und|²?u[.]) {#(%s)#}$" % (r,r),x)
 if m!= None:
  h=m.group(1)
  hom = re.sub(r'([0-9.]+)',r'<hom>\1</hom>',h)
  y1 = m.group(2)
  sep = m.group(3)  # und, u.
  y2 = m.group(4)
  ans = "%s<hw>{#%s#}</hw> %s <hw>{#%s#}</hw>" %(hom,y1,sep,y2)
  return ans
 # 6) {#X#} und with X not simple
 m = re.search(r"^{#(.*?)#} (²?und ²?|²?u[.] ²?){#(.*?)#}$" ,x)
 if m!= None:
  x1 = m.group(1)
  parts = x1.split(', ')
  newparts = ['<hw>{#%s#}</hw>' % part for part in parts]
  y1 = ', '.join(newparts)
  sep = m.group(2)  # und, u.
  x2 = m.group(3)
  y2 = '<hw>{#%s#}</hw>' % x2
  ans = "%s %s%s" %(y1,sep,y2)
  return ans
 return x0

def check(iline,line):
 if len(re.findall('{#',line)) != len(re.findall('#}',line)):
  print('check %s : %s' %(iline+1,line))

def hw_changes(lines):
 changes = []
 page = None
 nprob = 0
 for iline,line in enumerate(lines):
  if line.startswith('<H>'):
   continue
  check(iline,line)
  newline = re.sub(r'<hw>(.*?)</hw>',fchange,line)
  if newline == line:
   continue
  # generate change
  lnum = iline+1
  change = Change(lnum,line,newline)
  changes.append(change)
 return changes

class Change(object):
 def __init__(self,lnum,old,new):
  self.lnum = lnum
  self.old = old
  self.new = new
  
def write_changes(fileout,changes):
 outrecs = []
 for change in changes:
  outarr = []
  outarr.append('; ' + ('-'*60))
  outarr.append('%s old %s' %(change.lnum,change.old))
  outarr.append(';')
  outarr.append('%s new %s' %(change.lnum,change.new))
  outrecs.append(outarr)
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for line in outarr:
    f.write(line+'\n')
 print(len(outrecs),"changes written to",fileout)

if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] # change file

 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 changes = hw_changes(lines) # 
 write_changes(fileout,changes)
 
