# coding=utf-8
"""test5.py  see readme.txt for usage
   
"""
from __future__ import print_function
import sys,re,codecs

def search_pattern_in_line(pattern,line):
 # searchs for pattern in line and
 # returns array of strings describing the experiment
 outarr = []  # lines to be output somewhere
 outarr.append('LINE |%s|' % line)  # the line we are examining
 outarr.append('PATTERN |%s|' % pattern)
 # search the string for the first instance of the pattern, if any.
 try:
  m = re.search(pattern,line)
 except:
  outarr.append('Sorry,  something wrong with PATTERN')
  return outarr
 # m is either the special value None, or a Match object
 if m == None:
  # the pattern was not found in the line
  outarr.append('PATTERN not found in LINE')
  return outarr
 # In this case, print various info available in the Match object 'm'
 outarr.append('m.group(0) |%s|' %m.group(0))
 lastindex = m.lastindex
 if lastindex == None:
  outarr.append('PATTERN has no match groups')
  return outarr
 # note all the match groups
 outarr.append('PATTERN has %s match groups' % lastindex)
 for igroup in range(1,lastindex+1):
  outarr.append('m.group(%s) |%s|' %(igroup,m.group(igroup)))
 return outarr

if __name__=="__main__":
 if len(sys.argv) != 3:
  print('Program for learning about regular expression patterns')
  print(' and match groups  (Match object in python)')
  print(' match groups are formed by (...) in PATTERN')
  print('USAGE: python test5.py "PATTERN" "LINE"')
  print(' PATTERN is regex pattern to search for in the text string LINE')
  print(' Please, no " character in PATTERN or LINE')
  exit(0)
 pattern = sys.argv[1]
 line = sys.argv[2]
 outarr = search_pattern_in_line(pattern,line)
 for out in outarr:
  print(out)
 

 
