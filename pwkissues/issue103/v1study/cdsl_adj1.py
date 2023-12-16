# coding=utf-8
""" cdsl_adj1.py
"""
from __future__ import print_function
import sys, re,codecs
#import digentry  

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def meta_iline(lines):
 d = {}
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   if line in d:
    print('meta error duplicate',line)
   d[line] = iline
 return d

def update_line(line):
 # changes made by make_xml.py
 line = line.replace('<hw>','')
 line = line.replace('</hw>','¦')
 line = line.replace('-<lb/>','')
 line = line.replace('<lb/>','')
 # additional changes
 line = line.replace('<ab>m.</ab>','<lex>m.</lex>')
 line = line.replace('<ab>f.</ab>','<lex>f.</lex>')
 line = line.replace('<ab>n.</ab>','<lex>n.</lex>')
 line = line.replace('<ab>Adj.</ab>','<lex>Adj.</lex>')
 line = line.replace('<ab>Adv.</ab>','<lex>Adv.</lex>')
 #
 line = re.sub(r', ([0-9])', r',\1', line)
 line = re.sub(r'([0-9])[.]</ls>', r'\1</ls>.', line)
 line = re.sub(r' +$','',line)
 line = re.sub(r'\(Nachtr. ([0-9]+)[)〉]',  r'(<ls>Nachtr. \1</ls>)',line)
 #
 line = line.replace('.%}','%}.')
 line = line.replace('%},', ',%}')
 line = line.replace('--','—')
 line = re.sub(r'([0-9])\)',r'\1〉',line)
 line = re.sub(r'{%(.)%}', r'\1〉',line)
 line = line.replace('〉)',  '〉')  # correct some error above?
 line = line.replace(r"'s</is>", "</is>ʼs")
 #
 line = line.replace('#}¦, {#', '#}, {#')
 line = line.replace('#}¦ und',  '#} und')
 line = line.replace('¦ u. ',  ' <ab n="und">u.</ab> ')
 line = line.replace(' Bez.',' <ab>Bez.</ab>')
 line = line.replace(' Beiw.',' <ab>Beiw.</ab>')
 line = line.replace(' desgl.',' <ab>desgl.</ab>')
 line = line.replace(' z. B.', ' <ab>z. B.</ab>')
 line = line.replace('buddh.','<ab>buddh.</ab>')
 line = line.replace(' Hdschrr.',' <ab>Hdschrr.</ab>')
 line = line.replace('<ab>Comm.</ab> zu <ls>', '<ls><ab>Comm.</ab> zu ')
 line = line.replace('</ls>. <ab>fgg.</ab>',  '. fgg.</ls>')
 line = line.replace(' st. ', ' <ab>st.</ab> ')
 #
 line = re.sub(r'([0-9]+[.]) {#',  r'<hom>\1</hom> {#',line)
 line = line.replace('<ab>ebend.</ab>',  '<ls><ab>ebend.</ab></ls>')
 line = line.replace('<ls>ZACH.</ls> Beitr.',  '<ls>ZACH. Beitr.</ls>')
 line = line.replace('<as1>Prākrit</as1>', '<lang>Prākrit</lang>')
 line = line.replace('^2^','²')
 line = re.sub(r'([0-9]+)〉 ([a-z])〉',  r'\1〉\2〉',line)
 line = line.replace('</ls>, <ab>Sch.</ab>',  ', <ab>Sch.</ab></ls>')
 line = line.replace('  ',' ')
 # <ls>KĀD.</ls> (1872〉 75,13.
 line = re.sub(r'<ls>KĀD.</ls> \(([0-9]+)〉 ([0-9]+,[0-9]+)[.]',
               r'<ls>KĀD. (\1) \2</ls>.', line)
 line = re.sub(r'<ls>HARṢAC.</ls> \(([0-9]+)〉 ([0-9]+,[0-9]+)[.]',
               r'<ls>HARṢAC. (\1) \2</ls>.', line)
 line = re.sub(r'<ls>PAÑCAT.</ls> ed. orn. ([0-9]+,[0-9]+)[.]',
               r'<ls>PAÑCAT. ed. orn. \1</ls>.', line)
 line = re.sub(r'<ls>ZACH. Beitr.</ls> ([0-9]+)',
               r'<ls>ZACH. Beitr. \1</ls>', line)
 line = re.sub(r'<ls>MĀLATĪM.</ls> \(ed. Bomb.\) ([0-9]+,[0-9]+)',
               r'<ls>MĀLATĪM. (ed. Bomb.) \1</ls>', line)
 line = line.replace('</ls>. <ab>fg.</ab>',  '. <ab>fg.</ab></ls>')
 line = re.sub(r'</ls> \(([0-9]+,[0-9]+)〉.',
               r' (\1).</ls>',line)
 line = re.sub(r'<ls><ab>ebend.</ab></ls> ([0-9,]+[0-9])\.',
               r'<ls><ab>ebend.</ab> \1</ls>.',line)
 return line
def update(lines):
 newlines = []
 for line in lines:  # old ab 
  if line.startswith(('<L>', '<LEND>', '<althws>')):
   newlines.append(line)
  elif line.strip() == '':
   newlines.append(line)
  else:
   newline = update_line(line)
   newlines.append(newline)
 return newlines

def write_lines(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for out in lines:
   f.write(out+'\n')  
 print(len(lines),"lines written to",fileout)

if __name__=="__main__":
 filein = sys.argv[1]  # initial cdsl version
 fileout = sys.argv[2] # revised cdsl version

 lines = read_lines(filein)
 newlines = update(lines)
 write_lines(fileout,newlines)
 
