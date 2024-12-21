change_pw_1.txt 2099
 make species field lower case.
--------------------
change_pw_2.txt  194
; case 1: (11) revert <bot n="X">Y</bot> to <bot>X</bot>
; case 2: (20) capitalize genus:
; case 3: (7) instances alternate genus names [paren]
; case 4: (167) alternate species name. Nearly all are print changes.
  Example: {%<bot>Areca faufel</bot>%} oder {%<bot>Catechu</bot>%}
           {%<bot>Areca faufel</bot>%} oder {%<bot>Areca catechu</bot>%}
--------------------
change_pw_3.txt 1554
; case 1: gs=0,0 (genus not found and species not found)
  Some 'bot' changed to 'zoo'.
; case 2: gs=0,N (genus not found but species found)
; case 3: gs=N,0 (genus found but species not found)
; case 4: auth corrections
; case 5: gs changes

These changes aim to make the bot references agree with current
botanical databases.  Primarily, this uses data from
https://powo.science.kew.org/
-----
Royal Botanic Gardens KEW | Plants of the World Online

Govaerts R (ed.). 2023. WCVP:
World Checklist of Vascular Plants.
Facilitated by the Royal Botanic Gardens, Kew.
[WWW document] URL https://doi.org/10.34885/jdh2-dr22 [accessed 28 September 2023].

Download of DATA: wcvp.zip
https://sftp.kew.org/pub/data-repositories/WCVP/
