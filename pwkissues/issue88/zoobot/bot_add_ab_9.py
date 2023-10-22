#-*- coding:utf-8 -*-
"""bot_add_ab_9.py Additional bot tags
"""
import sys,re,codecs
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec cannot encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def init_dbot_special():
 d={}
 # (1143): <bot>Elacocarpus Ganitrus</bot>
 d[1143] = \
  ('<div n="1">— 5〉 *{%der Same von Elacocarpus Ganitrus <ab n="und">u.</ab> einer anderen Pflanze%}.',
  '<div n="1">— 5〉 *{%der Same von <bot>Elacocarpus Ganitrus</bot> <ab n="und">u.</ab> einer anderen Pflanze%}.')
 # (1352): <bot>Elacocarpus Ganitrus</bot>
 d[1352] = \
  ('<div n="1">— 1〉 {%ein Rosenkranz den Samenkörnern des Elacocarpus Ganitrus%}.',
  '<div n="1">— 1〉 {%ein Rosenkranz den Samenkörnern des <bot>Elacocarpus Ganitrus</bot>%}.')
 # (10323): <bot>Calotropis gigantea</bot>
 d[10323] = \
  ('*{#atyarka#}¦ <lex>m.</lex> {%die weisse Calotropis gigantea%} <ls>RĀJAN. 10,29</ls>.',
  '*{#atyarka#}¦ <lex>m.</lex> {%die weisse <bot>Calotropis gigantea</bot>%} <ls>RĀJAN. 10,29</ls>.')
 # (11071): <bot>Barringtonia acutangula Gaertn.</bot>
 d[11071] = \
  ('<div n="1">— 1〉 <lex>m.</lex> {%Barringtonia actangula Gaertn%}.',
  '<div n="1">— 1〉 <lex>m.</lex> {%<bot>Barringtonia actangula Gaertn.</bot>%}')
 # (25266): <bot>Flacourtia cataphracta</bot>
 d[25266] = \
  ('<div n="1">— 2〉 *{%das Blatt der Flacourtia cataphracta%} <ls>GAL.</ls>',
  '<div n="1">— 2〉 *{%das Blatt der <bot>Flacourtia cataphracta</bot>%} <ls>GAL.</ls>')
 # (36301): <bot>Valeriana jatamansi Jones</bot>
 d[36301] = \
  ('*{#aBramAMsI#}¦ <lex>f.</lex> {%eine kleinere Species der Valeriana jatamansi Jones%} (im Gebirge <is>Kedāra</is>) <ls>RĀJAN. 12,104</ls>.',
  '*{#aBramAMsI#}¦ <lex>f.</lex> {%eine kleinere Species der <bot>Valeriana jatamansi Jones</bot>%} (im Gebirge <is>Kedāra</is>) <ls>RĀJAN. 12,104</ls>.')
 # (38013): <bot>Emblica officinalis Gaertn.</bot>
 d[38013] = \
  ('<div n="1">— 2〉 *<lex>f.</lex> {#A#} {%Weinstock und Emblica officinalis Gaertn%}.',
  '<div n="1">— 2〉 *<lex>f.</lex> {#A#} {%Weinstock und <bot>Emblica officinalis Gaertn.</bot>%}')
 # (38216): <bot>Cocculus cordifolius</bot>
 d[38216] = \
  ('{#amftAzwaka#}¦ <lex>n.</lex> {%eine Verbindung von acht Stoffen, unter denen%} {#amftA#} {%(Cocculus cordifolius) vornan steht%} <ls>Mat. med. 136. 192</ls>.',
  '{#amftAzwaka#}¦ <lex>n.</lex> {%eine Verbindung von acht Stoffen, unter denen%} {#amftA#} {%(<bot>Cocculus cordifolius</bot>) vornan steht%} <ls>Mat. med. 136. 192</ls>.')
 # (40990): <bot>Nelumbium speciosum</bot> oder <bot>Nymphaea nelumbo</bot>
 d[40990] = \
  ('<div n="1">— 1〉 <lex>n.</lex> {%die am Tage blühende wohlriechende Blüthe von Nelumbium speciosum oder Nymphaea nelumbo%}. Davon <ab>Nom. abstr.</ab> {#°tA#} <lex>f.</lex> <ls n="Chr.">251,27</ls>. {#°tva#} <lex>n.</lex> •[Page1105-3] •<ls>TARKAS. 43</ls>.',
  '<div n="1">— 1〉 <lex>n.</lex> {%die am Tage blühende wohlriechende Blüthe von <bot>Nelumbium speciosum</bot>%} oder {%<bot>Nymphaea nelumbo</bot>%}. Davon <ab>Nom. abstr.</ab> {#°tA#} <lex>f.</lex> <ls n="Chr.">251,27</ls>. {#°tva#} <lex>n.</lex> •[Page1105-3] •<ls>TARKAS. 43</ls>.')
 # (54856): <bot>Physalis flexuosa L.</bot>
 d[54856] = \
  ('<div n="1">— 2〉 *<lex>f.</lex> {#A#} {%physalis flexuosa%} L.',
  '<div n="1">— 2〉 *<lex>f.</lex> {#A#} {%<bot>physalis flexuosa L.</bot>%}')
 # (62608): <bot>Agati grandiflora</bot>
 d[62608] = \
  ('<div n="2">— b〉 {%von der Pflanze Agati grandiflora herrührend%}.',
  '<div n="2">— b〉 {%von der Pflanze <bot>Agati grandiflora</bot> herrührend%}.')
 # (69223): <bot>Asparagus</bot> und *— <bot>Zizyphus</bot>
 d[69223] = \
  ('<div n="1">— 3〉 *{%eine Art Asparagus%} und *— {%Zizyphus%} <ls>NIGH. PR.</ls>',
  '<div n="1">— 3〉 *{%eine Art <bot>Asparagus</bot>%} und *— {%<bot>Zizyphus</bot>%} <ls>NIGH. PR.</ls>')
 # (71434): <bot>Semecarpus Anacardium L.</bot>
 d[71434] = \
  ('{#Aruzkara#}¦ <lex>n.</lex> {%die Frucht von Semecarpus Anacardium%} L.',
   '{#Aruzkara#}¦ <lex>n.</lex> {%die Frucht von <bot>Semecarpus Anacardium L.</bot>%}')
 # (71659): <bot>Calotropis gigantea</bot>
 d[71659] = \
  ('<div n="2">— b〉 {%von der Calotropis gigantea kommend%}.',
  '<div n="2">— b〉 {%von der <bot>Calotropis gigantea</bot> kommend%}.')
 # (72984): <bot>Feronia elephantum</bot>
 d[72984] = \
  ('<div n="2">— c〉 *{%die Rinde von Feronia elephantum%}.',
  '<div n="2">— c〉 *{%die Rinde von <bot>Feronia elephantum</bot>%}.')
 # (82498): <bot>Aconitum ferox Wall.</bot>
 d[82498] = \
  ('<div n="1">— 5〉 *<lex>n.</lex> {%die Wurzel von Aconitum ferox Wall%}.',
  '<div n="1">— 5〉 *<lex>n.</lex> {%die Wurzel von <bot>Aconitum ferox Wall.</bot>%}')
 # (97010): <bot>Eleusine indica Gaertn.</bot>
 d[97010] = \
  ('<div n="1">— 3〉 <lex>m.</lex> {%leusine indica Gaertn%}. <ls>MAHĪDH.</ls> zu <ls>VS. 16,45</ls>.',
  '<div n="1">— 3〉 <lex>m.</lex> {%<bot>Eleusine indica Gaertn.</bot>%} <ls>MAHĪDH.</ls> zu <ls>VS. 16,45</ls>.')
 # (97607): <bot>Piper longum</bot>
 d[97607] = \
  ('<div n="2">— b〉 {%die Wurzel von Piper longum%}.',
  '<div n="2">— b〉 {%die Wurzel von <bot>Piper longum</bot>%}.')
 # (104616): <bot>Feronia elephantum</bot>
 d[104616] = \
  ('{#elavAlu#} und {#°ka#}¦ <lex>n.</lex> {%die wohlriechende Rinde von Feronia elephantum; ein rothes Pulver (der Same einer <ab>best.</ab> Pflanze)%} <ls>Mat. med. 297</ls>.',
  '{#elavAlu#} und {#°ka#}¦ <lex>n.</lex> {%die wohlriechende Rinde von <bot>Feronia elephantum</bot>; ein rothes Pulver (der Same einer <ab>best.</ab> Pflanze)%} <ls>Mat. med. 297</ls>.')
 # (118990): <bot>Asa foetida</bot>
 d[118990] = \
  ('<div n="2">— d〉 {%das Blatt der Asa foetida%}.',
  '<div n="2">— d〉 {%das Blatt der <bot>Asa foetida</bot>%}.')
 # (146656): <bot>Bos grunniens</bot>
 d[146656] = \
  ('<div n="2">— c〉 <ab>Pl.</ab> {%Schweif%} (des Bos grunniens) <ls n="Chr.">233,16</ls>.',
  '<div n="2">— c〉 <ab>Pl.</ab> {%Schweif%} (des <bot>Bos grunniens</bot>) <ls n="Chr.">233,16</ls>.')
 # (148595): <bot>Piper Chaba</bot>
 d[148595] = \
  ('<div n="2">— b〉 *{%schwarzer Pfeffer und *das Korn von Piper Chaba%} <ls>RĀJAN. 6,31. 42</ls>.',
  '<div n="2">— b〉 *{%schwarzer Pfeffer und *das Korn von <bot>Piper Chaba</bot>%} <ls>RĀJAN. 6,31. 42</ls>.')
 # (148653): <bot>Piper longum</bot>
 d[148653] = \
  ('*{#kolamUla#}¦ <lex>n.</lex> {%die Wurzel von Piper longum%} <ls>RĀJAN. 6,22</ls>.',
  '*{#kolamUla#}¦ <lex>n.</lex> {%die Wurzel von <bot>Piper longum</bot>%} <ls>RĀJAN. 6,22</ls>.')
 # (171240): <bot>Bos grunniens</bot>
 d[171240] = \
  ('*{#giripriyA#}¦ <lex>f.</lex> {%das Weibchen des Bos grunniens%}.',
  '*{#giripriyA#}¦ <lex>f.</lex> {%das Weibchen des <bot>Bos grunniens</bot>%}.')
 # (189805): <bot>Bos grunniens</bot>
 d[189805] = \
  ('<div n="1">— 2〉 <lex>m.</lex> <lex>n.</lex> {%der als Fliegenwedel gebrauchte Schweif des Bos grunniens%}.',
  '<div n="1">— 2〉 <lex>m.</lex> <lex>n.</lex> {%der als Fliegenwedel gebrauchte Schweif des <bot>Bos grunniens</bot>%}.')
 # (214912): <bot>Bos Gaurus</bot>
 d[214912] = \
  ('<div n="2">— a〉 {%Schwanz, — eines Schakals, jeglicher Schwanz mit Ausnahme des vom Bos Gaurus%}.',
  '<div n="2">— a〉 {%Schwanz, — eines Schakals, jeglicher Schwanz mit Ausnahme des vom <bot>Bos Gaurus</bot>%}.')
 # (217884): <bot>Calotropis gigantea</bot>
 d[217884] = \
  ('<div n="2">— h〉 *{%Calotropis gigantea und eine weisse Varietät derselben%} <ls>RĀJAN. 10,29</ls>.',
  '<div n="2">— h〉 *{%<bot>Calotropis gigantea</bot> und eine weisse Varietät derselben%} <ls>RĀJAN. 10,29</ls>.')
 # (243226): <bot>Feronia elephantum</bot>
 d[243226] = \
  ('{#dADitTa#}¦ <lex>Adj.</lex> (*<lex>f.</lex> {#I#}) {%von der Feronia elephantum kommend;%} <lex>n.</lex> {%die Frucht dieses Baumes%}.',
  '{#dADitTa#}¦ <lex>Adj.</lex> (*<lex>f.</lex> {#I#}) {%von der <bot>Feronia elephantum</bot> kommend;%} <lex>n.</lex> {%die Frucht dieses Baumes%}.')
 # (251804): <bot>Feronia elephantum</bot>
 d[251804] = \
  ('<div n="2">— b〉 *{%die wohlriechende Rinde von Feronia elephantum%} <ls>RĀJAN. 4,126</ls>.',
  '<div n="2">— b〉 *{%die wohlriechende Rinde von <bot>Feronia elephantum</bot>%} <ls>RĀJAN. 4,126</ls>.')
 # (252754): <bot>Acacia Catechu</bot>
 d[252754] = \
  ('*{#duzKadira#}¦ <lex>m.</lex> {%ein der Acacia Catechu verwandter Baum%}.',
  '*{#duzKadira#}¦ <lex>m.</lex> {%ein der <bot>Acacia Catechu</bot> verwandter Baum%}.')
 # (288286): <bot>Azadirachta indica</bot>
 d[288286] = \
  ('*{#nimbapaYcaka#}¦ <lex>n.</lex> {%die fünf Dinge (Blätter, Rinde, Blüthe, Frucht und Wurzel) der Azadirachta indica%} <ls>RĀJAN. 22,30</ls>.',
  '*{#nimbapaYcaka#}¦ <lex>n.</lex> {%die fünf Dinge (Blätter, Rinde, Blüthe, Frucht und Wurzel) der <bot>Azadirachta indica</bot>%} <ls>RĀJAN. 22,30</ls>.')
 # (300341): <bot>Nauclea Cadamba</bot>
 d[300341] = \
  ('*{#nEpa#}¦ <lex>Adj.</lex> (<lex>f.</lex> {#I#}) {%von der Nauclea Cadamba kommend%}.',
  '*{#nEpa#}¦ <lex>Adj.</lex> (<lex>f.</lex> {#I#}) {%von der <bot>Nauclea Cadamba</bot> kommend%}.')
 # (303193): <bot>Feronia elephantum</bot>
 d[303193] = \
  ('{#paYcakApitTa#}¦ <lex>Adj.</lex> {%mit den fünf Erzeugnissen der Feronia elephantum zubereitet%}.',
  '{#paYcakApitTa#}¦ <lex>Adj.</lex> {%mit den fünf Erzeugnissen der <bot>Feronia elephantum</bot> zubereitet%}.')
 # (310060): <bot>Gynandropsis pentaphylla</bot>
 d[310060] = \
  ('<div n="2">— b〉 <ab>Bez.</ab> {%verschiedener Pflanzen%} <ls>CARAKA. 1,4</ls>. nach den Lexicographen {%Gynandropsis pentaphylla,%} {#kAkolI, kzIrakAkolI#} (<ls>RĀJAN. 3,16</ls>)., {#kuwumbinI#}. (<ls>RĀJAN. 5,76</ls>)., {#dugDikA, SvetavidArikanda#} (<ls><ab>Comm.</ab> zu CARAKA. 1,4</ls>) und {#svarRakzIrI#}.',
  '<div n="2">— b〉 <ab>Bez.</ab> {%verschiedener Pflanzen%} <ls>CARAKA. 1,4</ls>. nach den Lexicographen {%<bot>Gynandropsis pentaphylla</bot>,%} {#kAkolI, kzIrakAkolI#} (<ls>RĀJAN. 3,16</ls>)., {#kuwumbinI#}. (<ls>RĀJAN. 5,76</ls>)., {#dugDikA, SvetavidArikanda#} (<ls><ab>Comm.</ab> zu CARAKA. 1,4</ls>) und {#svarRakzIrI#}.')
 # (387954): <bot>Semecarpus Anacardium</bot>
 d[387954] = \
  ('{#BallAta#}¦ <lex>m.</lex> {#°ka#} <lex>m.</lex> (<ls>BHĀVAPR. 1,179</ls>) und *{#kI#} <lex>f.</lex> {%Semecarpus Anacardium;%} <lex>n.</lex> {%die Nuss%}.',
  '{#BallAta#}¦ <lex>m.</lex> {#°ka#} <lex>m.</lex> (<ls>BHĀVAPR. 1,179</ls>) und *{#kI#} <lex>f.</lex> {%<bot>Semecarpus Anacardium</bot>;%} <lex>n.</lex> {%die Nuss%}.')
 # (452691): <bot>Caesalpina Sappan</bot>
 d[452691] = \
  ('*{#raktAkta#}¦ <lex>n.</lex> {%rother Sandel oder Caesalpina Sappon%}.',
  '*{#raktAkta#}¦ <lex>n.</lex> {%rother Sandel oder <bot>Caesalpina Sappon</bot>%}.')
 # (467804): <bot>Piper aurantiacum</bot>
 d[467804] = \
  ('<div n="2">— a〉 *{%ein <ab>best.</ab> Arzeneistoff; Piper aurantiacum%} (?) <ls>RĀJAN. 6,113</ls>.',
  '<div n="2">— a〉 *{%ein <ab>best.</ab> Arzeneistoff; <bot>Piper aurantiacum</bot>%} (?) <ls>RĀJAN. 6,113</ls>.')
 # (469154): <bot>Bos grunniens</bot>
 d[469154] = \
  ('*{#romagucCa#}¦ <lex>m.</lex> und *{#romagutsa#} <lex>n.</lex> {%der als Fliegenwedel gebrauchte Schweif des Bos grunniens%}.',
  '*{#romagucCa#}¦ <lex>m.</lex> und *{#romagutsa#} <lex>n.</lex> {%der als Fliegenwedel gebrauchte Schweif des <bot>Bos grunniens</bot>%}.')
 # (470998): <bot>Nelumbium speciosum</bot>
 d[470998] = \
  ('{#lakzmIvasati#}¦ <lex>f.</lex> {%die Wohnstätte der%} <is>Lakṣmī</is> {%als%} <ab>Bez.</ab> {%der Blüthe von Nelumbium speciosum%}.',
  '{#lakzmIvasati#}¦ <lex>f.</lex> {%die Wohnstätte der%} <is>Lakṣmī</is> {%als%} <ab>Bez.</ab> {%der Blüthe von <bot>Nelumbium speciosum</bot>%}.')
 # (516826): <bot>Piper longum</bot>
 d[516826] = \
  ('<div n="1">— 4〉 *<lex>n.</lex> {%die Wurzel von Piper longum%} <ls>RĀJAN. 6,23</ls>. — {#virUpAya#} <ls>CĀṆ. 73</ls> bei <ls>WEBER.</ls> fehlerhaft für {#prakopAya#}; <ab>vgl.</ab> <ls>Spr. 1287</ls>.',
  '<div n="1">— 4〉 *<lex>n.</lex> {%die Wurzel von <bot>Piper longum</bot>%} <ls>RĀJAN. 6,23</ls>. — {#virUpAya#} <ls>CĀṆ. 73</ls> bei <ls>WEBER.</ls> fehlerhaft für {#prakopAya#}; <ab>vgl.</ab> <ls>Spr. 1287</ls>.')
 # (520535): <bot>Piper longum</bot>
 d[520535] = \
  ('<div n="2">— d〉 *Piper longum.',
  '<div n="2">— d〉 *{%<bot>Piper longum</bot>%}.')
 # (521795): <bot>Cactus indicus</bot>
 d[521795] = \
  ('*{#viSvasAraka#}¦ <lex>m.</lex> {%Cacutus indicus%}.',
  '*{#viSvasAraka#}¦ <lex>m.</lex> {%<bot>Cacutus indicus</bot>%}.')
 # (544350): <bot>Ungius adoratus</bot>
 d[544350] = \
  ('<div n="1">— 2〉 *{%Ungius adoratus oder ein anderer Parfum%}.',
  '<div n="1">— 2〉 *{%<bot>Ungius adoratus</bot>%} oder {%ein anderer Parfum%}.')
 # (557601): <bot>Piper longum</bot>
 d[557601] = \
  ('<div n="1">— 2〉 *{%die Wurzel von Piper longum%}. Auch {#sira#} geschrieben.',
  '<div n="1">— 2〉 *{%die Wurzel von <bot>Piper longum</bot>%}. Auch {#sira#} geschrieben.')
 # (558659): <bot>Feronia elephantum</bot>
 d[558659] = \
  ('<div n="2">— n〉 *{%die wohlriechende Rinde von Feronia elephantum%} <ls>H. an. 2,538</ls>.; <ab>vgl.</ab> <ls>ZACH. Beitr. 85</ls>.',
  '<div n="2">— n〉 *{%die wohlriechende Rinde von <bot>Feronia elephantum</bot>%} <ls>H. an. 2,538</ls>.; <ab>vgl.</ab> <ls>ZACH. Beitr. 85</ls>.')
 # (571782): <bot>Aegle Marmelos</bot>
 d[571782] = \
  ('<div n="2">— b〉 {%die Prachtfrucht,%} <ab>d. i.</ab> {%die Frucht von Aegle Marmelos%}.',
  '<div n="2">— b〉 {%die Prachtfrucht,%} <ab>d. i.</ab> {%die Frucht von <bot>Aegle Marmelos</bot>%}.')
 # (592788): <bot>Alstonia scholaris</bot>
 d[592788] = \
  ('<div n="2">— a〉 {%die Blüthe von Alstonia scholaris%}.',
  '<div n="2">— a〉 {%die Blüthe von <bot>Alstonia scholaris</bot>%}.')
 return d

d_bot_special = init_dbot_special()

class Bot:
 def __init__(self,line):
  # line example:
  #  (516826): <bot>Piper longum</bot>
  m = re.search(r'^\(([0-9]+)\): <bot>(.*?)</bot>$',line)
  self.line = line
  if m == None:
   self.status = False
   print('todo: %s' % line)
   return
  self.status = True
  self.name = m.group(2)
  self.lnum = int(m.group(1))
  self.count = 0  # number changed
  name = self.name
  if self.lnum in d_bot_special:
   replace = d_bot_special[self.lnum]
  elif name.endswith('.'):
   name0 = name[0:-1]  # remove trailing period
   replace = ('{%' + name0 + '%}.' , '{%<bot>' + name + '</bot>%}')
   # print('%s -> %s' % replace)
  else:
   replace = ('{%' + name + '%}' , '{%<bot>' + name + '</bot>%}')
  self.replacements = [
    replace
  ]
  
  if False: # dbg
   for x in self.replacements:
    print(x)
    
def init_bot_recs(filein):
 lines = read_lines(filein)
 d = {}
 recs = []
 ntodo = 0
 for line in lines:
  rec = Bot(line)
  if rec.status:
   recs.append(rec)
   if rec.lnum in d:
    print('Unexpected duplicate',rec.lnum)
   d[rec.lnum] = rec
  else:
   ntodo = ntodo + 1
 nrecs = len(recs)
 print(nrecs,"records from",filein)
 print(ntodo,"records remain to be done")
 return recs,d

def check_bot_recs(bot_recs,lines):
 n = 0
 outarr = []
 outarr.append('def init_dbot_special():')
 outarr.append(' d={}')
 for rec in bot_recs:
  if rec.count != 1:
   #print('todo:', rec.line)
   lnum = rec.lnum
   iline = lnum - 1
   line = lines[iline]
   outarr.append(' # %s' % rec.line)
   outarr.append(" d[%s] = \\\n  ('%s',\n  '%s')" % (lnum,line,line))
   n = n + 1
 outarr.append(' return d')

 print(n,"cases todo")
 fileout = "temp_bod_add_9.txt"
 write(fileout,outarr)
 
def adjust(lines,dlnum):
 newlines = []  # returned
 metaline = None
 nchg = 0
 for iline,line in enumerate(lines):
  lnum = iline + 1
  if lnum not in dlnum:
   newline = line
  else:
   rec = dlnum[lnum]
   replace = rec.replacements[0]
   old,new = replace
   newline = line.replace(old,new)
   if newline != line:
    rec.count = rec.count + 1
   
  newlines.append(newline)
  if newline != line:
   nchg = nchg + 1
 print(nchg,"lines changed")
 return newlines

def write(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for line in lines:
   f.write(line + '\n')
 print(len(lines),"written to",fileout)
 
if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 filein1 = sys.argv[2] # 
 fileout = sys.argv[3] # revised xxx.txt
 lines = read_lines(filein)
 bot_recs,bot_recs_d = init_bot_recs(filein1)
 newlines = adjust(lines,bot_recs_d)

 write(fileout,newlines)
 check_bot_recs(bot_recs,lines)
 
