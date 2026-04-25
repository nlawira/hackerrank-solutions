# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

T = int(input())
for _ in range(T):
    number = input()
    if re.search(r'^[+-]?\d*\.\d*$', str(number)):
        try:
            float(number)
            print("True")
        except:
            print("False")
    else:
        print("False")