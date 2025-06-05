
=================================================
activating links to mbhbomb app1 
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/mbhbomb
local urls:
localhost/sanskrit-lexicon-scans/mbhbomb/app1/?N,N

Github url:
https://sanskrit-lexicon-scans.github.io/mbhbomb/app1/?N,N

https://sanskrit-lexicon-scans.github.io/mbhbomb/
shows README.md  (with markdown converted to html)
# link abbreviations in xxxauth.txt

3-parameter references 
pwg MBH. 
pw  MBH. N,N,N : 3471 
pw  MBH. ed. Bomb. N,N,N : 9
pwkvn MBH. 
sch Mbh.
mw  MBh. R,N,N : 232
mw  MBh. (ed. Bomb.) N,N,N : 2
mw  MBh. (ed. Bombay) N,N,N : 1

# -------------------


# edit local csl-websanlexicon ... basicadjust.php

 /c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php
 

cd /c/xampp/htdocs/cologne/csl-websanlexicon/v02
sh generate_web.sh pwg  ../../pwg
sh generate_web.sh pw  ../../pw
sh generate_web.sh pwkvn  ../../pwkvn
sh generate_web.sh sch  ../../sch
sh generate_web.sh mw  ../../mw

sh apidev_copy.sh  # simple search gets new basicadjust.php

Proceed to readme_checks.txt 
When these checks are finished,
this csl-websanlexicon step is finished locally.

Push csl-websanlexicon, csl-apidev to github

