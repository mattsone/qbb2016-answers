#!/usr/bin/env python

import sys
num_alignments = 0
total = 0
for line in sys.stdin:
    if line.startswith("@"):
        continue
    else:
        num_alignments += 1
        fields = line.rstrip("\r\n").split("\t")
        total += int(fields[4])

average_MAPQ = float(total) / float(num_alignments)

print average_MAPQ



        

        
