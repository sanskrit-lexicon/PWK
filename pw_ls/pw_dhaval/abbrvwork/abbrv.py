# coding=utf-8
#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
from lxml import etree # lxml.de
import re
import codecs
import datetime
import sys

"""
# Abbreviations of PW
Run `makeabbrv.sh` from pywork/abbrvwork directory to regenerate the lists.

# Dependencies
[lxml](http://lxml.de/) to parse pw.xml

# Logic
1. `<ls>something</ls>` tag usually holds the literary source data.

2. Output of all scripts are stored in abbrvoutput folder.

3. The text `something` is scraped via lxml and stored in abbrvlist.txt file (1st raw file).

4. abbrvlist.txt file still has some references which are pure numbers. We have discarded them as of now and stored them in purenumberabbrvlist.txt (byproduct). (See https://github.com/sanskrit-lexicon/PWK/issues/11 for details).

5. The list which is not pure numbers, but has some alphabet preceding it is stored in properrefs.txt (raw file 2).

6. The properrefs.txt file still has entries like `TA7N2D2JA-BR.25,13,3.` where the last entries are the canto / shloka number. They need to be removed.

7. The canto or shloka numbers are removed and only unique entries, sorted alphabetically are kept in cleanrefs.txt (raw file 3).

8. Errors usually come solo. Therefore, we have kept a code which sorts cleanrefs based on their occurrences. Sorted data is stored in sortedcrefs.txt. Sorting is done first based on number of occurrences and then alphabetically.

9. sortedcrefs.txt has the data is `ls@key1@key2@Lnumber@occurrence`.

10. It is difficult to read the `ls`, because it is in Anglisized Sanskrit. Therefore we add another field `lsinIAST@ls@key1@key2@Lnumber@occurrence` in  sortedcrefsiast.txt via `transcoder/as_roman.py` file.

11. The file `displayhtml.php` takes sortedcrefsiast.txt as input and gives the following output `SrNo-Lno-ReferenceinAS-ReferenceinIASTwithlinktowebpage-key1withlinktopdf-key2-counter`.

12. This file displayhtml.php would make it easy to locate the reference in dictionaries.

13. For corrections, copy the file `sortedcrefs.txt` as `finalabbrv.txt`. (This is not automated, because otherwise it may be overwritten if handled recklessly).

14. If there are errors found in HTML file, correct the `referenceinAS` in the finalabbrv.txt file.

15. If there is no error, place a ';' before the line in finalabbrv.txt.

16. Once the testing is over, run `python postprocess.py`. It would separate the file into change.txt and nochange.txt.

17. Jim would have to find a way to integrate these files into XML corrections.


# Improvements in statistics
1. First run - 3679 entries

2. After removing terminal period(.) i.e. `clean = clean.strip('.')` - 3341 entries
"""

xmlfilename = sys.argv[1]  # e.g., ../pw.xml
print "Using xmlfile",xmlfilename
# Function to return timestamp
def printtimestamp():
	return datetime.datetime.now()
print "Parsing started at", printtimestamp()
print
entries = etree.parse(xmlfilename) # Parse xml
print "Parsing ended at", printtimestamp()
print

# Argument abbrvtag is the tag which contains literary resources data in the given XML file. 
# For PW, it is 'ls'.
def scrapeabbrv(abbrvtag):
	global entries # Fetched parse XML.
	g = codecs.open('abbrvoutput/abbrvlist.txt', 'w','utf-8') # Opened file to store
	pw = entries.xpath('/pw/H1/body/'+abbrvtag) # Scraped only elements in XML tree which have the abbrvtag.
	wholeabbrvlist = []
	for pws in pw:
		abbrvtext = pws.text
		key1 = pws.getparent().getparent().find('h/key1').text.strip()
		key2 = pws.getparent().getparent().find('h/key2').text.strip()
		lnum = pws.getparent().getparent().find('tail/L').text.strip()
		wholeabbrvlist.append((abbrvtext,key1,key2,lnum))
	for (a,b,c,d) in wholeabbrvlist:
		if a is None:
			a = "" # A patch to overcome errors in windows for Nonetype.
		g.write(a+"@"+b+"@"+c+"@"+d+"\n") # Store one in a line in the storage file.
	g.close()
	return wholeabbrvlist # Also return a list.
print "Started scraping the abbreviations from pw.xml at ", printtimestamp()
print
# Change the abbrvtag with suitable tag if you want to extend the code for other dictionaries.
wholeabbrvlist = scrapeabbrv("ls")
print "Stored abbreviations in abbrvoutput/abbrvilst.txt at ", printtimestamp()
print

def segregatepurenumbers():
	global wholeabbrvlist # Fetched global.
	n = codecs.open('abbrvoutput/purenumberabbrvlist.txt','w','utf-8') # n for numbers
	propfile = codecs.open('abbrvoutput/properrefs.txt','w','utf-8') # a for abbreviations (which we are interested in).
	properrefs = []
	for (a,b,c,d) in wholeabbrvlist:
		if a is None:
			a = ""
		if re.match(r'^([^a-zA-Z]*)$',a): # Removing improper reference tags.
			n.write(a+"@"+b+"@"+c+"@"+d+"\n") # Store one in a line in the storage file.
		elif re.match(r'^([0-9a-z()&.,]+)$',a): # Same
			n.write(a+"@"+b+"@"+c+"@"+d+"\n") # Store one in a line in the storage file.
		else:
			propfile.write(a+"@"+b+"@"+c+"@"+d+"\n") # Store one in a line in the storage file.
			properrefs.append((a,b,c,d)) # Append to the list
	propfile.close()
	return properrefs # Return list

print "Segretating references with only numbers to abbrvoutput/purenumberabbrvlist.txt and "
print "proper references to abbrvoutput/properrefs.txt at", printtimestamp()
print
properrefs = segregatepurenumbers()
print "Completed segretating references at ", printtimestamp()
print

def clean_special(a,clean):
 """  a = original abbreviation
      clean = 'standard' cleaned abbreviation
      Return an 'adjusted' cleaned abbreviation, which in a few
      cases differs from 'clean'
 """
 cleanadj = clean # usual case
 starts = ['Mat.med','H.an','DAC2AK.(1925)','VET.(U.)',
   'VIKR.dra7v','PISCHEL,deGr.pr','Bibl.ind','KAP.(BALL.)',
   'HARIV.LANGL','PAN4K4AT.ed.orn',
   'Lot.delab.l','C2RUT.(BR.)','HAM5SOP','K4AURAP.(A.)',
   'MED.avj','WILSON,Sel.Spec','VA7MANA','ROXB',
   'GAN2IT.GRAH',  # to catch GAN2IT.GRAHAJ
   'PRA7JAC2K4ITTAV', # to catch PRA7JAC2K4ITTAVIVEKA
   'MAHA7BH.(K.)', # so the (K.) won't be dropped.
   'HANUM.UP',  # so S. will be dropped
   # issue 27
   'R2SHIMAN2D2ALASTOTRA', # so number dropped
   u'BÜHLER,Rep', # so .No dropped
   'PANDIT', # so IX dropped
   # issue 53
   u'VP.²',  # so ok if next character is a digit
   ]
 for start in starts:
  try:
   if a.startswith(start):
    cleanadj = start
    return cleanadj
  except:
   print "ERROR", start
   exit(1)

 #return cleanadj
 # 2nd method (start,cleanadj) tuples
 startpairs = [
  # Roman numeral confusions
  ('A7RJABH.IX','A7RJABH'),
  ('A7RJABH.V','A7RJABH'),
  ('C2A7C2VATA.XI','C2A7C2VATA'),
  ('C2IC2.I','C2IC2'),
  ('HIT.I','HIT'),
  ('KA7D.I','KA7D'),
  ('MED.V','MED'),
  ('MEGH.III','MEGH'),
  ('MEGH.IX','MEGH'),
  ('MEGH.V','MEGH'),
  ('MEGH.VIII','MEGH'),
  ('MEGH.X','MEGH'),
  ('MEGH.XI','MEGH'),
  ('MEGH.XII','MEGH'),
  ('MIT.II','MIT'),
  ('PAN4K4AT.I','PAN4K4AT'),
  ('R.V','R'),
  ('R2V.V','R2V'),
  ('SV.I','SV'),
  ('TBR.I','TBR'),
  ('TS.I','TS'),
  ('VAM5C2ABR.IX.XXIV','VAM5C2ABR'),
  ('VAM5C2ABR.X','VAM5C2ABR'),
  # PWK/issue/27
  ('C2A7N2D2.Einl.S','C2A7N2D2'),
  # PWK/issue/31  Seite confusion
  ('A7R.UP.S','A7R.UP'),
  ('A7RJABH.S','A7RJABH'),
  ('A7RSH.BR.S','A7RSH.BR'),
  ('AIT.UP.S','AIT.UP'),
  ('ANARGHAR.S','ANARGHAR'),
  ('BA7DAR.S','BA7DAR'),
  ('BR2H.A7R.UP.S','BR2H.A7R.UP'),
  (u'BÜHLER,Rep.S',u'BÜHLER,Rep'),
  ('C2A7N2D2.S','C2A7N2D2'),
  ('C2IRA-UP.S','C2IRA-UP'),
  ('DAC2AR.S','DAC2AR'),
  ('DEC2I7N.S','DEC2I7N'),
  ('G4A7BA7LOP.S','G4A7BA7LOP'),
  ('G4AIM.S','G4AIM'),
  ('GAN2AR.S','GAN2AR'),
  ('GI7T.S','GI7T'),
  ('GOBH.C2RA7DDHAK.S','GOBH.C2RA7DDHAK'),
  ('GOBH.S','GOBH'),
  ('GOVINDA7N.S','GOVINDA7N'),
  ('HAM5SOP.S','HAM5SOP'),
  ('HANUM.UP.S','HANUM.UP'),
  ('HARIV.S','HARIV'),
  ('K4ARAKA.S','K4ARAKA'),
  ('K4HA7ND.UP.S','K4HA7ND.UP'),
  ('K4U7LIKOP.S','K4U7LIKOP'),
  ('KA7TJ.C2R.S','KA7TJ.C2R'),
  ('KA7VJAPR.S','KA7VJAPR'),
  ('KAUSH.UP.S','KAUSH.UP'),
  ('KUSUM.S','KUSUM'),
  ('LI7LA7V.S','LI7LA7V'),
  ('NJA7JAM.S','NJA7JAM'),
  ('NR2S.UP.S','NR2S.UP'),
  ('PAN4K4AD.S','PAN4K4AD'),
  ('PRAB.S','PRAB'),
  ('SAM5HITOPAN.S','SAM5HITOPAN'),
  ('SAM5NJ.UP.S','SAM5NJ.UP'),
  ('SARVOPAN.S','SARVOPAN'),
  ('TAITT.A7R.S','TAITT.A7R'),
  ('TAITT.UP.S','TAITT.UP'),
  ('UTTAMAK4.S','UTTAMAK4'),
  ('VA7MANA.S','VA7MANA'),
  ('VA7SAV.S','VA7SAV'),
  ('VAM5C2ABR.S','VAM5C2ABR'),
  ('VIKR.S','VIKR'),
  ('VIKRAMA7N5KAK4.S','VIKRAMA7N5KAK4'),
  # PWK/issues/37
  ('SADDH.P.4,','SADDH.P.4'),
  # PWK/issues/48
  ('C2AM5K.zu.BA7DAR.S.','C2AM5K.zu.BA7DAR'),
  ('WILSON,SA7M5KHJAK.S','WILSON,SA7M5KHJAK'),
  # PWK/issues/57
  ('Verz.d.B.H.No','Verz.d.B.H'),
  ('PAN4K4AT.V','PAN4K4AT'),
  ('VAM5C2ABR.XXXI','VAM5C2ABR'),
  ('MA7RK.P.Einl','MA7RK.P'),
  ('S.S.S.Einl','S.S.S'),
  ('R2V.PRA7T.Einl','R2V.PRA7T'),
  ('GAN2IT.S','GAN2IT'),
  (u'BÜHLER,Rep.No',u'BÜHLER,Rep'),
  ('A7PAST.Uebers.','A7PAST'),
  ('K4ARAKA.ed.Calc.S','K4ARAKA.ed.Calc'),
  ('MED.t','MED'), # hw = Gawa
  ('MED.dh','MED'), # hw = anyavat, aBiDeya
  ('G4AIM.I.S','G4AIM'),
  ('BRAHMOP.S','BRAHMOP'),
  ('AV.PRA7T.S','AV.PRA7T'),
  ('SUBHA7SHITA7V.Einl','SUBHA7SHITA7V'),
  ('AMR2T.UP.S','AMR2T.UP'),
  ('UG4G4VAL.S','UG4G4VAL'),
  ('R.GORR.Th','R.GORR'),
  ('NI7LAK.:','NI7LAK'),
  ("C2AM5KARA's",'C2AM5KARA'),
  ('KALPAS.S','KALPAS'),
  ('MAHA7BH.Bd','MAHA7BH'), #assume 'Bd' is an abbreviation
  ('MED.dh','MED'),  # assume 'dh' is abbreviation
  ('FOUCAUX.S','FOUCAUX'),
  ('MAHA7BH.Einl','MAHA7BH'),
  ('HARIV.Adhj','HARIV'), # Adjh =? abbreviation of aDyAya (chapter)
  ('C2A7K.(PISCH)','C2A7K.(PISCH)'),  # not sure if needed. so (PISCH) kept
  ("KIELHORN'S",'KIELHORN'),
  ("ROTH'S","ROTH"),
  ("AUFRECHT'S","AUFRECHT"),
  ('A7RJABH.Einl','A7RJABH'),
  ("K4AKRADATTA'S","K4AKRADATTA"),
  ('Mel.asiat','Mel.asiat'), # so asiat won't be dropped
  ("KERN'S","KERN"),
  (u"BÜHLER's",u"BÜHLER"),
  ('R.ed.Bomb.C2l','R.ed.Bomb'),
  ('DAC2AR.Einl','DAC2AR'), # Einl. =? introduction 
  ('C2A7K.CH','C2A7K'), # CH assumed to be abbreviation
  ('Ind.Antiq.No','Ind.Antiq'),
  ('JACOBI,KALPAS.Intr','JACOBI,KALPAS'),
  ('WASSILIEW,der.Buddh.S','WASSILIEW,der.Buddh'),
  ('HIT.IV','HIT'),
  ('C2A7J(PISCH.)','C2A7J(PISCH.)'),
  ('ZIMMER,Altind.Leben','ZIMMER,Altind.Leben'),
  ('KIELH.Rep.(1881)','KIELH.Rep.(1881)'),
  ('TS.Comm','TS'),
  ('R2V.V','R2V'),
  (u"M.MÜLLER'S",u"M.MÜLLER"),
  ('C2KDR.Hdschr','C2KDR'), # Hdschr = Handschrift = handwriting
  ('BHA7VAPR.Hdschr','BHA7VAPR'),
  ('TA7N2D2JA-BR.Hdschr','TA7N2D2JA-BR'),
  ('A7PAST.C2R.C2l','A7PAST.C2R'), # C2l = Sloka
  ('HARSHAK4.ed.Bomb','HARSHAK4.ed.Bomb'),
  ('Verz.d.Pet.H.No','Verz.d.Pet.H'),
  ("GRASSMANN'S","GRASSMANN"),
  ('BURNELL,T.No','BURNELL,T'),
  ('C2A7RN5G.S','C2A7RN5G'),
  ('NJA7JAM.Einl','NJA7JAM'),
  ('HEM.PAR.Gr','HEM.PAR.Gr'),
  ('GILD,Bibl','GILD'),
  ('VARA7H.BR2H.S.S','VARA7H.BR2H.S'),
  ('PAN4K4A7C2IKA7(ed.SOLF)','PAN4K4A7C2IKA7(ed.SOLF)'),
  ('SV.(Calc.Ausg.)','SV.(Calc.Ausg.)'),
  ('GR2HJA7S.(ed.BLOOMFIELD)','GR2HJA7S.(ed.BLOOMFIELD)'),
  ('P.,Sch','P'),
  ('JOLLY,Sch.','JOLLY'),
  ('C2AT.BR.z.B','C2AT.BR.'), # z.B = zum Beispiel = for example
  ('NJA7JAS.Comm.S','NJA7JAS'),
  ('BI7G4AG.C2l','BI7G4AG'),
  ('NR2S.UP.(Bibl.ind.)','NR2S.UP.(Bibl.ind.)'),
  ('MED.sh','MED'),
  ('H.an','H'),
  ('C2A7K.Ch','C2A7K'),
 
 ]
 for (start,cleanadjman) in startpairs:
  if a.startswith(start):
   return cleanadjman
 # default
 return cleanadj

def removenumbers():
	global properrefs
	cleanfile = codecs.open('abbrvoutput/cleanrefs.txt','w','utf-8')
	cleanrefs = []
	for (a,b,c,d) in properrefs:
		# Nov 28, 2015. ejf first remove (...)  and [...]
                clean = a
                clean = re.sub(r'(.)\(.*?\)',r'\1',clean)
                clean = re.sub(r'(.)\[.*?\]',r'\1',clean)                
		clean = re.sub(u'¨',u'$',clean) # Some unicode issues sorted. Not converted them back as of now.
		clean = re.sub(u'›',u'$$',clean)
		#clean = re.sub(u'ý',u'^2',clean)
                clean = re.sub(u'²',u'^2',clean)
		#clean = re.sub(r'[.]([0-9,.a-z();\^\$]+)$','',clean) # Removed the trailing numbers of cantos / shlokas etc.
		# Removed the trailing numbers of cantos / shlokas etc.
		clean = re.sub(r'[.]([0-9,.a-z();\^\$]+)$','',clean) 
                # ejf.  Replace '.'+digit+<rest> with .
                clean = re.sub(r'[.][0-9].*$','.',clean)
		clean = clean.strip('.') # Removed trailing period after the numbers are removed (if any).
                # Dec 13, 2015. Special cleaning
                clean = clean_special(a,clean)
		cleanrefs.append((clean,b,c,d))
	cl1 = []
	ur1 = []
	for (p,q,r,s) in cleanrefs:
		#if p not in ur1 and re.sub('[.]S$','',p) not in ur1:
		# Dec 31, 2015 (ejf). Removed the 'S' logic, as it
		# inhibits matching of 'KAP.S', for instance.
		if p not in ur1 :
			cl1.append((p,q,r,s))
			ur1.append(p)
	uniquerefs = ur1 # Return only the unique references.
	uniquerefs.sort() # Sort alphabetically.
	for i in xrange(len(cl1)):
		cleanfile.write(cl1[i][0]+"@"+cl1[i][1]+"@"+cl1[i][2]+"@"+cl1[i][3]+"\n") # Write to cleanrefs.txt
	cleanfile.close()
	return (uniquerefs, cleanrefs) # Return a tuple with uniquerefs and cleanrefs as members. Both have their utility.
	
print "Removing numbers from properrefs and storing only names of works to abbrvoutput/cleanrefs.txt at ", printtimestamp()
print
(uniquerefs, cleanrefs) = removenumbers()
print "Completed storing clean references at ", printtimestamp()
print
		
def occurrence():
	global cleanrefs, uniquerefs # Fetched from global
	abbstats = codecs.open('abbrvoutput/sortedcrefs.txt','w','utf-8') # Sorted according to occurrences first and alphabetically second.
	occurlist = []
	onlyls = [a for (a,b,c,d) in cleanrefs]
	uniquerefs.sort()
	ur1 = uniquerefs[:]
	for (a,b,c,d) in cleanrefs:
		if a in ur1:
			count = onlyls.count(a)
			occurlist.append((a,b,c,d,count))
			ur1.remove(a)
	occurlist.sort(key=lambda x: (x[4],x[0]))
	for (a,b,c,d,e) in occurlist:
		abbstats.write(a+"@"+b+"@"+c+"@"+d+"@"+str(e)+"\n")
	abbstats.close()
	

print "Sorting the cleanrefs based on occurrences in pw.xml, and storing in sortedcrefs.txt"
print
print "This may take around 1 minute. Please be patient."
print
occurrence()
print "Execution ended at", printtimestamp()
print 
print "Total ", len(uniquerefs), "unique references"
print 
