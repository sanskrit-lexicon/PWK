""" transcode.py

"""
import codecs,sys,re
sys.path.append('../lsprep3')
import transcoder
transcoder.transcoder_set_dir('../slp')

def transcode(line,tranin,tranout):
 def f(m):
  x = m.group(1)
  parts = re.split(r'(\[Page.*?\])',x)
  newparts = []
  for part in parts:
   if part.startswith('[Page'):
    newpart = part
   else:
    newpart = transcoder.transcoder_processString(part,tranin,tranout)
   newparts.append(newpart)
  y = ''.join(newparts)
  return '{#%s#}' % y
 newline = re.sub(r'{#(.*?)#}',f,line)
 return newline

if __name__ == "__main__":
 tranin,tranout = sys.argv[1].split(',')
 filein = sys.argv[2]
 fileout = sys.argv[3]

 f = codecs.open(filein,"r","utf-8")
 fout = codecs.open(fileout,"w","utf-8")
 n = 0
 for line in f:
  n = n + 1
  lineout = transcode(line,tranin,tranout)
  fout.write(lineout)
 f.close()
 fout.close()
 print(n,"lines from",filein,"converted from %s to %s" %(tranin,tranout))
 print(n,"lines written to",fileout)


