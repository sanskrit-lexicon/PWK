#-*- coding:utf-8 -*-
"""wide.py
 
"""
import sys,re,codecs

#sys.stdout.reconfigure(encoding='utf-8')

def part_to_wide(part0,dbg=False):
 part = part0
 part = part.replace('-²','')  # THIS IS VERY TRICKY
 part = part.replace('²','')
 part = re.sub(r'-?\[Page.*?\]','',part)
 return part

def count_wide(lines):
 wided = {}
 page = None
 for iline,line0 in enumerate(lines):
  line = line0
  for m in re.finditer(r'{\|(.*?)\|}',line):
   part = m.group(1)
   try:
    wide = part_to_wide(part)
   except:
    print('error. %s\n%s\n%s' %(iline+1,line0,part))
    exit(1)
   if wide == '':
    print("exception: line#=%s\npart='%s'" % (iline+1,part))
    continue
   # update wided
   if wide not in wided:
    wided[wide] = 0
   wided[wide] = wided[wide] + 1
 return wided

def unused_wide_reduce(d):
 e = {} # new merged dictionary
 keys = sorted(d.keys())
 prev = '-----' # some non-key
 for key in keys:
  if key.endswith('.'):
   key1 = key[0:-1]
   if key1 in e:
    e[key1] = e[key1] + d[key]
   else:
    e[key] = d[key]
  else: # key does not end in '.'
   e[key] = d[key]
 ekeys = e.keys()
 print('lsname_reduce %s -> %s' %(len(keys),len(ekeys)))
 return e

def removenum(s):
 s1 = re.sub(r'[0-9-]','',s)
 return s1

def write_wide(fileout,widedict):
 recs = [[k,widedict[k],removenum(k)] for k in widedict]
 recs1 = sorted(recs,key = lambda rec: rec[2])
 with codecs.open(fileout,"w","utf-8") as f:
   for key,n,key1 in recs1:
    n = widedict[key]
    out = '%04d %s' %(n,key)
    f.write(out+'\n')
 print(len(recs),"wide text written to",fileout)

if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2]
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 print(len(lines),'lines read from',filein)
 wided = count_wide(lines)
 write_wide(fileout,wided)
