import numpy as np
print(np.__version__)

A=[1,2,3,4,5]
B=np.array(A)

print(type(B))
print(B)
print(np.shape(B))

print(B.dtype)

C=np.array([A,A,A])
print(C)
print(np.shape(C))
print(B.dtype)
print(B.ndim)