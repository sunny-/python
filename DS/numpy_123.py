import numpy as np
p = np.array([range(i,i+3)for i in [2,4,6]])
print (p)
print(type (p[0]))

print ((np.zeros(10,dtype=int)))

print ((np.ones((3,5),dtype=float)))

print (np.full((3,5),3.14))


np.random.seed(0) # seed for reproducibility
x1 = np.random.randint(10, size = 6)
x2 = np.random.randint(10, size = (3,4))
x3 = np.random.randint(10, size = (3,4,5))

print (x3)

print (x1)
x2[0,0] = 11.23

print("x3 ndim: ", x3.ndim)
print("x3 shape:", x3.shape)
print("x3 size: ", x3.size)

print("x3 dtype: ", x3.dtype)

print("x3 itemsize: ", x3.itemsize, "bytes")

print("nbytes: ", x3.nbytes, "bytes")

x2_copy = x2[:2,:3].copy()
print (x2_copy)

x2_copy[0,0] = 100

print (x2)
print (x2_copy)


x = [1, 2, 3, 99, 99, 3, 2, 1]
a1,a2,a3 = np.split(x,[2,4])
print (a1,a2,a3)

g = np.arange(16)
h = g.reshape((4,4))

print(g)

print(h)

u,l = np.vsplit(h,[2])

print(u,l)







