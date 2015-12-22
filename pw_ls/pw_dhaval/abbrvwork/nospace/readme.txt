# Find the references in the pw.txt which are not preceded by a space or a '('.
# Requires change from '[^ ([]¯' -> '[^ ([] ¯'.
grep '[^ ([]¯' ../../../../../Cologne_localcopy/pw/orig/pw.txt > nospacebeforeref.txt

# Find the references in pw.txt which have ( or [ just preceding the ¯.
# The program generating pw.xml needs to be modified to generate `(<ls>VP.2,1,7</ls>).` instead of `(<ls>VP.2,1,7).</ls>` etc.
grep '[([]¯' ../../../../../Cologne_localcopy/pw/orig/pw.txt > bracketbeforeref.txt
