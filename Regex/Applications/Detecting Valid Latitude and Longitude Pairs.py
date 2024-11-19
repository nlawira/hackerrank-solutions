# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

N = int(input())
for _ in range(N):
    coor = str(input())
    if re.search(r'^\([+-]?(90(\.0+)?|[1-8]?\d(\.\d+)?), [+-]?(180(\.0+)?|(1[0-7]\d|[1-9]?\d)(\.\d+)?)\)$', coor):
        print("Valid")
    else:
        print("Invalid")