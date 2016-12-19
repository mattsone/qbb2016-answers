#!/usr/bin/env python

import sys
import os
import h5py
import numpy as np
import math


np.seterr(divide='ignore')

file = h5py.File("enrichment_out.heat")
file.keys()
counts = file['0.counts'][...]
expected = file['0.expected'][...]
positions = file['0.positions'][...]
regions = file['regions'][...]

counts1 = np.ma.masked_equal(counts,0)
expected1 = np.ma.masked_equal(expected,0)

enrichments = np.log(counts1/expected1)
enrichments_unmasked = np.ma.filled(enrichments,0)

ctcf = open("/Users/cmdb/qbb2016-answers/lab_wk_7/ctcf_peaks.tsv")

ctcf_positions = []

for i, line in enumerate(ctcf):
    ctcf_line = line.rstrip( "\r\n" ).split('\t')
    if ctcf_line[0] == 'chrX':
         ctcf_positions.append(ctcf_line[1])

ctcf_index = []
ctcf_location = []
ctcf_location1 = []
for i,j in enumerate(positions):
    for pos in ctcf_positions:
        if int(pos) >= j[0] and int(pos) <= j[1]:
            ctcf_location.append(positions[i])
            ctcf_index.append(i)
            ctcf_location1.append(pos)

top = {}
for i,j in enumerate(enrichments_unmasked):
        for k,l in enumerate(j): 
            if l == max(j):
                top[i] = k

print "First Frag                   Second Frag"
for key in top.keys():
    if key in ctcf_index:
        print positions[int(key)], positions[int(top[key])]
   
    
        
        
        

             
        
        


	
