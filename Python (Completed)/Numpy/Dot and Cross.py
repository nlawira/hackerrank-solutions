import numpy as np

n =int(input())
A = np.empty((n,n), dtype=int)
B = np.empty((n,n), dtype=int)
for i in range(n):
    temp = list(map(int, input().split()))
    A[i] = temp
for i in range(n):
    temp = list(map(int, input().split()))
    B[i] = temp
C = np.empty((n,n), dtype=int)
for i in range(n):
    temp = np.empty(n, dtype=int)
    for j in range(n):
        temp[j] = np.dot(A[i], B.transpose()[j])
    C[i] = temp
print(C)
