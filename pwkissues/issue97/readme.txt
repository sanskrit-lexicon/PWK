italic tooltips
This documents work begun 04-01-2024.
For motivation, please see this and related comments.
 https://github.com/sanskrit-lexicon/PWK/issues/97#issuecomment-1652222579

# this directory
cd /c/xampp/htdocs/sanskrit-lexicon/pwk/pwkissues/issue97

AB's css example:
cp ../issue106/italic_tooltip/italic_tooltips.html .

The css in this example does indeed result in italic tooltip text.

Modifications to csl-websanlexicon
web/webtc/main.css
  Add CSS for 'i > .tooltip' and '.tooltip'
basicdisplay.php

