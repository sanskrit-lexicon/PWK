
verbs01a for pw.

Analysis of pw verbs and upasargas.
This work was done in a temporary subdirectory (temp_verbs01a) of csl-orig/v02/pw/.
Thus the relative path '../../mw/mw.txt' resolves to 'csl-orig/v02/mw/mw.txt'.

The shell script redo.sh reruns 5 python programs, from mwverb.py to preverb1.py.


* mwverbs
python mwverb.py mw ../../mw/mw.txt mwverbs.txt
#copy from v02/mw/temp_verbs
#cp ../../mw/temp_verbs/verb.txt mwverbs.txt
each line has 5 fields, colon delimited:
 k1
 L
 verb category: genuinroot, root, pre,gati,nom
 cps:  classes and/or padas. comma-separated string
 parse:  for pre and gati,  shows x+y+z  parsing prefixes and root

* mwverbs1.txt
python mwverbs1.py mwverbs.txt mwverbs1.txt
Merge records with same key (headword)
Also  use 'verb' for categories root, genuineroot, nom
and 'preverb' for categories pre, gati.
Format:
 5 fields, ':' separated
 1. mw headword
 2. MW Lnums, '&' separated
 3. category (verb or preverb)
 4. class-pada list, ',' separated
 5. parse. Empty for 'verb' category. For preverb category U1+U2+...+root

* pw_verb_filter.

python pw_verb_filter.py ../pw.txt pw_verb_exclude.txt pw_verb_include.txt pw_verb_filter.txt
pw_verb_include.txt contains metalines for entries that are believed to be
 verbs, but that are not otherwise detected.

pw_verb_exclude.txt contains metalines for records that are NOT verbs,
but that have some of the patterns for roots.  

Thes two files are derived empirically.

Patterns for roots:
 3 = '¦[ ,]*{#[^#]*t[ie]#}'   Example: {#aMSApay#}¦, {#aMSApa/yati#} 
 N = '[dD]enom[.] von'
 S = Sautra
 U = Has upasarga text. <div n="p">— Mit {#([a-zA-Z]+)#}
  (pw_verb_exclude_lex.txt)

Counts of total pattern combinations.
1926 3
0039 3N
0001 3S
0652 3U
0002 N
0001 NU
0002 S
0195 U
0001 X
2819 verbs written to pw_verb_filter.txt


Format of file pw_verb_filter.txt:
;; Case 0001: L=16, k1=aMSay, k2=*aMSay, code=3

* pw_verb_filter_map
python pw_verb_filter_map.py pw_verb_filter.txt pw_mw_map_edit.txt mwverbs1.txt pw_verb_filter_map.txt

Get correspondences between pw verb spellings and
 - pw verb spellings
 - mw verb spellings
Uses pw_mw_map_edit.txt  , which contains some correspondences
developed by earlier work.  The program pw_verb_filter_map.py also has 200+
numerous 'hard-coded' correspondences, derived empirically; these
are in the 'map2mw_special' variable; there are also several rules used
to derive correspondences.

Consider:
```
;; Case 0037: L=3091, k1=aDyApay, k2=aDyApay, code=3, #upasargas=0, mw=aDI (diff)
```
In this case, in MW, `aDI` shows a causal form 'aDyApaya'; that is why 'aDI' is
said to be the MW verb corresponding to the PW verb entry 'aDyApay'.


Format of pw_verb_filter_map.txt:
 Adds a field mw=xxx to each line of pw_verb_filter.txt,
indicating the MW root believed to correspond to the PW root.
For example, aMSay in PW is believed to correspond to aMS in MW.
;; Case 0001: L=16, k1=aMSay, k2=*aMSay, code=3, mw=aMS

In 95 cases, no correspondence could be found. These use 'mw=?'. For example:
;; Case 0005: L=354, k1=akzigocaray, k2=akzigocaray, code=3, mw=?


* preverb1.txt
python preverb1.py slp1 ../pw.txt pw_verb_filter_map.txt mwverbs1.txt pw_preverb1.txt

For each of the entries of pw_verb_filter_map.txt, the program analyzes the
text of PW looking for upasargas.  An upasarga is identifed by the pattern
U (see above).
```

The number of upasargas found is reported on a line for the verb entry.
The first PW verb entry has no upasargas:
;; Case 0001: L=16, k1=aMSay, k2=*aMSay, code=3, #upasargas=0, mw=aMS (diff)


The fourth PW verb entry has 2 upasargas:
```
;; Case 0004: L=249, k1=akz, k2=akz, code=3U, #upasargas=2 (1/1), mw=akz (same)
01        nis        akz               nirakz               nirakz yes nis+akz
02        sam        akz               samakz               samakz no 
```
For each upasarga, an attempt is made to match the prefixed verb to a
known MW prefixed verb.  
In this example, nis+akz was matched to MW nirakz; The 'yes' notation
indicates the prefixed verb match.
However, the upasarga 'sam' with the root 'akz' found no match in MW, using
the spelling 'samakz'; the 'no' notation indicates this.

Altogether, there are currently 5767 'yes' cases, and 1624 'no' cases.

One subtlety of the PW-MW matching process is that spelling differences of the
underlying root (differences between PW and MW) are taken into account.
For example:
```
;; Case 0009: L=843, k1=aGAy, k2=aGAy, code=3U, #upasargas=1 (1/0), mw=aGAya (diff)
01        aBi       aGAy              aByaGAy             aByaGAya yes aBi+aGAya
```
The PW root 'aGAy' is matched with the mw root 'aGAya'.
When combined with the upasarga 'aBi',  the implicit PW prefixed verb is
'aByaGAy'; and the corresponding MW prefixed verb is 'aByaGAya'. In this case 
there is an EXPLICIT MW entry for 'aByaGAya', hence the 'yes' notation.  
Incidentally, the parsing expression 'aBi+aGAya' is taken from MW.

There are many varied (sandhi) spelling changes occur when certain combinations of upasargas
are combined with certain roots.  My derivation of these changes is empirical, by which
I mean a mis-mash of rules which lead to as many correspondences as possible.  

---------------------------------------------------------------
