A = input().split(" ")
N = int(input())
logical = list()
for _ in range(N):
    otherSets = input().split(" ")
    if len(A) <= len(otherSets):
        logical.append(False)
    elif all(map(lambda x:x in A, otherSets)) == True:
        logical.append(True)
    else:
        logical.append(False)
print(all(logical))