
python homchk.py ../temp_pw_1.txt temp.txt
764479 lines read from ../temp_pw_1.txt
homchk: 7097 ok, 0 questionable
0 records written to temp1.txt

----------------------------------------------------

python nohomchk.py ../temp_pw_1.txt temp.txt
----------------------------------------------------
----------------------------------------------------
remove <h>N from metalines.
python hremove.py ../temp_pw_1.txt ../temp_pw_1a.txt
764479 lines read from ../temp_pw_1.txt
7097 lines changed
764479 lines written to ../temp_pw_1a.txt

----------------------------------------------------
Misc. changes to temp_pw_1a.txt
touch ../change_1a_2.txt

-- 01
python change_denom.py ../temp_pw_1a.txt temp_change.txt
# manually insert temp_change.txt into ../change_1a_2.txt,
-- 02
 manual change L=45920
 added to change_1a_2.txt
-- 03 possible root markup
 consonant-vowel-consonant
python possible_roots.py ../temp_pw_2.txt temp_possible_roots.txt
edit possible_roots_edit.txt
STATUS: 355 entries to change. Waiting for AB comment
python code/possible_roots_change.py temp_pw_2.txt possible_roots_edit.txt temp_possible_roots_change.txt

----------------------------------------------------
02-19-2024
 Alternate headword candidates 'close to' broken bar

**********************************************************
Notes on earlier work, currently a false trail
**********************************************************
----------------------------------------------------
# classification of broken-bar line
python bb.py ../temp_pw_2.txt ../bb

----------------------------------------------------
python bb_k2prob.py '02' ../bb temp_bb_k2prob.txt

For simple (no alternate headwords) cases, the
k2 of metaline should equal the DERIVED k2 from broken bar line (X¦)
  
sh bb_k2prob_all.sh
# should show '0 records written to ...' for each bbcode
# There should be a check of each code in regexraws of bb.py,
  except the 'NA' code
  
----------------------------------------------------
python morealt.py ../temp_pw_2.txt morealt_2_cand1.txt  morealt_2_cand2.txt morealt_2_NOALT_A.txt moreAlt_2_NOALT_B.txt

764479 lines read from ../temp_pw_2.txt
6336 records written to morealt_2_cand1.txt
4452 records written to morealt_2_cand2.txt
13413 records written to morealt_2_NOALT_A.txt
6853 records written to moreAlt_2_NOALT_B.txt

----------------------------------------------------
Process the candidates by sub-cases.
These changes will be applied to temp_pw_2.txt
-- 01  tA and tva
python cand_change.py '01' morealt_2_cand1.txt temp_change_3_01.txt temp_cand1_todo_01.txt

python updateByLine.py ../temp_pw_2.txt temp_change_3_01.txt ../temp_pw_3_unused.txt
----------------------------------------------------
TODO:
---
14 matches for "^.*?{#[^#]*\[.*¦" in buffer: temp_pw_1.txt
example: <L>5223<pc>1-062-a<k1>antarantaHsTa<k2>antaranta[H]sTa
{#antaranta[H]sTa#}¦
---
feminine form alt-headwords ?
----------------------------------------------------
misc. corrections TODO
--- mADyMdina -> mADyaMdina
<L>82626<pc>5-018-c<k1>maDyaMdina<k2>2. *maDyaMdina
406499 <hom>2.</hom> *{#maDyaMdina#}¦ <lex>Adj.</lex> = {#mADyMdina#}
--- root?
<L>67280<pc>4-088-a<k1>pIq<k2>pIq
330732 {#pIq#}¦ (<ab>Vgl.</ab> {#piz#}) {%pressen,%} Nur <ab>perf.</ab> {#pipIqe#} <ab>Caus.</ab> — {#pIqa/yati#} episch auch <ab>Med.</ab>
---
<L>67287<pc>4-088-b<k1>pIqAkara<k2>pIqAkara
330838 {#pIqAkara#}¦ (219) und {#pIqAkft#} <lex>Adj.</lex> {%Leid zufügend, Schaden bringend%}.
(<ls n="Chr.">219,2</ls>)
---
<L>8419<pc>1-098-c<k1>amftasravA<k2>*amftasravA
38139 *{#amftasravA#}¦ <lex>f.</lex> {%eine <ab>best.</ab> Pflanze%} (im <is>Citrakūṭa</is>). Auch *{#MsravI#} <ls>GAL.</ls>
{#MsravI#} -> {#°sravI#}
---
<L>204464<pc>3-259-c<k1>kup<k2>1. kup
691871 <hom>1.</hom> {#kup#}¦ mit {#ud#}
mark as root (there are others)
----------------------------------------------------
