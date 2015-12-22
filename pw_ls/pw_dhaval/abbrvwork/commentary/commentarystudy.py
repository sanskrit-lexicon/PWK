#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
#from lxml import etree # lxml.de
import re
import codecs
import datetime
import sys

"""
commentarystudy.python
Try to study some characteristics of commentaryrefs.txt file.

"""
def triming(lst):
	return [member.strip() for member in lst]
def trimnums(word):
	word = word.rstrip('.')
	word = re.sub('[.][0-9,.]+$','',word)
	return word
def readrefs():
	return triming(codecs.open('commentaryrefs.txt','r','utf-8').readlines())
def writelisttofile(lst,outputfile,mode='w'):
	fout = codecs.open(outputfile,mode,'utf-8')
	for member in lst:
		member = unicode(member)
		fout.write(member+'\n')
	fout.close()
def separaterefs():
	commleft = []
	bothsides = []
	leftside = []
	rightside = []
	lines = readrefs()
	for line in lines:
		line = line.encode('utf-8')
		m = re.search('•Comm. ‹zu› ¯([A-Za-z0-9.,]*)',line)
		if m:
			for member in m.groups():
				commleft.append(trimnums(member))
	commleft = list(set(commleft))
	commleft = sorted(commleft)
	writelisttofile(commleft,'commleft.txt')
	print len(commleft)
separaterefs()
	