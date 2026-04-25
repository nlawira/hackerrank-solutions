# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

N = int(input())
for _ in range(N):
    S = str(input())
    S = re.sub(r"(?<=\s)&&(?=\s)", "and", S)
    print(re.sub(r"(?<=\s)\|\|(?=\s)", "or", S))