italic tooltips
This documents work begun 04-01-2024.
For motivation, please see this and related comments.
 https://github.com/sanskrit-lexicon/PWK/issues/97#issuecomment-1652222579

# this directory
cd /c/xampp/htdocs/sanskrit-lexicon/pwk/pwkissues/issue97

AB's css example:
cp ../issue106/italic_tooltip/italic_tooltips.html .

The css in this example does indeed result in italic tooltip text.
But browsers show the tooltip twice. (double-vision)

-----------------------------------------------------------------
Several experiments: Download any of these files and open in a browser
* copilot_0.html  Example from Microsoft copilot.  Works properly
  tooltip text is from the custom data-tooltip attribute.
* copilot_0a.html Shows the double-vision problem.
  tooltip text is from the (built-in) 'title' attribute
* italic_tooltips.html  (described above) double-vision, title attribute.
* italic_tooltips_0.html use custom 'titletip' attribute for tooltip text.

Next will 
* copilot_1.html  Removes double-vision problem, by
  changing the 'title' attribute to an arbitrary not-built-in attribute name.
  In this case, 'title' -> 
  
Modifications to csl-websanlexicon
web/webtc/main.css
  Add CSS for 'i > .tooltip' and '.tooltip'
basicdisplay.php
---------------------------------------------------------
s
