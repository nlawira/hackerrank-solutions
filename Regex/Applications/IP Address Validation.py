# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

N = int(input())
for _ in range(N):
    i = str(input())
    if re.search(r'^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$', i):
        print("IPv4")
    elif re.search(r'^([a-f0-9]{1,4}:){7}([a-f0-9]{1,4})$', i):
        print("IPv6")
    else:
        print("Neither")