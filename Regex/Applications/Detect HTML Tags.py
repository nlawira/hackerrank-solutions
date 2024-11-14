# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

sol = []
N = int(input())
for i in range(N):
    s = re.findall(r'<(\w+)>?', input())
    for j in s:
        if j not in sol:
            sol.append(j)
print(';'.join(sorted(sol)))
