#-*- coding:utf-8 -*-
"""init_hw.py
 
"""
import sys,re,codecs
def addhw_version1(x0):
 x = re.sub(r"<p>({#[*]?[A-Za-z£_¹'º]+#})",r'<p><hw>\1</hw>',x0)
 if x != x0:
  return x
 def f2(m):
  # r'<p>\1<hw>\2</hw>'
  hom = re.sub(r'([0-9.]+)',r'<hom>\1</hom>',m.group(1))
  hw = "<hw>%s</hw>" % m.group(2)
  ans = "<p>%s%s" %(hom,hw)
  return ans
 x = re.sub(r"<p>([0-9. ]+)({#[*]?[A-Za-z£_¹'º]+#})",f2,x0)
 if x != x0:
  return x
 x = re.sub(r'<p>({#[^#]+#})',r'<p><hw1>\1</hw1>',x0)
 if x != x0:
  return x
 def f4(m):
  # r'<p>\1<hw>\2</hw>'
  hom = re.sub(r'([0-9.]+)',r'<hom>\1</hom>',m.group(1))
  hw = "<hw1>%s</hw1>" % m.group(2)
  ans = "<p>%s%s" %(hom,hw)
  return ans
 x = re.sub(r'<p>([0-9. ]+)({#[^#]+#})',f4,x0)
 if x != x0:
  return x
 x = x.replace('<p>({#ahnavAyya£#})','<p>(<hw>{#ahnavAyya£#}</hw>)')
 if x != x0:
  return x
 x = x.replace('<p>3. und 4. {#vyay#}','<p><hom>3.</hom> und <hom>4.</hom> <hw>{#vyay#}</hw>')
 if x != x0:
  return x
 return x0

def addhw(x0):
 x = re.sub(r"<p>([0-9. ]*{#[*]?[A-Za-z£_¹'º]+#})",r'<p><hw>\1</hw>',x0)
 if x != x0:
  return x
 x = re.sub(r'<p>([0-9. ]*{#[^#]+#})',r'<p><hw>\1</hw>',x0)
 if x != x0:
  return x
 if x != x0:
  return x
 # two special cases
 x = x.replace('<p>({#ahnavAyya£#})','<p><hw>({#ahnavAyya£#})</hw>')
 if x != x0:
  return x
 #x = x.replace('<p>3. und 4. {#vyay#}','<p><hom>3.</hom> und <hom>4.</hom> <hw>{#vyay#}</hw>')
 x = re.sub('<p>(3. und 4. {#vyay#})',r'<p><hw>\1</hw>',x0)
 if x != x0:
  return x
 return x0

def addhw1(x):
 def f(m):
  a = m.group(1)
  b = m.group(2)
  c = m.group(3)
  ans = '<hw>%s%s%s</hw>' %(a,b,c)
  return ans
 y = re.sub(r'<hw>(.*?)</hw>(,? ²?und ²?)({#[^#]*#})',f,x)
 z = re.sub(r'<hw>(.*?)</hw>(,? ²?u[.] ²?)({#[^#]*#})',f,y)
 return z

def hwmarkup(lines):
 newlines = []
 page = None
 nprob = 0
 for iline,line in enumerate(lines):
  m = re.search(r'\[Page(.*?)\]',line)
  if m != None:
   newpage = m.group(1)
  if line.startswith('<H>'):
   newlines.append(line)
   page = newpage  # so page in first <H> is used.
   continue
  assert line.startswith('<p>')
  newline = addhw(line)
  newline = addhw1(newline)
  if newline == line:
   nprob = nprob + 1
  newline = newline.replace('<p>','<p n="%05d" pc="%s">'%(iline+1,page))
  newlines.append(newline)
  page = newpage
 print(nprob,"lines no <hw> markup")
 return newlines

def analyze(lines):
 regexes = [
  '</hw> [0-9]+[.]',
  '</hw> [IV]+[.]',
  '</hw>,? <ls>',
  '</hw>,? [*]?[mfn][.]',
    '</hw> (Adj|Adv|)[.]',
  '</hw> [0-9]+[)]',
  '</hw>,? {%',
  '</hw>[.,;]? (mit|auch|nach|oder|als|lies) ',
  '</hw>,? (Nom|Gen|Absol|Loc|Dat|Acc)[.]',
  '</hw>,? [(]',
  '</hw>,? (Pl|Sg|Du|Perf|Abl|Comm|Bez)[.]',
  '</hw>[.,;]? [*]?(Partic|vgl|Z|Nachtr|N|S|Caus|s|Desid|Instr)[.]',
  '</hw>,? (so|wohl|ist|nicht|in|am|vor) ',
  '</hw>,? (im|eher|füge|streiche|zu|das) ',
  '</hw>,? (etwa|Titel|genauer) ',
  '</hw>,? (soll|v[.] l[.]|angeblich|wegen|=|für|über) ',
  '</hw>,? (die|führt|der|st[.]|ebend[.]|steht) ',
  '</hw>[,;]? (Compar[.]|vgl[.]|Accent|dass[.]|auf) ',
  '</hw>[.,;]? (Nomin[.]|Intens[.]|Pass[.]|Denomin[.]|Interj[.]|Infin[.]) ',
  '</hw>[.,;]? (oben|häufige|scheinbar|metrisch) ',
  '</hw>[.,;]? (von|bedeutet|wird|bei|Cit[.]|wann|fehlerhaft|besser) ',
  '</hw>[.,;]? (vielleicht|richtig|Partikel|Anderes|anders) ',
  '</hw>[.,;]? (Partikel,|Voc[.]|an|wohlauch|Beiw[.]|wiederholt|bisweilen) ',
  '</hw>[.,;]? (Med[.]|statt|könnte|kann|fgg[.]|scheint|eine) ',
  '</hw>[.,;]? ({[|]|\[Page|adj[.] |Name |richtig[.] |liesse |gedr[.] )',
  '</hw>[.,;]? ([?] <ls>|werden |sind \[0-9]+[)] |u[.] s[.] w[.] )',
  '</hw>[.,;]? (definirt |und am |{#jAgAra#}|²[fn][.] |sind |17, 4 |andere |onomatop[.])',
  '</hw>[.,;]? (umzu-²stellen|3, lies |3, 4. \[Page7|5 fehlerhaft |5 zu streichen)',
  '</hw>[.,;]? (²\(vgl.|81, 1. 5|²<ls>|1 \(steht|[*]Mit |schlechte |stehen )',
  '</hw>[.,;]? (um-²zustellen|[*]zu |nur )',
  '</hw>[.,;]? (5 unter|²IV|IV, |häufig |u\. {%Aushauch%}|viel-²leicht)',
  '</hw>[.,;]? ([?] ebend.|1ste |2\) zu )',
  '</hw>[.,;]? (²I|umzustellen)',
  '</hw>[.]? $',
  ]
 d = {}
 for regex in regexes:
  d[regex] = 0
 neclines = []
 for line in lines:
  if line.startswith('<H>'):
   continue
  found = False
  for regex in regexes:
   if re.search(regex,line):
    found = True
    d[regex] = d[regex]+ 1
    break
  if not found:
   neclines.append(line)
 for regex in regexes:
  print('%4d "%s"' %(d[regex],regex))
 return neclines

def write(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
   for line in lines:
    f.write(line+'\n')
 print(len(lines),"written to",fileout)

if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] # characters in {#X#}
 fileout1 = sys.argv[3]
 
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 newlines = hwmarkup(lines) # 
 write(fileout,newlines)
 #
 neclines = analyze(newlines)
 write(fileout1,neclines)
 
