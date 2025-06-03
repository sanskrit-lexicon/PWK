apps for malavikagni repo


https://sanskrit-lexicon-scans.github.io/malavikagni/
shows README.md  (with markdown converted to html)
----------------
edit malavikagni/README.md

=================================================
app0 for malavikagni repo : ipage
internal page number
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/malavikagni
local url:
localhost/sanskrit-lexicon-scans/malavikagni/app0/N
  N 3 to 108
  
Github url:
https://sanskrit-lexicon-scans.github.io/malavikagni/app0/?N

----------------
# app0 is similar to that of /rajatar/app0
cd /c/xampp/htdocs/sanskrit-lexicon-scans/malavikagni
cp -r ../rajatar/app0 .

For this repo, we choose to make an index for ALL internal pages.
This is different than the rajatar goal.
epage 1-5 ignored
epage 6,  title page (no ipage)  i
epage 7,  blank  ii
epage 8, praefatio iii
epage 9, iv
epage 10, v
epage 11, vi
epage 12, vii 
epage 13, viii  (typo  print shows vii)
epage 14, ix
epage 15, x  (blank)
epage 16, ipage 1 first main page
epage 89, ipage 74 last main page

epage 90, ipage 75 first prakrit page
epage 109, ipage 94 last prakrit page

epage 110, ipage 95  first Varietas scripturae page
epage 123, ipage 108 last Varietas scripturae page

epage 124-129  ignored


# 
cp app0/pywork/make_js_index.py app0/pywork/tempwork_make_js_index.py

# get the index for app1 (we'll use it for app0 also)

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue149/index.txt app0/pywork/
# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue149/make_js_index.py app0/pywork/

# revise make_js_index.py so
- only page, ipage and vp, title in each record of index.js
- all prefac

# generate index.js
cd app0/pywork
python make_js_index.py index.txt index.js

# copy index.js to app0 
cp index.js ../

-------------------------------------

cd /c/xampp/htdocs/sanskrit-lexicon-scans/malavikagni/app0

TITLE Mālavikāgnimitra, O. Tullberg, 1840

# Edit index.html
--- head/title: malavikagni
--- body/title: {TITLE}

# Edit info.html
--- head/title: malavikagni info
--- body/title: {TITLE}
--- app0 

# Edit main.js
# pdfpages:  malavikagni-NNN.pdf,  where NNN is external page number

=================================================
app1 for malavikagni repo  (1-parameter verse)
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/malavikagni
local url:
localhost/sanskrit-lexicon-scans/malavikagni/app1/N
 
Github url:
https://sanskrit-lexicon-scans.github.io/malavikagni/app1/?N

----------------

# app1 is similar to that of /shakuntala/app1
cd /c/xampp/htdocs/sanskrit-lexicon-scans/malavikagni
cp -r ../shakuntala/app1 .

# get the index for malavikagni

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue149/index.txt app1/pywork/
# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue149/make_js_index.py app1/pywork/

# generate index.js
cd app1/pywork
python make_js_index.py index.txt index.js

# copy index.js to app1 
cp index.js ../

-------------------------------------

cd /c/xampp/htdocs/sanskrit-lexicon-scans/malavikagni/app1

# Edit index.html
--- head/title: malavikagni
--- body/title: {TITLE}

# Edit info.html
--- head/title: malavikagni info
--- body/title: {TITLE} 
--- app1 


=================================================
app2 for malavikagni repo  (2-parameters) ipage,line-number

=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/malavikagni
local url:
localhost/sanskrit-lexicon-scans/malavikagni/app2/N,N
 
Github url:
https://sanskrit-lexicon-scans.github.io/malavikagni/app2/?N,N

https://sanskrit-lexicon-scans.github.io/malavikagni/

----------------

# app2 is similar to that of /shakuntala/app2
cd /c/xampp/htdocs/sanskrit-lexicon-scans/malavikagni
cp -r ../shakuntala/app2 .

# get the index for malavikagni

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue149/index.txt app2/pywork/
# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue149/make_js_index.py app2/pywork/

# generate index.js
cd app2/pywork
python make_js_index.py index.txt index.js

# copy index.js to app2 
cp index.js ../

-------------------------------------

cd /c/xampp/htdocs/sanskrit-lexicon-scans/malavikagni/app2

# Edit index.html
--- head/title: malavikagni
--- body/title: {TITLE}

# Edit info.html
--- head/title: malavikagni info
--- body/title: {TITLE}
--- app2 

# Edit main.js
# pdfpages:  malavikagni-NNN.pdf


=================================================
app3 for malavikagni repo  (2-parameters) anka,verse

This is for MW references.


=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/malavikagni
local url:
localhost/sanskrit-lexicon-scans/malavikagni/app3/N,N
 
Github url:
https://sanskrit-lexicon-scans.github.io/malavikagni/app3/?N,N

https://sanskrit-lexicon-scans.github.io/malavikagni/

----------------

# app3 is similar to that of app2
cd /c/xampp/htdocs/sanskrit-lexicon-scans/malavikagni
cp -r app2 app3

# get the index for malavikagni

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue149/index.txt app3/pywork/
# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue149/make_js_index.py app3/pywork/

# generate index.js
cd app3/pywork
python make_js_index.py index.txt index.js

# copy index.js to app3 
cp index.js ../

-------------------------------------

cd /c/xampp/htdocs/sanskrit-lexicon-scans/malavikagni/app3

# Edit index.html
--- head/title: malavikagni
--- body/title: {TITLE}

# Edit info.html
--- head/title: malavikagni info
--- body/title: {TITLE}
--- app3 

# Edit main.js
# pdfpages:  malavikagni-NNN.pdf

From index:
anka   fromv tov
0 or 1 :  (1,21)  (1,21) + 0
2 : (22,35)       (1,14) + 21
3 : (36,58)       (1,23) + 35
4 : (59,75)       (1,17) + 58
5 : (76,95)       (1,20) + 75
# --------------------

i,1        praRatabahuPala x=1+0 = 1 pg 18 ok
i,2        prasahya x=2+0 = 2, pg 19  NOT FOUND
i,6/7	   bArhataka x= 6 pg. FOUND vAhataka MW: (<ab>w.r.</ab> <s>vAhataka</s>)
i,8        saMrohaRa  x=8 pg 24  found saMropaRa
i,11/12	   sutIrTa  x=11 FOUND
i,15       Sizwa  x = 15 pg. 29 NOT FOUND  (pg 29 has Slizwa)
i,15       Slizwa x = 15 pg. 29  FOUND! <ls>Mālav. i, 15</ls> (<ab>v.l.</ab> <s>Sizwa</s>)
i,15       saMkrAnti x = 15 pg. 29 FOUND!
i,17/18    nirhrIka  x=17+0 = 17, pg 31 NOT FOUND
i,19/20    catuzpada x = 19+0 = 19 pg 32 NOT FOUND  Found on pg 31
i,21       maDyamasvara x=21+0 = 21 pg 33 = ipage 18  NOT FOUND
            Word is in verse 20!  
ii,1       tiraskariRI x=1+21 = 22 ok
ii,11      tiraskariRI x=11+21 = 32 pg 38 ok
ii,26/27   cArutA check  AN ERROR!
iii,2      tIkzRatara  x=2+35 = 37 pg 43  ok
iii,20      caRqatA     x=20+35 = 55, pg 56 ok caRqi tAm
iii,19      cirAt       x=19+35 = 54, pg 55  ok
iv,2        gamita      x=2+58 = 60, pg 59 ok
iv,12       sevitf      x=12+58 = 70, pg 68 ok
v,4         jAlaka      x=4+75  = 79, pg 78 ok
v,19/20     caritArTa   x=19+75 = 94, pg 88 ok

When local debugging done, sync sanskrit-lexicon-scans/malavikagni to Github.


