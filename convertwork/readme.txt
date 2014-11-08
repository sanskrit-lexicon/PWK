convertwork/readme.txt for PW
Nov 7, 2014

This summarizes the conversion of pw_orig_utf8.txt to pw_orig_slp1.txt.
As described in readme.org, this is accomplished by the transcode.py program,
along with a slightly customized hk_slp1.xml transcoding file.  

This change was motivated by the need to code certain hiatuses (a-u as in
pra-uga and a-i);  in 'standard' HK, this is not possible, since the 
sequence 'au' represents the diphthong औ. While it would be possible to
develop some arbitrary non-standard HK extension to represent a hiatus,  SLP1
already has solved this problem; SLP1 uses 'O' for the diphthong औ; and
represents the hiatus a-u simply by 'au' , as in prauga = प्रउग .


As described more fully for the PWG dictionary, the conversion is conceptually
simple. Devanagari text occurs in #{X} forms in the original digitization
(pw_orig_utf8.txt), where X is provided in the Harvard-Kyoto (HK) 
transliteration.  The transcoding file hk_slp1.xml describes how to convert
an HK transliteration X to the corresponding SLP1 transliteration Y.

Theoretically, applying the inverse transcoding (specified in transcoding
file slp1_hk.xml) to Y should get X back.  Usually this is true for PW,
but there are a few places where it fails. Normally, this is due to the
occurrence of various non-Devanagari codes within X; notably, English
punctuation 'period' is represented by the '.' character; also, page breaks
often occur as part of X.   Our solution to this problem is to break up
X into parts in such a way that the non-Devanagari parts are excluded.
So, for instance 
 '#{kA ƒPage2.052-3ƒ rAgfha}' is replaced by 
 '#{kA }ƒPage2.052-3ƒ#{ rAgfha}'
In PW, there is another peculiarity that has been altered in the conversion
to SLP1.  For example, under headword anIzvara (HK), one finds in the
original digitization the form ' #{anIza^1}' which indicates that
the reference is to homonym 1 of anIza.  Now, in the SLP1 transliteration
the caret character '^' has the function of representing the svarita accent.
So, the naive conversion to SLP1 would result (under headword anISvara (SLP1),
the form ' #{anISa^1}', which would have the wrong interpretation that the
'a' has a svarita accent.  When one looks at the scan for anISvara, one 
actually sees the form '1. #{anISa}', where the homonym number precedes the
devanagari text.  Our solution to this problem in pw_orig_utf8_slp1.txt is 
the coding '^1. #{anISa}', where we have reverted to the scan form, but have
retained from pwg_orig_utf8.txt the  useful '^' preceding the homonym number 1.

One final transformation made in the construction of pwg_orig_utf8_slp1.txt 
does not directly relate to the coding of devanagari; it relates to the
ellipsis character '…'.  In the original digitization, this ellipsis character
functions serves as a 'glue' to connect related sequences of text.  It 
occurs as a replacement for the space character in groupings
#{X…Y} (Devanagari), {%X…Y%} (Italics), and ‹X…Y› (Non-italic German).
Since the braces {} or angle-braces ‹› also represent the grouping, there
is no need to use the ellipsis within these groups; so the ellipsis character
has been replace by the space character within these groups.  We think this
modest change makes the digitization easier to read.   Incidentally, there
are 700 records of the resulting digitization where the ellipsis character
still occurs; and we have, as of this writing, retained these instances of 
the ellipsis.

Incidentally, the difforig file contains the 64 lines where the
double conversion HK->SLP1->HK  (as performed by transcode.py) does NOT 
function as the identity transformation.  It would probably be a good idea
to examine pwg_orig_utf8_slp1.txt for these cases to see if some manual
adjustment is required to adequately reflect the scanned text.
