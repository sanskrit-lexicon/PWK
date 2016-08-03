""" sortbib.py
    July 26, 2016
  the Merge1 class and init_mergebibnew function are drawn 
  from pwbib_new_work/properrefs1.py
"""
import sys,re,codecs,os

class Merge1(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  (self.abbrvsort,self.abbrv,self.seqnum,self.volume,self.titleunicode)= \
    re.split(r':',line)
  self.line = line
  if self.volume == '0':
   self.volume = 'X'  # so it will sort after all the 'real' volumes
  self.matches=[] # properrefs that match abbrv.

 def __repr__(self):
  title=self.titleunicode
  # remove a colon, which occurs once, so ':' can be used as 
  #field separator
  title=re.sub(r':','-',title)
  nmatch = len(self.matches)
  nmatch = "%s"%nmatch
  volume=self.volume
  if self.volume == 'X':  # the members of pwbib_new
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
   ndup=ndup+1
   print 
   print "Duplicate bibrec # %03d"%ndup
   r = d[a]
   print "  old: ",r.line.encode('utf-8')
   print "  new: ",rec.line.encode('utf-8')
  else:
   d[a]=rec
 print ndup,"Duplicate abbreviations found in",filein
 return (d,recs)

def reset_seqnum(recs):
 """ Change sequence number to be sequential WITHIN VOLUME
     This assumes the records are properly sorted already.
 """
 volume = None
 for rec in recs:
  if rec.volume != volume:
   volume = rec.volume
   seqnum = 0
  seqnum = seqnum + 1
  rec.seqnum = "%03d" %seqnum
if __name__ == "__main__":
 filebib = sys.argv[1] # mergebibnew.txt
 fileout = sys.argv[2] # sortbib.txt
 (dbibrec,bibrecs) = init_mergebibnew(filebib)
 # sort bibrecs in place
 bibrecs.sort(key=lambda(rec): rec.volume + rec.seqnum)
 # reset the seqnum
 reset_seqnum(bibrecs)
 nout = 0
 with codecs.open(fileout,"w","utf-8") as f:
  for rec in bibrecs:
   #if rec.volume == 'X': # pwbib_new
   # continue # skip these
   out = "%s\t%s\t%s\n" %(rec.abbrv,rec.volume + rec.seqnum,rec.titleunicode)
   nout=nout+1
   f.write(out)
 print len(bibrecs),"records read from",filebib
 print nout,"records written to",fileout


