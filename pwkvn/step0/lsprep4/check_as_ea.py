""" check_as_ea.py.  
   Reads utf-8 encoded file.
   Tabulates :
   (a) number of occurrences of 'letter-digits'
   (b) number of occurrences of 'extended-ascii'.
"""
import sys,codecs,re
from collections import Counter

def check_as(lines,fout):
 c = Counter()
 for line in lines:
  # exclude 'e0x' in [Page0x
  line = line.replace('[Page0','')
  line = line.replace('[Page1','')
  results = re.findall(r'[a-zA-Z][0-9]+',line)
  c.update(results)
 keys = sorted(c.keys(),key=lambda(x): x.encode('ascii').lower())
 
 #for (key,value) in c.iteritems():
 for key in keys:
  value = c[key]
  fout.write("%s %s\n" %(key,value))

def check_ea(lines,fout):
 c = Counter()
 for line in lines:
  results = [x for x in line if (ord(x) > 127)]
  c.update(results)
 for (key,value) in c.iteritems():
  fout.write("%s %s\n" %(key,value))

#-----------------------------------------------------
if __name__=="__main__":
 filein = sys.argv[1]
 with codecs.open(filein,"r","utf-8") as f:
  lines = f.readlines()
 fileout = sys.argv[2]
 fout = codecs.open(fileout,"w","utf-8")
 fout.write("; Anglicized Sanskrit codes and frequency\n")
 check_as(lines,fout)
 fout.write("; Extended ascii codes and frequency\n")
 check_ea(lines,fout)
 fout.close()

