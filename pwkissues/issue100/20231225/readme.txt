
thomas.txt :
1. copy-paste text posted by Thomas in skype.
2. With emacs change  to C-qC-j  (new line)

thomas_utf8.txt
# thomas.txt is in cp1252 encoding.
# convert the to utf8 encoding, for consistency with csl-orig.
python ../cp1252_utf8.txt thomas.txt thomas_utf8.txt

#  Changes to pwg
Edit /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
L=97802 Wörterbuch -> Wörterbuchs
 slp1 = Sabdakalpadru
L=39367 ascertainment -> ascertainement [French!]
 slp1 = nirUha
  <fr>ascertainement</fr>

# Changes to pw  (pwk)
Edit /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
L=8453  (amftodana)  Söhnen -> Sohnes
L=17565 (Iza)  Söhnen -> Sohnes
L=11869 (aSvabAhu) Söhnen -> Sohnes

29 matches for "Söhnen" in buffer: pw.txt
1601 matches in 1590 lines for "Sohnes" in buffer: pw.txt

--------------

L=71268 (pratibimba) ausnahmasweise -> ausnahmsweise
-----
[in surrounding texts]
L=46402 (tula)
auf der wage halten -> auf der Wage halten

------
L=129811 (sOkara)
vor ehrt -> verehrt
------
L=78005 (brahmayoni) Walfahrtsortes -> Wallfahrtsortes
L=87459 (muYjavawa) Walfahrtsortes -> Wallfahrtsortes
L=129811 (sOkara) Walfahrtsortes -> Wallfahrtsortes
----------------------------
L=65907 (pAdaSuSrUzA) ehrfurchtsvolle -> Ehrfurchsvolle
Jim altered this (change a period to comma, per print)
NOTE: comma put 'inside' the closing italic. Consistent with rest of pw.txt
OLD: {%das den Füssen zu Willen Sein%}. ehrfurchtsvoller Ausdruck statt des einfachen
NEW: {%das den Füssen zu Willen Sein,%} ehrfurchtsvoller Ausdruck statt des einfachen

--------------
L=99767 (vA) von einem Gerüche -> von einem Geruche
--------------
L=96679 (lokAntara) bewohut -> bewohnt  (wrong L, Jim)
NOTE: bewohut occurs only in 95579
L=95579 (laNka) bewohut -> bewohnt

-----
L=24579 (karaRa) (page 2-022) Rechstsprache -> Rechssprache [a printing error]
NOTE: added note in csl-corrections/dictionaries/pw/pw_printchange.txt

-----
L=83284 (mandara) [in surrounding text]
  des Sitzen verschiedener Götter -> des Sitzes verschiedener Götter
-----
L=13305 (aho) Woder -> Weder
