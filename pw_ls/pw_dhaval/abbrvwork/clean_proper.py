# coding=utf-8
""" clean_proper.py (ejf) Feb 16, 2016
 Moved from abbrv.py, so this logic is available separately.
 The clean_one_properref function cleans the literary source abbreviation
 which is first field of the four-field (@-separated) records of properref.txt
"""
import re
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
  ('GAN2IT.S.','GAN2IT'), # Could be same as GAN2IT.SPASHT2
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
  ('C2A7RN5G.S.','C2A7RN5G'), # could be same as C2A7RN5G.SAM5H
  ('NJA7JAM.Einl','NJA7JAM'),
  ('HEM.PAR.Gr','HEM.PAR.Gr'),
  ('GILD,Bibl','GILD'),
  ('VARA7H.BR2H.S.S','VARA7H.BR2H.S'),
  ('PAN4K4A7C2IKA7(ed.SOLF)','PAN4K4A7C2IKA7(ed.SOLF)'),
  ('SV.(Calc.Ausg.)','SV.(Calc.Ausg.)'),
  ('GR2HJA7S.(ed.BLOOMFIELD)','GR2HJA7S.(ed.BLOOMFIELD)'),
  ('P.,Sch','P'),
  ('JOLLY,Sch.','JOLLY'),
  ('C2AT.BR.z.B','C2AT.BR'), # z.B = zum Beispiel = for example
  ('NJA7JAS.Comm.S','NJA7JAS'),
  ('BI7G4AG.C2l','BI7G4AG'),
  ('NR2S.UP.(Bibl.ind.)','NR2S.UP.(Bibl.ind.)'),
  ('MED.sh','MED'),
  ('H.an','H'),
  ('C2A7K.Ch','C2A7K'),
  # PWK/issues/59
  ('Va7rtt.,Sch','Va7rtt'),
  ('MA7LATI7M.ed.Bomb.S','MA7LATI7M.ed.Bomb'),
  ('PAN4K4AT.ed.KOSEG.Ausg','PAN4K4AT.ed.KOSEG'),
  ('GOBH.Einl.S','GOBH'),
  ('C.H.TAWNEY','C.H.TAWNEY'),
  ('PAN4K4AT.ed.Bomb.I','PAN4K4AT.ed.Bomb'),
  ('NJA7JAS.S','NJA7JAS'),
  (u'Kön.Pr.Ak.d.Ww',u'Kön.Pr.Ak')
 ]
 for (start,cleanadjman) in startpairs:
  if a.startswith(start):
   return cleanadjman
 # default
 return cleanadj

# Feb 16, 2016 (ejf).  Refactor, so that all the 'cleaning' logic
# for one element (a,b,c,d) of properrefs is done in this function.
# The reason is so that another program can re-use these details.
def clean_one_properref(a,b,c,d):
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
 return clean
