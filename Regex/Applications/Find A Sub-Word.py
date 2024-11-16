# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

n = int(input())
sen = []
for _ in range(n):
    sen.append(str(input()))
q = int(input())
for _ in range(q):
    total = 0
    s = str(input())
    pattern = r"(?<=\w)" + s + r"(?=\w)"
    for i in sen:
        sol = re.findall(pattern, i)
        total += len(sol)
    print(total)