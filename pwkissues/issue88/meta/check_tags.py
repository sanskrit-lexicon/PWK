""" check_tags.py Assumes input is utf8-unicode, and similarly writes.
    10-17-2017.
    08-08-2023 (python3)
    08-23-2023 (tailored for xxx-meta2.txt update)
"""
import re,sys
import codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def check_tags(lines):
# set up regex callback 'repl' with access to dictionary asdict
 asdict = {}
 # count tags in lines
 n = 0
 for line in lines:
  n = n + 1
  tags = re.findall(r'<.*?>',line)
  if line.startswith(('<L>','<LEND>')):
   tags = ['meta'+tag for tag in tags] 
  for c in tags:
   if c not in asdict:
    asdict[c] = 0
   asdict[c] = asdict[c] + 1
 return asdict

def make_outarr_1(asdict):
 keys = asdict.keys()
 keys = sorted(keys)
 outarr = []
 for key in keys:
  if key.startswith('</'):
   # skip closing tags
   continue
  asobj = asdict[key]
  if ' ' in key:
   # skip tags with attributes
   continue
  out = "%s   %5d " %(key,asobj)
  outarr.append(out)
 return outarr

def make_outarr_2(asdict):
 # local abbreviations (space in <X> = key)
 keys = asdict.keys()
 keys = sorted(keys)
 outarr = []
 ntot = 0
 outarr.append('') # will replace with ntot
 for key in keys:
  if key.startswith('</'):
   # skip closing tags
   continue
  asobj = asdict[key]
  if ' ' not in key:
   # skip tags that have no attributes
   continue
  ntot = ntot + asdict[key]
  out = "%s   %5d " %(key,asobj)
  outarr.append(out)
 outarr[0] = '%s Total tags with attributes' % ntot
 return outarr

def write_outarr(fileout,outarr):
 fout = codecs.open(fileout,'w','utf-8')
 for out in outarr:
  fout.write("%s\n" % out)
 fout.close()
 print(len(outarr),"lines written to",fileout)

#-----------------------------------------------------
if __name__=="__main__":
 filein = sys.argv[1]
 fileout = sys.argv[2]
 fileout1 = sys.argv[3]  # for 'local' abbreviation tags
 lines = read_lines(filein)
 d = check_tags(lines)
 outarr = make_outarr_1(d) 
 write_outarr(fileout,outarr)
 outarr= make_outarr_2(d)
 write_outarr(fileout1,outarr)
 
