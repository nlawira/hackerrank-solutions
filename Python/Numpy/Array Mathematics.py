import numpy as np

N, M = map(int, input().split())

A=np.array([input().split() for _ in range(N)],int)
B=np.array([input().split() for _ in range(N)],int)

print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)
print(A**B)