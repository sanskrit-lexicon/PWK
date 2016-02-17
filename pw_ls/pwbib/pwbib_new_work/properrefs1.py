# coding=utf-8
"""properrefs1.py  Feb 16, 2016
  Read mergebibnew
  Read each record  from pw_dhaval/abbrvwork/abbrvoutput/properrefs.txt
  Perform the 'cleaning' of abbrv.py
  Write out the record, with the 'cleaned' abbreviation as an additional field.
 python properrefs1.py mergebibnew.txt ../../pw_dhaval/abbrvwork/abbrvoutput/properrefs.txt properrefs1.txt 
"""
import sys,re,codecs,os
# add to import path so clean_proper is found 
parent=os.path.realpath('../../pw_dhaval/abbrvwork/')
#print parent
sys.path.insert(0, parent)
from clean_proper import clean_one_properref 

class Merge1(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  (self.abbrvsort,self.abbrv,self.seqnum,self.volume,self.titleunicode)= \
    re.split(r':',line)
  self.line = line
  self.matches=[] # properrefs that match abbrv.

 def __repr__(self):
  title=self.titleunicode
  # remove a colon, which occurs once, so ':' can be used as 
  #field separator
  title=re.sub(r':','-',title)
  nmatch = len(self.matches)
  nmatch = "%s"%nmatch
  volume=self.volume
  if self.volume == '0':  # the members of pwbib_new
   matches = self.matches[0:10]  # at most 10
   # Each element is a tuple (key1,lnum).
   matches1 = ["%s,%s" % x for x in matches]
   title = ";".join(matches1)
   volume="new"
  x=[self.abbrvsort,self.abbrv,self.seqnum,volume,nmatch,title]
  return ':'.join(x)

def init_mergebibnew(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = [Merge1(x) for x in f]
 print len(recs),"records read from",filein
 # construct dictionary on abbrv field
 d = {}
 ndup=0
 for rec in recs:
  a = rec.abbrv
  if a in d:
   print "Duplicate bibrec:",rec.line.encode('utf-8')
   ndup=ndup+1
  else:
   d[a]=rec
 print ndup,"Duplicate abbreviations found in",filein
 return (d,recs)

def match(fileproper,fileout,dbibrec):
 f = codecs.open(fileproper,"r","utf-8")
 fout = codecs.open(fileout,"w","utf-8")
 nok=0
 notok=0
 for line in f:
  line = line.rstrip('\r\n')
  (abbrv,key1,key2,lnum) = re.split('@',line)
  clean = clean_one_properref(abbrv,key1,key2,lnum)
  if clean in dbibrec:
   nok=nok+1
   bibrec = dbibrec[clean]
   out = "%s@%s" % (line,clean)
   fout.write("%s\n" % out)
   r = (key1,lnum)
   bibrec.matches.append(r)
  else:
   notok=notok+1
   print "Unknown abbreviation:",line.encode('utf-8')
 f.close()
 fout.close()
 print nok,notok
 print nok,"records written to",fileout

def merge_update(filebib1,bibrecs):
 f = codecs.open(filebib1,"w","utf-8")
 for bibrec in bibrecs:
  f.write('%s\n' % bibrec)
 f.close()

if __name__ == "__main__":
 filebib = sys.argv[1] # mergebibnew.txt
 fileproper = sys.argv[2] # properrefs.txt
 fileproper1 = sys.argv[3] # properrefs1.txt
 #pwbibnewrecs = crefmatch.init_pwbib_new(filenew)
 (dbibrec,bibrecs) = init_mergebibnew(filebib)
 match(fileproper,fileproper1,dbibrec)
 #merge_update(filebib1,bibrecs)

