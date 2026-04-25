# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque

T = int(input())
for _ in range(T):
    n = int(input())
    sideLengths = deque(map(int, input().split()))
    start = -1
    for i in range(n):
        if sideLengths[0] >= sideLengths[-1] and (start >= sideLengths[0] or start == -1):
            start = sideLengths[0]
            sideLengths.popleft()
        elif sideLengths[0] < sideLengths[-1] and (start >= sideLengths[-1] or start == -1):
            start = sideLengths[-1]
            sideLengths.pop()
        else:
            print("No")
            break
    if len(sideLengths) == 0:
        print("Yes")