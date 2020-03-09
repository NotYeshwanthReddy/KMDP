


def sampling(CP,EP,data,SBS,percentage=10):
    CP_sample = np.random.choice(CP, (len(CP)*percentage)//100)
    EP_sample = np.random.choice(EP, (len(EP)*percentage)//100)
    
# Incomplete function
    return CP_sample, EP_sample

