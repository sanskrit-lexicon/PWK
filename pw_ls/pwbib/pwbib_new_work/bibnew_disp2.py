# coding=utf-8
"""bibnew_disp2.py  Feb 17, 2016
  Create a working document to help with completing mergebibnew.txt
  In addition to the mergebibnew.txt input, this display incorporates
  information from
   - properrefs1.txt 
      - For all references, shows how many times the reference occurs
      - For 'new' references, shows up to 10 of the
        dictionary instances where the reference occurs.
   - tab_table.txt  (MW authorities
  Generate 

 python bibnew_disp2.py mergebibnew.txt properrefs1.txt tab_table.txt bibnew_disp2.txt
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

 def disp2(self):
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
  elif self.volume=='MW':
   volume=self.volume
  else:
   volume="PW-v"+self.volume
  #x=':'.join([self.abbrv,"id=%s"%self.seqnum,volume,"#=%s"%nmatch,title])
  if volume == 'MW':
   x = '%s  (%s) : %s ' %(self.abbrv,volume,title)
  else:
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

def disp2(fileout,bibrecs):
 f = codecs.open(fileout,"w","utf-8")
 for bibrec in bibrecs:
  out = bibrec.disp2()
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

class MWauth(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  (self.abbrv,self.title,self.type)= re.split('\t',line)
  abbrv = re.sub(r'[.]$','',self.abbrv) # remove trailing period
  self.abbrvsort=re.sub(r'[0-9]+','',abbrv) # remove numbers
  self.abbrvsort=self.abbrvsort.upper()  # all caps
  

def init_mwauth(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = [MWauth(line) for line in f]
 return recs

def mwrec_merge1_line(mwrec):
 seqnum='_'
 volume='MW'
 title=re.sub(r':','-',mwrec.title) + (' (%s)'%mwrec.type)
 fields=(mwrec.abbrvsort,mwrec.abbrv,seqnum,volume,title)
 return ':'.join(fields)

def merge_mw_bibrecs(bibrecs,mwrecs):
 for mwrec in mwrecs:
  line = mwrec_merge1_line(mwrec)
  r = Merge1(line)
  bibrecs.append(r)
 return sorted(bibrecs,key=lambda(x):x.abbrvsort)

if __name__ == "__main__":
 filebib = sys.argv[1] # mergebibnew.txt
 fileproper = sys.argv[2] # properrefs1.txt
 filemw = sys.argv[3]
 filebib2 = sys.argv[4] # bibnew_disp2.txt (output)
 #pwbibnewrecs = crefmatch.init_pwbib_new(filenew)
 (dbibrec,bibrecs) = init_mergebibnew(filebib)
 proprecs = init_proprecs(fileproper)
 match(dbibrec,proprecs)
 mwrecs = init_mwauth(filemw)
 bibmwrecs = merge_mw_bibrecs(bibrecs,mwrecs)
 disp2(filebib2,bibmwrecs)

