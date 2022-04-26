
Start with version 20: ../../orig/pwk1-7VN_ansi_20.txt
python ../cp1252_utf8.py ../../orig/pwk1-7VN_ansi_20.txt temp_pwkvn_20.txt


========================================================================

========================================================================

========================================================================
========================================================================
headword expansion handling º (masculine ordinal) (later to become degree)
temp_pwkvn_21.txt: manual changes to pwkvn_20.
cp temp_pwkvn_20.txt temp_pwkvn_21.txt

581 matches in 468 lines for "<hw>{#º" in buffer: temp_pwkvn_21.txt
49 <hw>{#ºyate#}</hw> -> {#ºyate#}
52 <hw>{#ºyate#}</hw> -> {#ºyate#}
10 Other verb 3s removed as hw:
hws={#anal#}, {#ºlati#} remove {#ºlati#} as hw
hws={#abhijJ#}, {#ºjJati#}
hws={#arthakAmy#}, {#ºmyati#}
hws={#caTacaT#}, {#ºTati#}
hws={#ripav#}, {#ºvati#}
hws={#kailAs#}, {#ºsati#}
hws={#kSIrod#}, {#ºdati#}
hws={#darpaN#}, {#ºNati#}
hws={#pratibimb#}, {#ºmbati#}
hws={#nadasy#}, {#ºsyate#}
------------------------------
19 cases remove 3s verb form from hws
hws={#kUD#}, {#kUDayati#}x
hws={#jyut#}, {#jyo£tati#}x
hws={#Ilay#}, {#Ila£yati#}x
hws={#aNTh#}, {#aNThati#}x
hws={#ark#}, {#arkati#}x
hws={#cuT#}, {#coTayati#}x
hws={#dAz#}, {#dA£zati#}x
hws={#din#}, {#dinati#}x
hws={#dharm#}, {#dharmati#}x
hws={#dharmay#}, {#dharmayati#}x
hws={#nArIy#}, {#yate#}x
hws={#pard#}, {#pardate#}x
hws={#bhayAy#}, {#bhayAyate#}x
hws={#gUrd#}, {#gUrdati#}x
hws={#laD#}, {#laDati#}x
hws={#aGkur#}, {#aGkurati#}x
hws={#kroJc#}, {#kroJcati#}x
hws={#poJch#}, {#poJchate#}x
hws={#lard#}, {#lardayati#}x

02915, 15853  {#ºnibandhana#} ->? {#ºNibandhana#} (HK) based on alphabetical
kalyAnibandhana -> kalyANibandhana
print change? (not made) 05-05-2022

118 matches for "<p.*?><hw>{#º" in buffer: temp_pwkvn_21.txt
No changes needed for these.

========================================================================

python meta1.py temp_pwkvn_21.txt tempwork_pwkvn.txt temp_meta1.txt
 copy temp_meta1.txt to meta1_edit.txt and manually change.
 meta1_edit.txt will serve as input to meta2.py

========================================================================
python meta2.py temp_pwkvn_21.txt meta1_edit.txt temp_pwkvn_21a.txt

skipping line <p n="01380" pc="1-295-c"> merged into prior record.
skipping line <p n="16981" pc="7-339-c">TYPO.  grahASTaka part of preceding


========================================================================
Begin analyses to uncover problems.

analyze1_problems.txt  Constructed manually
 These are the known cases where there is a volume 7 headword which
 asserts to be mentioned in volume 1-6, but in which there is no
 volume 1-6 reference found.
 
python meta2_analyze1.py temp_pwkvn_21a.txt analyze1_problems.txt temp_analyze1.txt
  658 cases written to temp_analyze1.txt initial difference
  630 cases
 These are potential errors.
 Corrections are made in temp_pwkvn_21.txt and meta1_edit.txt.

During this work, noticed that page 299 of volume 1 is missing.
 Thus, further work will be required.

$ python ../diff_to_changes.py temp_pwkvn_20.txt temp_pwkvn_21.txt change_21.txt
659 changes written to change_21.txt.

Some print differences not yet resolved:
1a <p n="01761" pc="2-285-b"><hw>{#akUrmapRSant#}
1b <p n="09459" pc="7-289-c"><hw>{#akUrmapRSat#}
2a <p n="04916" pc="4-290-c"><hw>{#aklezam#}</hw>
2b <p n="09505" pc="7-290-a"><hw>{#akleza#}</hw> I. 1. 4.
3a <p n="00117" pc="1-283-a"><hw>{#agRhyamAnakAraNa#}</hw>
3b <p n="09639" pc="7-290-d"><hw>{#agRhyamANakAraNa#
4a ?
4b <p n="09831" pc="7-291-d"><hw>{#acaladakSa#}</hw> 1.  NOT FOUND
5a <p n="03374" pc="3-248-b"><hw>{#a£dipsant#}</hw>  PROBABLE PRINT ERROR
5b <p n="10397" pc="7-295-b"><hw>{#a£ditsant#}</hw> I. 3.
6a ?
6b <p n="10459" pc="7-295-c"><hw>{#advaita#}</hw> 2. NOT FOUND
7a 
7b <p n="10503" pc="7-295-d"><hw>{#adhikaraNa#}</hw> 2. NOT FOUND
8a 
8b <p n="10520" pc="7-296-a"><hw>{#a£dhidaivatya#}</hw> I. 1. NOT FOUND
9a <p n="03535" pc="3-250-b"><hw>{#ºanivedaka#}</hw>
9b <p n="11072" pc="7-299-b"><hw>{#anivezaka#}</hw> 3.
10a <p n="02194" pc="2-289-c"> ... {#annaMbhaTTIya#}
10b <p n="11490" pc="7-301-d"><hw>{#annaMbhaTIya#}</hw> 2.
11a <p n="03776" pc="3-253-a"><hw>{#abhyAgAre#}</hw>
11b <p n="12312" pc="7-306-d"><hw>{#abhyAgAra#}</hw> I. 3. 
12a <p n="01195" pc="1-293-c"><hw>{#arocakin#}</hw> Adj.  arocakin not in vn7
12b <p n="12624" pc="7-308-d"><hw>{#arocin#}</hw> I. 1. arocin not in vn1;
; arocakin in PW, but not arocin.  Conjecture: arocin in vol7 is print error
13a <p n="01204" pc="1-293-c"><hw>{#arthakAraNAt#}</hw>
13b <p n="12660" pc="7-309-a"><hw>{#arthakAraNa#}</hw> I. 1. 
14a <p n="03869" pc="3-254-a"><hw>{#alantarAm#}<
14b <p n="12807" pc="7-310-a"><hw>{#alaMtarAm#}</hw> 3.
15a <p n="01311" pc="1-294-c"><hw>{#a£vasvadvant#}</hw>
15b <p n="13027" pc="7-311-c"><hw>{#a£vasvadant#}</hw>
16a <p n="02498" pc="2-293-a"><hw>{#asurendrA#}</hw> f.
16b <p n="13637" pc="7-315-b"><hw>{#asurendra#}</hw> I. 2.
17a <p n="01499" pc="1-296-c"><hw>{#AkumAraº#}</hw>
17b <p n="13815" pc="7-316-c"><hw>{#AkumAram#}</hw> I. 1
18a <p n="01568" pc="1-297-b"><hw>{#ApyAyinI#}</hw> f.
18b <p n="14148" pc="7-318-d"> ... und <hw>{#ApyAyin#}</hw> I. 1.
19a <p n="04077" pc="3-256-a"><hw>{#AsapuTa£#}</hw>
19b <p n="14399" pc="7-320-c"> ... <hw>{#AsanapuTa£#}</hw> 3.
20a <p n="04087" pc="3-256-b"><hw>{#indIvarAkSI#}</hw> f.
20b <p n="14493" pc="7-321-a"><hw>{#indIvarAkSa#}</hw> I. 3.
21a <p n="01635" pc="1-298-a"><hw>{#indukA#}</hw> f.
21b <p n="14494" pc="7-321-b"><hw>{#induka#}</hw>, <hw>{#ºkA#}</hw> I. 1.
22a <p n="02666" pc="2-295-a"><hw>{#ujjvalA#}</hw> f.
22b <p n="14674" pc="7-322-c"><hw>{#ujjvala#}</hw> I. 2.
23a <p n="06805" pc="5-250-a"><hw>{#utkaNThitacittI#}</hw>
23b <p n="14687" pc="7-322-c"><hw>{#utkaNThitacintI#}</hw> 5.
24a <p n="04183" pc="3-257-b"><hw>{#upanItarAga#}</hw>
24b <p n="15018" pc="7-324-d"><hw>{#upanItirAga#}</hw> 3.
25a <p n="04212" pc="3-257-c"><hw>{#ubhayAbAhu#}</hw>
25b <p n="15158" pc="7-325-d"><hw>{#ubhayAvAhu#}</hw>
26a <p n="02821" pc="2-296-c"><hw>{#evamAyuSpramANa#}</hw>
26b <p n="15459" pc="7-328-a"><hw>{#evamAyuSyapramANa#}</hw> 2.
27a <p n="02860" pc="2-297-a"><hw>{#kanakasenA#}</hw> f.
27b <p n="15651" pc="7-329-b"><hw>{#kanakasena#}</hw> II. 2. 
28a <p n="05501" pc="4-298-a"><hw>{#kuzezayalocanA#}</hw> f.
28b <p n="16214" pc="7-333-c"><hw>{#kuzezalocanA#}</hw> 4.
28c <p n="03060" pc="2-299-b"><hw>{#*kSArapattrikA#}</hw> f.
28d <p n="16525" pc="7-335-d"><hw>{#kSArapattraka#}</hw> II. 2.
29a <p n="03065" pc="2-299-b"><hw>{#kSetranirmANavidhi#}</hw> m. T
29b <p n="16553" pc="7-336-a"><hw>{#kSetranirmANanidhi#}</hw> 2.
30a <p n="04567" pc="3-261-b"><hw>{#ghanAsthika#}</hw>
30b <p n="17024" pc="7-339-d"><hw>{#ghanAsthikapha#}</hw> II. 3.
31a <p n="03141" pc="2-300-b"> ... <hw>{#caNDikAkilaka#}</hw>
31b <p n="17096" pc="7-340-b"><hw>{#caNDikA#}</hw>, <hw>{#ºkIlaka#}</hw>
32a <p n="03145" pc="2-300-b"><hw>{#caturvedatattvArthasArasaMgraha#}</hw>
32b <p n="17130" pc="7-340-c"><hw>{#caturvedatattvArthasaMgraha#}</hw>
33a <p n="03156" pc="2-300-c">... <hw>{#cayanamantrapAda#}</hw>
33b <p n="17176" pc="7-340-d"><hw>{#cayana#}</hw> ... <hw>{#ºmantrapada#}</hw>
34a <p n="08861" pc="6-301-b"><hw>{#ciJciNI#}</hw> f.
34b <p n="17255" pc="7-341-c"><hw>{#ciJcaNI#}</hw> II. 6.
35a <p n="05612" pc="4-299-b"><hw>{#jalaruhekSaNa#}
35b <p n="17465" pc="7-343-a"><hw>{#jalaruhekSaNA#}</hw> 4.
36a <p n="07342" pc="5-256-a"><hw>{#dadhighana#}</hw>
36b <p n="18005" pc="7-347-c"><hw>{#dadhigaNa#}</hw> 5.
37a <p n="09054" pc="6-303-b"><hw>{#pAMsukhelana#}</hw>
37b <p n="19212" pc="7-357-c"><hw>{#pAMsulekhana#}</hw> 6.  (probably right)
38a <p n="05901" pc="4-302-c"><hw>{#prAGmukham#}</hw> Adv.
38b <p n="19782" pc="7-362-c"><hw>{#prAGmukha#}</hw> IV. 4.
39a <p n="07854" pc="5-261-b"><hw>{#bapyanIla#}  (agrees mw)
39b <p n="19887" pc="7-363-b"><hw>{#bandhurIya#}</hw>, <hw>{#bappa#}</hw>, <hw>{#ºka#}</hw> u. <hw>{#bappanIla#}</hw> 5. 
40a <p n="09146" pc="6-304-b"><hw>{#bAlAha#}</hw>, <hw>{#vAlAha#}</hw> und <hw>{#vAlAhaka#}</hw>
40b <p n="09146" pc="6-304-b"><hw>{#bAlAha#}</hw>, <hw>{#vAlAha#}</hw> und <hw>{#vAlAhaka#}</hw>
41a <p n="08043" pc="5-263-b"><hw>{#mahAzvetA#}</hw>
41b <p n="20381" pc="7-367-c"><hw>{#mahAzveta#}</hw> V. 5.
42a <p n="09331" pc="6-306-c"><hw>{#viSka£bhe#}</hw>
42b <p n="21204" pc="7-375-d"> ...  und <hw>{#viSka£mbhe#}</hw> 6. 
43a <p n="08659" pc="6-299-a"><hw>{#urandhrA#}</hw>
43b <p n="15163" pc="7-326-a"><hw>{#uraMdhrA#}</hw> 6.
44a <p n="08111" pc="5-264-b"><hw>{#ruMS#}</hw> (vgl. <hw>{#rUS#}</hw>)
44b <p n="20763" pc="7-371-b"><hw>{#ruS#}

 {##} º> {##} <prev>{##}</prev>



print changes:
1a <p n="09747" pc="7-291-b"><hw>{#aghazaMsin#}</hw> 1. 5.
1b <p n="09747" pc="7-291-b"><hw>{#aghazaMsin#}</hw> I. 5. 
2a <p n="10663" pc="7-296-d"><hw>{#atatipAtayant#}</hw> 3.
2b <p n="10663" pc="7-296-d"><hw>{#anatipAtayant#}</hw> 3.
3a <p n="10777" pc="7-297-c"><hw>{#anabhijJAta#}</hw> 1. 3.
3b <p n="10777" pc="7-297-c"><hw>{#anabhijJAta#}</hw> 1.
4a <p n="03566" pc="3-250-c"><hw>{#anuSThAyajJayajJIya#}</hw> fehlerhaft für {#atuSThAyajJAyajJIya#}.
4b <p n="03566" pc="3-250-c"><hw>{#anuSThAyajJayajJIya#}</hw> fehlerhaft für {#anuSThAyajJAyajJIya#}.    [atu -> anu]
5a <p n="11484" pc="7-301-d"><hw>{#annadravyazUla#}</hw> 1.
5b <p n="11484" pc="7-301-d"><hw>{#annadravazUla#}</hw> 1.
6a <p n="11725" pc="7-303-b"><hw>{#apavatIya#}</hw> 3.
6b <p n="11725" pc="7-303-b"><hw>{#aparvatIya#}</hw> 3.
7a <p n="11824" pc="7-303-d"><hw>{#apuNyazIla#}</hw> 1.
7b <p n="11824" pc="7-303-d"><hw>{#apuNyazIla#}</hw> 2. 
8a <p n="11825" pc="7-303-d"><hw>{#aputryapazavya#}</hw> 2.
8b <p n="11825" pc="7-303-d"><hw>{#aputryapazavya#}</hw> 1.
9a <p n="05147" pc="4-293-c"><hw>{#aprayujyanAna#}</hw>
9b <p n="05147" pc="4-293-c"><hw>{#aprayujyamAna#}</hw>
10a <p n="12357" pc="7-307-b"><hw>{#amadhyaMdinasAci#}</hw> 5. 
10b <p n="12357" pc="7-307-b"><hw>{#amadhyaMdinasAci#}</hw> 6.
11a <p n="12663" pc="7-309-a"><hw>{#arthakilbiSin#}</hw> 1. 
11b <p n="12663" pc="7-309-a"><hw>{#arthakilbiSin#}</hw> 2.
12a <p n="06577" pc="5-247-b"><hw>{#anisaMvAda#}</hw>
12b <p n="06577" pc="5-247-b"><hw>{#avisaMvAda#}</hw>
13a <p n="02608" pc="2-294-b"> ... {#AzvalA-²yAnazrauta#}
13b <p n="02608" pc="2-294-b"> ... {#AzvalA-²yanazrauta#}
14a <p n="14520" pc="7-321-b"><hw>{#indramahAkAmuka#}</hw> I. 6.
14b <p n="14520" pc="7-321-b"><hw>{#indramahakAmuka#}</hw> I. 6. 
15a <p n="15503" pc="7-328-b"><hw>{#oSadhivanaspatimant#}</hw> 6.
15b <p n="15503" pc="7-328-b"><hw>{#oSadhivanaspativant#}</hw> 6.
16a <p n="04472" pc="3-260-b"><hw>{#krIDAparicchada#}</hw> m. {%Spielzeug.%}
16b <p n="04472" pc="3-260-b"><hw>{#krIDApariccheda#}</hw> m. {%Spielzeug.%} 
17a <p n="17931" pc="7-346-d"><hw>{#trivyAsa#}</hw> 6.
17b <p n="17931" pc="7-346-d"><hw>{#trivyAma#}</hw> 6. 
18a <p n="04897" pc="3-265-a"><hw>{#niruddhapakaza#}</hw> Z. 2, lies {#ddhaprakaza#}. [Page3-265-b]
18b <p n="04897" pc="3-265-a"><hw>{#niruddhapakaza#}</hw> Z. 2, lies {#ºddhaprakaza#}. [Page3-265-b] 
19a <p n="07656" pc="5-259-b"><hw>{#pAravalana#}</hw>
19b <p n="07656" pc="5-259-b"><hw>{#parivalana#}</hw>
20a <p n="07679" pc="5-259-b"><hw>{#paSTava£h#}</hw>
20b <p n="07679" pc="5-259-b"><hw>{#paSThava£h#}</hw>
21a <p n="07825" pc="5-261-a"><hw>{#prAcIpratIcitas#}</hw>
21b <p n="07825" pc="5-261-a"><hw>{#prAcInapratIcitas#}</hw>
22a <p n="11725" pc="7-303-b"><hw>{#apavatIya#}</hw> 3.
22b <p n="11725" pc="7-303-b"><hw>{#aparvatIya#}</hw> 3. 
23a <p n="11824" pc="7-303-d"><hw>{#apuNyazIla#}</hw> 1.
23b <p n="11824" pc="7-303-d"><hw>{#apuNyazIla#}</hw> 2
24a <p n="11825" pc="7-303-d"><hw>{#aputryapazavya#}</hw> 2.
24b <p n="11825" pc="7-303-d"><hw>{#aputryapazavya#}</hw> 1.
25a <p n="12357" pc="7-307-b"><hw>{#amadhyaMdinasAci#}</hw> 5.
25b <p n="12357" pc="7-307-b"><hw>{#amadhyaMdinasAci#}</hw> 6. 

Other:  discovered page 299 of volume 1 is missing
See step0/page299
========================================================================
Transfer version 21 to orig

transfer temp_pwkvn_21.txt to orig in cp1252 encoding
python ../utf8_cp1252.py temp_pwkvn_21.txt ../../orig/pwk1-7VN_ansi_21.txt

check invertibility
 python ../cp1252_utf8.py ../../orig/pwk1-7VN_ansi_21.txt temp.txt
 diff temp_pwkvn_21.txt temp.txt
 # no difference expected.
========================================================================
