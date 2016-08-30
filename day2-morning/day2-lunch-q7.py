#!/usr/bin/env python

import sys
total = 0
for line in sys.stdin:
    fields = line.rstrip("\r\n").split("\t")
    if line.startswith("@"):
        continue
    elif fields[2] == "2L" and (int(fields[3]) >= 10000 and int(fields[3]) <= 20000):
        total += 1
        
        

print total
