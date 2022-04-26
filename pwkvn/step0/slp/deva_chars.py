#-*- coding:utf-8 -*-
"""devachars.py
 
"""
import sys,re,codecs
def check_chars(lines):
 asdict = {}
 for iline,line in enumerate(lines):
  for m in re.finditer(r'{#(.*?)#}',line):
   x = m.group(1)
   parts = re.split(r'(\[Page.*?\])',x)
   for part in parts:
    if part.startswith('[Page'):
     continue
    for c in part:
     if c not in asdict:
      asdict[c] = 0
     asdict[c] = asdict[c] + 1
 print(len(asdict),"distinct characters in {#X#}")
 return asdict

def write_chars(fileout,eadict):
 keys = eadict.keys()
 keys = sorted(keys)
 
 with codecs.open(fileout,"w","utf-8") as f:
   for key in keys:
    out = "%s %5d" %(key,eadict[key])
    f.write(out+'\n')
 print(len(keys),"extended ascii counts written to",fileout)

if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] # characters in {#X#}
 
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 chard = check_chars(lines) # 
 write_chars(fileout,chard)
 
