import numpy

N, M= map(int, input().split())
arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

arr = numpy.array(arr)

print(numpy.transpose(arr))
print(arr.flatten())