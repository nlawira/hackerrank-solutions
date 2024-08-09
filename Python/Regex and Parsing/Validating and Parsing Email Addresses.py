# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

n = int(input())
for _ in range(n):
    name, email = map(str, input().split(' '))
    if re.search(r'^[a-zA-Z][\w.-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$', email.strip('<>')):
        print(name, email)