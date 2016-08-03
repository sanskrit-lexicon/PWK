
Documentation regarding preparing material for a display of the
PW bibliography.

Specifically, the objective is to enhance the display programs for PWK
 (such as the [basic display](http://www.sanskrit-lexicon.uni-koeln.de/scans/PWScan/2014/web/webtc/indexcaller.php)).

The enhancement is to have active hyperlinks for the bibliographic references,
similar to those that are available for the Monier-Williams displays at Cologne.

The present work prepares the way by constructing 
* a sqlite link file that may be used by the display program (webtc/disp.php) to
  construct a link to a static display of the PW bibliography
* and that static display of the PW bibliography.

The third step (done elsewhere) is to modify webtc/disp.php to interface
 with that sqlite link file.

The best version of the PW bibliography to work with seems to be 
 [mergebibnew.txt](https://github.com/sanskrit-lexicon/PWK/blob/master/pw_ls/pwbib/pwbib_new_work/mergebibnew.txt).

mergebibnew is essentially a csv file (with the colon character `:` as value separator), with the following fields:
* abbrvsort = a simplified abbreviation. Probably not useful here
* abbrv = the abbreviation as used in the dictionary; it is in the odd
  AS (Anglicized Sanskrit) form used by the digitized dictionary in the `<ls>`
  element.  (*digitized dictionary* here means the xml form of the 
  digitization, namely the file named pw.xml.)
* seqnum = sequence number (3-digit) of the item within a given volume.
* volume = the volume of the dictionary in which the given bibliographic entry
  was drawn.  This volume number is 1-7, for the actual dictionary.  But also
  there is a volume number of '0', which indicates that the abbreviation for
  this entry appears in one or more `<ls>` elements, but is currently
  not associated with a reference listed in the bibliographic sections of 
  any volume of the dictionary.
* titleunicode  is the title of the work, expressed in unicode encoding 
  of IAST type for Sanskrit words.

A reasonable first step seems to be to sort the entries of mergebibnew
by the volume:seqnum fields.  This is a reasonable order for the 
display of the authorities, since it (should) correspond to the scanned
image of the bibliographies.

There is a question about what to do with the volume 0 cases.  
~For now, I will just ignore them.~
Include the volume 0 cases, but write them as volume 'X', so they
will sort at the end of sortbib.txt.

```
python sortbib.py ../pwbib_new_work/mergebibnew.txt sortbib.txt
```

This sortbib.txt file is a csv file, tab-delimited, with three fields:
* abbrv = as above
* volseq = volume:seqnum
* titleunicode.

The use of tab-delimiting will make this suitable for a sqlite input file.
The file will be ordered by the 2nd field.
The first field can be used by disp.php.

As of this run of sortbib.py:
* 790 records from mergebibnew
* 503 records written to sortbib.txt
* Also, there are found 16 duplicate abbreviations.  The details of these
  are shown in sortbib_log.txt.  These are relevant to the present work,
  since, when a match is made in disp.php to a given abbreviation, the
  question will arise as to which of the duplicates should be shown.
  Some further revision will need to take this into account.

By the way, the scanned images may be found, for the separate volumes,
in the 'scanned display'. For instance, for the bibliographic entries from
volume 1, see page3 of the Preface for
 [vol. 1](http://www.sanskrit-lexicon.uni-koeln.de/scans/PWScan/index.php?sfx=jpg&vol=1)

