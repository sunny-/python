import numpy as np
# p = np.array([range(i,i+3)for i in [2,4,6]])
# print (p)
# print(type (p[0]))

# print ((np.zeros(10,dtype=int)))

# print ((np.ones((3,5),dtype=float)))

# print (np.full((3,5),3.14))


np.random.seed(0) # seed for reproducibility
x1 = np.random.randint(10, size = 6)
x2 = np.random.randint(10, size = (3,4))
x3 = np.random.randint(10, size = (3,4,5))

print (x3)


print("x3 ndim: ", x3.ndim)
print("x3 shape:", x3.shape)
print("x3 size: ", x3.size)

print("x3 dtype: ", x3.dtype)

print("x3 itemsize: ", x3.itemsize, "bytes")

print("nbytes: ", x3.nbytes, "bytes")



















