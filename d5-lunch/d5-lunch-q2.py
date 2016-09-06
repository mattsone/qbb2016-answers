#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(sys.argv[1], sep="\t")


df_roi_plus = df["strand"] == "+"

df_plus = df[df_roi_plus]

df_roi_minus = df["strand"] == "-"

df_minus = df[df_roi_minus]

df_start = []
df_start_minus = []
df_end = []
df_end_minus = []
df_chrom = 0
df_chrom1 = 0
df_t_name = 0
df_t_name1 = 0
chrom = ""



chromosome_list = ["2L","2R","3L","3R", "4" ]

for line in df_plus.itertuples():
    chrom = line[2] 
    if chrom not in chromosome_list:
        continue
    else:
        df_start = (line[4] - 500)
        df_end = (line[4] + 500)
        df_chrom = line[2]
        df_t_name = line[6]
        print df_chrom , "\t" , df_start, "\t" , df_end, "\t", df_t_name
    
for line1 in df_minus.itertuples():
    chrom = line1[2]
    if chrom not in chromosome_list:
        continue
    else:
        df_start_minus = (line1[5] - 500)
        df_end_minus = (line1[5] + 500)
        df_chrom1 = line1[2]
        df_t_name1 = line1[6]
        print df_chrom1 , "\t" , df_start_minus, "\t" , df_end_minus, "\t", df_t_name1












