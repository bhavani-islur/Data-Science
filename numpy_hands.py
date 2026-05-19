# matplot lib, seaborn,pandas , nymPy
# numpy is numerical python

import numpy as np
# print(np.__version__)
# print(np.unwrap.__doc__)

# data Structures in numpy
# 1) Scalar
a=np.array(10)
print(a)

print(type(a))
# vector
rv=np.array([1,2,3,4,5])
print(rv)
# print(rv.ndm)
print(type(rv))

# matrix
matrixs=np.matrix([[1,2,3],[4,5,6]])
print(matrixs)

# creating 2d arrays in different ways
# np.ones((3,2),100)
# np.full

print(np.random.sample((3,4)))

x=np.random.seed(123)
np.random.sample((3,4))

np.random
