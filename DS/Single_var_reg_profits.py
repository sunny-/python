import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
profit_data = pd.read_csv('/Users/sunny/Desktop/ML/ex1/ex1data1.txt',header = None, names = ['Population','Profits'])
vals = profit_data.values
plt.scatter(vals[:,0],vals[:,1])
plt.title('Graph')
plt.xlabel('Population')
plt.ylabel('Profits') 
plt.show()
