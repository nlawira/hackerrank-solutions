# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

total = 0
N = int(input())
for _ in range(N):
    if re.search(r'hackerrank', str(input()), re.IGNORECASE):
        total += 1
    else:
        continue
print(total)