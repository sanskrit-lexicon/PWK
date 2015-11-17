""" pwbib1.py
    Usage: python pwbib1.py pwbib0.txt pwbib1.txt
    Reads pwbib0 (using pwbib_parse0) into list of Pwbib records.
    converts 'abbrv' and 'title' fields to 'Roman' (using transcoder with
    as_roman.xml).  Saves Unicode abbrv field as a separate 
      field 'abbrvunicode'.
    Replaces title field with unicode.
    Writes all fields to output, as tab-delimited text file. (See writerecs for
    details of fields written)
    Starts with as_roman.xml as per pw_dhaval
"""
import codecs,sys,re
import pwbib_parse0
import transcoder
transcoder.transcoder_set_dir('.');

def convertrecs(recs,tranin,tranout):
 "Modifies recs"
 n=0
 for rec in recs:
  n=n+1
  try:
   rec.abbrvunicode = transcoder.transcoder_processString(rec.abbrv,tranin,tranout)
   rec.titleunicode = transcoder.transcoder_processString(rec.title,tranin,tranout)
  except:
   print "convertrecs problem",n,rec.line.encode('utf-8')
   #exit(1)

def writerecs(recs,fileout):
 fout = codecs.open(fileout,"w","utf-8")
 n=0
 for rec in recs:
  n = n + 1
  outarr=[]  # array of fields to write.
  outarr.append(rec.abbrv)
  outarr.append('%03d' % n) # sequence number in pwbib0
  if rec.checked:
   outarr.append('+') # code for marked as 'checked' in pwbib0
  else:
   outarr.append('-') # code for marked as 'unchecked' in pwbib0
  outarr.append(rec.type) # == (standard) or xx (non-standard)
  outarr.append(rec.volume) # text volume (1-6)
  outarr.append(rec.abbrvunicode) # unicode form of abbreviation
  outarr.append(rec.titleunicode) # unicode form of title
  # join fields with '\t'
  out = '\t'.join(outarr)
  fout.write('%s\n' % out)
 fout.close()

if __name__ == "__main__":
 filein = sys.argv[1]
 recs = pwbib_parse0.parse(filein)
 print len(recs),"parsed from",filein
 #rec = recs[0]
 #print "dbg:",rec.line,rec.checked,rec.abbrv
 #exit(1)
 fileout = sys.argv[2]
 tranin = 'as'
 tranout = 'roman'
 convertrecs(recs,tranin,tranout)
 writerecs(recs,fileout)


