#!/usr/bin/env python

import sys
count = 0
for line in sys.stdin:
    if line.startswith("@"):
        continue 
    fields = line.rstrip("\r\n").split("\t")
    if count < 10:
        count += 1
        print fields[2]
    
   