import numpy as np

size = tuple(map(int, input().split()))
print(np.zeros(size, dtype=np.int32))
print(np.ones(size, dtype=np.int32))
