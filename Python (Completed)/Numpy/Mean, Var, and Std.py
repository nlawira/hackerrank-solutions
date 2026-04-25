import numpy as np

n, m = map(int,input().split())
arr = np.empty((n, m), dtype=int)
for i in range(n):
    m_list = list(map(int, input().split()))
    arr[i] = m_list
print(np.mean(arr, axis=1))
print(np.var(arr, axis=0))
print(np.round(np.std(arr, axis=None), 11))
