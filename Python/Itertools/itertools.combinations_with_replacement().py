# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations_with_replacement

inp = input()
S = sorted(list(str(inp.split()[0])))
k = int(inp.split()[1])
for i in list(combinations_with_replacement(S, k)):
    print(''.join(i))
