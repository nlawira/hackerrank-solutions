import numpy as np

N, M, P = map(int, input().split())
col1 = []
col2 = []
for _ in range(N):
    col1.append(list(map(int, input().split())))
for _ in range(M):
    col2.append(list(map(int, input().split())))
col1 = np.array(col1)
col2 = np.array(col2)
print(np.concatenate((col1, col2)))