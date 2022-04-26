Original digitizations from Thomas Malten

As of 03-21-2022 12:30 PM,
pwk1-7VN_ansi.txt  is copy of pwk1-7VN_ansi_10.txt

Following is brief description of the various versions.

pwk1-7VN_ansi_0.txt received from Thomas Malten Feb 12, 2022.
-----
pwk1-7VN_ansi_1.txt received from Thomas Malten Feb 22, 2022.
 revision to accents.
-----
pwk1-7VN_ansi_2.txt received from Thomas Malten Feb 23, 2022.
AS (letter-number) markup and <ls> tag.
-----
pwk1-7VN_ansi_3.txt Mar 14, 2022 Jim Funderburk.
In the process of making corrections in the Feb 23 version,
Thomas inadvertently changed the number of lines from 22569 to 37860.

All lines in the 0,1 versions start with '<p>' or '<H>'(9).
Next program restores Feb 23 version to 22569 lines.
Mar 14, 2022 EJF
python joinlines.py pwk1-7VN_ansi_2.txt pwk1-7VN_ansi_3.txt

-----
pwk1-7VN_ansi_4.txt Mar 15, 2022 Jim Funderburk.
Manual changes:
1. 1 line (line 2985)
<gr>beta</b> -> <gr>beta</gr>
2. ; [Page7-291-a]
9677 old <p>{#agnima£ya, agni£mukha, agniraja#} und ²agnirU£pa I. 1. 

9677 new <p>{#agnima£ya, agni£mukha, agniraja#} und ²{#agnirU£pa#} I. 1. 

3. ×   MULTIPLICATION SIGN -> x (ascii x)  
  1 instance line 4747
4. Ñ -> N5
  134 instances (first at line 47)
-----
pwk1-7VN_ansi_5.txt Mar 15, 2022 Jim Funderburk.
Manual changes:
1. <ls>² -> ²<ls> 1646 instances. first at line 44
2. <ls>( -> (<ls> 91 instances. first at line 537.

-----
pwk1-7VN_ansi_6.txt Mar 15, 2022 Jim Funderburk.
Manual changes:
1. 67 matches in 58 lines for "<ls>[^A-Z]" in buffer: pwk1-7VN_ansi_5.txt
  Many of these have an '<ls>' erroneously within {#...#}.
2a. ' M. <ls>MÜLLER' -> ' <ls>M. MÜLLER' 23 instance (first at 6132)
2b. ' M. <ls>²MÜLLER' -> ' <ls>M. ²MÜLLER'
3a. '<ls>KULL. zu M.' -> '<ls>KULL. zu <ls>M.' 9 instance (777)
3b. '<ls>KULL. ²zu <ls>M.' -> '<ls>KULL. ²zu <ls>M.' 3 instance (5582)
4. 4 similar changes

19746 old <p>{#pra£zasti#} 5. Vgl. <ls>BÜHLER in Wiener ²Z. f. d. K. d. M. 2, 86. fgg. 

19746 new <p>{#pra£zasti#} 5. Vgl. <ls>BÜHLER in <ls>Wiener ²Z. f. d. K. d. M. 2, 86. fgg. 

20058 old <p>{#bhadramukha#} IV. Vgl. <ls>BÜHLER in Wiener ²Zeitschr. f. d. K. d. M. 2, 181. 
20058 new <p>{#bhadramukha#} IV. Vgl. <ls>BÜHLER in <ls>Wiener ²Zeitschr. f. d. K. d. M. 2, 181. 

20202 old <p>{#bhrUNa#} IV. zu diesem und den fol-²genden Compp. vgl. <ls>BÜHLER in Wie-²ner Zeitschr. f. d. K. d. M. 2, 182. fgg. ²2. {#ma#} V. 5. 
20202 new <p>{#bhrUNa#} IV. zu diesem und den fol-²genden Compp. vgl. <ls>BÜHLER in <ls>Wie-²ner Zeitschr. f. d. K. d. M. 2, 182. fgg. ²2. {#ma#} V. 5. 

21184 old <p>{#vizAkhadatta#} VI. Ueber sein Zeit-²alter s. <ls>YACOBI in Wiener Zeitschr. ²f. d. K. d. M. 2, 212. fgg. 
21184 new <p>{#vizAkhadatta#} VI. Ueber sein Zeit-²alter s. <ls>YACOBI in <ls>Wiener Zeitschr. ²f. d. K. d. M. 2, 212. fgg. 


5. YACOBI -> JACOBI (6 instances)
6. ' M. #, #' -> ' <ls>M. #, #'  (where # is a digit sequence)
    20 instances, first at line 3388
7. 4 additional misc. changes involving ' M.'
4177 old <p>{#upajJIvitar#} Nom. ag. {%lebend von%} (Gen.) <ls>ME-²DHAT. zu M. 
4177 new <p>{#upajJIvitar#} Nom. ag. {%lebend von%} (Gen.) <ls>ME-²DHA1T. zu <ls>M. 

7365 old <p>{#*dAntadeva, *dAntabhadra#} und {#*dAntasena#} m. N. pr. ver-²schiedener Männer M. <ls>MÜLIER, Ren. 311, N. 1. 
7365 new <p>{#*dAntadeva, *dAntabhadra#} und {#*dAntasena#} m. N. pr. ver-²schiedener Männer <ls>M. MÜLLER, Ren. 311, N. 1. 

12763 old <p>{#ardhika#} I. 3. Auch M. (<ls>JOLLY) 4, 253. 
12763 new <p>{#ardhika#} I. 3. Auch <ls>M. (<ls>JOLLY) 4, 253. 

16177 old <p>{#kurukSetra#} II. 2) zu streichen, da M. ²7, 193 {#kaurukSetrAn#} die richtige Lesart ²ist. 
16177 new <p>{#kurukSetra#} II. 2) zu streichen, da <ls>M. ²7, 193 {#kaurukSetrAn#} die richtige Lesart ²ist. 

8. RAYAN. -> RA1JAN. (24 instances) (first at 4050)

9. ' Verz.' -> ' <ls>Verz.' (33 instances, first at 4999)
   '²Verz.' -> '²<ls>Verz.' (2 instance, line 6372)

10. '<ls>Y. R. A. S.' -> '<ls>J. R. A. S.'  (5 instance, first 326)
  Journal Royal Asiactic Society ?

-----
pwk1-7VN_ansi_7.txt Mar 15, 2022 Jim Funderburk.
 changes involving 'R.'
1. 'R. <ls>GORR.' -> '<ls>R. GORR.'  20. First at line 954
2. ' R. ²<ls>GORR.' -> ' <ls>R. ²GORR.' (1)
3. 1 instance
19433 old <p>{#pUrdvAra#} IV. R. ed. <ls>GORR. 2, 26, 5 ({#purdvAra#} ²gedr.).
19433 new <p>{#pUrdvAra#} IV. <ls>R. ed. GORR. 2, 26, 5 ({#purdvAra#} ²gedr.).
4. ' R. #' -> ' <ls>R. #'  (# a digit sequence)
    (58 instances, first at line 98)
5. '²R. #' -> '²<ls>R. #'  (# a digit sequence)
    (10 instances, first at line 3652)
6. ' R. ed. Bomb.' -> ' <ls>R. ed. Bomb.'
    (98 instances, first at line 2340)
7. ' R. ²ed. Bomb.' -> ' <ls>R. ²ed. Bomb.'
    (14 instances, first line 1211)
8. ' R. ed. ²Bomb.' -> ' <ls>R. ed. ²Bomb.'
    (20 instances, first at line 12176)
9. ' R. ²#' -> ' <ls>R. ²#'  (# = digit)
    (5 isntances, first at line 1998)
10. 7 additional similar changes
2923 old <p>{#kAja#}, nach dem Comm. zu R. {%Korb.%} 
2923 new <p>{#kAja#}, nach dem Comm. zu <ls>R. {%Korb.%} 

3931 old <p>2. {#a£zvapRSTha#}, Anderes vermuthet R. <ls>PISCHEL in <ls>Z. d. ²d. m. G. 35, 711. fgg. Das Wort ist aber nicht auf ²den Stein, sondern auf {|Va1yu|} zu beziehen. 
3931 new <p>2. {#a£zvapRSTha#}, Anderes vermuthet <ls>R. PISCHEL in <ls>Z. d. ²d. m. G. 35, 711. fgg. Das Wort ist aber nicht auf ²den Stein, sondern auf {|Va1yu|} zu beziehen. 

3984 old <p>1. {#asma£#}, zu {#asme£#} vgl. R. <ls>PISCHEL in <ls>Z. d. d. m. G. ²35, 716. 
3984 new <p>1. {#asma£#}, zu {#asme£#} vgl. <ls>R. PISCHEL in <ls>Z. d. d. m. G. ²35, 716. 

15895 old <p>{#kAjala#} II. {%Salbe%} (?) <ls>DAS4A R. und <ls>AV. ²PADDH. zu <ls>KAUS4. 54, 6. Vgl. {#kajjala#}. 
15895 new <p>{#kAjala#} II. {%Salbe%} (?) <ls>DAS4AR. und <ls>AV. ²PADDH. zu <ls>KAUS4. 54, 6. Vgl. {#kajjala#}. 

19433 old <p>{#pUrdvAra#} IV. R. ed. <ls>GORR. 2, 26, 5 ({#purdvAra#} ²gedr.). 
19433 new <p>{#pUrdvAra#} IV. <ls>R. ed. GORR. 2, 26, 5 ({#purdvAra#} ²gedr.). 

20764 old <p>{#*rukmiNIharaNa#} n. {%der Raub der%} R., ²Titel einer Erzählung <ls>MAHA1VY. 245. 
20764 new <p>{#*rukmiNIharaNa#} n. {%der Raub der%} <ls>R., ²Titel einer Erzählung <ls>MAHA1VY. 245. 

21833 old <p>{#sAmAtyaka#} Adj. = {#sAmAtya#} 2) R. [Page7-382-d] ²ed. Bomb. 4, 60, 16. 
21833 new <p>{#sAmAtyaka#} Adj. = {#sAmAtya#} 2) <ls>R. [Page7-382-d] ²ed. Bomb. 4, 60, 16. 

-----
pwk1-7VN_ansi_8.txt Mar 15, 2022 Jim Funderburk.
 changes involving 'P.'

1. 'AGNI P.' -> 'AGNI-P.'  1
2. 1 '<ls>CA1S4. zu P.' -> <ls>KA1S4. zu P.
3. (23) '<ls>KA1S4. zu P.' ->'<ls>KA1S4. zu <ls>P.'
4. (1) '<ls>KA1S4. zu ²P.' -> '<ls>KA1S4. zu ²<ls>P.'
5. (50) ' P. #' -> ' <ls>P. #'  (# digit)
6. (4) ' P. ²#' -> ' <ls>P. ²#'  (# digit)
7. (11) '²P. #' -> ' ²<ls>P. #'  (# digit)

8. (1) 'Vartt.' -> 'Va1rtt.'
9. (4) 'HEMADRI' -> 'HEMA1DRI'
10. (2) 'MARK. P.' -> 'MA1RK. P.'
11. (1) 'SADD. P.' -> 'SADDH. P.' (print change, line 18454)

TEMPORARY :
'BHA1G. P.' -> 'BHA1G._P.'  (161)
'MA1RK. P.' -> 'MA1RK._P.' (30)
'MARK. P.' -> 'MA1RK._P.' (2)
'BHAG. P.' -> 'BHA1G._P.' (14)
'SADDH. P.' -> 'SADDH._P.' (12)
'SADD. P.' -> 'SADDH._P.' (1)  (print change)
'PR. P.' -> 'PR._P.'  (26)
------------------------
pwk1-7VN_ansi_9.txt Mar 17, 2022 Jim Funderburk.
Misc. corrections to ls names.
------------------------
pwk1-7VN_ansi_10.txt Mar 21, 2022 Thomas
2 corrections
------------------------

pwk1-7VN_ansi_11.txt Mar 21, 2022 Jim
3 corrections.  Ref step0/lsprep2/readme.txt
 step0/lsprep2/change_11.txt
------------------------
pwk1-7VN_ansi_12.txt Mar 21, 2022 Jim
programmatically add </ls> Ref step0/lsprep2/readme.txt
------------------------
pwk1-7VN_ansi_13.txt Mar 21, 2022 Jim
misc. manual changes
 step0/lsprep2/change_13.txt  303 lines changed
------------------------
pwk1-7VN_ansi_14.txt Mar 24, 2022 Jim
misc. manual changes
 step0/lsprep2/change_14.txt  44 lines changed
------------------------
pwk1-7VN_ansi_15.txt Mar 25, 2022 Jim
misc. manual changes
 step0/lsprep3/change_15.txt  600+ lines changed
------------------------
pwk1-7VN_ansi_16.txt Mar 28, 2022 Jim
misc. manual changes
 step0/wide/change_16.txt  153 lines changed
------------------------
pwk1-7VN_ansi_17.txt Apr 1, 2022 Jim
misc. manual changes related to Devanagari
 step0/slp/change_17.txt  152 lines changed
------------------------
pwk1-7VN_ansi_18.txt Apr 1, 2022 Jim
constructed by step0/slp/init_hw.py program 
 preliminary '<hw>X</hw>' markup.
 Also temporary <p n="00006" pc="1-282-a"> markup.
------------------------
pwk1-7VN_ansi_19.txt Apr 1, 2022 Jim
misc. manual changes related to <hom>, <hw> markup
 step0/slp/change_19.txt 123  lines changed
------------------------
pwk1-7VN_ansi_20.txt Apr 1, 2022 Jim
change_20.txt constructed by multi_hw.py.
Refine <hw> markup to handle multiple headwords per line.
 step0/slp/change_20.txt  2273 lines changed.
------------------------
pwk1-7VN_ansi_21.txt Apr 1, 2022 Jim
Analysis of headwords, comparing volume 7 (cumulative) with volumes 1-6.
Refine <hw> markup to handle multiple headwords per line.
 step0/meta/change_21.txt  659 lines changed.
------------------------
pwkvn_vol1_page299_ansi.txt  Apr 9, 2022 Thomas
All previous pwkvn versions were missing page 299 of volume1.
This file has the missing entries.
50 new entries (+ 18 14 18)
------------------------
pwk1-7VN_ansi_22.txt Apr 12, 2022 Jim
markup of page299, and insertion into version 22.
Refer step0/page299/readme.txt

------------------------
pwk1-7VN_ansi_23.txt Apr 14, 2022 
install German changes from Thomas
Refer step0/german1/readme.txt, and change_23.txt
 27 changes

------------------------
pwk1-7VN_ansi_24.txt Apr 14, 2022 
Add <althws>{#X#}</althws> markup
Refer step0/final/readme.txt

------------------------
pwk1-7VN_ansi_25.txt Apr 15, 2022 
Refer step0/final/readme.txt
Manual corrections (see step0/final/change_25.txt  294)

------------------------
pwk1-7VN_ansi_26.txt Apr 16, 2022 
Refer step0/final/readme.txt
Manual corrections (see step0/final/change_26.txt  52)

------------------------
pwk1-7VN_ansi_27.txt Apr 16, 2022 
Refer step0/final/readme.txt
Add <ab>X</ab> markup

------------------------
pwk1-7VN_ansi_28.txt Apr 20, 2022 
Refer step0/lsnum/readme.txt
Manual changes (step0/lsnum/changes_28.txt 127)
Also add <as1>X</as1> markup

-
------------------------

misc. observations
------------------------

pwk1-7VN_ansi.txt received from Thomas Malten Feb 22, 2022.
  Revision to accents, 

Digitization of Verbesserungen und Nachtrage for PWK dictionary,
in each of 7 volumes.

text is in cp1252 encoding.
Devanagari text coded as {#X#} where X is essentially Harvard-Kyoto transliteration.
IAST text is generally coded in AS (letter-number) form.

==========================================================
Notes 02-20-2022 discuss with Thomas
