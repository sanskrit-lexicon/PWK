""" fuzzymatch1.py
  Jan 4, 2016
  Fuzzy match of two sets of PW abbreviations:
   - crefminusbib.txt
   - pwbib_abbrv_all.txt
 
"""
import re
import sys,codecs
import levenshtein



def suggest_v3(w,sanhws,m=2,skipexact=True,matchFirst=False):
    # w is a string
    # sanhws is assumed to be an iterable, whose elements
    # are objects with attributes
    #  - key
    #  - len
    # modified to screen further by length of word
    # if matchFirst is True,
    #   Assume first letter of 'w' is correct.
    #   For efficiency, consider only sanhws that start with same letter
    # Do not return exact match 
    if matchFirst:
     w0 = w[0]
     hws=[x for x in sanhws if x.key[0] == w0]
    else:
     hws=sanhws
    # Feb 3, 2015
    lw = len(w)
    hws = [x for x in hws if (abs(x.len - lw) < m)] #? < m or > m ?
    #print "%s headwords start with %s" %(len(hws),w0)
    nearlist=[] # list of hws whose levenshtein distance from w is <= 
    low = 99
    for hw in hws:
        if (w == hw.key) and skipexact:
            continue
        d=levenshtein.levenshtein1(w,hw.key,m)
        if d == -1:
            continue
        nearlist.append((d,hw))
        if (d < low): # update low distance
            low = d
    # include ones only = low
    ans = [x[1] for x in nearlist if x[0] == low]
    
    #s = sorted(nearlist,key=lambda(x):x[0]) # sort by d
    return ans


class Abbrv(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.abbrv = line.strip() # remove whitespace, if any
  self.key = self.abbrv
  self.len = len(self.key)

class Result(object):
 def __init__(self,prob,suggestions):
  self.prob = prob  # an Abbrv object
  self.suggestions = suggestions # array of Abbrv objects

def main():
 filein1 = sys.argv[1] # crefminusbib
 filein2 = sys.argv[2] # pwbib_abbrv_all
 fileout1 = sys.argv[3] # likely.txt
 fileout2 = sys.argv[4] # maybe.txt
 fileout3 = sys.argv[5] # nomatch.txt
 with codecs.open(filein1,"r","utf-8") as f:
  aprobs = [Abbrv(x) for x in f]
 with codecs.open(filein2,"r","utf-8") as f:
  agivens = [Abbrv(x) for x in f]
 
 maxdiff = 2 # could read in
 naprob=0
 results=[]
 for aprob in aprobs:
  aprobkey = aprob.key
  suggestions = suggest_v3(aprobkey,agivens,m=maxdiff,skipexact=False)
  results.append(Result(aprob,suggestions))
  naprob = naprob+1
  if naprob==100000:  #very big, so all will be processed
   print "debug break after",naprob
   break
 fout1 = codecs.open(fileout1,'w','utf-8')
 fout2 = codecs.open(fileout2,'w','utf-8')
 fout3 = codecs.open(fileout3,'w','utf-8')
 n1 = 0
 n2 = 0
 n3 = 0
 for result in results:
  if len(result.suggestions) == 0:
   fout3.write("%s\n" % result.prob.key)
   n3 = n3 + 1
   continue
  # some suggestions
  prob = result.prob
  suggestions = result.suggestions
  key = prob.key
  suggestkeys = [s.key for s in suggestions] # list of string
  if key in suggestkeys: 
   # an exact match is NOT expected
   print "Unexpected Exact Match:",key
   continue
  suggest = ' ; '.join(suggestkeys)
  if (len(suggestions) == 1) and (len(key)>3):
   #unique suggestion, and the key is not too short
   fout1.write('%s:%s\n' % (key,suggest))
   n1 = n1 + 1
  else:
   fout2.write('%s:%s\n' % (key,suggest))
   n2 = n2 + 1
 fout1.close()
 fout2.close()
 fout3.close()
 print n1,"records to",fileout1
 print n2,"records to",fileout2
 print n3,"records to",fileout3

if __name__=="__main__":
 main()
