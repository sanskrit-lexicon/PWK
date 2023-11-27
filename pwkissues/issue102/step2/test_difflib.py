# Import the difflib module
import difflib
import re
def test1():
 s1 = '!√{#aNkUray#}¦ {#°yati#} = {#aNkuray#}.'
 s2 = '!√{#aNkUray#}¦ {#°yati#} = !√{#aNkuray#}.'
 a1 = re.split(r' ',s1)
 a2 = re.split(r' ',s2)
 print('s1=',s1)
 print('a1=',a1)
 print('s2=',s2)
 print('a2=',a2)
 #Create a Differ object
 d = difflib.Differ()
 # Compare the two strings line by line
 result = d.compare(s1, s2)

 # Print the result as a list of strings
 print(list(result))

 result = d.compare(a1,a2)
 print(list(result))

def test2():
 s1 = '!√{#aNkUray#}¦ {#°yati#} = {#aNkuray#}.'
 s2 = '!√{#aNkUray#}¦ {#°yati#} = !√{#aNkuray#}.'
 a1 = re.split(r' ',s1)
 a2 = re.split(r' ',s2)
 print('a1=',a1)
 print('a2=',a2)
 #Create a Differ object
 d = difflib.Differ()
 # compare the words
 result = d.compare(a1,a2)
 print(list(result))

def test3():
 s1 = '!√{#aNkUray#}¦ {#°yati#} = {#aNkuray#}.'
 s2 = '!√{#aNkUray#}¦ {#°yati#} = !√{#aNkuray#}.'
 a1 = re.split(r' ',s1)
 a2 = re.split(r' ',s2)
    
 diff = difflib.ndiff(a1, a2)
 print(''.join(diff))
    
def test4():
 s1 = '!√{#aNkUray#}¦ {#°yati#} = {#aNkuray#}.'
 s2 = '!√{#aNkUray#}¦ {#°yati#} = !√{#aNkuray#}.'
 a1 = re.split(r' ',s1)
 a2 = re.split(r' ',s2)
 
 diff = difflib.ndiff(a1, a2)
 print('\n'.join(diff))
def test5():
 s1 = '!√{#aNkUray#}¦ {#°yati#} = {#aNkuray#}.'
 s2 = '!√{#aNkUray#}¦ {#°yati#} = !√{#aNkuray#}.'
 a1 = re.split(r' ',s1)
 a2 = re.split(r' ',s2)
 
 diff = difflib.ndiff(a1, a2)
 print('\n'.join(diff))

def test6():
 import difflib
 from difflib import SequenceMatcher
 str1 = 'I like pizza'
 str2 = 'I like tacos'
 seq = SequenceMatcher(a=str1, b=str2)
 print(seq.ratio())

def test7():
 import difflib
 from difflib import SequenceMatcher
 str1 = 'I like tacos'
 str2 = 'I like tacos'
 x1 = str1.split()
 x2 = str2.split()
 seq = SequenceMatcher(a=x1, b=x2)
 print(seq.ratio())

def test8():
 import difflib
 from difflib import Differ
 str1 = "I would like to order a pepperoni pizza"
 str2 = "I would like to order a veggie burger"
 str1_lines = str1.splitlines()
 str2_lines = str2.splitlines()
 d = difflib.Differ()
 diff = d.compare(str1_lines, str2_lines)
 print('\n'.join(diff))
 # output
 # I would like to order a 
 # '- ' pepperoni pizza
 # '+ ' veggie burger

def test9():
 import difflib
 from difflib import Differ
 str1 = "I would like to order a pepperoni pizza"
 str2 = "I would like to order a veggie burger"
 str1_lines = str1.split()
 str2_lines = str2.split()
 d = difflib.Differ()
 diff = d.compare(str1_lines, str2_lines)
 print('\n'.join(diff))
 # output
 # I would like to order a 
 # '- ' pepperoni pizza
 # '+ ' veggie burger


def test10_work(str1,str2,dbg=False):
 import difflib
 from difflib import Differ
 x1 = str1.split()
 x2 = str2.split()
 d = difflib.Differ()
 diff = d.compare(x1, x2)
 ans = []
 prev = None
 ans1 = []
 for a in diff:
  if a.startswith('  '):
   a1 = ('=',a[2:])
  elif a.startswith('- '):
   a1 = ('-',a[2:])
  elif a.startswith('+ '):
   a1 = ('+',a[2:])
  elif a.startswith('? '):
   a1 = ('?',a[2:])
 
  else:
   print('unexpected a="%s"' % a)
  ans1.append(a1)
 if dbg:
  for a1 in ans1:
   print(a1)
 #
 ans2 = []

 for i,a1 in enumerate(ans1):
  code = a1[0]
  s = a1[1]
  if i == 0:
   a2 = code + ' ' + s
   ans2.append(a2)
   prevcode = code
  elif code == prevcode:
   ans2[-1] = ans2[-1] + ' ' + s
  else:
   a2 = code + ' ' + s
   ans2.append(a2)
   prevcode = code
 return ans2

def test10a():
 str1 = "I would like to order a pepperoni pizza"
 str2 = "I would like to order a veggie burger"
 ans = test10_work(str1,str2)
 for a in ans:
  print(a)

def test10b():
 s1 = '{#aNkakAra#}¦ <lex>m.</lex> {%ein von einer Partei zur Entscheidung einer Sache erwählter Kämpfer%} <ls>BĀLAR. 214,3. 5. 216,13</ls>. Davon {#°tva#} <lex>n.</lex> <ab>Nom. abstr.</ab> <ls n="Chr.">214,9</ls>. {#°kAri#} <lex>Adv.</lex> mit {#kar#} {%zu einem solchen Kämpfer erwählen%} <ls n="Chr. 214,">17</ls>.'
 s2 = '{#aNkakAra#}¦ <lex>m.</lex> {%ein von einer Partei zur Entscheidung einer Sache erwählter Kämpfer%} <ls>BĀLAR. 214,3. 5. 216,13</ls>. Davon {#°tva#} <lex>n.</lex> <ab>Nom. abstr.</ab> <ls n="BĀLAR.">214,9</ls>. {#°kAri#} <lex>Adv.</lex> mit {#kar#} {%zu einem solchen Kämpfer erwählen%} <ls n="BĀLAR. 214,">17</ls>.'
 
 ans = test10_work(s1,s2)
 for a in ans:
  print(a)

# 
# s2=
if __name__ == "__main__":
 test10b()
 
