# coding=utf-8
"""bibnew_disp1.py  Feb 17, 2016
  Create a working document to help with completing mergebibnew.txt
  In addition to the mergebibnew.txt input, this display incorporates
  information from
   - properrefs1.txt 
      - For all references, shows how many times the reference occurs
      - For 'new' references, shows up to 10 of the
        dictionary instances where the reference occurs.
  Generate 

 python bibnew_disp1.py mergebibnew.txt properrefs1.txt bibnew_disp1.txt
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

 def disp1(self):
  title=self.titleunicode
  #title=re.sub(r':','-',title)
  nmatch = len(self.matches)
  nmatch = "%s"%nmatch
  outarr=[] # array of 1 or more lines
  if self.volume == '0': # extra blank line
   outarr.append(' ')
  if self.volume == '0':  # the members of pwbib_new
   title = 'title='+title
   volume="new"
  else:
   volume="PW-v"+self.volume
  #x=':'.join([self.abbrv,"id=%s"%self.seqnum,volume,"#=%s"%nmatch,title])
  x = '%s  (id=%s, %s , count=%s) : %s ' %(self.abbrv,self.seqnum,volume,nmatch,title)
  newpfx ='  * '
  newpfx1='    '
  if self.volume == '0':
   outarr.append(newpfx+x)
  else:
   outarr.append(x)
  if self.volume == '0':  # the members of pwbib_new
   matches = self.matches[0:10]  # at most 10
   # Each element Properref object
   matches1 = ["%s,%s" % (x.key1,x.lnum) for x in matches]
   instances = ";".join(matches1)
   outarr.append(newpfx1 + ('instances = %s' % instances))
   outarr.append('') # extra blank line
  return ('\n'.join(outarr) + '\n')

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

def match(dbibrec,proprecs):
 # update bibrecs using proprecs
 nok=0
 notok=0
 for rec in proprecs:
  if rec.abbrv in dbibrec:
   nok=nok+1
   bibrec = dbibrec[rec.abbrv]
   bibrec.matches.append(rec)
  else: # not expected to occur.
   notok=notok+1
   print "Unknown abbreviation:",line.encode('utf-8')

def disp1(fileout,bibrecs):
 f = codecs.open(fileout,"w","utf-8")
 for bibrec in bibrecs:
  out = bibrec.disp1()
  f.write(out)
 f.close()

class Properref(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  (self.ref,self.key1,self.key2,self.lnum,self.abbrv)= re.split('@',line)

def init_proprecs(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = [Properref(line) for line in f]
 return recs

if __name__ == "__main__":
 filebib = sys.argv[1] # mergebibnew.txt
 fileproper = sys.argv[2] # properrefs1.txt
 filebib1 = sys.argv[3] # bibnew_disp1.txt (output)
 #pwbibnewrecs = crefmatch.init_pwbib_new(filenew)
 (dbibrec,bibrecs) = init_mergebibnew(filebib)
 proprecs = init_proprecs(fileproper)
 match(dbibrec,proprecs)
 disp1(filebib1,bibrecs)

