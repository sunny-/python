import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# profit_data is data frame
data = pd.read_csv('/Users/sunny/Desktop/ML/ex1/ex1data1.txt',header = None, names = ['Population','Profits'])
vals = data.values #vals is array
plt.scatter(vals[:,0],vals[:,1])
plt.title('Graph')
plt.xlabel('Population')
plt.ylabel('Profits') 
# plt.show()




def compute_cost(x,y,theta):
	inner = np.power(((x*theta.T)-y),2)
	return np.sum(inner)/(2*len(x))

data.insert(0,'Theta0',1) #inserts 1 at the fisrt column

cols = data.shape[1] #gives number of columns
x = data.iloc[:,0:cols-1]
y = data.iloc[:,cols-1:cols]

x = np.matrix(x.values)
y = np.matrix(y.values)
theta = np.matrix(np.array([0,0]))