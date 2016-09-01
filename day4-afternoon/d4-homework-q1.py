#!/usr/bin/env python

"""
Usage: ./d4-homework-q1.py <metadata.csv> <ctab_dir> <replicates.csv>

Plots samples as line across developmental stages, and plots replicates as scatterplot.
"""



import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




df_meta = pd.read_csv(sys.argv[1])

ctab_dir = sys.argv[2]
df_replicates = pd.read_csv(sys.argv[3])

fem_Sxl = []
male_Sxl = []
replicates_Sxl = []
replicates_male = []
replicates_female = []
df_roi = df_meta["sex"] == "female"
dm_roi = df_meta["sex"] == "male"
rf_roi = df_replicates["sex"] == "female"
rm_roi = df_replicates["sex"] == "male"
for sample in df_meta[df_roi]["sample"]:
    filename = ctab_dir + "/" + sample + "/t_data.ctab"
    df = pd.read_table(filename)
    df_roi2 = df["t_name"]== "FBtr0331261"
    fem_Sxl.append(df[df_roi2]["FPKM"].values)
for sample in df_meta[dm_roi]["sample"]:
    filename = ctab_dir + "/" + sample + "/t_data.ctab"
    df = pd.read_table(filename)
    dm_roi2 = df["t_name"]== "FBtr0331261"
    male_Sxl.append(df[dm_roi2]["FPKM"].values)
for sample in df_replicates[rf_roi]["sample"]:
    filename = ctab_dir + "/" + sample + "/t_data.ctab"
    rf = pd.read_table(filename)
    rf_roi2 = rf["t_name"]== "FBtr0331261"
    replicates_female.append(rf[rf_roi2]["FPKM"].values)
for sample in df_replicates[rm_roi]["sample"]:
    filename = ctab_dir + "/" + sample + "/t_data.ctab"
    rf = pd.read_table(filename)
    rm_roi2 = rf["t_name"]== "FBtr0331261"
    replicates_male.append(rf[rm_roi2]["FPKM"].values)


#male_Sxl = male_Sxl[]
plt.figure()
x = [0,1,2,3,4,5,6,7]   
xlabel = ["10", "11", "12", "13", "14A", "14B", "14C", "14D"]    
plt.xticks(x, xlabel, rotation='horizontal')
plt.xlabel("Developmental Stage")
plt.ylabel("mRNA Abundance FPKM")
plt.title("Sxl - FBtr0331261")
plt.plot(fem_Sxl, 'r-',label="Female")
plt.plot(male_Sxl, label="Male")
plt.scatter([4,5,6,7], replicates_female, color='red')
plt.scatter([4,5,6,7], replicates_male, alpha=0.7)
plt.legend(loc="upper left")
#plt.show()
plt.savefig("d4-homework-q1.png")
plt.close()