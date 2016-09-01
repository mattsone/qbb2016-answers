#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt


chromosomes = ["2L", "2R", "3L", "3R", "4", "X"]
def rolling(file1,file2,window_size):

    sample1 = pd.read_table(file1)

    sample2 = pd.read_table(file2)
    
    #print sample1

    for i in chromosomes:
        
        sample1_roi = sample1["chr"] == i
        sample2_roi = sample2["chr"] == i
        
        #print sample1_roi
        
        sample1_chrom = sample1[sample1_roi]
        sample2_chrom = sample2[sample2_roi]
        
        
        
        smoothed1 = sample1_chrom["FPKM"].rolling(window_size).mean()
        smoothed2 = sample2_chrom["FPKM"].rolling(window_size).mean()
        
        #print smoothed1

        plt.figure()
        plt.plot(smoothed1, label="Sample1")
        plt.plot(smoothed2, label="Sample2")
        plt.legend(loc="upper right")
        plt.title("Chromosome %s FPKM Rolling Mean (size=%s)" % (i, window_size))

        plt.savefig("%s.png" % i)
        plt.close()


rolling(sys.argv[1], sys.argv[2], int(sys.argv[3]))


