#!/usr/bin/env python


import sys
import fasta

#from fasta import FASTAReader



def kmer_match(target,query,k):
    
    k = int(k)
    kmer_start = {}
    seq_name = {}
    
    for ident, sequence in fasta.FASTAReader(open(target)):
        sequence = sequence.upper()
        for i in range(0,len(sequence) - k):
            kmer = sequence[i: i+k]
            if kmer not in kmer_start:
                kmer_start[kmer] = []
                seq_name[kmer] = []
            kmer_start[kmer].append(i)
            seq_name[kmer].append(ident)
    
    query_matched = {}
    query_name = {}
    for ident, sequence in fasta.FASTAReader(open(query)):
        
        sequence = sequence.upper()
        for i in range(0,len(sequence) - k):
            kmer = sequence[i: i+k]
            if kmer in query_matched:
                query_matched[kmer].append(i)
            elif kmer in kmer_start:
                query_matched[kmer] = []
                query_matched[kmer].append(i)
                query_name[kmer] = []
                query_name[kmer].append(seq_name[kmer])
            
            
            
    
    for ident in query_matched:
        print "Identifier: %s" % query_name[ident]
        print "Kmer: %s" % ident
        print "Target start: %s" % kmer_start[ident]
        print "Query start: %s" % query_matched[ident] 
    
    
kmer_match(sys.argv[1], sys.argv[2], sys.argv[3])
        