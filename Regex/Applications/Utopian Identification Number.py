# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

N = int(input())
for _ in range(N):
    new_id = str(input())
    if re.search(r'^[a-z]{,3}\d{2,8}[A-Z]{3,}$', new_id):
        print("VALID")
    else:
        print("INVALID")