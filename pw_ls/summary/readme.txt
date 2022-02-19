PWK/pw_ls/summary



Refer:
 https://github.com/sanskrit-lexicon/PWK/issues/85

Start with a copy of latest pw.txt at 
  cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw.txt

and with a copy of latest pwbib_input.txt
cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pw/pywork/pwauth/pwbib_input.txt temp_pw_tooltip.txt


# -------------------------------------------------------------
 Get a count of <ls> by lsname

python lsextract_all.py temp_pw.txt temp_pw_tooltip.txt lsextract_pw.txt

