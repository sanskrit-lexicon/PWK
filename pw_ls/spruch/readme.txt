pwk/pw_ls/spruch


Refer:
 https://github.com/

Start with a copy of csl-orig/v02/pw/pw.txt at commit
  cb165f79d06ff0a4ec93628023df600f1031d02f
# change to csl-orig repository on local installation
cd /c/xampp/htdocs/cologne/csl-orig/
# generate temp_pw_00.txt in this spruch directory
  git show cb165f79:v02/pw/pw.txt > /c/xampp/htdocs/sanskrit-lexicon/PWK/pw_ls/spruch/temp_pw_00.txt
# return to this spruch directory
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pw_ls/spruch/
# -------------------------------------------------------------
2933 matches in 2907 lines for "<ls>Spr[.]" in buffer: temp_pw_00.txt
2452 matches in 2439 lines for "<ls>Spr[.] +[0-9]+[.]</ls>" in buffer: temp_pw_00.txt
301 matches in 296 lines for "<ls>Spr[.] +[0-9]+</ls>" in buffer: temp_pw_00.txt

## list all instances of Spr. in pw.txt along with headwords
B
/c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pw/pywork/pwauth/pwbib_input.txt
python listls_abnormal.py 'Spr.' temp_pw_00.txt listls_abnormal_Spr.txt
(listls_abnormal.py based on ../pw_ls_AB/listls1_all.py)
 first run shows 180 'abnormal' ls elements, where 'normal' is
 <ls>Spr. [0-9]+[.]?</ls>
   normal examples: <ls>Spr. 123.</ls>   ,<ls>Spr. 1234</ls>
 Abnormal:
   4 <ls>Spr.</ls> 
  96 <ls>Spr. 3786. 7655.</ls>
  36 <ls>Spr. 99. fg.</ls> *Note 2
   9 <ls>Spr. 301. fgg.</ls> *Note 2

* Note 1 Investigate Separately -- ls markup of these 'Spr.' may be wrong
  Requires individual examination. See
  
* Note 2 These will be also be considered 'normal', as they are easily parsed into
  references to a single verse in


; <L>19525<pc>1239-1<k1>upacitra<k2>upacitra<e>100
changes to 4 <ls>Spr.</ls> lines
python make_change_ls.py 1 temp_pw_00.txt temp_change_01.txt
  generates prototype changes.
  Actual 'new' lines manual, and inserted into change_01.txt.

python make_change_ls.py 2 temp_pw_00.txt temp_change_02.txt

<ls>Spr. 182. 521.</ls> -> <ls>Spr. 182.</ls> <ls n="Spr.">521.</ls>
107 lines changed.  Changes inserted into change_01.txt

python listls_abnormal.py 'Spr.' temp_pw_01.txt temp_listls_abnormal_Spr.txt

python make_change_ls.py 3 temp_pw_00.txt temp_change_03.txt

<ls>Spr. I. J. K.</ls> ->
  <ls>Spr. I.</ls> <ls n="Spr.">J.</ls>  <ls n="Spr.">K.</ls> 
107 lines changed.  Changes inserted into change_01.txt
python ../pw_ls_AB/updateByLine.py temp_pw_00.txt change_01.txt temp_pw_01.txt

python listls_abnormal.py 'Spr.' temp_pw_01.txt temp_listls_abnormal_Spr.txt

12 remaining 'abnormals'. Do them manually, after generating the
prototype changes.
python make_change_ls.py 4 temp_pw_00.txt temp_change_04.txt

One other 'normal':
<L>5521<pc>1065-2<k1>anDas  <ls>Spr. 7826, N.</ls>  

<L>25469<pc>2034-1<k1>kalADara  <ls>Spr. 7861,d.</ls> <ls>Spr. 7861,b.</ls>

python ../pw_ls_AB/updateByLine.py temp_pw_00.txt change_01.txt temp_pw_01.txt


python listls_abnormal.py 'Spr.' temp_pw_01.txt listls_abnormal1_Spr.txt

python listls_instances.py 'Spr.' temp_pw_01.txt  listls_instances.txt
3066 instances written to listls_instances.txt


install temp_pw_01.txt into csl-orig.

cp temp_pw_01.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'pw ' redo_xampp_all.sh
sh generate_dict.sh pw  ../../pw
sh xmlchk_xampp.sh pw
 #prints 'ok'

Make csl-websanlexicon changes to refer to web1.

