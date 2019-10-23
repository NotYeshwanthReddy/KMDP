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
import numpy as np
import heapq


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
	return SBS

def read_SBS(fileLocation):
	SBS = pd.read_csv(fileLocation, header=None)
	return SBS



def N_Calc():
	Nsbs = [[0]*2]*w
	for i in range(w):
		EP_count=0
		CP_count=0
		for j in range(0, (h*30)//100):
			if SBS[j][i]==1:
				EP_count+=1
		for j in range((h*30)//100, h):
			if SBS[j][i]==1:
				CP_count+=1
		Nsbs[0][i] = EP_count
		Nsbs[1][i] = CP_count
	return Nsbs

def N(cust):
	EP_count = Nsbs[0][cust]
	CP_count = Nsbs[1][cust]
	return EP_count+CP_count

def P(cp_i, c_j):
	P=0
	if SBS[cp_i, c_j]==1:
		P = 1 / N[EP, CP, c_j]
	else:
		pass
	return P

def E(kCP, C):
	E = 0
	for cp_i in kCP:
		for c_j in C:
			E += P(cp_i, c_j)
	return E

def Espga(S, C):
	E = 0
	for cj in C:
		E+=P(S, cj)
	return E

def SPGA(k):
	k = [0]*k
	heapq.heapify(k)
	Nsbs = N_Calc()
	for cp in CP:
		S = cp
		E = Espga(S, C)
		heapq.heappush(k, E)
		heapq.heappop(k)
	return k


try:
	SBS = read_SBS("data_process/car_SBS.csv")
except:
	SBS = create_SBS("car/car.data")
SBS = np.array(SBS, dtype=np.uint8)
np.random.shuffle(SBS)

h=len(SBS)
w=len(SBS[0])

C = np.arange(0, w)
EP = np.arange(0, (h*30)//100)
CP = np.arange((h*30)//100, h)
# kCP = ?

k = SPGA(5)
print(k)