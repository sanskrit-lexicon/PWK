issue95/litsrc/readme.txt

------------------------
# pwbib_input_0.txt
#  initial value of the pw ls tooltip file
cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pw/pywork/pwauth/pwbib_input.txt pwbib_input_0.txt

------------------
gra_tooltip.txt
# tooltip file for Grassman  (for comparison)
cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/gra/pywork/graauth/tooltip.txt graauth_tooltip.txt

------------------
record structure of pwbib_input_0.txt

1020	AV.	Av.	ATHARVAVEDA, Ausg. von ROTH und WHITNEY (ROTH). 

There are 4 tab-delimited fields:
- identifier:   In current scheme, this field is not important. However,
   the value should be different for different lines.
- abbrev:  This field is comparable to the pw.txt markup abbreviation.
  e.g.<ls>AV. 29,130,8.</ls>  matches record above
- abbrev_disp:  This field is used to DISPLAY the abbreviation.
                See below for further discussion
- tooltip:  Provides the tooltip in displays.

-----------------
How is the  display generated?


