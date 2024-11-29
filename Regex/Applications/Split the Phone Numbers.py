# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

N = int(input())
for _ in range(N):
    matched = re.search(r'^(\d{1,3})[\s-](\d{1,3})[\s-](\d{4,10})$', str(input()))
    print("CountryCode="+matched.group(1)+",LocalAreaCode="+matched.group(2)+",Number="+matched.group(3))