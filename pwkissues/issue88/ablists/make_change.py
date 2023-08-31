# coding=utf-8
""" make_change.py
"""
from __future__ import print_function
import sys, re,codecs
import digentry

class Change(object):
 def __init__(self,iline,newline):
  self.iline = iline # index into entry.datalines
  # the old line is entry.datalines[iline]
  self.newline = newline # the new line

def change_1a(line):
 replacements = [('<ab>N.ag.</ab>', '<ab>N. ag.</ab>'),
  ('<ab>N.pr.</ab>', '<ab>N. pr.</ab>'),
  ('<ab>Nom.abstr.</ab>', '<ab>Nom. abstr.</ab>'),
  ('<ab>Nom.ag.</ab>', '<ab>Nom. ag.</ab>'),
  ('<ab>s.u.</ab>', '<ab>s. u.</ab>'),
  ('<ab>u.s.w.</ab>', '<ab>u. s. w.</ab>'),
  ('<ab>v.a.</ab>', '<ab>v. a.</ab>'),
  ('<ab>v.l.</ab>', '<ab>v. l.</ab>'),
  ('<ab>v.u.</ab>', '<ab>v. u.</ab>'),]
 for old,new in replacements:
  line = line.replace(old,new)
 return line

def change_1b(line):
 replacements = [
 ('absol.', '<ab>absol.</ab>'), # 3
 ('Adjj.', '<ab>Adjj.</ab>'), # 1
 ('Advv.', '<ab>Advv.</ab>'), # 1
 ('anat.', '<ab>anat.</ab>'), # 1
 ('Anf.', '<ab>Anf.</ab>'), # 78
 ('Anm.', '<ab>Anm.</ab>'), # 2
 ('Anmm.', '<ab>Anmm.</ab>'), # 1
 ('Arithm.', '<ab>Arithm.</ab>'), # 2
 ('Astr.', '<ab>Astr.</ab>'), # 36
 ('astr.', '<ab>astr.</ab>'), # 45
 ('astrol.', '<ab>astrol.</ab>'), # 107
 ('astron.', '<ab>astron.</ab>'), # 14
 ('Astron.', '<ab>Astron.</ab>'), # 14
 ('Ausg.', '<ab>Ausg.</ab>'), # 42
 ('Aut.', '<ab>Aut.</ab>'), # 1
 ('Autt.', '<ab>Autt.</ab>'), # 1
 ('Buddh.', '<ab>Buddh.</ab>'), # 10
 ('Chrest.', '<ab>Chrest.</ab>'), # 1
 ('Coll.', '<ab>Coll.</ab>'), # 2
 ('coll.', '<ab>coll.</ab>'), # 8
 ('collect.', '<ab>collect.</ab>'), # 12
 ('compon.', '<ab>compon.</ab>'), # 1
 ('Compp.', '<ab>Compp.</ab>'), # 19
 ('concr.', '<ab>concr.</ab>'), # 4
 ('Condit.', '<ab>Condit.</ab>'), # 10
 ('copul. Comp.', '<ab>copul. Comp.</ab>'), # 6
 ('Correl.', '<ab>Correl.</ab>'), # 6
 ('demonstr.', '<ab>demonstr.</ab>'), # 1
 ('Demonstr.', '<ab>Demonstr.</ab>'), # 2
 ('Den.', '<ab>Den.</ab>'), # 1
 ('dergl.', '<ab>dergl.</ab>'), # 11
 ('Desgl.', '<ab>Desgl.</ab>'), # 1
 ('dgl.', '<ab>dgl.</ab>'), # 56
 ('dopp.', '<ab>dopp.</ab>'), # 4
 ('Dram.', '<ab>Dram.</ab>'), # 1
 ('ebd.', '<ab>ebd.</ab>'), # 1
 ('enklit.', '<ab>enklit.</ab>'), # 1
 ('Erkl.', '<ab>Erkl.</ab>'), # 1
 ('etc.', '<ab>etc.</ab>'), # 15
 ('etym.', '<ab>etym.</ab>'), # 6
 ('euphem.', '<ab>euphem.</ab>'), # 9
 ('excl.', '<ab>excl.</ab>'), # 2
 ('Fem.', '<ab>Fem.</ab>'), # 3
 ('Femin.', '<ab>Femin.</ab>'), # 2
 ('Gedr.', '<ab>Gedr.</ab>'), # 1
 ('Gegens.', '<ab>Gegens.</ab>'), # 36
 ('Geom.', '<ab>Geom.</ab>'), # 1
 ('geom.', '<ab>geom.</ab>'), # 2
 ('geometr.', '<ab>geometr.</ab>'), # 1
 ('geschr.', '<ab>geschr.</ab>'), # 28
 ('Hdschrr.', '<ab>Hdschrr.</ab>'), # 32
 ('hdschrr.', '<ab>hdschrr.</ab>'), # 1
 ('Imper.', '<ab>Imper.</ab>'), # 20
 ('Imperat.', '<ab>Imperat.</ab>'), # 22
 ('imperat.', '<ab>imperat.</ab>'), # 1
 ('Imperf.', '<ab>Imperf.</ab>'), # 25
 ('Impers.', '<ab>Impers.</ab>'), # 4
 ('inbes.', '<ab>inbes.</ab>'), # 18
 ('indef.', '<ab>indef.</ab>'), # 3
 ('Indefin.', '<ab>Indefin.</ab>'), # 1
 ('Indic.', '<ab>Indic.</ab>'), # 3
 ('infin.', '<ab>infin.</ab>'), # 1
 ('insbe.', '<ab>insbe.</ab>'), # 1
 ('insbes.', '<ab>insbes.</ab>'), # 754
 ('Insbes.', '<ab>Insbes.</ab>'), # 51
 ('Inschr.', '<ab>Inschr.</ab>'), # 3
 ('instebs.', '<ab>instebs.</ab>'), # 1
 ('instr.', '<ab>instr.</ab>'), # 28
 ('intens.', '<ab>intens.</ab>'), # 1
 ('interr.', '<ab>interr.</ab>'), # 9
 ('Interr.', '<ab>Interr.</ab>'), # 4
 ('interrog.', '<ab>interrog.</ab>'), # 1
 ('Intr.', '<ab>Intr.</ab>'), # 12
 ('intr.', '<ab>intr.</ab>'), # 2
 ('Intrans.', '<ab>Intrans.</ab>'), # 1
 ('intransit.', '<ab>intransit.</ab>'), # 2
 ('Jahrh.', '<ab>Jahrh.</ab>'), # 4
 ('klass.', '<ab>klass.</ab>'), # 5
 ('liturg.', '<ab>liturg.</ab>'), # 3
 ('masc.', '<ab>masc.</ab>'), # 1
 ('Masc.', '<ab>Masc.</ab>'), # 1
 ('Math.', '<ab>Math.</ab>'), # 4
 ('math.', '<ab>math.</ab>'), # 1
 ('mathem.', '<ab>mathem.</ab>'), # 3
 ('Mathem.', '<ab>Mathem.</ab>'), # 2
 ('Neg.', '<ab>Neg.</ab>'), # 3
 ('Negat.', '<ab>Negat.</ab>'), # 1
 ('neutr.', '<ab>neutr.</ab>'), # 1
 ('Obj.', '<ab>Obj.</ab>'), # 43
 ('obj.', '<ab>obj.</ab>'), # 1
 ('onomat.', '<ab>onomat.</ab>'), # 3
 ('Onomatop.', '<ab>Onomatop.</ab>'), # 1
 ('Opt.', '<ab>Opt.</ab>'), # 3
 ('Optat.', '<ab>Optat.</ab>'), # 1
 ('optat.', '<ab>optat.</ab>'), # 1
 ('Ortsadv.', '<ab>Ortsadv.</ab>'), # 1
 ('Oxyt.', '<ab>Oxyt.</ab>'), # 1
 ('parox.', '<ab>parox.</ab>'), # 6
 ('Part.', '<ab>Part.</ab>'), # 1
 ('Personif.', '<ab>Personif.</ab>'), # 10
 ('personif.', '<ab>personif.</ab>'), # 26
 ('Phil.', '<ab>Phil.</ab>'), # 1
 ('philos.', '<ab>philos.</ab>'), # 2
 ('poss.', '<ab>poss.</ab>'), # 1
 ('Pot.', '<ab>Pot.</ab>'), # 1
 ('Poten.', '<ab>Poten.</ab>'), # 1
 ('praet.', '<ab>praet.</ab>'), # 21
 ('Praet.', '<ab>Praet.</ab>'), # 1
 ('Prec.', '<ab>Prec.</ab>'), # 3
 ('pron.', '<ab>pron.</ab>'), # 1
 ('Pronom.', '<ab>Pronom.</ab>'), # 1
 ('Pronomm.', '<ab>Pronomm.</ab>'), # 2
 ('proparox.', '<ab>proparox.</ab>'), # 2
 ('proparoxyt.', '<ab>proparoxyt.</ab>'), # 1
 ('Präpp.', '<ab>Präpp.</ab>'), # 1
 ('Red.', '<ab>Red.</ab>'), # 5
 ('redupl.', '<ab>redupl.</ab>'), # 1
 ('refl.', '<ab>refl.</ab>'), # 1
 ('reflex.', '<ab>reflex.</ab>'), # 5
 ('Rel.', '<ab>Rel.</ab>'), # 2
 ('relat.', '<ab>relat.</ab>'), # 1
 ('Relat.', '<ab>Relat.</ab>'), # 7
 ('resp.', '<ab>resp.</ab>'), # 2
 ('rhet.', '<ab>rhet.</ab>'), # 8
 ('s. d.', '<ab>s. d.</ab>'), # 1
 ('s. v.', '<ab>s. v.</ab>'), # 1
 ('sog.', '<ab>sog.</ab>'), # 3
 ('Subj.', '<ab>Subj.</ab>'), # 5
 ('subj.', '<ab>subj.</ab>'), # 2
 ('subst.', '<ab>subst.</ab>'), # 4
 ('Substr.', '<ab>Substr.</ab>'), # 1
 ('Suff.', '<ab>Suff.</ab>'), # 1
 ('term. techn.', '<ab>term. techn.</ab>'), # 1
 ('Trans.', '<ab>Trans.</ab>'), # 2
 ('Ueberh.', '<ab>Ueberh.</ab>'), # 2
 ('Uebers.', '<ab>Uebers.</ab>'), # 5
 ('Uebertr.', '<ab>Uebertr.</ab>'), # 3
 ('unbest.', '<ab>unbest.</ab>'), # 4
 ('uneig.', '<ab>uneig.</ab>'), # 19
 ('Uneig.', '<ab>Uneig.</ab>'), # 1
 ('ungedr.', '<ab>ungedr.</ab>'), # 2
 ('Unterschr.', '<ab>Unterschr.</ab>'), # 12
 ('urspr.', '<ab>urspr.</ab>'), # 2
 ('Verb.', '<ab>Verb.</ab>'), # 6
 ('Vergl.', '<ab>Vergl.</ab>'), # 1
 ('viell.', '<ab>viell.</ab>'), # 4
 ('Zahladv.', '<ab>Zahladv.</ab>'), # 2
 ]
 for old,new in replacements:
  line = line.replace(old,new)
 return line

def change_1c(line):
 replacements = [
 ('Adj. Comp.', '<ab>Adj. Comp.</ab>'), # 0,1
 ('Astrol.', '<ab>Astrol.</ab>'), # 41,44
 ('Beiz.', '<ab>Beiz.</ab>'), # 2,3
 ('Bes.', '<ab>Bes.</ab>'), # 5,3
 ('Cit.', '<ab>Cit.</ab>'), # 51,53
 ('Collect.', '<ab>Collect.</ab>'), # 5,6
 ('Compar.', '<ab>Compar.</ab>'), # 216,217
 ('Demin.', '<ab>Demin.</ab>'), # 44,45
 ('Denomin.', '<ab>Denomin.</ab>'), # 53,55
 ('Etym.', '<ab>Etym.</ab>'), # 2,3
 ('fut.', '<ab>fut.</ab>'), # 81,78
 ('Fut.', '<ab>Fut.</ab>'), # 75,76
 ('Handschrr.', '<ab>Handschrr.</ab>'), # 2,1
 ('imper.', '<ab>imper.</ab>'), # 8,4
 ('medic.', '<ab>medic.</ab>'), # 59,60
 ('Mss.', '<ab>Mss.</ab>'), # 2,1
 ('onomatop.', '<ab>onomatop.</ab>'), # 58,59
 ('Parox.', '<ab>Parox.</ab>'), # 4,3
 # ('oxyt.', '<ab>oxyt.</ab>'), # 22,20 interferes with paroxyt.
 #('paroxyt.', '<ab>paroxyt.</ab>'), # 2,1 interferes with proparoxyt
 ('Perf.', '<ab>Perf.</ab>'), # 49,50
 ('Pers.', '<ab>Pers.</ab>'), # 2,1
 ('Praep.', '<ab>Praep.</ab>'), # 42,46
 ('Praes.', '<ab>Praes.</ab>'), # 42,45
 ('praes.', '<ab>praes.</ab>'), # 8,11
 ('priv.', '<ab>priv.</ab>'), # 4,5
 ('proparox.', '<ab>proparox.</ab>'), # 0,2
 ('präd.', '<ab>präd.</ab>'), # 1,2
 ('Präs.', '<ab>Präs.</ab>'), # 0,1
 ('Pt.', '<ab>Pt.</ab>'), # 0,1
 ('Rec.', '<ab>Rec.</ab>'), # 5,3
 ('Rhet.', '<ab>Rhet.</ab>'), # 21,22
 ('rit.', '<ab>rit.</ab>'), # 6,3
 ('Roxb.', '<ab>Roxb.</ab>'), # 5,1
 ('s. u. d.', '<ab>s. u. d.</ab>'), # 0,4
 ('Simpl.', '<ab>Simpl.</ab>'), # 74,75
 ('Ved.', '<ab>Ved.</ab>'), # 2,1
 ('überh.', '<ab>überh.</ab>'), # 548,549
 ('übertr.', '<ab>übertr.</ab>'), # 238,239
 ]
 for old,new in replacements:
  line = line.replace(old,new)
 return line

def change_1d(line):
 replacements = [
  # ('a', 'NEW'), # x,y
  # x = number of 'a' in cdsl-pw
  # y = number of <ab>a</ab> in ab-pw
  ('desgl.', '<ab>desgl.</ab>'), # 570,575
  ('<ab>Nom.</ab> Abstr.', '<ab>Nom. Abstr.</ab>'),
  ('<ab>Nom.</ab> act.', '<ab>Nom.</ab> <ab>act.</ab>'),
  ('<lex>adj.</lex> Comp.', '<ab>adj. Comp.</ab>'),
  ('<ab>Adv.</ab>', '<lex>Adv.</lex>'),
  ('<ab>adv.</ab> Comp.', '<ab>adv. Comp.</ab>'),
  ('<lex>Adj.</lex> Cmop.', '<ab>Adj. Comp.</ab>'),
  ('Bed.', '<ab>Bed.</ab>'), # 734,745
  ('Beiw.', '<ab>Beiw.</ab>'), # 465,475
  ('Bez.', '<ab>Bez.</ab>'), # 2292,2307
  ('buddh.', '<ab>buddh.</ab>'), # 747,759
  ('d.h.', '<ab>d. h.</ab>'), # 0,45
  ('d.i.', '<ab>d. i.</ab>'), # 43,365
  ('(eig.', '(<ab>eig.</ab>'),
  (' fin.', ' <ab>fin.</ab>'),
  (' bes.', ' <ab>bes.</ab>'),
  ('Gramm.', '<ab>Gramm.</ab>'),
  ('(gramm.', '(<ab>gramm.</ab>'),
  (' gramm.', ' <ab>gramm.</ab>'),
  ('(gen.', '(<ab>gen.</ab>'),
  ('impers.', '<ab>impers.</ab>'), # 312,317
  (' ders.', ' <ab>ders.</ab>'),
  ('{#Acidoha#}¦ ( {#Aciddoha#} Ind.)',
   '{#Acidoha#} ({#Aciddoha#} <ab>Ind.</ab>)¦'),
  ('intrans.', '<ab>intrans.</ab>'),
  ('(trans.', '(<ab>trans.</ab>'),
  (' trans.', ' <ab>trans.</ab>'),
  (' Pron.',' <lex>Pron.</lex>'),
  (' inter.', '<ab>inter.</ab>'),
  ('(Kalb.', '(<ab>Kalb.</ab>'),
  ('(musik.', '(<ab>musik.</ab>'),
  (' musik.', ' <ab>musik.</ab>'),
  ('<ab>N.</ab> Pr.', '<ab>N. Pr.</ab>'),
  ('<ab>Nom.</ab> Abstr.', '<ab>Nom. Abstr.</ab>'),
  ('<ab>Nom.</ab> Ag.', '<ab>Nom. Ag.</ab>'),
  ('<ab>Nom.</ab> pr.', '<ab>Nom. pr.</ab>'),
  ('<lex>Adj.</lex> ord.', '<lex>Adj.</lex> <ab>ord.</ab>'),
  ('(oxyt.', '(<ab>oxyt.</ab>'),
  (' oxyt.', ' <ab>oxyt.</ab>'),
  (' paroxyt.', ' <ab>paroxyt.</ab>'),
  ('(pass.', '(<ab>pass.</ab>'),
  (' pass.', ' <ab>pass.</ab>'),
  (' perf.', ' <ab>perf.</ab>'),
  (' pro<ab>parox.</ab>', ' <ab>proparox.</ab>'),
  ('mit präs.', 'mit <ab>Präs.</ab>'),
  ('Qual.%} Ausnahmsweise pt.', 'Qual%}. Ausnahmsweise <ab>Pt.</ab>'),
  ('¦ S.', '¦ <ab>S.</ab>'),
  ('S. {#', '<ab>S.</ab> {#'),
  ('<ab>s. u.</ab> d.', '<ab>s. u. d.</ab>'),
  ('(sc.', '(<ab>sc.</ab>'),
  (' sc.', ' <ab>sc.</ab>'),
  ('(st.', '(<ab>st.</ab>'),
  (' st.', ' <ab>st.</ab>'),
  ('Superl.', '<ab>Superl.</ab>'),
  ('z.B.', '<ab>z. B.</ab>'),
  (' z. B.', ' <ab>z. B.</ab>'),
  ('indecl.', '<lex>indecl.</lex>'),
  ('pronom.', '<lex>pronom.</lex>'),
  ('<ab>Adj.</ab>','<lex>Adj.</lex>'),
  ]
 for old,new in replacements:
  line = line.replace(old,new)
 return line
#  ('', '<ab></ab>'),

def make_changes(entries,option):
 # add 'changes' attribute to each each entry.
 # changes will be a list of Change objects.
 n = 0
 changeFcn = globals()["change_"+option]
 for entry in entries:
  changes = []
  # metaline = entry.metaline
  # lnummeta = entry.linenum1
  for iline,line in enumerate(entry.datalines):
   newline = changeFcn(line)
   if newline == line:
    # Our replacement didn't change the line. Don't generate a change
    continue
   # Our replacement DID change the line. DO generate a Change object
   change = Change(iline,newline)
   # Append change to list of changes for this entry
   changes.append(change)
  # bottome of for iline loop
  # add the 'changes' attribute to the entry
  entry.changes = changes

def write_changes(fileout,entries):
 # get total number of lines changed, for documentation
 nchange = 0 # total number of changes
 nechange = 0 # # number of entries with 1 or more changes
 for entry in entries:
  nchange = nchange + len(entry.changes)
  if len(entry.changes) != 0:
   nechange = nechange + 1
 # generate useful print statement
 print('%s  (%s changes in %s entries) ' % (fileout,nchange,nechange))
 # prepare arrays of output 'records'
 # consisting of a  title, and a record for each entry with a change
 outrecs = []  
 # title section
 outarr = []
 # initial comma means this is a 'comment' in a change file.
 outarr.append('; **********************************************************')
 outarr.append('; %s  (%s changes in %s entries) ' % (fileout,nchange,nechange))
 outarr.append('; **********************************************************')
 outrecs.append(outarr)
 # output records for each entry with a change
 for entry in entries:
  # title for this subsection of changes
  changes = entry.changes
  n = len(entry.changes)
  if n == 0:
   continue # no lines changed in this entry
  outarr = []  # lines in change file for changes in this entry.
  # subtitle for the change(s) in this entry
  outarr.append('; ----------------------------------------------------------')
  # shorten the metaline
  meta = re.sub(r'<k2>.*$','',entry.metaline)
  outarr.append('; (%s) %s' % (n,meta)) 
  outarr.append('; ----------------------------------------------------------')
  # section for each change
  for ichange,change in enumerate(changes):
   if ichange != 0:
    # a separator from previous change
    outarr.append('; ..................................')
   # now for the change
   # unpack the attributes for this change
   iline = change.iline
   newline = change.newline
   # get the line number of the line in the digitization file
   # linenum1 is the line number of the metaline in the file.
   lnum = entry.linenum1 + iline + 1
   # the old line
   oldline = entry.datalines[iline]
   # now prepare for output of the transaction
   outarr.append('%s old %s' %(lnum,oldline))
   outarr.append('%s new %s' %(lnum,newline))
  # append the lines for changes in this entry as another 'record' of output
  outrecs.append(outarr)
 # --- now we send all lines of all outrecs to our output file
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 
if __name__=="__main__":
 option = sys.argv[1] 
 filein = sys.argv[2] # (old) digitization
 fileout = sys.argv[3] # change file
 # get list of Entry records from digitization
 # For structure of an entry record,
 # see __init__ of Entry class in digentry.py
 entries = digentry.init(filein)
 # add a 'changes' attribute to each entry
 make_changes(entries,option)
 # generate output
 write_changes(fileout,entries)
 
