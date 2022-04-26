"""unixify.py  Convert all line endings to '\n'
   03-18-2017
"""
import sys,re,codecs

if __name__ == "__main__":
 filename = sys.argv[1]
 with codecs.open(filename,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 with codecs.open(filename,"w","utf-8") as f:
  for line in lines:
   f.write(line + '\n')

