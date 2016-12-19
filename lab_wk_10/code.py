#!/usr/bin/env python



import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage, leaves_list 
from scipy import cluster
import scipy.cluster.hierarchy as hier
from sklearn import datasets
from sklearn.cluster import KMeans
import sklearn.metrics as sm


hema_data = pd.read_table(open("/Users/cmdb/qbb2016-answers/lab_wk_10/hema_data.txt"),   header = 0, delim_whitespace=True)

 
'''
#Linkages and dendrogram code
linkage1 = linkage(hema_data[0:6], method='average')
linkage2 = linkage(hema_data[0:], method='average')
'''
'''
#Dendrogram
plt.figure()


dendrogram(
    linkage1,
    leaf_rotation=90.,  
    leaf_font_size=8.,
    labels = (list(hema_data))  
)

plt.show()

dendrogram(
    linkage2,
    leaf_rotation=90.,  
    leaf_font_size=8.,
      
)

plt.show()
'''


#Differentially Expressed Genes Between Early and Late

early_genes = []
late_genes =[]

early_genes = (hema_data.CFU + hema_data.mys)/2
late_genes = (hema_data.poly + hema_data.unk)/2

differential = (late_genes/early_genes)

model = KMeans(n_clusters=3)
model.fit(hema_data[[1,2,3,4,5,6]])
    
significant = []

highest_diff = []
for index, gene in enumerate(differential):
    if gene > 2 or gene < .5:
        significant.append((hema_data.gene.iloc[index],differential.iloc[index]))
    if gene == max(differential):
        highest_diff.append((index,hema_data.gene.iloc[index],differential.iloc[index]))

#Getting group of genes similar to the highest differentially expressed gene based on Kmeans
print highest_diff
highest_diff_group = []
label1 = -1
for i,label in enumerate(model.labels_):
    if i == highest_diff[0][0]:
        label1 = label
        highest_diff_group.append((hema_data.gene.iloc[i],differential.iloc[i]))
    elif label == label1:
        highest_diff_group.append((hema_data.gene.iloc[i],differential.iloc[i]))
for i in highest_diff_group:
    if i[1] > 2 or i[1] < .5:
        print i[0]
        

        
'''
#Elbow method to determine number of clusters for Kmeans
elbow_method = [cluster.vq.kmeans(hema_data[[0,1]],i) for i in range(1,10)]
plt.plot([var for (cent,var) in elbow_method])

#Kmeans 
model = KMeans(n_clusters=3)
model.fit(hema_data)

#plotting Kmeans
plt.figure(figsize=(14,7))
colormap = np.array(['red', 'lime', 'black'])
plt.scatter(hema_data.CFU, hema_data.poly, c=colormap[model.labels_], s=40)
plt.title('K Means CFU vs Poly')
plt.savefig("K_Means_CFU_Poly")
plt.close()
'''














 
