# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

n = int(input())
for _ in range(n):
    i = str(input())
    if re.search(r'^[_.]\d+[a-zA-Z]*_?$', i):
        print("VALID")
    else:
        print("INVALID")