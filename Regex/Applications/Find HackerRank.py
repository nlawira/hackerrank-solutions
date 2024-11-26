# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

N = int(input())
for _ in range(N):
    text = str(input())
    if re.search(r'^hackerrank$', text):
        print(0)
    elif re.search(r'^hackerrank', text):
        print(1)
    elif re.search(r'hackerrank$', text):
        print(2)
    else:
       print(-1)