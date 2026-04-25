# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

S = str(input())
sol = re.search(r'([a-zA-Z0-9]{1})\1+', S)
if sol:
    print(sol.group(1)[0])
else:
    print('-1')