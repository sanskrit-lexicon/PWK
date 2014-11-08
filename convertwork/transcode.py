# coding=utf-8
""" transcode.py for PW
 Reads/Writes utf-8
 For missing
 Oct 18, 2014:  Take care of 'junk' in #{..} to preserve invertibility
  Use local copy of hk_slp1.xml and slp1_hk.xml to also transcode accents
"""
import sys, re,codecs
sys.path.insert(0,"../")  # where transcoder resides

import transcoder
#transcoder.transcoder_set_dir("../");
transcoder.transcoder_set_dir("");
def adjust_hk_slp1(m):
 x1 = m.group(1)
 x2 = m.group(2)
 x3 = m.group(3)
 partsin = re.split(u'(ƒPage.*?ƒ)|([.])',x2)
 partsout = [x1]
 for part in partsin:
  #if re.search(u'^(ƒPage.*?ƒ)$',part):
  if not part:
   continue
  elif part.startswith(u'ƒ'): #re.search(u'^(ƒPage.*?ƒ)$',part):
   partsout.append('}%s#{' % part)
  elif re.search(r'^([.])$',part):
   partsout.append('}%s#{' % part)
  else:
   partout = transcoder.transcoder_processString(part,'hk','slp1')
   partsout.append(partout)
 partsout.append(x3)
 out = ''.join(partsout)
 return out

def ellipsis_space(m):
 x = m.group(0)
 y = re.sub(u'…',' ',x)
 return y

def space_ellipsis(m):
 x = m.group(0)
 y = re.sub(' ',u'…',x)
 return y

def adjust_slp1_hk(m):
 x1 = m.group(1)
 x2 = m.group(2)
 x3 = m.group(3)
 y2 =  transcoder.transcoder_processString(x2,'slp1','hk')
 return "%s%s%s" %(x1,y2,x3)

def dbgout(fout,s):
 if fout:
  fout.write("%s\n" % s)

def hk_slp(filein,fileout):
 # slurp txt file into list of lines
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
    inlines = f.readlines()
 # open output xml file, and write header
 fout = codecs.open(fileout,'w','utf-8')
 nchg=0
 mlines = len(inlines)
 if False: # dbg
  mlines = 1000
  print "DEBUG %s lines" %mlines
 for i in xrange(0,mlines):
  line=inlines[i].rstrip('\r\n')
  # special miscoding in PW
  line=re.sub(r'#{([^}]*?)[\^]([1-9])}',r' ^\2. #{\1}',line)
  
  out = re.sub(r'(#{)(.*?)(})',adjust_hk_slp1,line)
  # convert 'key1' and 'key2' if present
  m = re.search('^<H1>(...){(.*?)}(.){(.*?)}(.*)$',out)
  if m:
   out = key_transcode(m,'hk','slp1')
  # convert … to <space> in {}
  out = re.sub(r'{.*?}',ellipsis_space,out)
  out = re.sub(u'‹.*?›',ellipsis_space,out)
  fout.write('%s\n' % out)
 fout.close()

def key_transcode(m,fromcode,tocode):
 x1 = m.group(1)
 key1=m.group(2)
 x2 = m.group(3)
 key2=m.group(4)
 body=m.group(5)
 key1a = transcoder.transcoder_processString(key1,fromcode,tocode)
 key2a = transcoder.transcoder_processString(key2,fromcode,tocode)
 out = "<H1>%s{%s}%s{%s}%s" %(x1,key1a,x2,key2a,body)
 return out

def slp_hk(filein,fileout):
 # slurp txt file into list of lines
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
    inlines = f.readlines()
 fout = codecs.open(fileout,'w','utf-8')
 nchg=0
 mlines = len(inlines)
 for i in xrange(0,mlines):
  line=inlines[i].rstrip('\r\n')
  out0 = re.sub(r'(#{)(.*?)(})',adjust_slp1_hk,line)
  out1 = re.sub(r'}[.]#{','.',out0)
  #out2 = re.sub(r'#}[.]','.#}',out1)
  #out3 = re.sub(r'#} [.]','#}.',out2)
  out2 = re.sub(u'}(ƒPage.*?ƒ)#{',r'\1',out1)
  out = re.sub(r' [\^]([1-9])[.] #{(.*?)}',r'#{\2^\1}',out2)
  if False:  # i == 564:
   print line.encode('utf-8')
   print out0.encode('utf-8')
   print out1.encode('utf-8')
   print out2.encode('utf-8')
   print out.encode('utf-8')

  # convert 'key1' and 'key2' if present
  m = re.search('^<H1>(...){(.*?)}(.){(.*?)}(.*)$',out)
  if m:
   out = key_transcode(m,'slp1','hk')
  # convert … to <space> in {}
  out = re.sub(r'{.*?}',space_ellipsis,out)
  out = re.sub(u'‹.*?›',space_ellipsis,out)
  fout.write('%s\n' % out)
 fout.close()



if __name__=="__main__":
 option = sys.argv[1]
 filein = sys.argv[2] # 
 fileout = sys.argv[3] #
 print "CHANGING ELLIPSE"
 if option == '1':
  hk_slp(filein,fileout)
 elif option == '2':
  slp_hk(filein,fileout)
 else:
  print "Bad option = ",option
  print "option must be 1 or 2"

