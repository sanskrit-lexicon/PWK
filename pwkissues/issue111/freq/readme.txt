---------------------------------------------------
generate a sorted list of bot tag instances with frequences

python bot_freq.py ../temp_pw_0.txt bot_freq_pw_0.txt
8291 bot tags
1387 distinct bot tags
1387 written to bot_freq_pw_0.txt

python bot_freq.py ../temp_mw_0.txt bot_freq_mw_0.txt
8922 bot tags
1558 distinct bot tags
1558 written to bot_freq_mw_0.txt

# also show the pw bot tags with corresponding counts of mw.
python bot_freq_withmw.py ../temp_pw_0.txt bot_freq_mw_0.txt bot_freq_pw_0_withmw_0.txt
8291 bot tags
1387 distinct bot tags
1387 written to bot_freq_pw_0_withmw_0.txt

