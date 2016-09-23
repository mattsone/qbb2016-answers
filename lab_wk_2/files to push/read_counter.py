#!/usr/bin/env python

import sys
import fasta


contigs = fasta.FASTAReader(open(sys.argv[1]))

sequence_length = []
contig_count = 0

for identifier, sequence in contigs:
    contig_count += 1 
    sequence_length.append(len(sequence))

n_50 = 0
total = 0
middle = 0
running_count = 0
middle = sum(sequence_length)/2
for item in reversed(sequence_length):
    total += item
    if total >= middle:
        n_50 = item
        break

print "N 50:", n_50   
print "Num of Contigs:" ,contig_count
print "Average Length:" ,(sum(sequence_length)/len(sequence_length))
print "Minimum Length:" ,min(sequence_length)
print "Maximum Length:" ,max(sequence_length)

    
    




