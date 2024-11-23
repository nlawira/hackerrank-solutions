# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

emails = set()
N = int(input())
for _ in range(N):
    e_find = re.findall(r"[\w\.]+@[\w\.]+[A-Za-z]+", str(input()))
    for email in e_find:
        emails.add(email)
print(";".join(sorted(list(emails))))