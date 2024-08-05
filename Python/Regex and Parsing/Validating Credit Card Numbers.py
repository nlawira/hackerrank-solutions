# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

N = int(input())
for _ in range(N):
    if re.match(r'^(?=[456])(?!.*(\d)(-?\1){3})\d{4}(-?\d{4}){3}$', str(input())):
        print("Valid")
    else:
        print("Invalid")