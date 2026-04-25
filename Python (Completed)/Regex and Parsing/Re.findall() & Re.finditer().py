# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

S = str(input())
sol = re.findall(r'(?![^AEIOUaeiou])[AEIOUaeiou]{2,}(?=[^AEIOUaeiou])', S)
if sol:
    [print(x) for x in sol]
else:
    print('-1')