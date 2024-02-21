# coding=utf-8
""" bb.py
"""
from __future__ import print_function
import sys, re,codecs
#import digentry  

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for out in lines:
   f.write(out+'\n')  
 print(len(lines),"lines written to",fileout)

def write_recs(fileout,outrecs):
 # outrecs is array of array of lines
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
   out = ''  # blank line separates recs
   f.write(out+'\n')
 print(len(outrecs),"records written to",fileout)


class BBrec:
 def __init__(self,metaline,bbdata,bbcode):
  self.metaline = metaline
  self.bbdata = bbdata
  self.bbcode = bbcode# filled in later

def get_bbregexes():
 slp1 = "aAiIuUfFxXeEoOMHkKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh|'"
 slp1a = slp1 + "^/\\\\" # accents
 #slp1b = slp1a + '°'
 regexraws = [
  ('01', r"^{#([%s]*?)#}$" % slp1a),  # 
  ('01a', r"^[*]{#([%s]*?)#}$" % slp1a),
  ('01b', r"^[*][!√]+{#([%s]*?)#}$" % slp1a),
  ('01c', r"^[!√]+{#([%s]*?)#}$" % slp1a),
  ('01d', r"^{#([%s]*?)#}[*]$" % slp1a),
  
  ('02', r"^<hom>([0-9]+)[.]</hom> {#([%s]*?)#}$" % slp1a),
  ('02a', r"^<hom>([0-9]+)[.]</hom> [*]{#([%s]*?)#}$" % slp1a),
  ('02b', r"^<hom>([0-9]+)[.]</hom> [*][!√]+{#([%s]*?)#}$" % slp1a),
  ('02c', r"^<hom>([0-9]+)[.]</hom> [!√]+{#([%s]*?)#}$" % slp1a),

  # ° at beginning or end
  ('03', r"^{#°([%s]*?)#}$" % slp1a),
  ('03a', r"^{#([%s]*?)°#}$" % slp1a),
  ('03b', r"^<hom>([0-9]+)[.]</hom> {#°([%s]*?)#}$" % slp1a),
  ('03c', r"^<hom>([0-9]+)[.]</hom> {#([%s]*?)°#}$" % slp1a),

  # in ({#X#})
  ('04', r"^\({#([%s]*?)#}\)$" % slp1a),
  ('04a', r"^<hom>([0-9]+)[.]</hom> \({#([%s]*?)#}\)$" % slp1a),
  
  #
  # multiple headwords before broken bar
  # ('10', r"^{#([%s]*?)#} und {#([%s]*?)#}$" % (slp1a,slp1a)),
  # ('10a', r"^{#([%s]*?)#}, {#([%s]*?)#}$" % (slp1a,slp1a)),
  # ('10b', r"^\({#([%s]*?)#}\) {#([%s]*?)#}$" % (slp1a,slp1a)),
  # ('10c', r"^[*]{#([%s]*?)#} und [*]{#([%s]*?)#}$" % (slp1a,slp1a)),
  
  # ('11', r"^<hom>([0-9]+)[.]</hom> {#([%s]*?)#} und {#([%s]*?)#}$" % (slp1a,slp1a)),

  ('NA', r"^.*$")  # no other match
  ]
 #regexes = [(code,re.compile(regex)) for code,regex in regexraws]
 regexes = []
 regexmap = {}  # key is bbcode
 for code,regexraw in regexraws:
  #print('%s = :%s:' %(code,regexraw))
  try:
   regex = re.compile(regexraw)
  except:
   print('regex ERROR',code)
   print(regexraw)
   exit(1)
  regexes.append((code,regex,regexraw))
  regexmap[code] = regex,regexraw
 return regexes,regexmap

bbregexes,regexmap = get_bbregexes()

def bbclassify(lines):
 bbrecs = []
 for iline,line in enumerate(lines):
  if not line.startswith('<L>'):
   # line not a metaline.
   # newlines.append(line)
   continue
  # line is metaline
  # check for consistency with next line 
  iline1 = iline + 1
  line1 = lines[iline1] 
  bbdata = re.sub(r'¦.*$','',line1)
  found = False
  bbcodes = regexmap.keys()
  for bbcode in bbcodes:
   regex,regexraw = regexmap[bbcode]
   m = re.search(regex,bbdata)
   if m != None:
    bbrec = BBrec(line,bbdata,bbcode)
    bbrecs.append(bbrec)
    found = True
    break
  if not found:
   print('bbclassify ERROR',line)
   print('::%s::' % bbdata)
   exit(1)
 return bbrecs

def write_bbrecs(dirout,bbrecs):
 bbcodes = regexmap.keys()
 for bbcode in bbcodes:
  fileout = '%s/bb_%s.txt' %(dirout,bbcode)
  outrecs = []
  for bbrec in bbrecs:
   if bbrec.bbcode != bbcode:
    continue
   outarr = []
   fields = (bbrec.metaline,bbrec.bbdata)
   out = '\t'.join(fields)
   outarr.append(out)
   outrecs.append(outarr)
  write_recs(fileout,outrecs)
  
if __name__=="__main__":
 filein = sys.argv[1]  # initial cdsl version pw.txt
 dirout = sys.argv[2]  # directory for output files
 
 lines = read_lines(filein)
 print(len(lines),"lines read from",filein)

 bbrecs = bbclassify(lines)
 write_bbrecs(dirout,bbrecs)
 
 #write_recs(fileout,outrecs)
 
