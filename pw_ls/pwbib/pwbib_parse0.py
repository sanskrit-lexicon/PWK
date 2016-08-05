""" pwbib_parse0.py
    Nov. 16, 2015.  Test module to parse pwbib
    Command-line usage:
    python pwbib_parse0.py <pwbibx.txt>
    Aug 8, 2016.  Introduced raw_title attribute.
    When type is '==', raw_title and title are the same.
    When type is 'xx', title is an amalgam of abbrv and raw_title
"""
import codecs,sys,re

def title_adjust_xx(a,t):
 """ a is the abbreviation and t is the raw title.  Construct
     an adjusted title.
 """
 if a.endswith('.'):
  #a = a[0:-1]
  pass
 m = re.search(r'^\(([A-Z].*?)\)(.*)$',t)
 if m:
  if m.group(1) != 'JOLLY':
   t1 = a + m.group(1) + m.group(2)  
  else:
   t1 = a + ' ' +  t
 else:
  t1 = a + ' ' +  t
 return t1
class Pwbib(object):
 """ a record corresponding to a relevant line of pwbibx.txt"""
 def __init__(self,line,n):
  line = line.rstrip('\r\n')
  self.n = n # line number in file
  self.line = line  # the unparsed line
  self.ok=False
  try:
   m = re.search(r'^([+.]+)(.*?) == (.*)\(vol[.] *([1-6])\) *$',line)
   if m:
    self.type='=='
    self.ok = True
    if m.group(1) == '+.':
     self.checked = True
    else:
     self.checked = False
    self.abbrv = m.group(2)
    self.title = m.group(3)
    self.volume = m.group(4)
   else:
    m = re.search(r'^([+.]+)([^ ]+) +(.*)\(vol[.] *([1-6])\) *$',line)
    if m:
     self.type='xx'
     self.ok = True
     if m.group(1) == '+.':
      self.checked = True
     else:
      self.checked = False
     self.abbrv = m.group(2)
     self.raw_title = m.group(3)
     self.volume = m.group(4)
     self.title = title_adjust_xx(self.abbrv,self.raw_title)
    else:
     print "ERROR parsing",n,line.encode('utf-8')
     exit(1)
  except:
   pass

def parse(filein):
 f = codecs.open(filein,"r","utf-8")
 recs = [] # return list of Pwbib records
 dbg = True #False # no debug messages for skipped lines
 n = 0
 for line in f:
  n = n + 1
  if not (line.startswith('+.') or line.startswith('.')):
   if dbg:
    #print "skip line",n,line.encode('utf-8')
    pass
   continue
  rec = Pwbib(line,n)
  if not rec.ok:
   print "Format problem with line",n
   print line.encode('utf-8')
   continue
  recs.append(rec)
  if dbg:
   if rec.type == 'xx':
    a = rec.abbrv.encode('utf-8')
    t = rec.title.encode('utf-8')
    rt = rec.raw_title.encode('utf-8')
    print "Adjust title in line\n",n,"abrv=",a," , raw title=",rt,"\nadj title=",t,"\n"
 f.close()
 return recs

if __name__ == "__main__":
 filein = sys.argv[1]
 recs = parse(filein)
 print len(recs),"parsed from",filein

