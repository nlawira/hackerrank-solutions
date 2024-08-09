# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

N = int(input())
for _ in range(N):
    S = str(input())
    if re.search(r"^[789]\d{9}$", S):
        print("YES")
    else:
        print("NO")