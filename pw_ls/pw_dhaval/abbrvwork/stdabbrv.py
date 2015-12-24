#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
from lxml import etree # lxml.de
import re
import codecs
import datetime
import sys
import levenshtein

"""
python stdabbrv.py abbrvfile creffile outputfile bibfile
e.g.
python stdabbrv.py ../../pwbib/crefminusbib.txt abbrvoutput/sortedcrefs.txt ../../pwbib/pwbib1.txt

crefminusbib.txt has data like 'AGN'
sortedcrefs.txt has data like `AGN@SAlagrAma@SAlagrAma@111783@1`
We have to combine these two and get data in standard format.
Expected output is `¯AGN@SAlagrAma@SAlagrAma@111783:¯AGN:n:`
For standard format - see https://github.com/sanskrit-lexicon/CORRECTIONS/issues/146#issuecomment-163463468

"""
def getcref(inputword,creflist):
	for cref in creflist:
		if cref.startswith(inputword+'@'):
			return cref
			break
def addunicode(line):
	line = line.strip()
	line = line.encode('utf-8')
	return line

def suggest_v3(w,sanhws,m=6,skipexact=True):
    # modified to screen further by length of word
    # Assume first letter of 'w' is correct.
    # For efficiency, consider only sanhws that start with same letter
    # Do not return exact match 
    w0 = w[0]
    hws= sanhws
    # Feb 3, 2015
    lw = len(w)
    hws = [x for x in hws if (abs(len(x) - lw) < m)] #? < m or > m ?
    #print "%s headwords start with %s" %(len(hws),w0)
    nearlist=[] # list of hws whose levenshtein distance from w is <= 
    low = 99
    for hw in hws:
        if (w == hw) and skipexact:
            continue
        d=levenshtein.levenshtein1(w,hw,m)
        if d == -1:
            continue
        nearlist.append((d,hw))
        if (d < low): # update low distance
            low = d
    # include ones only = low
    ans = [x[1] for x in nearlist if x[0] == low]
    
    #s = sorted(nearlist,key=lambda(x):x[0]) # sort by d
    #return ans[0].encode('utf-8') # If need be, all can be returned. Not now
    if len(ans) == 0:
        return w
    else:
        return ans[0]

def init_pwbib1(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = [Pwbib1(line) for line in f]
 return recs
class Pwbib1(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  (self.abbrv,self.seqnum,self.checked,self.type,self.volume,
   self.abbrvunicode,self.titleunicode) = re.split('\t',line)
  self.cref=None # filled in by matching
  self.duplicate = False  # True if this abbrv is a duplicate. There are 12 such.
  # compute adjusted key
  key = self.abbrv
  key = re.sub(r' ','',key)
  key = re.sub(r'[.,]*$','',key)
  # Dec 13, 2015.  Force a few other adjustments
  # change abbreviation spelling for some
  changes = [
   ('OPP.Cat','OPP.CAT'),
   ('PRATIG4N4A7S(U7TRA)','PRATIG4N4A7S'),
   ("KUHN'SZ","KUHN'S.Z"),
   ('C2A7KTA7N(ANDATARAM5GIN2I)','C2A7KTA7N'),
   ('KAT2HOP(ANISHAD)','KAT2HOP'),
   ('K4AURAP.(A.)','K4AURAP'),
   ('KAP.(BALL.)','KAP'),
   ('SUPARN2.undSUPARN2A7DHJ','SUPARN2'),
   ('PRAKRIJA7K(AUMUDI),Hdschr.(AUFRECHT).RA7JENDR.Not','PRAKRIJA7K')
  ]
  for (old,new) in changes:
   if key == old:
    key = new
    break
  self.abbrvadj=key
  

pwbib_unusedkeys=[
 # Dec 15, 2015
 'MAHA7B','C2RIMA7LA7M','Bydragen','HARISV','gan2a',
 'SVAPNAK4(INTA7MAN2I)','LEUMANN,Aup.Gl',
 'Ind.Str','MAYR,Ind.Erb',
 # Dec 18, 2015
 'VA7RA7HAP','PRAG4A7PATI','MAITR.PADDH','KHAN2D2APR','ALAM5KA7RAS',
 # Dec 19, 2015 
 u'BÜHLER,Rep.1872-73',
 'DEVI7BHA7G',
 'GAN2ITA,MADHJA7M(A7DHJA7JA)','GAN2ITA,K4ANDRAGR(AHA7DHIKA7RA)',
 # Dec 20, 2015
 'KA7TJ.C2RA7DDHAK', 'VA7MANAP','C2OBH','NI7LAK.miteinerZahl',
 'SAHR2DAJA7LOKA','KA7VJA7L','K4HA7NDOGJAP','KIELHORN,Rep',
]
def adjust_bibrecs(bibrecs):
 recs=[] # returned
 removed=[] 
 for rec in bibrecs:
  if rec.abbrvadj  in pwbib_unusedkeys:
   removed.append(rec)
  #elif rec.duplicate:
  # removed.append(rec)
  else:
   recs.append(rec) # keep
 # write removed to stdout
 for i in xrange(0,len(removed)):
  rec = removed[i]
  out = "Case %02d: %s : %s" % (i+1,rec.abbrv,rec.titleunicode)
 
 return recs
		
if __name__=="__main__":
	abbrvfile = sys.argv[1]
	creffile = sys.argv[2]
	filebib = sys.argv[3]
	abbrvlist = codecs.open(abbrvfile,'r','utf-8').read().split()
	creflist = codecs.open(creffile,'r','utf-8').read().split()
	output = []
	bibrecs = init_pwbib1(filebib)
	bibrecs = adjust_bibrecs(bibrecs)
	biblist = [mem.abbrvadj for mem in bibrecs]
	for abbrv in abbrvlist:
		cref = getcref(abbrv,creflist)
		[ls,k1,k2,lnum,count] = cref.split('@')
		output.append((ls,k1,k2,lnum,count))
	output = sorted(output, key=lambda x:x[4], reverse=True) # See https://github.com/sanskrit-lexicon/PWK/issues/42 for logic
	for (ls,k1,k2,lnum,count) in output:
		#print '¯'.encode('utf-8')
		suggest = suggest_v3(ls,biblist)
		if suggest == ls:
			line = unicode(u'¯'+ls+'@'+k1+'@'+k2+'@'+lnum+':'+u'¯'+suggest+':n:')
		else:
			line = unicode(u'¯'+ls+'@'+k1+'@'+k2+'@'+lnum+':'+u'¯'+suggest+':t:')
		line = addunicode(line)
		print line
	