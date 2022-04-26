""" as_roman.py

"""
import codecs,sys,re
import transcoder
transcoder.transcoder_set_dir('.')

if __name__ == "__main__":
 tranin,tranout = sys.argv[1].split(',')
 filein = sys.argv[2]
 fileout = sys.argv[3]

 f = codecs.open(filein,"r","utf-8")
 fout = codecs.open(fileout,"w","utf-8")
 n = 0
 for line in f:
  n = n + 1
  lineout = transcoder.transcoder_processString(line,tranin,tranout)
  fout.write(lineout)
 f.close()
 fout.close()
 print(n,"lines from",filein,"converted from %s to %s" %(tranin,tranout))
 print(n,"lines written to",fileout)


