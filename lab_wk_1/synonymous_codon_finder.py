#!/usr/bin/env python

import sys
from itertools import cycle
import fasta
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from collections import Counter

query_dna_reader = fasta.FASTAReader(open(sys.argv[1]))
matches_dna_reader = fasta.FASTAReader(open(sys.argv[2]))

synonymous_codon = []
non_synonymous_codon = []


codontable = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }


match_codon = ''
query_codon = ''
synonymous_dict = {}
non_synonymous_dict = {}
matches_dna_split = []
query_dna_split = []
for identifier, sequence in query_dna_reader:
    query_dna_split = [sequence[i:i+3] for i in range(0, len(sequence), 3)]
for identifier, sequence in matches_dna_reader:
    matches_dna_split = [sequence[i:i+3] for i in range(0, len(sequence), 3)]
for index, i in enumerate(query_dna_split):
    synonymous_dict[index] = 0
    non_synonymous_dict[index] = 0
index = 0
#for identifier, sequence in matches_dna_reader:
for (x,y) in zip(matches_dna_split, cycle(query_dna_split)):
      
    match_codon = str(x)
       
    query_codon = str(y)
    
    if match_codon not in codontable:
            continue
    if query_codon not in codontable:
            continue
    if match_codon == query_codon:
            continue
    if codontable[match_codon] == codontable[query_codon]:
        synonymous_dict[index] += 1
            #synonymous_codon.append(index)
    else:
            #non_synonymous_codon.append(index)
        non_synonymous_dict[index] += 1
    if index <= 3427:
        index += 3
    else:
        index = 0

d3 = {}
for k, v in non_synonymous_dict.items():
    d3[k] = v - synonymous_dict.get(k, 0)
    
#d_S = Counter(synonymous_dict)
#print d3

dN_dS_list = [ [v] for k, v in d3.items() ]
index_list = [[k] for k,v in d3.items()]

a = np.array(dN_dS_list)
final = stats.zscore(a)



#print final
#print index_list

plt.figure()
plt.title('Zscore for dN-dS along AA position')
plt.xlabel('Codon/AA position')
plt.ylabel('Z-Score')
plt.scatter(index_list, final)
plt.savefig('z-scores.png')


#for thing in final:
    #if thing > 3:
        #print thing


#d_N = Counter(non_synonymous_dict)

#d_N_d_S = d_N.subtract(d_S)

#print d_N_d_S 
#synonymous_dict_list = []
#synonymous_dict_list = [ [k,v] for k, v in synonymous_dict.items() ]
#non_synonymous_list = [ [k,v] for k, v in non_synonymous_dict.items() ]

#for i inz_score.append()

#print synonymous_dict_list
#print non_synonymous_dict


        
   

        
        

            
        
      



