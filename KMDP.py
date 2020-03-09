"""
Created on 	: 12/10/19
Developer 	: Yeshwanth Reddy
File Type	  : Python
"""

import pandas as pd
import numpy as np
import heapq
import random
import datetime

from load_data import read_Data, read_SBS, create_Data, create_SBS
from clustering import KMeans
from clustering import MeanShift
from clustering import AffinityPropagation


from algorithms.SPGA import SPG
from algorithms.IG import IG
from algorithms.UBP import UBP
from algorithms.Apriori import Apriori


# Taking K1 as 5
k=5

# Change the fileLocation to your car.data folder.
read_data_location = "./data_process/car.csv"
read_SBS_location = "./data_process/car_SBS.csv"
dataset_location = "./dataset/car/car.data"

# Creating the Satisfaction Bit String of every customer
try:
  data = read_Data(read_data_location) 
  SBS = read_SBS(read_SBS_location)
except:
  data = create_Data(dataset_location) 
  SBS = create_SBS(dataset_location, data)



rows=len(SBS)
cols=len(SBS[0])

# Creating Sets of Customers, Candidate Products and Existing Products.
C = np.arange(0, cols)
EP = np.arange(0, (rows*30)//100)
CP = np.arange((rows*30)//100, rows)
# kCP = ?

# SPGA
timeTaken = datetime.datetime.now()
SPG_k = SPG(k, SBS, EP, CP)
timeTaken = datetime.datetime.now() - timeTaken 
print("Single Product Based Greedy Algorithm : \n", SPG_k)
print("Time taken:", timeTaken.seconds)

# IG
timeTaken = datetime.datetime.now()
IG_k = IG(k, SBS, EP, CP)
timeTaken = datetime.datetime.now() - timeTaken
print("Incremental Based Greedy Algorithm : \n", IG_k)
print("Time taken:", timeTaken.seconds)

# # UBP
# timeTaken = datetime.datetime.now()
# UBP_k = UBP(k, SBS, EP, CP)
# timeTaken = datetime.datetime.now() - timeTaken
# print("Upper Bound Pruning Algorithm : \n", UBP_k)
# print("Time taken:", timeTaken.seconds)



"""**********************************ROUGH********************"""

# # Cluster number of each datapoint
# labels = list(kmeans.labels_)
# # print(labels)

# arr = [[] for i in range(n_clusters)]
# for i,j in enumerate(labels):
#   arr[j].append(i)

# Clusters = [[] for i in range(n_clusters)]
# for i in range(n_clusters):
#   Clusters[i] = data[arr[i],:]
# # Print the no. of products each cluster contains.
# for i in range(n_clusters):
#   print("%d: %d"% (i,len(Clusters[i])), end='\n')


# # Cluster no of selected products.
# selected_products = []
# print("\nproducts selected by SPG algo")
# for i in SPG_k:
#   selected_products.append(labels[i[1]])
# print(selected_products)
# print("\nproducts selected by IG algo")
# for i in IG_k:
#   selected_products.append(labels[i])
# print(selected_products)



# Run over the cluster from which majority of the products have been selected previously.
# cluster = max(set(selected_products), key = selected_products.count)
# print(cluster)
