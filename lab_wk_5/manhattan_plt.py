#!/usr/bin/env python

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

for filename in os.listdir("/Users/cmdb/qbb2016-answers/lab_wk_5/Phenotypes"):
    if filename.endswith(".qassoc"):
        current_pheno = pd.read_table(open(os.path.join("/Users/cmdb/qbb2016-answers/lab_wk_5/Phenotypes", filename)), delim_whitespace=True) 
        man_y = -np.log10(current_pheno['P'])
        man_x = current_pheno['SNP']
        pheno = filename
        
        plt.figure()
        ax = plt.subplot()
        plt.scatter(man_x, man_y)
        threshold = 5
        ax.axhline(y=threshold, color='r', linestyle=':')
        plt.title(pheno)
        plt.xlabel("SNP")
        plt.ylabel("-log10(P-value)")
        plt.savefig(pheno+".png")
        plt.close()
    else:
        continue
        
        
        
        
        