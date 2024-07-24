# Enter your code here. Read input from STDIN. Print output to STDOUT
# Works on Pypy 3

import re

T = int(input())
for _ in range(T):
    S = input().strip()
    try:
        re.compile(S)
        print("True")
    except re.error:
        print("False")