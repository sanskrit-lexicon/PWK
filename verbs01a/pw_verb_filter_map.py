#-*- coding:utf-8 -*-
"""pwg_verb_filter_map.py
"""
from __future__ import print_function
import sys, re,codecs

class Pwgverb(object):
 def __init__(self,line):
  line = line.rstrip()
  self.line = line
  m = re.search(r'L=([^,]*), k1=([^,]*), k2=([^,]*), code=(.*)$',line)
  self.L,self.k1,self.k2,self.code = m.group(1),m.group(2),m.group(3),m.group(4)
  self.pw=None
  self.mw = None
 
def init_pwgverb(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = [Pwgverb(x) for x in f if x.startswith(';; Case')]
 print(len(recs),"records read from",filein)
 return recs

class Pwmw(object):
 def __init__(self,line):
  line = line.rstrip()
  self.line = line
  self.pw,self.mw = line.split(':')
 
def init_pw_mw(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = [Pwmw(x) for x in f if not x.startswith(';')]
 print(len(recs),"records read from",filein)
 return recs

class MWVerb(object):
 def __init__(self,line):
  line = line.rstrip()
  self.line = line
  self.k1,self.L,self.cat,self.cps,self.parse = line.split(':')
  self.used = False

def init_mwverbs(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = [MWVerb(x) for x in f]
 print(len(recs),"mwverbs read from",filein)
 #recs = [r for r in recs if r.cat == 'verb']
 #recs = [r for r in recs if r.cat in ['root','genuineroot']]
 #recs = [r for r in recs if r.cat == 'verb']
 print(len(recs),"verbs returned from mwverbs")
 d = {}
 for rec in recs:
  k1 = rec.k1
  if k1 in d:
   print('init_mwverbs: Unexpected duplicate',k1)
  d[k1] = rec
 return recs,d

map2mw_special = {
 'aMSay':'aMS',
 'aMsay':'aMs',
 'aNkay':'aNk',
 'aNgay':'aNg',
 'huMkar':'huMkf',
 'unmUlay':'unmUl',
 'aMSApay':'aMS',
 'aYcay':'aYc',
 'anDay':'anD',
 'Urjay':'Urj',
 'kuhay':'kuh',
 'kzAray':'kzar',
 'jyApay':'jyA',  # causal
 'tilakAy':'tilakaya',   # are both forms ok?
 'nivAsay':'nivas',   # causal
 'mfgy':'mfg',
 'varRay':'varR',
 'vittay':'vitt',
 'Sulkay':'Sulk',
 'Sulbay':'Sulb',
 'SUrpay':'SUrp',
 'SvaBray':'SvaBr',
 'saMgrAmay':'saMgrAm',  # prefixed form in mwverbs
 'sAway':'sAw',
 'suKay':'suK',
 'stenay':'sten',
 'sTUlay':'sTUl',
 'sPuway':'sPuw', # causal
 'BAvay':'BU',  # causal, also denom. of bahu in pwg.
 'arR':'fR',
 'art':'ft',
 'arP':'fP',
 'aSv':'aSva',
 'ulaRq':'ulaq',
 'fBukzIn':'fBukzIRa',
 'kamalAhAs':'kamalAhAsa',
 'kartra':'kartr',
 'kfpaR':'kfpaRa',
 'kfzR':'kfzRa',
 'gomat':'gomata',
 'gozw':'gozwa',
 'GraRR':'GfRR',
 'carp':'cfp',
 'Carp':'Cfp',
 'jA':'jE',
 'Jar':'JF',
 'taraMg':'taraMga',
 'tarkz':'tfkz',
 'tarR':'tfR',
 'tarP':'tfP',
 'dyA':'dyE',
 'dvar':'dvf',
 'Darj':'Dfj',
 'Darm':'Darma',
 'Dvar':'Dvf',
 'nar':'nF',
 'parj':'pfj',
 'parq':'pfq',
 'pIv':'pIva',
 'preR':'prER',   # both refer to pER
 'Braq':'Bfq',
 'marR':'mfR',
 'mliC':'mleC',
 'yucC':'yuC',
 'rAjAn':'rAjAna',
 'lacC':'laC',
 'vark':'vfk',
 'varS':'vfS',
 'vAvart':'vAvft',
 'vrIMs':'vrIs',
 'vrUz':'vrUs',   # in MW, could add alternate headword 'vrUz' after 210819,vrUs
 'SaSv':'SaSva',
 'sarB':'sfB',
 'sIv':'siv',
 'starkz':'stfkz',
 'starh':'stfh',
 'stA':'stE',
 'sparh':'spfh',
 'viklav':'viklavaya',
 'varD':'vfD',  # mw has varD, but vfD is better match
 'dar':'dF',
 'sarj':'sfj',
 'staB':'stamB',
 'Gar':'Gf',
 'hUrC':'hurC', # mw has both forms.  Only hurC with prefixes
 'avaDIray':'avaDIr',
 'Ary':'Ar',  # also 'Ar' in pwg
 'camIkar':'camIkf',
 'pUr':'pF', # causal
 'prativimbay':'pratibimbaya',
 'kawakawA':'kawakawAya',
 'kumBay':'kumB',
 'krIqApay':'krIq', # causal
 'tIrTIkar':'tIrTIkf',
 'sv':'sva',
 'svaj':'svaYj', # for mapping preverbs
 'SA':'Si',
 'avacUrRay':'avacUrR',
 'Ips':'Ap', # desiderative of Ap
 'uttaraMg':'uttaraMga',
 'utsukay':'utsukAya',
 'unmUl':'unmUla',
 'karakAsAr':'karakAsAra',
 'karpUr':'karpUra',
 'kalah':'kalaha',
 'kalpaSatAy':'kalpaSata',
 'kuzuB':'kuzuBya',
 'keliSvetasahasrapattr':'keliSvetasahasrapattra',
 'kzIbay':'kzIb',
 'klIbay':'klIb',
 'kzepay':'kzip', # or kzi
 'gaC':'gam',
 'gardaB':'gardaBa',
 'gir':'gF',
 'gUrDay':'gUrD',
 'GarR':'GfR',
 'GiR':'GiRR',
 'Golay':'Gol',
 'cimicimAy':'cimicimAya',
 'jagannetr':'jagannetra',
 'jaNgah':'jaMh',  # intensive
 'jIvApay':'jIv', #causal
 'tantasy':'taMs', # intensive.  also tantasya entry
 'dantapattr':'dantapattra',
 'dIdi':'dI',
 'duHK':'duHKa',
 'durvAtay':'durvAtAya',
 'DrAj':'DraYj',
 'papasy':'papasya',
 'pallav':'pallava',
 'pARqucCattr':'pARqucCattra',
 'pib':'pA',
 'pIyUz':'pIyUza',
 'pUray':'pF', # causal
 'prabal':'prabala',
 'pruzwAy':'pruzwAyate', # mw verb form
 'preNKol':'preNKola',
 'mawAmawAy':'mawamawAya',
 'mitr':'mitra',
 'mits':'mA',  # desiderative also 'mI'
 'yaC':'yam',
 'radAvalidvaMdva':'radAvalidvandva',
 'raz':'fz',
 'romAYc':'romAYca',
 'laYjApay':'laYj',
 'lahalahAy':'lahalahAya',
 'lAwy':'lAwyAya', #?
 'lApay':'lap', # causal
 'vaRwApay':'vaRw',
 'vaBra':'vaBr',
 'varkz':'vfkz',
 'varDApay':'vfD', # causal
 'vikAsinIlotpal':'vikAsinIlotpala',
 'viDav':'viDava',
 'vipay':'vip', # causal
 'vilInay':'vilI', # causal of prefixed verb
 'SabdApay':'Sabd', # class 10 form?
 'SaraSarAy':'SaraSarAya',
 'SimiSimAy':'SimiSimAya',
 'SiriSirAy':'SiriSirAya',
 'SuBay':'SuB', # causal
 'SrIKaRqatamAlapattr':'SrIKaRqatamAlapattra',
 'zaRqay':'zaRqaya',
 'zaRqIy':'zaRqIya',
 'saMpAtay':'sampat', # causal
 'sambary':'sambarya',
 'saMBARqay':'samBARqaya',
 'saMBUyasy':'samBUyasya',
 'saMmuKay':'sammuKaya',
 'savitar':'savitara',
 'suDAdrav':'suDAdrava',
 'suradvip':'suradvipa',
 'sKuqa':'sKuq',
 'sPAyatkErav':'sPAyatkErava',
 'sPuwabudbud':'sPuwabudbuda',
 'haMs':'haMsa',
 'hAr':'hAra',
 'hArApay':'hf', # causal
 'hoQ':'hoQa',
 'hoQAy':'hoQa',
 'aDyApay':'aDI', # causal
 'aruz':'aruza',
 'utpAMsay':'utpuMsaya',  # mentioned in MW.
 'udgiray':'udgF', # causal
 'oMkArIy':'omkArIya',
 'katray':'katr',
 'kamalabAlanAlAy':'kamalabAlanAlaya', # note nAlAy vs. nAlaya (A/a). ?
 'karRay':'karR',
 'kir':'kF',
 'kutsy':'kuts',
 'kUpay':'kUp',
 'krIqArAjatasuDIpAtr':'krIqArAjatasuDApAtra',  # note suDI v. suDA
 'Karba':'Karb',
 'gahay':'gah', # class 10
 'gil':'gF',
 'tir':'tF',
 'tIvray':'tIvraya',
 'dulay':'duri',
 'dUtay':'dUtaya',
 'drAGay':'drAG', # causal
 'nakzatramAlAy':'nakzatramAlAya',
 'nizkay':'nizk',
 'padmakoSAy':'padmakoSAya',
 'praR':'pF',
 'prasAd':'prasAda',
 'prAyaScittIy':'prAyaScittIya',
 'prAley':'prAleya',
 'prASApay':'prAS', # caus. of prefix pra + aS
 'maRway':'maRw',
 'SUray':'SUr',
 '':'',
 '':'',

 
}
"""
 PWG corrections
"""
def map2mw(d,k1):
 if k1 in map2mw_special:
  return map2mw_special[k1]
 if k1 in d:
  return k1
 if k1.endswith('y'):
  k = k1 + 'a'
  if k in d:
   return k
 
 return '?'
 if not k1.endswith('a'):
  return None
 k = k1[0:-1] # remove final 'a'
 if k in d:
  return k
 k2 = re.sub(r'(.)\1',r'\1',k)
 if k2 in d:
  return k2
 return '?'

def pwgmap(recs,pwmw,mwd):
 pwmwd = {}
 for r in pwmw:
  pw = r.pw
  mw = r.mw
  if pw in pwmwd:
   print('duplicate pw',pw)
  pwmwd[pw] = mw

 for rec in recs:
  if rec.k1 in pwmwd:
   rec.pw = rec.k1
   rec.mw = pwmwd[rec.k1]
   if rec.mw == '?':
    rec.mw = map2mw(mwd,rec.k1)
   continue
  rec.pw='?'
  # try mw spelling directly
  rec.mw = map2mw(mwd,rec.k1)


def write(fileout,recs):
 n = 0
 with codecs.open(fileout,"w","utf-8") as f:
  for rec in recs:
   n = n + 1
   line = rec.line
   # add mw
   out = '%s, mw=%s' %(line,rec.mw)
   f.write(out + '\n')
 print(n,"records written to",fileout)

if __name__=="__main__": 
 filein = sys.argv[1] #  pwg_verb_filter.txt
 filein1 = sys.argv[2] # pw_mw_map_edit.txt
 filein2 = sys.argv[3] # mwverbs1
 fileout = sys.argv[4]

 recs = init_pwgverb(filein)
 pwmwrecs = init_pw_mw(filein1)
 mwverbrecs,mwverbsd= init_mwverbs(filein2)
 pwgmap(recs,pwmwrecs,mwverbsd)
 write(fileout,recs)
