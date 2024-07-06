M_len = int(input())
M = set(input().split(" "))
N_len = int(input())
N = set(input().split(" "))
A = M.symmetric_difference(N)
for i in sorted(map(int,A)):
    print(i)