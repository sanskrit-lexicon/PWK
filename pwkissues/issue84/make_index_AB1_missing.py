# coding=utf-8
""" make_index_AB1_missing.py
"""
from __future__ import print_function
import sys, re, codecs
import json

def roman_to_int(roman):
 droman_int = {'I':1, 'II':2, 'III':3, 'IV':4,
                'V':5, 'VI':6, 'VII':7, 'VIII':8, 'IX':9,
                'X':10, 'XI':11, 'XII':12,'':0}
 if roman in droman_int:
  return droman_int[roman]
 else:
  # error condition
  return None
 
# global parameters
parm_regex_split = '\t' #    r'[ ]+'
parm_numcols = [8] # (7,8)  assume always a remark, which may be empty
parm_numparm = 3  
parm_vol = r'^(1|2|3|4|5|6)$'
parm_page = r'^([0-9]+)([xyz])?$'
parm_parvan = r'^([0-9]+)$'
parm_adhy = r'^([0-9]+)([A])?$'
parm_fromv = r'^([0-9]+)([abcd])?$'
parm_tov = r'^([0-9]+)([abcd])?$'
parm_ipage = r'^([0-9]+)+([ab])?$'   # not used
parm_vpstr_format = '%s%s'  # ???

class Pagerec(object):
 """
Format of malavikagni
vol, page, parvan. adhy, fromv, tov ipage
""" 
 def __init__(self,line,iline,filevol=None):
  line = line.rstrip('\r\n')
  self.line = line
  self.iline = iline
  parts = re.split(parm_regex_split,line)
  self.status = True  # assume all is well
  self.status_message = 'All is ok'
  if len(parts) not in parm_numcols:
   self.status = False
   self.message = 'Expected %s values. Found %s value' %(parm_numcols,len(parts))
   return
  # give names to the column values
  raw_vol = parts[0]
  raw_page = parts[1] # internal to volume. digits
  raw_parvan = parts[2]
  raw_adhy = parts[3]
  raw_fromv = parts[4]
  raw_tov = parts[5]
  raw_ipage = parts[6]
  raw_comment = parts[7]

  self.raw_vol = raw_vol
  self.raw_page = raw_page
  self.raw_parvan = raw_parvan
  self.raw_adhy = raw_adhy
  self.raw_fromv = raw_fromv
  self.raw_tov = raw_tov
  self.raw_ipage = raw_ipage
  self.raw_comment = raw_comment

  # check vol
  m_vol = re.search(parm_vol,raw_vol)
  if m_vol == None:
   self.status = False
   self.status_message = 'Unexpected vol: %s' % raw_vol
   return
  # check page 
  m_page = re.search(parm_page,raw_page)
  if m_page == None:
   self.status = False
   self.status_message = 'Unexpected page: %s' % raw_page
   return
  m_parvan = re.search(parm_parvan,raw_parvan)
  if m_parvan == None:
   self.status = False
   self.status_message = 'Unexpected parvan: %s' % raw_parvan
   return
  m_adhy = re.search(parm_adhy,raw_adhy)
  if m_adhy == None:
   self.status = False
   self.status_message = 'Unexpected adhy: %s' % raw_adhy
   return
  # check fromv 
  m_fromv = re.search(parm_fromv,raw_fromv)
  if m_fromv == None:
   self.status = False
   self.status_message = 'Unexpected fromv: %s' % raw_fromv
   return
  # check tov 
  m_tov = re.search(parm_tov,raw_tov)
  if m_tov == None:
   self.status = False
   self.status_message = 'Unexpected tov: %s' % raw_tov
   return
  # check ipage
  m_ipage = re.search(parm_ipage,raw_ipage)
  if m_ipage == None:
   self.status = False
   self.status_message = 'Unexpected ipage: %s' % raw_ipage
   return

  # set self.vol as integer
  self.vol = int(raw_vol)
  # set self.page as string
  self.page = m_page.group(1)  # digits
  self.pagex = m_page.group(2) # x,y,z or empty string
  self.parvan = int(raw_parvan)
  #self.adhy = raw_adhy
  self.adhy = int(m_adhy.group(1))
  # set self.fromv as integer
  self.fromv = int(m_fromv.group(1))
  x1 =  m_fromv.group(2)
  if x1 == None:
   self.fromvx = ''
  else:
   self.fromvx = x1;
  # set self.tov as integer
  self.tov = int(m_tov.group(1))
  x2 =  m_tov.group(2)
  if x2 == None:
   self.tovx = ''
  else:
   self.tovx = x2;
  # set self.ipage as 
  self.ipage = raw_ipage
  # vpstr  # format consistent with format of filename of scanned page
  # VNNNNx
  if self.pagex == None:
   pagex = ''
  else:
   pagex = self.pagex
  self.vpstr = '%d%04d%s' %(self.vol, int(self.page), pagex)
  self.newpage = None
 
 def newline(self):
  newpage = self.newpage
  oldpage = self.page
  vol = self.vol
  comment = self.raw_comment
  if (newpage == oldpage):
   newcomment = comment
  else:
   base,fraction = newpage.split('.')
   assert len(base) <= 3
   assert vol != 5  # which takes 4 positions: mbhbomb5-NNNN.pdf
   ibase = int(base)
   newfile = 'mbhbomb%s-%03d.%s.pdf' %(vol,ibase,fraction)
   newcomment = newfile
  newparts = [
   self.raw_vol,
   newpage,
   self.raw_parvan,
   self.raw_adhy,
   self.raw_fromv,
   self.raw_tov,
   self.raw_ipage,
   newcomment,
  ]
  newline = '\t'.join(newparts)
  return newline
 
def init_pagerecs(filein,filevol=None):
 """ filein is a csv file, with first line as fieldnames
 """
 recs = []
 with codecs.open(filein,"r","utf-8") as f:
  for iline,line in enumerate(f):
   if (iline == 0):
    # assert line.startswith('volume') # skip column-title line
    print('Skipping column title line:',line)
    continue
   pagerec = Pagerec(line,iline,filevol=None)
   if pagerec.status:
    # No problems noted
    recs.append(pagerec)
   else:
    lnum = iline + 1
    print('Problem at line # %s:' % lnum)
    print('line=',line)
    print('message=',pagerec.status_message)
    exit(1)
 print(len(recs),'Success: Page records read from',filein)
 return recs

def write_recs(fileout,recs):
 with codecs.open(fileout,"w","utf-8") as f:
  for rec in recs:
   out = rec.newline()
   f.write(out + '\n')
 print(len(recs),'revised lines written to',fileout)

def compute_newpage(page0,page):
 m = re.search(r'^([0-9]+)([xyz])',page)
 if m == None:
  print('compute_newpage: ERROR. page=',page,'page0=',page0)
  exit(1)
 pagebase = m.group(1)
 m0 = re.search(r'^([0-9]+)$',page0)
 if m0 != None:
  # page0 has no suffix.
  isfx = 1
  newpage = '%s.%s' %(pagebase,isfx)
  return newpage
 # page0 has suffix. it should be '.N' where N is a digit 1-8
 m0 = re.search(r'^([0-9]+)[.]([1-8])$',page0)
 if m0 == None:
  print('compute_newpage: ERROR. page0 = ',page0)
  exit(1)
 pagebase0 = m0.group(1)
 assert pagebase == pagebase0
 pagesfx0 = m0.group(2) # the digit N
 isfx0 = int(pagesfx0)
 isfx = isfx0 + 1  # increment suffix
 newpage = '%s.%s' %(pagebase,isfx)
 return newpage
  
def edit_pagerecs(recs): 
 for irec,rec in enumerate(recs):
  vol = rec.raw_vol
  page = rec.raw_page
  pagex = rec.pagex
  #if irec == 0:
  # print('vol=%s, page=%s, pagex=%s' %(vol,page,pagex))
  if pagex == None:
   rec.newpage = page
  else:
   rec0 = recs[irec - 1]
   page0 = rec0.newpage
   newpage = compute_newpage(page0,page)
   rec.newpage = newpage
   
if __name__ == "__main__":
 filein=sys.argv[1]  # tab-delimited index file
 fileout = sys.argv[2]
 filevol = None
 pagerecs = init_pagerecs(filein,filevol=None)
 edit_pagerecs(pagerecs)
 write_recs(fileout,pagerecs)

