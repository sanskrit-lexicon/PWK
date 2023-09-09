pwkissues/issue88/readme.txt
Improve abbreviation markup in PWK.
August 2023
This continues the work of 'abbrev' directory.

# this directory
cd /c/xampp/htdocs/sanskrit-lexicon/pwk/pwkissues/issue88

Ref: https://github.com/sanskrit-lexicon/PWK/issues/88

temp_pw_0.txt  take from csl-orig

cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw_0.txt
(commit 7c848d6546389c6c8d7612819dde0cce89601a6d)

cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pw/pywork/pwab/pwab_input.txt pwab_input_0.txt
  (commit 2bbf9918b768b9fdb934bf63b53999773b488f27)


*********************************************************************
meta/
stats on tags (global and local) and also on extended ascii characters.

*********************************************************************
ablists/
Andhrabharati lists of abbreviations 
---------------------------------------------------------------------
temp_pw_ab_0.txt
  from https://github.com/sanskrit-lexicon/PWK/files/12148898/pw.AB.v1.zip
  Andhrabharati version.

wc -l temp_pw*
  682608 temp_pw_0.txt
  674189 temp_pw_ab_0.txt
 so the ab version has about 8000+ fewer lines.

Make a few changes in temp_pw_ab_0.txt for xml validity (see dev1_ab below)
See file corrections_ab_1.txt
# make change_ab_1.txt
python corr_to_change.py temp_pw_ab_0.txt corrections_ab_1.txt change_ab_1.txt
16 read from corrections_ab_1.txt

# install changes into temp_pw_ab_1.txt
python updateByLine.py temp_pw_ab_0.txt change_ab_1.txt temp_pw_ab_1.txt
16 change transactions from change_ab_1.txt

construct dev version

--- devab_1
sh redo_dev.sh ab_1
# validity checked.

Note: temp_pw_ab_1.txt is now almost the same as
  pwkissues/issue95/temp_pw_ab_1.txt

diff ../issue95/temp_pw_ab_1.txt ../issue88/temp_pw_ab_1.txt
475943,475944c475943,475944
< <div n="p">— Mit {#vi#} ({#°lIyate#}, {#°lilyus#}, {#°lIya#}, *⁾{#°lAya#})
< <F>*⁾Wäre bis auf das {#la#} ein regelmässige Imperfect von {#ay#}, {#ayate#} mit {#nis#}.</F>
---
> <div n="p">— Mit {#vi#} ({#°lIyate#}, {#°lilyus#}, {#°lIya#}, *{#°lAya#})
> [Fußnote: *Wäre bis auf das {#la#} ein regelmässiges Imperfect von {#ay#}, {#ayate#} mit {#nis#}.]

====================================================================
08-24-2023.
ablists 
ab_glob0.txt contains initial statistics regarding counts of
 <ab>X</ab> using temp_pw_0.txt and temp_pw_ab_1.txt
We now 'cp temp_pw_0.txt temp_pw_1.txt'.

Various 'systematic' differences in the count are examined,
and changes are made to temp_pw_1.txt. 
Mostly these change 'X' to '<ab>X</ab>'.
We use (and revise) ab_glob1.txt to keep track of the
revised counts <ab>X</ab> from temp_pw_1.txt and temp_pw_ab_1.txt.
ab_glob1.txt contains the final status after this phase of changes.
There are now 304 abbreviations, and 129 of these have differenct
counts in temp_pw_1.txt and temp_pw_ab_1.txt.

The last step is to resolve these remaining differences.
We start with copies temp_pw_2.txt and temp_pw_ab_2.txt.
We know these have the same metalines.
The technique used here compares, for each entry, the
sequence of <ab>X</ab> from the two versions. This is done by
the compare_texts.py program, which prints out the first
difference in the <ab> sequences (along with some context).
Then, the difference is resolved by manual examination of the
texts of temp_pw_2 and temp_pw_ab_2; changes are made manually
Notes of these changes are in
ablists/change_2_notes.txt and ablists/change_2_ab_notes.txt.

The end is reached when there is <ab> sequences are the same
for all entries in both versions.

At this point we construct ab_glob2.txt which confirms that
for each X of the 304 abbreviations, the counts of <ab>X</ab>
is the same for revised temp_pw_2.txt and temp_pw_ab_2.txt.

Note ab_glob2.txt can be used later for pwab_input.txt

change_pw_ab_2.txt containts 673 changes when comparing
the original temp_pw_ab_0.txt and final temp_pw_ab_2.txt

python diff_to_changes_dict.py temp_pw_ab_0.txt temp_pw_ab_2.txt change_pw_ab_2.txt
673 changes written to change_pw_ab_2.txt

Incidentally,
sh redo_dev.sh ab_2
 confirms that temp_pw_ab_2.txt generates valid xml.
sh redo_prod.sh 2
 confirms that temp_pw_2.txt generates valid xml.

====================================================================

python diff_to_changes_dict.py temp_pw_ab_0.txt temp_pw_ab_2.txt change_pw_ab_2.txt
673 changes written to change_pw_ab_2.txt


====================================================================
The changes from version 2 to version 3 are
change_pw_3.txt and change_pw_ab_3.txt
ablists/readme.txt may provide some details.

The changes from version 3 to version 4 are
change_pw_4.txt and change_pw_ab_4.txt
Refer ablists/readme.txt
====================================================================
sh redo_dev.sh ab_4
 confirms that temp_pw_ab_4.txt generates valid xml.
sh redo_prod.sh 4
 confirms that temp_pw_4.txt generates valid xml.
====================================================================
====================================================================
====================================================================

********************************************************************
