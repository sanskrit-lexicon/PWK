from lxml import etree # lxml.de
import codecs

def parse1(xmlfile):
 f = codecs.open(xmlfile,"r","utf-8")
 n=0
 for line in f:
  n=n+1
  if not line.startswith('<H1>'):
   continue
  try:
   root = etree.fromstring(line)
  except:
   print "ERROR at line ",n
 f.close()
 print "done parse1"   

xmlfile = '../pw.xml'
parse1(xmlfile)
#entries = etree.parse(xmlfile)

