#-*- coding:utf-8 -*-
"""bot_freq_gs.py
"""
import sys,re,codecs
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec cannot encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for line in lines:
   f.write(line+'\n')  
 print(len(lines),"written to",fileout)

def update_lines(lines,gsd,gd,sd):
 options = ('gs','g','s')
 dicts = (gsd,gd,sd)
 newlines = []
 for line in lines:
  m = re.search(r'^<bot>(.*?)</bot> ([0-9]+)$',line)
  bot = m.group(1)
  nbot = m.group(2)
  botwords = bot.split(' ')
  g,s = (botwords[0],botwords[1])
  counts = [] 
  for ikey,key in enumerate([(g,s),g,s]):
   d = dicts[ikey]
   if key in d:
    n = d[key]
   else:
    n = 0
   counts.append('%s=%s' %(options[ikey],n))
  extra = ','.join(counts)
  newline = '%s %s' %(line,extra)
  newlines.append(newline)
 return newlines

def init_gsdict(lines,option):
 d = {} 
 n = 0
 for iline,line in enumerate(lines):
  line = line.rstrip('\r\n')
  # update d
  g,s,num = line.split(',')
  if option == 'gs':
   key = (g,s)
  elif option == 'g':
   key = g
  elif option == 's':
   key = s
  else:
   print('init_gsdict_error: unknown option',option)
   exit(1)
  if key not in d:
   d[key] = 0
   n = n + 1
  d[key] = d[key] + int(num)
 print(n,"distinct %s keys"%option)
 return d

if __name__=="__main__":
 filein = sys.argv[1] #  bot_freq_pw_2.txt
 filein1 = sys.argv[2] # wcvp_gs.txt
 fileout = sys.argv[3] # revised xxx.txt
 lines = read_lines(filein)
 print(len(lines),"lines read from",filein)
 lines1 = read_lines(filein1)
 print(len(lines1),"lines read from",filein1)
 
 gsd = init_gsdict(lines1,'gs')
 gd = init_gsdict(lines1,'g')
 sd = init_gsdict(lines1,'s')
 newlines = update_lines(lines,gsd,gd,sd)
 write_lines(fileout,newlines)

 
