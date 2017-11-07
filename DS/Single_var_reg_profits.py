import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
profit_data = pd.read_csv('/Users/sunny/Desktop/ML/ex1/ex1data1.txt',header = None, names = ['Population','Profits'])
vals = profit_data.values
plt.scatter(vals[:,0],vals[:,1])
plt.title('Graph')
plt.xlabel('Population')
plt.ylabel('Profits') 
# plt.show()
# profit_data.plot(kind='scatter', x='Population', y='Profits')
# plt.scatter('Population','Profits')
# profit_data['theta0'] = 1
# cf = np.zeros(shape = (2,1)) # Value of Xo
# iteration = 1500
# alpha = 0.01 
#