# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations

inp = input()
S = sorted(list(str(inp.split()[0])))
k = int(inp.split()[1])
for i in range(1, k+1):
    for sol in combinations(S, i):
        print(''.join(sol))