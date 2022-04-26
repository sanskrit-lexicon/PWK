#-*- coding:utf-8 -*-
"""ls3.py
 
"""
import sys,re,codecs

sys.stdout.reconfigure(encoding='utf-8')

def part_to_lsname(part0,dbg=False):
 # part is the string following some <ls>
 part = part0
 #lsparts = re.split(r'(-²)|(²)|(-\[Page.*?\])|( \[Page.*?\])|( )',part)
 part = part.replace('-²','')  # THIS IS VERY TRICKY
 part = part.replace('²','')
 part = re.sub(r'[- ]\[Page.*?\]','',part)
 lsname = part
 # some tidying up of lsname
 if lsname.endswith(')'):
  lsname = lsname[0:-1]
 elif lsname.endswith((').' ,'),')):                          
  lsname = lsname[0:-2] 
 elif lsname.endswith(','):
  # remove the ending comma
  lsname = lsname[0:-1]  
 return lsname

def count_ls1(lines):
 lsnamed = {}
 exceptions = []
 page = None
 for iline,line0 in enumerate(lines):
  line = line0
  for m in re.finditer(r'<ls>(.*?)</ls>',line):
   part = m.group(1)
   lsname = part_to_lsname(part)
   if lsname == '':
    print("exception: line#=%s\npart='%s'" % (iline+1,part))
    continue
   # update lsnamed
   if lsname not in lsnamed:
    lsnamed[lsname] = 0
   lsnamed[lsname] = lsnamed[lsname] + 1
 # reduce dictionary by merging, for example,
 # 0008 BLOOMFIELD and 0002 BLOOMFIELD. to
 #  0010 BLOOMFIELD
 lsnamed = lsname_reduce(lsnamed)
 return lsnamed

def lsname_reduce(d):
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

def write_ls(fileout,lsdict):
 recs = [[k,lsdict[k],removenum(k)] for k in lsdict]
 recs1 = sorted(recs,key = lambda rec: rec[2])
 with codecs.open(fileout,"w","utf-8") as f:
   for key,n,key1 in recs1:
    n = lsdict[key]
    out = '%04d %s' %(n,key)
    f.write(out+'\n')
 print(len(recs),"ls counts written to",fileout)

def write_exceptions(fileout,exceptions):
 exceptions1 = sorted(exceptions)
 with codecs.open(fileout,"w","utf-8") as f:
   for x in exceptions1:
    out = x
    f.write(out+'\n')
 print(len(exceptions),"exceptions written to",fileout)

def write_changes(fileout,changes):
 outrecs=[]
 for change in changes:
  outarr=[]
  lnum = change.lnum
  line = change.line
  page = change.page
  newline = change.newline
  outarr.append(';Page %s' % page)
  outarr.append('%s old %s' %(lnum,line))
  outarr.append(';')
  outarr.append('%s new %s' %(lnum,newline))
  outarr.append('; ---------------------------')
  outrecs.append(outarr)
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
    for out in outarr:
     f.write(out+'\n')
 print(len(changes),"changes written to",fileout)

if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] # ls3.txt
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 print(len(lines),'lines read from',filein)
 lscountd = count_ls1(lines)
 write_ls(fileout,lscountd)
 exit(1)
 #write_exceptions(filedbg,exceptions)
 #write_changes(filechg,changes)
 with codecs.open(filenew,"w","utf-8") as f:
  for out in newlines:
   f.write(out+'\n')
 print(len(newlines),"lines written to",filenew)
 
