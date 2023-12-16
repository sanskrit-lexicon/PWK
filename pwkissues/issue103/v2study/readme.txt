pwkissues/issue103/v2study/readme.txt

Begin 12-15-2023
Compare version v1 and v2 from Andhrabharati.
See #103 comments for these versions.
The files are named
temp_pwkvn_ab_1.txt and  temp_pwkvn_ab_2.txt

wc -l temp_pwkvn*
  90461 temp_pwkvn_ab_1.txt
  90460 temp_pwkvn_ab_2.txt

cp temp_pwkvn_ab_2.txt temp_pwkvn_ab_2a.txt

Note: Corrected 7 '</ab>act.</ab>' -> '<ab>act.</ab>'

diff temp_pwkvn_ab_1.txt temp_pwkvn_ab_2a.txt > diff_1_2a.txt
wc -l diff_1_2a.txt
138 diff_1_2a.txt

So just a small number of changes.
