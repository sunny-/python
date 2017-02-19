import numpy as np

import pandas as pd 

import matplotlib.pyplot as plt

import seaborn

# np.random.seed(0)

# def comp_reci(values):
# 	output = np.empty(len(values))
# 	for i in range(len(values)):
# 		output[i] = 1.0/values[i]
# 	print (output)
# 	return output

# values = np.random.randint(1,10,size=5)

# # print(values)

# comp_reci(values)

# print (1.0/values)

# a = np.arange(5)/np.arange(1,6)

# print (a)

# x = np.arange(9).reshape((3,3))
# p = 2**x

# print(p)
# y = np.arange(9)
# q= y+2
# print(q)

# x = np.array([-2,-1,0,1,2])
# print (abs(x))

# y = np.array([3-4j,4-3j])
# print (abs(y))

# th = np.linspace(0,np.pi,3)

# print("theta =", th)
# print("sin(theta) =",np.sin(th))

# p = [1,2,3]
# print("p =", p)
# print("e^p =", np.exp(p))

# from scipy import special

# x = [1,5,10]
# print("gamma(x) =", special.gamma(x))

# x = np.arange(5)
# y = np.empty(5)
# np.multiply(x,10,out=y)
# print(x)
# print(y)


# y = np.zeros(10)
# np.power(2,x,out=y[::2])

# print(y)


# x = np.arange(1,6)
# print(np.add.reduce(x))

# print(np.multiply.reduce(x))

# print(np.add.accumulate(x))

# print(np.multiply.accumulate(x))


# x = np.arange(1,6)
# print(np.multiply.outer(x,x))


# L = np.random.random(100)

# print(sum(L))
# %timeit sum(L)

# print (np.sum(L))
# %timeit np.sum(L)

# data = pd.read_csv('president_heights.csv')
# heights = np.array(data['height(cm)'])
# print("Mean of President heights :", np.mean(heights))
# print("Min of President heights :", np.min(heights))
# print("Standard Deviation of President heights  :", np.std(heights))
# print("25th percentile of President heights :", np.percentile(heights,25))

# plt.hist(heights)
# plt.show()
# plt.title('president_heights')

rainfall = pd.read_csv('Seattle2014.csv')['PRCP'].values
inches = rainfall/254
inches.shape
plt.hist(inches,40)
plt.show()

np.sum((inches>0.5)& (inches<1))

print("Number days without rain: ", np.sum(inches == 0))
print("Number days with rain: ", np.sum(inches != 0))
print("Days with more than 0.5 inches:", np.sum(inches > 0.5))
print("Rainy days with < 0.1 inches :", np.sum((inches > 0) &
(inches < 0.2)))

# construct a mask of all rainy days
rainy = (inches > 0)
# construct a mask of all summer days (June 21st is the 172nd day)
summer = (np.arange(365) - 172 < 90) & (np.arange(365) - 172 > 0)
print("Median precip on rainy days in 2014 (inches): ",
np.median(inches[rainy]))
print("Median precip on summer days in 2014 (inches): ",
np.median(inches[summer]))
print("Maximum precip on summer days in 2014 (inches): ",
np.max(inches[summer]))
print("Median precip on non-summer rainy days (inches):",
np.median(inches[rainy & ~summer]))

# 







