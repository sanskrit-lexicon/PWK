""" mergebibnew.py  Feb 16, 2016
  Merge pwbib1.txt and pwbib_new.txt
  sort by abbreviation
"""
import sys,re,codecs,os
parent=os.path.realpath('../')
print parent
sys.path.insert(0, parent)
import crefmatch

class Merge(object):
 def __init__(self,abbrv,seqnum,volume,titleunicode):
  self.abbrv=abbrv
  self.seqnum=seqnum
  self.volume=volume
  self.titleunicode=titleunicode
  self.abbrvsort=re.sub(r'[0-9]+','',abbrv) # remove numbers
  self.abbrvsort=self.abbrvsort.upper()  # all caps
 def __repr__(self):
  title=self.titleunicode
  # remove a colon, which occurs once, so ':' can be used as 
  #field separator
  title=re.sub(r':','-',title)
  x=[self.abbrvsort,self.abbrv,self.seqnum,self.volume,title]
  return ':'.join(x)
  
def merge(bibrecs,newrecs):
 recs=[] # list of Merge records, returned
 n = len(bibrecs)
 for r in bibrecs: # r is a Pwbib1 object
  rec = Merge(r.abbrvadj,r.seqnum,r.volume,r.titleunicode)
  recs.append(rec)
  seq = int(r.seqnum)
  if not (1<=seq<=n):
   print "seq anomaly:",r.line.encode('utf-8')
 i=n
 for r in newrecs: # r is a Pwbibnew object, the abbreviation
  i=i+1
  seqnum = "%d" % i
  volume = "%d" % 0
  try:
   rec = Merge(r.abbrv,seqnum,volume,"?")
  except:
   print "ERROR newrec: r=",r
   exit(1)
  recs.append(rec)
 return recs

if __name__ == "__main__":
 filebib = sys.argv[1] # pwbib1.txt
 filenew = sys.argv[2] # pwbib_new.txt
 fileout = sys.argv[3]
 pwbibnewrecs = crefmatch.init_pwbib_new(filenew)
 bibrecs = crefmatch.init_pwbib1(filebib)
 mergerecs= merge(bibrecs,pwbibnewrecs)
 # sort mergerecs on abbrvsort field, and print as tab-delimited-fields
 recs = sorted(mergerecs,key=lambda(x):x.abbrvsort)
 with codecs.open(fileout,"w","utf-8") as f:
  for rec in recs:
   f.write('%s\n' % rec)

  
