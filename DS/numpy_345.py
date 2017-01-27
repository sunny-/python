import numpy as np
np.random.seed(0)

def comp_reci(values):
	output = np.empty(len(values))
	for i in range(len(values)):
		output[i] = 1.0/values[i]
	print (output)
	return output

values = np.random.randint(1,10,size=5)

# print(values)

comp_reci(values)
