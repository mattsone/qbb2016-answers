#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats 
from numpy import linspace,hstack
from scipy.stats.kde import gaussian_kde

df_ctab = pd.read_csv(sys.argv[1], sep="\t")



df_roi = df_ctab["FPKM"] > 0

df_above_zero = df_ctab[df_roi]
log_values = []
log_values = np.log(df_above_zero["FPKM"].values)


gaussian = gaussian_kde(log_values)



x = linspace(-8,10,100)
plt.figure()
plt.xlabel("Log(FPKM)")
plt.ylabel("Kernel Density")
plt.title("Kernel Density Estimation and Histogram of Log(FPKM) from SRR072893)")
plt.hist(log_values, normed=1, alpha=.2)
plt.plot(x,gaussian(x), 'r', label="Kernel Density")
plt.legend(loc="upper left")

plt.savefig("d4-homework-q4.png")
plt.close()
