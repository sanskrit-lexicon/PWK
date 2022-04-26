import sys,re,codecs


if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] # 
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 with codecs.open(fileout,"w","utf-") as f:
  for i,line in enumerate(lines):
   x,w = re.split(r' +',line)
   out = '%s %s' %(i+1,w)
   f.write(out+'\n')


