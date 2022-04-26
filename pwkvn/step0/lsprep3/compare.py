""" compare.py

"""
import codecs,sys,re
import transcoder
transcoder.transcoder_set_dir('.')

class Pwls:
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.count,self.lsiast,self.tooltip = line.split('\t')
  self.ls = transcoder.transcoder_processString(self.lsiast,'roman','as')
  self.used = None
  
def init_pwls(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  recs = [Pwls(line) for line in f]
 # drop first three records
 print(len(recs),"Pwls records read from",filein)
 print("  skipping %s, %s, %s" %(recs[0].ls,recs[1].ls, recs[2].ls))
 recs = recs[3:]
 return recs

class Vnls:
 def __init__(self,line):
  line = line.rstrip('\r\n')
  m = re.search(r'^([0-9]+) (.*)$',line)
  self.count = m.group(1)
  self.lsiast = m.group(2)
  self.ls = transcoder.transcoder_processString(self.lsiast,'roman','as')
  self.used = None
  
def init_vnls(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  recs = [Vnls(line) for line in f]
 print(len(recs),"Vnls records read from",filein)
 return recs

def find_ls(pwrecs,ls):
 for pwrec in pwrecs:
  if ls == pwrec.ls:
   return pwrec
 return None

def  compare(vnrecs,pwrecs):
 for vnrec in vnrecs:
  pwrec = find_ls(pwrecs,vnrec.ls)
  if pwrec != None:
   vnrec.used = pwrec
   pwrec.used = vnrec

def write_comp(fileout,vnrecs):
 nok = 0
 nprob = 0
 with codecs.open(fileout,"w","utf-8") as f:
  for vnrec in vnrecs:
   pwrec = vnrec.used
   if pwrec == None:
    count = '00000'
    title = 'NONE'
    nprob = nprob + 1
   else:
    title = pwrec.tooltip
    count = pwrec.count
    nok = nok + 1
   out = '%s\t%s\t%s\t%s' %(vnrec.count,vnrec.ls,count,title)
   f.write(out+'\n')
 print('%s matches found, %s unmatched' %(nok,nprob))
 print('%s records written to %s' %(nok+nprob,fileout))

def write_unused(fileout,pwrecs):
 # sort using as-coded ls
 for rec in pwrecs:
  rec.ls_sort = re.sub(r'[0-9]+','',rec.ls)
 
 pwrecs1 = sorted(pwrecs,key = lambda rec: rec.ls_sort)
 nprob = 0
 with codecs.open(fileout,"w","utf-8") as f:
  for pwrec in pwrecs1:
   if pwrec.used != None:
    continue
   out = '%s\t%s\t%s' % (pwrec.count,pwrec.ls,pwrec.tooltip)
   nprob = nprob + 1
   f.write(out+'\n')
 print('%s unmatched pwbib records written to %s' %(nprob,fileout))
       
if __name__ == "__main__":
 filein1 = sys.argv[1] # vnls4
 filein2 = sys.argv[2] # pwls
 fileout1 = sys.argv[3] #ls matched to pwbib
 fileout2 = sys.argv[4] # pwbib not used
          
 vnrecs = init_vnls(filein1)
 pwrecs = init_pwls(filein2)

 compare(vnrecs,pwrecs)
 write_comp(fileout1,vnrecs)
 write_unused(fileout2,pwrecs)
 
