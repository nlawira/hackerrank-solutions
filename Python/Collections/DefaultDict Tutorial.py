# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(list)
for i in range(n):
    d[str(input())].append(str(i+1))
for _ in range(m):
    char1 = str(input())
    if char1 in d.keys():
        print(' '.join(d[char1]))
    else:
        print('-1')