#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_table(sys.argv[1])
df2 = pd.read_table(sys.argv[2])

df_roi = df["FPKM"].values
df2_roi = df2["FPKM"].values

M_values = []
A_values = []
M_values = (np.log2(df_roi)-np.log2(df2_roi))
A_values = 0.5*(np.log2(df_roi)+np.log2(df2_roi))


plt.figure()
plt.ylabel("M")
plt.xlabel("A")
plt.title("MA Plot for SRR072893 and SRR072915 FPKM Values")
plt.scatter(A_values, M_values, alpha=0.2)
plt.savefig("d4-homework-q3.png")
plt.close



