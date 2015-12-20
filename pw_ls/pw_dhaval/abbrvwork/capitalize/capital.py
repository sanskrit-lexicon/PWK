#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
from lxml import etree # lxml.de
import re
import codecs
import datetime
import sys

"""
Capitalization issues in the literary resources in pw.txt
See https://github.com/sanskrit-lexicon/PWK/issues/35 for details
"""

fin = codecs.open('../../../../../Cologne_localcopy/pw/pwtxt/pw.txt','r','utf-8')
fout = codecs.open('cap0.txt','w','utf-8') 
for line in fin.readlines():
	line = line.strip()
	if re.search(u'¯[A-Z0-9]*[a-z]+[^ ]*',line):
		fout.write(line+"\n")
fout.close()

		

