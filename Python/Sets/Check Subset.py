T = int(input())
for _ in range(T):
    A_len = int(input())
    A = input().split(" ")
    B_len = int(input())
    B = input().split(" ")
    print(all(map(lambda x: x in B, A)))