# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

S = str(input())
k = str(input())

sol = re.finditer(r'(?=('+re.escape(k)+'))', S)
if re.search(r'(?=('+re.escape(k)+'))', S):
    for match in sol:
        print((match.start(), match.end()+len(k)-1))
else:
    print((-1, -1))