
# pwbib

 Note: sh redo.sh remakes everything.  It uses sortedcref.txt from pw_dhaval
 directory. 

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

(Aug 5, 2016). This program now makes adjustments to the title field, for those entries
of pwbib0 which DON'T have an ==.  (these are marked as type=xx in pwbib1.txt).
The unadjusted and adjusted titles are written to stdout, and are captured in a file by:
```
python pwbib_parse0.py pwbib0.txt > pwbib_parse0_log.txt
```

**step4** pwbib1 -  first conversion of AS to Unicode.
python pwbib1.py pwbib0.txt pwbib1.txt
Some details discussed in https://github.com/sanskrit-lexicon/PWK/issues/14

**step5** crefmatch
 match pwbib1.txt to sortedcrefs.txt
python crefmatch.py pwbib1.txt ../pw_dhaval/abbrvwork/abbrvoutput/sortedcrefs.txt  crefmatch.txt


**pwbib_unused.txt**  Work file containing abbreviations of pwbib that 
  are believed to be unused in the literary citations of pw.txt.

**step6** pwbib_new_work
sh redo.sh

merges pwbib1 and pwbib_new . Creates some displays including mw references

**step7** displayprep
```
python sortbib.py ../pwbib_new_work/mergebibnew.txt sortbib.txt
```

sortbib.txt is used by the pywork/pwauth to integrate the bibliographies
in the web displays of the PW dictionary.

