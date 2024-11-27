# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

n = int(input())
for _ in range(n):
    s = str(input())
    sol = re.search(r'^[hH][iI]\s[^dD]', s)
    if sol:
        print(s)