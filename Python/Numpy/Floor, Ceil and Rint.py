import numpy as np
np.set_printoptions(legacy='1.13')

A = list(map(float,input().split(" ")))
print(np.floor(A))
print(np.ceil(A))
print(np.rint(A))
