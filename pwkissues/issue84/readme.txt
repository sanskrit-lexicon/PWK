issue84/readme.txt
05-30-2025 begun ejf

MBH. BOMBAY edition
pdfs: /e/pdfwork/mbhbomb/pdfs (pages rotated)
  There are 6 volumes:  mbhbomb1.pdf , ... , mbhbomb6.pdf  
  Also mbhbomb_titular.pdf.
  
indexes:
 index1_orig.txt, ..., index6_orig.txt
 
Ref: https://github.com/sanskrit-lexicon/PWK/pwkissues/84

This issue84 directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue84

----------------------------------------
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue84
mkdir indexes
cd indexes
cp /e/pdfwork/mbhbomb/index?_orig.txt .

# index_orig.txt
# concatenate the indexes, make minor adjustments.
cd /c/xampp/htdocs/sanskrit-lexicon/PWK/pwkissues/issue84
python make_index_orig.py indexes index_orig.txt
41 lines with non-empty remark
6519 cases written to index_orig.txt

# index.txt
numerous adjustments (mostly for missing data ---)
a few corrections

python make_index.py index_orig.txt index.txt
6519 cases written to index.txt

----------------------------------------
Format observations:
vol.	page	parva	adhy.	from v.	to v.	ipage	optional-remark


----------------------------------------
index.txt changes

python make_index.py index_orig.txt index.txt
6518 Success: Page records read from index.txt


----------------------------------------
# construct index.js, and check for internal consistencies

python make_js_index.py index.txt index.js
6518 Success: Page records read from index.txt

Note title line of index.txt does not contribute to index.js

 preliminary check of pwg links
 5 Checks succeeded.  See readme_checks.txt

----------------------------------------
'ready for repo' message in https://github.com/sanskrit-lexicon/PWG/issues/149
----------------------------------------
2025-06-05
index_AB.txt
https://github.com/sanskrit-lexicon/PWK/issues/84#issuecomment-2943060552

python make_js_index.py index_AB.txt index_AB.js
6529 Success: Page records read from index_AB.txt

diff index.js index_AB.js | wc -l
781

Note: In construction of app1, use index_AB.txt.
  See readme_app.txt

2025-06-06
 index_AB.txt revised
Ref: https://github.com/sanskrit-lexicon/PWK/issues/84#issuecomment-2948211955
# remake index.js
python make_js_index.py index_AB.txt index_AB.js
# 6530 Success: Page records read from index_AB.txt

# copy to mbhbomb/app1/pywork/index.txt

----------------------------------------
06-07-2025  index_AB1_missing.txt
proposal for missing scans in index

python make_index_AB1_missing.py index_AB1.txt index_AB1_missing.txt

----------------------------------------
06-09-2025  index_AB2.txt

renamed from index_AB.revised.txt
Ref: https://github.com/sanskrit-lexicon/PWK/issues/84#issuecomment-2954404516
This to be used instead of index_AB1_missing.txt.

# construct index
python make_js_index.py index_AB2.txt index_AB2.js
6529 Success: Page records read from index_AB2.txt

Andhrabharati also proposes names for the 22 missing scan pages.

1-624x 1-624y
1-638x 1-638y
1-664x 1-664y
2-288x 2-288y
3-66x  3-66y
3-104x 3-104y
3-126x 3-126y
4-408x 4-408y
4-570x 4-570y
4-632x 4-632y
4-638x 4-638y

Revise readme_app.txt  to use index_AB2.txt for app1
And revise sanskrit-lexicon-scans/mbhbomb/app1
----------------------------------------
ADDITIONAL STEPS   

app construction.
2 apps needed:  see readme_app.txt
app1 -- parvan,adhyaya,verse
app0 -- all pages

----------------------------------------
modify basicadjust.php for pwg, pw, pwkvn, sch, mw
see readme_websanlexicon.txt

----------------------------------------
checks of links from dictionaries
see readme_checks.txt  (one NOT FOUND).

sync to github:  csl-websanlexicon, csl-apidev, csl-orig, csl-corrections
pull github to cologne server
regenerate displays for pwg, pw, pwkvn, sch, mw
=============================================================
THE END

