import sys,re,codecs


if __name__=="__main__":
 filein1 = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 filein2 = sys.argv[2]
 fileout = sys.argv[3] # 
 with codecs.open(filein1,"r","utf-8") as f:
  lines1 = [x.rstrip('\r\n') for x in f]
 with codecs.open(filein2,"r","utf-8") as f:
  lines2 = [x.rstrip('\r\n') for x in f]
 n1 = len(lines1)
 assert n1 == len(lines2)
 with codecs.open(fileout,"w","utf-") as f:
  for i in range(n1):
   m1 = re.search(r'^([0-9]+) (.*)$',lines1[i])
   seq1,german = m1.group(1),m1.group(2)
   m2 = re.search(r'^([0-9]+) (.*)$',lines2[i])
   try:
    seq2,english = m2.group(1),m2.group(2)
   except:
    print('problem line %s: %s' %(i+1,lines2[i]))
    exit(1)
   assert seq1 == seq2
   outarr = [seq1,german,english]
   out = '%s %s %s' %(seq1,german,english)
   f.write(out+'\n')


