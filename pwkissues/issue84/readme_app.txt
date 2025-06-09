apps for mbhbomb repo


https://sanskrit-lexicon-scans.github.io/mbhbomb/
shows README.md  (with markdown converted to html)
----------------
edit mbhbomb/README.md

=================================================
app0 for mbhbomb repo : external page
external page number
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/mbhbomb
local url:
localhost/sanskrit-lexicon-scans/mbhbomb/app0/N
  N 3 to 108
  
Github url:
https://sanskrit-lexicon-scans.github.io/mbhbomb/app0/?N

----------------
# app0 is similar to that of /bhattikavya/app0
cd /c/xampp/htdocs/sanskrit-lexicon-scans/mbhbomb
cp -r ../bhattikavya/app0 .

For this repo, we choose to make an index for ALL external pages.

# 
cp app0/pywork/make_js_index.py app0/pywork/tempwork_make_js_index.py

# get the index for app1 (we'll use it for app0 also)

cp /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue84/index.txt app0/pywork/
# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue84/make_js_index.py app0/pywork/

# revise make_js_index.py so
- only vp, title in each record of index.js


# generate index.js
cd app0/pywork
python make_js_index.py index.txt index.js

# copy index.js to app0 
cp index.js ../

-------------------------------------
mbhbomb has pdfpages arranged as follows:
pdfpages1  mbhbomb1-001.pdf  to  mbhbomb1-679.pdf
pdfpages2  mbhbomb2-001.pdf  to  mbhbomb2-643.pdf
pdfpages3  mbhbomb3-001.pdf  to  mbhbomb3-881.pdf
pdfpages4  mbhbomb4-001.pdf  to  mbhbomb4-837.pdf
pdfpages5/pdfpages5.1/mbhbomb5-0001.pdf  to mbhbomb5-0999.pdf
pdfpages5/pdfpages5.2/mbhbomb5-1000.pdf  to mbhbomb5-1023.pdf

pdfpages6  mbhbomb6-001.pdf  to  mbhbomb6-705.pdf

Rearranged  pdfpages5, so
pdfpages5 mbhbomb5-0001.pdf  to mbhbomb5-1023.pdf

-------------------------------------

cd /c/xampp/htdocs/sanskrit-lexicon-scans/mbhbomb/app0

TITLE Mahâbhârata épopée classique. India, 1850.

source: Google Books

# Edit index.html
--- head/title: mbhbomb
--- body/title: {TITLE}

# Edit info.html
--- head/title: mbhbomb info
--- body/title: {TITLE}
--- app0 

# Edit main.js
# pdfpages:  mbhbomb-NNN.pdf,  where NNN is external page number

=================================================
app1 for mbhbomb repo  (3-parameter)
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/mbhbomb
local url:
localhost/sanskrit-lexicon-scans/mbhbomb/app1/N,N,N
 
Github url:
https://sanskrit-lexicon-scans.github.io/mbhbomb/app1/?N,N,N

----------------

# app1 is similar to that of /ramayanabom/app1
cd /c/xampp/htdocs/sanskrit-lexicon-scans/mbhbomb
cp -r ../ramayanabom/app1 .

# get the index for mbhbomb.  Use index_AB2.txt from issue84

cp /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue84/index_AB2.txt app1/pywork/index.txt
# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue84/make_js_index.py app1/pywork/

# generate index.js
cd app1/pywork
python make_js_index.py index.txt index.js

# copy index.js to app1 
cp index.js ../

-------------------------------------

cd /c/xampp/htdocs/sanskrit-lexicon-scans/mbhbomb/app1

# Edit index.html
--- head/title: mbhbomb
--- body/title: {TITLE}

# Edit info.html
--- head/title: mbhbomb info
--- body/title: {TITLE} 
--- app1 

# edit main.js
=================================================

When local debugging done, sync sanskrit-lexicon-scans/mbhbomb to Github.


