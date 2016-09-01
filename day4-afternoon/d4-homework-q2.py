#!/usr/bin/env python

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_ctab = pd.read_csv(sys.argv[1], sep="\t")



df_roi = df_ctab["FPKM"] > 0

df_above_zero = df_ctab[df_roi]
log_values = []
log_values = np.log(df_above_zero["FPKM"].values)
print log_values

plt.figure()
plt.ylabel("Frequency")
plt.xlabel("log(FPKM)")
plt.title("Histogram for log(FPKM) for SRR072893")
plt.hist(log_values)
plt.savefig("d4-homework-q2.png")
plt.close()
