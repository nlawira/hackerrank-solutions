# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

N = int(input())
for _ in range(N):
    pan = str(input())
    if re.search(r'^[A-Z]{5}\d{4}[A-Z]$', pan):
        print("YES")
    else:
        print("NO")