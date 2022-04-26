#  Transforming pwkvn to Form
consistent with current coding
of csl-orig/v02/pw/pw.txt.

We work with cp1252 versions of pwkvn in ../orig directory.
Each of these versions have 22569 lines

===========================================================
conversion between cp1252 and utf8
===========================================================
The utility cp1252_utf8.py converts from cp1252 to utf8 encoding.
The utility utf8_cp1252.py converts from utf8 to cp1252.

The
python cp1252_utf8.py cp1252_version.txt utf8_version.txt

python utf8_cp1252.py utf8_version.txt cp1252_version.txt
Converting cp1252 -> utf8 -> cp1252a  results in cp1252a == cp1252
i.e. diff cp1252 cp1252a shows NO differences.

===========================================================
extended ascii characters
===========================================================
ea.py reads a utf8 version, and generates frequency count
of extended ascii characters
##---------------------------------------------------------
Find list of extended ASCII.
python ea.py utf8_version.txt ea.txt

some characters of interest are shown:
   The counts depend on which version of pwkvn is used.
1. pwkvn only £  (\u00a3)  2436 := POUND SIGN
   These noticed in {#X#} coding of Devanagari.  Purpose? Accent?
2. pwkvn only º  (\u00ba)  2044 := MASCULINE ORDINAL INDICATOR
   pw    only °  (\u00b0) 20488 := DEGREE SIGN
   replace MOI with DS in pwkvn
3. pwkvn only °  (\u00d7)     1 := MULTIPLICATION SIGN
   not sure --- change to simple 'x'?
4. pwkvn ²  (\u00b2) 12899 := SUPERSCRIPT TWO
   pw    ²  (\u00b2)   580 := SUPERSCRIPT TWO
   are the usages the same, or should pwkvn be altered
5. pwkvn ñ  (\u00f1)     3 := LATIN SMALL LETTER N WITH TILDE
   Not sure if these are intended.

===========================================================
lsprep1
Contains program used for analysis of <ls> markup.
This program was used in determining many corrections to pwkvn.
It generates a list ls1.txt of ls names, which is based on
pwk1-7VN_ansi_9.txt
===========================================================
lsprep2
Begins with pwk1-7VN_ansi_10.txt
Adds </ls> markup and makes several other changes.
Final result used to generate pwk1-7VN_ansi_14.txt.
===========================================================
lsprep3
Begins with orig/pwk1-7VN_ansi_14.txt
Convert AS (letter number) to IAST (letter with diacritics) for <ls>X</ls>

Construct orig/pwk1-7VN_ansi_15.txt
 change_15.txt :  600+ changes from version 14 to 15
 notes_15.txt : comparisons between pw.txt ls abbreviations and
                pwkvn ls abbreviations.
 as_roman.py program to literary source abbreviations to IAST.
 The pwkvn text at version 15 retains the AS markup.

===========================================================
wide :  AS markup in the text marked as 'wide' {|X|}
===========================================================
slp :   {#X#} to slp1 and check for errors.
        Also add <hw> and <hom> markup.
        End is version 20 of pwkvn.
===========================================================
meta:   Add initial metaline markup to ansi version.
===========================================================
page299:  incorporate missing page digitization into pwkvn
===========================================================
german1: Apply corrections to german
===========================================================
final:   Form of pwkvn as a Cologne dictionary (pwkvn.txt)
===========================================================
lsnum:   Extend ls markup to include numbers.
         Also use <ls n="X">N</ls> markup where needed.
===========================================================
 
