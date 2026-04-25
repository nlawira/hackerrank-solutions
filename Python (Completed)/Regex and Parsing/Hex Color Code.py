# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

N = int(input())
for _ in range(N):
    sol = re.findall(r'#[0-9a-fA-F]{3,6}(?=[);,])', str(input()))
    if sol:
        print(*sol, sep="\n")