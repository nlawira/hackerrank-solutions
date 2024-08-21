import numpy as np

N = int(input())
arr = np.empty((N,N), dtype = 'float')
for i in range(N):
    arr[i] = list(map(float, input().split(' ')))
print(np.round(np.linalg.det(arr), 2))
