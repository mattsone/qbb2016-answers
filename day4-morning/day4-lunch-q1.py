#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt

df_ctab = pd.read_table(sys.argv[1])
df2_ctab = pd.read_table(sys.argv[2])

df_sxl = df_ctab["gene_name"] == "Sxl" 
df2_sxl = df2_ctab["gene_name"] == "Sxl"

df_roi = df_ctab[df_sxl]
df2_roi = df2_ctab[df2_sxl]


df_fpkm = df_roi["FPKM"] > 0
df2_fpkm = df2_roi["FPKM"] > 0


df_final = df_roi[df_fpkm]
df2_final = df2_roi[df2_fpkm]



df_plot_vals = df_final["FPKM"]
df2_plot_vals = df2_final["FPKM"]

print df_plot_vals
print df2_plot_vals
samples = ["SRR072893", "SRR072915"]

plt.figure()
plt.title("Log(FPKM) Sxl Abundance")
plt.yscale("log")
plt.ylabel("Log(FPKM)")
#plt.set_yscale('log')
plt.boxplot([df_plot_vals,df2_plot_vals], labels=samples)

plt.savefig("d4-lunch-q1.png")
