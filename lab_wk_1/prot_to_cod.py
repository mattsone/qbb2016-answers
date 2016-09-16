#!/usr/bin/env python

import sys
import fasta


blast_out = fasta.FASTAReader(open(sys.argv[1]))
mafft_out = fasta.FASTAReader(open(sys.argv[2]))

amino_acids = []
nucleotides = []

for i in mafft_out:
    amino_acids.append(i)
    
for i in blast_out:
    nucleotides.append(i)
for item in zip(nucleotides, amino_acids):    
#for item in itertools.izip(nucleotides, amino_acids):
    sequence = []
    n = 0
    nucleotide = item[0][1]
    aminoacid = item[1][1]
    
    for i in aminoacid:
        if i == "-":
            sequence.append("---")
        else:
            codon = nucleotide[n:n+3]
            n += 3
            sequence.append(codon)
        
    print ">"+item[0][0]
    print "".join(sequence)    