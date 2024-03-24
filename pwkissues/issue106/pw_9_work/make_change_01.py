# coding=utf-8
""" make_change_01.py for pw_9_work
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 print(len(lines),"from",filein)
 return lines

def write_lines(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for out in lines:
   f.write(out+'\n')  
 print(len(lines),"lines written to",fileout)

class Change:
 def __init__(self,metaline,lnum,old,new,cat):
  self.metaline = metaline
  self.lnum = lnum
  self.old = old
  self.new = new
  self.cat = cat
  #assert cat in ['meta','other','metabb']

def write_changes_helper(c):
 outarr = []
 #outarr.append('; %s cat=%s' % (c.metaline,c.cat))
 outarr.append('; %s' % c.metaline)
 # auto-comment-out some changes
 if c.cat.endswith('nochg'):
  outarr.append('; %s old %s' %(c.lnum,c.old))
  outarr.append(';')
  outarr.append('; %s new %s' %(c.lnum,c.new))
 else:
  outarr.append('%s old %s' %(c.lnum,c.old))
  outarr.append(';')
  outarr.append('%s new %s' %(c.lnum,c.new))
 outarr.append('; ----------------------------------------------')
 return outarr

def write_changes(fileout,changes,option):
 outrecs = []
 cats = []
 for c in changes:
  if c.cat not in cats:
   cats.append(c.cat)
 cats = sorted(cats)
 for cat0 in cats:
  changes1 = [c for c in changes if c.cat == cat0]
  outarr = [] # header
  outarr.append('; ******************************************************')
  if cat0.endswith('nochg'):
   outarr.append('; cat=%s: %s changes NOT MADE' % (cat0,len(changes1)))
   print('; cat=%s: %s' % (cat0,len(changes1)))
  else:
   outarr.append('; cat=%s: %s changes' % (cat0,len(changes1)))
   print('; cat=%s: %s changes' % (cat0,len(changes1)))
  outarr.append('; ******************************************************')
  outrecs.append(outarr)
  for c in changes1:
   outarr = write_changes_helper(c)
   outrecs.append(outarr)
 write_recs(fileout,outrecs,blankflag=False)

def write_recs(fileout,outrecs,printflag=True,blankflag=True):
 # outrecs is array of array of lines
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
   if blankflag:
    out = ''  # blank line separates recs
    f.write(out+'\n')
 if printflag:
  print(len(outrecs),"records written to",fileout)

def get_cat_0(old,new,cat0):
 old1 = old.replace('¦','')
 new1 = new.replace('¦','')
 old2 = old1.replace('.)',').')
 new2 = new1.replace('.)',').')
 if '¦' in old:
  if old1 == new1:
   cat = cat0 + ':¦'
  elif old2 == new2:
   cat = cat0 + ':¦).'
  else:
   cat = cat0 + ':¦other'
 else: # not '¦' in old:
  if old2 == new2:
   cat = cat0 + ':).'
  else:
   cat = cat0 + ':other'
 return cat

def get_cat_1(old,new,cat0):
 data = [
  ('a', '¦ (!) ',' (!)¦ '),
  ('b', '¦(!) ',' (!)¦ '),
  ('c','¦ (?) ',' (?)¦ '),
  ('d','#}(!)','#} (!)'),
  ]
 for cat1,a,b in data:
  old1 = old.replace(a,b)
  if old1 == new:
   catnew = '%s:%s' % (cat0,cat1)
   return catnew
 # None of the transformations explain the difference
 cat1 = 'other'
 catnew = '%s:%s' % (cat0,cat1)
 return catnew

def get_cat_2(old,new,cat0):
 data1 = [
  # Schol. = Scholiast
  ('a', ' <ab>Schol.</ab> zu <ls>' , ' <ls><ab>Schol.</ab> zu '),
  # Vorrede = preface
  ('b', 'Vorrede zu <ls>' , '<ls>Vorrede zu '),  # preface
  # Comm. = Commentary
  ('c', '</ls> <ab>Comm.</ab>' , ' <ab>Comm.</ab></ls>'),
  ('d', '— ?' , '—?'),
  ('e', ' Mit' , ' mit'),
  ('f', '_' , ' '),
  ('g', '%} ?' , '?%}'),
  ('ls7', '<ab>Schol.</ab> zu <ls>' , '<ls><ab>Schol.</ab> zu '),
  ('ls8', '<ab>Sch.</ab> zu <ls>' , '<ls><ab>Sch.</ab> zu '),
  ('h', '{%*' , '*{%'),
  ('ls6', 'Text zu <ls>Lot.' , '<ls>Text zu Lot.'),
  ('ls2', '<ls>SĀY.</ls> zu <ls>' , '<ls>SĀY. zu '),
  ('ls3', '<ls>KĀŚ.</ls> zu <ls>' , '<ls>KĀŚ. zu '),
  ('ls4', '<ls>ŚAṂK.</ls> zu <ls>' , '<ls>ŚAṂK. zu '),
  ('ls5', '</ls> zu <ls>' , ' zu '),
  #('b', '' , ''),
  ]
 for cat1,a,b in data1:
  old1 = old.replace(a,b)
  if old1 == new:
   catnew = '%s:%s' % (cat0,cat1)
   return catnew
 #
 old1 = re.sub(r'[.,]','',old)
 new1 = re.sub(r'[.,]','',new)
 if old1 == new1:
  cat1 = 'punct'
  catnew = '%s:%s' % (cat0,cat1)
  return catnew
 # replacement of a 'naked' ls
 m = re.search(r'<ls>([0-9., ]+)</ls>',old)
 if m != None:
  x = m.group(0)
  old1 = old.replace(x,'')
  z = m.group(1)
  new1 = re.sub(r'<ls[^>]*>%s</ls>' % z,'',new)
  if old1 == new1:
   cat1 = 'ls10'
   catnew = '%s:%s' % (cat0,cat1)
   return catnew
 # difference only within <ls...</ls>
 old1 = re.sub(r'<ls[^<]*</ls>','',old)
 new1 = re.sub(r'<ls[^<]*</ls>','',new)
 if old1 == new1:
   cat1 = 'ls'
   catnew = '%s:%s' % (cat0,cat1)
   return catnew
 # difference with <ls> and <ab>Comm.</ab>
 old1 = re.sub(r'<ls[^<]*</ls>','',old)
 old1 = re.sub(r'<ab>Comm.</ab>','',old1)
 old1 = re.sub(r'<ab>Schol.</ab>','',old1)
 old1 = old1.replace(' ','')
 new1 = re.sub(r'<ls[^<]*</ls>','',new)
 new1 = new1.replace(' ','') 
 if old1 == new1:
   cat1 = 'ls1'
   catnew = '%s:%s' % (cat0,cat1)
   return catnew
 # difference only in Devanagari
 old1 = old.replace('{#','')
 old1 = old1.replace('#}','')
 old1 = old1.replace(' ','')
 old1 = re.sub(r'<ls[^<]*</ls>','',old1)
 new1 = new.replace('{#','')
 new1 = new1.replace('#}','')
 new1 = new1.replace(' ','')
 new1 = re.sub(r'<ls[^<]*</ls>','',new1)
 if old1 == new1:  # no instances!
   cat1 = 'lsdeva'
   catnew = '%s:%s' % (cat0,cat1)
   return catnew
 if len(old) == len(new):
   cat1 = 'samelen'
   catnew = '%s:%s' % (cat0,cat1)
   return catnew
 """
 if abs(len(old) - len(new)) == 1:
   cat1 = 'samelen1'
   catnew = '%s:%s' % (cat0,cat1)
   return catnew
 """
 # None of the transformations explain the difference
 cat1 = 'other'
 catnew = '%s:%s' % (cat0,cat1)
 return catnew

lnums_nochange = [
 # hiatus, etc.
 13602, 13603, 320820, 320821, 344710, 344711, 362995, 407261, 407262,
 494459, 550699, 550700, 617662, 617663,
 62994,  # prAg_hAra
 81850, # {#ISvare (<ab>Loc.</ab>) nityasuKAvasTApanam#
 
 ]
lnums_nochange_query = [
 #41908,  # (are 're)
 #89417,
 ]
lnums_ok = [  # these have been examined by Jim and Jim agrees.
 22247, 34714, 69282, 100973, 111891, 132517, 217725, 220641, 232716, 240902,
 275432, 275433, 337863, 341223, 387317, 400458, 492332, 502208, 643018, 645182,
 733270, 749510, 411906, 706474, 756156, 516390, 616445, 709049, 754514, 762587,
 475631, 346038,
 ]
revisions = [
 # (lnum,ab,abnew)
 (753997,
  """!√{#PARway#}¦ <ab>Denomin.</ab> von {#PARwa#} <ls>DĀRILA [Page7-363-b] zu KAUŚ. 25,18</ls>.<info n="sup_7"/>""",
  """!√{#PARway#}¦ <ab>Denomin.</ab> von {#PARwa#} <ls>DĀRILA zu KAUŚ. 25,18</ls>.[Page7-363-b]<info n="sup_7"/>"""),
 ]
def init_pwchanges(lines,lines1,cat0):
 # lines ../temp_pw_9.txt
 # lines1  temp_pw_ab_1.txt
 changes = []
 meta = None
 Fname = 'get_cat_%s' %cat0
 catF = globals()[Fname]

 for iline,line in enumerate(lines):
  line1 = lines1[iline]
  if line.startswith('<L>'):
   meta = line
  if line == line1:
   continue
  metaline = meta
  lnum = iline + 1
  old = line
  new = line1
  cat = catF(old,new,cat0)
  if lnum in lnums_nochange:
   cat = '%s:revised_nochg' % cat0
  elif lnum in lnums_nochange_query:
   cat = '%s:?nochg' % cat0
  elif lnum in lnums_ok:
   cat = '%s:ok' % cat0
  for lnum_new,new1,new2 in revisions:
   if lnum_new == lnum:
    assert new == new1
    new = new2
    cat = '%s:revised' % cat0
    break
  change = Change(metaline,lnum,old,new,cat)
  changes.append(change)
 return changes

def make_changes_1(lines,lines1):
 cat = '1'
 changes = init_pwchanges(lines,lines1,cat)
 return changes

def make_changes_2(lines,lines1):
 cat = '2'
 changes = init_pwchanges(lines,lines1,cat)
 return changes

if __name__=="__main__":
 option = sys.argv[1]
 filein = sys.argv[2]   # pw file
 filein1 = sys.argv[3] # AB's version of pw
 fileout = sys.argv[4]  # change file
 lines = read_lines(filein)
 lines1 = read_lines(filein1)
 Fname = 'make_changes_%s' %option
 changeF = locals()[Fname]
 changes = changeF(lines,lines1)
 write_changes(fileout,changes,option)
