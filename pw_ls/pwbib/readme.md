
# pwbib

**step0** pwbib_orig.txt was received from Thomas Malten Nov 16, 2015.  It comprises a
digitization of the list of works as presented in the 6 volumes of the
PW dictionary.

**step1** pwbib_utf8.txt The pwbib_orig.txt file is in the cp1252 encoding.   Since the utf-8 encoding is more convenient, pwbib_utf8.txt was created as a copy in the utf-8 encoding.  The programmatic step:
```
python cp1252-to-utf8.py pwbib_orig.txt pwbib_utf8.txt

**step2** pwbib0.txt.  Starts as a copy of pwbib_utf8.txt.
  Manual editing changes made for the purpose of regularizing parsing.
  Ref: https://github.com/sanskrit-lexicon/PWK/issues/14

**step3** parsing.  
python pwbib_parse0.py pwbib0.txt
This parses the file into 502 relevant lines, with a regular structure, as
described in  https://github.com/sanskrit-lexicon/PWK/issues/14
Note: the command line usage above just checks that no anomalies are found.
The main use of it is as a module to be used by other programs, such as
pwbib1.py.

**step4** pwbib1 -  first conversion of AS to Unicode.
python pwbib1.py pwbib0.txt pwbib1.txt
Some details discussed in https://github.com/sanskrit-lexicon/PWK/issues/14
