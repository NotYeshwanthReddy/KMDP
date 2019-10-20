"""
Created on 	: 12/10/19
Developer 	: Yeshwanth Reddy
File Type	: Python
"""

#    buyingCost   v-high, high, med, low
#    maintCost    v-high, high, med, low
#    doors        2, 3, 4, 5-more
#    seats        2, 4, more
#    lug_boot     small, med, big
#    safety       low, med, high


import pandas as pd
import random
import numpy as np


def create_SBS(fileLocation = "car/car.data"):
	fileName = fileLocation.split("/")[-1].split(".")[0]
	print("Reading data...")
	data = pd.read_csv(fileLocation, header=None)
	data = np.array(data)

	print("Formatting data...")
	data[data=='5more'] = 5
	data[data=='vhigh'] = 3
	data[data=='more'] = 2
	data[data=='high'] = 2
	data[data=='big'] = 2
	data[data=='med'] = 1
	data[data=='low'] = 0
	data[data=='small'] = 0
	# Classes defining if a user BUYs or NOT.
	data[data=='unacc'] = 0
	data[data=='acc'] = 1
	data[data=='good'] = 2
	data[data=='vgood'] = 3
	
	data = np.array(data, dtype=np.int8)

	print("creating Empty SBS table...")
	no_cust = data.shape[0]//3
	SBS = np.zeros((data.shape[0], no_cust), dtype=np.int8)
	
	print("Filling SBS table...")
	for i in range(data.shape[0]):
		for j in range(SBS.shape[1]):
			if data[i][-1] == 3: 	# 90% chance
				SBS[i][j]= 0 if random.randint(0,100)%10==0 else 1
			elif data[i][-1] == 2:  # 75% chance
				SBS[i][j]= 0 if random.randint(0,100)%4==0 else 1
			elif data[i][-1] == 1:  # 50% chance
				SBS[i][j]= 0 if random.randint(0,100)%2==0 else 1
			elif data[i][-1] == 0:  # 10% chance
				SBS[i][j]= 1 if random.randint(0,100)%10==0 else 0
	
	print("Saving to file...")
	pd.DataFrame(data, dtype=np.int8).to_csv("data_process/"+fileName+".csv", header=None, index=None)
	pd.DataFrame(SBS, dtype=np.int8).to_csv("data_process/"+fileName+"_SBS.csv", header=None, index=None)


def read_SBS(fileLocation):
	SBS = pd.read_csv(fileLocation, header=None)
	return SBS


# create_SBS("car/car.data")
SBS = read_SBS("data_process/car_SBS.csv")
