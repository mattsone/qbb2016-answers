#!/usr/bin/env python

"""
For each matched kmer, extend on either end to find longest exact match.
For each target sequence, print matches from longest to shortest.

Usage: kmer_matcher.py <target.fa> <query.fa> <k>
"""

import sys
import fasta

## from fasta import FASTAReader

def kmer_match(target, query, k):
    k = int(k)
    kmer_start = {}
    seq_name = {}
    sequences = {}

    for identifier, sequence in fasta.FASTAReader(target):
        sequences[identifier] = sequence
        sequence = sequence.upper()
        for i in range(0,len(sequence) - k):
            kmer = sequence[i:i+k]
            if kmer not in kmer_start:
                kmer_start[kmer]= []
                seq_name[kmer] = []
            kmer_start[kmer].append(i)
            seq_name[kmer].append(identifier)
    
    # for kmer, count in kmer_counts.iteritems():
    #     print kmer, count
    
    query_match = {}
    query_name = {}
    count = 0
    sequence1 = None
    
    for identifier, sequence1 in fasta.FASTAReader(query):
        sequence1 = sequence1.upper()
        for i in range(0,len(sequence1) - k):
            kmer = sequence1[i:i+k]
            if kmer in query_match:
                query_match[kmer].append(i)
            elif kmer in kmer_start:
                query_match[kmer]=[]
                query_match[kmer].append(i)
                query_name[kmer]=[]
                query_name[kmer].append(seq_name[kmer])
            count += 1
    
    num1 = 0
    num2 = 0
    beginning = 0
    end = 0
    final_sequences = []
    final_sequences_sorted = []


    for kmer in query_match.keys():
        l1 = query_match[kmer]
        l2 = kmer_start[kmer]
        for j,pos_target in enumerate(l2):
            identifier = seq_name[kmer][j]
            sequence = sequences[identifier]
            for pos_query in l1:
                num1, num2 = 0, 0
                # if sequence[pos_target:pos_target+k] == sequence1[pos_query:pos_query+k]
                while sequence[pos_target - num1] == sequence1[pos_query - num1]:
                    num1 += 1
                    beginning = pos_query - num1
                    beginning2 = pos_target - num1
                    if beginning == 0 or beginning2 == 0:
                        break
                while sequence[pos_target + num2] == sequence1[pos_query + num2]:
                    num2 += 1
                    end = pos_query + num2
                    end2 = pos_target + num2
                    if end == len(sequence1) or end2 == len(sequence):
                        break
                if (end - beginning) > 11 :        
                	final_sequences.append(sequence1[beginning:end])
                #if len(final_sequences) == 1000:
    #print len(final_sequences)
    return sorted(final_sequences, key=len, reverse=True)

    

    
print "\n".join(kmer_match(open(sys.argv[1]),open(sys.argv[2]),sys.argv[3])[:1000])


    
    
    