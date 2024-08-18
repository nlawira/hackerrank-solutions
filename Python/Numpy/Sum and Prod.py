import numpy as np
n, m= map(int, input().split())
arr = np.empty((n, m), dtype=int)
for i in range(n):
    arr[i] =list(map(int, input().split()))
print(np.prod(np.sum(arr, axis=0)))
