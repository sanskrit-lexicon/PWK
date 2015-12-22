# Logic
A. grep ' ‹zu› ' ../../../../../Cologne_localcopy/pw/orig/pw.txt > commentaryrefs.txt
This command fetches all the ' ‹zu› ' occurrences from pw.txt and stores to commentaryrefs.txt
B. Run commentarystudy.py
This takes commentaryrefs.txt as input and gives the following output.
a. commleft.txt - references where the pattern matches '•Comm. ‹zu› ¯([A-Za-z0-9.,]*)'
