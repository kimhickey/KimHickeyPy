#!C:\Python34\python.exe
# Change top line to fit your environment
#
# This script demonstrates a simple style - as though running from the interpreter
# instead of a script to be re-used on multiple occasions for different customers
# and campaigns

# '\/aff\/callback\/nyr8nx.*cid=X9KN0' can be used to find the campaign without tracking
# callbacks for customer nyr8nx

import re

f = open('elblogs.txt','r');
cbk_count=0
cmp_count=0

for line in f:
    if re.search('\/aff\/callback\/nyr8nx', line) is not None:
        cbk_count+=1
        if re.search('cid=X9KN0', line) is not None:
            cmp_count+=1
print(str(cbk_count)+" callback counts, "+str(cmp_count)+" campaign counts")



