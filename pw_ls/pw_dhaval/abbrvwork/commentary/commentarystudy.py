#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
#from lxml import etree # lxml.de
import re
import codecs
import datetime
import sys

"""
Usage:
python commentarystudy.python
Try to study some characteristics of commentaryrefs.txt file.

"""
def triming(lst):
	return [member.strip() for member in lst]
def trimnums(word):
	word = word.rstrip('.')
	word = word.rstrip(' ')
	word = re.sub('\(.*\)$','',word)
	word = re.sub('[.]*[0-9,.()]+$','',word)
	return word
def readrefs():
	return triming(codecs.open('commentaryrefs.txt','r','utf-8').readlines())
def writelisttofile(lst,outputfile,mode='w'):
	fout = codecs.open(outputfile,mode,'utf-8')
	for member in lst:
		fout.write(member.decode('utf-8')+'\n')
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
		m = re.search('¯([A-Za-z0-9]*)[ .]*‹zu›[ ]*¯([^ ]*)',line)
		if m:
			for member in m.groups():
				bothsides.append(trimnums(m.group(1))+'.zu.'+trimnums(m.group(2)))
		m = re.search('¯([A-Za-z0-9]*)[ .]*‹zu›[ ]*[^¯]',line)
		if m:
			for member in m.groups():
				leftside.append(trimnums(m.group(1)))
		m = re.search(' [^¯]([A-Za-z0-9]*)[ .]*‹zu›[ ]*[¯]([A-Za-z0-9,.]*)',line)
		if m:
			for member in m.groups():
				rightside.append(m.group(2))
	commleft = list(set(commleft))
	commleft = sorted(commleft)
	writelisttofile(commleft,'commleft.txt')
	bothsides = list(set(bothsides))
	bothsides = sorted(bothsides)
	writelisttofile(bothsides,'bothsides.txt')
	leftside = list(set(leftside))
	leftside = sorted(leftside)
	writelisttofile(leftside,'leftside.txt')
	rightside = list(set(rightside))
	rightside = sorted(rightside)
	writelisttofile(rightside,'rightside.txt')
	print len(commleft), 'entries with "Comm" written to the left'
	print len(bothsides), 'entries with references on both sides'
	print len(leftside), 'entries with references on left side and no reference on right side'
	print len(rightside), 'entries with no reference on left side and reference on right side'
separaterefs()
	