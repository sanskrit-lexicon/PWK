punct/readme.txt

Punctuation changes.
See https://github.com/sanskrit-lexicon/PWK/issues/95#issuecomment-1652023255

---------------------------------------------------
# punctuation at end of italic text in temp_pw_ab_7
In temp_pw_ab_7.txt, periods are after:  {X%}. - exceptions
8 matches for "\.%}" in buffer: temp_pw_ab_7.txt
   7791:*{#atiguhA#}¦ <lex>f.</lex> {%Haemionites cordifolia Roxb.%}
  93514:*{#upavawa#}¦ <lex>m.</lex> {%Buchanania latifolia Roxb.%}
 105780:<div n="2">— c〉 {%Artocarpus Lacucha Roxb.%}
 128657:<div n="2">— i〉 mystische <ab>Bez.</ab> {%des Lautes m.%}
 159010:<div n="2">— e〉 mystische <ab>Bez.</ab> {%des Lautes m.%}
 159045:{#kzvela#}¦ <lex>m.</lex> mystische <ab>Bez.</ab> {%des Lautes m.%}
 214573:<div n="2">— d〉 {%Ei.%}
 301901:<div n="2">— b〉 {%Ei.%}
 
The 'Roxb.' cases:  add bot markup
The other cases:  Put period outside italic.
cp ../temp_pw_ab_7.txt ../temp_pw_ab_8.txt
Modify temp_pw_ab_8 manually

In issue88 folder:
python diff_to_changes_dict.py temp_pw_ab_7.txt temp_pw_ab_8.txt temp_change_ab_8_1.txt
8 changes written to temp_change_ab_8_1.txt

touch change_pw_ab_8.txt
insert temp_change_ab_8_1.txt

# check
python updateByLine.py temp_pw_ab_7.txt change_pw_ab_7.txt temp.txt
diff temp.txt temp_pw_ab_7.txt | wc -l
# 0 as expected
-----------------------------------------------------------------
3131 matches in 2954 lines for ";%}" in buffer: temp_pw_ab_7.txt
1 match for "%};" in buffer: temp_pw_ab_7.txt

5956 matches in 5671 lines for ",%}" in buffer: temp_pw_ab_7.txt
10 matches for "%}," in buffer: temp_pw_ab_7.txt

Note: In this work, I will follow the preference of Andhrabharati
  to leave final comma and semicolon BEFORE the closing '%}' of italic text.
  Ref: https://github.com/sanskrit-lexicon/PWK/issues/88#issuecomment-1756701308

Will change only the 1 semicolon and 10 commas from AFTER to BEFORE
  in temp_pw_ab_8.
  See 'Part 2' of change_pw_ab_8.txt
-----------------------------------------------------------------

Make temp_pw_8.txt consistent in some punctuation details

# remove extra spaces 'around' punctuation.
# see space_replacements function in punct1.py
python punct1.py ../temp_pw_7.txt ../temp_pw_8a.txt

python punct2.py ../temp_pw_8a.txt ../temp_pw_8.txt
112593 lines changed


grep -E ",%}" temp_pw_8.txt  | wc -l
5738

grep -E ";%}" temp_pw_8.txt  | wc -l
2957

grep -E "[.]%}" temp_pw_8.txt  | wc -l
0
----
grep -E "%}[.]" temp_pw_8.txt  | wc -l
107838
grep -E "%}," temp_pw_8.txt  | wc -l
0
grep -E "%};" temp_pw_8.txt  | wc -l
0
-------------------------------------
Install temp_pw_8.txt in csl-orig repository, and update displays
cd ../  # issue88

-----------------------
# do local install
cp temp_pw_8.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt

# check local installation
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pw  ../../pw
sh xmlchk_xampp.sh pw
# ok
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue88

# push repositories to GitHub
----- csl-orig
cd /c/xampp/htdocs/cologne/csl-orig
git pull # check for other revisions. 
git status  # v02/pw/pw.txt
git add .
git commit -m "PW: Revise pw.txt based on temp_pw_8.txt
  Ref: https://github.com/sanskrit-lexicon/PWK/issues/88"
git push

--------------------------------------------
update cologne displays
login to cologne
---- csl-orig
git pull
---- csl-pywork
cd v02
sh generate_dict.sh pw  ../../PWScan/2020/

--------------------------------------------
sync this repository to Github
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue88

git add .
git commit -m "temp_pw_8, temp_pw_ab_8. #88"

