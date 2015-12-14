"""crefmatch.py
   Dec 4, 2015
Usage: python crefmatch.py pwbib1.txt ../pw_dhaval/abbrvwork/abbrvoutput/sortedcrefs.txt crefmatch.txt
"""
import codecs,sys,re

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
   ('K4AURAP.(A.)','K4AURAP')
  ]
  for (old,new) in changes:
   if key == old:
    key = new
    break
  self.abbrvadj=key
  
def init_pwbib1(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = [Pwbib1(line) for line in f]
 return recs

pwbib_unusedkeys=[
 'MAHA7B','C2RIMA7LA7M','Bydragen','HARISV','gan2a',
 'SVAPNAK4(INTA7MAN2I)','LEUMANN,Aup.Gl',
 'Ind.Str','MAYR,Ind.Erb'
]
def adjust_bibrecs(bibrecs):
 recs=[] # returned
 removed=[] 
 for rec in bibrecs:
  if rec.abbrvadj  in pwbib_unusedkeys:
   removed.append(rec)
  else:
   recs.append(rec) # keep
 # write removed to stdout
 print len(removed),"known unused records removed from pwbib for purposes of matching"
 for i in xrange(0,len(removed)):
  rec = removed[i]
  out = "Case %02d: %s : %s" % (i+1,rec.abbrv,rec.titleunicode)
  print out.encode('utf-8')
 print "END OF REMOVALS"
 print '-'*80
 print
 
 return recs

class Cref(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  (self.abbrv,self.key1,self.key2,self.L,self.count) = re.split('@',line)
  self.bib=None # filled in by matching

def init_cref(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = [Cref(line) for line in f]
 return recs

if __name__ == "__main__":
 filebib = sys.argv[1]
 filecref = sys.argv[2]
 fileout = sys.argv[3]

 bibrecs = init_pwbib1(filebib)
 crefrecs = init_cref(filecref)
 print len(bibrecs),"records from",filebib
 bibrecs=adjust_bibrecs(bibrecs)
 print len(bibrecs),"After adjustment,records from",filebib

 print len(crefrecs),"records from",filecref

 # dictionary on abbrv for crefrecs
 crefdict = {}
 for crefrec in crefrecs:
  key = crefrec.abbrv
  if key in crefdict:
   print "cref duplicate abbrv:",key
  else:
   crefdict[key]=crefrec

 # dictionary on abbrv for bibrecs
 bibdict = {}
 for bibrec in bibrecs:
  key = bibrec.abbrvadj
  # remove blanks, if any, and ending period
  if key in bibdict:
   old = bibdict[key].seqnum
   new = bibrec.seqnum
   print "bib duplicate abbrv:",key,old,new
   bibrec.duplicate = True
  else:
   bibdict[key]=bibrec
 # Cull out entries which are in pwbib1.txt but are absent in sortedcrefs.txt
 bibminuscref = codecs.open('bibminuscref.txt','w','utf-8')
 # for each bibrec
 for key in bibdict.keys():
  if key in crefdict:
   bibrec = bibdict[key]
   crefrec = crefdict[key]
   bibrec.cref = crefrec
   crefrec.bib = bibrec
  else:
   #print key.encode('utf-8'), '- not found in cref' 
   bibminuscref.write(key+"\n")
 
 # ull out entries which are in sortedcrefs.txt but are absent in pwbib1.txt
 crefminusbib = codecs.open('crefminusbib.txt','w','utf-8')
 crefbibintersect = codecs.open('crefbibintersect.txt','w','utf-8')
 for key in crefdict.keys():
  if key not in bibdict:
   #print key.encode('utf-8'), '- not found in bib' 
   crefminusbib.write(key+"\n")
  else:
   #print key.encode('utf-8'), '- found in both cref and bib' 
   crefbibintersect.write(key+"\n")

 nmatches = len([x for x in bibrecs if (x.cref != None)])
 print nmatches,"matching abbreviations"
 numcrefs = sum([int(x.count) for x in crefrecs])
 print numcrefs,"total abbreviation instances from crefs"
 numcrefsmatch = sum([int(x.cref.count) for x in bibrecs if (x.cref != None)])
 print numcrefsmatch,"of these accounted for by matching abbreviations"

 #
