#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
from lxml import etree # lxml.de
import re
import codecs
import datetime
import sys

"""
python stdabbrv.py abbrvfile creffile outputfile
e.g.
python stdabbrv.py ../../pwbib/crefminusbib.txt abbrvoutput/sortedcrefs.txt ../../pwbib/diffstudy/correctionsubmission/cmbsub.txt

crefminusbib.txt has data like 'AGN'
sortedcrefs.txt has data like `AGN@SAlagrAma@SAlagrAma@111783@1`
We have to combine these two and get data in standard format.
Expected output is `¯AGN@SAlagrAma@SAlagrAma@111783:¯AGN:n:`
For standard format - see https://github.com/sanskrit-lexicon/CORRECTIONS/issues/146#issuecomment-163463468

"""
def getcref(inputword,creflist):
	for cref in creflist:
		if cref.startswith(inputword+'@'):
			return cref
			break
def addmacron(line):
	line = line.strip()
	line = line.encode('utf-8')
	base = line.split('@')[0]
	line = line.replace(base,'¯'+base)
	return line
	
	
if __name__=="__main__":
	abbrvfile = sys.argv[1]
	creffile = sys.argv[2]
	abbrvlist = codecs.open(abbrvfile,'r','utf-8').read().split()
	creflist = codecs.open(creffile,'r','utf-8').read().split()
	output = []
	for abbrv in abbrvlist:
		cref = getcref(abbrv,creflist)
		[ls,k1,k2,lnum,count] = cref.split('@')
		output.append((ls,k1,k2,lnum,count))
	output = sorted(output, key=lambda x:x[4], reverse=True)
	for (ls,k1,k2,lnum,count) in output:
		#print '¯'.encode('utf-8')
		line = ls+'@'+k1+'@'+k2+'@'+lnum+':'+ls+':n:'
		line = addmacron(line)
		print line
	