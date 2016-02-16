"""properrefs1.py  Feb 16, 2016
  Read mergebibnew
  Read each record  from pw_dhaval/abbrvwork/abbrvoutput/properrefs.txt
  Perform the 'cleaning' of abbrv.py
  Write out the record, with the 'cleaned' abbreviation as an additional field.
 python properrefs1.py mergebibnew.txt ../../pw_dhaval/abbrvwork/abbrvoutput/properrefs.txt properrefs1.txt
"""
import sys,re,codecs,os
parent=os.path.realpath('../../pw_dhaval/abbrvwork/')
print parent
sys.path.insert(0, parent)
from abbrv import clean_one_properref 

class Merge1(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  (self.abbrv,self.seqnum,self.volume,self.titleunicode,self.abbrvsort)= \
    re.split(r':',line)
  
 def __repr__(self):
  title=self.titleunicode
  # remove a colon, which occurs once, so ':' can be used as 
  #field separator
  title=re.sub(r':','-',title)
  x=[self.abbrvsort,self.abbrv,self.seqnum,self.volume,title]
  return ':'.join(x)
  
if __name__ == "__main__":
 filebib = sys.argv[1] # mergebibnew.txt
 filenew = sys.argv[2] # properrefs.txt
 fileout = sys.argv[3] # properrefs1.txt
 #pwbibnewrecs = crefmatch.init_pwbib_new(filenew)
