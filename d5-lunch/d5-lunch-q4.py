#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm


df = pd.read_csv(sys.argv[1], sep="\t")
df_bigwig = pd.read_table(sys.argv[2], header=None)

df_bigwig_fpkm = df_bigwig[5].values

df_roi_plus = df["strand"] == "+"

df_plus = df[df_roi_plus]

df_roi_minus = df["strand"] == "-"

df_minus = df[df_roi_minus]


df_fpkm = 0
df_fpkm1 = 0
df_t_name = 0
df_t_name1 = 0
chrom = ""
fpkm_list=[]


chromosome_list = ["2L","2R","3L","3R", "4" ]

for line in df_plus.itertuples():
    chrom = line[2] 
    if chrom not in chromosome_list:
        continue
    else:
        
        df_fpkm = line[12]
        df_t_name = line[6]
        fpkm_list.append(df_fpkm)
    
for line1 in df_minus.itertuples():
    chrom = line1[2]
    if chrom not in chromosome_list:
        continue
    else:
        df_fpkm1 = line1[12]
        df_t_name1 = line1[6]
        fpkm_list.append(df_fpkm1)


regression = sm.OLS(fpkm_list, df_bigwig_fpkm).fit()
print regression.summary()

























