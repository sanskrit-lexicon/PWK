pwkissues/issue88101/readme.txt
bot tag analysis
Begun 11-13-2023

# this directory
cd /c/xampp/htdocs/sanskrit-lexicon/pwk/pwkissues/issue101

# issue 101 link
 https://github.com/sanskrit-lexicon/PWK/issues/101

# start with temp_pw_0.txt as copy of
  csl-orig/v02/pw/pw.txt at commit d847fe33dd4e2626ebf8869325e0bca452a5f20d
# prepare temp_pw_hk_0.txt as HK version for @maltenth:
(ref: https://github.com/sanskrit-lexicon/PWK/blob/master/pwkissues/issue95/pwtranscode/readme.txt)

---------------------------------------------------
generate a sorted list of bot tag instances with frequences
----- bot_freq_pw_0.txt
python bot_freq.py temp_pw_hk_0.txt bot_freq_pw_0.txt
8259 bot tags
1438 distinct bot tags
<bot>Acacia Catechu Willd.</bot> 1
<bot>Acacia Catechu</bot> 48
<bot>Acacia catechu</bot> 3

----- bot_freq_mw.txt
python bot_freq.py /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt bot_freq_mw.txt
9244 bot tags
1560 distinct bot tags
<bot>Acacia Catechu</bot> 45

----- bot_freq_pw_0_withmw.txt
python bot_freq_withmw.py temp_pw_hk_0.txt bot_freq_mw.txt bot_freq_pw_0_withmw.txt
8259 bot tags
1438 distinct bot tags
<bot>Acacia Catechu Willd.</bot> 1 MW 0
<bot>Acacia Catechu</bot> 48 MW 45
<bot>Acacia catechu</bot> 3 MW 0

-------------------------------------------
11-27-2023
German word corrections.
See german/readme.txt.
Final results are in change_pw_2.txt, change_pw_3.txt, and unchanged.txt
New version of pw.txt is temp_pw_3.txt
temp_pw_3_hk.txt is hk version.

-------------------------------------------
12-08-2023
German word corrections (non-italic text).
See german1/readme.txt.
Final results are in german1 directory:
 change_word_regular.txt  
 change_word_irregular.txt
 change_word_thomas.txt
New version of pw.txt is temp_pw_3c.txt

temp_pw_3c_hk.txt is hk version.
